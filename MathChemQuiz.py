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
