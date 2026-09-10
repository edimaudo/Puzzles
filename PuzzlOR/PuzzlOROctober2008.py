# PuzzlOR October 2008 Noah's 3DPP

import operator

def space_left(alist,blist):
    for value in blist:
        alist[3] -= value[3]
    return alist[3]
    

def calc_size(alist):
    output = 1
    for value in alist:
        output*=value
    return output

def main():
    ark = [3,3,5]
    arkInfo = [
        ["elephant",2,[2,2,2]],
        ["cow",2,[3,2,1]],
        ["giraffe",2,[1,1,4]],
        ["fox",2,[1,1,3]],
        ["ladybug",2,[1,1,1]],
        ["Noah",1,[1,1,1]]
    ]
    fitList = []
    for info in arkInfo:
        temp = info[1] * calc_size(info[2])
        info.extend([temp])
        fitList.append(info)
    fitListIncrease = sorted(fitList,key=operator.itemgetter(3))
    fitListDecrease = sorted(fitList,key=operator.itemgetter(3),reverse=True)

    arkCalc = ["ark",1,ark,calc_size(ark)]
    
    ##packing size
    if space_left(arkCalc,fitListIncrease) < space_left(arkCalc,fitListDecrease):
        print("Choose Increasing algorithm")
    else:
        print("Choose decreasing algorithm")
    
    ##second question yes use decreasing algorithm


    



main()
