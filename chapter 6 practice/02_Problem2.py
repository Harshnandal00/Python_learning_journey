a = int(input("Enter your marks: "))
b = int(input("Enter your marks: "))
c = int(input("Enter your marks: "))

total_percentage = (100*(a + b + c))/300

if(total_percentage>=40 and a>33 and b>33 and c>33):
    print("Congrats, You have passed the exam.", total_percentage)
    
else:
    print("Sorry to say but you have failed", total_percentage)    
    print("better luck next time.")