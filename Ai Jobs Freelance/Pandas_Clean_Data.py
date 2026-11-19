import pandas as pd
import matplotlib.pyplot as plt
#----------------
# load data
df = pd.read_csv(r'Ai Jobs Freelance/freelance_ai_jobs.csv')
clean_df = df.copy()
# Cleaning Data
clean_df = clean_df.drop('Links' , axis=1)
clean_df = clean_df.drop('Descriptions' , axis=1)
clean_df = clean_df.drop('Posted_Dates' , axis=1)
clean_df = clean_df.drop('Owners' , axis=1)


#-------------------------------

top_skills = []

for s in clean_df['Skills']:
    for skill in s.split('\n') :
        top_skills.append(skill)

skills = pd.Series(top_skills)

skills_compare = skills.value_counts().head(8)
print(skills_compare)

clean_df['Salarys'] = (clean_df['Salarys'].str.replace('$' , '' ,).str.replace('.00' , '').str.replace(',' , ''))

clean_df['Salarys'] = pd.to_numeric(clean_df['Salarys'] , errors='coerce')

max_salary = clean_df['Salarys'].max()
average_salary = clean_df['Salarys'].mean()
min_salary = clean_df['Salarys'].min()

print(max_salary)
print(average_salary)
print(min_salary)