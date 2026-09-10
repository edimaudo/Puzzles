#puzzlOR June 2009 Grocery queuing 

import random
import math
import sys

def calc_avg(alist):
    return sum(alist)/len(alist)

def process_queue(queueInfo,checkoutTime):
    timeData = []
    for value in queueInfo:
        countval = 0
        maxval = value        
        while countval < maxval:
            processingTime = 0
            processingTime = random.expovariate(1.0/checkoutTime)
            timeData.append(processingTime)
            countval+=1
    return sum(timeData)
        
def assign_queue(queueInfo):
    smallestQueue = min(queueInfo)
    output = queueInfo.index(smallestQueue)
    return queueInfo[output]

def assign_customer(customers,queueInfo):
    customerCount = 1
    while customerCount < customers:
        output = assign_queue(queueInfo)
        queueInfo[output]+=1
        customerCount+=1
    return queueInfo
        

def trad_queue(customerArrival,checkOut):
    waiting_time = []
    queue1 = 0
    queue2 = 0
    queue3 = 0
    count = 0
    maxcount = 10
    while count < maxcount:
        arrivalInfo = int(random.expovariate(1.0/customerArrival))
        queueInfo = [queue1,queue2,queue3]
        customerToCheckout = assign_customer(arrivalInfo,queueInfo)
        waiting_time.append(process_queue(customerToCheckout,checkOut))
        count+=1
    return calc_avg(waiting_time)

def new_queue(cashier,customerArrival,checkOut):
    _lambda = 1.0/customerArrival
    _mu = 1.0/checkOut
    output = 0    
    for k in range(cashier-1):
        output += (1.0/math.factorial(k)) * math.pow((_lambda/_mu),k)    
    finaloutput = output + ((1.0/math.factorial(cashier)) *  (math.pow((_lambda/_mu),cashier)) * ((cashier*_mu) / ((cashier*_mu) - _lambda)))
    _p = 1.0/finaloutput
    avg_waiting_time = _p * ((_mu * math.pow(_lambda/_mu,cashier)) / ((math.factorial(cashier-1)) * (math.pow((cashier*_mu) - _lambda,2))))    
    
    return avg_waiting_time
    
def main():
    try:
        random.seed(1)
        trad= trad_queue(2,5)
        new = new_queue(3,2,5)
        print(trad,new)
        waiting_time_delta =abs(trad - new)
        print(waiting_time_delta)
    except:
        e = sys.exc_info()
        print(e)
        sys.exit(1)    


if __name__ == "__main__":
    main()