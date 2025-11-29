"""
@author: Gauri Ganjoo
@date: 2025-Nov-28
@description: This script performs renames files on box.
"""

import os
import pandas as pd

year = year = input("Please enter the year (e.g., 2016): ")
box_path = '/Users/{sunnet_id}/Library/CloudStorage/Box-Box/rest of path to files that will be renamed/'+year+'/'

df = pd.read_csv("renamingnow.csv")


for index, row in df.iterrows():
	try:
		os.rename(box_path+df.iloc[index,0], box_path+df.iloc[index,1])
		print(str(df.iloc[index,0]), 'renamed to', str(df.iloc[index,1]))
	except FileNotFoundError:
		print(box_path+df.iloc[index,0], 'not found')


# import os
# import pandas as pd

# year = input("Please enter the year (e.g., 2016): ")
# box_path = '/Users/gganjoo/Library/CloudStorage/Box-Box/mignot-sleep-DATA/BIDMC_transfer/Domino_EDFs(2015-present)/'+year+'/'
# # box_path = '/Users/gganjoo/Downloads/2023_staging'

# # Load the CSV file containing the renaming information
# df = pd.read_csv("renamingnow.csv")

# for index, row in df.iterrows():
#     old_name = os.path.join(box_path, df.iloc[index, 0])
#     new_name = os.path.join(box_path, df.iloc[index, 1])
    
#     try:
#         # Rename the directory
#         os.rename(old_name, new_name)
#         print(f"{old_name} renamed to {new_name}")
#     except FileNotFoundError:
#         print(f"{old_name} not found")
#     except OSError as e:
#         print(f"Error renaming {old_name} to {new_name}: {e}")







