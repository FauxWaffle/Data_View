import streamlit as st
import stream_back
import pandas as pd


st.set_page_config(layout="wide")
metrics = stream_back.df_all()

st.header("Data Summary:")
col_data_1, col_data_2 = st.columns(2)

metrics_sum = (metrics['File Sum'] / 1000).round(2)
metrics_count = metrics['Total Count']

with col_data_1:
    st.write("Total Size in GB: ", metrics_sum)
    st.write("Median File Size in MB:", metrics['File Med'])
    st.write("Number of Files Never Accessed:", metrics_count)
with col_data_2:
    st.write("Max File Size in MB:", metrics['File Max'])
    st.write("Min File Size in MB:", metrics['File Min'])


st.header('Data Controls:')

col1, col2 = st.columns(2)


with col1:
    metric_1 = st.toggle("File Size - MB")
    metric_2 = st.toggle("Created On")
    metric_3 = st.toggle("Last Access")
with col2:
    metric_4 = st.toggle("Last Modify")
    metric_5 = st.toggle("File Owner")
    metric_6 = st.toggle("Never Accessed - Click Header to Filter YES")


display_df = pd.DataFrame({'File Name': metrics['File Name']})


# Add other columns based on selected toggles
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


