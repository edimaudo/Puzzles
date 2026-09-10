
import itertools
import math
import sys

def euclidean_distance(alist):
    a = alist[0]
    b = alist[1]
    c = [math.pow(a[i] - b[i],2) for i in range(len(b))]
    return math.sqrt(sum(c))

def calculate_distance(alist,adict):
	distance = 0
	maxvalue = len(alist)
	count = 0
	endCheck = True
	while (endCheck):
		if (count == 8):
			
			distance += euclidean_distance(adict[alist[count]]) + euclidean_distance(adict[alist[count+1]]) 
			+ euclidean_distance([adict[alist[count]][1],adict[alist[count+1]][0]])
			endCheck = False
		else:
			distance += euclidean_distance(adict[alist[count]]) + euclidean_distance(adict[alist[count+1]]) 
			+ euclidean_distance([adict[alist[count]][1],adict[alist[count + 1]][0]])
			count+=1
			
	return distance

def main():
	try:
	    areainfo = {"a":[[2,1],[5,2]],
	                "b":[[7,1],[9,4]],
	                "c":[[9,2],[6,6]],
	                "d":[[5,4],[2,3]],
	                "e":[[4,5],[7,9]],
	                "f":[[8,5],[2,4]],
	    	  		"g":[[3,7],[7,7]],
	                "h":[[4,8],[1,10]],
	    	  		"i":[[3,10],[10,7]],
	                "j":[[8,10],[9,8]]
	                }
	    areavalues = ["a","b","c","d","e","f","g","h","i","j"]

	   
	    print(min(list(calculate_distance(value,areainfo)  for value in itertools.permutations(areavalues))))

	except:
		e = sys.exc_info()
		print(e)
		sys.exit(1)



if __name__ == "__main__": 
    main()