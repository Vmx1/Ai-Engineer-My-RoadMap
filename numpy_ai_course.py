import numpy as np     #--> made by mahmoud sameh i wrote all of this without AI 10|1|2026 : 12:33AM
#----------------------
# some basics of numpy
#------------
a = np.array([
    [10,20,30,40],
    [50,60,70,80]  # np.shape = (r,c) : 2 , 4
    ])           # np.size = عدد البيانات اللي هي 8 عناصر
                # np.ndim = عدد الابعاد ... الخلاصة عدد ال[]
                # np.dtype = نوع البيانات هل int or bool or float

#-----------------
#Vector
#---------
a = np.array([10,20,30,40])
b = np.array([50,60,70,80])  # z = a + b : عبارة عن element wise multiplication يعني element_1 + element_2 = result

z = a @ b # dot = هي عبارة عن كل element_1 x element_2 + element_3 + element_4 = result 

#----------------
# Matrix
#---------

students = np.array([

    [19, 180, 60],
    [21, 175, 70],
    [20, 182, 75]
])

print(students[:,0])  # : يعني كل حاجة + الرقم اللي بعده
print(np.max(students)) # اقصى عنصر
print(np.min(students)) # اقل عنصر
print(np.std(students)) # مدى بعد التشتت عن المتوسط 
print(np.mean(students)) # يعني متوسط الاعمار هو 20 mean = a + b + c \ عددهم

#---------------
# Bonus 
#-----
products = np.array([
   [ 500, 4.5, 100],
   [700, 4.8 , 250],
   [700, 4.8 , 250],
])

print(np.shape(products))

# 100 | 100 done :)
#--------------------------
# Matrix multiplication vs elements wise multiplication
#--------
# الخلاصة في الماتريكس row x col. زي اللي كنا مذكرنها 
# z = a + b : عبارة عن element wise multiplication يعني element_1 + element_2 = result
#-------------
# standardization
a = np.array([10,20,30,40])

m = np.mean(a)

standard = a - m 

print(standard)

#--------
# Bonus 
#------
prices = np.array([500, 700, 450])

z = print(prices + 100)
z = print(prices * 2 )
print(prices[[0,1]] , 'MS')

data = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(data + 5)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

result = a @ b 

print(result)

#-------------------
# 100 | 100 done :)
#------------------
# reshape
#--------
# يعني تغيير ال(r,c) بس بشرط ان r x c = عدد العناصر
#--------
A = np.array([
    [1, 2],
    [3, 4]
])

print(A.reshape(1,-1)) # بتقول لnumpy -1 يعني احسب او اعملها تلقائياً
#--------------------
# Axis
#-----------
students = np.array([
    [19, 180, 60],
    [21, 175, 70],
    [20, 182, 75]
])

print(np.mean(students , axis=1)) # axis(0) نتيجة كل عمود , axis(1) نتيجة كل صف

#--------------
# Bonus
#-----
x = np.array([1, 2, 3, 4, 5, 6])
print(x.reshape(2,-1))

students = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(np.mean(students , axis=0))
print(np.mean(students , axis=1))
#---------------- 
# 100 | 100 done
#---------
# transpose , flatten ,reshape 
#------
print(np.transpose(students)) # transpose بيحول الrow to column
print(students.flatten()) # 2D -> 1D بيحول الماتريكس لفيكتور
print(students.reshape(-1,1)) # reshape (r , c)
#------------
# boolen masking
#----

prices = np.array([300, 500, 650, 800, 1000, 1200])
print(prices[(prices > 500 ) & (prices <= 1000)])
print(prices[(prices < 400 ) | (prices > 1000)]) # in numpy we dont use { and , or } , its { & , | }
 
premium = prices[prices >= 800 ]
print(premium)

scores = np.array([90, 75, 88, 60, 95, 70])
print(scores[[1,3,5]])
print(scores[[0,5]]) 

print(scores[scores > 80]) # the different is 1st one is for boolen masking to get each elements are bigger than 80 : [90 88 95] ,
print(scores[3]) # 2nd one is index list to get one element

#---------------
# 100 | 100 done
#-----------
# Random numbers 
#------
print('#' * 22)
# 1
x = np.random.randint(1, 100)

# 2
y = np.random.randint(1, 100, size=10)

# 3
z = np.random.randint(1, 100, size=(3, 3))


print(x)
print(y)
print(z)
#------------------------
# Numpy is Done :)
#--------
# Final Project of Numpy
#xoxoxoxoxoxoxoxoxoxoxoxox

students1 = np.array([
    [80, 90, 70],   # Ahmed
    [60, 75, 85],   # Ali
    [95, 88, 92],   # Omar
    [50, 65, 55]    # Youssef
])

average = np.mean(students1 , axis=1)
print(average)
print(np.mean(students1 , axis=0))
print(students1.max())
print(average[average >= 60])
print(average[average > 80])
print(students1.reshape(3,4))
print(average[[0 , 2]])

#------------------------
# 10 | 2 | 2026 11:41PM
#-----