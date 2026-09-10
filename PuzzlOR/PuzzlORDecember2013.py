# golf queueing

import math
import random
import sys
import random

#3 min
#FIFO
def main():
	try:
		random.seed(1)
		time_total = 0
		count_begin = 0
		count_end = 100
		while(count_begin < count_end):
			hole_begin = 1
			hole_end = 9
			while hole_begin <= hole_end:

				inter_arrival_time = 10.0
				time_info = random.expovariate(1.0/inter_arrival_time)
				
				#skill in minutes
				player_skill = [5,7,10]

				#select player
				player_choice = random.random()
				
				if player_choice <= 0.33:
					player_time = random.normalvariate(player_skill[0],1)
				elif player_choice <= 0.66:
					player_time = random.normalvariate(player_skill[1],1)
				else:
					player_time = random.normalvariate(player_skill[2],1)
				hole_begin+=1
				time_total+=time_info + player_time 
			count_begin+=1

		print(time_total)


	except:
		e = sys.exc_info()
		print(e)
		sys.exit(1)

if __name__ == "__main__":
	main()