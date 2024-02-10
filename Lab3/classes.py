# 1
class Number:
    # def __init__(self, num):
    #     self.num = num
    def get_String(self, num):
        self.num = num
    def printString(self):
        print(self.num.upper())
        
num = Number()
num.get_String(input())
num.printString()
# 2
class Shape:
    def area(self):
        print(0)

class Square(Shape):
    def __init__(self, length):
        self.length = length  
    def area(self):
        self.area = self.length ** 2
        print(self.area)

length = Square(int(input()))
length.area()
# 3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width  
    def area(self):
        self.area = self.length * self.width
        print(self.area)

area = Rectangle(int(input()), int(input()))
area.area()
# 4
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other_point):
        distance = math.sqrt((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2)
        print(distance)
# 5
class Bank:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, dep):
        self.dep = dep
        self.balance += self.dep
    def withdraw(self, wit):
        self.wit = wit
        if self.balance - self.wit < 0:
            print("Not enough money")
        else:
            self.balance -= self.wit
            print("ur balance:", self.balance)

u1 = Bank(input(),int(input()))
u1.deposit(int(input()))
u1.withdraw(int(input()))

u2 = Bank(input(),int(input()))
u2.deposit(int(input()))
u2.withdraw(int(input()))

u3 = Bank(input(),int(input()))
u3.deposit(int(input()))
u3.withdraw(int(input()))

# 6 
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print(prime_numbers)

