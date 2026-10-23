import pandas as pd #--> made by mahmoud sameh i wrote all of this without AI 10|2|2026 : 11:56M
#-------------------
# some basics of pandas
#-----------
# DataFrame -> table like excel
#-------
df = pd.DataFrame({
    "name": ["Ahmed", "Ali", "Omar", "Youssef", "Hassan"],
    "age": [20, 21, 19, 22, 20],
    "score": [85, 72, 95, 60, 88]
})
print(df[['score']])
print(df.head(5)) # هات اول خمس بيانات
print(df.tail(5)) # هات اخر خمس بيانات
print(df[['name','score'] ])
#--------------------------------
# Boolen masking زي اللي في numpy (Filtering)
#------------------------
# Bonus 
#-----
print(df[df['score'] > 80])
print(df[df['age'] < 21])
print(df[(df['score'] >= 70) & (df['age'] <= 20)])
print(df[(df['score'] < 70) | (df['age'] > 21)])
print('xo' * 20)
#---------
# 100 | 100 done :)
#----
# iloc vs loc -> iloc = index location & loc = position and label
#-----------
print(df.loc[2])
print(df.iloc[3])
print(df.loc[2 , 'score'])
print(df.loc[df['age'] <= 20 , ['name' , 'age']])
print('xo' * 20)
#------------------
print(df.sort_values(['name' , 'age'] , ascending=[False , True])) # from bigger to smaller
df2 = df.rename(columns={'score':'f'}) # rename column's name
print(df2)

# ----------------------
# bonus 
#------

df["passed"] = df["score"] >= 70

top_student = df.loc[df['score'] >= 80 , ["name","score"]]
print(top_student)

without_age = df.drop(columns='age')
print(without_age)

new_column = df.rename(columns={
    'score':'grade'
})
print(new_column)

final_df = df.loc[(df['score'] >=80) & (df['age'] <= 20) , ["name","age","score","passed"]]
print(final_df)

# Missing value & Duplicates    
#----------------


df_clean = pd.DataFrame({
    "name": ["Ahmed", "Ali", "Omar", "Youssef", "Hassan", "Mona"],
    "age": [20, 21, None, 22, 20, None],
    "score": [85, None, 95, 60, None, 88],
    "city": ["Cairo", "Alex", "Cairo", None, "Giza", "Alex"]
})

print(df_clean.isna().sum() ) # عدد القيم الفارغة
print(df_clean.dropna()) # شيل الصفوف و الاعمدة اللي تحتوي على none
print(df_clean.dropna(subset=['score'])) # حذف الصفوف اللي الدرجة فيها مفقودة فقط
df_clean["city"] = df_clean["city"].fillna("Unknown") # تعويض القيم الفارغة بقيمة اخرى
#-----------------
# Duplicates 
#------

df_dup = pd.DataFrame({
    "name": ["Ahmed", "Ali", "Ahmed", "Omar", "Ali"],
    "score": [85, 72, 85, 95, 72],
    "city": ["Cairo", "Alex", "Cairo", "Giza", "Alex"]
})

df_dup.duplicated() # كشف التكرار 
print(df_dup.duplicated(subset=['name' , 'score']))# كشف التكرار في اعمدة معين
df_unique = df_dup.drop_duplicates() # بتحذف اخر ظهور من البيانات 
df_unique = df_dup.drop_duplicates(keep='last') # بتحذف اول ظهور من البيانات 

#----------------------
# aggregation & GroupBy
#--------
print('#################')

df = pd.DataFrame({
    "name": ["Ahmed", "Ali", "Mona", "Omar", "Sara", "Youssef"],
    "class": ["A", "B", "A", "B", "A", "A"],
    "score": [80, 90, 70, 60, 100, 85],
    "passed": [True, True, True, False, True, True]
})

# هنجمع كل اللي في فصل A و هنخليهم في فصل واحد كذلك في فصل B
print(df.groupby('class').agg({ # هنحسب الداتا ازاي أو اضافة خصائص مثل اكبر و متوسط و اصغرالبيانات 
    'score' : ['max'] 
}))
#----------------------
# Bonus
#------
print(df.groupby(['class' , 'passed']).agg({
    'score' : ['max','mean']
}
))
#-----------
# apply () يعني تطبيق شرط على البيانات قبل اضافتها
#-----------------
df = pd.DataFrame({
    "name": ["Ahmed", "Mona", "Ali", "Sara", "Omar"],
    "score": [95, 75, 50, 88, 65]
})

def check_score(score):
    if score >= 70 :
        return 'Passed'

    elif score < 70 :
        return 'Failed'

df['status'] = df['score'].apply(check_score)

print(df)

#-------------------
# merge and concat
#------

scores = pd.DataFrame({ # left
    "name": ["Ahmed", "Mona", "Ali"],
    "score": [95, 75, 50]
})

ages = pd.DataFrame({  # right
    "name": ["Ahmed", "Ali", "Sara"],
    "age": [19, 20, 22]
})

print(pd.merge(scores, ages, on="name", how="right"))  # بكل اختصار هي عبارة عن ربط البيانات بسويط مشترك مثل الاسم 
# right يعني ثبت دول عشان الاهم و ادمج باقي الجدول الاخر 
# left يعني ثبت دول عشان الاهم و ادمج باقي الجدول الاخر 
# inner لازم تطابق يعني لو اسم في جدول الاول مش موجود في التاني يتجاهلوا
# outer ادمج كلو على بعضه مش شرط تطابق , واذا عدم توفر بيانات بيكتب nan
#--------------------------------------------------------------------------
# concat 
#--------
# باختصار دي اضافة صفوف و اعمدة  
print('#' *20)
group1 = pd.DataFrame({
    "name": ["Ahmed", "Mona"],
    "score": [95, 75]
})

group2 = pd.DataFrame({
    "name": ["Ali", "Sara"],
    "score": [50, 88]
})


result = pd.concat([group1 , group2] , ignore_index=True )
 # دمج جدول الاول بالتاني دون الحاجة لوسيط مشترك , هيضيف الجدول التاني في شكل صف
 # axis = 0 (default) => row
print(result)

#---------------

names = pd.DataFrame({
    "name": ["Ahmed", "Mona", "Ali"]
})

scores_only = pd.DataFrame({
    "score": [95, 75, 50]
})

result = pd.concat([names , scores_only] , 
                   axis=1)  # هنا عمل اضافة الجدول في شكل عمود
# axis = 1 --> column
print(result)

#-------------------------
# read csv , read execl
#------
print('_' * 20)
data = pd.read_csv('students.csv') # read csv as dataframe
data['passed'] = data['score'] >= 70 # adding a new column
data.to_csv('students_result.csv' , index=False) # save changes 

top_student = data[data['score']] >= 80 # boolen masking
top_student.to_excel('top_students.xlsx')
