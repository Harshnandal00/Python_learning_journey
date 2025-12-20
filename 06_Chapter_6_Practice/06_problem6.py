marks = int(input("Enter your marks: "))

if(marks<=100 and marks>=90):
    Grade = "Ex"
elif(marks<90 and marks>=80):
    Grade = "A"
elif(marks<80 and marks>=70):
    Grade = "B"
elif(marks<70 and marks>=60):
    Grade = "C"
elif(marks<60 and marks>=50):
    Grade = "D"
elif(marks<50):
    Grade = "F"
    
print("Your Grade is: ", Grade)    
    