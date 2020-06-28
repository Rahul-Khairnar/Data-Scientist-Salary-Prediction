
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("deep_clean_data.csv")
#print(df.columns)

df_model = df[["Avg_salary","Rating","Size","Type of ownership","Industry","Sector","Revenue","No. of Competitors","Per_Hour","Employer_provided","State","job_loc","Age_of_company","Python","SPARK","AWS","EXCEL","Job_Titles_Simplified","Title_Seniority","Job_Description_Length"]]

df_dummy = pd.get_dummies(df_model)

from sklearn.model_selection import train_test_split

X = df_dummy.drop("Avg_salary", axis = 1)
y = df_dummy.Avg_salary.values

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 42)

import statsmodels.api as sm

X_sm = X = sm.add_constant(X)
model = sm.OLS(y,X_sm)
#print(model.fit().summary())

from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import cross_val_score

lm = LinearRegression()
lm.fit(X_train,y_train)

print(np.mean(cross_val_score(lm,X_train, y_train, scoring = "neg_mean_absolute_error",cv = 3)))
