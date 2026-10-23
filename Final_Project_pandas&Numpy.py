import numpy as np
import pandas as pd

students = pd.DataFrame({
    "student_id": [101, 102, 103, 104, 105, 106],
    "name": ["Ahmed", "Mona", "Ali", "Sara", "Omar", "Youssef"],
    "class": ["A", "A", "B", "B", "A", "B"],
    "math": [90, 75, 45, 88, 60, 98],
    "science": [85, 80, 50, 92, 65, 95],
    "english": [88, 70, 55, 85, 72, 90]
})

print(students)