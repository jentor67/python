import sys
import time

"""turning100.py: Determine the year they turn 100"""

"""Command line"""
#For python >= 3.0
""">python3 turning100.py"""
#For python < 3.0
""">python turning100.py"""
__author__    = "John Major"
__copyright__ = "Copyright 2018, Jentor"

question1 = "Give me your name: " 
question2 = "Give me your age: "


while True:
    if (sys.version_info > (3,0)):
        # python3 code
        name = input(question1)
    else:
        name = raw_input(question1)
   
    if len(name) < 3:
        print("Name doesn't seem valid must be 3 or more characters")
        continue
    else:
        #All is good
        break      
    
while True:
    try:
        if (sys.version_info > (3,0)):
            # python3 code
            age = int(input(question2))
        else:
            # python2 code
            age = int(raw_input(question2))
    except ValueError:
        print("Sorry, I didn't understant that.")
        continue

    if age < 0:
        print("Sorry, your response must not be negative.")
        continue
    else:
        #All is good
        break


presentYear = int(time.strftime("%Y"))

yearTurning50 = (100 - age) + presentYear 

print(" ")
print("Your name in " + name + " and your age is " + str(age) + ",")
print("therefore you will be 100 in the year " + str(yearTurning50))
