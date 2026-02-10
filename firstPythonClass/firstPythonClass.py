### ---------------- 1 se N tak prime numbers print karo ------------------- ###
number = int(input("Enter a number: "))

for i in range(2, number + 1):
    # Check if i is prime
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, "is a prime")


####### ------- Check if the given number is an Armstrong number ------- #######
number = int(input("Enter a number: "))
num = number  # Save original number
arr = []

# Extract digits
while num > 0:
    digit = num % 10
    arr.append(digit)
    num = num // 10

# Calculate sum of digits raised to power of number of digits
result1 = 0
n = len(arr)
for x in arr:
    result1 += x ** n

# Check Armstrong
if result1 == number:
    print(number, "is an Armstrong number")
else:
    print(number, "is NOT an Armstrong number")


####### ------- Calculate power of a number ------- #######
base = int(input("Enter base: "))
power = int(input("Enter power: "))
result = 1

for i in range(power):
    result *= base

print(f"{base}^{power} = {result}")


####### ------- Check if a number is prime using sqrt optimization ------- #######
import math

num = int(input("Enter number to check prime: "))
if num <= 1:
    print(num, "is not a prime number")
else:
    is_not_prime = False
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            is_not_prime = True
            break

    if is_not_prime:
        print(num, "is NOT a prime number")
    else:
        print(num, "is a prime number")


####### ------- Sum of odd numbers from 1 to N ------- #######
num = int(input("Enter number to sum odd numbers up to: "))
sum_odd = 0

for i in range(1, num + 1):
    if i % 2 != 0:
        sum_odd += i

print("Sum of odd numbers from 1 to", num, "is:", sum_odd)


####### ------- Factorial calculation (example for 5!) ------- #######
res = 1
for x in range(5, 1, -1):
    res *= x
print("5! =", res)


####### ------- Fibonacci series ------- #######
a, b = 0, 1
num = int(input("How many Fibonacci terms to print? "))
for i in range(num):
    print(a, end=" ")
    a, b = b, a + b
print()


####### ------- Working with lists example ------- #######
myList = [10, 20, 30, 40, 50]
for x in myList:
    print(x)

names = ["Jahangir", "Ali", "Khaskheli", "Muhammad", "Younis"]
print("4th name in list:", names[3])
