# Day 04: Lists in Python

# ------------------Typing Basics-------------------
numbers = [3, 5, 23, 53, 54, 22]
print("Numbers list:", numbers)
print("First number:", numbers[0])
print("Last number:", numbers[5])

total = 0
for num in numbers:
    print(num)
    total += num
print("Total of numbers:", total)

# ------------------Marks Example-------------------
marks = [87, 57, 44, 98, 54, 65]
total_marks = 0
for mark in marks:
    print(mark)
    total_marks += mark
print("Total marks:", total_marks)
print("Average marks:", total_marks / len(marks))

# ------------------Learned new thing-------------------
# len(obj) tells how many items are in a collection like list, string, tuple, dict(keys), or set

# ------------------Adding items to a list (append)-------------------
numbers2 = []
numbers2.append(34)
numbers2.append(65)
numbers2.append(97)
print("Numbers2 list after append:", numbers2)

# ------------------Interactive Example-------------------
number = []  # empty list to store numbers

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    number.append(num)

print("\nNumbers entered:", number)
print("Total numbers entered:", len(number))

# Finding the last index
highest_index = len(number) - 1
print("Index of the last element:", highest_index)

# ------------------Golden Rules-------------------
# If you want items → loop over items
# If you want positions → loop over indexes

# Core Insight:
# range() controls how many times the loop runs
# len(list) tells how much data you actually collected
# They are not the same thing

