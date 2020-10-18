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

    