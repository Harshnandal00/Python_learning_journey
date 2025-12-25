username = input("Please enter the username: ").lower()

password_input = input("Please enter the password: ")

if password_input.isdigit():
    password = int(password_input)

    if username == "admin" and password == 1245:
        print("Access allowed! Welcome back, admin.")
    else:
        print("Access denied. Username or password is incorrect.")
else:
    print("Password must be a number.")
