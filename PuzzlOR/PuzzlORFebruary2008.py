# PuzzlOR February 2008 - decision trees
import sys
import math

COLD = {"COST":500,"name":"cold", "PROB":0.5,"TEST_PROB":0.8}
FLU = {"COST":800,"name":"flu","PROB":0.2, "TEST_PROB":0.9}
BACTERIA = {"COST":1200,"name":"bacteria","PROB":0.3,"TEST_PROB":0.95}
TEST_COST = 200
PENICILLIN_COST = 50
BACTERIA_TREATED = 200


def main():


	try:
		BACTERIA_COST = BACTERIA["PROB"] * BACTERIA["TEST_PROB"] * BACTERIA["COST"]
		FLU_COST = FLU["PROB"] * FLU["TEST_PROB"] * FLU["COST"]
		COLD_COST = COLD["PROB"] * COLD["TEST_PROB"] * COLD["COST"]

		##1 if a > b else -1 
		outcome = []
		if COLD_COST > TEST_COST:
			outcome.append(0)
		else:
			outcome.append(1)
		if BACTERIA_COST > TEST_COST + PENICILLIN_COST:
			outcome.append(0)
		else:
			outcome.append(1)
		if FLU_COST > TEST_COST:
			outcome.append(0)
		else:
			outcome.append(1)		
		
		if (sum(outcome) >= 2):
			print("Yes, go to hopsital")
		else:
			print("No, don't go")
	except:
		e = sys.exc_info()
		print(e)
		sys.exit()


if __name__ == "__main__":
	main()