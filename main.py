import streamlit as st
import stream_back
import pandas as pd
from stream_back import *

st.set_page_config(layout="wide")
metrics = stream_back.df_all()

st.header("Data Summary:")


col_data_1, col_data_2, col_data_3 = st.columns(3)

#--Computing Data Metrics--#

metrics_sum = (metrics['File Sum'] / 1024).round(2)
metrics_count = metrics['Total Count']

never_accessed_size = (metrics['Never Touched Size'] / 1024).round(2)


#--Displaying Data Summary--#

with col_data_1:
    st.write("Total Size in GB:", metrics_sum)
    st.write("Total Number of Rows", metrics['DF Count'])
    st.write("Number of Files Never Accessed:", metrics_count)
with col_data_2:
    st.write("Max File Size in MB:", metrics['File Max'])
    st.write("Min File Size in MB:", metrics['File Min'])
    st.write("Median File Size in MB:", metrics['File Med'])
    st.write('Number of Files at Zero KB:', metrics['Zero KB'])
with col_data_3:
    st.write("Largest File Name:", metrics['Max File Name'])
    st.write("Total GB of Never Accessed:", never_accessed_size)
    st.write("Average Size of Untouched File:", metrics['Average Untouched'])


st.markdown("---")


#--Toggles for Data Controls--#
st.header('Data Controls:')
tab_main, tab_second = st.tabs(["All Data", "No File Owner"])


col1, col2 = st.columns(2)

with tab_main:
    with col1:
        metric_1 = st.toggle("File Size - MB")
        metric_2 = st.toggle("Created On")
        metric_3 = st.toggle("Last Access")

    with col2:
        metric_4 = st.toggle("Last Modify")
        metric_5 = st.toggle("File Owner")
        metric_6 = st.toggle("Never Accessed - Click Header to Filter YES")

sid_count = metrics['SID as Owner'].count()
with tab_second:
    st.write("Total Number of Unowned Files:", sid_count)
    export_data = convert_df(metrics['Export Results'])
    st.download_button(
        label="Download SID list to CSV",
        data=export_data,
        file_name="Files_no_owner.csv",
        mime='text/csv'
    )


display_df = pd.DataFrame({'Path': metrics['Folder Path'],'File Name': metrics['File Name']})


if metric_1:
    display_df['File Size'] = metrics['File Size']
if metric_2:
    display_df['Created On'] = metrics['Created On']
    
if metric_3:
    display_df['Last Access'] = metrics['Last Access']
    
if metric_4:
    display_df['Last Modify'] = metrics['Last Touch']
    
if metric_5:
    display_df['File Owner'] = metrics['File Owner']
    
if metric_6:
    display_df['Never Accessed'] = metrics['Not Touched']



st.dataframe(display_df, use_container_width=False)


#--SID as Owner--#


st.markdown("---")
with tab_second:
    deleted_owner = {
        'File Name': metrics['SID File'],
        'No File Owner': metrics['SID as Owner']
    }

    sid_df = pd.DataFrame(deleted_owner)

    st.table(sid_df)





#--Dataframe build for Table--#


st.header('Storage Costs in USD:')


storage_cost = {'Premium': 0.15, 'Hot': 0.018, 'Cool': 0.01, 'Cold': 0.0036, 'Archive': 0.00099}

for storage in storage_cost:
    if storage == 'Premium':
        total_cost_prem = metrics_sum * storage_cost['Premium']
        total_unused_cost_prem = never_accessed_size * storage_cost['Premium']
    elif storage == 'Hot':
        total_cost_hot = metrics_sum * storage_cost['Hot']
        total_unused_cost_hot = never_accessed_size * storage_cost['Hot']
    elif storage == 'Cool':
        total_cost_cool = metrics_sum * storage_cost['Cool']
        total_unused_cost_cool = never_accessed_size * storage_cost['Cool']
    elif storage == 'Cold':
        total_cost_cold = metrics_sum * storage_cost['Cold']
        total_unused_cost_cold = never_accessed_size * storage_cost['Cold']
    elif storage == 'Archive':
        total_cost_arch = metrics_sum * storage_cost['Archive']
        total_unused_cost_arch = never_accessed_size * storage_cost['Archive']


options = {
    'Storage Tiers': ['Premium', 'Hot', 'Cool', 'Cold', 'Archive'],
    'Price': [0.15, 0.018, 0.01, 0.0036, 0.00099],
    'Monthly Cost in Use': [total_cost_prem.round(2), total_cost_hot.round(2), total_cost_cool.round(2), total_cost_cold.round(2),
                        total_cost_arch.round(2)],
    'Monthly Cost Never Accessed' : [total_unused_cost_prem.round(2), total_unused_cost_hot.round(2), total_unused_cost_cool.round(2),
                          total_unused_cost_cold.round(2), total_unused_cost_arch.round(2)]
}


table_df = pd.DataFrame(options)
st.table(table_df)
