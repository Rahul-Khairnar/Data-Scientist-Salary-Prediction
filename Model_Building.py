
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("deep_clean_data.csv")

## CHOOSE RLEVANT DATA
## CREATE SEPARATE COLUMNS FOR EVERY COLUMN CONTAINING CATEORICAL VALUES. 
## CREATE TRAIN, VALIDATE AND TEST DATA FROM THE WHOLE DATA

## MODELS
## 1. LINEAR REGRESSION
## 2. LASSOO REGRESSION
## 3. RANDOM FORESTS

## TUNE THESE MODELS USING GRIDSEARCH CV
## TEST ENSEMBLES

print(df.columns)

df_model = df[["Avg_salary","Rating","Size","Type of ownership","Industry","Sector","Revenue","No. of Competitors","Per_Hour","Employer_provided","State","Age_of_company","Python","R_Studio","AWS","EXCEL","Job_Titles_Simplified","Title_Seniority","Job_Description_Length"]]



