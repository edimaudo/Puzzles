# PuzzlOR October 2010 Home Improvement
import math
import operator

def euclidean_distance(a,b):
    c = [math.pow(a[i] - b[i],2) for i in range(len(a))]
    return round(math.sqrt(sum(c)),2)

def calc_min_distance(costdata, houseinfo):
    output = [[house,euclidean_distance(house[0],costdata)] for house in houseinfo]
    sorted_output = sorted(output,key=operator.itemgetter(0))
    return output[0]

houseinfo = [
    [[0,15000,0,5000,1000],181000],
    [[10000,15000,30000,5000,0],213000],
    [[0,15000,0,0,1000],176000],
    [[0,15000,0,0,1000],169000],
    [[10000,0,30000,0,1000],191000],
    [[10000,0,30000,0,1000],187000],
    [[0,15000,30000,0,1000],199000],
    [[0,15000,30000,5000,0],201000],
    [[0,15000,30000,0,0],200000]
    ]

costinfo = {
"New Bathroom":[10000,0,0,0,0],
"New Kitchen":[0,15000,0,0,0],
"Pool":[0,0,30000,0,0],
"Wood Floors":[0,0,0,5000,0],
"New Paint":[0,0,0,0,1000]
}

tempoutputList = [[cost,calc_min_distance(costinfo[cost], houseinfo)] for cost in costinfo]
outputlist = [[value[0],value[1][1]] for value in tempoutputList]
print(outputlist)
sorted_outputlist = sorted(outputlist,key=operator.itemgetter(1))
print(sorted_outputlist[0])
