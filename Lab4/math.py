# 1
import math

degree = int(input())

print(math.radians(degree))
# 2
import math

height = int(input())
base1 = int(input())
base2 = int(input())

area = ((base1 + base2)/2) * height

print(area)
# 3
import math

num_of_sides = int(input())
length = int(input())

area = (num_of_sides * length**2) / (4 * math.tan(math.pi / num_of_sides))

print(area)
# 4
import math

length = float(input())
height = float(input())

area = length * height

print(area)