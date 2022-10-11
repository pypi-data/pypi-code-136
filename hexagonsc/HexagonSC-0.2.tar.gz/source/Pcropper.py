#%%
#header
from time import sleep
from PIL import ImageGrab
import cv2
import numpy
import keyboard
#%%
#image capture loop
def imcapture(): #captures and autocrops an image to the contracts window
    print("\n Please press Alt+Printscreen with the contract screen active to begin an interrogation")
    while True:
        if keyboard.is_pressed("print screen"):
            break
    sleep(.5)
    img = ImageGrab.grabclipboard()
    img = numpy.array(img) 
# Convert RGB to BGR 
    img = img[:, :, ::-1].copy() 
    return cropper(img)
#%%
#cv2 image only crop
def cropper(cv2img): #dynamic cropping!11!1
    #1080x1920
    #75%x21% of total screenspace capture: use distance from center
    
    #cv2img[181:895,338:740,:] #what i want
    #maybe reduce 740 to 634
    #ratio= .5625 or 9:16
    imgHeight=cv2img.shape[0]
    imgWidth=cv2img.shape[1]
   #.172 was default
    minHeight=.16759*imgHeight
    maxHeight=imgHeight-.17129*imgHeight #suuposed to be -minheight, but tuning, lol.
    totalWidth=.2740740*imgHeight #was .37222
    centerWidthSpacer=.30185185185185187*imgHeight #was .2037037repeat
    maxWidth=imgWidth * .5 -centerWidthSpacer
    minWidth=maxWidth-totalWidth
    minWidth=round(minWidth)
    maxWidth=round(maxWidth)
    minHeight=round(minHeight)
    maxHeight=round(maxHeight)
    croppedImage=cv2img[minHeight:maxHeight,minWidth:maxWidth,:]
    #cropped list. gimme 10 seprate little shjts
    croppedList=[]
   
    for i in range (10):
        subimage=[]
        
        subMaxHeight=round((i+1)/10*croppedImage.shape[0])
        subMinHeight=round((i)/10*croppedImage.shape[0])
        subHeight=round((subMaxHeight-subMinHeight)*.3)

        case1=i==9
        if (case1):
            subimage=croppedImage[subMinHeight+subHeight:croppedImage.shape[0],:,:]

        case2=i==0
        if (case2):
            subimage=croppedImage[0+subHeight:subMaxHeight,:,:]

        if (not case1 and  not case2):
            subimage=croppedImage[subMinHeight+subHeight:subMaxHeight,:,:]
        
      
       # if(i==7):
            
        
        croppedList.append(subimage)
        
    return croppedList

#%% 
#show that image   

def display(img):
    cv2.imshow("img",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
#%%
#img=imcapture()
#display(img)
#%%
#img=cv2.imread("test5.png")
#img=cropper(img)
#display(img)
# %%
