# PuzzlOR December 2009 Fish Finder

import string
import operator
from collections import Counter

def get_resource_count(alist,fishResource):
    outputList = []
    for value in alist:
        outputList.extend(fishResource[value])
    checkVal =  Counter(outputList)
    output = []
    for value in checkVal:
        if checkVal[value] > 1:
            output.append(value)
    return(output)

def main():
    xVal = range(1,11)
    yVal = [i for i in string.ascii_uppercase[:9]]
    area = [str(y) + str(x) for x in xVal for y in yVal]

    fishSpot = {
    'A1':[],
    'B1':["shallow","sun","warm","reeds"],'C1':["shallow","sun","warm","reeds"],
    'D1':["shallow","sun","warm","reeds"],'E1':["shallow","sun","warm","reeds"],
    'F1':["shallow","sun","warm","reeds"], 'G1':["shallow","sun","cool","reeds"],
    'H1':[], 'I1':[],
    'A2':["shallow","sun","warm","reeds"],
    'B2':["shallow","sun","warm","reeds"],
    'C2':["medium","sun","warm","reeds"],'D2':["medium","sun","warm","reeds"],
    'E2':["medium","sun","warm","reeds"],'F2':["medium","sun","cool","reeds"],
    'G2':["shallow","sun","cool"], 'H2':["shallow","sun","cool"], 'I2':[],
    'A3':["shallow","sun","warm","reeds"],
    'B3':["medium","sun","warm","reeds"], 'C3':["medium","sun","warm","reeds"],
    'D3':["deep","sun","warm","reeds"], 'E3':["deep","sun","warm"],
    'F3':["medium","sun","warm"],'G3':["medium","sun","cool"],
    'H3':["shallow","shade","cool"],
    'I3':["medium","sun","cool"],
    'A4':["shallow","sun","warm","reeds"],
    'B4':["shallow","sun","warm","reeds"],
    'C4':["medium","sun","warm","reeds"],
    'D4':["medium","sun","warm"],
    'E4':["medium","sun","warm"],
    'F4':["medium","sun","warm"],
    'G4':["medium","shade","warm"],
    'H4':["medium","shade","cool"],
    'I4':["shallow","shade","cool"],
    'A5':[], 'B5':["shallow","sun","warm","reeds"],
    'C5':["shallow","sun","warm"],'D5':["shallow","sun","warm"],
    'E5':["shallow","sun","warm"],
    'F5':["medium","shade","warm"],
    'G5':["deep","shade","warm"],
    'H5':["medium","shade","cool"], 'I5':["shallow","shade","cool","reeds"],
    'A6':[], 'B6':[], 'C6':[], 'D6':[], 'E6':["shallow","shade","warm"],
    'F6':["medium","shade","cool"],
    'G6':["deep","shade","cool"],
    'H6':["medium","shade","cool","reeds"], 'I6':["shallow","shade","cool","reeds"],
    'A7':[], 'B7':[], 'C7':[], 'D7':[],
    'E7':["shallow","shade","warm"],
    'F7':["medium","shade",'warm'],
    'G7':["deep","shade","cool","reeds"],
    'H7':["medium","shade","cool","reeds"], 'I7':["shallow","shade","cool","reeds"],
    'A8':[],'B8':[], 'C8':[], 'D8':[],
    'E8':["shallow","shade","warm"],'F8':["medium","shade","warm","reeds"],
    'G8':["medium","shade","cool","reeds"],
    'H8':["medium","shade","cool","reeds"], 'I8':["shallow","shade","cool","reeds"],
    'A9':[], 'B9':[], 'C9':[], 'D9':[],
    'E9':["shallow","shade","warm","reeds"], 'F9':["shallow","shade","warm","reeds"],
    'G9':["medium","shade","cool","reeds"],
    'H9':["shallow","shade","cool","reeds"], 'I9':["shallow","shade","cool","reeds"],
    'A10':[], 'B10':[], 'C10':[], 'D10':[], 'E10':[],
    'F10':["shallow","shade","warm","reeds"],'G10':["shallow","shade","cool","reeds"],
    'H10':["shallow","shade","cool","reeds"], 'I10':[]
    }

    goodFishingSpot = ["D3","H4","E7","G9"]
    badFishingSpot = ["G1","G3","D5","G6"]

    goodSpotCharacteristics = get_resource_count(goodFishingSpot,fishSpot)
    badSpotCharacterisitics = get_resource_count(badFishingSpot,fishSpot)
    goodSpot = [i for i in goodSpotCharacteristics  if i not in badSpotCharacterisitics]
    

    output = [i for i in fishSpot if set(fishSpot[i]) == set(goodSpot)]
    print(output)
    



main()
