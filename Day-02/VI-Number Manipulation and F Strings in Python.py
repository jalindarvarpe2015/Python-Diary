# Number Manipulation and F strings in Python

print(8 / 3)
# 2.6666666666666665

print(int(8/3))
# 2

print(round(8/3))
# 3

print(round(8/3, 2))
# 2.67

print(round(2.666666665, 2))
# 2.67

print(8 // 3)
# 2

print(type(8//3))
# <class 'int'>

print(4/2)
# 2.0

print(type(4/2))
# <class 'float'>

print(4//2)
# 2

print(type(4//2))
#2
#<class 'int'>



score = 0

# user score a point 

score += 1         # score = score + 1
print(score)
# 1


# F strings

scoree  = 0
height  = 1.8
isWinning = True

#f strings
print(f"your score is {scoree}, your heght is {height}, your winnins is {isWinning}")
# your score is 0, your heght is 1.8, your winnins is True

# without f strings
print("your score is ", scoree, "your heogth is ", height, "your winning is ", isWinning)
# your score is  0 your heogth is  1.8 your winning is  True