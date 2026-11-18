# Maded By Mahmoud Sameh 11|18|2026 without AI
#____________________________________________
import pandas as pd
import numpy as np
import matplotlib as plot
#------------------------
# Read Csv 
#--------
df = pd.read_csv(r'c:\Users\mohan\Downloads\freelance_tech_market_100_synthetic.csv')
#-----------------
# Structural Inspection
#------
print(df.head(5))
print(df.tail(5))
r , c = df.shape
print('Rows : ' , r)
print('Columns : ' , c)
print(df.columns)
print(df.dtypes)
df.info()
#-----------------
# Duplicate
#--------
missing_value = df.isna().sum()
print('Is there empty values : ' , missing_value)
is_duplicated_rows = df.duplicated().sum()
print('Sum of Duplicate : ' , is_duplicated_rows)
is_duplicated_ids = df.duplicated('project_id').sum()
print('Sum of Duplicate Project ID : ' , is_duplicated_ids)
#--------------------------
# unique , value count , nunique
#----------
print(df['platform'].unique())
print(df['skill'].unique())
print(df['posted_month'].unique())
print(df['data_type'].unique())
print(df['specialty'].unique())
print(df['experience_level'].unique())
print(df['platform'].value_counts())
print(df['experience_level'].value_counts())
print(df['specialty'].value_counts())
#---------------------------
# Statistical Inspection
#-----------
print(df.describe())
print(df.describe(include='object'))
max_salary = df['budget_usd'].max()
min_salary = df['budget_usd'].min()
average_salary = df['budget_usd'].mean()
median_salary = df['budget_usd'].median()
print('Max. Salary : ' ,max_salary)
print('Min. Salary : ' ,min_salary)
print('Average Salary : ' , average_salary)
print('Median Salary : ' , median_salary)
#----------------------
# Distribution Inspection
#-----------
total_projects = df['specialty'].value_counts()

print('Total Project : ', total_projects)

print('Total Platform Projects : ', df['platform'].value_counts())

print('Unique Experience Levels : ', df['experience_level'].unique())

print('Total Exper. level : ', df['experience_level'].value_counts())

print('Total Months : ', df['posted_month'].value_counts())
#-----------------------------------------------
# Stage 2
#--------
clean_df = df.copy() # New DF
print(clean_df.dtypes)
#------
# Value Validation
#-----------------
print((clean_df['budget_usd'] <= 0).sum())
print((clean_df['applicants_or_sellers_signal'] < 0).sum())
print((clean_df['illustrative_demand_weight'] < 0).sum())

valid_platform = ['Upwork', 'Fiverr', 'Freelancer']
invalid_platforms = (~clean_df['platform'].isin(valid_platform)).sum()
print('Invalid Platforms:', invalid_platforms)

valid_levels = ['Entry', 'Intermediate', 'Expert']
invalid_levels = (~clean_df['experience_level'].isin(valid_levels)).sum()
print('Invalid Levels:', invalid_levels)

clean_df['posted_month'] = pd.to_datetime(clean_df['posted_month'] , format='%Y-%m' , errors='coerce') 
invalid_dates = clean_df['posted_month'].isna().sum()
print(invalid_dates)
#------------------
# Data Cleaning
#--------
print(clean_df) # لا يوجد أي مشكلة ابداً ولن احذف أي بيانات 

print(clean_df.shape)
#-------------------------

missing_value = clean_df.isna().sum()
print('Sum of Missing Values : ' , missing_value)


is_duplicated = clean_df.duplicated().sum()
print('Sum of Duplicate Rows : ' , is_duplicated)


is_duplicated_ids = clean_df.duplicated('project_id').sum()
print('Sum of Duplicate Project ID : ' , is_duplicated_ids)

#------------------------

clean_df.to_csv('clean_freelance_market.csv' , index=False)

#------------------------------
# Stage 3
#---------
# Specialty Analysis

for c in clean_df['specialty'].value_counts():
    percentage = c / clean_df['specialty'].value_counts().sum() * 100
    print(percentage)

#-------------------

