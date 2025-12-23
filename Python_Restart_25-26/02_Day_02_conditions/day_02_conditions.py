"""
Day 02: Conditional Statements in Python

Topics:
- if
- if-else
- if-elif-else
- input()
- logical operators (and, or, not)
"""

# ---------IF condition--------------------
name = input("Please enter your name here: ")
if name == "Harsh":
    print("Welcome back! You are recognized as Master of the system. ")

# ---------IF - Else condition-------------    
age = int(input("Please entery your correct age: "))
if age >=18:
    print("You are welcome to the club\nEnjoy your time here with beautiful scenery.")

else:
    print("You are a minor and not allowed here.\nPlease leave.")

# -----------IF elif else condition-------------
Marks_obtained = int(input("Please enter your correct marks here: "))
if Marks_obtained >= 90:
    print("Excellent! Keep it up our Topper! ")

elif Marks_obtained >= 80:
    print("Very Good! Just a little more to become a top student ")

elif Marks_obtained >= 70:
    print("Above average. Can do a lot better if you pay more attention to studies ")

elif Marks_obtained >= 60:
    print("You Barely passed. I think you should attend extra classes.")

else:
    print("You Failed! Better prepare at parent teacher meeting.")

# ------------------logical operators----------------

#---and---
Your_name = input("Please enter your name: ")
Your_age = int(input("Please enter your age: "))
if Your_name == str and Your_age >= 18:
    print("Access Allowed! Welcome back User.")
else:
    print("Access Denied! Please leave.")
   
#---or---
stream = input("What is your stream pal! : ")
college = input("From which college are you from: ")
if stream == "BCA" or college == "Jaat college":
    print("access allowed! you are gangster , og gang ")
else:
    print("ha! you sucker! you are not from og gang, get out of here!")
    
