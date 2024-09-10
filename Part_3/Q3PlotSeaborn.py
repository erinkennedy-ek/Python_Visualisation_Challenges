# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 11:34:00 2023

@author: erink
"""


import dask.dataframe as dd
import matplotlib.pyplot as plt 
import seaborn as sns # attempted question


#Question 3(c)

#Read the CSV file into a dataframe and display first 5 rows

#avocado=dd.read_csv("C:/Users/A00275664/OneDrive - TUS MM/avocado.csv", dtype={'XLarge Bags': 'float64'}) 
avocado = dd.read_csv("C:/Users/ErinK/OneDrive - TUS MM/avocado.csv", dtype={'XLarge Bags': 'float64'}) 

#Display first five rows
print(avocado.head())

#Create the plot in the picture with a Seaborn specific method

plt.scatter(avocado['AveragePrice'], avocado['Total Volume'], alpha=.5) #Using matplotlib
plt.xlabel('Price') 
plt.ylabel('Total Volume') 
plt.title('Total Volume vs Average Price') 
plt.show() 

#Create the same plot but with the hue parameter set to year and dots for the 
#total volume ranging in size from 10-100

#plt.scatter(avocado['AveragePrice'], y=['Total Volume'], #First attempt
#hue=['year'], size=['Total Volume'], s=(10,100))

    # Did not figure out how to change size range

plt.scatter(avocado['AveragePrice'], avocado['Total Volume'], s=(10), c=avocado['year'], cmap='Greens')
plt.xlabel('AveragePrice')
plt.ylabel('Total Volume')
plt.show()

#((Statology, 2020)https://www.statology.org/matplotlib-scatterplot-color-by-value/)

#Create a plot that looks like the following
    #get error

region_data = ['TotalUS', 'West', 'WestTexNewMexico'] 
region_data = avocado[avocado['region'].isin(region_data)] 
custom = {'TotalUS': 'red', 'West': 'orange', 'WestTexNewMexico': 'blue'} 
sns.boxplot(data=region_data, x='year', 
            y='Total Volume', hue='region', palette = custom)

plt.boxplot(avocado['year'], y=avocado['Total Volume'], c=avocado['region'])
plt.xlabel('Year')
plt.ylabel('Total Volume')
plt.title('Total Volume by Year for Specified Regions')
plt.legend(title='Region')
plt.show()

#2nd attempt
#get error
region_data = ['TotalUS', 'West', 'WestTexNewMexico'] 
region_data = avocado[avocado['region'].isin(region_data)] 
custom = {'TotalUS': 'red', 'West': 'orange', 'WestTexNewMexico': 'blue'} 
sns.barplot(x='year', y='Total Volume', hue='region', 
            data = region_data, palette =custom, edgecolor='none')
plt.show()
