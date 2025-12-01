"""
@author: Gauri Ganjoo
@date: 2025-Dec-01
@description: This script takes the names saved by the event_export.bat file and guesses the current names. 
"""


import csv
import pandas as pd
import os

df = pd.read_csv('processed_subdirectories.csv', encoding = 'ascii')
print(df.columns)

# Function to extract the required columns
def extract_columns(df):
    # Initialize lists to hold the new column values
    staging_names = []
    redone_names = []
    already_staged_names = []

    for log in df['Processing Log ']:
        # Split the log into parts
        parts = log.split('\\')
        
        # Extract the relevant parts
        if len(parts) >= 6:
            # Extract the last part for the file name
            file_name = os.path.basename(log)
            # Extract the year and patient name from the path
            year = parts[5]
            patient_name = ' '.join(parts[6:-1]).strip()
            patient_name_redone = parts[6]

           
            # Construct the new column values
            staging_name = os.path.join('staging_data', year, file_name.replace('.dt2', '').replace('.dt3', '').replace('\\',"/")).replace("Z:/Research/Gauri/",'')
            redone_name = os.path.join('redone_psgs', 'ResearchClosed', year, patient_name_redone)
            already_staged_name = os.path.join('redone_psgs', f'{year}_already_staged', patient_name)

            # Append to the lists
            staging_names.append(staging_name)
            redone_names.append(redone_name)
            already_staged_names.append(already_staged_name)
        else:
            # Handle cases where the log format is unexpected
            staging_names.append(None)
            redone_names.append(None)
            already_staged_names.append(None)

    # Add the new columns to the DataFrame
    df['staging_name'] = staging_names
    df['redone_name'] = redone_names
    df['already_staged_name'] = already_staged_names

    df['redone_name'] = df['redone_name'].str.replace(' 1$', '', regex=True)
    df['already_staged_name'] = df['already_staged_name'].str.replace(' 1$', '', regex=True)
    df['staging_name'] = df['staging_name'].str.replace('.dtx','',regex=True)
    return df

# Apply the function to extract columns
result_df = extract_columns(df)

# Display the result
# print(result_df)

result_df.to_csv('processed_subdirectories2.csv', index = False)



