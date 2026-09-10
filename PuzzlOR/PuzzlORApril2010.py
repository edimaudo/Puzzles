#PuzzlOR April 2010 Patient 21

import math
from operator import itemgetter

def euclidean_distance(a,b):
    c = [math.pow(a[i] - b[i],2) for i in range(len(a))]
    return math.sqrt(sum(c))

def main():

    patientinfo = {
    "patient1":[[0,0,1,1],"Cold"],
    "patient2":[[1,1,1,0],"Cold"],
    "patient3":[[1,1,0,1],"Cold"],
    "patient4":[[1,0,0,1],"Cold"],
    "patient5":[[1,1,0,1],"Cold"],
    "patient6":[[0,1,1,1],"Cold"],
    "patient7":[[1,0,0,1],"Cold"],
    "patient8":[[1,1,0,0],"Cold"],
    "patient9":[[0,1,0,0],"Cold"],
    "patient10":[[0,0,1,1],"Cold"],
    "patient11":[[1,0,0,1],"Flu"],
    "patient12":[[1,0,0,1],"Flu"],
    "patient13":[[0,1,1,0],"Flu"],
    "patient14":[[1,1,0,0],"Flu"],
    "patient15":[[1,0,1,0],"Flu"],
    "patient16":[[1,0,0,0],"Flu"],
    "patient17":[[1,0,0,1],"Allergies"],
    "patient18":[[0,1,1,0],"Allergies"],
    "patient19":[[0,0,1,0],"Allergies"],
    "patient20":[[1,0,1,0],"Allergies"]
    }

    patient21 = [0,1,1,1]
    symptom = [[patientinfo[patient][1],euclidean_distance(patientinfo[patient][0],patient21)]for patient in patientinfo]
    print(sorted(symptom, key=itemgetter(1)))

main()

