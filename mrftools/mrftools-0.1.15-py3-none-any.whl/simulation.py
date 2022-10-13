import numpy as np
import numba
from numba import jit
import h5py
from matplotlib import pyplot as plt

from mrftools import DictionaryParameters, SequenceParameters

class Simulation: 
    def __init__(self,sequenceParameters, dictionaryParameters, name="", numTimepoints = -1, phaseRange=(-2*np.pi, 2*np.pi), numSpins=1, results=[], truncationMatrix=[], truncatedResults=[]):
        self.sequenceParameters = sequenceParameters
        self.dictionaryParameters = dictionaryParameters
        if numTimepoints == -1:
            numTimepoints = len(sequenceParameters.timepoints)
        self.numTimepoints = numTimepoints
        self.phaseRange = phaseRange
        self.numSpins = numSpins
        self.results = results
        self.truncationMatrix = truncationMatrix
        self.truncatedResults = truncatedResults
        if not name:
            self.name = sequenceParameters.name + "_" + dictionaryParameters.name + "_" + str(numSpins) # Doesn't account for phase range
        else:
            self.name = name

    @staticmethod
    @jit(parallel=True, nopython=True)
    def ExecuteNumbaSimulation(numTimepoints,T1s,T2s,B1s,TRs,TEs,FAs,phaseValues):

        numberOfExperiments = np.int32(numTimepoints)         
        numberOfDictionaryEntries = len(T1s)
        numberOfSpins = len(phaseValues)
        FAs = np.radians(FAs)
        Mx0 = np.zeros((numTimepoints,numberOfDictionaryEntries,numberOfSpins))
        My0 = np.zeros((numberOfExperiments,numberOfDictionaryEntries,numberOfSpins))
        Mz0 = np.zeros((numberOfExperiments,numberOfDictionaryEntries,numberOfSpins))
        phaseValueCosines = np.cos(phaseValues)
        phaseValueSines = np.sin(phaseValues)
                            
        for dictionaryEntryNumber in numba.prange(0,numberOfDictionaryEntries):
            
            T1 = T1s[dictionaryEntryNumber]
            T2 = T2s[dictionaryEntryNumber]
            B1 = B1s[dictionaryEntryNumber]
            
            Mx = np.zeros(numberOfSpins)
            My = np.zeros(numberOfSpins)
            Mz = np.zeros(numberOfSpins)
            Mz[:] = -0.95
            
            for iTimepoint in range(numTimepoints):
                fa = FAs[iTimepoint] * B1
                tr = TRs[iTimepoint]
                te = TEs[iTimepoint]
                tre = tr-te
                
                At2te = np.exp(-1*te/T2)
                At1te = np.exp(-1*te/T1)
                Bt1te = 1-At1te
                
                At2tr = np.exp(-1*tre/T2)
                At1tr = np.exp(-1*tre/T1)
                Bt1tr = 1-At1tr
            
                crf = np.cos(fa)
                srf = np.sin(fa)

                # Applying flip angle 
                Myi = My
                Mzi = Mz
                My = np.multiply(crf,Myi)-np.multiply(srf,Mzi)
                Mz = np.multiply(srf,Myi)+np.multiply(crf,Mzi)

                # Relaxation over TE
                Mx = np.multiply(Mx,At2te)
                My = np.multiply(My,At2te)
                Mz = np.multiply(Mz,At1te)+Bt1te

                # Reading value after TE and before TRE
                Mx0[iTimepoint,dictionaryEntryNumber,:]=Mx[:]
                My0[iTimepoint,dictionaryEntryNumber,:]=My[:]
                Mz0[iTimepoint,dictionaryEntryNumber,:]=Mz[:]

                # Relaxation over TRE (TR-TE) 
                Mx = Mx*At2tr
                My = My*At2tr
                Mz = Mz*At1tr+Bt1tr

                # Applying off-resonance to spins
                Mxi = Mx
                Myi = My
                Mx = np.multiply(phaseValueCosines,Mxi) - np.multiply(phaseValueSines,Myi)
                My = np.multiply(phaseValueSines,Mxi) + np.multiply(phaseValueCosines,Myi)

        return Mx0,My0,Mz0
        
    @staticmethod
    @jit(parallel=True, nopython=True)
    def ParallizedMeans(Mx0,My0,Mz0):
        MeansXo = np.zeros((np.shape(Mx0)[0],np.shape(Mx0)[1]))
        MeansYo = np.zeros((np.shape(Mx0)[0],np.shape(Mx0)[1]))
        MeansZo = np.zeros((np.shape(Mx0)[0],np.shape(Mx0)[1]))

        for n in numba.prange(np.shape(Mx0)[1]):
            for timepoint in range(np.shape(Mx0)[0]):
                MeansXo[timepoint,n] = np.mean(Mx0[timepoint,n,:])
                MeansYo[timepoint,n] = np.mean(My0[timepoint,n,:])
                MeansZo[timepoint,n] = np.mean(Mz0[timepoint,n,:])
        return MeansXo, MeansYo, MeansZo

    def Execute(self, numBatches = 1):
        TRs = []
        TEs = []
        FAs = []
        T1s= []
        T2s = []
        B1s = []

        for timepoint in self.sequenceParameters.timepoints:
            TRs.append(timepoint['TR'])
            TEs.append(timepoint['TE'])
            FAs.append(timepoint['FA'])

        phaseValues = np.linspace(self.phaseRange[0], self.phaseRange[1], self.numSpins)
        dictEntriesPerBatch = int(len(self.dictionaryParameters.entries)/numBatches)
        print("Simulating " + str(numBatches) + " batch(s) of ~" + str(dictEntriesPerBatch) + " dictionary entries")
        Mxy = np.zeros((self.numTimepoints, len(self.dictionaryParameters.entries)), np.complex128)
        for i in range(numBatches):
            firstDictEntry = i*dictEntriesPerBatch
            if i == (numBatches-1):
                lastDictEntry = len(self.dictionaryParameters.entries)
            else:
                lastDictEntry = firstDictEntry+dictEntriesPerBatch
            print("Starting Batch: " + str(i) + " (Entries " + str(firstDictEntry) + "->" + str(lastDictEntry)+ ")")
            T1s.clear();T2s.clear();B1s.clear()
            for dictionaryEntry in self.dictionaryParameters.entries[firstDictEntry:lastDictEntry]:
                T1s.append(dictionaryEntry['T1'])
                T2s.append(dictionaryEntry['T2'])
                B1s.append(dictionaryEntry['B1'])
            Mx0,My0,Mz0 = self.ExecuteNumbaSimulation(self.numTimepoints, np.asarray(T1s),np.asarray(T2s),np.asarray(B1s),np.asarray(TRs),np.asarray(TEs),np.asarray(FAs),phaseValues)
            Mx,My,Mz = self.ParallizedMeans(Mx0,My0,Mz0)
            Mxy[:,firstDictEntry:lastDictEntry] = Mx+(My*1j)
        self.results = Mxy
        return self.results

    def CalculateSVD(self, truncationNumber):
        dictionary = self.results.transpose()
        dictionaryNorm = np.sqrt(np.sum(np.power(np.abs(dictionary[:,:]),2),1))
        dictionaryShape = np.shape(dictionary)
        normalizedDictionary = np.zeros_like(dictionary)
        for i in range(dictionaryShape[0]):
            normalizedDictionary[i,:] = dictionary[i,:]/dictionaryNorm[i]
        (u,s,v) = np.linalg.svd(normalizedDictionary, full_matrices=False)
        vt = np.transpose(v)
        self.truncationMatrix = vt[:,0:truncationNumber]
        self.truncatedResults = np.matmul(normalizedDictionary,self.truncationMatrix).transpose()

    def Export(self, filename, force=False, includeFullResults=True, includeSVDResults=True):
        if ".mrf" in filename:
            outfile = h5py.File(filename, "a")
            try:
                outfile.create_group("simulations")
            except:
                pass
            if (self.name in list(outfile["simulations"].keys())) and not force:
                print("Simulation '" + self.name + "' already exists in .mrf file. Specify 'force' to overwrite")
            else:
                try:
                    del outfile["simulations"][self.name]
                except:
                    pass
                simulation = outfile["simulations"].create_group(self.name)
                simulation.attrs.create("name", self.name)
                simulation.attrs.create("numTimepoints", self.numTimepoints)
                simulation.attrs.create("phaseRange", self.phaseRange)
                simulation.attrs.create("numSpins", self.numSpins)
                self.sequenceParameters.Export(filename, force)
                simulation["sequenceParameters"] = outfile["/sequenceParameters/"+self.sequenceParameters.name]
                self.dictionaryParameters.Export(filename, force)
                simulation["dictionaryParameters"] = outfile["/dictionaryParameters/"+self.dictionaryParameters.name]
                if(includeFullResults):
                    simulation["results"] = self.results
                else:
                    simulation["results"] = []
                if(includeFullResults):
                    simulation["truncationMatrix"] = self.truncationMatrix
                    simulation["truncatedResults"] = self.truncatedResults
                else:
                    simulation["truncationMatrix"] = []
                    simulation["truncatedResults"] = []

                outfile.close()
        else:
            print("Input is not a .mrf file")

    def Plot(self, numTimepoints=-1, dictionaryEntryNumbers=[], plotTruncated=False):
        if numTimepoints == -1:
            numTimepoints = len(self.sequenceParameters.timepoints)
        if dictionaryEntryNumbers == []:
            dictionaryEntryNumbers = [int(len(self.dictionaryParameters.entries)/2)]
        ax = plt.subplot(1,1,1)
        if not plotTruncated:
            for entry in dictionaryEntryNumbers:
                plt.plot(abs(self.results[:,entry]), label=str(self.dictionaryParameters.entries[entry]))
        else:
            for entry in dictionaryEntryNumbers:
                plt.plot(abs(self.truncatedResults[:,entry]), label=str(self.dictionaryParameters.entries[entry]))
        ax.legend()

    def GetAverageResult(self, indices):
        return np.average(self.results[:,indices], 1)

    def FindPatternMatches(self, querySignals, useSVD=False, truncationNumber=25):
        if querySignals.ndim == 1:
            querySignals = querySignals[:,None]
        if not useSVD:
            querySignalsTransposed = querySignals.transpose()
            normalizedQuerySignal = querySignalsTransposed / np.linalg.norm(querySignalsTransposed, axis=1)[:,None]
            simulationResultsTransposed = self.results.transpose()
            normalizedSimulationResultsTransposed = simulationResultsTransposed / np.linalg.norm(simulationResultsTransposed, axis=1)[:,None]
            innerProducts = np.inner(normalizedQuerySignal, normalizedSimulationResultsTransposed)
            return np.argmax(abs(innerProducts), axis=1)
        else:
            if self.truncatedResults[:] == []:
                self.CalculateSVD(truncationNumber)
            signalsTransposed = querySignals.transpose()
            signalSVDs = np.matmul(signalsTransposed, self.truncationMatrix)
            normalizedQuerySignalSVDs = signalSVDs / np.linalg.norm(signalSVDs, axis=1)[:,None]
            simulationResultsTransposed = self.truncatedResults.transpose()
            normalizedSimulationResultsTransposed = simulationResultsTransposed / np.linalg.norm(simulationResultsTransposed, axis=1)[:,None]
            innerProducts = np.inner(normalizedQuerySignalSVDs, normalizedSimulationResultsTransposed)
            return np.argmax(abs(innerProducts), axis=1)

    @staticmethod
    def Import(filename, simulationName):
        if ".mrf" in filename:
            infile = h5py.File(filename, "r")
            simulationGroup = infile["simulations"][simulationName]
            simulationName = simulationGroup.attrs.get("name")
            simulationNumTimepoints = simulationGroup.attrs.get("numTimepoints")
            simulationPhaseRange = simulationGroup.attrs.get("phaseRange")
            simulationNumSpins = simulationGroup.attrs.get("numSpins")
            simulationResults = simulationGroup["results"][:]
            simulationTruncationMatrix = simulationGroup["truncationMatrix"][:]
            simulationTruncatedResults = simulationGroup["truncatedResults"][:]
            sequenceParametersGroup = simulationGroup["sequenceParameters"]
            importedSequenceParameters = SequenceParameters(sequenceParametersGroup.attrs.get("name"), sequenceParametersGroup["timepoints"][:])
            dictionaryParametersGroup = simulationGroup["dictionaryParameters"]
            importedDictionaryParameters = DictionaryParameters(dictionaryParametersGroup.attrs.get("name"), dictionaryParametersGroup["entries"][:])
            new_simulation = Simulation(importedSequenceParameters, importedDictionaryParameters, simulationName, simulationNumTimepoints, simulationPhaseRange, simulationNumSpins, simulationResults, simulationTruncationMatrix, simulationTruncatedResults)
            infile.close()
            return new_simulation
        else:
            print("Input is not a .mrf file")
    
    @staticmethod
    def GetAvailableSimulations(filename):
        if ".mrf" in filename:
            infile = h5py.File(filename, "r")
            return list(infile["simulations"].keys())
        else:
            print("Input is not a .mrf file")

