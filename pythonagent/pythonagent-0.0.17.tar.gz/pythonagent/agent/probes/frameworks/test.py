import json
import os
from datetime import datetime
import platform
import time
import threading 
import traceback
import sys
import multiprocessing
import psutil



#****creating a function for thread dump related variables ********

def dumpstacks():
 
    #vmName=my_system.system

    my_system = platform.uname()
    osName=my_system.system
    osVersion=my_system.version
    arch=my_system.machine
    b =multiprocessing.cpu_count()
    #l=psutil.getloadavg()
    l=os.getloadavg()
    res=sum(list(l))
    u=round(res,2)/3
    #ndbuild = sdk_getNdBuild()
    #ndbuild := C.GoString(C.sdk_getNdBuild())
    k=("Full thread dump Python Agent :- [ Dump Taken at : "+ datetime.now().strftime("%d/%m/%Y %H:%M:%S")+ " , Where BCIAgent build = \" 4.7.0 BUILD 93\" ")

    #k=("Full thread dump BCI Agent :- [ Dump Taken at : "+ datetime.now().strftime("%d/%m/%Y %H:%M:%S")+ " , Where BCIAgent build =\" " + ndbuild + " \""  )
    a=""

    nid="0x0"
    prio="5"
    vendor=""
    version=""   
   
    system_name = os.getenv('HOSTNAME')
 #//****append the thread details into list(code)*****//    
    code=[]
    o=[]
    al=[]
    for thread in threading.enumerate():
        
        """ if thread.daemon == True:
           s= 'wait'
        elif (thread.is_alive() == True ):
           s="Runnable"
        else:
           pass
        #if not thread.isDaemon():
           #s= 'wait'"""
        o.append(thread.name)

        if not thread.isDaemon():
           s= 'wait'
   
        elif thread.is_alive() == True:
           s='runable'
        
        elif thread.daemon == False:
           s='waiting'
        
        elif threading.Lock != null :
            s='locked'
       
        else:
           pass
        
    i=0
    for threadId, stack in sys._current_frames().items():
               
            code.extend(["\n\n'%s'" % o[i] + ' ' + "prio=%s"%prio + ' ' + "tid=%d"% threadId  + ' ' + "nid=%s"%nid + ' ' + "%s"%s+ ' ' + "\n" + "java.lang.Thread.State: %s "% s])
            i=i+1
               
            for filename, lineno, name, line in traceback.extract_stack(stack):
                 code.append('File: "%s", line %d, in %s, at %s' % (filename, lineno, name,datetime.now()))
                 if line:
                      code.append("  %s" % (line.strip()))
    print ("\n".join(code))

#//*****in dictionary thread dump entry page details comming ********//

    thread1_details = {"":k,"vmName":osName,"version":version ,"vendor":vendor , "osName":osName,"osVersion":osVersion,"arch":arch,"noOfProcessors":b,"SysLoadAvg":u,"deadlocked threads ":a }

#//*********all details dump into logs location************//

    def write_json(target_path, target_file, data):
        if not os.path.exists(target_path):
            try:
                os.makedirs(target_path)
            except Exception as e:
                print(e)
                raise
        with open(os.path.join(target_path, target_file), 'w') as f:
            json.dump(data, f)
            f.write("\n".join((code)))


    nd_home = os.environ.get('ND_HOME')
    write_file = nd_home + '/logs/'

    write_json(write_file,
               datetime.now().strftime('thread_dump_%H_%M_%d_%m_%Y.txt'), thread1_details)

#dumpstacks()
