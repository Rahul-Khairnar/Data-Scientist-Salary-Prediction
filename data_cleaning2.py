# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 22:25:18 2020

@author: Rahul Khairnar
"""
import pandas as pd

df = pd.read_csv("clean_data.csv")

def title_simplifier(job_title):
    
    if "data scientist" in job_title.lower():
        return "Data Scientist"
    
    elif "data engineer" in job_title.lower():
        return "Data Engineer"
    
    elif "analyst" in job_title.lower():
        return "Analyst"
    
    elif "machine learning" in job_title.lower():
        return "Machine Learning Engineer"
    
    elif "manager" in job_title.lower():
        return "manager"
  
    elif "director" in job_title.lower():
        return "Director";
    
    else:
        return "Other Titles"
    
def title_seniority(title):
    
    if 'sr' in title.lower() or 'sr.' in title.lower() or 'senior' in title.lower() or 'lead' in title.lower() or 'principal' in title.lower():
        return "Senior"
   
    elif "jr" in title.lower() or "jr." in title.lower() or "junior" in title.lower():
        return "Junior"
    
    else:
        return "Not Mentioned"
## SORTING JOB TITLES INTO A BETTER CATEGORIES USING THE ABOV FUNCTIONS
df["Job_Titles_Simplified"] = df["Job Title"].apply(title_simplifier)
#print(df["Job_Titles_Simplified"].value_counts())

## CHECKING IF JOB TITLE HAS SENIOR OR JUNIOR MENTIONED IN IT AND SORTING IT
df["Title_Seniority"] = df["Job Title"].apply(title_seniority)
#print(df["Title_Seniority"].value_counts())
## STATE COLUMNS 
df["State"] = df["State"].apply(lambda x: x.strip() if x.strip().lower()!= "los angeles" else "CA")
print(df["State"].value_counts())
## JOB DESCRIPTION LENGTH
def length(job_title):
    length_title = len(job_title)
    return length_title

df["Job_Description_Length"] = df["Job Description"].apply(lambda x:len(x))

## COMPETITOR COUNT
df["No. of Competitors"] = df["Competitors"].apply(lambda x: len(x.split(",")) if x!='-1' else 0)

## COMPANY NAME WITHOUT RATINGS
df["Comp_Name"] = df["Comp_Name"].apply(lambda x: x.split("\n")[0])

## RESOLVING THE PER HOUR PROBLEM
df["min_salary"] = df.apply(lambda x: x.min_salary*2 if x.Per_Hour == 1 else x.min_salary, axis = 1)
df["max_salary"] = df.apply(lambda x: x.max_salary*2 if x.Per_Hour == 1 else x.max_salary, axis = 1)

df["Avg_salary"] = df.apply(lambda x: (x.min_salary+x.max_salary)/2 if x.Per_Hour == 1 else x.Avg_salary, axis = 1)

## EXPORTING DATA TO CSV
df.to_csv("deep_clean_data.csv", index = False)


    