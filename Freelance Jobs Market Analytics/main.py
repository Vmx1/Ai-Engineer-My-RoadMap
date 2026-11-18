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

print('Total Exper. level : ', df['experience_level'].value_counts())

print('Total Months : ', df['posted_month'].value_counts())
#-----------------------------------------------
# Stage 2
#--------