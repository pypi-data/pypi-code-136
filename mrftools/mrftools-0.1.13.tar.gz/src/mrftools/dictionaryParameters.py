import numpy as np
import h5py
from matplotlib import pyplot as plt

DictionaryEntry = np.dtype([('T1', np.float32), ('T2', np.float32), ('B1', np.float32)])
WHITE_MATTER_3T = np.array([(0.8, 0.04, 1.)],dtype=DictionaryEntry)
GREY_MATTER_3T = np.array([(1.200, 0.065, 1.)],dtype=DictionaryEntry)
CSF_3T = np.array([(3.000, 0.500, 1.)],dtype=DictionaryEntry)

class DictionaryParameters:
    def __init__(self, name, entries=[]):
        self.name = name
        self.entries = entries

    def __str__(self):
        return "(" + str(len(self.entries)) + ")"

    def Initialize(self, T1s, T2s, B1s=[1]):
        self.entries = np.empty(len(T1s)*len(B1s), dtype=DictionaryEntry)
        if (len(T1s)!=len(T2s)):
            print("Import Failed: T1/T2 files must have identical number of entries")
            return 
        for b1Index in range(len(B1s)):
            for t1Index in range(len(T1s)):
                index = b1Index*len(T1s) + t1Index
                self.entries[index] = (T1s[t1Index], T2s[t1Index], B1s[b1Index])
        print("Dictionary Parameter set '"+ self.name + "' initialized with " + str(len(self.entries)) + " entries")
    
    def Export(self, filename, force=False):
        if ".mrf" in filename:
            outfile = h5py.File(filename, "a")
            try:
                outfile.create_group("dictionaryParameters")
            except:
                pass
            if (self.name in list(outfile["dictionaryParameters"].keys())) and not force:
                print("Dictionary Parameter set '" + self.name + "' already exists in .mrf file. Specify 'force' to overwrite")
            else:
                try:
                    del outfile["dictionaryParameters"][self.name]
                except:
                    pass
                dictionaryParameters = outfile["dictionaryParameters"].create_group(self.name)
                dictionaryParameters.attrs.create("name", self.name)
                dictionaryParameters["entries"] = self.entries
                outfile.close()
        else:
            print("Input is not a .mrf file")

    def ExportToTxt(self, baseFilepath="", includeB1=False):
        t1File = open(baseFilepath+self.name+"_T1s.txt","w")
        t2File = open(baseFilepath+self.name+"_T2s.txt","w")
        for entry in self.entries:
            t1File.write(f'{entry["T1"]:7.5f}'+"\n")
            t2File.write(f'{entry["T2"]:7.5f}'+"\n") 
        t1File.close()
        t2File.close()
        if(includeB1):
            b1File = open(baseFilepath+self.name+"_B1s.txt","w")
            for entry in self.entries:
                b1File.write(f'{entry["B1"]:7.5f}'+"\n") 
            b1File.close()
    
    def Plot(self):
        plt.plot(self.entries['T1'], self.entries['T2'])

    def GetNearestEntry(self, T1, T2, B1=1):
        T1diff = np.absolute(self.entries['T1']-T1)
        T2diff = np.absolute(self.entries['T2']-T2)
        B1diff = np.absolute(self.entries['B1']-B1)
        diffs = np.squeeze(np.dstack([T1diff,T2diff,B1diff]))
        normedDiffs = np.linalg.norm(diffs,axis=1)
        index = np.argmin(normedDiffs)
        return (index, self.entries[index])

    def GetRegionNear(self, T1, T2, B1=1, T1Radius=-1, T2Radius=-1, B1Radius=-1):
        if T1Radius == -1:
            T1Radius = T1*0.1
        if T2Radius == -1:
            T2Radius = T2*0.1
        if B1Radius == -1:
            B1Radius = B1*0.1

        T1Indices = np.squeeze(np.where(np.absolute(self.entries['T1']-T1) < T1Radius))    
        T2Indices = np.squeeze(np.where(np.absolute(self.entries['T2']-T2) < T2Radius))
        B1Indices = np.squeeze(np.where(np.absolute(self.entries['B1']-B1) < B1Radius))

        resultList = list(set(T1Indices) & set(T2Indices) & set(B1Indices))
        return (resultList, self.entries[resultList])

    @staticmethod
    def GetAvailableDictionaryParameters(filename):
        if ".mrf" in filename:
            infile = h5py.File(filename, "r")
            return list(infile["dictionaryParameters"].keys())
        else:
            print("Input is not a .mrf file")

    @staticmethod
    def Import(filename, name):
        if ".mrf" in filename:
            infile = h5py.File(filename, "r")
            dictionaryParametersGroup = infile["dictionaryParameters"][name]
            new_dictionary_parameters = DictionaryParameters(name, dictionaryParametersGroup["entries"][:])
            infile.close()
            return new_dictionary_parameters
        else:
            print("Input is not a .mrf file")

    @staticmethod
    def ImportFromTxt(name, T1Filepath, T2Filepath, B1Filepath=""):
        new_dictionary_parameters = DictionaryParameters(name)
        T1s = np.loadtxt(T1Filepath)
        T2s = np.loadtxt(T2Filepath)
        if(B1Filepath != ""):
            B1s = np.loadtxt(B1Filepath)
            new_dictionary_parameters.Initialize(T1s, T2s, B1s)
        else:
            new_dictionary_parameters.Initialize(T1s,T2s)
        return new_dictionary_parameters

    @staticmethod
    def GenerateFixedPercent(name, t1Range=(100,4000), t2Range=(1,400), percentStepSize=5, includeB1=False, b1Range=(0.5,1.5), b1Stepsize=0.05):
        new_dictionary_parameters = DictionaryParameters(name)
        T1s = []
        T2s = []
        t1 = t1Range[0]
        t2 = t2Range[0]
        while t1 <= t1Range[1]:
            T1s.append(t1/1000)
            t1 = t1*(1+(percentStepSize/100))
        while t2 <= t2Range[1]:
            T2s.append(t2/1000)
            t2 = t2*(1+(percentStepSize/100))
        pairs = []
        for t1Val in T1s:
            for t2Val in T2s:
                if(t1Val>t2Val): # Don't include pairs with T2 longer than T1
                    pairs.append((t1Val,t2Val))
        T1sFromPairs = []
        T2sFromPairs = []
        for pair in pairs:
            T1sFromPairs.append(pair[0])
            T2sFromPairs.append(pair[1])
        if(includeB1):
            B1s = np.arange(b1Range[0], b1Range[1], b1Stepsize)
            new_dictionary_parameters.Initialize(T1sFromPairs,T2sFromPairs, B1s)
        else:
            new_dictionary_parameters.Initialize(T1sFromPairs, T2sFromPairs)
        return new_dictionary_parameters

    @staticmethod
    def GenerateFixedStep(name, t1Range=(100,4000), t2Range=(1,400), fixedStepSize=1, includeB1=False, b1Range=(0.5,1.5), b1Stepsize=0.05):
        new_dictionary_parameters = DictionaryParameters(name)
        T1s = []
        T2s = []
        t1 = t1Range[0]
        t2 = t2Range[0]
        while t1 <= t1Range[1]:
            T1s.append(t1/1000)
            t1 = t1+fixedStepSize
        while t2 <= t2Range[1]:
            T2s.append(t2/1000)
            t2 = t2+fixedStepSize
        pairs = []
        for t1Val in T1s:
            for t2Val in T2s:
                if(t1Val>t2Val): # Don't include pairs with T2 longer than T1
                    pairs.append((t1Val,t2Val))
        T1sFromPairs = []
        T2sFromPairs = []
        for pair in pairs:
            T1sFromPairs.append(pair[0])
            T2sFromPairs.append(pair[1])
        if(includeB1):
            B1s = np.arange(b1Range[0], b1Range[1], b1Stepsize)
            new_dictionary_parameters.Initialize(T1sFromPairs,T2sFromPairs, B1s)
        else:
            new_dictionary_parameters.Initialize(T1sFromPairs, T2sFromPairs)
        return new_dictionary_parameters
