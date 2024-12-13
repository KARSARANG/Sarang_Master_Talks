#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def displayEnggQuiz():
    score=0
    for x,y in Enggquiz.items():
        print(x)
        useranswer = input().lower()
        if useranswer==y:
            print("Yes!You got it right!")
            score=score+1
        else:
            print("Oops!That was wrong!")
            
    print("Your Score is",score)
score=0   
Engggoal1="Innovation distinguishes between a leader and a follower.Do you\nA.agree, have an innovative thought(s) and enthusiastic to work on it\nB.agree, but like to have a routine life\nC.agree, but reluctant to exhibit as if what others might think\nD.agree, but never got encouragement for my thoughts"

print(Engggoal1)

userchoice=input("please enter your choice A or B or C or D ")
if userchoice=='A':
    score=score+10
elif userchoice=='B':
    score=score+3
elif userchoice=='C':
    score=score+5
elif userchoice=='D':
    score=score+8
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

