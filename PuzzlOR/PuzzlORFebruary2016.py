# PuzzlOR February 2016 Toy Builder

def main():
    profit_list = []
    #A - airplane, H-Helicpoter, C-Car
    for A in range(9):
        for H in range(8):
            for C in range(8):
                Profit = 7*A + 8*H + 5*C
                Blue = 3*A + 2*H + C
                Green = 2*A + 4*H + 2*C
                Red = A + H + 4*C
                if (Blue <= 25 and Green <= 29 and Red <= 30):
                    profit_list.append(Profit)
    print(max(profit_list))
    
if __name__ == "__main__":
    main()


