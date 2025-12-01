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

