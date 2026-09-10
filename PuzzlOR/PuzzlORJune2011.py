# PuzzlOR June 2011 Matchmaker

import itertools

def main():
    final_match = []
    # name 'eye',hair
    women = [['Name','Eyes','Hair'],[1,"brown","blonde"],
             [2,"green","brunette"],[3,"blue","black"],
            [4,"brown","black"],[5,"brown","brunette"],
            [6,"brown","black"]]
    men = [['Name','Eyes','Hair'],['A',"green","brunette"],
           ['B',"blue","blonde"],["C","brown","blonde"],
            ["D","green","brunette"],["E","green","black"],
            ["F","blue","blonde"]]
    
    for data in itertools.permutations([1,2,3,4,5,6]):
        count = 1
        match = []
        for value in data:
            m = ((women[value][1] == men[count][1] or women[value][2] == men[count][2]))
            match.append(m)
            count+=1
        if sum(match) == 6:
            final_match.append(data)
    for match in final_match:
        print(match)
        
        
if __name__ == "__main__":
    main()

#def checkVal(value,position, alist):
#    if len(alist) == 0:
#        return False
#    for val in alist:
#        if value == val[position]:
#            return True
#    return False
#
###'eye',hair
#women = [[1,"brown","blonde"],[2,"green","brunette"],[3,"blue","black"],
#[4,"brown","black"],[5,"brown","brunette"],[6,"brown","black"]]
#men = [['A',"green","brunette"],['B',"blue","blonde"],["C","brown","blonde"],
#["D","green","brunette"],["E","green","black"],["F","blue","blonde"]]
#
#women = sorted(women,key=operator.itemgetter(1,2))
#men = sorted(men,key=operator.itemgetter(1,2))
#
#finallist = []
#for man in men:
#    for woman in women:
#        if not checkVal(man[0],0,finallist) and not checkVal(woman[0],1,finallist) and (man[1] == woman[1] or man[2] == woman[2]):
#            finallist.append([man[0],woman[0]])
#print(finallist)
