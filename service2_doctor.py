


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
total=listening_ability()*0.7+question_ability()*0.3
print("Your score is ",int(total))
if(total>=27):
    print('You did great.Congrats')
elif(total>=20):
    print("Good!Keep Learning!!")

