# PuzzlOR June 2008
# Traveling spaceman problem

import math
import random
import itertools
import operator
from collections import Counter
from operator import itemgetter

def calc_distance(alist,valueLookUp):
    sumval = 0
    countval = 0
    while countval < len(alist)-1:
        val1 = valueLookUp[alist[countval]]
        val2 = valueLookUp[alist[countval + 1]]
        sumval += euclidean_distance(val1,val2)
        countval += 1
    return sumval

def euclidean_distance(a,b):
    c = [math.pow(a[i] - b[i],2) for i in range(len(a))]
    return math.sqrt(sum(c))

def main():

    Galaxy = {
    "a":[26,38,30],
    "b":[75,6,55],
    "c":[3,46,66],
    "d":[73,59,75],
    "e":[37,72,7],
    "f":[42,83,67],
    "g":[21,77,91],
    "h":[80,18,4]
    }

    values = ['b','c','d','e','f','g','h']
    tempvalues = []
    for arrangement in itertools.permutations(values):
        temp = list(arrangement)
        temp.insert(0,"a")
        temp.append("a")
        tempvalues.append(temp)
    finallist = []
    for value in tempvalues:
        finallist.append([calc_distance(value,Galaxy),value])
    sorted_a = sorted(finallist,key=operator.itemgetter(0))
    print(sorted_a[0][0],sorted_a[0][1][0:8])

main()


