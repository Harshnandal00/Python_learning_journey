# Write a python function to print multiplication table of a given number.

def table(n):
    for i in range(0 , 20):
        i += 1
        print(f"{n} x {i} = {n * i}")
    return "table complete"

n = int(input("Enter your number: "))
t = table(n)