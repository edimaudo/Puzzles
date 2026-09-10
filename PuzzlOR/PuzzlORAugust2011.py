#PuzzlOR August 2011 Logical Hospital

import math
import random

def calc_avg(alist):
    if len(alist) == 0:
        return 0
    return sum(alist)/len(alist)

def calc_time(patientData,station):
    time_data = []    
    for patient in patientData:
        time_data_list = []
        if patient == 0:
            pass
        else:
            maxval = patient
            while maxval > 0:
                if maxval == 1:
                    time_data_list.append(random.normalvariate(21,4))
                    break
                else:
                    time_data_list.extend([random.normalvariate(21,4),random.normalvariate(21,4)])
                    maxval-=2
        time_data.append(time_data_list)
    
    avg_time = [calc_avg(value) for value in time_data]
    return (avg_time)


def main():
    count = 0
    maxcount = 1
    timelist = []
    while count < maxcount:
        #Patient Arrival
        patientInterArrival = 6
        numPatients = int(math.ceil(random.normalvariate(patientInterArrival,2)))
        patientScreen = [0,0,0]

        #Patient Assignment
        for value in range(1,numPatients):
            patientType =  round(random.random()*100,2)
            if patientType <= 33.30:
                patientScreen[0]+=1
            elif patientType <= 66.60:
                patientScreen[1]+=1
            else:
                patientScreen[2]+=1

        #Prescreening
        patientER = []
        patientER.append(math.ceil(patientScreen[0] * 0.8))
        patientER.append(math.ceil(patientScreen[1] * 0.5))
        patientER.append(math.ceil(patientScreen[2] * 0.2))

        #ER station assignment
        station = 2
        #print(calc_time(patientER,station))
        timelist.append(calc_time(patientER,station))
        count+=1
    print(timelist)
    


if __name__ == '__main__':
    main()


