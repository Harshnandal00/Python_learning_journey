#  5.
# Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *
a = int(input("Enter your number: "))
def func1(a):
    if(a == 0):
        return
    print("*" * a)
    func1(a-1)
    
    
b = func1(a)