import pandas as pd
import numpy as np
import networkx as nx
import math
import random
from datetime import datetime
import os
from scipy import stats

from randomConnectivity import randomConnectivity



def patientBased(disease, network, networkPath, currencyMetaPer, 
        countDataPath, sampleDataPath, diseaseGenesPath, 
        upORdownRegulated, 
        minNumNodesR, numRandomGroups,
        pGRange, fRange,
        diseaseStatus_patient, diseaseStatus_control,
        method="patientBase",
        combination = "X0"):     
    
    directory = datetime.today().strftime('%d%m%Y')
    if not os.path.exists(directory):
        os.makedirs(directory)
    
# =============================================================================
# Data Import  
# =============================================================================
    ##### Network #####
    GC = nx.read_gexf(networkPath) 
    
    ##### Gene Expression Data #####
    countData = pd.read_csv(countDataPath, index_col=0)
    
    ##### Patient/Control Data #####
    sampleData = pd.read_csv(sampleDataPath, index_col=0)
    
    ##### GWAS Data #####
    diseaseGenesListEnsembl = pd.read_csv(diseaseGenesPath, index_col=0)         
    
    ##### Gene Centric Metabolic Network & Expression Data Intersection #####
    GCS = GC.subgraph(set(countData.T.index))
    
    
    
# =============================================================================
# Expression Data Cleaning            
# =============================================================================
    
    #patient & control data
    sampleDataS = sampleData.loc[countData.index]

    healthyID = list(sampleDataS[(sampleDataS["diseaseStatus"]==diseaseStatus_control)].index)
    patientID = list(sampleDataS[(sampleDataS["diseaseStatus"]==diseaseStatus_patient)].index)
    
    numSamples = np.min([len(healthyID), len(patientID)])    
    
    Controls = random.sample(healthyID, numSamples)
    Patients = random.sample(patientID, numSamples)
    
    #expression data
    expressionMetabolicS = countData.loc[Patients+Controls, list(GCS.nodes())]    
    expressionMetabolicS = expressionMetabolicS.apply(pd.to_numeric, errors='coerce')
    
    
# =============================================================================
# Connectivity    
# =============================================================================
    
    #connectivity - control
    
    connAnalysisControlAll = connectivityPatientBase(GCS, expressionMetabolicS, Controls, 
                                                  pGRange, fRange, upORdownRegulated)
    
    #connectivity - patient
    
    connAnalysisPatientsAll = connectivityPatientBase(GCS, expressionMetabolicS, Patients, 
                                                   pGRange, fRange, upORdownRegulated)
    
    
    #number of nodes
    numNodEdgC = connAnalysisControlAll[1]
    numNodEdgP = connAnalysisPatientsAll[1]
    
    #connectivity random
    randomConnectivityData = randomConnectivity(GCS, numNodEdgP, numNodEdgC, numRandomGroups)
    
    randomConnectivityControlMean = randomConnectivityData[0]
    randomConnectivityControlStd = randomConnectivityData[1]
    randomConnectivityPatientMean = randomConnectivityData[2]
    randomConnectivityPatientStd = randomConnectivityData[3]
    
# =============================================================================
# Min Number of Nodes Limit & Max Diff     
# =============================================================================
    resultDF0 = pd.DataFrame()
    
    for minNumNodes in minNumNodesR:
        
        #revise control connectivity wrt min num of nodes
        numNodEdgBinC = np.where(numNodEdgC<minNumNodes,0,1)
        connAnalysisControl = connAnalysisControlAll[0]*numNodEdgBinC
        
        #revise patient connectivity wrt min num of nodes
        numNodEdgBinP = np.where(numNodEdgP<minNumNodes,0,1)
        connAnalysisPatients = connAnalysisPatientsAll[0]*numNodEdgBinP
        
        #revise random connectivity wrt min num of nodes
        randomConnectivityControlMeanB = randomConnectivityControlMean * numNodEdgBinC
        randomConnectivityControlStdB = randomConnectivityControlStd * numNodEdgBinC
        randomConnectivityPatientMeanB = randomConnectivityPatientMean * numNodEdgBinP
        randomConnectivityPatientStdB = randomConnectivityPatientStd * numNodEdgBinP
        
        #avoid dividing by zero
        randomConnectivityControlStdB = randomConnectivityControlStdB.replace(0, 1)
        randomConnectivityPatientStdB = randomConnectivityPatientStdB.replace(0, 1)
        
        #calculate z-scores
        connAnalysisControl_zscore = (connAnalysisControl-randomConnectivityControlMeanB)/randomConnectivityControlStdB
        connAnalysisPatient_zscore = (connAnalysisPatients-randomConnectivityPatientMeanB)/randomConnectivityPatientStdB
        zScoreDiff = connAnalysisPatient_zscore-connAnalysisControl_zscore
     
    
        # find the index that max diff
        indexMax = list(zScoreDiff.stack().idxmax())
        #maxZscore = zScoreDiff.max().max()
       
    
        ##### Max Diff Filtered Genes #####
        pG, f = indexMax
        numGenes = GCS.number_of_nodes()
        numUpDown = math.ceil(numGenes * pG)
        
        PatientGenes = filteredGenesPatientBase(GCS, Patients, expressionMetabolicS,
                                                numUpDown, f, upORdownRegulated)
        #connectivity
        SP = GCS.subgraph(PatientGenes)        
        
        
        ##### GWAS Match #####
        Intersection = len(set(SP.nodes()).intersection(set(list(diseaseGenesListEnsembl.ensembl))))
        
        detectedDiseaseGenes = set(SP.nodes()).intersection(set(list(diseaseGenesListEnsembl.ensembl)))        
        
        diseaseGenesInGraph = len(set(GCS.nodes()).intersection(set(list(diseaseGenesListEnsembl.ensembl))))
    
    
        ##### SAVE #####
        
        resultDict = {"disease":disease, "network": network,
                    "currencyMetaPer": currencyMetaPer,
                    "upORdownRegulated": upORdownRegulated,
                    "method": method,
                    "minNumberNodes": minNumNodes, #eliminate graphs that has less than "minNumberNodes" nodes
                    "numRandomGroups":numRandomGroups,#number of randomly generated groups to estimate avg, std connectivity
                    "numNodes":GCS.number_of_nodes(),
                    "numEdges":GCS.number_of_edges(),
                    "numSamples":numSamples, #patient+control
                    
                    "numDiseaseGenes":len(diseaseGenesListEnsembl),
                    "numDiseaseGenesInGraph":diseaseGenesInGraph,
                    "numDetectedDiseaseGenes":SP.number_of_nodes(),
                    
                    "subgraphEdges":SP.number_of_edges(),
                    "maxDiffIndex_pG":indexMax[0],
                    "maxDiffIndex_f":indexMax[1],
                    
                    "maxDiffPatientConn":connAnalysisPatients.loc[pG, f],
                    "maxDiffControlConn":connAnalysisControl.loc[pG, f],
                    "maxDiffConnDiff":connAnalysisPatients.loc[pG, f]-connAnalysisControl.loc[pG, f],
                    "maxDiffPatientZScore":connAnalysisPatient_zscore.loc[pG, f],
                    "maxDiffControlZScore":connAnalysisControl_zscore.loc[pG, f],
                    "maxDiffZScoreDiff":connAnalysisPatient_zscore.loc[pG, f]-connAnalysisControl_zscore.loc[pG, f],
                    
                    "intersection":Intersection
                    }
        
        resultDF = pd.DataFrame.from_dict(resultDict, orient="index")
        resultDF0 = pd.concat([resultDF0, resultDF.T])
        
# =============================================================================
# Save         
# =============================================================================
      
        
        fn1="result/" + directory + "/"
        fn2= "_" +method + "_" + combination + "_" + disease +"_"+ network + "_" + upORdownRegulated + "_currMet" + str(currencyMetaPer*10).replace(".", "") +"_minNode"+str(minNumNodes)+ ".csv"
        
        resultDF0.to_csv(fn1+"resultSummary"+fn2)
        
        pd.DataFrame(PatientGenes).to_csv(fn1+"patientGeneList"+fn2)
        pd.DataFrame(detectedDiseaseGenes).to_csv(fn1+"detectedDiseaseGenes"+fn2)
        
        numNodEdgC.to_csv(fn1+"numberNodesControl"+fn2)
        numNodEdgP.to_csv(fn1+"numberNodesPatient"+fn2)
        
        zScoreDiff.to_csv(fn1+"zScoreDiff"+fn2)
        connAnalysisControl_zscore.to_csv(fn1+"connAnalysisControl_zscore"+fn2)
        connAnalysisPatient_zscore.to_csv(fn1+"connAnalysisPatient_zscore"+fn2)
                
                
        connAnalysisPatients.to_csv(fn1+"connAnalysisPatients"+fn2)
        connAnalysisControl.to_csv(fn1+"connAnalysisControl"+fn2)
        
        randomConnectivityControlMean.to_csv(fn1+"randomConnectivityControlMean"+fn2)
        randomConnectivityControlStd.to_csv(fn1+"randomConnectivityControlStd"+fn2)
        randomConnectivityPatientMean.to_csv(fn1+"randomConnectivityPatientMean"+fn2)
        randomConnectivityPatientStd.to_csv(fn1+"randomConnectivityPatientStd"+fn2)        
        
        
    #return resultDF0




def connectivityPatientBase(G, expressionMetabolic, Patients, 
                            pGRange, fRange, upORdownRegulated="updown"):  
    
    """
    G: gene centric metabolic network
    expressionMetabolic: expression matrix
    Patients: patients list
    pGRange: density values list
    fRange: filtering threshold values list
    minNumEdges: graphs that have less than "minNumEdges" edges will be eliminated
    """  
    
    numGenes = G.number_of_nodes()
    
    connP = pd.DataFrame(index=pGRange, columns=fRange)
    numNodEdg = pd.DataFrame(index=pGRange, columns=fRange)
   
    for pG in (pGRange):
        
        numUpDown = math.ceil(numGenes * pG)
        
        for f in fRange:

            PatientGenes = filteredGenesPatientBase(G, Patients, expressionMetabolic,
                                                    numUpDown, f, upORdownRegulated)                              
            
            #connectivity
            SP = G.subgraph(PatientGenes)
            
            if SP.number_of_nodes() > 1:
                connectivityP = 1-(nx.number_of_isolates(SP) / SP.number_of_nodes())
            else:
                connectivityP=0

            connP.loc[pG, f] = connectivityP
            numNodEdg.loc[pG, f] = SP.number_of_nodes()#, SP.number_of_edges())
            
    connP = connP.apply(pd.to_numeric, errors='coerce')
            
    return connP, numNodEdg

def filteredGenesPatientBase(G, Patients, expressionMetabolic, numUpDown, f, upORdownRegulated):
    
    """
    G: gene centric metabolic network
    Patients: patients list
    expressionMetabolic: expression matrix
    numUpDown: number of up/down regulated genes
    f: filtering threshold
    """
    
    allDiseaseRelated={}
    #connectivityPatients=[]

    for i in (Patients):
        
        if upORdownRegulated == "updown":        
            z = np.abs(stats.zscore(expressionMetabolic.loc[i]))
            z = pd.Series(z)
            patientGenes = list(z.sort_values(ascending=False).head(numUpDown).index)
        elif upORdownRegulated == "up":
            z = stats.zscore(expressionMetabolic.loc[i])
            z = pd.Series(z)
            patientGenes = list(z.sort_values(ascending=False).head(numUpDown).index)           
        elif upORdownRegulated == "down":
            z = stats.zscore(expressionMetabolic.loc[i])
            z = pd.Series(z)
            patientGenes = list(z.sort_values(ascending=False).tail(numUpDown).index)

        #count each gene
        for ii in patientGenes:
            if ii in allDiseaseRelated.keys():
                allDiseaseRelated[ii]=allDiseaseRelated[ii]+1
            else:
                allDiseaseRelated[ii]=1

    filteredPatientGenesList=[]

    if f >=0:
        for (key, value) in allDiseaseRelated.items():
            if value>=f:
                filteredPatientGenesList.append(key)
    elif f < 0:
        for (key, value) in allDiseaseRelated.items():
            if value<=-f:
                filteredPatientGenesList.append(key)
    
    return filteredPatientGenesList