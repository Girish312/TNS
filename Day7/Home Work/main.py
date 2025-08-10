# Write a program that takes a sentence and creates a dictionary with word counts.
"""
sentence = input("Enter a sentence: ").lower()
words = sentence.split()
wCount = {}

for word in words:
    if word in wCount:
        wCount[word] += 1
    else:
        wCount[word] = 1

print("Word counts:", wCount)
"""

# Write a program to map roll numbers to names using two lists and form a dictionary.
"""
roll_numbers = []
names = []

n = int(input("How many students:"))

for i in range(n):
    roll = int(input("Enter roll number: "))
    name = input("Enter name: ")
    roll_numbers.append(roll)
    names.append(name)

student_dict = {}

for i in range(n):
    student_dict[roll_numbers[i]] = names[i]

print("Roll number to name mapping:", student_dict)
"""

# Write a program that takes a dictionary of students and their marks, and prints the name(s) of the student(s) with the highest marks
"""
students = {"Girish": 85,"Devesh": 92,"Yash": 92,"Kartik": 88}

max_marks = 0
for marks in students.values():
    if marks > max_marks:
        max_marks = marks

print("Highest marks:", max_marks)
print("Student with highest marks:")

for name, marks in students.items():
    if marks == max_marks:
        print(name)
"""
