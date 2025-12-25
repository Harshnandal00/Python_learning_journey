age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ").lower()

if age >= 18:
    if has_id == "yes":
        print("Access authorized. Welcome.")
    else:
        print("ID not found.")
        make_id = input("Do you want to register and create an ID? (yes/no): ").lower()
        if make_id == "yes":
            print("Registration successful. Access granted.")
        else:
            print("Access denied. ID is required.")
else:
    print("Access denied. You are underage.")
