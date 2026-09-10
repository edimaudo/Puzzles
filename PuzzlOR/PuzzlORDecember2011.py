import random
#December 2011
#Dice Game

#http://www.puzzlor.com/2011-12_DiceGame.html

#goal:Which die should you choose in order to maximize your chance of winning?

#dies
diceA = [1,1,1,1,7,7]
diceB = [4,4,4,4,4,4]
diceC = [2,2,2,2,6,6]
diceD = [3,5,3,3,5,5]



def maxDice(diceA,diceB,diceC,diceD):
    randomvalA = random.randint(0,5)
    randomvalB = random.randint(0,5)
    randomvalC = random.randint(0,5)
    randomvalD = random.randint(0,5)
    
    diceAval = diceA[randomvalA]
    diceBval = diceB[randomvalB]
    diceCval = diceC[randomvalC]
    diceDval = diceD[randomvalD]
    
    tempList = []
    tempList.append(diceAval)
    tempList.append(diceBval)
    tempList.append(diceCval)
    tempList.append(diceDval)
    
    for value in tempList:
        if tempList[0] == max(tempList):
            return "A wins"
        elif tempList[1] == max(tempList):
            return "B wins"
        elif tempList[2] == max(tempList):
            return "C wins"
        else:
            return "D wins"

count = 0
wincount = []
while count < 10001:
    wincount.append(maxDice(diceA,diceB,diceC,diceD))
    count = count + 1

wincountVal = []
wincountVal.append(wincount.count("A wins"))
wincountVal.append(wincount.count("B wins"))
wincountVal.append(wincount.count("C wins"))
wincountVal.append(wincount.count("D wins"))

print (wincountVal)
print ("")
print ("After 10000 rolls choose: ")
for value in wincountVal:
    if wincountVal[0] == max(wincountVal):
        print("Choose Dice A")
        break
    elif wincountVal[1] == max(wincountVal):
        print("Choose Dice B")
        break
    elif wincountVal[2] == max(wincountVal):
        print ("Choose Dice C")
        break
    else:
        print ("Choose Dice D")
        break

