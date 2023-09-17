# rock paper scissors game using matrix method
import random

def convert(inp):
    if(inp == "rock"):
        return 0
    elif(inp == "paper"):
        return 1
    else:
        return 2
    
def decision(i,j):
    decisions = [[2,1,0],[0,2,1],[1,0,2]]
    if(decisions[i][j] == 1):
        print("User Wins the Round!")
        return 1
    elif(decisions[i][j] == 0):
        print("Computer Wins the Round!")
        return 0
    else:
        print("The round is a Draw!")

userCount = 0
computerCount = 0
while(userCount<5 and computerCount<5):
    choices = ["rock","paper","scissors"]
    user = input("Rock, Paper or Scissors? : ").lower()
    computer = random.choice(choices)
    if(user not in choices):
        print("Invalid input, Disqualified!!")
        break
    user = convert(user)
    computer = convert(computer)
    win = decision(user,computer)
    if(win == 1):
        userCount+=1
    else:
        computerCount+=1
if(userCount>computerCount):
    print("User wins the Game!")
else:
    print("Computer wins the Game!")