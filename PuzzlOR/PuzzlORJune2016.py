# PuzzlOR  June 2016 Elevators

def find_first(alist):
    output = []
    for data in alist:
        if data[1] == "up":
            output.append(data[0]*15)
        elif data[1] == "down":
            output.append(data[0]*1)
        else:
            output.append(data[0]*2)
    minvalindex = output.index(min(output))
    return minvalindex
            


def main():
    testdata = [[2,"up"],[4,"stop"],[6,"down"]]
    if find_first(testdata) == 0:
        print ("A")
    elif find_first(testdata) == 1:
        print ("B")
    else:
        print ("C")
    ##print("=================")
main()


def validate():
    dataset = [
    [[8,"stop"],[5,"down"],[3,"up"]],
    [[6,"down"],[9,"stop"],[3,"up"]],
    [[9,"up"],[6,"down"],[2,"up"]],
    [[8,"stop"],[11,"down"],[8,"up"]],
    [[11,"stop"],[5,"up"],[8,"up"]],
    [[7,"down"],[4,"up"],[5,"stop"]],
    [[7,"up"],[5,"up"],[12,"stop"]],
    [[5,"down"],[8,"up"],[12,"down"]],
    [[2,"up"],[12,"stop"],[5,"up"]],
    [[7,"up"],[5,"up"],[12,"stop"]]]

    for data in dataset:
        value = find_first(data)
        if value == 0:
            print("A")
        elif value == 1:
            print("B")
        else:
            print("C")
    

#validate()