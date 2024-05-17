# Data_View
Get file statistics via Python and then view through Streamlit.

To begin, ~~run data_pull.ps1 in terminal as ADMIN - as PowerShell will install Python libraries if not present~~.

If Python is not installed, please install before continuing and add to path.
Run:
pip install streamlit
pip install pandas

Once complete, right click on folder where you unizpped the files and select, Open in Terminal.
Run the collections.py file and then enter your UNC path. No quotes or tic marks.
After completion Streamlit will auto-launch.


The script will pull file statistics on selected UNC path, then check if creation date and last touch date are equal.
All file statistics will be placed in the datafile.csv file within the CSV folder.


3/16/24:
- Working on adding 3rd tab for date range slider to show files within date range with SID as owner and not being accessed during the time frame selected.
- Fix quotes on UNC path causing code halt.
- Adding dynamic field for user input based prices of storage (currently coded to on-demand storage prices of Azure).

5/17/24:
- Rewrote the PS1 script in Python. Now data collection happens much quicker.


For questions or issues with running: OrrinDabney@Outlook.com
