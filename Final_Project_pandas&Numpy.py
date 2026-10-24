import numpy as np #--> made by mahmoud sameh i wrote all of this without AI 10|24|2026 : 2:44M
import pandas as pd
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
#-------------------
# [2] pandas | Second Step -> groupby & agg
#---------
classes = students.groupby('class').agg({
    'math': ['mean' , 'min' , 'max'],
    'science': ['mean' , 'min' , 'max'],
    'english': ['mean' , 'min' , 'max']
})
print(classes)
#-------------
# continue
#---------
