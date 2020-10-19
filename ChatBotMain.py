import Service1
import Service2
import random
#ListOfWelcomeMessages contains different welcome messages
ListOfWelcomeMessages = ['Hello Friend, My hearty welcome to you','Namaste, I welcome to my world']
#Pick one welcome message at random
WelcomeMessage = random.sample(ListOfWelcomeMessages,1)
#Convert Welcome Message from list to string
WelMsg = ""
WelMsg = WelcomeMessage[0]
#Print Welcome message
print ((WelMsg))
#Get name of the person
name = input("May I know your good name please!\n")
#get current date time
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H")
current_time = int(current_time)
#Based on time of the login, chotbot wishes the user GM, GA or GE
if(int(current_time)<12):
    print("Good Morning",name,"!","Once again welcome you")
elif (current_time >= 12 and current_time <= 15):
    print("Good Afternoon",name,"!","Once again welcome you")
elif (current_time >15):
    print("Good Evening",name,"!","Once again welcome you")
ch1 = 'Y'
while(ch1=='Y'):
    menuItem=int(input("Here is the list of services that I can extend to you. \n 1. I can let you know your level of expertise in a particular subject.\n2. I can let you know skill gap if you tell me your goal.Please enter 1 or 2:"))
    try:
        if(menuItem == 1):
            ch2 = 'Y'
            while(ch2=='Y'):
                print("I am very glad to provide your level of expertise.\nPlease enter subject for which you want to be tested (1, 2 or 3):\n1. Maths\n2. Biology\n3. Chemistry ")
        #Read subject choice
                try:
                    subChoice = int(input())
                    if (subChoice == 1):
                        Service1.displayMathsQuiz()
                    elif (subChoice == 2):
                        Service1.displaybioquiz()
                    elif (subChoice == 3):
                        Service1.displayChemQuiz()
                    else:
                        print("Wrong entry")
                    ch2 = input(("Do you want to continue with another quiz?(Y/N):"))
                except ValueError:
                    print("No valid integer! Please try again ...")
        elif (menuItem == 2):
            goalChoice = int(input("Please enter what is your goal.\n1. I want to become Doctor\n2. I want to become Engineer\nPlease enter 1 or 2:"))
            if (goalChoice == 1):
                Service2.medicalGoal()
            elif(goalChoice == 2):
                Service2.displayEnggGoal()
    except ValueError:
        print("No valid integer! Please try again ...")
    ch1 = input("Do you want me to provide another service?Y/N")

        

