# PuzzlOR August 2015 Moon Rover

import itertools
import numpy as np
from scipy.spatial.distance import pdist, squareform

def main():
    
    #site_name = ["A8","B3","D10","E2","G3","G6","G8","H1",'H4',"I7"]
#    site_name_position = {
#    "A8":[[1,8],3],"B3":[[2,3],3],"D6":[[4,6],0],"D10":[[4,10],5],
#    "E2":[[5,2],4],"G3":[[7,3],5],"G6":[[7,6],4],"G8":[[7,8],2],
#    "H1":[[8,1],2],'H4':[[8,4],1],"I7":[[9,7],1]
#    }
    site_location = np.array([[4,6],[1,8],[2,3],[4,10],[5,2],[7,3],[7,6],[7,8],
                              [8,1],[8,4],[9,7]])             
    site_score = [0,3,3,5,4,5,4,2,2,1,1]
    site_euclidean_distance = (squareform(pdist(site_location,"euclidean")))
    max_path_value = 0
    for path in itertools.permutations([1,2,3,4,5,6,7,8,9,10]):
        site = 0
        path_length = 0.00
        path_value = 0
        for site_data in path:
            distance = site_euclidean_distance[site][site_data]
            if(path_length+distance > 25.0):
                break
            else:
                path_length+=distance
                site = site_data
                path_value += site_score[site]
        if(path_value > max_path_value):
            max_path_value = path_value
            best_path = path
    print(max_path_value,best_path)
    
if __name__ == "__main__":
    main()
    




