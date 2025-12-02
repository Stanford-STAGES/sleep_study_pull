Code used for exporting sleep studies from Domino and how to save them for lab use.
# Zdrive Scripts

## copying_without_vids.bat
Edit the source and destination directory before running. Make the destination directory somewhere in the research folder on the Zdrive.

## event_export.bat
Before running this script, you need to open Domino on the computer you will run this script on and export the event files of a sleep study, with all annotations selected, to the loacation you want to save all the other event files.
This will save the location and format you want to export the event files. Once you have done that, you can close Domino and prepare to run the script. You will need to download nirmd and keep it in the same location as the event_export.bat file.
You want run this script on the files you created that have no videos attached. This script will create a file called "processed_subdirectories.log". Save it as "processed_subdirectories.csv"

## prep_processed_log.py, move_folders.py
Run prep_processed_log.py to generate a file called "processed_subdirectories2.csv". Then run move_folders.py. It will move some of the directories around based on the locations and file names guessed in "processed_subdirectories2.csv". The purpose is to move some of the sleep studies out of your measurement folder(see event_export.bat) before rerunning event_export.bat because it is not a recursive script and will start over each time you run it. After you have moved the folders from your measurement folder, rerun event_export.bat. 

Repeat until all the event folders have been exported. You will need to keep a close eye out for any issues that may occur. 
Once all event folder have been made, use filezilla to transfer them to Stanford Medicine box. After they are on Stanford Medicine box, You will need to rename the edfs and some of the event folders.

# Box_Drive_scripts
These scripts should be run on a computer with box drive. Also watch the storage capacity if running on a PC. 
## edf_new_names.py
Before running, create a file "find_info.csv" with a column "Filename" that lists the edfs you want to rename. Note that they must all be in the same "year" folder on box. When you run this script, it will ask you for the year you are pulling from on box. The script will create a file called 'renaming.csv' with two columns [original_name, new_name]. 

Open renaming.csv and check if any of the new names are duplicates of each other. If two EDFs have the same new name, keep the larger EDF and delete the smaller one. If they are the same size, only keep one. Once there are no duplicates, close renaming.csv and rename it to renamingnow.csv.

## edf_rename.py 
Edit the box path accordingly. It will ask you for a "year" folder when you run it. It will rename the edfs in the folder you dictate according to the names given in renamingnow.csv. 

This script can also be repurposed for event folders if you need to rename multiple event folders(i.e. adding RESEARCH or MSLT to name). 

