# #  1.Write a program using functions to find greatest of three numbers?

def find_greatest_no():
    a = int(input("Enter your number: "))
    b = int(input("Enter your number: "))
    c = int(input("Enter your number: "))
    if(a>b and a>c):
        print("The greatest number is 'a' = ", a)
    elif(b>a and b>c):
        print("The greatest number is 'b' = ", b)
    elif(c>a and c>b):
        print("The greatest number is 'c' = ", c)
    
    elif(a == c and a>b):
        print("'a' and 'c' both numbers are equal and greatest. = " , a)
        
    elif(b == a and b>c):
        print("'a' and 'b' both numbers are equal and greatest. = " , a)
        
    elif(c == b and c>a):
        print("'b' and 'c' both numbers are equal and greatest. = " , b)
    
    elif(a==b==c):
        print("All the numbers are equal")
        
    return "This is the function i made"

a = find_greatest_no()



# -------------------------------------------------------------------------------

# pasted from chatgpt but it's concept are not have been studied yet.

# def find_greatest_no(a, b, c):
#     if a == b == c:
#         print("All the numbers are equal =", a)
#     else:
#         greatest = max(a, b, c)
#         equal_vars = []
#         if a == greatest:
#             equal_vars.append('a')
#         if b == greatest:
#             equal_vars.append('b')
#         if c == greatest:
#             equal_vars.append('c')

#         if len(equal_vars) == 1:
#             print(f"The greatest number is '{equal_vars[0]}' = {greatest}")
#         else:
#             print(f"{' and '.join(equal_vars)} are equal and greatest = {greatest}")

# # Example use:
# x = int(input("Enter number a: "))
# y = int(input("Enter number b: "))
# z = int(input("Enter number c: "))
# find_greatest_no(x, y, z)
    