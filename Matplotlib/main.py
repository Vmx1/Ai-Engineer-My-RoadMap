#--> made by mahmoud sameh i wrote all of this without AI 11|15|2026 : 8:22AM
import matplotlib.pyplot as plt
#------------------------
# First Plot 
#-----

students = ["Ahmed", "Mona", "Ali", "Sara", "Omar"]

grades = [85, 92, 65, 78, 88]

plt.plot(students , grades)

plt.title('Student\'s Grade')

plt.xlabel('Student')
plt.ylabel('Grade')

#--------------
# Line Plot
#--------------------

plt.plot(
    students ,
    grades ,
    marker='o',
    linestyle = '--',
    linewidth = 3
)

plt.xlabel("students")
plt.ylabel("grades")

plt.show()

#--------
