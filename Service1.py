def displaybioquiz():
    count=0
    print("Get ready for a Bio quiz! Press enter to start the quiz!!")
    input("")
    scidict={
        "What is the Ph value of human blood?":"7.4",
        "Can you guess the metal present in chlorophyll?":"magnesium",
        "Tell me! Who is the father of zoology?":"aristotle",
        "Name an insect with 13 chambered heart.":"cockroach",
        "How many chromosome in our body?":"46"
    }
    for key,value in scidict.items():
        print(key)
        ans=input().lower()
        if ans==value:
            count=count+1
            print("Yes! You are right!")
        else:
            print("Sorry! You are wrong...")
    print()
    if count>=4:
        print("Wohoo! Congrats, you scored",count)
    elif count>=2:
        print("Hey! you scored",count,"that's great.Keep Learning!")
    else:
        print("Your score is not upto the mark.Your Score is:",count)
    print()
    print("--------------------------------------------------")
    print()
    print("Do you want to know the answers!?, press enter")
    input("")
    print()
    print("And the answers for the questions are: ")
    for key,value in scidict.items():
        print("Q.",key)
        print("Ans:",value)

def displayMathsQuiz():
    score = 0
    for x,y in MathsQuestions.items():
        print(x)
        useranswer = input()
        if(useranswer == y):
            score = score +1
    print("Your score",score)

MathsQuestions = {"What is the value of the following expression:(2+3%5*7)": "23","Which natural number has no predecessor?":"1","This number’s irrationality property was first discovered by Pythagoras. What is its value?":"2","What do you get if you divide the number of hours in a week by the sum of the sides of a triangle, and the number of natural satellites of the earth?":"42",
                 "Which of the following number is an odd integer contains the digit 5, is divisible by 3 and lies between the square of 12 and 13?":"165","20 % of 2 is equal to(round off to one decimal)":"0.4"}
def displayChemQuiz():
    score=0
    for x,y in ChemQuestions.items():
        print(x)
        useranswer = input().lower()
        if useranswer==y:
            score=score+1
    print("YOur Score",score)

ChemQuestions = {" Water-based liquids can be described as acidic, neutral, or basic, with respect to pH. Which of these describes milk?"
:"slightly acidic","What is the most common isotope of hydrogen?":"protium","You can't live without water! What is its chemical formula?":"h2o","The symbol Ag stands for which element?":"silver","What do you call an atom that has more protons than electrons?"
:"cation"," A drop of food coloring spreading out in a cup of water is an example of which transport process?":"diffusion"}
