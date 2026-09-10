# PuzzlOR February 2011
# Best Host

def main():
    people = ["Andrew","Betty","Cara","Dave","Erica","Frank"]
    arrangement = []

    validArrangement= {
    "Andrew":["Dave","Andrew","Frank"],
    "Betty":["Cara","Betty","Erica"],
    "Cara":["Betty","Cara","Frank"],
    "Dave":["Andrew","Dave","Erica"],
    "Erica":["Betty","Erica","Dave"],
    "Frank":["Andrew","Frank","Cara"]
    }

    templist = []
    templist.extend(validArrangement["Andrew"])
    while len(templist) != len(people):
        temp = validArrangement[templist[0]]
        for value in temp:
            if value not in templist:
                templist.insert(0,value)
    print(templist)
        
    

main()
