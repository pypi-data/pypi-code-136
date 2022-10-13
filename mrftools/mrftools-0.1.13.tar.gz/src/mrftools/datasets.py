import numpy as np
import numba
from numba import jit
import re
import h5py
import os
from matplotlib import pyplot as plt
import nibabel as nib
from pathlib import Path
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__

class DatasetManager: 
    def __init__(self, localDataRootDir, connectionString=None):
        self.localDataRootDir = localDataRootDir
        self.connectionString = connectionString   
    
    @staticmethod
    def loadDatasetFromFiles(t1_file, t2_file, m0_file,mprage_file, tse_file, 
                             registered_mprage_file=None, registered_tse_file=None):
        T1_img = nib.load(t1_file)
        T1 = T1_img.get_fdata()
        T2_img = nib.load(t2_file)
        T2 = T2_img.get_fdata()
        M0_img = nib.load(m0_file)
        M0 = M0_img.get_fdata()
        MPRAGE_img = nib.load(mprage_file)
        MPRAGE = MPRAGE_img.get_fdata()
        TSE_img = nib.load(tse_file)
        TSE = TSE_img.get_fdata()
        output = (T1,T2,M0,MPRAGE,TSE)
        registered_MPRAGE = None
        if(registered_mprage_file is not None):
            registered_MPRAGE_img = nib.load(registered_mprage_file)
            registered_MPRAGE = registered_MPRAGE_img.get_fdata()
            output = output + registered_MPRAGE
        registered_TSE = None
        if(registered_tse_file is not None):
            registered_TSE_img = nib.load(registered_tse_file)
            registered_TSE = registered_TSE_img.get_fdata()
            output = output + registered_TSE
        return output
    

    def saveToDataset(self, subject, scanner, set, label, nifti):
        path_base = self.localDataRootDir+"/"+subject+"/"+scanner+"/"+set
        filename = path_base + "_" + label + ".nii"
        nib.save(nifti,filename)
        
    def saveToDataset(self, subject, scanner, set, label, numpyData, niftiTransformSourceLabel):
        path_base = self.localDataRootDir+"/"+subject+"/"+scanner+"/"+set
        filename = path_base + "_" + label + ".nii"
        niftiTransformSourceFilename = path_base + "_" + niftiTransformSourceLabel + ".nii"
        niftiTransformSource = nib.load(niftiTransformSourceFilename)
        newNifti = nib.Nifti1Image(numpyData,niftiTransformSource.affine)
        nib.save(newNifti,filename)

    def loadDataset(self, subject, scanner, set, includeRegisteredMPRAGE=False, includeRegisteredTSE=False):
        path_base = self.localDataRootDir+"/"+subject+"/"+scanner+"/"+set
        registered_mprage_file = None
        if(includeRegisteredMPRAGE):
            registered_mprage_file = path_base+"_mprage_registered.nii"
        registered_tse_file = None
        if(includeRegisteredTSE):
            registered_tse_file = path_base+"_tse_registered.nii"
        return self.loadDatasetFromFiles(path_base+"_t1.nii", path_base+"_t2.nii", path_base+"_m0.nii",
                                         path_base+"_mprage.nii", path_base+"_tse.nii", registered_mprage_file, registered_tse_file)

    def fetchDatasetFromAzure(self, subject, scanner, set):
        if(self.connectionString == None):
            print("Dataset Manager Azure connection string not set.")
            return None
        else:
            blob_service_client = BlobServiceClient.from_connection_string(self.connectionString)
            container_name = "nifti-source"
            container_client = blob_service_client.get_container_client(container_name)
            uri_base = subject+"/"+scanner+"/"+set
            path_dir = self.localDataRootDir+"/"+subject+"/"+scanner
            path_base = path_dir+"/"+set
            print(path_base)
            Path(path_dir).mkdir( parents=True, exist_ok=True )
            container_client = blob_service_client.get_container_client(container= container_name) 
            with open(path_base+"_t1.nii", "wb") as download_file:
                download_file.write(container_client.download_blob(uri_base+"_t1.nii").readall())
            with open(path_base+"_t2.nii", "wb") as download_file:
                download_file.write(container_client.download_blob(uri_base+"_t2.nii").readall())
            with open(path_base+"_b1.nii", "wb") as download_file:
                download_file.write(container_client.download_blob(uri_base+"_b1.nii").readall())
            with open(path_base+"_m0.nii", "wb") as download_file:
                download_file.write(container_client.download_blob(uri_base+"_m0.nii").readall())
            with open(path_base+"_tse.nii", "wb") as download_file:
                download_file.write(container_client.download_blob(uri_base+"_tse.nii").readall())
            with open(path_base+"_mprage.nii", "wb") as download_file:
                download_file.write(container_client.download_blob(uri_base+"_mprage.nii").readall())
            return self.loadDataset(subject, scanner, set)

    def pushDatasetToAzure(self, containerName, subject, scanner, set, regex):
        if(self.connectionString == None):
            print("Dataset Manager Azure connection string not set.")
            return None
        else:
            blob_service_client = BlobServiceClient.from_connection_string(self.connectionString)
            container_name = containerName
            container_client = blob_service_client.get_container_client(container_name)
            uri_base = subject+"/"+scanner
            path_dir = self.localDataRootDir+"/"+subject+"/"+scanner
            Path(path_dir).mkdir( parents=True, exist_ok=True )
            container_client = blob_service_client.get_container_client(container= container_name) 
            files = os.listdir(path_dir)
            filesToUpload = []
            for file in files:
                if(re.search(regex,file)):
                    filesToUpload.append(file)
            for file in filesToUpload:
                filepath = path_dir+"/"+file
                uri = uri_base+"/"+file
                blob_client = blob_service_client.get_blob_client(container=container_name, blob=uri)
                # Upload the created file
                with open(filepath, "rb") as data:
                    blob_client.upload_blob(data)
                    print("Uploaded: " + uri)
                    
     
        
