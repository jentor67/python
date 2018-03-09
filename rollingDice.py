import sys
import random 

"""rollingDice.py: Create a six sided dice"""
"""Command line"""
#For python >= 3.0
""">python3 rollingDice.py"""
#For python < 3.0
""">python rollingDice.py"""

__author__    = "John Major"
__copyright__ = "Copyright 2018, Jentor"

question1 = "Do you want to roll again?(y/n) " 

def askQuestion():
    if (sys.version_info > (3,0)):
        # python3 code
        decision = input(question1)
    else:
        # python2 code
        decision = raw_input(question1)
    return decision

    
while True:
    print(random.randint(1,6))

    decision = askQuestion()

    while decision != "y" and decision != "Y" and decision != "n" and decision != "N": 
        print("Don't understand please write y, Y, n, or N")
        decision = askQuestion()

    if decision == "n" or decision == "N":
        break

print("Thank you for playing")    
