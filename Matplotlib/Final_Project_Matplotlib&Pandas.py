import pandas as pd
import matplotlib.pyplot as plt
#-----------------------------
# Pandas
#--------

data = {
    'student': [
        'Ahmed', 'Mona', 'Ali', 'Sara',
        'Omar', 'Youssef', 'Nour', 'Adam',
        'Salma', 'Karim', 'Jana', 'Ziad'
    ],

    'class': [
        'A', 'A', 'A', 'A',
        'B', 'B', 'B', 'B',
        'C', 'C', 'C', 'C'
    ],

    'math': [85, 92, 65, 78, 88, 98, 72, 55, 95, 60, 82, 74],

    'science': [90, 85, 70, 95, 80, 95, 78, 60, 92, 68, 88, 72],

    'english': [88, 90, 75, 85, 82, 90, 80, 65, 96, 72, 91, 78]
}

df = pd.DataFrame(data)
# print(df.shape)
# print(df.head(5))
# print(df.tail(5))
# print(df.dtypes)
# print(df.isna().sum())
# print(df.duplicated().sum())
# print(df.describe())
students_subjects = df[['math','science','english']]
total_average = students_subjects.mean(axis=1)
df['total_average'] = total_average
print(df.sort_values('total_average' , ascending=False , ignore_index=True))
print('Best Students : ',df.loc[(df['total_average'] >= 90) , ['student' , 'total_average']])
print('Bad Students : ',df.loc[(df['total_average'] < 70) , ['student' , 'total_average']])
#----------
classes = df.groupby('class')[['math' , 'science' , 'english']].mean()
total_classes = classes.mean(1)
best_class = total_classes.idxmax()
bad_class = total_classes.idxmin()
print(best_class)
print(bad_class)

def performce_student(score) :
    if score >= 90 :
        return 'Excellent'
    elif score >= 80 :
        return 'Very Good'
    elif score >= 70 :
        return 'Good'
    else  :
        return 'Bad'

df['performance'] = df['total_average'].apply(performce_student)
print(df)
#---------------------
# Matplotlib
#-------

fig , axes = plt.subplots(2,2 , figsize=(14,9))
fig.suptitle(
    'Student Performance Analytics',
    fontsize=16,
    fontweight='bold'
)
# Bar
df.plot(
    x='student' ,
    y='total_average',
    kind='bar' ,
    ax=axes[0,0],
    xlabel='Students',
    ylabel='Total Average',
    
)
# line
avg_subject = df[['math','science','english']].mean()
avg_subject.plot(
    kind='line',
    ax=axes[0,1],
    marker = 'o',
    color='red',
    linestyle='-.',
    xlabel='Subjects'
)
# Histogam
df.plot(
    x='total_average',
    kind='hist' ,
    ax=axes[1,0],
    bins=5,
    xlabel='Average Score',
    ylabel='Number of Students'
)
# scatter

df.plot(
    x='math',
    y='science',
    kind='scatter',
    ax=axes[1,1]
)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()