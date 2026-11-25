import pandas as pd
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
# Filtering Data

top_skills = []

for s in clean_df['Skills']:
    for skill in s.split('\n') :
        top_skills.append(skill)
#----------------------
skills = pd.Series(top_skills)

skills_compare = skills.value_counts().head(8)

clean_df['Salarys'] = (clean_df['Salarys'].str.replace('$' , '' ,).str.replace('.00' , '').str.replace(',' , ''))

clean_df['Salarys'] = pd.to_numeric(clean_df['Salarys'] , errors='coerce')

max_salary = clean_df['Salarys'].max()
average_salary = clean_df['Salarys'].mean()
min_salary = clean_df['Salarys'].min()


top_project =clean_df.loc[(clean_df['Salarys'] >= 1500 ) , ['Titles' , 'Salarys' , 'Proposals']].sort_values('Salarys',ascending=False , ignore_index=True)

#-----------------------------
# report
#------
print('[1] Best Tech Skills' , skills_compare)
print('[2] Max Salary' , max_salary)
print('[3] Avg. Salary' , average_salary)
print('[4] Min Salary' , min_salary)
print('[5] Top Projects' , top_project)
