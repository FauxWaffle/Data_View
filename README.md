# Data_View
Get file statistics via PowerShell and then view through Python.

To begin, run data_pull.ps1 in terminal as ADMIN - as PowerShell will install Python libraries if not present. 

After installation of Streamlit and Pandas, terminal will prompt for UNC path input. No need to add "" around path.

**!! BE AWARE THAT IF YOU HAVE FILES IN DIRECTORY WHICH ARE LINKS TO O365 (_not currently downloaded_), FILES WILL BE DOWNLOADED FOR "NOTOUCH" VERIFICATION !!**

The script will pull data statistics on selected UNC path, then check if creation date and last touch date are equal. If they are, it will write those files to a "notouch" csv file.
All file statistics will be placed in the datafile.csv file within the CSV folder.

**I have left the NOTOUCH comparison commented out (lines: 46-51 and line 55). This will shorten runtime by a lot.** 

Line 58 will autolaunch Streamlit which will open a local web-server in your default browser. From here you will be able to view/export your CSV with desired toggles selected. You can click column headers to sort.

!! Not final stage of program. Still in progress !!


2/29/2024:
I have added the "not touched" metric in with Python versus using PowerShell. This allows for a bit quicker data collection.
Once toggles are selected, if you hover over the header row you can select, EXPORT, which will save a CSV with the data fields selected.

For questions: OrrinDabney@Outlook.com
