## Data Scientist Salary Prediction: Project Overview
* Created a tool that estimates the salary that a particular Data Scientist role should get.   This will help the data scientists to negotiate their income during job interviews.
* Worked on a dataset of about 1000 job descriptions from glassdoors.com using python selenium.
* Did data mining on the dataset gathered and looked out for keywords like Python, R, Excel,   Spark, AWS to get the prediction of the salaries as accurate as possible and reduce the       error.
* Created models like Random Forest, Multiple Linear Regression and Lasso Regression.
* Used GridSearchCV to optimize the performance of the model by tuning the parameters.
* Implemented the client facing API using Flask.


## Resources Used and Referred to 
**Python Version:** 3.7  
**Spider IDE:** 4.1.3
**Packages:** Pandas, Numpy, Sklearn, Matplotlib, Seaborn, Flask, Json, Pickle, Requests  
**For Web Framework Requirements:**  ```pip install -r requirements.txt```    
**Flask Productionization:** https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2

## About the Dataset
The dataset consiseted of the following rows for about 1000 different job openings across various states of the United States of America:
* Job Title
* Salary Estimate
* Job Description
* Rating
* Company
* Location
* Company Headquarters
* Company Size
* Company Fouded Date
* Type of Ownership
* Industry
* Sector
* Revenue
* Competitors

## Data Cleaning
After getting the dataset, I cleaned the dataset so that it was more usable for getting insights. The cleaning included:

* Parsed only the numeric values out of salary.
* Parsed the salary column hourly wages if was provided by the employer in the job description.
* Removed rows without salary
* Parsed the rating of company name column
* Made new columns for job locations based on cities and states
* Checked if the job opening was in the same state as the company's headquarters and made a new column for it
* Calculated age of the company from the dat of founding.
* Made columns for different skills if those were mentioned in the Job Description column. Skills parsed were:
    * Python
    * R
    * Excel
    * AWS
    * Spark
* Grouped various data titles into 7 major categories:
    * Data Scientist
    * Data Engineer
    * Analyst
    * Machine Learning Engineer
    * Director
    * Other titles(Titles which were ver few in number)
* Checked for the seniority of the title and grouped all titles into 3 categories
    * Senior
    * Junior
    * Not Mentioned
* Calculated the length of Job Description as provided by the employer

## Exploratory Data Analysis
I tried to get insights by doing EDA from the data set obtained after cleaning the original dataset. I created pivot tables, heat maps, bar charts, histograms etc. for seeing the distribution of the data and to check the dependency of one column on the other. Below are some highlights of the EDA performed:

![alt text](https://github.com/Rahul-Khairnar/Data-Scientist-Salary-Prediction/blob/master/EDA_Photos/City_bar.png "Job roles in various Cities")


![alt text](https://github.com/Rahul-Khairnar/Data-Scientist-Salary-Prediction/blob/master/EDA_Photos/Heat_amp.png "Dependency of numeric columns on one another")


![alt text](https://github.com/Rahul-Khairnar/Data-Scientist-Salary-Prediction/blob/master/EDA_Photos/Pivot_table.PNG "Pivot tables to show title seniority in various job roles")

## Model Building

First I transformed the whole data into dummy variables. The whole data was split into 70-30% ratio for train and test data sets respectively. 

Based on our exploratory data analysis, I tried three different models just to compare the results and see which one suits the best and can be used. I calculated Mean Absolute Error because it is easy to intrepret and outliers have minimum effect on MAE. 

The three different models used were:
**Multiple Linear Regression:** This was the baseline for comparing results.
**Lasso Regression:** This was used because the data is normalized.
**Random Forests:** This was used because our datasets have values particularly in 0s and 1s. Hence it was obvious to be the perfect fit for our dataset.

## Model Performances
The best performing model out of the three we had chosen was Random Forests. It outperformed the other models in both test and validation datasets.

**Random Forest:** MAE = 11.079229345059012
**Multiple Linear Regression:** MAE = 19.921946173173083
**Lasso Regression:** MAE = 18.94859522551425

![alt text](https://github.com/Rahul-Khairnar/Data-Scientist-Salary-Prediction/blob/master/Model_performance.PNG "Performances of all Models")

## Productionization

In this step, I built a Flask End point API which was hosted on the local webserver by following the TDS tutorial. The turorial was referred from the link mentiond in the resources section. A list of parameters was passed using the request formed by using the request module and we obtained the predicted salary in the output window of spider.
