# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 12:45:05 2023

@author: A00275664
"""
import pandas as pd

#Question 2(b)
#Read data from csv file into df & dsiplay first 5 rows
exams = pd.read_csv("C:/Users/erink/OneDrive - TUS MM/exams.csv")
#exams = pd.read_csv("C:/Users/A00275664/OneDrive - TUS MM/exams.csv")

#Use the pandas plot() method to create a box plot
race_mean = exams.groupby('race/ethnicity').agg({ 'reading score': 'mean', 'writing score': 'mean', 'math score': 'mean' }).reset_index
race_mean.plot.box()

#Use pandas plot() to recreate the plot
exams.plot.scatter(x = 'math score', y = 'reading score');

#Group the data by gender & calc avg scores. Create a bar plot
gender_mean = exams.groupby('gender').agg({ 'reading score': 'mean', 'writing score': 'mean', 'math score': 'mean' }).reset_index()
print(gender_mean)

#exams.groupby('gender')['reading score','writing score','math score'].agg(['mean']).plot.bar()

exams.groupby('gender').agg({ 'reading score': 'mean', 'writing score': 'mean', 'math score': 'mean' }).plot.bar()
