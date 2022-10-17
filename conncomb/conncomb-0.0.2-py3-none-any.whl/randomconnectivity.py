import random
import networkx as nx
import numpy as np


def randomConnectivity(G, numNodEdgP, numNodEdgC, numRandomGroups):
    """
    

    Parameters
    ----------
    G : network
        DESCRIPTION.
    numNodEdgP : data frame pG x f
        number of nodes - patient subgraphs
    numNodEdgC : data frame pG x f
        number of nodes - control subgraphs
    numRandomGroups : TYPE
        DESCRIPTION.

    Returns
    -------
    randomConnectivityControlMean : TYPE
        DESCRIPTION.
    randomConnectivityControlStd : TYPE
        DESCRIPTION.
    randomConnectivityPatientMean : TYPE
        DESCRIPTION.
    randomConnectivityPatientStd : TYPE
        DESCRIPTION.

    """
    
    #create  a list with umber of nodes
    numNodes = list(set(numNodEdgC.stack().tolist()).union(set(numNodEdgP.stack().tolist())))
    numNodes.remove(0)
    
    #calculate mean and std of randoms
    randomConnectivityMean = {}
    randomConnectivityStd = {}
    
    for n in numNodes:
        
        connectivityN=[]
        
        for i in (range(numRandomGroups)):
            randomGenes = random.sample(list(G.nodes()), n)
            
            SG = G.subgraph(randomGenes)
            
            if SG.number_of_nodes() > 1:
                connectivity = 1-(nx.number_of_isolates(SG) / SG.number_of_nodes())
            else:
                connectivity = 0
                
            connectivityN.append(connectivity)
            
        randomConnectivityMean[n] = np.mean(connectivityN)
        randomConnectivityStd[n] = np.std(connectivityN)
     
    randomConnectivityControlMean = numNodEdgC.copy()
    randomConnectivityControlStd = numNodEdgC.copy()
    randomConnectivityPatientMean = numNodEdgP.copy()
    randomConnectivityPatientStd = numNodEdgP.copy()
    
    #map number of nodes to mean and std
    for col in numNodEdgC.columns:
        randomConnectivityControlMean[col] = randomConnectivityControlMean[col].map(randomConnectivityMean)
        randomConnectivityControlStd[col] = randomConnectivityControlStd[col].map(randomConnectivityStd)
        randomConnectivityPatientMean[col] = randomConnectivityPatientMean[col].map(randomConnectivityMean)
        randomConnectivityPatientStd[col] = randomConnectivityPatientStd[col].map(randomConnectivityStd)
    
    return randomConnectivityControlMean, randomConnectivityControlStd, randomConnectivityPatientMean, randomConnectivityPatientStd












