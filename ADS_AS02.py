# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 14:11:57 2023

@author: bhagy
"""

#Import required modules
import pandas as pd
import matplotlib.pyplot as plt


#Start of 1st program CO2 Emission (in KT) from 1990 to 2015
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

print(data_co2emi_t_cleaned.describe())

print(data_co2emi_t_cleaned.iloc[1:, :])

# plot the bar chart
chart1 = data_co2emi_t_cleaned.iloc[1:, :].plot(kind='bar', stacked=False, colormap='rainbow')
#labelling x axis and y axis
chart1.set_xlabel('Year')
chart1.set_ylabel('CO2 Emission (in KT)')
#Add Title to the graph
chart1.set_title('CO2 Emission from 1990 to 2015')
#Add legend to explain the each lineplot 
chart1.legend(loc='center left', bbox_to_anchor=(1, 0.5))
# save the plot output as png
plt.savefig('CO2_Emission.png')
#Display the plot
plt.show()


#Start of 2nd program Electricity production from oil, gas and coal sources (% of total) from 1990 to 2015
#Reading data from the source file. Here source file type is csv. 
#Therefore pandas reading funtion must be pd.read_csv
data_Electricity = pd.read_csv("API_EG.ELC.FOSL.ZS_DS2_en_csv_v2_5358479.csv", header=2, index_col='Country Name', usecols=['Country Name', 'Indicator Name', '1990', '1995', '2000', '2005', '2010', '2015', '2020'])


print(data_Electricity)
#selected_countries = ['Brazil', 'United States', 'China', 'United Kingdom', 'Australia', 'Russian Federation', 'South Africa', 'Canada', 'India', 'Spain']

selected_data_Electricity = data_Electricity.loc[selected_countries]
print(selected_data_Electricity)

# transpose the dataframe
data_Electricity_transposed = selected_data_Electricity.transpose()


print(data_Electricity_transposed)

data_Electricity_t_cleaned = data_Electricity_transposed.dropna()

# set the year column as an integer

data_Electricity_t_cleaned.iloc[1:, :] = data_Electricity_t_cleaned.iloc[1:, :].astype(int)

print(data_Electricity_t_cleaned)

print(data_Electricity_t_cleaned.iloc[1:, :])

# plot the bar chart
chart2 = data_Electricity_t_cleaned.iloc[1:, :].plot(kind='bar', stacked=False, colormap='rainbow')
#labelling x axis and y axis
chart2.set_xlabel('Year')
chart2.set_ylabel('Electricity production from oil, gas and coal sources (% of total)')
#Add Title to the graph
chart2.set_title('Electricity Generation from 1990 to 2015')
#Add legend to explain the each lineplot 
chart2.legend(loc='center left', bbox_to_anchor=(1, 0.5))
# save the plot output as png
plt.savefig('Electricity Generation.png')
#Display the plot
plt.show()

#Start of 3rd program Population (% of total) from 1990 to 2015
#Reading data from the source file. Here source file type is csv. 
#Therefore pandas reading funtion must be pd.read_csv
data_population = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_5358404.csv", header=2, index_col='Country Name', usecols=['Country Name', 'Indicator Name', '1990', '1995', '2000', '2005', '2010', '2015', '2020'])

selected_data_population = data_population.loc[selected_countries]
print(selected_data_population)

# transpose the dataframe
data_population_transposed = selected_data_population.transpose()

print(data_population_transposed)

data_population_t_cleaned = data_population_transposed.dropna()

# set the year column as an integer

data_population_t_cleaned.iloc[1:, :] = data_population_t_cleaned.iloc[1:, :].astype(int)

print(data_population_t_cleaned)

print(data_population_t_cleaned.iloc[1:, :])

plt.figure()
#For loop to load required data using headers.
plt.plot(data_population_t_cleaned.iloc[1:, :])
   
#labelling x axis and y axis
plt.xlabel('Year')
plt.ylabel('Population (% of total)')

#Add legend to explain the each lineplot 
plt.legend(selected_countries, loc='center left', bbox_to_anchor=(1, 0.5))
#Add Title to the graph
plt.title("Population (% of total) from 1990 to 2015")
# save the plot output as png
plt.savefig("Population.png")
#Display the plot
plt.show()

#Start of 4th program Electric  Power consumption (kWh per capita) from 1990 to 2015
#Reading data from the source file. Here source file type is csv. 
#Therefore pandas reading funtion must be pd.read_csv
data_powerconsum = pd.read_csv("API_EG.USE.ELEC.KH.PC_DS2_en_csv_v2_5359189.csv", header=2, index_col='Country Name', usecols=['Country Name', 'Indicator Name', '1990', '1995', '2000', '2005', '2010', '2015', '2020'])

selected_data_powerconsum = data_powerconsum.loc[selected_countries]
print(selected_data_powerconsum)

# transpose the dataframe
data_powerconsum_transposed = selected_data_powerconsum.transpose()


print(data_powerconsum_transposed)

data_powerconsum_t_cleaned = data_powerconsum_transposed.dropna()

# set the year column as an integer

data_powerconsum_t_cleaned.iloc[1:, :] = data_powerconsum_t_cleaned.iloc[1:, :].astype(int)

print(data_powerconsum_t_cleaned)

print(data_powerconsum_t_cleaned.iloc[1:, :])

plt.figure()
#For loop to load required data using headers.
plt.plot(data_powerconsum_t_cleaned.iloc[1:, :])
   
#labelling x axis and y axis
plt.xlabel('Year')
plt.ylabel('Electric  Power consumption (kWh per capita)')

#Add legend to explain the each lineplot 
plt.legend(selected_countries, loc='center left', bbox_to_anchor=(1, 0.5))
#Add Title to the graph
plt.title("Electric  Power consumption from 1990 to 2015")
# save the plot output as png
plt.savefig("Electric  Power consumption.png")
#Display the plot
plt.show()



#Start of 5th program Electricity production from nuclear sources (% of total) from 1990 to 2015
#Reading data from the source file. Here source file type is csv. 
#Therefore pandas reading funtion must be pd.read_csv
data_nuclearpower = pd.read_csv("API_EG.ELC.NUCL.ZS_DS2_en_csv_v2_5362829.csv", header=2, index_col='Country Name', usecols=['Country Name', 'Indicator Name', '1990', '1995', '2000', '2005', '2010', '2015', '2020'])

selected_data_nuclearpower = data_nuclearpower.loc[selected_countries]
print(selected_data_nuclearpower)

# transpose the dataframe
data_nuclearpower_transposed = selected_data_nuclearpower.transpose()


print(data_nuclearpower_transposed)

data_nuclearpower_t_cleaned = data_nuclearpower_transposed.dropna()

# set the year column as an integer

data_nuclearpower_t_cleaned.iloc[1:, :] = data_nuclearpower_t_cleaned.iloc[1:, :].astype(int)

print(data_nuclearpower_t_cleaned)

print(data_nuclearpower_t_cleaned.iloc[1:, :])

plt.figure()
#For loop to load required data using headers.
plt.plot(data_nuclearpower_t_cleaned.iloc[1:, :])
   
#labelling x axis and y axis
plt.xlabel('Year')
plt.ylabel('Electricity production from nuclear sources (% of total)')

#Add legend to explain the each lineplot 
plt.legend(selected_countries, loc='center left', bbox_to_anchor=(1, 0.5))
#Add Title to the graph
plt.title("Electricity production from nuclear sources from 1990 to 2015")
# save the plot output as png
plt.savefig("Electricity production from nuclear source.png")
#Display the plot
plt.show()


#Start of 5th program Electricity production from renewable sources, excluding hydroelectric (kWh) from 1990 to 2015
#Reading data from the source file. Here source file type is csv. 
#Therefore pandas reading funtion must be pd.read_csv
data_renewable = pd.read_csv("API_EG.ELC.RNWX.KH_DS2_en_csv_v2_5358682.csv", header=2, index_col='Country Name', usecols=['Country Name', 'Indicator Name', '1990', '1995', '2000', '2005', '2010', '2015', '2020'])

selected_data_renewable = data_renewable.loc[selected_countries]
print(selected_data_renewable)

# transpose the dataframe
data_renewable_transposed = selected_data_renewable.transpose()


print(data_renewable_transposed)

data_renewable_t_cleaned = data_renewable_transposed.dropna()

# set the year column as an integer

#data_renewable_t_cleaned.iloc[1:, :] = data_renewable_t_cleaned.iloc[1:, :].astype(int)

print(data_renewable_t_cleaned)

print(data_renewable_t_cleaned.iloc[1:, :])

plt.figure()
#For loop to load required data using headers.
plt.plot(data_renewable_t_cleaned.iloc[1:, :])
   
#labelling x axis and y axis
plt.xlabel('Year')
plt.ylabel('Electricity production from renewable sources, excluding hydroelectric (kWh)')

#Add legend to explain the each lineplot 
plt.legend(selected_countries, loc='center left', bbox_to_anchor=(1, 0.5))
#Add Title to the graph
plt.title("Electricity production from renewable sources from 1990 to 2015")
# save the plot output as png
plt.savefig("Electricity production from renewable sources.png")
#Display the plot
plt.show()