import pandas as pd
import numpy as np
import streamlit as st


df = pd.read_csv('csv/datafile.csv')
#print(df['File Size'].median())


zero_kb = 0
for smallest_files in df['File Size']:
    if smallest_files == 0:
        zero_kb += 1

#--Search for SID as Owner--#

pattern = r'S-1'

filtered_df = df[df['File Owner'].str.contains(pattern) | df['File Name'].str.contains(pattern)]
result_dict = dict(zip(filtered_df['File Owner'], filtered_df['File Name']))
#result_totals = result_dict['File Name'].count()

#--Getting Metrics--#

#Might need to look at the Wine python app I made and ignore all zero kb lines so the math works.

df['File Size'] = (df['File Size'] / 1000).round(2)
size_sort = df.sort_values(by=['File Size'], ascending=False)
file_size_sum = df['File Size'].sum()
file_size_max = df['File Size'].max()
file_size_min = df['File Size'].min()
file_size_med = df['File Size'].median()


max_file_size_name = df.loc[df['File Size'] == df['File Size'].max()]["File Name"].squeeze()

#--Never Accessed Files--
df['Never Accessed'] = np.where(df['Created On'] == df['Last Access'], 'Yes', 'No')
yes_rows = df[df['Never Accessed'] == 'Yes']
yes_rows = yes_rows.shape[0]
never_accessed_df = df[df['Never Accessed'] == 'Yes']
yes_total_size = never_accessed_df['File Size'].sum()
yes_average = never_accessed_df['File Size'].median()

#--Total Number of Rows--
df_count = df['File Name'].count()



def df_all():
    metrics = {
        'File Name': df['File Name'],
        'File Size': df['File Size'],
        'Last Touch': df['Last Touch'],
        'Created On': df['Created On'],
        'Last Access': df['Last Access'],
        'File Owner': df['File Owner'],
        'SID as Owner': filtered_df['File Owner'],
        'SID File': filtered_df['File Name'],
        'Export Results': result_dict,
        'Size Sorted': size_sort,
        'File Sum': file_size_sum,
        'File Max': file_size_max,
        'File Min': file_size_min,
        'File Med': file_size_med,
        'Not Touched': df['Never Accessed'],
        'Total Count': yes_rows,
        'Never Touched Size': yes_total_size,
        'Average Untouched': yes_average,
        'DF Count': df_count,
        'Max File Name': max_file_size_name,
        'Zero KB': zero_kb,
        'Folder Path': df['Path']
    }
    return metrics



@st.cache_data
def convert_df(result_dict):
    return filtered_df.to_csv().encode('utf-8')






if __name__ == "__main__":
    print(df_all())
