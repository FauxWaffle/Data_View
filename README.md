# Data_View
Get file statistics via PowerShell and then view through Python.

To begin, run data_pull.ps1 in terminal as ADMIN - as PowerShell will install Python libraries if not present. 
If Python is not installed, please install before continuing.

After installation of Streamlit and Pandas, terminal will prompt for UNC path input. Adding quotes around UNC path will cause an error.



The script will pull file statistics on selected UNC path, then check if creation date and last touch date are equal.
All file statistics will be placed in the datafile.csv file within the CSV folder.


3/16/24:
- Working on adding 3rd tab for date range slider to show files within date range with SID as owner and not being accessed during the time frame selected.
- Fix quotes on UNC path causing code halt.
- Adding dynamic field for user input based prices of storage (currently coded to on-demand storage prices of Azure).

For questions or issues with running: OrrinDabney@Outlook.com
