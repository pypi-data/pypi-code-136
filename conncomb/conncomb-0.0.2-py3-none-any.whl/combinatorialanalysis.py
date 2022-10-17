

import itertools
import numpy as np
from scipy import spatial
import pandas as pd







def generateIterlist(numPatients, n):
    
    patients = [list(i) for i in itertools.product(range(2), repeat=numPatients)]
    controls = [[np.abs(value-1) for value in sublist] for sublist in patients]

    for i in range(len(patients)):
        patients[i].extend(controls[i])

    #iterlist = [list(item) for sublist in patients for item in sublist]

    iterlist = []
    for pat in patients:
        iterlist.append([i for i, e in enumerate(pat) if e == 0])
    
    distanceList = []
    for pat in patients:
        distanceList.append(spatial.distance.hamming(patients[n], pat))
    
    iterDF = pd.DataFrame(iterlist)
    distanceDF = pd.DataFrame(distanceList)

    return iterDF, distanceDF