# PuzzlOR October 2009 Connected and Infected

import numpy as np

def calc_population(population_data):
    return round(sum([sum(value) for value in population_data]),0)

constval = 10**9		
currentBlue = 0.5 * constval		
currentRed = 0.5 * constval		
currentViolet = 4 * constval		
currentYellow = 1 * constval		
currentGreen = 0.5 * constval		
currentPopulation = currentBlue + currentRed + currentViolet + currentYellow		
+ currentGreen

population_data = [[10000,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
population_update = [[0.3,0.3,0.3,0,0],[0.3,0.3,0,0.3,0.3],[0.3,0,0.3,0,0],[0,0.3,0,0.3,0],
                     [0,0.3,0,0,0.3]]

checkVal = False                     
monthCount = 0                 
while not checkVal:
    if calc_population(np.array(population_data)) >= 0.5*currentPopulation:
        checkVal = True
        break
    else:
        monthCount+=1
        population_data = population_data + np.dot(np.array(population_data),np.matrix(population_update))
print(monthCount)



