#
#Hexagon image-to-json (ITJ)
# this is a program that will take the most recent Printscreen(taken from star citizen)
#and export pertinant text from that image to the webscraper
#Author: Tracey Gibson
#%%
#image loading library


import cv2
#image to string library
from pytesseract import pytesseract
import numpy as np


#Image Processor


#Colors for scan screen
#Type  R  G  B
#Model=np.flip([39, 143, 224])
#Health=np.flip([ 87, 243, 216])
#Pilot=np.flip([ 135, 55, 240])
#Owner=np.flip([ 255, 59, 57])

#image to string
def its(img): 
    return pytesseract.image_to_string(img)

def gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def gBlur(img):
    return cv2.GaussianBlur(img,(2,2),cv2.BORDER_DEFAULT)

def threshold(img):
    return cv2.threshold(img,0,255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

#evaluate each pixel in the cropped image and assign it a black or white value based upon a hardcoded color

def nameExtractor(part): #Return a list of names present within the provided string, formated for the contracts list.
    Names=[]
     #name number
    while True:
        if(part.find("Suspect:")!= -1): #yes suspect
            part=part.partition("Suspect:") 
            part=part[2] #give me everything after the prefix
            name=""
            for j in range (len(part)):#create the name string
                
                if(part[j+1]=='\n'):

                    break #we stop for newlines here
                #» fuckin chars man
                badChar=[' ','.','»','(',')']
                badc=False
                for i in badChar:
                    if(part[j+1]==i):
                        badc=True
                    
                if(not badc):
                    name+=part[j+1]

                

            name=[name] #why do i have to do this (lol)
            Names.extend(name)
        else: # no suspect
            break
    return Names
def colorClipper(img,Color):
    for j in range(img.shape[1]):
        for i in range(img.shape[0]):
            x,y,z=img[i,j]
            if (isColor(x,y,z,Color[0])):
                img[i,j]=[0,0,0]
            
            else:
                img[i,j]=[255,255,255]
    return img
    
def isColor(b,g,r,Color):
    #check wether or not a colored pixel is within a delta value of a color
    colorP=Color-50
    colorM=Color+50
    bul=np.all(colorP[0]<=b<=colorM[0] and colorP[1]<=g<=colorM[1] and colorP[2]<=r<=colorM[2])
    return bul


#this is where the main method sorta starts
#test image: 'Test6.png'
def bountyIdentify (img):
    #Name=np.flip([ 239, 231, 240])#the color of the text in RGB
    #Colors=np.array([Name])
    #img=cv2.imread(img) #db1
    #display("img")

    #img=colorClipper(img,Colors)
    img=cv2.bitwise_not(img)
    img=gray(img)
    img=cv2.convertScaleAbs(img,0,2)
    #img=gBlur(img)
    
    #img=threshold(img)
    #--- post process debug
    #cv2.imshow("one",img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    #---
    iString = its(img)
    #print(iString)
    return nameExtractor(iString)
def bountyList(subImageList):
    nameList=[]
    for i in range (10):
        name=bountyIdentify(subImageList[i])
        nameList.extend(name)
    return nameList
#import Pcropper
#imList=Pcropper.imcapture()
#print(bountyList(imList))

#bountyIdentify(cv2.imread("test14.png")) #db1


    # %%
# %%
