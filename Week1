#1.Print Hello World
print("Hello,World!")
#2.Sum of 2 numbers
num1= 2
num2= 4
sum= num1 + num2
print("The sum of",num1,"and",num2,"is",sum)
#3.Find the square of a number
def square(num):
    return num*num
print(square)
#4.Accpet the user name and greet them
name= input("Please enter your name:")
print("Greetings,",name)
#5.Check whether the number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
num = 7
print(f"The number {num} is {check_even_odd(num)}.")
#6.Write a Python program that takes a list and returns a new list with unique elements of the first list
def get_unique_elements(input_list):
    unique_elements = set()
    for element in input_list:
        unique_elements.add(element)
    return list(unique_elements)
input_list = [1, 2, 2, 3, 4, 4, 5]+
unique_list = get_unique_elements(input_list)
print("Original list:", input_list)
print("List with unique elements:", unique_list)
#7.Convert celsius into fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
celsius_temp = 25
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C is equal to {fahrenheit_temp}°F")
#8.Calculate the area of a circle.
import math
def area_of_circle(radius):
    return math.pi * radius ** 2
radius = 5
area = area_of_circle(radius)
print(f"The area of the circle with radius {radius} is {area:.2f}")
#9. Reverse a given string
def reverse_string(input_string):
    return input_string[::-1]
original_string = "Hello, world!"
reversed_string = reverse_string(original_string)
print(f"Original string: {original_string}")
print(f"Reversed string: {reversed_string}")
#10.Check if a number is a prime number.
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
num = 29
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
#11.Calculate the factorial of a number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = 5
result = factorial(num)
print(f"The factorial of {num} is {result}.")
#12.Find the largest item from a given list
def find_largest_item(input_list):
    if not input_list:
        return None
    largest_item = input_list[0]
    for item in input_list:
        if item > largest_item:
            largest_item = item
    return largest_item
input_list = [10, 3, 5, 67, 23, 98, 45]
largest_item = find_largest_item(input_list)
print(f"The largest item in the list is {largest_item}.")
#13.Write a Python program to check whether a number is in a given range.
def is_in_range(number, start, end):
    return start <= number <= end
num = 15
range_start = 10
range_end = 20
if is_in_range(num, range_start, range_end):
    print(f"{num} is in the range of {range_start} to {range_end}.")
else:
    print(f"{num} is not in the range of {range_start} to {range_end}.")
#14.Calculate the number of upper case letters and lower case letters in a string
def count_case(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    
    print("Uppercase letters:", upper_count)
    print("Lowercase letters:", lower_count)


string = input("Enter a string: ")
count_case(string)
