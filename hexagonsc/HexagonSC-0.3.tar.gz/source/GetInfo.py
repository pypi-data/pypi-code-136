#%%
#main script?


from BountyToList import bountyList
from Pcropper import *
from SCRAPE import usrScrape

#%
def getInfo():

    #%
    img=imcapture()
    #display(img)
#%
    
    citList=bountyList(img)

    citNumb=len(citList)
    Info=[tuple]
    for i in range (citNumb-1):
       Info.append(tuple)
    
 #holy shit, tuple lists? 
#%

    for i in range (citNumb): #remember to equate the orgname list to get orgnames
       ed,oi=usrScrape(citList[i])
       Info[i]=[[citList[i]],[ed],[oi.get("Name")],[oi.get("Rank")]]
    return Info

#print(getInfo())
# %