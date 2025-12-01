"""
@author: Gauri Ganjoo
@date: 2025-Dec-01
@description: Moves directories based on paths and names generated using prep_processed_log.py. 
"""

import os
import shutil
import pandas as pd

# Load the CSV file into a DataFrame
csv_file_path = 'processed_subdirectories2.csv'  # Update this with the path to your CSV file
df = pd.read_csv(csv_file_path)

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    staging_name = row['staging_name']
    redone_name = row['redone_name']
    already_staged_name = row['already_staged_name']
    
    # Check if staging_name exists
    if os.path.exists(staging_name):
        print(f"Staging name exists: {staging_name}")
        
        # Check if redone_name exists
        if os.path.exists(redone_name):
            print(f"Redone name exists: {redone_name}")
            
            # Move the directory from redone_name to already_staged_name
            try:
                shutil.move(redone_name, already_staged_name)
                print(f"Moved {redone_name} to {already_staged_name}")
            except Exception as e:
                print(f"Error moving {redone_name} to {already_staged_name}: {e}")
        else:
            print(f"Redone name does not exist: {redone_name}")
    else:
        print(f"Staging name does not exist: {staging_name}")
