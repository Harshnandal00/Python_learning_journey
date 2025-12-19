##  Write a program to print multiplication table of n
# using for loops in reversed order.??

table = int(input("Enter your number: "))

for no in range(-10, 0):
    print(f"{table} x {-no} = {table*(-no)}")


