# 1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces
grams_amount = float(input())
ounces_result = grams_to_ounces(grams_amount)
print(ounces_result)

# 2
F = float(input("Введите температуру по Фаренгейту: "))
C = (5 / 9) * (F - 32)
print("Температура по Цельсию: ", C)

# 3
def solve(numheads, numlegs):
    for numrabbits in range(numheads + 1):
        numchickens = numheads - numrabbits
        if (4 * numrabbits + 2 * numchickens) == numlegs:
            return numrabbits, numchickens
    return 0
numheads = 35
numlegs = 94
result = solve(numheads, numlegs)
print(f"рабит: {result[0]}")
print(f"чикен: {result[1]}")
# 4
def filter_prime(numbers):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    return [num for num in numbers if is_prime(num)]
user_input = input("введите лист: ")
numbers = [int(num)for num in user_input.split()]
prime_numbers = filter_prime(numbers)
print(prime_numbers)
# 5
def generate_permutations(string):
    if len(string) == 0:
        return []
    elif len(string) == 1:
        return [string]
    else:
        permutations = []
        for i in range(len(string)):
            char = string[i]
            remaining_chars = string[:i] + string[i+1:]
            for permutation in generate_permutations(remaining_chars):
                permutations.append(char + permutation)
        return permutations
# Example usage
user_input = input()
permutations = generate_permutations(user_input)
print(permutations)
# 6
def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence
sentence = "We are ready"
reversed_sentence = reverse_sentence(sentence)
print(reversed_sentence)
# 7
def has_33(nums):
    pass
has_33([1, 3, 3]) # True
has_33([1, 3, 1, 3]) # False
has_33([3, 1, 3]) # False
# 8
def check_007(lst):
    for i in range(len(lst) - 2):
        if lst[i] == 0 and lst[i+1] == 0 and lst[i+2] == 7:
            return True
    return False
numbers = [1, 2, 0, 0, 7, 8, 9]
result = check_007(numbers)
print(result)  # True
# 9
def calculate_sphere_volume(radius):
    pi = 3.14159
    volume = (4/3) * pi * (radius ** 3)
    return volume
radius = 5
volume = calculate_sphere_volume(radius)
print(f"The volume of a sphere with radius {radius} is {volume}.")
# 10
def get_unique_elements(lst):
    unique_lst = []
    for element in lst:
        if element not in unique_lst:
            unique_lst.append(element)
    return unique_lst
# 11
def is_palindrome(word):
    word = word.lower()
    return word == word[::-1]

print(is_palindrome("madam"))
print(is_palindrome("hello"))
# 12
def histogram(numbers):
    for num in numbers:
        print('*' * num)

numbers = [4, 9, 7]
histogram(numbers)
# 13
import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    secret_number = random.randint(1, 20)
    guesses_taken = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break

guess_the_number()