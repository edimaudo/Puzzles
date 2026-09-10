#Puzzlor Shelter in place

import math
import itertools
import sys
import string
import operator
from operator import itemgetter

def generate_area(xVal,yVal):
    return [str(x) + str(y) for x in xVal for y in yVal]

def generate_coordinate(value,alist):
    tempList = []
    tempVal = value[0]
    tempNum = int(value[1])
    tempVal1 = int(alist.index(tempVal)) + 1
    tempList.extend([tempVal1,tempNum])
    return tempList

def manhattan_distance(a,b):
    c = [abs(a[i] - b[i]) for i in range(len(a))]
    return sum(c)

def calculate_distance(position,placeData, positionInfo):
	food_data = placeData['food']
	water_data = placeData['water']
	firewood_data = placeData['firewood']

	temp_food = [manhattan_distance(generate_coordinate(position,positionInfo),generate_coordinate(food_info,positionInfo)) for food_info in food_data]
	temp_food.sort()

	temp_water = [manhattan_distance(generate_coordinate(position,positionInfo),generate_coordinate(water_info,positionInfo)) for water_info in water_data]
	temp_water.sort()

	temp_firewood = [manhattan_distance(generate_coordinate(position,positionInfo),generate_coordinate(firewood_info,positionInfo)) for firewood_info in firewood_data]
	temp_firewood.sort()

	total_distance = 2*(temp_food[0] + (3*temp_water[0]) + (2*temp_firewood[0]))
	
	output = [position,total_distance]

	return output

def main():
	try:
		xVal = [i for i in string.ascii_uppercase[:10]]
		yVal = range(1,11)
		places = generate_area(xVal,yVal)

		items = {
		'food':["A6","E9","I9"],
		'water':["F6","G9","H3"],
		'firewood':["B10","E1","I4"]
		}

		distance_info = [calculate_distance(place,items,xVal) for place in places]
		sorted_a = sorted(distance_info,key=operator.itemgetter(1))
		print(sorted_a[0])

	except:
		e = sys.exc_info()
		print(e)
		sys.exit(1)


if __name__ == "__main__":
	main()