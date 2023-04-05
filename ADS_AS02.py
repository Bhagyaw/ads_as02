# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 14:11:57 2023

@author: bhagy
"""

#Import required modules
import pandas as pd
import matplotlib.pyplot as plt


#Start of main program
#Reading data from the source file. Here source file type is csv. 
#Therefore pandas reading funtion must be pd.read_csv
data_co2emi = pd.read_csv("API_EN.ATM.CO2E.KT_DS2_en_csv_v2_5358347.csv", header=2, index_col='Country Name', usecols=['Country Name', 'Indicator Name', '1990', '1995', '2000', '2005', '2010', '2015', '2020'])


print(data_co2emi)
selected_countries = ['Brazil', 'United States', 'China', 'United Kingdom', 'Australia', 'Russian Federation', 'South Africa', 'Canada', 'India', 'Spain']

selected_data_co2emi = data_co2emi.loc[selected_countries]
print(selected_data_co2emi)

# transpose the dataframe
data_co2emi_transposed = selected_data_co2emi.transpose()


print(data_co2emi_transposed)

data_co2emi_t_cleaned = data_co2emi_transposed.dropna()

# set the year column as an integer

data_co2emi_t_cleaned.iloc[1:, :] = data_co2emi_t_cleaned.iloc[1:, :].astype(int)

print(data_co2emi_t_cleaned)

print(data_co2emi_t_cleaned.iloc[1:, :])

# plot the bar chart
ax = data_co2emi_t_cleaned.iloc[1:, :].plot(kind='bar', stacked=True, colormap='rainbow')
ax.set_xlabel('Country')
ax.set_ylabel('CO2 Emission (in KT)')
ax.set_title('CO2 Emission for Brazil and China from 1990 to 2015')
plt.show()
