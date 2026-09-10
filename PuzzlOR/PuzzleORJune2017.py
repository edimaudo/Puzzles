
#PuzzlOR June 2017
#https://pubsonline.informs.org/do/10.1287/orms.2017.03.22/full/


import math
import random
from collections import Counter
import operator

# route position and cost
route_position_cost = 
{
    1:[[2,0]]
    2:[[3,0],[17,0]],
    3:[[5,],[4]],
    4:[[3],[4]],
    5:[[3],[4]],
    6:[[3],[4]],
    7:[[3],[4]],
    8:[[3],[4]],
    9:[[3],[4]],
    10:[[3],[4]],
    11:[[3],[4]],
    12:[[3],[4]],
    13:[[3],[4]],
    14:[[3],[4]],
    15:[[3],[4]],
    16:[[3],[4]],
    17:[[18,0]],
    18:[[3],[4]],
    19:[[3],[4]],
    20:[[3],[4]],
    21:[[3],[4]],
    22:[[3],[4]],
    23:[[3],[4]],
    24:[[3],[4]],
    25:[[3],[4]],
    26:[[3],[4]],
    27:[[3],[4]],
    28:[[3],[4]],
    29:[[3],[4]],
    30:[[3],[4]]

}

def generate_random(alist):
    return random.randint(0,len(alist)-1)

def main():
    route = []
    cost = 0
    start_cost = 1000
    min_count = 0
    max_count = 10000
    start_posiiton = 1
    end_position = 31
    simulation_check = True

    while min_count < max_count:
        while simulation_check:
            if start_posiiton = 1:
                new_position_cost = route_position_cost[start_posiiton]
                simulation_check = False
            else:
                pass
                simulation_check = False
        # update cost
        # update position


        min_count = min_count + 1


    


if __name__ = "__main__":
    main()



