def displayEnggGoal():
    Engggoal1="Innovation distinguishes between a leader and a follower.Do you\nA.agree, have an innovative thought(s) and enthusiastic to work on it\nB.agree, but like to have a routine life\nC.agree, but reluctant to exhibit as if what others might think\nD.agree, but never got encouragement for my thoughts"
    print(Engggoal1)

    userchoice=input("please enter your choice A or B or C or D ")
    if userchoice=='A':
        score=10
    elif userchoice=='B':
        score=3
    elif userchoice=='C':
        score=5
    elif userchoice=='D':
        score=8
    else:
        print("wrong input given.")
    if score==10:
        print("Awesome!!You are on the right track.Keep moving and wish you all the very best.")
    elif score==3:
        print("Cool!But try to add some spark in your life by being innovative. Wish you good luck.")
    elif score==8:
        print("Great!!Never get pulledm down by others.Always believe in your individulity and just keep moving. Wish you all the best for your endevour.")
    elif score==3:
        print("Good!Just try to create such opportunities to exhibit your thoughts.Have friendly people around you who encourage you always .whis you good luck.")


    Engggoal2=input("When given an opportunity to speak spontaneously\nA.I will be the first one to grab the chance\nB.Have interest but think what my friends or others comment later\nC.Not a stage person\nD.Lack confidence to speak due to lack of communication skills")
    print(Engggoal2)
    userchoice=input("please enter your choice A or B or C or D ")
    if userchoice=='A':
        print("Thats fantastic!You are a ver good public speaker.")
    elif userchoice=='B':
        print("Good that you have got the interest.But never think about other's comments.")
    elif userchoice=='C':
        print("Its very important to cultivate speaking skill inorder to be a very good teamleader.So please cultivate.")
    elif userchoice=='D':
        print("Build that confidence in you that you can do it!!You are the best!!")

    else:
        print("wrong input given")
    print("Thank you")

def listening_ability():
    """Function which stores all the questions & coreresponding options in a dictionary and records the responses given by the user, validates it"""
    a=10
    b=9
    c=8
    sc1=0
    lt_ques={
        'How do you feel when someone express their worry to you?':['Get involve in the solution for their problem','Feel sorry for them and leave it as their fate','Feel bored listening to their problems'],
        'what is the level of understanding you get on a topic after hearing a lecture?':['I can grasp the topic by-heart after hearing','I can get complete grip if I hear the lecture and simultaneously make a notes','I need to re-read the whole topic'],
        'What is your opinion on the ability to memorise while listening':["It's a great skill/ability","It is beneficial but not much essential,'It is not very useful to memorise in the present age, as we already devices which can record and store"]
    }
    print("Hey! Now is a small test for you testing your listening skills...Get set Go!")
    for key,value in lt_ques.items():
        print(key)

        for item,i in zip(value,range(97,100)):
            print(chr(i)+". "+item)
        print("Enter your choice [a or b or c]")
        inp=input()
        if(inp=='a'):
            sc1=sc1+a
        elif(inp=='b'):
            sc1=sc1+b
        else:
            sc1=sc1+c
    return sc1
def question_ability():
    a=10
    b=9
    c=8
    sc2=0
    ques_ques={
        'What do you do if your classmate has not been attending college for over a week?':['Call him /inquire about him','Wait for one more day for his/her arrival','Think that he would definitely come some day'],
        'how do you react if someone asks your personal details?':['Question them why they want to know about us','Suspect them and run away from there','Tell them our details'],
        'What would you do if two of your friends had a serious fight?':['Inquire about the cause of the problem and when it all started','Take one of your friends side and start fighting on his behalf','Enjoy the fight and crack jokes about the entire issue']
    }
    print("Hey! Now is a small test for you testing your questioning ability which is one of the important skills for a doctor...Get set Go!")
    for key,value in ques_ques.items():
        print(key)

        for item,i in zip(value,range(97,100)):
            print(chr(i)+". "+item)
        print("Enter your choice [a or b or c]")
        inp=input()
        if(inp=='a'):
            sc2=sc2+a
        elif(inp=='b'):
            sc2=sc2+b
        else:
            sc2=sc2+c
    return sc2
def medicalGoal():
	total=listening_ability()*0.7+question_ability()*0.3
	print("Your score is ",int(total))
    