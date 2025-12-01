Code used for exporting sleep studies from Domino and how to save them for lab use.

# copying_without_vids.bat
Edit the source and destination directory before running. Make the destination directory somewhere in the research folder on the Zdrive.

# event_export.bat
Before running this script, you need to open Domino on the computer you will run this script on and export the event files of a sleep study, with all annotations selected, to the loacation you want to save all the other event files.
This will save the location and format you want to export the event files. Once you have done that, you can close Domino and prepare to run the script. You will need to download nirmd and keep it in the same location as the event_export.bat file.

You want run this script on the files you created that have no videos attached. This script will create a file called processed_subdirectories.log that will be needed for the next step.


