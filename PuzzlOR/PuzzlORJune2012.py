#PuzzlOR June 2012 Lost at sea
import math
import random
from collections import Counter
import operator

def checkDiagonal(a,b):
    aval = a[0]
    anum = int(a[1])
    bval = b[0]
    bnum = int(b[1])
    output = False
    if aval != bval and abs(anum-bnum) == 1:
        output = True
    return output

def get_random_list(alist):
    return random.randint(0,len(alist)-1)

def checkVal(value, alist):
    if value in alist:
        return True
    return False

def newPosition(current,positioninfo):
    outputlist = []
    finallist = []
    tempval = current[0]
    tempnum = int(current[1])
    templistval = positioninfo[tempval]
    templistnum = []
    if tempnum == 1:
        templistnum.extend([tempnum,tempnum+1])
    elif tempnum in [2,3,4,5,6,7]:
        templistnum.extend([tempnum-1,tempnum,tempnum+1])
    elif tempnum == 8:
        templistnum.extend([tempnum-1,tempnum])
    for val in templistval:
        for num in templistnum:
            finallist.append(val + str(num))
    for val in finallist:
        if not checkDiagonal(current,val) and val != current:
            outputlist.append(val)
    return outputlist[get_random_list(outputlist)]
    

def main():

    positioninfo = {
    "A":["A","B"],
    "B":["A","B","C"],
    "C":["B","C","D"],
    "D":["C","D","E"],
    "E":["D","E","F"],
    "F":["E","F","G"],
    "G":["F","G","H"],
    "H":["G","H"]
    }
    position_data = ['A1', 'A5', 'B1', 'B5', 'C1', 'C5', 'D1', 'D5', 'E1', 'E5',
    'F1', 'F5', 'G1', 'G5', 'H1', 'H5', 'A2', 'A6', 'B2', 'B6', 'C2', 'C6',
    'D2', 'D6', 'E2', 'E6', 'F2', 'F6', 'G2', 'G6', 'H2', 'H6', 'A3', 'A7',
     'B3', 'B7', 'C3', 'C7', 'D3', 'D7', 'E3', 'E7', 'F3', 'F7', 'G3', 'G7', 'H3',
     'H7', 'A4', 'A8', 'B4', 'B8', 'C4', 'C8', 'D4', 'D8', 'E4', 'E8',
     'F4', 'F8', 'G4', 'G8', 'H4', 'H8']

    position_value = {
    'A1': 2,'A2': 2,'A3': 0,'A4': 1,
    'A5': 1,'A6': 0,'A7': 3,'A8': 3,
    'B1': 1,'B2': 3,'B3': 2,'B4': 1,
    'B5': 1,'B6': 4,'B7': 3,'B8': 0,
    'C1': 2,'C2': 2,'C3': 3,'C4': 3,
    'C5': 0,'C6': 0,'C7': 3,'C8': 0,
    'D1': 2,'D2': 4,'D3': 3,'D4': 3,
    'D5': 3,'D6': 1,'D7': 1,'D8': 3,
    'E1': 2,'E2': 2,'E3': 3,'E4': 1,
    'E5': 4,'E6': 2,'E7': 2,'E8': 2,
    'F1': 4,'F2': 4,'F3': 0,'F4': 2,
    'F5': 1,'F6': 3,'F7': 4,'F8': 4,
    'G1': 1,'G2': 1,'G3': 2,'G4': 2,
    'G5': 1,'G6': 4,'G7': 1,'G8': 2,
    'H1': 3,'H2': 1,'H3': 4,'H4': 4,
    'H5': 0,'H6': 0,'H7': 4,'H8': 3
    }

    countval = 0
    maxval = 50000
    finalList = []
    while countval < maxval:
        startPosition = position_data[random.randint(0,len(position_data) - 1)]
        lookPosition = []
        sumval = 0
        countcheck = 0
        maxcheck = 10
        while countcheck < maxcheck:
            if checkVal(startPosition,lookPosition):
                startPosition = newPosition(startPosition,positioninfo)
            else:
                sumval += position_value[startPosition]
                lookPosition.append(startPosition)
                startPosition = newPosition(startPosition,positioninfo)
                countcheck+=1
        finalList.append(sumval)
        countval+=1
    finalList.sort()
    print(finalList[len(finalList)-1])
main()




