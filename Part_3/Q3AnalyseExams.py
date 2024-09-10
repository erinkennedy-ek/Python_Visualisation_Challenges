# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 13:08:43 2023

@author: erink
"""

#Question 3(a)

#Read data from CSV file into dataframe & display first five rows

import dask.dataframe as dd

exams = dd.read_csv("C:/Users/erink/OneDrive - TUS MM/exams.csv")
#exams = dd.read_csv("C:/Users/A00275664/OneDrive - TUS MM/exams.csv")


print(exams.head())

#Display the basic info for the DF & its col using info()
print(exams.info())
#((Dask, 2023),https://docs.dask.org/en/stable/generated/dask.dataframe.DataFrame.info.html)

#Display statistical info for math score, reading score and writing score col. using decribe()
print(exams[['writing score', 'reading score', 'math score']].describe().compute())
#((Dask, 2018)https://docs.dask.org/en/stable/generated/dask.dataframe.DataFrame.describe.html)

#Group data by race/ethnicity & display mean scores
race_mean = exams.groupby('race/ethnicity').agg({ 'reading score': 'mean', 'writing score': 'mean', 'math score': 'mean' }).compute()
print(race_mean)

#Display a single column as a DF with a bracket notation
print(exams[['race/ethnicity']].compute())

#Display a single col. as a series with bracket notation
print(exams['race/ethnicity'].compute())

#Display a single col. as a series with dot notation
print(exams.lunch.compute())

#Display only rows for females with math score >= 80

women_80 = exams[(exams['gender'] == 'female') & (exams['math score'] >= 80)]
print(women_80.compute())
