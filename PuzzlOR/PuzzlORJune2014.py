#June 2014 - Frog and Fly

import math
import random
from collections import Counter
import operator

def generate_random(alist):
    return random.randint(0,len(alist)-1)

def move(currentPosition,allPosition,possibleMoves):
    tempval = allPosition[currentPosition]
    newPosition = tempval[generate_random(tempval)]
    checkval = False
    while not checkval:
        if newPosition in possibleMoves:
            return newPosition
        newPosition = tempval[generate_random(tempval)]

def main():

    frogMoves = ["A1","B1","A2","B2","A3","B3"]
    flyMoves = ["A1","B1","C1","A2","C2","C3"]

    pond ={
    "A1":["B1","A2","B2"],
    "A2":["A1","B1","B2","A3","B3"],
    "A3":["A2","B2","B3"],
    "B1":["A1","A2","B2","C1","C2"],
    "B2":["A1","B1","C1","A2","C2","A3","B3","C3"],
    "B3":["A2","A3","B2","C2","C3"],
    "C1":["B1","B2","C2"],
    "C2":["B1","C1","B2","B3","C3"],
    "C3":["B2","C2","B3"]
    }

    catch = []
    countval = 0
    maxval = 10000
    frogPosition = frogMoves[generate_random(frogMoves)]
    flyPosition = flyMoves[generate_random(flyMoves)]
    while countval < maxval:
        if frogPosition == flyPosition:
            catch.append(frogPosition)
            countval+=1
        frogPosition = move(frogPosition,pond,frogMoves)
        flyPosition = move(flyPosition, pond,flyMoves)
    a = dict(Counter(catch))
    print(a)
    sorted_a = sorted(a.items(), key=operator.itemgetter(1))
    print(sorted_a[len(sorted_a) - 1][0],round(sorted_a[len(sorted_a) - 1][1]/maxval,2))


main()
