# PuzzlOR December 2010 Minipoly
import random
import operator

def diceRoll():
    return random.randint(1,4)

def boardValue(value):
        if value == "Green":
        	return 1
        elif value == "Yellow":
        	return 4
        elif value == "Red":
        	return 5
        elif value == "Blue":
        	return 7

def boardPosition(value):
        if value == 1:
            return "Green"
        elif value == 2:
            return boardPosition(2 + diceRoll())
        elif value == 3:
            return "Yellow"
        elif value == 4:
            return boardPosition(diceRoll())
        elif value == 5:
            return "Red"
        elif value == 6 or value == 7:
            return "Blue"

rollcount = 0
maxvalue = 100000
outcome = {}
currentboardposition = 0
while (rollcount < maxvalue):
    currentboardposition += diceRoll()
    if currentboardposition > 7:
        currentboardposition -= 7
    createdvalue = boardPosition(currentboardposition)
    if createdvalue in outcome:
        outcome[createdvalue] += 1
    else:
        outcome[createdvalue] = 1
    rollcount+=1

sorted_x = sorted(outcome.items(), key=operator.itemgetter(1))
print(sorted_x[len(sorted_x)-1][1]/maxvalue)


