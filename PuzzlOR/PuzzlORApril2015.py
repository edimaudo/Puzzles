# PuzzlOR April 2015 - Desert Island

import random
import math
import sys
import numpy as np

def secure():
	np.random.seed(1)
	secure_water_source = [0,1]
	secure_water_source_prob = [0.8,0.2]
		
	secure_water_source_death = [0,1]
	secure_water_source_death_prob = [0.70,0.30]

	build_shelter_source = [0,1]
	build_shelter_source_prob = [0.85,0.15]

	build_shelter_source_death = [0,1]
	build_shelter_death_prob = [0.85,0.15]

	secure_food_source = [0,1]
	secure_food_source_prob = [0.9,0.1]
		
	secure_food_source_death = [0,1]
	secure_food_source_death_prob = [0.95,0.05]  
		
	totalcount = 10000
	begincount = 0
	watercount = 0
	sheltercount = 0
	foodcount = 0
	maincount = 0
		
	while (begincount < totalcount):
		watercount = 0
		sheltercount = 0
		foodcount = 0
		secure_water_outcome = np.random.choice(secure_water_source,p=secure_water_source_prob)
		secure_water_death_outcome = np.random.choice(secure_water_source_death,p=secure_water_source_death_prob)
		if secure_water_outcome in[0,1] and secure_water_death_outcome == 0:
		    watercount  = 1
		secure_shelter_outcome = np.random.choice(build_shelter_source,p=build_shelter_source_prob)
		secure_shelter_death_outcome = np.random.choice(build_shelter_source_death,p=build_shelter_death_prob)
		if secure_shelter_outcome in[0,1] and secure_shelter_death_outcome == 0:
		    sheltercount = 1		    
		secure_food_outcome = np.random.choice(secure_food_source,p=secure_food_source_prob)
		secure_food_death_outcome = np.random.choice(secure_food_source_death,p=secure_food_source_death_prob)
		if secure_food_outcome in[0,1] and secure_food_death_outcome == 0:
		    foodcount = 1	
		if (watercount + sheltercount + foodcount) == 3:
			maincount+=1
		begincount+=1
	return (maincount/10000.00)



def main():
    print(secure())

if __name__ == "__main__":
    main()