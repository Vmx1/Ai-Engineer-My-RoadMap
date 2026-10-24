import numpy as np #--> made by mahmoud sameh i wrote all of this without AI 10|24|2026 : 2:44M
import pandas as pd
#-------------------------
# Student Performance Analytics
#----------------
students = pd.DataFrame({
    "student_id": [101, 102, 103, 104, 105, 106],
    "name": ["Ahmed", "Mona", "Ali", "Sara", "Omar", "Youssef"],
    "class": ["A", "A", "B", "B", "A", "B"],
    "math": [90, 75, 45, 88, 60, 98],
    "science": [85, 80, 50, 92, 65, 95],
    "english": [88, 70, 55, 85, 72, 90]
})
#-----------------------
# [1] Numpy | First Step
#----------------------
# convert pandas to numpy 
#-----------
nmpy  = students[['math' , 'science' , 'english']].to_numpy() # from Dataframe pandas to numpy
print(np.mean(nmpy , axis=0)) # average score of each column
print(np.max(nmpy)) # max. score
print(np.min(nmpy)) # min. score
print(np.std(nmpy)) # بعد تشتت من المتوسط 
print(nmpy.reshape(1,-1)) # reshaping a columns and reshaping a rows automatic -1
print(nmpy.reshape(-1,1)) # reshaping a rows and reshaping a columns automatic -1
print(nmpy[[0 , 2 , 3]]) # boolen masking
print(nmpy[1]) # Indexing
print(nmpy.flatten()) # from 2Dim to 1Dim
print(nmpy[(nmpy >= 80) & (nmpy <= 70) ]) # boolen masking , nmpy >= 80 and nmpy =< 70
#------------------- 
# [2] pandas | Second Step -> groupby & agg
#---------
print(students.head(3))
print(students.tail(2))

classes = students.groupby('class').agg({ # Grouping all students in class A , B
    'math': ['mean' , 'min' , 'max'],
    'science': ['mean' , 'min' , 'max'],
    'english': ['mean' , 'min' , 'max']
})
print(classes)
#-------------
# continue
#---------
df = pd.DataFrame({
    "name": ["Ahmed", "Ali", "Omar", "Youssef", "Hassan"],
    "age": [20, 21, 19, 22, 20],
    "score": [85, 72, 95, 60, 88]
})
print(df.iloc[0]) # Index location
print(df.loc[0 , ['name' , 'score']]) # location by number with specific things : name , score
print(df.loc[(df['score'] >= 80)])
df['passed'] = df['score'] >= 70 # if score >= 70 : True else False
#--------------
# apply()
#---
def check_score(score) :
    if score >= 90 :
        return 'Execellent'
    elif score >= 80 :
        return 'Very Good'
    elif score >= 70 :
        return 'Good'

df['status'] = df['score'].apply(check_score).fillna('Bad') 
print(df.sort_values(['score'], ascending=False)) # from bigger to smaller

#-----------------
# merge & concat
#----

scores = pd.DataFrame({ # left
    "name": ["Ahmed", "Mona", "Ali"],
    "score": [95, 75, 50]
})

ages = pd.DataFrame({  # right
    "name": ["Ahmed", "Ali", "Sara"],
    "age": [19, 20, 22]
})

print(pd.merge(scores , ages , on='name' , how='outer').fillna('None'))

#-------
# Concat 
#----

group1 = pd.DataFrame({
    "name": ["Ahmed", "Mona"],
    "score": [95, 75]
})

group2 = pd.DataFrame({
    "name": ["Ali", "Sara"],
    "score": [50, 88]
})

print(pd.concat([group1 , group2] , ignore_index=True))
#-------------
# read csv , excel
#---

csv_data = pd.read_csv('students.csv') 
print(csv_data)


tops_student = csv_data[csv_data['score'] >= 80 ].sort_values(['score'] , ascending=False)
tops_student['status'] = tops_student['score'].apply(check_score)

tops_student.to_excel('top_students.xlsx' , index=False)

print(pd.read_excel('top_students.xlsx'))

#------------------------
# The End | First Step is Done :) 10|24|2026 at 4:02 AM  @Mahmoud Sameh 