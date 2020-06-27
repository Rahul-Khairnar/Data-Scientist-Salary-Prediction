# -*- coding: utf-8 -*-
"""
Created on Mon May 18 20:27:12 2020

@author: Rahul Khairnar
"""

#SALARY PARSING
#COMPANY NAME TEXTT ONLY
#STATE FIELD SPLITTING
#AGE OF THE COMPANY
#PARSING OF JOB DESCRIPTION


import pandas as pd
import matplotlib as mpl
from datetime import *

today = datetime.now()
year = today.year
print(year)

df = pd.read_csv("data_science.csv")
df.head()

df.shape

## SALARY CLEANING ##
df["Per_Hour"] = df["Salary Estimate"].apply(lambda x:1 if "per hour" in x.lower() else 0)
df["Employer_provided"] = df["Salary Estimate"].apply(lambda x:1 if "Employer Provided" in x.lower() else 0)

df = df[df["Salary Estimate"]!="-1"]

Salary = df["Salary Estimate"].apply(lambda x: x.split('(')[0])

striped_salary = Salary.apply(lambda x: x.replace("K","").replace("$","")) 

Salary_minus_hr = striped_salary.apply(lambda x: x.replace("Per Hour","").replace("Employer Provided Salary:",""))

df["min_salary"] = Salary_minus_hr.apply(lambda x: int(x.split("-")[0]))
df["max_salary"] = Salary_minus_hr.apply(lambda x: int(x.split("-")[1]))
df["Avg_salary"] = (df["min_salary"]+df["max_salary"])/2

## SALARY CLEANING SUCCESSFUL ##

## GETTING THE AGE OF THE COMPANY FROM ITS ESTABLISHMENT DATE
df["Age_of_company"] = df["Founded"].apply(lambda x: int(year-x))
df["Age_of_company"] = df["Age_of_company"].replace(to_replace = 2021,value= -1)
## GETTING AGE SUCESSFUL ##
df["State"] = df["Location"].apply(lambda x: x.split(",")[1])
df["City"] = df["Location"].apply(lambda x: x.split(",")[0])

df["job_loc"] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis  = 1)

#### JOB DESCRIPTION PARSING PYTHON, R Studio, AWS, SPARK, EXCEL
df["Python"] = df["Job Description"].apply(lambda x: 1 if "python" in x.lower() else 0)
df["R_Studio"] = df["Job Description"].apply(lambda x: 1 if "r studio" in x.lower() else 0)
df["R_Studio"] = df["Job Description"].apply(lambda x: 1 if " R " in x else 0)
df["AWS"] = df["Job Description"].apply(lambda x: 1 if "aws" in x.lower() else 0)
df["SPARK"] = df["Job Description"].apply(lambda x: 1 if "spark" in x.lower() else 0)
df["EXCEL"] = df["Job Description"].apply(lambda x: 1 if "excel" in x.lower() else 0)

## EXPORTING THE DF AS A CSV
clean_data =df.iloc[:,1:30]
clean_data.to_csv("clean_data.csv", index = False)
