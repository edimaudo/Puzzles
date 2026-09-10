#puzzlOR Cookie bakeoff

import math
from operator import itemgetter

def euclidean_distance(a,b):
    c = [math.pow(a[i] - b[i],2) for i in range(len(a))]
    return math.sqrt(sum(c))

Batch = {
'Batch1':[[3, 4, 1], 70],
'Batch2':[[1, 4, 3], 95],
'Batch3':[[2, 2, 4], 45],
'Batch4':[[2, 1, 5], 20],
'Batch5':[[2, 3, 3], 85],
'Batch6':[[3, 2, 3], 55],
'Batch7':[[2, 5, 1], 80],
'Batch8':[[1, 1, 6], 15],
'Batch9':[[1, 5, 2], 90],
'Batch10':[[3, 3, 2], 75],
'Batch11':[[4, 2, 2], 40],
'Batch12':[[1, 3, 4], 65],
'Batch13':[[1, 6, 1], 60],
'Batch14':[[4, 1, 3], 25],
'Batch15':[[4, 3, 1], 50]
}

Recipe = {"Recipe1":[1,2,5],"Recipe2":[2,4,2],"Recipe3":[3,1,4]}

finallist = []

for b in Batch:
    finallist.append([b,euclidean_distance(Batch[b][0],Recipe["Recipe1"]),Batch[b][1],"Recipe 1"])
    finallist.append([b,euclidean_distance(Batch[b][0],Recipe["Recipe2"]),Batch[b][1],"Recipe 2"])
    finallist.append([b,euclidean_distance(Batch[b][0],Recipe["Recipe3"]),Batch[b][1], "Recipe 3"])
sorted(finallist, key=itemgetter(2), reverse=True)

templist = []
for value in finallist:
    if value[2] >= 95:
        templist.append(value)
print(sorted(templist, key=itemgetter(1,2))[0][3])




