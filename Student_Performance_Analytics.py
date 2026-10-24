import numpy as np  # --> made by mahmoud sameh i wrote all of this without AI 10|24|2026 : 4:50M
import pandas as pd
#-------------------
# Student Performance Analytics For Next Step
#-----------------------
students = pd.DataFrame({
    "student_id": [101, 102, 103, 104, 105, 106],
    "name": ["Ahmed", "Mona", "Ali", "Sara", "Omar", "Youssef"],
    "class": ["A", "A", "B", "B", "A", "B"],
    "math": [90, 75, 45, 88, 60, 98],
    "science": [85, 80, 50, 92, 65, 95],
    "english": [88, 70, 55, 85, 72, 90]
})
#-------------------
# First : average
#-------
np_data = students[['math' , 'science' , 'english']].to_numpy()
students['average'] = np.mean(np_data , axis=1) # 0 : column , 1 = row

best_average = students["average"].max()
best_student = students.loc[students["average"] ==  best_average , ['name' , 'average']] 

print(best_student)
#---------------
# ascending order
#------

print(students.sort_values("average" , ascending=True ,ignore_index=True))

#-----------
# Status
#-------
def check_score(score) :
    if score >= 90 :
        return 'Excellent'
    elif score >= 80 :
        return 'Very Good'
    elif score >= 70 :
        return 'Good'
    else :
        return 'Bad'
    
students['status'] = students['average'].apply(check_score)

print(students[['name' , 'average' , 'status']])

#------------------------