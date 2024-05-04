num_char = len(input("enter your name"))
print("your name has" + num_char + " characters")

'''
enter your namejalindar
Traceback (most recent call last):
  File "/Users/A200281530/git/Python-Diary/Day-02/I-Primitive Data Types.py", line 2, in <module>
    print("your name has" + num_char + " characters")
TypeError: can only concatenate str (not "int") to str

'''

print(type(num_char))
# <class 'int'>

# can only concatenate str (not "int") to str
# for that you need to convert int datatypes into str first 


num_char = len(input("enter your name"))

new_num_char = str(num_char)

print("your name has jalindar" + new_num_char + " characters")
