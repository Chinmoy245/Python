# 26. Sum of 2 numbers using command line arguments
import sys
a = int(sys.argv[1])
b = int(sys.argv[2])
print("Sum =", a + b)

# 27. Usage of various operators
a = 10
b = 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

# 28. Check eligibility for voting
age = int(input("Enter age: "))
print("Eligible for voting" if age >= 18 else "Not eligible")

# 29. Check leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
