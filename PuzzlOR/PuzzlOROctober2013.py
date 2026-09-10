# PuzzlOR October 2013 Chutes and Ladders
import math
import random

def generate_roll():
    return random.randint(1,3)

def checkPosition(position):
    newPosition = 0
    if position in [2,3,8,10,11,12]:
        newPosition = position
    elif position in [4,5]:
        newPosition = 5
    elif position == 6:
        newPosition = 11
    elif position == 7:
        newPosition = 2
    elif position == 9:
        newPosition = 8
    else:
        newPosition = position
    return newPosition

def main():
    totalrolls = 10000
    countval = 0
    rolllist = []
    while countval < totalrolls:
        numOfRolls = 0
        gameEnd = False
        currentPosition = 1
        while not gameEnd:
            newPosition = checkPosition(currentPosition + generate_roll())
            numOfRolls+=1
            if newPosition >= 12:
                gameEnd = True
            currentPosition = newPosition
        rolllist.append(numOfRolls)
        countval+=1
    print(rolllist)
    print("Avg number of rolls is " + str(round(sum(rolllist)/totalrolls,1)))
    
    
main()
