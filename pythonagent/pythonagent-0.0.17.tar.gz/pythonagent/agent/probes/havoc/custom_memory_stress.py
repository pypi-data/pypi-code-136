import sys
import time
import psutil

MEGA = 2 ** 20
GIGA = 2 ** 30

def alloc_max_str(totaltobeleaked, memoryLeaksInSec, mbleakspertime, leaksINMB):
    '''
    Function to load memory by assigning string of requested size

    Arguments:
        memory: amount of memory to be utilized in MB
    Returns:
        a : String of size 'memory'
    '''
    i = 1
    a = ''

    li = []
    while True:

        #start_time = time.time()
        end_time = int((time.time()))+int(memoryLeaksInSec)
        try:
            a = ' ' * (int(i * int(((mbleakspertime))*MEGA)))
            li.append(a)
            if((psutil.virtual_memory().used >> 20) >= int(totaltobeleaked)):
                break
            elif sys.getsizeof(a) / MEGA == int(leaksINMB):
                break
            
        except MemoryError:
            break
        time.sleep(end_time-time.time())
        i += 1
    del li 
    return a

def pmem():
    '''
    Function to display memory statistics
    '''
    tot, avail, percent, used, free = psutil.virtual_memory()[0:5]
    tot, avail, used, free = tot / GIGA, avail / GIGA, used / GIGA, free / GIGA
    print("Memory Stats: total = %s GB \navail = %s GB \nused = %s GB \nfree = %s GB \npercent = %s"
          % (tot, avail, used, free, percent))


def memory_stress(totaltobeleaked, memoryLeaksInSec, totalDurationInSec, mbleakspertime, leaksINMB):
    '''
    Function to stress memory and display memory Stats

    Arguments:
        memory: amount of memory to be utilized in MB
        exec_time: time for which the system is supposed to keep the object

    Returns:
        a : String of size 'memory'
    '''
    pmem()
    obj = alloc_max_str(totaltobeleaked, memoryLeaksInSec, mbleakspertime, leaksINMB)
    pmem()
    return obj

def apply_memory_leak(leaksINMB,totalDurationInSec, memoryLeaksInSec):
    totaltobeleaked = int(int(psutil.virtual_memory().used >> 20) + int(leaksINMB))
    mbleakspertime = int(leaksINMB)/(int(totalDurationInSec)/int(memoryLeaksInSec))
    memory_stress(totaltobeleaked, memoryLeaksInSec, totalDurationInSec, mbleakspertime, leaksINMB)

#need to create a check for memory should not be greater than total from psutil.virtual_memory().total

