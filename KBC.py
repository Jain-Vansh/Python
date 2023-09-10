# Kaun Banega Crorepati

questions = ["What is the capital of India?","Who is our Prime Minister?","Who is Uncharted's main character?","Real name of soap?"]

answers = ["Delhi","Narendra Modi","Nathan Drake","John MacTavish"]

options = [["Mumbai","Delhi","Bangalore","Nagpur"],["Jawaharlal Nehru","Mahatma Gandhi","Narendra Modi","Rahul Gandhi"],["Sully","Nathan Drake","Sam Drake","Charlie Cutter"],["John Price","John MacTavish","Simon Riley","Makarov"]]

cash = [500,1000,5000,10000]

won = -1

for i in range(len(questions)):
    print(questions[i],"\n")
    print("The Options Are:- \n")
    print("1.",options[i][0])
    print("2.",options[i][1])
    print("3.",options[i][2])
    print("4.",options[i][3],"\n")
    
    choice = input("Enter your option: ")

    if(choice == answers[i]):
        print("Its the correct answer!\n")
        won+=1
        continue
    else:
        print("Sorry Its the incorrect answer!")
        break

if(won == -1):
    print("You did not win anything!")
else:
    print("You won,",cash[won])


    
