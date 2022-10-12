import threading

class RepeatedTimer(threading.Thread):
    def __init__(self, method, delay):
        super().__init__()
        self.daemon = True
        self._stopper = threading.Event()
        self.delay = delay
        self.method = method

    def run(self):
        while not self._stopper.wait(self.delay):
            self.method()
            
    def stopped(self):
        return self._stopper.isSet()

    def stop(self):
        self._stopper.set()