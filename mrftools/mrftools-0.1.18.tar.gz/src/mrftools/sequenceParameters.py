from __future__ import annotations
import numpy as np
import h5py
from mrftools import SequenceType
from matplotlib import pyplot as plt


Timepoint = np.dtype([('TR', np.float32), ('TE', np.float32), ('FA', np.float32)])

class SequenceParameters:
    def __init__(self, name:str, type:SequenceType, timepoints=[]):
        self.name = name
        self.type = type
        self.timepoints = timepoints

    def __str__(self):
        return self.name + " || Type: " + self.type + " || " + str(self.timepoints)

    def Initialize(self, TRs:list(float), TEs:list(float), FAs:list(float)):
        self.timepoints = np.empty(len(TRs), dtype=Timepoint)
        if (len(TRs)!=len(TEs)) or (len(TRs)!=len(FAs)):
            print("Sequence Parameter Import Failed: TR/TE/FA files must have identical number of entries")
            return 
        for index in range(len(TRs)):
            self.timepoints[index] = (TRs[index], TEs[index], FAs[index])
        print("Sequence Parameter set '"+ self.name + "' initialized with " + str(len(self.timepoints)) + " timepoint definitions")
   
    def Export(self, filename:str, force=False):
        if ".mrf" in filename:
            outfile = h5py.File(filename, "a")
            try:
                outfile.create_group("sequenceParameters")
            except:
                pass
            if (self.name in list(outfile["sequenceParameters"].keys())) and not force:
                print("Sequence Parameter set '" + self.name + "' already exists in .mrf file. Specify 'force' to overwrite")
            else:
                try:
                    del outfile["sequenceParameters"][self.name]
                except:
                    pass
                sequenceParameters = outfile["sequenceParameters"].create_group(self.name)
                sequenceParameters.attrs.create("name", self.name)
                sequenceParameters.attrs.create("type", self.type.name)
                sequenceParameters["timepoints"] = self.timepoints
                outfile.close()
        else:
            print("Input is not a .mrf file")

    def ExportToTxt(self, baseFilepath=""):
        trFile = open(baseFilepath+self.name+"_TRs.txt","w")
        teFile = open(baseFilepath+self.name+"_TEs.txt","w")
        faFile = open(baseFilepath+self.name+"_FAs.txt","w")
        for timepoint in self.timepoints:
            trFile.write(f'{timepoint["TR"]:7.5f}'+"\n")
            teFile.write(f'{timepoint["TE"]:7.5f}'+"\n") 
            faFile.write(f'{timepoint["FA"]:7.5f}'+"\n")   
        trFile.close()
        teFile.close()
        faFile.close()

    def Plot(self, numTimepoints=-1):
        if numTimepoints == -1:
            numTimepoints = len(self.timepoints)
        plt.subplot(311)
        plt.plot(range(numTimepoints), self.timepoints['TR'][0:numTimepoints])
        plt.gca().set_title("TRs")
        plt.subplot(312)
        plt.plot(range(numTimepoints), self.timepoints['TE'][0:numTimepoints])
        plt.gca().set_title("TEs")
        plt.subplot(313)
        plt.plot(range(numTimepoints), self.timepoints['FA'][0:numTimepoints])
        plt.gca().set_title("FAs")

    @staticmethod
    def GetAvailableSequenceParameters(filename:str) -> list(str):
        if ".mrf" in filename:
            infile = h5py.File(filename, "r")
            return list(infile["sequenceParameters"].keys())
        else:
            print("Input is not a .mrf file")

    @staticmethod
    def Import(filename:str, name:str) -> SequenceParameters:
        if ".mrf" in filename:
            infile = h5py.File(filename, "r")
            sequenceParameterGroup = infile["sequenceParameters"][name]
            sequenceParameterName = sequenceParameterGroup.attrs.get("name")
            sequenceParameterType = sequenceParameterGroup.attrs.get("type")
            new_sequence = SequenceParameters(sequenceParameterName, sequenceParameterType, sequenceParameterGroup["timepoints"][:])
            infile.close()
            return new_sequence
        else:
            print("Input is not a .mrf file")

    @staticmethod
    def ImportFromTxt(name:str, type:SequenceType, trFilepath:str, teFilepath:str, faFilepath:str, baseTR = 0) -> SequenceParameters:
        new_sequence_parameters = SequenceParameters(name, type)
        TRs = np.loadtxt(trFilepath)
        TRs = TRs + baseTR
        TEs = np.loadtxt(teFilepath)
        FAs = np.loadtxt(faFilepath)
        new_sequence_parameters.Initialize(TRs, TEs, FAs)
        return new_sequence_parameters

