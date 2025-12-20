#         PROJECT 1: SNAKE, WATER, GUN GAME
# We all have played snake, water gun game in our childhood. 
# If you haven’t, google the rules of this game and write a python 
# program capable of playing this game with the user.
'''
snake = 1
water = 0
gun = -1
'''

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
    if(user == 1 and computer == 0):
        print(f"your move: {dict2[user]}\ncomputer's move: {dict2[computer]}")
        print("You have won! Congratulations.")
        
    elif(user == 1 and computer == -1):
        print(f"your move: {dict2[user]}\ncomputer's move: {dict2[computer]}")
        print("You Lose!")
        
    elif(user == 0 and computer == -1):
        print(f"your move: {dict2[user]}\ncomputer's move: {dict2[computer]}")
        print("You have won! Congratulations.")
        
    elif(user == 0 and computer == 1):
        print(f"your move: {dict2[user]}\ncomputer's move: {dict2[computer]}")
        print("You Lose!")
        
    elif(user == -1 and computer == 1):
        print(f"your move: {dict2[user]}\ncomputer's move: {dict2[computer]}")
        print("You have won! Congratulations.")
        
    elif(user == -1 and computer == 0):
        print(f"your move: {dict2[user]}\ncomputer's move: {dict2[computer]}")        
        print("You Lose!")
        
        
    else:
        print("Something went weong.\nPlease try again.")



    