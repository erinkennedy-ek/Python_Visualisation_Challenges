# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 16:08:55 2023

@author: erink
"""

import dask.dataframe as dd
import matplotlib.pyplot as plt

# Question 3-2(c)

#Read data from csv file into df & display first 5 rows

exams = dd.read_csv("C:/Users/erink/OneDrive - TUS MM/exams.csv")
#exams = dd.read_csv("C:/Users/A00275664/OneDrive - TUS MM/exams.csv")

print(exams.head())

#Use seaborn catplot to recreate plot
    #not in correct order
value_counts = exams['parental level of education'].value_counts().compute()
colours=["blue", "orange", "green", "red", "purple", "brown"]
plt.bar(value_counts.index, value_counts.values, color=colours)
plt.xlabel('parental level of education')
plt.ylabel('count')
plt.show()
#((Stack Overflow, 2018),https://stackoverflow.com/questions/48939795/how-to-plot-a-count-bar-chart-grouping-by-one-categorical-column-and-coloring-by)

#Rotate the x labels for the plot to make them readable

value_counts = exams['parental level of education'].value_counts().compute()
colours=["blue", "orange", "green", "red", "purple", "brown"]
plt.bar(value_counts.index, value_counts.values, color=colours)
plt.xlabel('parental level of education')
plt.xticks(rotation=45)
plt.ylabel('count')
plt.show()
#(Stack Overflow, 2016)(https://stackoverflow.com/questions/10998621/rotate-axis-tick-labels))

#Create a seaborn scatter plot that compares the writing scores with the 
#reading scores. Use a different colour which students took a test prep course

plt.scatter(x='writing score', y='reading score', data=exams,
            cmap='test preparation course')
plt.colorbar(label='Test Preparation Course')
plt.show()
#((McDonald, 2021), https://www.bing.com/videos/riverview/relatedvideo?&q=matplotlib+scatter+plot+with+a+dataset&&mid=E293016EBF32D27A19A6E293016EBF32D27A19A6&&FORM=VRDGAR)