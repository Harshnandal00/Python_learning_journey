"""
Day 02: Conditional Statements in Python

Topics:
- if
- if-else
- if-elif-else
- logical operators (and, or, not)
- nested if
"""

# --------- IF condition ---------
name = input("Please enter your name: ")

if name == "Harsh":
    print("Welcome back! You are recognized as Master of the system.")

# --------- IF - ELSE condition ---------
age = int(input("Please enter your correct age: "))

if age >= 18:
    print("You are welcome to the club.")
    print("Enjoy your time here with beautiful scenery.")
else:
    print("You are a minor and not allowed here.")
    print("Please leave.")

# --------- IF - ELIF - ELSE condition ---------
marks_obtained = int(input("Please enter your marks: "))

if marks_obtained >= 90:
    print("Excellent! Keep it up, topper!")
elif marks_obtained >= 80:
    print("Very good! Just a little more to reach the top.")
elif marks_obtained >= 70:
    print("Above average. You can do much better.")
elif marks_obtained >= 60:
    print("You barely passed. Extra effort is needed.")
else:
    print("You failed. Prepare well for improvement.")

# --------- Logical Operators ---------

# AND operator
user_name = input("Please enter your name: ")
user_age = int(input("Please enter your age: "))

if user_name != "" and user_age >= 18:
    print("Access allowed! Welcome.")
else:
    print("Access denied.")

# OR operator
stream = input("Enter your stream: ")
college = input("Enter your college name: ")

if stream == "BCA" or college == "Jaat college":
    print("Access allowed! OG gang confirmed.")
else:
    print("Access denied. Not from OG gang.")

# NOT operator
user_id = False

if not user_id:
    print("Please log in first!")

# --------- Nested IF ---------
user_age = int(input("Enter your age: "))
user_name = input("Enter your name: ")

if user_age >= 18:
    if user_name != "":
        print("Verification successful. You are human.")
    else:
        print("Verification failed. Name missing.")
else:
    print("You are a minor. Access denied.")
