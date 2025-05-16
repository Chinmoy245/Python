# 15. Multiply all numbers in a list
def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# 16. Check if a number is perfect
def is_perfect(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num

# 17. Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

# 18. Check if a string is a pangram
import string
def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    return alphabet <= set(sentence.lower())

# 19. Sum of digits of a number
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# 20. Generate a list of four random numbers
import random

def generate_random_list():
    return [random.randint(1, 100) for _ in range(4)]
