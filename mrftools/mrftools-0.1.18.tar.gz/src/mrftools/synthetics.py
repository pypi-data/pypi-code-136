import numpy as np
import numba
from numba import jit
import h5py
from matplotlib import pyplot as plt
import nibabel as nib
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
from mrftools import SyntheticSequenceType

class BlochSyntheticGenerator: 
    def __init__(self,type:SyntheticSequenceType,TR,TE,TI_1=-1, TI_2=-1):
        self.type = type   
        self.TR = TR
        self.TE = TE
        self.TI_1 = TI_1
        self.TI_2 = TI_2
    
    @staticmethod
    def calculateFSESignal(TR, TE, T1, T2, PD):
        return PD * np.exp(-TE/T2) * (1 - np.exp(-1*(TR-2*TE)/T1))
    
    @staticmethod
    def calculateIRSignal(TR, TE, TI, T1, T2, PD):
        return PD * np.exp(-TE/T2) * (1 - 2*np.exp(-TI/T1) + np.exp(-1*(TR-2*TE)/T1))         
    
    @staticmethod  
    def calculateDIRSignal(TR,TE,TI_1,TI_2,T1,T2,PD):
        return PD * np.exp(-TE/T2) * (1 - 2*np.exp(-TI_1/T1) + 2*np.exp(-TI_2/T1) - np.exp(-1*(TR-2*TE)/T1))

    @staticmethod  
    @jit(parallel=True, nopython=True)
    def generateSyntheticFSE(TR, TE, T1s, T2s, M0s):   
        synthetic = np.zeros(T1s.shape)
        for voxelIndex in numba.prange(0,len(T1s)):
            T1 = T1s[voxelIndex]
            T2 = T2s[voxelIndex]
            PD = M0s[voxelIndex]
            synthetic[voxelIndex] = PD * np.exp(-TE/T2) * (1 - np.exp(-1*(TR-2*TE)/T1))
        return synthetic
    
    @staticmethod      
    @jit(parallel=True, nopython=True)
    def generateSyntheticIR(TR, TE, TI_1, T1s, T2s, M0s):   
        synthetic = np.zeros(T1s.shape)
        for voxelIndex in numba.prange(0,len(T1s)):
            T1 = T1s[voxelIndex]
            T2 = T2s[voxelIndex]
            PD = M0s[voxelIndex]
            TI = TI_1
            synthetic[voxelIndex] = PD * np.exp(-TE/T2) * (1 - 2*np.exp(-TI/T1) + np.exp(-1*(TR-2*TE)/T1))         
        return synthetic
    
    @staticmethod  
    @jit(parallel=True, nopython=True)
    def generateSyntheticDIR(TR, TE, TI_1, TI_2, T1s, T2s, M0s):   
        synthetic = np.zeros(T1s.shape)
        for voxelIndex in numba.prange(0,len(T1s)):
            T1 = T1s[voxelIndex]
            T2 = T2s[voxelIndex]
            PD = M0s[voxelIndex]
            synthetic[voxelIndex] = PD * np.exp(-TE/T2) * (1 - 2*np.exp(-TI_1/T1) + 2*np.exp(-TI_2/T1) - np.exp(-1*(TR-2*TE)/T1))      
        return synthetic
    
    def generateSynthetics(self, T1s, T2s, M0s, M0_scaling_factor=1):   
        print("Beginning simulation of " + str(self.type) + " contrast")
        T1_lin = T1s.reshape((-1))
        T2_lin = T2s.reshape((-1))
        M0_lin = M0s.reshape((-1)) * M0_scaling_factor
        output_lin = None
        
        if(self.type == SyntheticSequenceType.FSE):
            output_lin = BlochSyntheticGenerator.generateSyntheticFSE(self.TR, self.TE, T1_lin, T2_lin, M0_lin)
        elif(self.type == SyntheticSequenceType.IR):
            if(self.TI_1 == -1):
                print("Inversion Time TI_1 not set for Generator.")
                return None
            else:
                output_lin = BlochSyntheticGenerator.generateSyntheticIR(self.TR, self.TE, self.TI_1, T1_lin, T2_lin, M0_lin)
        elif(self.type == SyntheticSequenceType.DIR):
            if(self.TI_1 == -1 or self.TI_2 == -1):
                print("Inversion TI_1 or TI_2 not set for Generator.")
                return None
            else:
                output_lin = BlochSyntheticGenerator.generateSyntheticDIR(self.TR, self.TE, self.TI_1, self.TI_2, T1_lin, T2_lin, M0_lin)
        print("Finished simulation")
        return output_lin.reshape(T1s.shape)
