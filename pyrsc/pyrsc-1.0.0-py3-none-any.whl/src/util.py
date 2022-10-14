import psutil
import time

class CpuWatch:
    def __init__(self, max_perc:float=100, n_cores:int=0, sleep_interval:float=1.0, max_attempts:int=0):
        self.max_perc = max_perc
        self.n_cores = n_cores
        self.sleep_interval = sleep_interval
        self.max_attempts = max_attempts
        
    def __trigger(self):
        cpu_percs = psutil.cpu_percent(percpu=True)
        if sum([perc < self.max_perc for perc in cpu_percs]) >= self.n_cores:
            return True
        return False
    
    def __enter__(self):
        attempts = 0
        while (attempts <= self.max_attempts) or (self.max_attempts == 0):
            if self.__trigger():
                return self
            else:
                print(f'not enough resource is available to submit the job. Waiting for {self.sleep_interval} seconds')
                attempts += 1
                time.sleep(self.sleep_interval)
        raise Exception("attempts exceeds max_attempts")

    def __exit__(self, exc_type, exc_value, exc_tb):
        pass
    
def cpuwatch(max_perc:float, n_cores:int, sleep_interval:float, max_attempts:int):
    def inner(func):
        def wrapper(*args, **kwargs):
            with CpuWatch(max_perc=max_perc, n_cores=n_cores, sleep_interval=sleep_interval, max_attempts=max_attempts) as watcher:
                return func(*args, **kwargs)
        return wrapper
    return inner