# 21. Check if a number is even or odd
num = int(input("Enter a number: "))
print("Even" if num % 2 == 0 else "Odd")

# 22. Decimal equivalents of 1/2 to 1/10
for i in range(2, 11):
    print(f"1/{i} = {1/i}")

# 23. Display reversal of a number
num = int(input("Enter a number: "))
print("Reversed:", str(num)[::-1])

# 24. Find biggest among 3 numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Biggest number is:", max(a, b, c))

# 25. Countdown using while loop
n = int(input("Enter a number: "))
while n >= 0:
    print(n)
    n -= 1
