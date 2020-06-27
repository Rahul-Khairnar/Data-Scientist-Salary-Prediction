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
    
    elif "data engineer" in job_title.lower() or "data modeler" in job_title.lower():
        return "Data Engineer"
    
    elif "data analyst" in job_title.lower() or "analyst" in job_title.lower() or "analytics" in job_title.lower() or "analysis" in job_title.lower():
        return "Data Analyst"
    
    elif "machine learning" in job_title.lower():
        return "Machine Learning Engineer"
    
    elif "medical" in job_title.lower() or "medicine" in job_title.lower() or "clinical" in job_title.lower():
        return "Analyst- Medicine"
  
    elif "manager" in job_title.lower():
        return "Manager";
    
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
print(df["Job_Titles_Simplified"].value_counts())

## CHECKING IF JOB TITLE HAS SENIOR OR JUNIOR MENTIONED IN IT AND SORTING IT
df["Title_Seniority"] = df["Job Title"].apply(title_seniority)

## STATE COLUMNS 
df["State"] = df["State"].apply(lambda x: x.strip() if x.strip().lower()!= "los angeles" else "CA")

## JOB DESCRIPTION LENGTH
def length(job_title):
    length_title = len(job_title)
    return length_title

df["Job_Description_Length"] = df["Job Description"].apply(length)

## COMPETITOR COUNT
def comp_count(competitors):
    if(competitors != "-1"):
        li_competitors = competitors.split(",")
        return len(li_competitors)
    else:
        return "0"
df["No. of Competitors"] = df["Competitors"].apply(comp_count)

## COMPANY NAME WITHOUT RATINGS
df["Company Name"] = df["Company Name"].apply(lambda x: x.split("\n")[0])

## TYPE OF OWNERSHIP
def ownership(type):
    if("public" in type.lower()):
        return "Public"
    elif("private" in type.lower()):
        return "Private"
    else:
        return type
df["Type of ownership"] = df["Type of ownership"].apply(ownership)


## RESOLVING THE PER HOUR PROBLEM
df["min_salary"] = df.apply(lambda x: x.min_salary*2 if x.Per_Hour == 1 else x.min_salary, axis = 1)
df["max_salary"] = df.apply(lambda x: x.max_salary*2 if x.Per_Hour == 1 else x.max_salary, axis = 1)

df["Avg_salary"] = df.apply(lambda x: (x.min_salary+x.max_salary)/2 if x.Per_Hour == 1 else x.Avg_salary, axis = 1)

## EXPORTING DATA TO CSV
df.to_csv("deep_clean_data.csv", index = False)


    