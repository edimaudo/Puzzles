#August 2012
#Combination locks

#locks
lock1 = [39,6,75,88,15,57]
lock2 = [9,2,58,68,48,64]
lock3 = [29,55,16,67,8,91]
lock4 = [40,54,66,22,32,25]
lock5 = [49,1,17,41,14,30]
lock6 = [44,63,10,83,46,3]

for lockval1 in lock1:
    for lockval2 in lock2:
        for lockval3 in lock3:
            for lockval4 in lock4:
                for lockval5 in lock5:
                    for lockval6 in lock6:
                        if lockval1 + lockval2 + lockval3 + lockval4 + lockval5 + lockval6 == 419:
                            print ("The combination is " + str(lockval1) + ", " + str(lockval2) + ", " + str(lockval3) + ", "
                                   + str(lockval4) + ", " + str(lockval5) + ", " + str(lockval6))
