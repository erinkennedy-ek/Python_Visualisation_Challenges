# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 15:46:25 2023

@author: erink
"""

#Question 3-2(b)

#Read data from csv file into df & dsiplay first 5 rows

import dask.dataframe as dd
import matplotlib.pyplot as plt #used for more interactive plots

exams = dd.read_csv("C:/Users/erink/OneDrive - TUS MM/exams.csv")
#exams = dd.read_csv("C:/Users/A00275664/OneDrive - TUS MM/exams.csv")

print(exams.head())

#Use the pandas plot() method to create a box plot

race_mean = exams.groupby('race/ethnicity').agg({ 'reading score': 'mean', 'writing score': 'mean', 'math score': 'mean' }).compute()
race_mean.plot.box()

#Use pandas plot() to recreate the plot

plt.scatter(x='math score', y='reading score', data = exams);
#((McDonald, 2021), https://www.bing.com/videos/riverview/relatedvideo?&q=matplotlib+scatter+plot+with+a+dataset&&mid=E293016EBF32D27A19A6E293016EBF32D27A19A6&&FORM=VRDGAR)

#Group the data by gender & calc avg scores. Create a bar plot
gender_mean = exams.groupby('gender').agg({ 'reading score': 'mean', 'writing score': 'mean', 'math score': 'mean' }).compute()
print(gender_mean)

gender_mean.plot(kind='bar', figsize=(10, 6))
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Average Score by Gender')
plt.legend(title='Average Score')
plt.show() 