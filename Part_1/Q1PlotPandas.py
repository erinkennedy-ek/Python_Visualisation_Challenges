# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 12:48:23 2023

@author: A00275664
"""

import pandas as pd

#Question 1(b)
#Read the CSV file into a dataframe and display first 5 rows

data = pd.read_csv("C:/Users/erink/OneDrive - TUS MM/avocado.csv")

#Create a new df containing total of SmallBags, LargeBages & XlargeBags,
#grouped by type, then display the df

type_bags = data.groupby('type')[['Small Bags', 'Large Bags', 'XLarge Bags']].sum()
print(type_bags)

#Use the grouped data to create a bar plot 
#showing the no. of small, large & xl bags for both types of avocado

type_bags_bar=data.groupby('type')[['Small Bags', 'Large Bags', 'XLarge Bags']].sum().plot.bar()
print(type_bags_bar)


#Use org data to create a scatter plot for the Total Volume % Avg Price col

totalvol=data.plot.scatter(x = 'Total Volume', y = 'AveragePrice', s=5)
print(totalvol)