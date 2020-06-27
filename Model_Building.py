
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
import statsmodels.api as sm


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
## DF WITH COLUMNS RELEVANT TO THE MODEL BUILDING
df_model = df[["Avg_salary","Rating","Size","Type of ownership","Industry","Sector","Revenue","No. of Competitors","Per_Hour","Employer_provided","State","Age_of_company","Python","R_Studio","AWS","EXCEL","Job_Titles_Simplified","Title_Seniority","Job_Description_Length"]]

## DF WITH DUMMY DATA
df_dummy = pd.get_dummies(df_model)

## TRAIN, VALIDATE AND TEST
x = df_dummy.drop('Avg_salary', axis = 1)
y = df_dummy.Avg_salary.values

X_train,X_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)

## OLS MEANS ORDINARY LEAST SQUARES WHICH IS JUST ANOTHER NAME FOR LINEAR REGRESSION`

x_sm = x = sm.add_constant(x)
model = sm.OLS(y,x_sm)
print(model.fit().summary())
