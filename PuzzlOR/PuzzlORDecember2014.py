# PuzzlOR December 2014 Electrifying
import math
import itertools
import string

def find_min(alist):
    minval = min(alist)
    val = alist.index(minval)
    return val

def generate_distance(substation,neighborhood,yVal):
    distanceCalc = 0
    templist = []
    templist2 = []
    substation0position = generate_coordinate(substation[0],yVal)
    substation1position = generate_coordinate(substation[1],yVal)
    substation2position = generate_coordinate(substation[2],yVal)
    for area in neighborhood:
        areaCalc = generate_coordinate(area,yVal)
        templist = [
        round(euclidean_distance(areaCalc,substation0position),2),
        round(euclidean_distance(areaCalc,substation1position),2),
        round(euclidean_distance(areaCalc,substation2position),2)
        ]
        distanceCalc += min(templist) 
        templist2.append(find_min(templist))
    if len(set(templist2)) != 3:
        distanceCalc = 10000
    return distanceCalc

def generate_coordinate(value,alist):
    return [int(alist.index(value[0])) + 1,int(value[1:])]
    
def generate_area(xVal,yVal):
    return [str(y) + str(x) for x in xVal for y in yVal]

def euclidean_distance(a,b):
    c = [math.pow(a[i] - b[i],2) for i in range(len(b))]
    return math.sqrt(sum(c))

def main():
    xVal = range(1,11)
    yVal = [i for i in string.ascii_uppercase[:10]]
    neighborhoods = ["A6","B2","B4","B5","B7",
                     "C5","C10","D9","E2","E6",
                     "E8","F3","F5","G8","G9",
                     "H3","H5","H7","H8","J4"]
    allList = generate_area(xVal,yVal)
    countlist = []    
    for substations in itertools.combinations(allList,3):
         tempval = generate_distance(list(substations), neighborhoods, yVal)
         countlist.append(tempval)
    output = list(set(countlist))
    output.sort()
    print(output[0])

main()
