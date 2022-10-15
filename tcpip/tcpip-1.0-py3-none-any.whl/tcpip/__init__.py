
dict_hn = {'Arad': 336, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242, 'Eforie': 161,
             'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244,
             'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100, 'Rimnicu': 193,
             'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374}

dict_gn = dict(
    Arad=dict(Zerind=75, Timisoara=118, Sibiu=140),
    Bucharest=dict(Urziceni=85, Giurgiu=90, Pitesti=101, Fagaras=211),
    Craiova=dict(Drobeta=120, Pitesti=138, Rimnicu=146),
    Drobeta=dict(Mehadia=75, Craiova=120),
    Eforie=dict(Hirsova=86),
    Fagaras=dict(Sibiu=99, Bucharest=211),
    Giurgiu=dict(Bucharest=90),
    Hirsova=dict(Eforie=86, Urziceni=98),
    Iasi=dict(Neamt=87, Vaslui=92),
    Lugoj=dict(Mehadia=70, Timisoara=111),
    Mehadia=dict(Lugoj=70, Drobeta=75),
    Neamt=dict(Iasi=87),
    Oradea=dict(Zerind=71, Sibiu=151),
    Pitesti=dict(Rimnicu=97, Bucharest=101, Craiova=138),
    Rimnicu=dict(Sibiu=80, Pitesti=97, Craiova=146),
    Sibiu=dict(Rimnicu=80, Fagaras=99, Arad=140, Oradea=151),
    Timisoara=dict(Lugoj=111, Arad=118),
    Urziceni=dict(Bucharest=85, Hirsova=98, Vaslui=142),
    Vaslui=dict(Iasi=92, Urziceni=142),
    Zerind=dict(Oradea=71, Arad=75)
)

#practical 1 start 
#practical 1 bfs 
def getp1():
   print("""
   bfs
   copy form below
dict_hn={'Arad':336,'Bucharest':0,'Craiova':160,'Drobeta':242,'Eforie':161,
         'Fagaras':176,'Giurgiu':77,'Hirsova':151,'Iasi':226,'Lugoj':244,
         'Mehadia':241,'Neamt':234,'Oradea':380,'Pitesti':100,'Rimnicu':193,
         'Sibiu':253,'Timisoara':329,'Urziceni':80,'Vaslui':199,'Zerind':374}

dict_gn=dict(
Arad=dict(Zerind=75,Timisoara=118,Sibiu=140),
Bucharest=dict(Urziceni=85,Giurgiu=90,Pitesti=101,Fagaras=211),
Craiova=dict(Drobeta=120,Pitesti=138,Rimnicu=146),
Drobeta=dict(Mehadia=75,Craiova=120),
Eforie=dict(Hirsova=86),
Fagaras=dict(Sibiu=99,Bucharest=211),
Giurgiu=dict(Bucharest=90),
Hirsova=dict(Eforie=86,Urziceni=98),
Iasi=dict(Neamt=87,Vaslui=92),
Lugoj=dict(Mehadia=70,Timisoara=111),
Mehadia=dict(Lugoj=70,Drobeta=75),
Neamt=dict(Iasi=87),
Oradea=dict(Zerind=71,Sibiu=151),
Pitesti=dict(Rimnicu=97,Bucharest=101,Craiova=138),
Rimnicu=dict(Sibiu=80,Pitesti=97,Craiova=146),
Sibiu=dict(Rimnicu=80,Fagaras=99,Arad=140,Oradea=151),
Timisoara=dict(Lugoj=111,Arad=118),
Urziceni=dict(Bucharest=85,Hirsova=98,Vaslui=142),
Vaslui=dict(Iasi=92,Urziceni=142),
Zerind=dict(Oradea=71,Arad=75)
)
import queue as Q
#from RMP import dict_hn

start='Arad'
goal='Bucharest'
result=''

def BFS(city, cityq, visitedq):
    global result
    if city==start:
        result=result+' '+city
    for eachcity in dict_gn[city].keys():
        if eachcity==goal:
            result=result+' '+eachcity
            return
        if eachcity not in cityq.queue and eachcity not in visitedq.queue:
            cityq.put(eachcity)
            result=result+' '+eachcity
    visitedq.put(city)
    BFS(cityq.get(),cityq,visitedq)

def main():
    cityq=Q.Queue()
    visitedq=Q.Queue()
    BFS(start, cityq, visitedq)
    print("BFS Traversal from ",start," to ",goal," is: ")
    print(result)
    
main()
""")
#practical 2 idfs (iterative dfs)

def getp2():
    print("""
    idfs
    copy from below
dict_hn={'Arad':336,'Bucharest':0,'Craiova':160,'Drobeta':242,'Eforie':161,
         'Fagaras':176,'Giurgiu':77,'Hirsova':151,'Iasi':226,'Lugoj':244,
         'Mehadia':241,'Neamt':234,'Oradea':380,'Pitesti':100,'Rimnicu':193,
         'Sibiu':253,'Timisoara':329,'Urziceni':80,'Vaslui':199,'Zerind':374}

dict_gn=dict(
Arad=dict(Zerind=75,Timisoara=118,Sibiu=140),
Bucharest=dict(Urziceni=85,Giurgiu=90,Pitesti=101,Fagaras=211),
Craiova=dict(Drobeta=120,Pitesti=138,Rimnicu=146),
Drobeta=dict(Mehadia=75,Craiova=120),
Eforie=dict(Hirsova=86),
Fagaras=dict(Sibiu=99,Bucharest=211),
Giurgiu=dict(Bucharest=90),
Hirsova=dict(Eforie=86,Urziceni=98),
Iasi=dict(Neamt=87,Vaslui=92),
Lugoj=dict(Mehadia=70,Timisoara=111),
Mehadia=dict(Lugoj=70,Drobeta=75),
Neamt=dict(Iasi=87),
Oradea=dict(Zerind=71,Sibiu=151),
Pitesti=dict(Rimnicu=97,Bucharest=101,Craiova=138),
Rimnicu=dict(Sibiu=80,Pitesti=97,Craiova=146),
Sibiu=dict(Rimnicu=80,Fagaras=99,Arad=140,Oradea=151),
Timisoara=dict(Lugoj=111,Arad=118),
Urziceni=dict(Bucharest=85,Hirsova=98,Vaslui=142),
Vaslui=dict(Iasi=92,Urziceni=142),
Zerind=dict(Oradea=71,Arad=75)
)
import queue as Q
#from RMP import dict_hn

start='Arad'
goal='Bucharest'
result=''

def DLS(city, visitedstack, startlimit, endlimit):
    global result
    found=0
    result=result+city+' '
    visitedstack.append(city)
    if city==goal:
        return 1
    if startlimit==endlimit:
        return 0
    for eachcity in dict_gn[city].keys():
        if eachcity not in visitedstack:
            found=DLS(eachcity, visitedstack, startlimit+1, endlimit)
            if found:
                return found

def IDDFS(city, visitedstack, endlimit):
    global result
    for i in range(0, endlimit):
        print("Searching at Limit: ",i)
        found=DLS(city, visitedstack, 0, i)
        if found:
            print("Found")
            break
        else:
            print("Not Found! ")
            print(result)
            print("-----")
            result=' '
            visitedstack=[]

def main():
    visitedstack=[]
    IDDFS(start, visitedstack, 9)
    print("IDDFS Traversal from ",start," to ", goal," is: ")
    print(result)


main()      

    """)

#practical 3 A* search algorithm
def getp3():
    print("""
    A*
    copy form below
dict_hn={'Arad':336,'Bucharest':0,'Craiova':160,'Drobeta':242,'Eforie':161,
         'Fagaras':176,'Giurgiu':77,'Hirsova':151,'Iasi':226,'Lugoj':244,
         'Mehadia':241,'Neamt':234,'Oradea':380,'Pitesti':100,'Rimnicu':193,
         'Sibiu':253,'Timisoara':329,'Urziceni':80,'Vaslui':199,'Zerind':374}

dict_gn=dict(
Arad=dict(Zerind=75,Timisoara=118,Sibiu=140),
Bucharest=dict(Urziceni=85,Giurgiu=90,Pitesti=101,Fagaras=211),
Craiova=dict(Drobeta=120,Pitesti=138,Rimnicu=146),
Drobeta=dict(Mehadia=75,Craiova=120),
Eforie=dict(Hirsova=86),
Fagaras=dict(Sibiu=99,Bucharest=211),
Giurgiu=dict(Bucharest=90),
Hirsova=dict(Eforie=86,Urziceni=98),
Iasi=dict(Neamt=87,Vaslui=92),
Lugoj=dict(Mehadia=70,Timisoara=111),
Mehadia=dict(Lugoj=70,Drobeta=75),
Neamt=dict(Iasi=87),
Oradea=dict(Zerind=71,Sibiu=151),
Pitesti=dict(Rimnicu=97,Bucharest=101,Craiova=138),
Rimnicu=dict(Sibiu=80,Pitesti=97,Craiova=146),
Sibiu=dict(Rimnicu=80,Fagaras=99,Arad=140,Oradea=151),
Timisoara=dict(Lugoj=111,Arad=118),
Urziceni=dict(Bucharest=85,Hirsova=98,Vaslui=142),
Vaslui=dict(Iasi=92,Urziceni=142),
Zerind=dict(Oradea=71,Arad=75)
)
import queue as Q
#from RMP import dict_gn
#from RMP import dict_hn

start='Arad'
goal='Bucharest'
result=''

def get_fn(citystr):
    cities=citystr.split(" , ")
    hn=gn=0
    for ctr in range(0, len(cities)-1):
        gn=gn+dict_gn[cities[ctr]][cities[ctr+1]]
    hn=dict_hn[cities[len(cities)-1]]
    return(hn+gn)

def expand(cityq):
    global result
    tot, citystr, thiscity=cityq.get()
    if thiscity==goal:
        result=citystr+" : : "+str(tot)
        return
    for cty in dict_gn[thiscity]:
        cityq.put((get_fn(citystr+" , "+cty), citystr+" , "+cty, cty))
    expand(cityq)

def main():
    cityq=Q.PriorityQueue()
    thiscity=start
    cityq.put((get_fn(start),start,thiscity))
    expand(cityq)
    print("The A* path with the total is: ")
    print(result)

main()

    """)

#practical 4 Rbfs (Recursive Breadth First search)
def getp4():
    print("""
    rBfs
    copy from below
dict_hn={'Arad':336,'Bucharest':0,'Craiova':160,'Drobeta':242,'Eforie':161,
         'Fagaras':176,'Giurgiu':77,'Hirsova':151,'Iasi':226,'Lugoj':244,
         'Mehadia':241,'Neamt':234,'Oradea':380,'Pitesti':100,'Rimnicu':193,
         'Sibiu':253,'Timisoara':329,'Urziceni':80,'Vaslui':199,'Zerind':374}

dict_gn=dict(
Arad=dict(Zerind=75,Timisoara=118,Sibiu=140),
Bucharest=dict(Urziceni=85,Giurgiu=90,Pitesti=101,Fagaras=211),
Craiova=dict(Drobeta=120,Pitesti=138,Rimnicu=146),
Drobeta=dict(Mehadia=75,Craiova=120),
Eforie=dict(Hirsova=86),
Fagaras=dict(Sibiu=99,Bucharest=211),
Giurgiu=dict(Bucharest=90),
Hirsova=dict(Eforie=86,Urziceni=98),
Iasi=dict(Neamt=87,Vaslui=92),
Lugoj=dict(Mehadia=70,Timisoara=111),
Mehadia=dict(Lugoj=70,Drobeta=75),
Neamt=dict(Iasi=87),
Oradea=dict(Zerind=71,Sibiu=151),
Pitesti=dict(Rimnicu=97,Bucharest=101,Craiova=138),
Rimnicu=dict(Sibiu=80,Pitesti=97,Craiova=146),
Sibiu=dict(Rimnicu=80,Fagaras=99,Arad=140,Oradea=151),
Timisoara=dict(Lugoj=111,Arad=118),
Urziceni=dict(Bucharest=85,Hirsova=98,Vaslui=142),
Vaslui=dict(Iasi=92,Urziceni=142),
Zerind=dict(Oradea=71,Arad=75)
)
import queue as Q


start='Arad'
goal='Bucharest'
result=''

def get_fn(citystr):
    cities=citystr.split(',')
    hn=gn=0
    for ctr in range(0,len(cities)-1):
        gn=gn+dict_gn[cities[ctr]][cities[ctr+1]]
    hn=dict_hn[cities[len(cities)-1]]
    return(hn+gn)

def printout(cityq):
    for i in range(0,cityq.qsize()):
        print(cityq.queue[i])

def expand(cityq):
    global result
    tot,citystr,thiscity=cityq.get()
    nexttot=999
    if not cityq.empty():
        nexttot,nextcitystr,nextthiscity=cityq.queue[0]
    if thiscity==goal and tot<nexttot:
        result=citystr+'::'+str(tot)
        return
    print("Expanded city------------------------------",thiscity)
    print("Second best f(n)------------------------------",nexttot)
    tempq=Q.PriorityQueue()
    for cty in dict_gn[thiscity]:
            tempq.put((get_fn(citystr+','+cty),citystr+','+cty,cty))
    for ctr in range(1,3):
        ctrtot,ctrcitystr,ctrthiscity=tempq.get()
        if ctrtot<nexttot:
            cityq.put((ctrtot,ctrcitystr,ctrthiscity))
        else:
            cityq.put((ctrtot,citystr,thiscity))
            break
    printout(cityq)
    expand(cityq)
def main():
    cityq=Q.PriorityQueue()
    thiscity=start
    cityq.put((999,"NA","NA"))
    cityq.put((get_fn(start),start,thiscity))
    expand(cityq)
    print(result)
main()

    """)


def getp5():
    print(""" 
    #Decision-Tree learning algorithm.
#copy from below

import numpy as np
import pandas as pd
import sklearn as sk
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

#func importing dataset
def importdata():
      balance_data=pd.read_csv("balance-scale.data")

      #print the dataset shape
      print("Dataset Length : ",len(balance_data))
      
      #printing the dataset observations
      print("Dataset : ",balance_data.head())
      return balance_data

#func to split the dataset
def splitdataset(balance_data):
      #seperating the target variable
      X=balance_data.values[:,1:5]
      Y=balance_data.values[:,0]

      #splitting the dataset into train and test
      X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.3,random_state=100)
      return X,Y,X_train,X_test,y_train,y_test

#function to perform training with entropy
def train_using_entropy(X_train,X_test,y_train,y_test):
      #decision tree with entropy
      clf_entropy=DecisionTreeClassifier(criterion="entropy",random_state=100,max_depth=3,min_samples_leaf=5)

      #performing training
      clf_entropy.fit(X_train,y_train)
      return clf_entropy

def prediction(X_test,clf_object):
      y_pred=clf_object.predict(X_test)
      print("Predicted Values : ")
      print(y_pred)
      return y_pred

def cal_accuracy(y_test,y_pred):
      print("Accuracy : ",accuracy_score(y_test,y_pred)*100)

def main():
      data=importdata()
      X,Y,X_train,X_test,y_train,y_test=splitdataset(data)
      
      clf_entropy=train_using_entropy(X_train,X_test,y_train,y_test)

      print("Results using entropy : ")
      y_pred_entropy=prediction(X_test,clf_entropy)
      cal_accuracy(y_test,y_pred_entropy)

main()
    
    """)

def getp6():
    print("""
#Naive-Bayes learning algo for RWP(Restaurant Waiting Problem).
#copy from below

rwp_examples = dict(
    x1=dict(Alt='Y', Bar='N', Fri='N',Hun='Y',Pat='S',Price='$$$',Rain='N',Res='Y',Type='F',Est='0-10',ans='Y'),
    x2=dict(Alt='Y', Bar='N', Fri='N',Hun='Y',Pat='F',Price='$',Rain='N',Res='N',Type='T',Est='30-60',ans='N'),
    x3=dict(Alt='N', Bar='Y', Fri='N',Hun='N',Pat='S',Price='$',Rain='N',Res='N',Type='B',Est='0-10',ans='Y'),
    x4=dict(Alt='Y', Bar='N', Fri='Y',Hun='Y',Pat='F',Price='$',Rain='Y',Res='N',Type='T',Est='10-30',ans='Y'),
    x5=dict(Alt='Y', Bar='N', Fri='Y',Hun='N',Pat='F',Price='$$$',Rain='N',Res='Y',Type='F',Est='>60',ans='N'),
    x6=dict(Alt='N', Bar='Y', Fri='N',Hun='Y',Pat='S',Price='$$',Rain='Y',Res='Y',Type='I',Est='0-10',ans='Y'),
    x7=dict(Alt='N', Bar='Y', Fri='N',Hun='N',Pat='N',Price='$',Rain='Y',Res='N',Type='B',Est='0-10',ans='N'),
    x8=dict(Alt='N', Bar='N', Fri='N',Hun='Y',Pat='S',Price='$$',Rain='Y',Res='Y',Type='T',Est='0-10',ans='Y'),
    x9=dict(Alt='N', Bar='Y', Fri='Y',Hun='N',Pat='F',Price='$',Rain='Y',Res='N',Type='B',Est='>60',ans='N'),
    x10=dict(Alt='Y', Bar='Y', Fri='Y',Hun='Y',Pat='F',Price='$$$',Rain='N',Res='Y',Type='I',Est='10-30',ans='N'),
    x11=dict(Alt='N', Bar='N', Fri='N',Hun='N',Pat='N',Price='$',Rain='N',Res='N',Type='T',Est='0-10',ans='N'),
    x12=dict(Alt='Y', Bar='Y', Fri='Y',Hun='Y',Pat='F',Price='$',Rain='N',Res='N',Type='B',Est='0-10',ans='Y')
    )

#from RWP import rwp_examples
total_exp = 12
def tot(attribute, value):
    count = 0
    for key, val in rwp_examples.items():
        for key1, val1 in val.items():
            if key1 == attribute:
                if val1 == value:
                    count += 1
    return count
def getProbab(attribute, attribval, value):
    count = 0
    for key, val in rwp_examples.items():
        val1 = rwp_examples[key][attribute]
        val2 = rwp_examples[key]['ans']
        if val1 == attribval and val2 == value:
            count += 1
    probab = count / tot('ans', value)
    return probab
def main():
    PAltYes = tot('Alt', 'Y') / total_exp
    PAltNo = tot('Alt', 'N') / total_exp    
    PBarYes = tot('Bar', 'Y') / total_exp
    PBarNo = tot('Bar', 'N') / total_exp    
    PFriYes = tot('Fri', 'Y') / total_exp
    PFriNo = tot('Fri', 'N') / total_exp    
    PHunYes = tot('Hun', 'Y') / total_exp
    PHunNo = tot('Hun', 'N') / total_exp    
    PPatSome = tot('Pat', 'S') / total_exp
    PPatFull = tot('Pat', 'F') / total_exp
    PPatNone = tot('Pat', 'N') / total_exp
    PPriceCheap = tot('Price', '$') / total_exp
    PPriceAvg = tot('Price', '$$') / total_exp
    PPriceExp = tot('Price', '$$$') / total_exp    
    PRainYes = tot('Rain', 'Y') / total_exp
    PRainNo = tot('Rain', 'N') / total_exp    
    PResYes = tot('Res', 'Y') / total_exp
    PResNo = tot('Res', 'N') / total_exp    
    PTypeFrench = tot('Type', 'F') / total_exp
    PTypeItalian = tot('Type', 'I') / total_exp
    PTypeBurger = tot('Type', 'B') / total_exp
    PTypeThai = tot('Type', 'T') / total_exp    
    PEstFew = tot('Est', '0-10') / total_exp
    PEstMore = tot('Est', '10-30') / total_exp
    PEstStillMore = tot('Est', '30-60') / total_exp
    PEstTooMuch = tot('Est', '>60') / total_exp
    PAnsYes = tot('ans', 'Y') / total_exp
    PAnsNo = tot('ans', 'N') / total_exp    
    print('Probability for will wait if there is an Alternate Restaurant Nearby: ')
    print('Yes: Will Wait ', (getProbab('Alt', 'Y', 'Y') * PAnsYes/PAltYes) * 100, '%')
    print('No: Will Wait ', (getProbab('Alt', 'Y', 'N') * PAnsNo/PAltYes ) * 100, '%')
    print('Probability for will wait if there No is an Alternate Restaurant Nearby: ')
    print('Yes: Will Wait ', (getProbab('Alt', 'N', 'Y') * PAnsYes/PAltNo) * 100, '%')
    print('No: Will Wait ', (getProbab('Alt', 'N', 'N') * PAnsNo/PAltNo) * 100, '%')
    print('Probability for will wait if Estimated Wait time is 0-10 minutes: ')
    print('Yes: Will Wait ', (getProbab('Est', '0-10', 'Y') * PAnsYes/PEstFew) * 100, '%')
    print('No: Will Wait ', (getProbab('Est', '0-10', 'N') * PAnsNo/PEstFew) * 100, '%')
    print('Probability for will wait if Estimated Wait time is 10-30 minutes ')
    print('Yes: Will Wait ', (getProbab('Est', '10-30', 'Y') * PAnsYes/PEstMore) * 100, '%')
    print('No: Will Wait ', (getProbab('Est', '10-30', 'N') * PAnsNo/PEstMore) * 100, '%')
    print("Probability for Will Wait if the Estimated Wait Time is 30-60 mins: ")
    print("Yes: Will Wait: ",(getProbab('Est','30-60','Y')*PAnsYes/PEstStillMore)*100,"%")
    print("No: Will Wait: ",(getProbab('Est','30-60','N')*PAnsNo/PEstStillMore)*100,"%")
    print("Probability for Will Wait if the Estimated Wait Time is >60 mins: ")
    print("Yes: Will Wait: ",(getProbab('Est','>60','Y')*PAnsYes/PEstTooMuch)*100,"%")
    print("No: Will Wait: ",(getProbab('Est','>60','N')*PAnsNo/PEstTooMuch)*100,"%")
    print('Probability for will wait if there are Some Patrons ')
    print('Yes: Will Wait ', (getProbab('Pat', 'S', 'Y') * PAnsYes/PPatSome) * 100, '%')
    print('No: Will Wait ', (getProbab('Pat', 'S', 'N') * PAnsNo/PPatSome) * 100, '%')
    print("Probability for Will Wait if there are None Patrons: ")
    print("Yes: Will Wait: ",(getProbab('Pat','N','Y')*PAnsYes/PPatNone)*100,"%")
    print("No: Will Wait: ",(getProbab('Pat','N','N')*PAnsNo/PPatNone)*100,"%")
    print("Probability for Will Wait if there are Full Patrons: ")
    print("Yes: Will Wait: ",(getProbab('Pat','F','Y')*PAnsYes/PPatFull)*100,"%")
    print("No: Will Wait: ",(getProbab('Pat','F','N')*PAnsNo/PPatFull)*100,"%")
    print('Probability for will wait if the place is Thai ')
    print('Yes: Will Wait ', (getProbab('Type', 'T', 'Y') * PAnsYes/PTypeThai) * 100, '%')
    print('No: Will Wait ', (getProbab('Type', 'T', 'N') * PAnsNo/PTypeThai) * 100, '%')    
main()   
    
    """)

def getp7():
    print("""
#Implement feed forward back propagation neural network learning algorithm.
#copy form below
import numpy as np

class NeuralNetwork():
    def __init__(self):
        #seeding for random number generation
        np.random.seed()

        #converting weights to a 3 by 1 matrix
        self.synaptic_weights=2*np.random.random((3,1))-1

    #x is output variable
    def sigmoid(self, x):
        #applying the sigmoid function
        return 1/(1+np.exp(-x))

    def sigmoid_derivative(self,x):
        #computing derivative to the sigmoid function
        return x*(1-x)

    def train(self,training_inputs,training_outputs,training_iterations):

        #training the model to make accurate predictions while adjusting
        for iteration in range(training_iterations):
            #siphon the training data via the neuron
            output=self.think(training_inputs)

            error=training_outputs-output

            #performing weight adjustments
            adjustments=np.dot(training_inputs.T,error*self.sigmoid_derivative(output))

            self.synaptic_weights+=adjustments

    def think(self,inputs):
        #passing the inputs via the neuron to get output
        #converting values to floats

        inputs=inputs.astype(float)
        output=self.sigmoid(np.dot(inputs,self.synaptic_weights))

        return output

if __name__=="__main__":

    #initializing the neuron class
    neural_network=NeuralNetwork()

    print("Beginning randomly generated weights: ")
    print(neural_network.synaptic_weights)

    #training data consisting of 4 examples--3 inputs & 1 output
    training_inputs=np.array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])
    training_outputs=np.array([[0,1,1,0]]).T

    #training taking place
    neural_network.train(training_inputs,training_outputs,15000)

    print("Ending weights after training: ")
    print(neural_network.synaptic_weights)

    user_input_one=str(input("User Input One: "))
    user_input_two=str(input("User Input Two: "))
    user_input_three=str(input("User Input Three: "))

    print("Considering new situation: ",user_input_one,user_input_two,user_input_three)
    print("New output data: ")
    print(neural_network.think(np.array([user_input_one,user_input_two,user_input_three])))

    """)

#practical 8
def getp8():
    print("""

#Implement AdaBoost(Adaptive Boosting) learning algorithm.
#copy from below

import pandas
from sklearn import model_selection
from sklearn.ensemble import AdaBoostClassifier
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pandas.read_csv(url, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
seed = 7
num_trees = 30
#kfold makes trees with split number.
#kfold = model_selection.KFold(n_splits=10, random_state=seed)
#n_estimators : This is the number of trees you want to build before predictions.
#Higher number of trees give you better voting optionsand perfomance performance 
model = AdaBoostClassifier(n_estimators=num_trees, random_state=seed)
#cross_val_score method is used to calculate the accuracy of model sliced into x, y
#cross validator cv  is optional cv=kfold
results = model_selection.cross_val_score(model, X, Y)
print(results.mean())

    """)



def linux_nfs():
    print("""
make tow directories- mkdir /home/tycs /home/exam
                    - chmod 777 /home/tycs
                    - chmod 777 /home/exam
                    - vi /etc/exports
                    - rpmquery -qa | grep nfs
                    - chkconfig --level 5 nfs on
                    - chkconfig --list | grep nfs
                    - service nfs restart
                    - service network restart
                    - showmount -e
                    - mount -t nfs _your_Ip:/home/tycs /home/exam
                    - touch a1 a2 a3 /home/tycs
                    - cd /home/exam
                    ls 
                    cd /home/tycs

    finish
    """)

def linux_samba():
    print("""
- vi /etc/samba/smb.conf
make mygroup to WORKGROUP
[myshare]
    comment — Mary's and Fred's stuff
    path = /home/abcd
    valid users = rinshu pinsu
    public = yes
    writable = yes
    printable = no
    create mask = 0765
- service smb restart
useradd rinshu
smbpasswd -a rinshu
- mkdir /home/welcome
- chmod 777 /home/welcome

getsebool -a | grep samba
setsebool ........=1

ifconfig

enter ip addsess to run in windows

cd /home

cd rinshu 
ls
    
    """)


def linux_partition():
    print(""" 
- fdisk -l
- fdisk /dev/sdb
- fdisk /dev/sdb

- fdisk -l
- mkfs.ext3 /dev/sdb2
- mkfs.ext3 /dev/sdb2
- mkfs.ext3 /dev/sdb5

mount -t /dev/sdb5 /home/welcome
mount /dev/sdb5 /home/welcom
cd /home/welcom
    """)

def linux_apache():
    print("""
- rpmquery -qa | grep httpd
- cd /var/www/html/
- vim index.html           write content in it

- vim /etc/httpd/conf/httpd.conf

<VirtuatHost
ServerAdmin abc@abc.com
DocumentRoot /var/www/html/
ServerName prajyot
togs/dummy-host . example . com-error_tog
ErrorLog
togs/dummy-host.example.com-access_tog common
CustomLog
</VirtualHost>

- service httpd restart     2 times

- vim /etc/hosts
copy ip from this and paste in browser
- service httpd restart
    """)

def linux_vsftpd():
    print("""
- cd /var/ftp/pub/
- cat > abc.txt
skd skdf kasjhdj asdj 

- vim /etc/vsftpd/vsftpd.conf
- service vsftpd restart 2 times

-ftp:// your ip address     -> in browser



for extra 
vsftd program
1)ifconfig
2)service network restart
3)ifconfig
4)system-config-network
5)service network restart
6)ping 192.168.2.202
7)cd /var/ftp/pub/
8)cat > tjas.txt
Hello world
9)touch a1 a2 a3
10)ifconfig
11)vim /etc/vsftpd/vsftpd.conf
12)service vsftpd restart
13)ping 192.168.2.202
14)in Linux browser ftp://192.168.2.202
We will get created file
    """)



def ins_cescif():
    print("""
import java.util.Scanner;

public class your_file_name {

public static void main(String[] args) {
// TODO code application logic here
String message, encryptedmessage="";
int key;
char ch;
Scanner sc=new Scanner(System.in);
System.out.println("Enter a message: ");
message=sc.nextLine();

System.out.println("Enter Key: ");
key=sc.nextInt();
for(int i=0;i<message.length();i++)
{
ch=message.charAt(i);

if(ch>='a' && ch<='z')
{
ch=(char)(ch+key);
if(ch>'z') {ch=(char)(ch-'z'+'a'-1);}
encryptedmessage+=ch;

}

else if(ch>='A' && ch<='Z')
{
ch=(char)(ch+key);
if(ch>'Z') {ch=(char)(ch-'Z'+'A'-1);}
encryptedmessage+=ch;
}

else {encryptedmessage+=ch;}
}

System.out.println("Encrypted Message: "+encryptedmessage);
}
}
    """)

def ins_mono():
    print("""
import java.util.Scanner;
public class Your_file_name {
	public static String check(String n,char a[],char b[]){
		String temp = "";
			for(int i = 0;i < n.length();i++){
				for(int  j = 0;j < 26;j++){
					if(n.charAt(i) == a[j])
						temp += b[j];
					}
			}		
		return temp;
	}
	public static void main(String[] args) {
		char a[] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
		char b[] = {'z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'};
		Scanner s = new Scanner(System.in);
		String n = s.next();
		String temp = check(n,a,b);
		System.out.println("Encode : " + temp);	
		System.out.println("Decode  : "  +check(temp,b,a));
	}
}
    """)



def ins_vernam():
    print("""

import java.util.Scanner;
public class Your_file_name {
    static void check(String n,String otp){
        int temp[] = new int[n.length()];
        int temp1[] = new int[n.length()];
        for(int i = 0;i < n.length();i++){
            temp[i] = (n.charAt(i) - 97) + (otp.charAt(i) - 97);
            if(temp[i] > 25)
                temp[i] = temp[i] - 25;
        }
        Display(temp,"Encryption");
        for(int i = 0;i < temp1.length;i++){
            temp1[i] = temp[i] - (otp.charAt(i) - 97);
            if(temp1[i] < 0)
                temp1[i] += 25;
        }
        Display(temp1,"Decryption");
    }
    static void Display(int temp[],String f){
        System.out.println(f);
        for(int i = 0;i < temp.length;i++){
            char gg = (char)(temp[i] + 97);
            System.out.print(gg + " ");
        }
        System.out.println();
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String n = sc.next();
        String otp = sc.next();
        check(n,otp);
    }
}

    """)

def ins_col():
    print("""
public class Your_file_name {
public static void main(String[] args) {
String text;
int key1;
int key[]=new int[4];
Scanner sc=new Scanner(System.in);
System.out.println("Enter a message : ");
text=sc.nextLine();
char a[][]=new char[50][4];
int l = text.length();
int row;
if(l%4==0) {row=l/4;}
else {row=(l/4)+1;}
int k=0;
System.out.println("\nMatrix: ");
for (int i =0;i<row;i++)
{
for(int j=0;j<4;j++)
{
a[i][j]=text.charAt(k);
k++;
System.out.print(a[i][j]+" ");
if(l==k) {break;}
}
System.out.println(" \n");
}
String s="";
System.out.println("Enter a key: ");
for (int i=0;i<4;i++)
{
key[i]=sc.nextInt();
}
for (int i=0;i<4;i++)
{

key1=key[i];
for(int j=0;j<row;j++)
{
String c=a[j][key1]+" ";
if(c!="\0") {s=s+c;}
}
}
System.out.println("Cipher text: " +s);
}
}
      
    """)

def ins_colVish():
    print("""
import java.util.Scanner;
import java.lang.Math;
class hello2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = 0;
        String encrypt= "";
        //Taking input from user
        System.out.println("Enter value : ");
        String num = sc.next();
        System.out.println("Enter order from 1 to 5 : ");
        String order = sc.next();

        //Calculating number of row required
        int c = 0;
        if((num.length() % 5) == 0)
            c = num.length() / 5;
        else
            c = Math.round(num.length()/5)+1;


        //Taking 2D array
        char a[][] = new char[c][5];

        //Putting all num data into 2D array
        for(int i = 0;i < c;i++){
            for(int j = 0;j < 5;j++){
                if(x == num.length())
                    break;
                a[i][j] = num.charAt(x);
                x++;
            }
        }

//        //Print 2D array : a
//        for(int i = 1;i <= 5;i++){
//            System.out.print(i + " ");
//        }
//        System.out.println();
//        for(int i = 0;i < c;i++){
//            for(int j = 0;j < 5;j++){
//                System.out.print(a[i][j]+" ");
//            }
//            System.out.println();
//        }

        //Encryption Process
        for(int k = 0;k < 5;k++){
            for(int i = 0;i < c;i++){
                for(int j = 0;j < 5;j++){
                    int xm = Integer.parseInt(String.valueOf(order.charAt(k)));
                    if(xm == (j+1)){
                        encrypt += a[i][j];
                        break;
                    }
                }
            }
        }

        //Displaying Encrypted Message
        System.out.println("Encrypted : " +encrypt);
        System.out.println();

//#######Decryption Phase########

        System.out.println("Decryption Phase ");
        //Taking 2D array
        char b[][] = new char[c][5];

        //Decryption Process
        x = 0;
        for(int k = 0;k < 5;k++){
            for(int i = 0;i < c;i++){
                for(int j = 0;j < 5;j++){
                    int xm = Integer.parseInt(String.valueOf(order.charAt(k)));
                    if(xm == (j+1)){
                        b[i][j] = encrypt.charAt(x);
                        x++;
                        break;
                    }
                }
            }
        }

        //Print 2D array : b
        for(int i = 1;i <= 5;i++){
            System.out.print(i + " ");
        }
        System.out.println();
        for(int i = 0;i < c;i++){
            for(int j = 0;j < 5;j++){
                System.out.print(b[i][j]+" ");
            }
            System.out.println();
        }

        //Putting all data of array b into decrypt variable
        String decrypt = "";
        for(int i = 0;i < c;i++){
            for(int j = 0;j < 5;j++){
                decrypt += b[i][j];
            }
        }

        //Displaying Decrypted Message
        System.out.println("Decrypted : "+decrypt);
    }
}
    """)

def ins_railfence():
    print("""
import java.util.*;
   public class railfence
       { 
            public static void main(String[] args)
            {   
                  Scanner scan=new Scanner(System.in);
                  System.out.println("Enter the string for Encryption:"); 
                  String message = new String();
                  message =scan.next();
                  String c1="";
                  String cipherText="";
                  for(int i=0;i<message.length();i+=2)
                  {
                   c1+=message.charAt(i);          
                   }
                   for(int j=1;j<message.length();j+=2)
                   {         
                    c1+=message.charAt(j);
                    }
                    cipherText=c1;
                    System.out.println("The Cipher Text is:" +cipherText);
                    int len=cipherText.length();
                    if (len%2!=0)
                    {         
                      cipherText+=" ";
                       len=len+1;
                     }
                      int x;
                      x= (len/2);

                      String s1="";
                      String s2="";
                      s1=cipherText.substring(0,x);
                      s2=cipherText.substring(x,len);

                      String pt="";
                      for(int i=0;i<x;i++)
                      {
                        pt+=s1.charAt(i);
                        pt+=s2.charAt(i);
                      }
                       System.out.print("The plain text is:"+pt);
}
}

    """)

def ins_deffi():
    print("""
import java.util.Scanner;
class DiffieH {
	public static void main(String args[]){
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the value of Xa & Xb");
		int Xa=sc.nextInt();
		int Xb=sc.nextInt();
		System.out.println("Enter a Prime no. p");
		int p=sc.nextInt();
		System.out.println("Enter Primitive Root a, such that a<p");
		int a=sc.nextInt();
		int Ya=(int)((Math.pow(a,Xa))%p);
		int Yb=(int)((Math.pow(a,Xb))%p);
		int Ka=(int)((Math.pow(Yb,Xa))%p);
		int Kb=(int)((Math.pow(Ya,Xb))%p);
		if(Ka==Kb){
			System.out.println(Ka);
			System.out.println(Kb);
			System.out.println("Transmission Successful");
		}
		else{
			System.out.println("Transmission Failed");
		}
	}
}

    """)


def ins_shortsha():
    print("""
import java.security.*;
import java.math.BigInteger;
class Main {
	public static void main(String[] args) throws Exception{
		BigInteger bg = new BigInteger(1,MessageDigest.getInstance("SHA1").digest("hello".getBytes()));
		System.out.print(bg.toString(16));
	}
}

    """)

def ins_shortdes():
    print("""
import java.security.*;
import javax.crypto.*;
class Main {
	public static void main(String[] args) throws Exception{
		Cipher encCipher = Cipher.getInstance("DES/ECB/PKCS5Padding");
		Cipher dncCipher = encCipher;
		SecretKey secret = KeyGenerator.getInstance("DES").generateKey();
		encCipher.init(Cipher.ENCRYPT_MODE,secret);
		byte[] en = encCipher.doFinal("HELLO".getBytes());
		System.out.println(en);
		dncCipher.init(Cipher.DECRYPT_MODE,secret);
		System.out.println(new String(dncCipher.doFinal(en)));
	}
}

    """)

def ins_shortcc():
    print("""
import java.util.Scanner;
class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);	
		String n = sc.next();
		String enc = "";
		String dnc = "";
		for(int i = 0;i < n.length();i++){
			enc += (char)(((((int)n.charAt(i)-97)+3)%26)+97);
			dnc += (char)((((((int)enc.charAt(i)-97)-3)+26)%26)+97);
		}
		System.out.println("Encryption " +enc + "\nDecryption "+dnc);
	}	
}

    """)
