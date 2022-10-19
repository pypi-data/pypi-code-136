import os
import cv2
import sys
import time
import torch
import argparse
import torchvision
import numpy as np
import torch.nn as nn
from sympy import true
from pathlib import Path
import torch.optim as optim
import matplotlib.pyplot as plt
from torchvision import datasets, models, transforms

#device selection
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

#external modules
from .models.fuse_layers import fuse_pretrain_model

#preprocessing module
from .preprocessing.preprocess import preprocess_and_refine_data

#main function for training
def train_classifier(dataset_path = None,classes=None,
                     classifer_name="resnet18",
                     epochs=100,batch_size = 2,num_workers=2):

    #check if dataset path not provided
    if dataset_path is None:
        print("Dataset path not provided")
        print("Process End")
        exit(0)

    #check if no of classes not provided
    if classes is None:
        print("Number of Classes not provided")
        print("Process End")
        exit(0)
    
    #check if data and classes are none
    if classes is None and dataset_path is None:
        print("Number of Classes and Dataset path not provided")
        exit(0)
        
    else:
        res_direct_pth = "exp"
        
        if not os.path.exists("runs"):
            os.mkdir("runs")
            
        save_dir = increment_path(Path("runs/"+res_direct_pth), exist_ok=False)
        print(save_dir)
        os.mkdir(os.path.join(save_dir))
        print("..........User Provided Details..........\n")
        print("Device : ",device)
        print("No of Epochs : ",epochs)
        print("No of Classes : ",classes)
        print("Dataset Path : ",dataset_path)
        print("Classifier Name : ",classifer_name)
        print("\n..........data preprocessing Started..........\n")
        
        for train_val_fol in os.listdir(dataset_path):
            if train_val_fol=="train":
                train_fol = os.path.join(dataset_path,train_val_fol)
                
                
            elif train_val_fol == "valid":
                val_fol = os.path.join(dataset_path,train_val_fol)
        
        if train_fol is not None and val_fol is not None:
            train_dataloader,test_dataloader,train_set_length,test_set_length = preprocess_and_refine_data(train_fol,
                                                                                                            val_fol,batch_size,
                                                                                                            num_workers=num_workers)
            
            print("\n..........fusing classifier layers..........\n")
            model, criterion,optimizer = fuse_pretrain_model(classifer_name,device=device,classes=classes)
            
            print("\n..........Training Started..........\n")
            train_custom_model(model,criterion, optimizer,epochs,train_dataloader,test_dataloader,train_set_length,test_set_length,
                               save_dir,classifer_name)
        
        else:
            print("The Dataset folder not include train and valid directories")





def train_custom_model(model,criterion, optimizer,epochs,train_dataloader,test_dataloader,train_set_length,test_set_length,
                       save_dir,classifer_name):
    num_epochs = epochs
    start_time = time.time() 
    
    for epoch in range(num_epochs):
        print("Epoch {} running".format(epoch))
        """ Training Phase """
        model.train()    
        running_loss = 0.  
        running_corrects = 0 
        

        for i, (inputs, labels) in enumerate(train_dataloader):
            inputs = inputs.to(device)
            labels = labels.to(device) 

            optimizer.zero_grad()
            outputs = model(inputs)
            _, preds = torch.max(outputs, 1)
            loss = criterion(outputs, labels)

            loss.backward()
            optimizer.step()
            running_loss += loss.item() * inputs.size(0)
            running_corrects += torch.sum(preds == labels.data)
        epoch_loss = running_loss / train_set_length
        epoch_acc = running_corrects / train_set_length * 100.
        print('[Train #{}] Loss: {:.4f} Acc: {:.4f}% Time: {:.4f}s'.format(epoch, epoch_loss, epoch_acc, time.time() -start_time))
       
        
        """ Testing Phase """
        model.eval()
        with torch.no_grad():
            running_loss = 0.
            running_corrects = 0
            for inputs, labels in test_dataloader:
                inputs = inputs.to(device)
                labels = labels.to(device)
                outputs = model(inputs)
                _, preds = torch.max(outputs, 1)
                loss = criterion(outputs, labels)
                running_loss += loss.item() * inputs.size(0)
                running_corrects += torch.sum(preds == labels.data)
            epoch_loss = running_loss / test_set_length
            epoch_acc = running_corrects / test_set_length * 100.
            print('[Test #{}] Loss: {:.4f} Acc: {:.4f}% Time: {:.4f}s'.format(epoch, epoch_loss, epoch_acc, time.time()- start_time))
        
        torch.save(model.state_dict(),os.path.join(save_dir,classifer_name+'_retrained.pt'))
        print("Weights saved")  
        
        
def increment_path(path, exist_ok=False, sep='', mkdir=False):
    path = Path(path) 
    if path.exists() and not exist_ok:
        path, suffix = (path.with_suffix(''), path.suffix) if path.is_file() else (path, '')

        for n in range(2, 9999):
            p = f'{path}{sep}{n}{suffix}'  
            if not os.path.exists(p):  
                break
        path = Path(p)

    if mkdir:
        path.mkdir(parents=True, exist_ok=True) 

    return path
