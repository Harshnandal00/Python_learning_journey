# Day 03: Loops in Python
# Topics: for loop, while loop, break

# --------- FOR Loops ----------
print("For loop examples:")

# Simple loop from 0 to 4
for i in range(5):
    print(i)

# Loop from 1 to 5
for i in range(1, 6):
    print(i)

# Loop from 100 to 1000 with step of 100
for i in range(100, 1001, 100):
    print(i)

# Loop even numbers 0 to 20
for i in range(0, 21, 2):
    print(i)

# --------- WHILE Loops ----------
print("\nWhile loop examples:")

# Count from 1 to 10
count = 1
while count <= 10:
    print(count)
    count += 1

# Count down from 10 to 1
i = 10
while i > 0:
    print(i)
    i -= 1

# Even numbers using while
a = 0
while a <= 20:
    print(a)
    a += 2

# Infinite loop with break using 'q'
while True:
    value = input("Enter 'q' to quit or anything else to continue: ")
    if value.lower() == 'q':
        break
    print("You entered:", value)

# Infinite loop with break using a specific number
while True:
    number = int(input("Enter 2341 to quit or any other number: "))
    if number == 2341:
        break
    print("You entered:", number)
