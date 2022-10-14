import time
import os
import psutil
 
 
#def elapsed_since(start):
#    return time.strftime("%H:%M:%S", time.gmtime(time.time() - start))

def elapsed_since(start):
    #return time.strftime("%H:%M:%S", time.gmtime(time.time() - start))
    elapsed = time.time() - start
    if elapsed < 1:
        return str(round(elapsed*1000,2)) + " ms"
    if elapsed < 60:
        return str(round(elapsed, 2)) + " s"
    if elapsed < 3600:
        return str(round(elapsed/60, 2)) + " min"
    else:
        return str(round(elapsed / 3600, 2)) + " hrs"

def format_bytes(bytes):
    if abs(bytes) < 1000:
        return str(bytes)+" B"
    elif abs(bytes) < 1e6:
        return str(round(bytes/1e3,2)) + " kB"
    elif abs(bytes) < 1e9:
        return str(round(bytes / 1e6, 2)) + " MB"
    else:
        return str(round(bytes / 1e9, 2)) + " GB"
 
def get_process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss
 
 
def profile(func):
    def wrapper(*args, **kwargs):
        mem_before = get_process_memory()
        start = time.time()
        result = func(*args, **kwargs)
        elapsed_time = elapsed_since(start)
        mem_after = get_process_memory()
        print("{0}: memory before: {1}, after: {2}, consumed: {3}; exec time: {4}".format(
            func.__name__,
            format_bytes(mem_before), format_bytes(mem_after), format_bytes(mem_after - mem_before),
            elapsed_time))
        return result
    return wrapper
