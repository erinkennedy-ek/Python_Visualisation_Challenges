# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 00:25:45 2023

@author: erink
"""
# QUESTION 3

#Question 3(b)
#Read the CSV file into a dataframe and display first 5 rows

import dask.dataframe as dd
import matplotlib.pyplot as plt 


#avocado=dd.read_csv("C:/Users/A00275664/OneDrive - TUS MM/avocado.csv", dtype={'XLarge Bags': 'float64'}) 
avocado = dd.read_csv("C:/Users/ErinK/OneDrive - TUS MM/avocado.csv", dtype={'XLarge Bags': 'float64'}) 

#Display first five rows
print(avocado.head())

#Create a new df containing total of SmallBags, LargeBages & XlargeBags,
#grouped by type, then display the df

total_by_type = avocado.groupby('type')[['Small Bags', 'Large Bags', 'XLarge Bags']].count().compute()
print(total_by_type)

#Use the grouped data to create a bar plot showing the no. of small, large & xl bags for both types of avocado

total_by_type.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Type of Avocado')
plt.ylabel('Count')
plt.title('Counts of Small, Large, and XL Bags for Avocado Types')
plt.legend(title='Bag Sizes')
plt.show()


#Use org data to create a scatter plot for the Total Volume % Avg Price col
#Using the Matplotlib library
plt.scatter(avocado['AveragePrice'], avocado['Total Volume']) 
plt.xlabel('Price') 
plt.ylabel('Total Volume') 
plt.title('Total Volume vs Average Price') 
plt.show() 

 