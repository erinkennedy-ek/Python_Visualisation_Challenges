# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 12:06:14 2023

@author: A00275664
"""
import pandas as pd
import seaborn as sns

#Question 1(c)

#Read the CSV file into a dataframe and display first 5 rows
data = pd.read_csv("C:/Users/erink/OneDrive - TUS MM/avocado.csv")
#data = pd.read_csv("C:/Users/A00275664/OneDrive - TUS MM/avocado.csv")

#Create the plot with a Seaborn specific method
sns.relplot(data=data, kind='scatter', x='AveragePrice', y='Total Volume')

#Create the same plot but with the hue parameter set to year
#and dots for the total volume ranging in size from 10-100

sns.relplot(data=data, kind='scatter', x='AveragePrice', 
            y='Total Volume', hue='year', size='Total Volume', 
            sizes=(10, 100)) 

#Create a plot that looks like the following
#sns.catplot(data=data.query(region = 'Total US', 'West', 'WestTexNewMexico'), 
 #           hue = 'region', kind='box', x='year', y='Total Volume')

region_data = ['TotalUS', 'West', 'WestTexNewMexico'] 
region_data = data[data['region'].isin(region_data)] 
sns.catplot(data=region_data, x='year', y='Total Volume', hue='region', kind='box') 
#((AskPython, 2021) https://www.askpython.com/python-modules/pandas/pandas-isin)

region_data = ['TotalUS', 'West', 'WestTexNewMexico'] 
region_data = data[data['region'].isin(region_data)] 
custom = {'TotalUS': 'red', 'West': 'orange', 'WestTexNewMexico': 'blue'} 
sns.catplot(data=region_data, x='year', y='Total Volume', hue='region', kind='box', palette=custom) 