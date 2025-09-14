# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 15:46:17 2025

@author: zmah
"""

# GenAI BCG program
import pandas as pd
import os


# converting to df
df = pd.read_excel('raw_data.xlsx')
df = df.rename(columns={'Unnamed: 0': 'Metric', 'company': 'Company'})



# analysis
# Melting the year columns into a long format
melted_df = df.melt(id_vars=['Company', 'Metric'], var_name='Year', value_name='Value')

# Converting Year to int for sorting and calculations
melted_df['Year'] = melted_df['Year'].astype(int)

# Sorting values by Company, Metric, then Year
melted_df = melted_df.sort_values(by=['Company', 'Metric', 'Year'])

# Calculate year-over-year percentage change within each Company and Metric group
melted_df['YoY Change (%)'] = melted_df.groupby(['Company', 'Metric'])['Value'].pct_change() * 100

# (Optional) Pivot back to wide format for easier viewing
result_df = melted_df.pivot_table(index=['Company', 'Metric'], columns='Year', values=['Value', 'YoY Change (%)'])
result_df.columns = ['{}_{}'.format(val[0], val[1]) for val in result_df.columns]

print(result_df.head())