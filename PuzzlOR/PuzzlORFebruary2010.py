#PuzzlOR February 2010 Planet Colonisation

import operator

def get_resources(alist,resourceData,distance):
    return [[resourceData[i],distance,i] for i in alist if i in resourceData]

def generate_adjacent_position(position,positionData):
    return positionData[position]

def generate_distance(position,resourceData,positionData):
    outputList = []
    outputList2 = []
    resourceList = []
    positionList = []
    #check first position
    if position in resourceData:
        outputList.append([resourceData[position],0,position])

    adjacentPosition = generate_adjacent_position(position,positionData)
    outputList.extend(get_resources(adjacentPosition,resourceData,1))
    # generate left position
    leftPosition = generate_adjacent_position(adjacentPosition[0],positionData)
    outputList.extend(get_resources(leftPosition,resourceData,2))
    #generate middle position
    middlePosition = generate_adjacent_position(adjacentPosition[1],positionData)
    outputList.extend(get_resources(middlePosition,resourceData,2))
    #generate right position
    rightPosition = generate_adjacent_position(adjacentPosition[2],positionData)
    outputList.extend(get_resources(rightPosition,resourceData,2))

    #print(outputList)
    distanceCalc = 0
    for info in outputList:
        if info[0] not in resourceList and info[2] not in positionList:
            distanceCalc += info[1]
            resourceList.append(info[0])
            positionList.append(info[2])
    outputList2.extend([distanceCalc,resourceList])
    return outputList2

resources = {
2:"energy",
7:"food",
8:"water",
12:"energy",
14:"oxygen",
16:"water",
19:"oxygen",
20:"food",
}

positionData = {
1:[2,8,5],
2:[1,10,3],
3:[4,12,2],
4:[3,14,5],
5:[4,1,6],
6:[7,5,15],
7:[6,8,17],
8:[7,1,9],
9:[8,10,20],
10:[9,2,11],
11:[10,19,12],
12:[11,3,13],
13:[12,14,18],
14:[13,4,15],
15:[14,16,6],
16:[15,18,17],
17:[16,20,7],
18:[16,19,13],
19:[18,11,20],
20:[19,17,9]
}

landingPosition = range(1,21)

outputData = []
for position in landingPosition:
    temp = generate_distance(position,resources,positionData) + [position]
    if len(temp[1]) == 4:
        outputData.append(temp)

sortedOutpData = sorted(outputData,key=operator.itemgetter(0))
print(sortedOutpData[0][2])
