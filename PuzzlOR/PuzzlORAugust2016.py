# PuzzlOR Matchup August 2016

import itertools
import operator

manList = range(1,11)
womanList =range(1,11)

#Person    Politics    Hobby    Living Preference    Social
manInfo = {
1:["Liberal","Running","Rural","Introverted"],
2:["Liberal","Chess","Rural","Outgoing"],
3:["Conservative","Running","Urban","Introverted"],
4:["Liberal","Running","Rural","Introverted"],
5:["Conservative","Running","Rural","Introverted"],
6:["Conservative","Chess","Rural","Introverted"],
7:["Conservative","Chess","Urban","Introverted"],
8:["Liberal","Chess","Urban","Introverted"],
9:["Liberal","Running","Urban","Introverted"],
10:["Liberal","Running","Urban","Outgoing"]
}

womanInfo = {
1:["Conservative","Chess","Rural","Introverted"],
2:["Liberal","Running","Rural","Introverted"],
3:["Conservative","Chess","Rural","Outgoing"],
4:["Conservative","Running","Urban","Outgoing"],
5:["Conservative","Chess","Urban","Outgoing"],
6:["Liberal","Running","Urban","Introverted"],
7:["Conservative","Chess","Urban","Outgoing"],
8:["Conservative","Running","Urban","Outgoing"],
9:["Liberal","Chess","Urban","Introverted"],
10:["Liberal","Running","Rural","Introverted"]
}

def getScore(alist,blist):
    score = 0
    for value in range(len(alist)):
        if (alist[value] == blist[value]):
            score += 1
    return score

def createCombination(alist,blist):
    return list(itertools.product(alist,blist))

def checkScore(alist):
    scoreData = []
    for value in alist:
        scoreData.append([value,getScore(manInfo[value[0]],womanInfo[value[1]])])
    return scoreData

def calculateCombinationScore(alist):
    manData = []
    womanData = []
    score = 0
    for values in alist:
        if values[0][0] not in manData and values[0][1] not in womanData:
            manData.append(values[0][0])
            womanData.append(values[0][1])
            score+=values[1]
    return score
        

def main():
    combinationData = (createCombination(manList,womanList))
    scoreInfo = checkScore(combinationData)
    sorted_scoreInfo = sorted(scoreInfo,key = operator.itemgetter(1), reverse = True)
    highestMatchPairScore = (sorted_scoreInfo[0][1])
    totalMatchPairScore = calculateCombinationScore(sorted_scoreInfo)
    print(highestMatchPairScore,totalMatchPairScore)
   
if __name__ == "__main__":
    main()



