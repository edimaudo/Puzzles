# PuzzlOR December 2015 Crazy Cake

import itertools
import math
import random
from collections import Counter
import operator

def sortlist(val):
    val.sort()
    return val

def unique_items(L):
    found = set()
    for item in L:
        if item[0] not in found:
            yield item
            found.add(item[0])

slices = [18,48,19,59,46,72,67,57,49,80,50,69,10,48,83]
person = sum(slices)/5

templist = []
for i in slices:
    for j in slices:
        for k in slices:
            if i + j + k == person:
                templist.append([i,j,k])

newtemplist = []
for value in templist:
    newtemplist.append(sortlist(value))

sorted_a = sorted(newtemplist, key=operator.itemgetter(0,1,2))
print(list(unique_items(sorted_a)))


