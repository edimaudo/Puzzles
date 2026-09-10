# August 2010 Relief Mission

import math
import random
import operator
from collections import Counter
from operator import itemgetter


def manhattan_distance(a,b):
    c = [abs(a[i] - b[i]) for i in range(len(a))]
    return sum(c)

def euclidean_distance(a,b):
    c = [math.pow(a[i] - b[i],2) for i in range(len(a))]
    return math.sqrt(sum(c))

def average(x):
    assert len(x) > 0
    return float(sum(x)) / len(x)

def pearson_coefficient(x, y):
    assert len(x) == len(y)
    n = len(x)
    assert n > 0
    avg_x = average(x)
    avg_y = average(y)
    diffprod = 0
    xdiff2 = 0
    ydiff2 = 0
    for idx in range(n):
        xdiff = x[idx] - avg_x
        ydiff = y[idx] - avg_y
        diffprod += xdiff * ydiff
        xdiff2 += xdiff * xdiff
        ydiff2 += ydiff * ydiff

    if math.sqrt(xdiff2 * ydiff2) == 0:
        return 0
    return diffprod / math.sqrt(xdiff2 * ydiff2)



def main():
    villages = ['A5','B5','B9','B10','C1','C6','C8','C9','C10',
                'D2','D7','D10','E2','E9','F8','G2','H2','H6',
                'J8','J10']

    area = {
        'A1':[1,1],'A2':[1,2],'A3':[1,3],'A4':[1,4],
        'A5':[1,5],'A6':[1,6],'A7':[1,7],'A8':[1,8],
        'A9':[1,9],'A10':[1,10],'B1':[2,1],'B2':[2,2],
        'B3':[2,3],'B4':[2,4],'B5':[2,5],'B6':[2,6],
        'B7':[2,7],'B8':[2,8],'B9':[2,9],'B10':[2,10],
        'C1':[3,1],'C2':[3,2],'C3':[3,3],'C4':[3,4],
        'C5':[3,5],'C6':[3,6],'C7':[3,7],'C8':[3,8],
        'C9':[3,9],'C10':[3,10],'D1':[4,1],'D2':[4,2],
        'D3':[4,3],'D4':[4,4],'D5':[4,5],'D6':[4,6],
        'D7':[4,7],'D8':[4,8],'D9':[4,9],'D10':[4,10],
        'E1':[5,1],'E2':[5,2],'E3':[5,3],'E4':[5,4],
        'E5':[5,5],'E6':[5,6],'E7':[5,7],'E8':[5,8],
        'E9':[5,9],'E10':[5,10],'F1':[6,1],'F2':[6,2],
        'F3':[6,3],'F4':[6,4],'F5':[6,5],'F6':[6,6],
        'F7':[6,7],'F8':[6,8],'F9':[6,9],'F10':[6,10],
        'G1':[7,1],'G2':[7,2],'G3':[7,3],
        'G4':[7,4],'G5':[7,5],'G6':[7,6],'G7':[7,7],
        'G8':[7,8],'G9':[7,9],'G10':[7,10],
        'H1':[8,1],'H2':[8,2],'H3':[8,3],'H4':[8,4],'H5':[8,5],
        'H6':[8,6],'H7':[8,7],'H8':[8,8],'H9':[8,9],'H10':[8,10],'I1':[9,1],
        'I2':[9,2],'I3':[9,3],'I4':[9,4],'I5':[9,5],'I6':[9,6],
        'I7':[9,7],'I8':[9,8],
        'I9':[9,9],'I10':[9,10],'J1':[10,1],'J2':[10,2],
        'J3':[10,3],'J4':[10,4],'J5':[10,5],'J6':[10,6],
        'J7':[10,7],'J8':[10,8],'J9':[10,9],'J10':[10,10]
    }

    distance_calc = []
    distance_calc1 = []
    distance_calc2 = []
    for value in area:
        sumval = 0
        sumval1 = 0
        sumval2 = 0
        for village in villages:
            sumval += euclidean_distance(area[village],area[value])
            sumval1 += manhattan_distance(area[village],area[value])
            sumval2 += pearson_coefficient(area[village],area[value])
        distance_calc.append([value,sumval])
        distance_calc1.append([value,sumval1])
        distance_calc2.append([value,sumval2])
    sorted_a = sorted(distance_calc,key=operator.itemgetter(1))
    sorted_b = sorted(distance_calc1,key=operator.itemgetter(1))
    sorted_c = sorted(distance_calc2,key=operator.itemgetter(1))
    #print(sorted_a)
    print(sorted_a[0:2])
    print(sorted_b[0:2])
    print(sorted_c[0:2])
    #print(distance_calc)


main()
