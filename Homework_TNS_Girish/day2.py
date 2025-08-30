# Write a program to print the factorial of a number using a for loop.
"""
num = int(input("Enter your number: "))
fact= 1

for i in range(1, num+1): 
    fact *= i
print(f"Factorial of {num} is: {fact}")
"""

# Write program that prints all numbers from 1 to 100 that are divisible by 7 but not a multiple of 5
"""
for i in range(1, 101):
    if i % 7 == 0 and i % 5 != 0:
        print(i)
"""

# Write a program that takes a number and prints whether it is a palindrome or not.
"""
num = input("Enter a number: ")
revNum = num [::-1] # num[start:stop:step] 
if num == revNum:
    print("It is a palindrome.")
else:
    print("It's not a palindrome.")
"""