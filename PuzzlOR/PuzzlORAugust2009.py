# PuzzlOR August 2009 Bridges

import itertools
import random
import math
import operator

def calculate_distance(homeWorkData,bridgeData,chosenBridges):
    distance = 0
    firstBridge = bridgeData[chosenBridges[0]]
    secondBridge = bridgeData[chosenBridges[1]]
    for value in homeWorkData:
        tempdata = [manhattan_distance(value[0],firstBridge[0]) +
        manhattan_distance(firstBridge[0],firstBridge[1]) +
        manhattan_distance(firstBridge[1],value[1]),manhattan_distance(value[0],secondBridge[0]) +
        manhattan_distance(secondBridge[0],secondBridge[1]) +
        manhattan_distance(secondBridge[1],value[1])]
        distance += min(tempdata)
    return distance

def manhattan_distance(a,b):
    c = [abs(a[i] - b[i]) for i in range(len(a))]
    return sum(c)

def main():

    bridges = ["one","two","three","four"]
    bridgeData = {
    "one":[[6,12],[8,12]],
    "two":[[6,7],[8,7]],
    "three":[[6,4],[8,4]],
    "four":[[6,2],[8,2]]
    }

    homeWorkData = [[[4,12],[12,8]],[[2,11],[10,12]],
    [[3,8],[10,5]],[[2,7],[12,2]],[[2,4],[10,2]]]

    distanceinfo = []
    for value in itertools.combinations(bridgeData,2):
        chosenBridges = list(value)
        distanceinfo.append([chosenBridges,calculate_distance(homeWorkData,bridgeData,chosenBridges)])
    sorted_distance = sorted(distanceinfo, key=operator.itemgetter(1))
    print(sorted_distance[0])



main()
