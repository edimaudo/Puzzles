# PuzzlOR April 2013 Subs and Battleship

import math
from scipy.optimize import linear_sum_assignment
import numpy as np

def euclidean_distance(a,b):
    c = [math.pow(a[i] - b[i],2) for i in range(len(b))]
    return round(math.sqrt(sum(c)),2)

def get_distance(sub,ships):
    return [euclidean_distance(sub,ship)for ship in ships]

def main():
    
    subs = [[1, 1], [2, 2], [2, 6], [4, 2], [4, 3], 
            [4, 7], [6, 1], [7, 1], [7, 4], [9, 1], 
            [9, 5], [9, 7], [10, 2], [10, 3], [10, 6]]    
    ships = [[2, 1], [3, 4], [4, 9], [6, 1], [6, 2], 
             [6, 3], [6, 5], [6, 8], [7, 5], [7, 6], [7, 8], 
             [8, 7], [10, 1], [10, 4], [10, 1]]

    distance = [get_distance(sub,ships) for sub in subs]
    cost = np.array(distance)
    row_ind, col_ind = linear_sum_assignment(cost)
    print(row_ind)
    print(col_ind)
    print(cost[row_ind, col_ind].sum())


if __name__ == "__main__": 
    main() 