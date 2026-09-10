# PuzzlOR February 2009 Supply & Demand

import math
import operator

def find_closest(position,allPosition,positionUsed,xVal):
    positionData = []
    for value in allPosition:
        if value not in positionUsed:
            positionData.append([value,euclidean_distance(generate_coordinate(position,xVal),generate_coordinate(value,xVal))])
    sortedPosition = sorted(positionData,key=operator.itemgetter(1))       
    return sortedPosition[0]
                 
def euclidean_distance(a,b):
    return math.sqrt(sum([math.pow(a[i]-b[i],2) for i in range(len(a))]))

def manhattan_distance(a,b):
    return sum([abs(a[i] - b[i]) for i in range(len(b))])

def generate_coordinate(value,alist):
    return [int(alist.index(value[0])) + 1,int(value[1])]

def generate_area(xVal,yVal):
    return [str(x) + str(y) for x in xVal for y in yVal]

def assign(factories,townsData,xVal):
    assigned = []
    townAssigned = []
    scores = []
    for factory in factories:
        checkVal = False
        while not checkVal:
            if len(townAssigned) == len(factories):
                break
            closestTown = find_closest(factory,townsData,townAssigned,xVal)
            townData = townsData[closestTown[0]]
            factoryData = factories[factory]
            if factoryData > abs(townData):
                townAssigned.append(closestTown[0])
                factories[factory]+=townData
                scores.append(factories[factory])
                townsData[closestTown[0]] = 0
                assigned.append([factory,closestTown[0]])
            elif factoryData < abs(townData):
                scores.append(factoryData)
                townsData[closestTown[0]] += factoryData
                factories[factory] = 0
                assigned.append([factory,closestTown[0]])
                checkVal = True
                break
            elif factoryData == abs(townData):
                scores.append(factoryData)
                assigned.append([factory,closestTown[0]])
                townAssigned.append(closestTown[0])
                factories[factory] = 0
                townsData[closestTown[0]] = 0
                checkVal = True                
                break
    
    distance = sum([euclidean_distance(generate_coordinate(assigned[i][0],xVal),generate_coordinate(assigned[i][1],xVal)) 
    * scores[i] for i in range(len(scores))])
    return distance*10
               

        
xVal = ["A","B","C","D","E"]
yVal = [1,2,3,4,5]
area = generate_area(xVal,yVal)

factories = {"A1":500,"A5":1000,"C3":1500,"E2":1000}
towns = {"A4":-500,"B2":-2000,"C4":-500,"E1":-1500,"E5":-500}
factoryTownData = ["A1","A5","C3","E2","A4","B2","C4","E1","E5"]

possibleArea = [i for i in area if i not in factoryTownData]
possibleAreaCapacity = 1000

outputList = []
for area in possibleArea:
    towns2 = {}
    towns2.update(towns)
    temp = {}
    temp[area] = possibleAreaCapacity
    tempFactories = temp
    tempFactories.update(factories)               
    outputList.append(assign(tempFactories,towns2,xVal))
outputList.sort()
print(outputList[0])
    

        
       

        

   





