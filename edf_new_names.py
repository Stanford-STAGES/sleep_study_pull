"""
@author: Gauri Ganjoo
@date: 2025-Nov-28
@description: This script performs creates new file names for edfs based on information in their headers
"""

import pandas as pd
from pathlib import Path
import pyedflib
import mne
import re, datetime
import numpy as np
from charset_normalizer import from_bytes as fm
import os

def decode_str(b):
    return str(fm(b).best()).strip()

def read_header_edf(edf_filename):
    """
    Reference: https://github.com/akaraspt/deepsleepnet/blob/master/dhedfreader.py
    """
    with open(edf_filename, "rb") as f:
        h = {}
        assert f.tell() == 0  # check file position
        assert f.read(8) == b'0       '

        # recording info
        h['local_subject_id'] = decode_str(f.read(80))
        h['local_recording_id'] = decode_str(f.read(80))

        # # parse timestamp
        (day, month, year) = [int(x) for x in re.findall('(\d+)', str(f.read(8)))] 
        (hour, minute, sec)= [int(x) for x in re.findall('(\d+)', str(f.read(8)))]
        h['date_time'] = str(datetime.datetime(year + 2000, month, day, hour, minute, sec))
        # h['date_time'] = str(datetime.datetime(year + 2000, month, day))

        # misc
        header_nbytes = int(f.read(8))
        subtype = f.read(44)[:5]
        h['EDF+'] = 1 if subtype in ['EDF+C', 'EDF+D'] else 0
        h['contiguous'] = subtype != 'EDF+D'
        h['n_records'] = int(f.read(8))
        h['record_length'] = float(f.read(8))  # in seconds
        nchannels = h['n_channels'] = int(f.read(4))

        # read channel info
        channels = list(range(h['n_channels']))
        h['channels'] = [decode_str(f.read(16)) for n in channels]
        h['transducer_type'] = [decode_str(f.read(80)) for n in channels]
        h['units'] = [decode_str(f.read(8)) for n in channels]
        h['physical_min'] = np.asarray([float(f.read(8)) for n in channels])
        h['physical_max'] = np.asarray([float(f.read(8)) for n in channels])
        h['digital_min'] = np.asarray([float(f.read(8)) for n in channels])
        h['digital_max'] = np.asarray([float(f.read(8)) for n in channels])
        h['prefiltering'] = [decode_str(f.read(80)) for n in channels]
        h['n_samples_per_record'] = [int(f.read(8)) for n in channels]
        f.read(32 * nchannels)  # reserved

        # Extract additional information
        mrn = h['local_subject_id'].split(' ')[0]
        name = h['local_subject_id'].split(' ')[3]
        startdate = h['local_recording_id'].split(' ')[1]

        assert f.tell() == header_nbytes
        return [h['local_subject_id'], h['local_recording_id'], h['date_time'],h['record_length']*h['n_records']/3600] 

def read_raw_edf(edf_filename):
    f = mne.io.read_raw_edf(edf_filename)
    return f

def makefilepath(file,year):
    return '/Users/{sunnet_id}/Library/CloudStorage/Box-Box/rest of path to files that will be renamed/'+str(year)+'/'+file



# Path to the CSV file with list of edfs you want to rename
csv_file_path = 'find_info.csv'

# # Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)
df_list = list(df['Filename'])

# Get unique values from the 'path' column, excluding any NaN values
unique_paths = list(df['Filename'].dropna().unique())
new_names = []
year = input("Please enter the year (e.g., 2016): ")
info = {}

for index in range(len(unique_paths)):x
    print(unique_paths[index])
    edf_path = makefilepath(unique_paths[index], year)
    # print(read_header_edf(edf_path))
    header_list = read_header_edf(edf_path)[1].split(' ')
    date_string = [s for s in header_list if '-' in s][0]
    date_format = '%d-%b-%Y'
    date_object = datetime.datetime.strptime(date_string, date_format)
    european_date = str(date_object.day)+'-'+str(date_object.month)+'-'+str(date_object.year)
    # print(european_date)
    formatted_date = '-'.join([item.zfill(2) for item in european_date.split("-")])
    # print(formatted_date)
    new_names.append(unique_paths[index].split('(')[0]+formatted_date+'.edf')
pd.DataFrame({'original_name':unique_paths, 'new_name':new_names }).to_csv('renaming.csv', index = False)





