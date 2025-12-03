"""
@author: Gauri Ganjoo
@date: 2025
@description:
- Reads CSVs from STARR flowsheets.csv and patientCodebook.csv
- Extracts Epworth Sleepiness Scale (ESS) data for pediatric and adult cohorts
- Fills in missing ESS questions with 0, and computes missing TOTAL SCORE rows
- Produces a final CSV with columns ['MRN', 'Date', 'Template', 'Measure', 'Value', 'Comment']
"""

import pandas as pd

# Load flowsheet data and keep only relevant columns
df = pd.read_csv("flowsheets.csv")[['patient_id', 'date', 'template', 'measure', 'value', 'comment']]

# Filter to keep only Epworth Sleepiness Scale entries (case-insensitive)
df = df[df['template'].str.contains("Epworth Sleepiness Scale", case=False, na=False)]

# Normalize the 'measure' field to uppercase for consistent matching
df['measure'] = df['measure'].apply(lambda x: x.upper())

# Persist an initial copy for inspection (optional)
df.to_csv("checkme.csv", index=False)



def fill_missing_ess_rows(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fill missing ESS-related rows for each (patient_id, date) group.

    For each unique patient_id/date combination, ensures that all expected ESS
    measures are present. If any measures are missing, adds a new row with
    value = 0 and comment = None.

    It also ensures that a TOTAL SCORE row exists for that (patient_id, date) group
    and computes its value as the sum of the individual ESS measures.

    Args:
        df (pd.DataFrame): Input DataFrame with columns:
                           ['patient_id', 'date', 'template', 'measure', 'value', 'comment']

    Returns:
        pd.DataFrame: DataFrame with missing ESS rows added.
    """

    # Define the expected measures for adult and pediatric ESS
    ess_measures = [
        "1. SITTING AND READING",
        "2. WATCHING TV",
        "3. SITTING INACTIVE IN A PUBLIC PLACE",
        "4. AS A PASSENGER IN A CAR FOR AN HOUR WITHOUT A BREAK ",
        "5. LYING DOWN TO REST IN THE AFTERNOON WHEN CIRCUMSTANCES PERMIT",
        "6. SITTING AND TALKING TO SOMEONE",
        "7. SITTING QUIETLY AFTER A LUNCH WITHOUT ALCOHOL",
        "8. IN A CAR, WHILE STOPPED FOR A FEW MINUTES IN TRAFFIC",
        "ESS TOTAL SCORE"
    ]

    pediatric_ess_measures = [
        "LYING DOWN TO REST OR NAP IN THE AFTERNOON",
        "SITTING AND EATING A MEAL",
        "SITTING AND READING",
        "SITTING AND READING IN A CAR OR BUS FOR ABOUT HALF AN HOUR",
        "SITTING AND TALKING TO SOMEONE",
        "SITTING AND WATCHING TV OR A VIDEO",
        "SITTING QUIETLY BY YOURSELF AFTER LUNCH",
        "TOTAL SCORE"
    ]

    new_rows = []

    # Iterate through each unique (patient_id, date) group
    for (patient_id, date), group_df in df.groupby(['patient_id', 'date']):
        template = group_df['template'].iloc[0]

        if template == "Epworth Sleepiness Scale":
            expected_measures = ess_measures
            total_score_measure = "ESS TOTAL SCORE"
        elif template == "Pediatric Epworth Sleepiness Scale":
            expected_measures = pediatric_ess_measures
            total_score_measure = "TOTAL SCORE"
        else:
            continue  # Skip if the template is not recognized

        existing_measures = group_df['measure'].tolist()
        missing_measures = set(expected_measures) - set(existing_measures)

        # Add rows for missing measures (excluding the total score)
        for measure in missing_measures:
            if measure != total_score_measure:
                new_rows.append({
                    'patient_id': patient_id,
                    'date': date,
                    'template': template,
                    'measure': measure,
                    'value': 0,
                    'comment': None
                })

        # Calculate and add the total score if missing
        if (total_score_measure not in existing_measures) or (total_score_measure in missing_measures):
            # Calculate total score from existing rows
            total_score = group_df[group_df['measure'].isin(expected_measures[:len(expected_measures) - 1])]['value'].sum()

            # Add values from newly added rows to the total score
            for row in new_rows:
                if (row['patient_id'] == patient_id) and (row['date'] == date) and (row['measure'] in expected_measures[:len(expected_measures) - 1]):
                    total_score += row['value']

            new_rows.append({
                'patient_id': patient_id,
                'date': date,
                'template': template,
                'measure': total_score_measure,
                'value': total_score,
                'comment': None
            })

    # Append the newly created rows to the original DataFrame
    df = pd.concat([df, pd.DataFrame(new_rows)], ignore_index=True)

    return df

# Ensure 'date' is in datetime format (helps downstream processing)
df['date'] = pd.to_datetime(df['date'])

# Fill missing ESS rows
df = fill_missing_ess_rows(df)

# Load patient codebook and merge to obtain MRN (or equivalent)
patient_codebook = pd.read_csv('patientCodebook.csv', dtype=str).drop("name", axis=1)
df = df.merge(patient_codebook, how="left", left_on='patient_id', right_on='patient_id').drop('patient_id', axis=1)

# Create the final table with the required column names
final_table = pd.DataFrame()

final_table[['MRN', "Date", 'Template', 'Measure','Value', 'Comment']] = df[['mrn', 'date', 'template', 'measure', 'value', 'comment']]

# Save the final output
final_table.to_csv("filled_in.csv", index=False)




