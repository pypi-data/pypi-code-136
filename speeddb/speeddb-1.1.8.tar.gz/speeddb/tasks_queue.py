'''
## SpeedDB Tasks Queue

### Main Functions
`TasksQueue`:
   Parameters:
```
      max_threads:int = 1 (Optional) # Not working currently :/
```

'''

from queue import Queue, Empty
from concurrent.futures import ThreadPoolExecutor

class TasksQueue:
   '''
   Tasks Queue is a way to run multiple tasks (functions) in line

   >>> import speeddb
   >>> import time
   >>> tq = speeddb.TasksQueue())
   >>> def task(sec:int=1):
   ...     print(f"START: Task ({sec})")
   ...     time.sleep(sec)              
   ...     print(f"END: Task ({sec})")
   ... 
   >>> tq.add_task_and_execute(task, 3) 
   START: Task (3)
   >>> tq.add_task_and_execute(task, 2) 
   >>> END: Task (3)
   START: Task (2)
   END: Task (2)

   This might not look clear, but Task (3) started, then once it finished Task (2) started
   
   '''
   def __init__(self, max_threads:int=1):
      self._queue:Queue = Queue()
      self._threadPool = ThreadPoolExecutor(max_threads, "SpeedDB_TasksQueue")
   
   def add_task_and_execute(self, task, *args, **kwargs):
      unfinished_tasks = self._queue.unfinished_tasks

      self._queue.put({
         "task": task,
         "args": args,
         "kwargs": kwargs
      })
      
      if unfinished_tasks == 0:
         self._threadPool.submit(self._clear_queue)

   def _clear_queue(self):
      try:
         while not self._queue.empty():
            task, args, kwargs = map(self._queue.get_nowait().get, ("task", "args", "kwargs"))
            task(*args, **kwargs)
            self._queue.task_done()
      except Empty:
         pass