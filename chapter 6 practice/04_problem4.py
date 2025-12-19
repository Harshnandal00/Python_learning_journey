username = input("Enter your name: ")

if(len(username)<=10):
    print("your username contains\nless than 10 characters.")

else:
    print("Your username has exeded the max. character limit.")
    print("Please enter another name.")    