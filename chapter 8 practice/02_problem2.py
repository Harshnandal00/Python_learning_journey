# 2. Write a python program using function to convert(c to Fahrenheit.
#  formula to convert celcsius to Fahrenheit is : 

#                 F = ( C × 9/5 ) + 32


def convert_c_to_fahrenheit(c):
    f = ((c * 9/5)  + 32)
    print(f"Your tempurature in Fahrenheit is: ", f)
    return f
c = float(input("Enter the tempurature in c degree: "))

a = convert_c_to_fahrenheit(c)
