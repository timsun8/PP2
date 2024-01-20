# TOPIC - SYNTAX
print("Hello World")

if 5 > 2:
    print("YES")
# TOPIC - COMMENTS
# This is a comment

"""This is a comment
written in 
more than just one line"""
# TOPIC - VARIABLES
carname = "Volvo"

x = 50

x = 5
y = 10
print(x+y)

x = 5
y = 10
z = x + y
print(z)

x, y, z = "Orange", "Banana", "Cherry"

x = y = z = "Orange"

def myfunc():
    global x
    x = "fantastic"
# TOPIC - DATA TYPES
x = 5
print(type(x))
# answer is <class 'int'>

x = "Hello World"
print(type(x))
# answer is <class 'str'>

x = 20.5
print(type(x))
# answer is <class 'float'>

x = ["apple", "banana", "cherry"]
print(type(x))
# answer is <class 'list'>

x = ("apple", "banana", "cherry")
print(type(x))
# answer is <class 'tuple'>

x = {"name" : "John", "age" : 36}
print(type(x))
# answer is <class 'dict'>

x = True
print(type(x))
# answer is <class 'bool'>
# TOPIC - NUMBERS
x = 5
x = float(x)

x = 5.5
x = int(x)

x = 5
x = complex(x)
# TOPIC - STRINGS 
x = "Hello World"
print(len(x))

txt = "Hello World"
x = txt[0]

txt = "Hello World"
x = txt[2:5]

txt = " Hello World "
x = txt.strip()

txt = "Hello World"
txt = txt.upper()

txt = "Hello World"
txt = txt.lower()

txt = "Hello World"
txt = txt.replace("H", "J")

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))





