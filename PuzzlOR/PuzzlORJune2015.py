#PuzzlOR Campsite June 2015

import math
import random
from collections import Counter
import operator

def getSurroudingPosition(position, positionInfo):
    tempval = position[0]
    tempnum = int(position[1])
    templistnum = []
    finallist = []
    scoreval = 0
    templistval = positionInfo[tempval]
    if tempnum == 1:
        templistnum.extend([tempnum,tempnum+1])
    elif tempnum in [2,3,4,5,6,7]:
        templistnum.extend([tempnum-1,tempnum,tempnum+1])
    elif tempnum == 8:
        templistnum.extend([tempnum-1,tempnum])
    for val in templistval:
        for num in templistnum:
            finallist.append(val + str(num))
    return finallist

def getPositionValue(alist,positionValue, resourceScore):
    templist = []
    for value in alist:
        temp = positionValue[value]
        templist.extend(temp)
    resourcelist = list(set(templist))
    scoreval = 0
    for value in resourcelist:
        scoreval += resourceScore[value]
    return scoreval

def main():
    positionInfo = {
    "A":["A","B"],
    "B":["A","B","C"],
    "C":["B","C","D"],
    "D":["C","D","E"],
    "E":["D","E","F"],
    "F":["E","F","G"],
    "G":["F","G","H"],
    "H":["G","H"]
    }

    positionData = ['A1', 'A5', 'B1', 'B5', 'C1', 'C5', 'D1', 'D5', 'E1', 'E5',
    'F1', 'F5', 'G1', 'G5', 'H1', 'H5', 'A2', 'A6', 'B2', 'B6', 'C2', 'C6',
    'D2', 'D6', 'E2', 'E6', 'F2', 'F6', 'G2', 'G6', 'H2', 'H6', 'A3', 'A7',
     'B3', 'B7', 'C3', 'C7', 'D3', 'D7', 'E3', 'E7', 'F3', 'F7', 'G3', 'G7',
     'H3','H7', 'A4', 'A8', 'B4', 'B8', 'C4', 'C8', 'D4', 'D8', 'E4', 'E8',
     'F4', 'F8', 'G4', 'G8', 'H4', 'H8']

    positionValue = {
    'A1': [],'A2': [],'A3': ['water','mosquito'],
    'A4': [],'A5': ['swamp'],'A6': ['swamp','mosquito'],'A7': ['wood'],
    'A8': [],'B1': ['swamp'],'B2': ['mosquito'],
    'B3': [],'B4': [],'B5': ['water'],
    'B6': [],'B7': [],'B8': ['mosquito'],
    'C1': [],'C2': [],'C3': [],'C4': ['wood'],
    'C5': ['swamp','water','mosquito'],'C6': [],
    'C7': ['swamp'],'C8': ['water'],
    'D1': [],'D2': ['water','swamp'],
    'D3': [],'D4': ['water'],
    'D5': [],'D6': [],'D7': ['swamp'],'D8': ['water'],'E1': [],
    'E2': ['water'],'E3': ['water'],
    'E4': [],'E5': ['wood'],'E6': [],
    'E7': [],'E8': [],'F1': [],'F2': ['water','swamp'],
    'F3': [],'F4': [],'F5': [],'F6': [],'F7': [],'F8': [],
    'G1': ['mosquito'],'G2': [],'G3': ['wood','water','mosquito'],
    'G4': ['swamp'],'G5': ['water'],'G6': [],'G7': [],
    'G8': ['swamp'],'H1': [],'H2': [],'H3': ['swamp',],
    'H4': ['wood'],'H5': [],'H6': ['mosquito'],'H7': [],'H8': ['wood']
    }

    resourceScore = {
    'water':3,
    'swamp':-1,
    'wood':1,
    'mosquito':-2
    }

    scoreList = []
    for value in positionData:
        templist = getSurroudingPosition(value, positionInfo)
        score = getPositionValue(templist,positionValue, resourceScore)
        scoreList.append([value,score])
    sorted_a = sorted(scoreList,key=operator.itemgetter(1), reverse = True)
    print(sorted_a[0:3])

main()

