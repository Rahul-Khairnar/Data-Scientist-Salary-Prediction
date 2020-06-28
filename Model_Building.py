"""
Created on Sun Jun 28 10:18:45 2020

@author: Rahul Khairnar
"""
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
print("1")
import statsmodels.api as sm

X_sm = X = sm.add_constant(X)
model = sm.OLS(y,X_sm)
#print(model.fit().summary())

from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import cross_val_score

lm = LinearRegression()
lm.fit(X_train,y_train)
#print(np.mean(cross_val_score(lm,X_train, y_train, scoring = "neg_mean_absolute_error",cv = 3)))
print('2')
lm_l = Lasso(alpha=.13)
lm_l.fit(X_train,y_train)
#print(np.mean(cross_val_score(lm_l,X_train,y_train, scoring = 'neg_mean_absolute_error', cv= 3)))

alpha = []
error = []

for i in range(1,100):
    alpha.append(i/100)
    lml = Lasso(alpha=(i/100))
    error.append(np.mean(cross_val_score(lml,X_train,y_train, scoring = 'neg_mean_absolute_error', cv= 3)))
    
plt.plot(alpha,error)

err = tuple(zip(alpha,error))
df_err = pd.DataFrame(err, columns = ['alpha','error'])
df_err[df_err.error == max(df_err.error)]

# random forest 
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()
print(np.mean(cross_val_score(rf,X_train,y_train,scoring = 'neg_mean_absolute_error', cv= 3)))
print("3")
from sklearn.model_selection import GridSearchCV
parameters = {'n_estimators':range(10,300,10), 'criterion':('mse','mae'), 'max_features':('auto','sqrt','log2')}

gs = GridSearchCV(rf,parameters,scoring='neg_mean_absolute_error',cv=3)
gs.fit(X_train,y_train)

print("Now Starting")
print(gs.best_score_)
print(gs.best_estimator_)
print("4")

tpred_lm = lm.predict(X_test)
tpred_lml = lm_l.predict(X_test)
tpred_rf = gs.best_estimator_.predict(X_test)

from sklearn.metrics import mean_absolute_error
print(mean_absolute_error(y_test,tpred_lm))
print(mean_absolute_error(y_test,tpred_lml))
print(mean_absolute_error(y_test,tpred_rf))


