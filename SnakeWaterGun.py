# Snake Water Gun Game

import random

def check(user,comp):
    if(user == "snake"):
        if(comp == "water"):
            return 1
        elif(comp == "snake"):
            return 2
        else:
            return 0
    elif(user == "water"):
        if(comp == "water"):
            return 2
        elif(comp == "snake"):
            return 0
        else:
            return 1
    else:
        if(comp == "water"):
            return 0
        elif(comp == "snake"):
            return 1
        else:
            return 2


# main body
flag = True
userPoints = 0
computerPoints = 0
while(userPoints<5 and computerPoints<5):
    choices = ["snake","water","gun"]
    computer = random.choice(choices)
    user = input("Snake, Water or Gun: ").lower()
    if(user not in choices):
        print("That was an invalid input, Disqualified!!")
        break
    decision = check(user,computer)
    if(decision == 1):
        userPoints+=1
        print("User Wins the Round!!")
    elif(decision == 0):
        computerPoints+=1
        print("Computer Wins the Round!!")
    else:
        print("The Round is a Draw!!")
        continue
if(userPoints>computerPoints):
    print("User Wins the Game!!")
else:
    print("Computer Wins the Game!!")



