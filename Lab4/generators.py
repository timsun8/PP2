# 1
def squares_generator(N):
    for i in range(1, N+1):
        yield i*i

N = int(input())

for square in squares_generator(N):
    print(square)
# 2
def even_separate(n):
    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

n = int(input())

print(*even_separate(n), sep=", ")
# 3 
def divisible_by_3_4(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())

for num in divisible_by_3_4(n):
    print(num)
# 4
def squares(a, b):
    for i in range(a, b+1):
        yield i*i

a = int(input())
b = int(input())

for num in squares(a, b):
    print(num)
# 5
def return_to_0(n):
        while n >= 0:
            yield n
            n -= 1

n = int(input())

for num in return_to_0(n):
      print(num)
