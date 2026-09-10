# October 2011 Movie Stars

import math
from operator import itemgetter

def euclidean_distance(a,b):
    c = [math.pow(a[i] - b[i],2) for i in range(len(a))]
    return math.sqrt(sum(c))

def main():
    movieinfo = {
    'Alex':[4,5,1,4],
    "Bill":[4,1,5,5],
    "Carla":[2,4,2,2],
    "Dan":[2,3,4,5],
    "Evan":[5,3,1,2]
    }
    people = ["Alex","Bill","Carla","Dan"]

    output = []

    PrognosisNegative  = {
    "Alex":4,
    "Bill":2,
    "Carla":4,
    "Dan":2
    }

    for key in people:
        tempval = euclidean_distance(movieinfo[key],movieinfo["Evan"])
        output.append([key,tempval])
    print("Evan rating: " + str(PrognosisNegative[sorted(output, key=itemgetter(1))[0][0]]))
     

main()
