#PuzzlOR April 2009 Dance scheduling
import operator

def validPair(pair,alist):
	for value in alist:
		if pair[0] == value[0] or pair[1]==value[1]:
			return False
	return True

def main():
	dancePairs = [
	["Daniel","Mr. Brown",2],
	["Camila","Mr. Davis",4],
	["Brianna", "Ms. Evans",2],
	["Eve", "Ms. Clark", 3],
	["Ava", "Ms. Anderson",1],
	["Camila", "Ms Clark", 5],
	["Ava", "Mr. Davis", 3],
	["Eve", "Ms. Evans",1],
	["Camila", "Ms. Anderson",4],
	["Brianna", "Mr. Davis", 3]
	]

	schedule = []
	dancePairs1 = dancePairs

	while len(dancePairs1) > 1:
		temp = []
		validheat = False
		while not validheat:
			print(1)
			if len(dancePairs1) == 1:
				temp.append(dancePairs1[0])
				schedule.append(temp)
				validheat = True
				break
			else:
				if (dancePairs1[0][0] != dancePairs1[1][0] or dancePairs1[0][1] != dancePairs1[1][1]) and (validPair(dancePairs1[0],temp) 
				 and validPair(dancePairs1[1],temp)):
				 	temp.append(dancePairs1[0])
				 	del dancePairs1[0]
				else:
					validheat = True
					schedule.append(temp)
	print(schedule)
	print(len(schedule))
				
main()
