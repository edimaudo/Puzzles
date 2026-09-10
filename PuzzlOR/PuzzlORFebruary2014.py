#PuzzlOR February 2014 Pizza Delivery

import random
import sys
import math

# def main():
# 	try:
# 		random.seed(123)
# 		#of drivers needed
# 		drivers = []
# 		number_of_iterations = 10000
# 		iterationsComplete = True
# 		iterationsDone = 0
# 		while(iterationsComplete):
# 			if iterationsDone = 10000:
# 				iterationsComplete = False
# 				break
# 			else:
# 				#order arrival time
# 				interarrival_time = 6.0
# 				arrival_time = int(random.expovariate(1/interarrival_time))

# 				#service rate
# 				service_rate = math.ceil(random.uniform(20,61))

# 			iterationsDone += 1
# 	except:
# 		e = sys.exc_info()
# 		print(e)
# 		sys.exit(1)		

def main():
	random.seed(12)
	interarrival_time = 6.0
	arrival_time = int(random.expovariate(1/interarrival_time))	
	print(arrival_time)

if __name__ == "__main__":
    main()

# import random
# import sys
# import math

# def main():
# 	try:
# 		random.seed(3)

# 		#data
# 		#interarrival time of 6 minutes exponentially distributed
# 		interarrival_time = 6.0
# 		arrival_time = int(random.expovariate(1/interarrival_time))

# 		#service rate
# 		service_rate = math.ceil(random.uniform(20,61))

# 		#average order delivery time < 60 minutes
# 		max_time = 60

# 		number_customers = 10

# 		workers_needed = (number_customers * service_rate)/max_time
# 		print(int(workers_needed)+1)
# 	except:
# 		e = sys.exc_info()
# 		print(e)
# 		sys.exit(1)
   

# if __name__ == "__main__":
#     main()

# #PuzzlOR February 2014 Pizza Delivery
# import random
# import sys
# import math

# """
# assumption only 1 order per round trip

# """
# def calc_avg(alist):
# 	total = 0
# 	count = 0
# 	for value in alist:
# 		if value > 0:
# 			total+=value
# 			count+=1
# 	return math.ceil(total/count)

# def calc_driver(alist):
# 	driverCount = 0
# 	total = 0
# 	for value in alist:
# 		total+=value
# 		if total  <= 60:
# 			driverCount+=1
# 		if total >= 60:
# 			total = 0
# 	return driverCount

# def main():
# 	try:
# 		random.seed(1)
# 		driver_data = []
# 		count_begin = 0
# 		count_end = 100000
# 		while (count_begin < count_end):

# 			delivery_data = []
# 			interarrival_time = 6.0/60.0

# 			amount_order = int(random.expovariate(interarrival_time))
			
# 			for value in range(0,amount_order):
# 				pickup_delivery_time = math.ceil(random.uniform(20,61))
# 				delivery_data.append(pickup_delivery_time)
			
# 			driver_data.append(calc_driver(delivery_data))
# 			count_begin+=1
# 		driver_data.sort()
# 		print(calc_avg(driver_data))

# 	except:
# 		e = sys.exc_info()
# 		print(e)
# 		sys.exit(1)
   

# if __name__ == "__main__":
#     main()



