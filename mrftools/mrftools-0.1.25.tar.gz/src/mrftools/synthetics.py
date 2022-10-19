from mrftools import SyntheticSequenceType
import numpy as np
import numba
from numba import jit
import h5py
from matplotlib import pyplot as plt
import nibabel as nib
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
import tensorflow as tf
from tensorflow import keras
import tarfile
import os.path
from pathlib import Path

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

class AISyntheticGenerator: 
    def __init__(self,name,description,referenceBlochGenerator:BlochSyntheticGenerator=None, normalizeM0=True, normalizeTargetSeries=True, modelsDir="models"):
        self.name = name   
        self.description = description
        self.referenceBlochGenerator = referenceBlochGenerator
        self.normalizeM0 = normalizeM0
        self.normalizeTargetSeries = normalizeTargetSeries
        self.modelsDir=modelsDir
    
    def PrepareSequentialModel(self, normalizer=None, numUnits=32, activation='relu', loss='mean_absolute_error', optimizer:tf.keras.optimizers.Optimizer=tf.keras.optimizers.Adam(0.01)):
        if(normalizer is None):
            print("Using normalizer stored in object ")
            normalizer = self.normalizer
        self.model = tf.keras.Sequential([
            normalizer,
            tf.keras.layers.Dense(numUnits, activation=activation),
            tf.keras.layers.Dense(1)
        ])
        self.model.compile(loss=loss, optimizer=optimizer)
        self.model.summary()
        return self.model

    def PrepareTrainingData(self, root, subjects, scanners, sets, targetSeries, dataManager=None, simpleITKRunner=None, batch_size=5000, fetchFromAzure=True, flipTargetSeries=False):
        T1_lin = []; T2_lin = []; M0_lin = []; target_lin = []
        if(dataManager == None):
            print("Data Manager object not set.")
        else:
            for subject in subjects:
                for scanner in scanners:
                    for set in sets:
                        if(fetchFromAzure):
                            (T1, T2, M0) = dataManager.fetchSetFromAzure(subject, scanner, set)
                            target = dataManager.fetchSingleSeriesFromAzure(subject, scanner, set, targetSeries)
                        else:
                            (T1, T2, M0) = dataManager.loadMRFSeries(subject, scanner, set)
                            target = dataManager.loadSingleSeries(subject, scanner, set, targetSeries)
                        if(flipTargetSeries):
                            target = target[::-1, :, :]
                        if(simpleITKRunner is not None):
                            if(self.referenceBlochGenerator is not None):
                                referenceSynthetic = self.referenceBlochGenerator.generateSynthetics(T1, T2, M0)
                                dataManager.saveToSet(subject,scanner, set, targetSeries+"_reference_synthetic", referenceSynthetic, "t1")
                            else:
                                referenceSynthetic = M0 # Use M0 as synthetic image for registration if no simulator specified
                            target = simpleITKRunner.performRegistration(referenceSynthetic, target, numIterations=50)
                            dataManager.saveToSet(subject,scanner, set, targetSeries+"_registered_to_reference_synthetic", target, "t1")
                        if(self.normalizeM0):
                            M0 = M0 / np.max(M0)
                        if(self.normalizeTargetSeries):
                            target = target / np.max(target)
                        if(len(T1_lin) == 0):
                            T1_lin = T1.reshape((-1))
                        else:
                            T1_lin = np.concatenate((T1_lin, T1.reshape((-1))))
                        if(len(T2_lin) == 0):
                            T2_lin = T2.reshape((-1))
                        else:
                            T2_lin = np.concatenate((T2_lin, T2.reshape((-1))))
                        if(len(M0_lin) == 0):
                            M0_lin = M0.reshape((-1))
                        else:
                            M0_lin = np.concatenate((M0_lin, M0.reshape((-1))))
                        if(len(target_lin) == 0):
                            target_lin = target.reshape((-1))
                        else:
                            target_lin = np.concatenate((target_lin, target.reshape((-1))))  

            inputData = np.transpose([T1_lin, T2_lin, M0_lin])
            labels  = target_lin

            allIndices = np.arange(0,len(labels)-1)
            trainIndices = np.random.random_integers(0, len(labels)-1, int(len(labels) * 0.8))
            trainMask = np.isin(allIndices, trainIndices, invert=True)
            testIndices = allIndices[trainMask]

            self.trainData = inputData[trainIndices, :]
            self.trainLabels = labels[trainIndices]

            self.testData = inputData[testIndices, :]
            self.testLabels = labels[testIndices]

            self.normalizer = tf.keras.layers.Normalization(axis=-1)
            self.normalizer.adapt(self.trainData, batch_size=batch_size)

            print(self.normalizer.mean.numpy())
            first = np.array(self.trainData[:1])

            with np.printoptions(precision=2, suppress=True):
                print('First example:', first)
                print('Normalized:', self.normalizer(first).numpy())     
            return(self.normalizer, self.trainData, self.trainLabels, self.testData, self.testLabels)

    def TrainModel(self, batch_size=5000, epochs=10,verbose=0, trainData=None, trainLabels=None, testData=None, testLabels=None):
        if(trainData is None or trainLabels is None or testData is None or testLabels is None):
            print("Using train/test dataset stored in object ")
            trainData = self.trainData
            trainLabels = self.trainLabels
            testData = self.testData
            testLabels = self.testLabels
        history = self.model.fit(trainData,trainLabels,validation_data=(testData, testLabels),batch_size=batch_size,epochs=epochs,verbose=verbose)
        return history

    def SaveModel(self, compress=True):
        folder = self.modelsDir + "/" + self.name
        self.model.save(folder)  
        if(compress):
            compressedFile = folder + ".tar.gz"
            with tarfile.open(compressedFile, "w:gz") as tar:
                tar.add(folder, arcname=os.path.basename(folder))
            return compressedFile
        return folder
    
    def LoadModel(self, decompress=True):
        folder = self.modelsDir + "/" + self.name 
        if(decompress):
            compressedFile = folder+".tar.gz"
            with tarfile.open(compressedFile) as tar:
                tar.extractall(self.modelsDir)
        self.model = tf.keras.models.load_model(folder)
        return self.model       

    def LoadModelFromAzure(self, connectionString, container):
        folder = self.modelsDir + "/" + self.name
        compressedFileName = self.name+".tar.gz"
        compressedFilePath = self.modelsDir+"/"+compressedFileName
        uri = compressedFileName
        Path(self.modelsDir).mkdir( parents=True, exist_ok=True)
        blob_service_client = BlobServiceClient.from_connection_string(connectionString)
        container_client = blob_service_client.get_container_client(container=container) 
        with open(compressedFilePath, "wb") as download_file:
            download_file.write(container_client.download_blob(uri).readall())
        with tarfile.open(compressedFilePath) as tar:
            tar.extractall(self.modelsDir)
        self.model = tf.keras.models.load_model(folder)
        return self.model           

    def SaveModelToAzure(self, connectionString, container, overwrite=False):
        folder = self.modelsDir + "/" + self.name
        self.model.save(folder)  
        compressedFile = folder + ".tar.gz"
        with tarfile.open(compressedFile, "w:gz") as tar:
            tar.add(folder, arcname=os.path.basename(folder))
        uri = self.name+".tar.gz"
        blob_service_client = BlobServiceClient.from_connection_string(connectionString)
        try:
            container_client = blob_service_client.get_container_client(container)
        except Exception as e:
            container_client = blob_service_client.create_container(container)
        blob_client = blob_service_client.get_blob_client(container=container, blob=uri)
        with open(compressedFile, "rb") as data:
            blob_client.upload_blob(data, overwrite=overwrite)
            print("Uploaded: " + uri)
        return folder

    def generateSynthetics(self, T1, T2, M0, batch_size=5000):   
        print("Beginning simulation of " + str(self.name) + " contrast")
        T1_lin = T1.reshape((-1))
        T2_lin = T2.reshape((-1))
        if(self.normalizeM0):
            M0 = M0 / np.max(M0)
        M0_lin = M0.reshape((-1))
        inputData = np.transpose([T1_lin, T2_lin, M0_lin])
        outputLabels = self.model.predict(inputData, batch_size=batch_size).flatten()
        return outputLabels.reshape(T1.shape)
