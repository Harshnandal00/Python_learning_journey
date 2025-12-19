# Write a python function which converts inches to cms 

# 1 inch = 2.54 centimeters (cm)

def convert(inches):
    cms = (inches / 2.54)
    print("The result after converting inches to cms is: ", cms)
    return "Thanx for using this software."
inches = float(input("Enter your number (inches): "))
d = convert(inches)