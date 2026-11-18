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
#-----------------
# Duplicate
#--------
is_duplicated = df.duplicated().sum()
print('Sum of Duplicate : ' , is_duplicated)


