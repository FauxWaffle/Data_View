import pandas as pd
import numpy as np

df = pd.read_csv('csv/datafile.csv')
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
        'Max File Name': max_file_size_name
    }
    return metrics


if __name__ == "__main_st__":
    print(df_all())
