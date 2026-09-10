# PuzzlOR April 2012 McEverywhere

import math
import itertools
import sys
import string

def generate_coordinate(value,alist):
    tempList = []
    tempVal = value[0]
    tempNum = int(value[1])
    tempVal1 = int(alist.index(tempVal)) + 1
    tempList.extend([tempVal1,tempNum])
    return tempList

def generate_area(xVal,yVal):
    return [str(x) + str(y) for x in xVal for y in yVal]

def euclidean_distance(a,b):
    c = [math.pow(a[i] - b[i],2) for i in range(len(a))]
    return round(math.sqrt(sum(c)),2)

def calc_min(alist,blist):
    if len(alist) < 1:
        output = blist
    elif len(blist) < 1:
        output = alist
    else:
        output = [min(alist[i],blist[i]) for i in range(len(blist))]
    return output

def find_min(alist):
    countval = 0
    maxcount = len(alist)
    tempOutput = []
    while countval < maxcount:
        tempOutput = calc_min(tempOutput,alist[countval])
        countval += 1
    return tempOutput

def calc_distance(position,homeinfo,xdata):
    if len(position) < 2:
        output =  [euclidean_distance(generate_coordinate(i,xdata), \
        generate_coordinate(position[0],xdata)) for  i in homeinfo]
    else:
        outputData = []
        for i in position:
            area = [euclidean_distance(generate_coordinate(i,xdata),generate_coordinate(home,xdata)) \
            for home in homeinfo]
            outputData.append(area)
        output = find_min(outputData)
    outputList = [i for i in output if i <= 4]
    if len(outputList) == len(homeinfo):
        return position
    return None
    tempOutput = [euclidean_distance(generate_coordinate(i,xdata),generate_coordinate(home,xdata)) for home in homeinfo]
    outputData.append(tempOutput)
        
    return compare_list(outputData)
   
def compare_list(alist):
    countval = 0
    tempList = []
    while countval < len(alist)-1:
        tempList = calc_min(tempList,alist[countval])
    return tempList
    
def main():
    xVal = [i for i in string.ascii_uppercase[:10]]
    yVal = range(1,11) 
    homeLocation = ["A4","A8","A9","A10","B4","B7",
    "C8","C9","D2","E1","F2","F5","F6","G5","G9",
    "H3","H5","I5","I9","J7"]

    outputData = []
    area = generate_area(xVal,yVal)
    storeNo = [1,2,3,4,5]

    for store in storeNo:
        for val in itertools.combinations(area,store):
            position = list(val)
            output = calc_distance(position,homeLocation,xVal)
            if output != None:
                outputData.append(output)
        if len(outputData) > 1:
            print(store)
            sys.exit()

main()
