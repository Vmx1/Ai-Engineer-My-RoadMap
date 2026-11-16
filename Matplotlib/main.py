#--> made by mahmoud sameh i wrote all of this without AI 11|15|2026 : 8:22AM
import matplotlib.pyplot as plt
#------------------------
# First Plot 
#-----
study_hours = [1, 2, 3, 4, 5]
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
# grades = [45, 50, 55, 65, 68, 78, 85, 92]

# plt.scatter(study_hours , grades)
# plt.title('Student Evaluation')
# plt.xlabel('Study Hours')
# plt.ylabel('Grades')
# plt.show()
#--------
# Histogram Plot
#--------------------
# plt.hist(grades , bins=6)
# plt.title("Grades Distribution")
# plt.xlabel("Grades")
# plt.ylabel("Frequency")

#--------
# Subplots
#--------------------
fig , axes = plt.subplots(2,2)
# line plot
axes[0,0].plot(students , grades)
axes[0,0].set_title('Line Plot')
#----------
# bar plot
axes[0,1].bar(students , grades)
axes[0,1].set_title('Bar Plot')
# hist plot
axes[1,0].hist(grades , bins=5)
axes[1,0].set_title('Histogram Plot')
# scatter plot
axes[1,1].scatter(study_hours , grades)
axes[1,1].set_title('Scatter Plot')

plt.tight_layout()
plt.show()