#--> made by mahmoud sameh i wrote all of this without AI 11|15|2026 : 8:22AM
import matplotlib.pyplot as plt
#------------------------
# First Plot 
#-----

students = ["Ahmed", "Mona", "Ali", "Sara", "Omar"]

grades = [85, 92, 65, 78, 88]

# plt.plot(students , grades)

# plt.title('Student\'s Grade')

# plt.xlabel('Student')
# plt.ylabel('Grade')

#--------------
# Line Plot
#--------------------

# plt.plot(
#     students ,
#     grades ,
#     marker='o',
#     linestyle = '--',
#     linewidth = 3
# )

# plt.xlabel("students")
# plt.ylabel("grades")

#--------
# Bar Plot
#--------------------
# plt.bar(students , grades )
# plt.title('Student Grades')
# plt.xlabel('students')
# plt.ylabel('grades')
# plt.grid(axis="y")
# plt.show()

#--------
# scatter Plot
#--------------------
study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
grades = [45, 50, 55, 65, 68, 78, 85, 92]

plt.scatter(study_hours , grades)
plt.title('Student Evaluation')
plt.xlabel('Study Hours')
plt.ylabel('Grades')
plt.show()
#--------