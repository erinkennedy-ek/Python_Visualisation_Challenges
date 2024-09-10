# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 12:47:06 2023

@author: A00275664
"""

import seaborn as sns
import pandas as pd

# Question 2(c)
#Read data from csv file into df & display first 5 rows
exams = pd.read_csv("C:/Users/erink/OneDrive - TUS MM/exams.csv")
#exams = pd.read_csv("C:/Users/A00275664/OneDrive - TUS MM/exams.csv")

#Use seaborn catplot to recreate plot

sns.countplot(x='parental level of education', data=exams) 

#Rotate the x labels for the plot to make them readable
parent_plot = sns.countplot(x='parental level of education', data=exams) 
parent_plot.set_xticklabels(parent_plot.get_xticklabels(),rotation = 45)
#(Zach, 2022)

#Create a seaborn scatter plot that compares the writing scores with the 
#reading scores. Use a different colour which students took a test prep course

sns.scatterplot(x='writing score', y='reading score', data=exams, 
                hue='test preparation course', palette='Set1') 


