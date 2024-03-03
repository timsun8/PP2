import os
from string import ascii_uppercase

# 1
path = r'C:\Users\Timur\Desktop\PP2\Lab6'
print([name for name in os.listdir(path)]) #everything
print([name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]) # директории
print([name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name))]) # файлы


# 2
if os.path.exists(path):
    print("Путь существует")
else:
    print("Путь не существует")

if os.access(path, os.R_OK):
    print("Можно читать путь")
else:
    print("Невозможно читать путь")

if os.access(path, os.W_OK):
    print("Можно записывать в путь")
else:
    print("Невозможно записать в путь")

if os.access(path, os.X_OK):
    print("Можно создавать путь")
else:
    print("Невозможно создать путь")


# 3
if os.path.exists(path):
    head, tail = os.path.split(path)
    print(f"Имя файла: {tail}")
    print(f"Часть каталога: {head}")
else:
    print("Указанный путь не существует.")

# 4
with open(path, 'r') as file:
    line_count = sum(1 for line in file)

print(f'Количество строк в файле: {line_count}') 

# 5
mylist = ['A', 'B', 'C', 'D']

with open('C:\Users\Timur\Desktop\PP2\Lab6\demo.txt' , 'w') as file:
    for i in mylist:
        file.write(i + '\n')
file.close()

# 6
for char in ascii_uppercase:
    file = open('C:\Users\Timur\Desktop\PP2\Lab6\{fchar}'.format(fchar = char), 'x')
    file.close()

# 7

with open('C:\Users\Timur\Desktop\PP2\Lab6\demo.txt', 'r') as file1, open('/Users/ayaulymnurtaza/Downloads/lab6/dir-files/demofile2.txt', 'a') as file2:
  for line in file1:
    file2.write(line)

# 8
path = ''
path_bool = os.access(path, os.F_OK)

if path_bool == False:
    print("Не существует")

elif path_bool == True:
    os.remove(path)
    print("Удален")