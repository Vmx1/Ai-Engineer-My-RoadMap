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
print(df.dtypes)
print(df.info())
#-----------------
# Duplicate
#--------
is_empty = df.isna().sum()
print('Is there empty values : ' , is_empty)
is_duplicated_rows = df.duplicated().sum()
print('Sum of Duplicate : ' , is_duplicated_rows)
is_duplicated_ids = df.duplicated('project_id').sum()
print('Sum of Duplicate : ' , is_duplicated_ids)
#--------------------------
# unique , value count , nunique
#----------
print(df['platform'].unique())
print(df['platform'].nunique())
print(df['platform'].value_counts())
#---------------------------
# Statistical Inspection
#-----------
print(df.describe())
print(df.describe(include='object'))
max_salary = df['budget_usd'].max()
min_salary = df['budget_usd'].min()
average_salary = df['budget_usd'].mean()
print(max_salary)
print(min_salary)
print(average_salary)