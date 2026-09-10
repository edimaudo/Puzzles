# PuzzlOR April 2016 Cell Towers

import itertools
import sys
import math
import string

def get_all_surrounding(positionData,positionInfo, neighborhood):
    output = []
    for i in positionData:
        output.extend(get_surrouding_position(i,positionInfo))
    tempOutput = list(set(output))
    finalOutput = [value for value in tempOutput if value in neighborhood]
    return finalOutput
        
def generate_area(xVal,yVal):
    return [str(x) + str(y) for x in xVal for y in yVal]

def get_surrouding_position(position, positionInfo):
    tempval = position[0]
    tempnum = int(position[1:])
    templistnum = []
    templistval = positionInfo[tempval]
    if tempnum == 1:
        templistnum.extend([tempnum,tempnum+1])
    elif tempnum in [2,3,4,5,6,7,8,9]:
        templistnum.extend([tempnum-1,tempnum,tempnum+1])
    elif tempnum == 10:
        templistnum.extend([tempnum-1,tempnum])
    finalist = [val + str(num) for val in templistval for num in templistnum]
    return finalist

def main():
    xVal = [i for i in string.ascii_uppercase[:10]]
    yVal = range(1,11)
    
    area = generate_area(xVal,yVal)
    
    positionInfo = {
    "A":["A","B"],
    "B":["A","B","C"],
    "C":["B","C","D"],
    "D":["C","D","E"],
    "E":["D","E","F"],
    "F":["E","F","G"],
    "G":["F","G","H"],
    "H":["G","H","I"],
    "I":["H","I","J"],
    "J":["I","J"]
    }
    neighborhoods = ["A1","A2","A4","A5","A9",
    "B4","C2","C4","C6","C10","D4","D5","D8",
    "E1","E3","E4","E5","E7","E9","E10",
    "F1","F6","F8","F10","G2","G3","G5","G6",
    "G7","G8","H2","H6","H10","I1","I6",
    "I7","I8","J1","J2","J4","J8"]
    
    towerData = [2,3,4,5,6,7,8,9,10]
    checkData = math.ceil(0.7 * len(neighborhoods))
    outputData = [positionData for positionData in area if len(get_all_surrounding([positionData],positionInfo,neighborhoods)) >= 4]    
    
    for tower in towerData:
        for areaInfo in itertools.combinations(outputData,tower):
            positionData = list(areaInfo)
            if len(get_all_surrounding(positionData,positionInfo,neighborhoods)) >= checkData:
                print(tower, positionData)
                sys.exit()

               
main()
