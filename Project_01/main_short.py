# even if it is maked so short but to find that logic out we have used up a lot of time
# and by using this types to write the readabity have been decreased so we will have to 
# add more comment so that the other programers will have no problem in understanding 
# our code.
import random

userdata = input("Enter your move please, ")
computer = random.choice([1 , 0 , -1])

dict1 = { "s":1 ,"w":0,"g":-1}
user = dict1[userdata]
dict2 = {1:"snake", 0:"water", -1:"gun"}

if(user == computer):
    print(f"your move: {dict2[user]}\ncomputer's move: {dict2[computer]}")
    print("This was a draw\nPlease play again")
    
else:
    if(user == int):
        print("unexepted input")
        
    elif(user - computer == 2 or user - computer == -1):
        print(f"your move: {dict2[user]}\ncomputer's move: {dict2[computer]}") 
        print("You Lose")
    
    else:
        print(f"your move: {dict2[user]}\ncomputer's move: {dict2[computer]}") 
        print("You have won! Congratulations")
# else:
#     if(user == 1 and computer == 0):
#         print(f"your move: {dict2[user]}\ncomputer's move: {dict2[computer]}")
#         print("You have won! Congratulations.")
        
#     elif(user == 1 and computer == -1):
#         print(f"your move: {dict2[user]}\ncomputer's move: {dict2[computer]}")
#         print("You Lose!")
        
#     elif(user == 0 and computer == -1):
#         print(f"your move: {dict2[user]}\ncomputer's move: {dict2[computer]}")
#         print("You have won! Congratulations.")
        
#     elif(user == 0 and computer == 1):
#         print(f"your move: {dict2[user]}\ncomputer's move: {dict2[computer]}")
#         print("You Lose!")
        
#     elif(user == -1 and computer == 1):
#         print(f"your move: {dict2[user]}\ncomputer's move: {dict2[computer]}")
#         print("You have won! Congratulations.")
        
#     elif(user == -1 and computer == 0):
#         print(f"your move: {dict2[user]}\ncomputer's move: {dict2[computer]}")        
#         print("You Lose!")
        
        
#     else:
#         print("Something went weong.\nPlease try again.")




    