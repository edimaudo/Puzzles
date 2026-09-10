# # PuzzlOR August 2008 Markov Prison

# #1,5,6,10,11,12,16, 0.4712


# import random
# import numpy as np 
# from scipy import stats as st
# import scipy as sp


# def prisoner_move(position, prison):
# 	tempList = prison[position]
# 	tempValue = max(tempList)
# 	return tempValue

# def map_position_value(position):
# 	value = 3
# 	if position == "North":
# 		value = 0
# 	elif position == "South":
# 		value = 1
# 	elif position == "East":
# 		value = 2
# 	return value


# def guard_move(position, prison, guardType):
# 	guardPosition = ["North", "South", "East", "West"]
# 	guard1dataProbability = [0.2,0.4, 0.2, 0.2]
# 	guard2dataProbability = [0.4,0.1,0.2,0.3]
# 	guard1Position = map_position_value(np.random.choice(guardPosition,p=guard1dataProbability))
# 	guard2Position = map_position_value(np.random.choice(guardPosition,p=guard2dataProbability))
# 	nextMoves = prison[position]
# 	if guardType == "guard1":
# 		nextMove = nextMoves[guard1Position]
# 	else:
# 		nextMove = nextMoves[guard2Position]
# 	if nextMove == 0:
# 		nextMove = position
# 	return nextMove





# def main():
    
#     #prison data
#     prison = {
#     1:[0,5,0,2],
#     2:[0,6,3,1],
#     3:[0,7,4,2],
#     4:[0,8,0,3],
#     5:[1,9,6,0],
#     6:[2,10,7,5],
#     7:[3,11,8,6],
#     8:[4,12,0,7],
#     9:[5,13,10,0],
#     10:[6,14,11,9],
#     11:[7,15,12,10],
#     12:[8,16,0,11],
#     13:[9,0,14,0],
#     14:[10,0,15,13],
#     15:[11,0,16,14],
#     16:[12,0,0,15]
#     }
    
#     prison_route = {
#     1:[5,2],
#     2:[6,3,1],
#     3:[7,4,2],
#     4:[8,3],
#     5:[1,9,6],
#     6:[2,10,7,5],
#     7:[3,11,8,6],
#     8:[4,12,7],
#     9:[5,13,10],
#     10:[6,14,11,9],
#     11:[7,15,12,10],
#     12:[8,16,11],
#     13:[9,14],
#     14:[10,15,13],
#     15:[11,16,14],
#     16:[12,15]
#     }

#     countval = 0
#     maxcount = 10000
#     outcome = []
#     escape_route = []
#     while countval < maxcount:
#     	prisoner_position = []
#     	guard1Position = []
#     	guard2Position = []
#     	chase_end = False
#     	prisoner = 1
#     	guard1 = 16
#     	guard2 = 16
#     	while not chase_end:
#     		if prisoner == guard1 or prisoner == guard2:
#     			outcome.append("caught")
#     			chase_end = True
#     			break
#     		elif prisoner == 16:
#     			prisoner_position.append(16)
#     			escape_route.append(prisoner_position)
#     			outcome.append("escaped")
#     			chase_end = True
#     			break
#     		else:
#     			if prisoner not in prisoner_position:
#     				prisoner_position.append(prisoner)
#     				prisoner = prisoner_move(prisoner, prison_route)
#     			if guard1 not in guard1Position:
#     				guard1 = guard_move(guard1,prison,"guard1")
#     			if guard2 not in guard2Position:
#     				guard2 = guard_move(guard2,prison,"guard2")
#     	countval+=1
# 	print("Caught: " + str(len([value for value in outcome if value == "caught"])))
# 	print("Escaped: " +  str(len([value for value in outcome if value == "escaped"])))
# 	print(escape_route[0:5])






# if __name__ == "__main__":
#     main()


