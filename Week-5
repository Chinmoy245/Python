# 30. Generate first N natural numbers
n = int(input("Enter N: "))
for i in range(1, n+1):
    print(i, end=' ')

# 31. Check if number is palindrome
num = input("Enter a number: ")
print("Palindrome" if num == num[::-1] else "Not Palindrome")

# 32. Factorial of a number
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

n = int(input("Enter number: "))
print("Factorial:", factorial(n))

# 33. Sum of N natural numbers
n = int(input("Enter N: "))
print("Sum:", n * (n + 1) // 2)

# 34. Check Armstrong number
num = int(input("Enter a number: "))
sum_of_powers = sum(int(digit) ** len(str(num)) for digit in str(num))
print("Armstrong Number" if num == sum_of_powers else "Not Armstrong Number")

# 35. Generate prime numbers up to n
n = int(input("Enter n: "))
for num in range(2, n+1):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            break
    else:
        print(num, end=' ')
