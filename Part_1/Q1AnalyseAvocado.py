# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Question 1(a)
#Read the CSV file into a dataframe
import pandas as pd
data = pd.read_csv("C:/Users/erink/OneDrive - TUS MM/avocado.csv")
#Display type, memory, consumption and null count info using info()
info = data.info()
print(info)
#Display number unique values in each column
data.nunique()
#Display first and last five rows
print(data.head())
print(data.tail())
#Display first and last four columns
print(data.head(4))
print(data.tail(4))
#Access three columns with bracket notation, display first 5 rows
print(data['Date'].head())
print(data['Total Bags'].head)
print(data['Small Bags'].head)
#Access one column with dot notation
print(data.AveragePrice.head())
#Multiply Total Vol & AvgPrice, store result in EstimatedRevenue
data.columns = data.columns.str.replace(" ", "")
data['EstimatedRevenue'] = data.TotalVolume * data.AveragePrice
#Then display first 5 rows
print(data.EstimatedRevenue.head(4))
#Create a DF grouped by region & type, that inc avg price for grouped col.
data_region_type = data.groupby(['region', 'type'])['AveragePrice'].mean()                
print(data_region_type)
#Reset the index and display first 5 rows
data_region_type = data.set_index(['region','type']) 
print (data_region_type.head())
#Create a barplot showing the mean, median, stan dev of the TotalVolume col by year
totalvol_bar= data.groupby('year')['TotalVolume'].agg(['mean', 'median','std']).plot.bar()
print(totalvol_bar)