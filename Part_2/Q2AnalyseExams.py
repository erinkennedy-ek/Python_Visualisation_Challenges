# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 12:53:58 2023

@author: erink
"""


#Question 2(a)

#Read data from CSV file into dataframe & display first five rows
import pandas as pd




exams = pd.read_csv("C:/Users/erink/OneDrive - TUS MM/exams.csv")
#exams = pd.read_csv("C:/Users/A00275664/OneDrive - TUS MM/exams.csv")

exams.head()

#Display the basic info for the DF & its col using info()
print(exams.info())

#Display statistical info for math score, reading score and writing score col. using decribe()
print(exams[['writing score', 'reading score', 'math score']].describe())

#Group data by race/ethnicity & display mean scores
race_mean = exams.groupby('race/ethnicity').agg({ 'reading score': 'mean', 'writing score': 'mean', 'math score': 'mean' }).reset_index()
print(race_mean)

#Display a single column as a DF with a bracket notation
print(exams[['race/ethnicity']])

#Display a single col. as a series with bracket notation
print(exams['race/ethnicity'])

#Display a single col. as a series with dot notation
print(exams.lunch)

#Display only rows for females with math score >= 80
exams.query('gender == "female" and `math score` >= 80') 

#---------------------------------------------------------
