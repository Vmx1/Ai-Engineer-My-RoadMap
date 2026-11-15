# This Maded By Mahmoud Sameh 11|15|2026 ....it taken so long time to finish the first step
# but its okay we still have a chance to be better :) Never Give UP
#------------------------
import pandas as pd 
import numpy as np
#----------
# Read Csv Files
csv_1 = pd.read_csv('customer.csv')
csv_2 = pd.read_csv('orders_q1.csv')
csv_3 = pd.read_csv('orders_q2.csv')
#-------------
# Info & Describe
#------
csv_1.info()
print(csv_1.describe())

csv_2.info()
print(csv_2.describe())

csv_3.info()
print(csv_3.describe())
#---------------------
# How many Row and Columns
#-----
numpy_cs1 = csv_1.to_numpy()
print(numpy_cs1.shape)
numpy_cs2 = csv_2.to_numpy()
print(numpy_cs2.shape)
numpy_cs3 = csv_3.to_numpy()
print(numpy_cs3.shape)
#----------
# Finding Missing Values
#------
print(csv_1.isna().sum())
print(csv_2.isna().sum())
print(csv_3.isna().sum()) 
#-------------
# Duplicate Rows
#-----
print(csv_1.duplicated().sum())
print(csv_2.duplicated().sum())
print(csv_3.duplicated().sum())
#----------------------
# Finding a client who not in customers csv
#-------
orders_1 = csv_2['customer_id']
orders_2 = csv_3['customer_id']

orders= pd.concat([orders_1 , orders_2] , ignore_index=True).unique()
orders = set(orders)

customers = csv_1['customer_id'].unique()
customers = set(customers)

print(orders - customers)


#----------------------
# 
#-------






#----------------------
#
#-------