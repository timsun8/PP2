if 5 > 2:
  print("Five is greater than two!")
# Python will give you an error if you skip the indentation
# You have to use the same number of spaces in the same block of code, otherwise Python will give you an error

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Illegal variable names:Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

x = 1    # int
y = 2.8  # float
z = 1j   # complex

x = str("s1") # x will be 's1'
y = int(2.8) # y will be 2
z = float("3")   # z will be 3.0

for x in "banana":
    print(x)

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

b = "Hello, World!"
print(b[2:5])

a = "Hello, World!"
print(a.upper())
print(a.lower())

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))


