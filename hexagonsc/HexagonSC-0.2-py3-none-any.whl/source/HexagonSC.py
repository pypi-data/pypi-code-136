#Ui
#%%



from tabulate import tabulate
from GetInfo import *
import os
#%%

#qq[:][1].extend("1")
#[[], ['1', '1']]
#append to add list(()) (rows)
#extend at address to add columns
clear = lambda: os.system('cls')
clear()
while True:

    while True:
    #%%
        info=getInfo()
        maxorgs=0
        orgs=0
        if (type(info[0])!=list):
            print("NO APPREHEND SUSPECT: CONTRACTS DETECTED")
            break 

        for i in range (len(info)):
            orgs=info[i][2]
            orgs=orgs[0]
            if (len(orgs)>maxorgs):
                maxorgs=len(orgs)

        #%%
        #matrix formatter
        formattedMartrix=[]
        for j in range (maxorgs+1):
            formattedMartrix.append(list(()))
        iter=0
        for i in info:
            ranks=i[3]
            ranks=ranks[0]
            orgs=i[2]
            orgs=orgs[0]
            formattedMartrix[0].extend(i[0])
            formattedMartrix[0].extend(i[1])

            case1=len(orgs) == maxorgs
            if ( case1 ):
                for j in range (maxorgs):
                    rank=[str(ranks[j])]
                    org=[str(orgs[j])]

                    formattedMartrix[j+1].extend(org)
                    formattedMartrix[j+1].extend(rank)

            case2=len(orgs)<maxorgs and orgs
            if (case2):
                orgdiff=maxorgs-len(orgs)
                for j in range (maxorgs):
                    if (j > orgdiff-1):
                        formattedMartrix[j+1].extend(" ")
                        formattedMartrix[j+1].extend(" ")
                    else:
                        rank=[str(ranks[j])]
                        org=[str(orgs[j])]
                        formattedMartrix[j+1].extend((org))
                        formattedMartrix[j+1].extend((rank))


            if(not case1 and not case2):
                for j in range (maxorgs):
                    formattedMartrix[j+1].extend(" ")
                    formattedMartrix[j+1].extend(" ")
            iter=iter+1

        ranks=0
        orgs=0

        #%%
        clear()
        print(tabulate(formattedMartrix))


            
# %%