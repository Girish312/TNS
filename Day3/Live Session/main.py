"""
# iterating over a sequence or any iterable object. It's ideal when the number of iterations is known or determined by the size of the sequence.
for i in range(0,6):
    print("Hello World")

# repeatedly executing a block of code as long as a specified condition remains True. It's suitable when the number of iterations is not known beforehand and depends on a dynamic condition.
i=0
while (i<5):
    print("Hello World")
    i+=2

for i in range(5):
    print("Runs 5 times")
    for j in range(6):
        print("Runs 6 times")
        for x in range(2):
            print("Runs 2 times")
"""

"""
def greet():
    print("Hello Girish")
greet()
"""

"""
a = 10
def ageChecking ():
    if (a<18):
        for i in range(5):
            print("Under Age- Warning")
    else:
        print("Approved")

ageChecking()
"""