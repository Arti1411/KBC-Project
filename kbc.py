from time import sleep
import sys
import random
import os

intro = """
Rules to be followed:

1. The game consists of 15 MCQ questions.
2. There are 4 checkpoints in this game at question number 5, 10,and 15.
3. At any point you can quit the game by entering "x".

Press [Enter] to start the game.
"""

gameque = [
    "What is the maximum possible length of an identifier?",
    "Who developed the Python language?",
    "In which year was the Python language developed?",
    "In which language is Python written?",
    "Which one of the following is the correct extension of the Python file?",
    "In which year was the Python 3.0 version developed?",
    "What do we use to define a block of code in Python language?",
    "Which character is used in Python to make a single line comment?",
    "What is the method inside the class in python language?", 
    "Which of the following declarations is incorrect?",
    "Which of the following is not a keyword in Python language?",
    "Which of the following operators is the correct option for power(ab)?",
    "Which of the following functions is a built-in function in python language?",
    """What will be the output of this code?
        import math  
        abs(math.sqrt(36))""",
    """What will be the output of this code?
        any([5>8, 6>3, 3>1])  """
]

gameopt =[
    f"A.16\nB.32\nC.64\nD.None of these above",
    f"A.Zim Den\nB.Guido van Rossum\nC.Niene Stom\nD.Wick van Rossum",
    f"A.1995\nB.1972\nC.1981\nD.1989",
    f"A.English\nB.C\nC.PHP\nD.All of the above",
    f"A..py\nB..python\nC..p\nD.None of these",
    f"A.2008\nB.2000\nC.2010\nD.2005",
    f"A.Key\nB.Brackets\nC.Indentation\nD.None of these",
    f"A./\nB.//\nC.#\nD.!",
    f"A.Object\nB.Function\nC.Attribute\nD.Argument",
    f"A._x=2\nB.__x=3\nC.__xyz__=5\nD.None of these",
    f"A.val\nB.raise\nC.try\nD.with",
    f"A.a^b\nB.a**b\nC.a^^b\nD.a^*b",
    f"A.val()\nB.print()\nC.print[]\nD.None of these",
    f"A.Error\nB.-6\nC.6\nD.6.0",
    f"A.False\nB.Ture\nC.Invalid code\nD.None of these",
]

gameans = ["d", "b", "d", "b", "a", "a", "c", "c", "b", "d", "a", "b", "b", "d", "b"]

levels= [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]

winmoney = 0
checkque = []
lastcheckpoint = None
lengthofque = len(gameque)

def print_in_slow(string, lag):
	for s in string:
		if s not in '\t\n':
			print(s, end='')
			sleep(lag)
			sys.stdout.flush()
		else:
			print(s, end='')
			sys.stdout.flush()

def print_line_in_slow(string, lag):
	lines = string.split('\n')
	for line in lines:
		if line:
			print(line, end='\n')
			sleep(lag)
			sys.stdout.flush()
		else:
			print(line, end='\n')
			sys.stdout.flush()

title = "KAUN BANEGA CROREPATI"
print(title.center(530))
player = input("Enter your name: ")
print_in_slow(f'\nHello {player}\nWelcome to KBC game!\n\n', 0.04)
print_in_slow(intro, 0.02)
input()
os.system('cls')

for i in range(0, len(gameque)):
    while True:
        qno = random.randint(0, lengthofque)
        if qno not in checkque:
            checkque.append(qno)
            break  

    print_in_slow(f'\nQuestion for Rs.{levels[i]}\n', 0.03)
    print_line_in_slow(f'\n{i+1}. {gameque[i]}',0.5)
    print_line_in_slow(gameopt[i], 0.5)
    reply = str(input("\nEnter the answer: "))

    while reply not in 'abcd':
        if (reply == 'x'):             
            if lastcheckpoint:
                winmoney = levels[lastcheckpoint-1]
            print()
            print_line_in_slow(f'\nGame Ending!!\n\nThe Correct Answer is option {gameans[i]}\n\nYou won Rs.{winmoney:}', 0.09)
            sys.exit()

    else:
        if reply == gameans[i]:
            winmoney = levels[i]
            print_line_in_slow(f"\nCorrect answer, you have won Rs.{levels[i]}\n\n", 0.09)
            if i in [5,10,15]:
                  lastcheckpoint = i

        else:
            if lastcheckpoint:
                winmoney = levels[lastcheckpoint-1]
            print()
            print_line_in_slow(f"\nWrong answer\nCorrect answer is option {gameans[i]}\n\nGame Over!\n\nTotal win money Rs.{winmoney:}", 0.09)
            sys.exit()
else:                    
    print_line_in_slow()(f'\nCongratulations you completed the KBC game.\n\nTotal win money Rs.{winmoney:}', 0.09)