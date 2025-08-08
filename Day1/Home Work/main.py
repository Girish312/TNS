# Write a program that takes the radius as input and calculates the area and circumference of a circle.
# Formula: Area = 3.14 × r × r & Circumference = 2 × 3.14 × r
"""
radius = int(input("Enter the radius of the circle: "))

area = 3.14 * radius ** 2
circumference = 2 * 3.14 * radius

print(f"Area: {area}")
print(f"circumference: {circumference}")
"""

# Write a program to check if a number is divisible by both 3 and 5.
"""
num= int(input("Enter your number: "))
if num % 3 == 0 and num % 5 == 0:
    print("The number is divisible by both 3 and 5.")
else:
    print("The number is NOT divisible by both 3 and 5.")
"""

# Write a program that takes a 4-digit number from the user and prints the sum of its digits.
"""
num= input("Enter a 4 digit number: ")
total=0

for i in num:
    total += int(i)
print("Sum of digits is:", total)
"""