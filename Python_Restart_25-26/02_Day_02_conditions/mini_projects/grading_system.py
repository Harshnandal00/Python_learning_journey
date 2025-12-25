marks_input = input("Please enter your marks: ")

if marks_input.isdigit():
    marks = int(marks_input)

    if 0 <= marks <= 100:
        if marks >= 90:
            print("Grade A+ : Excellent!")
        elif marks >= 80:
            print("Grade A : Very Good!")
        elif marks >= 70:
            print("Grade B : Above Average")
        elif marks >= 60:
            print("Grade C")
        elif marks >= 50:
            print("Grade D")
        else:
            print("Fail. Better try again.")
    else:
        print("Marks must be between 0 and 100.")
else:
    print("Please enter a valid number.")
