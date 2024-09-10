# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 00:24:56 2023

@author: erink
"""
#((Dask,2023)https://www.dask.org/)
#((Matplotlib,2023), https://matplotlib.org/)

#Question 3-1(a)

#Read the CSV file into a dataframe
import dask.dataframe as dd
import matplotlib.pyplot as plt 


#avocado=dd.read_csv("C:/Users/A00275664/OneDrive - TUS MM/avocado.csv", 
#dtype={'XLarge Bags': 'float64'}) 
avocado = dd.read_csv("C:/Users/ErinK/OneDrive - TUS MM/avocado.csv", 
                      dtype={'XLarge Bags': 'float64'}) 
#(Sowmya, 2020)                      #Change Datatype for XLarge bags 
    
#Display type, memory consumption and null count info using info()

avocado.info().compute()
avocado.memory_usage #dask
#((Dask, 2023)https://docs.dask.org/en/stable/generated/dask.dataframe.Series.memory_usage.html#:~:text=DataFrame.memory_usage%20Bytes%20consumed%20by%20a%20DataFrame.%20Examples%20%3E%3E%3E,data%2C%20which%20is%20necessarily%20smaller%3A%20%3E%3E%3E%20s.memory_usage%28index%3DFalse%29%2024)

# Count null values in each column
null_counts = avocado.isnull().sum().compute()
print(null_counts)

#Display number unique values in each column

uq_vl={}
for i in avocado.columns:
   uq_vl[i] = len( avocado[i].unique())
print(uq_vl)
#https://stackoverflow.com/questions/30503321/finding-count-of-distinct-elements-in-dataframe-in-each-column

#Display first and last five rows
avocado.head() #dask 
avocado.tail()

#Display first and last four rows
avocado.head(4)
avocado.tail(4)

#Access 3 columns with bracket notation & display first 5 rows
selected_col = avocado[['Date', 'Total Volume', 'region']]
print(selected_col.head())

#Access one column with dot notation
print(avocado.Date.compute())

#Multiply Total Vol & AvgPrice, store result in EstimatedRevenue

avocado.assign(EstimatedRevenue=avocado['Total Volume'] * avocado['AveragePrice'])
print(avocado.head())

#Create a DF grouped by region & type, that inc avg price for grouped col. Reset index

region_type = avocado.groupby(['region', 'type'])['AveragePrice'].agg('mean').reset_index()
print(region_type.head())

#Create a barplot showing the mean, median, stan dev of the TotalVolume col by year

summ_stats = avocado.groupby('year')['Total Volume'].agg(['mean', 'median', 'std'], shuffle='tasks').compute()
summ_stats.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Year')
plt.ylabel('Value')
plt.title('Statistics of TotalVolume by Year')
plt.legend(title='Statistics')
plt.show() 

#The shuffle=tasks  was added as a parameter to tell Dask to handle the median in 
#a way that is more memory efficient as it is not as optimised as Pandas. 
#It helps when handling large datasets
#((Matplotlip, 2012), https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html)
#((Dask,2018), https://docs.dask.org/en/stable/dataframe-groupby.html)




 