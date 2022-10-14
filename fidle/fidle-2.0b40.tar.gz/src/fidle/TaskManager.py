# ------------------------------------------------------------------
#   _______        _    __  __                                   
#  |__   __|      | |  |  \/  |                                  
#     | | __ _ ___| | _| \  / | __ _ _ __   __ _  __ _  ___ _ __ 
#     | |/ _` / __| |/ / |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
#     | | (_| \__ \   <| |  | | (_| | | | | (_| | (_| |  __/ |   
#     |_|\__,_|___/_|\_\_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   
#                                                 __/ |          
#                                                |___/   
#                                                  fidle.TaskManager                          
# ------------------------------------------------------------------
#     
# A simple class to manage a list of tasks in a distributed way.
# Jean-Luc Parouty CNRS/MIAI/SIMaP 2022

# Task list is an array of dict
#
# <task list> = [ <task> ]
# <task>      = {  id     = <task id>,
#                  after  = [ <task id regex>, ...]
#                  status = "ready" | "running" | "done" | "desactivated",
#                  runner = <runner id>, 
#                  start  = <date time>,
#                  end    = <daate time>
#  }



import os,platform,sys
import json
import datetime, time
import re
import math
import random
from random  import uniform

import fidle.config
from fidle.Chrono import Chrono


class LockException(Exception):
    pass


class TaskManager:

    __version__  = fidle.config.VERSION


    # --------------------------------------------------------------
    # -- Init TaskManager
    # --------------------------------------------------------------
    #
    def __init__(self, tasklist         = [], 
                       taskfile         = './taskfile.json', 
                       lockfile         = './taskfile.lock', 
                       verbose          = 0,
                       sleep_start      = 4,
                       lock_check_delay = 0.100,
                       lock_retry_min   = 0.8,
                       lock_retry_max   = 1.2,
                       lock_retry_k     = 4 ):
        self.verbose = verbose
        self.whoami           = platform.uname()[1]+'-'+str(os.getpid())
        self.task_list        = tasklist
        self.task_file        = taskfile
        self.lock_file        = lockfile
        self.sleep_start      = sleep_start
        self.lock_check_delay = lock_check_delay
        self.lock_retry_min   = lock_retry_min
        self.lock_retry_max   = lock_retry_max
        self.lock_retry_k     = lock_retry_k

        # For monitoring (about)
        self.duration         = 0
        self.max_retry        = 0
        self.done_tasks       = 0

        # For random
        random.seed(os.getpid())

        # Locked state
        self.locked       = False

        # Checks afters
        self.__check_afters()

        # Verbosity
        if self.verbose>0 : self.show('Init TaskManager, done.')



    def __check_afters(self):
        for t in self.task_list:
            # No after    : add after None
            t['after'] = t.get('after', None)
            # After empty : set None
            if t['after'] == '' : t['after']=None
            # After None  : ok
            if t['after'] is None : continue
            # After is a string
            if isinstance(t['after'], str) : t['after'] = [s.strip() for s in t['after'].split(',')]
            # Not a list...
            if not isinstance(t['after'], list) :
                self.show(f"*** Oups, after directive for task [{t['id']}] is invalid...")
                sys.exit(1)



    # --------------------------------------------------------------
    # -- Verbosity
    # --------------------------------------------------------------
    #

    def show(self, *what):
        '''
        Print informations with a <time> <host-pid> prefix
        if an info item is "tasks", then print tasks list. 
        Params:
            *whats : list of informations
        Return:
            None
        '''
        when = datetime.datetime.now().strftime('%H:%M:%S.%f')
        for w in what:
            if w=='tasks':
                print(f'\n{when} {self.whoami} : Tasks list :')
                print( json.dumps(self.task_list, ensure_ascii=False, indent=4))
            else:
                print(f'{when} {self.whoami} : {w}')
            
    def about_this_runner(self):
        '''
        Display a summary of the runnable() session
        Params:
            None
        Returns:
            None
        '''
        self.show('About this runner :')
        self.show(f'    Done tasks     : {self.done_tasks}' )
        self.show(f'    Lock retry     : {self.max_retry}'   )
        self.show(f'    Total duration : {self.total_duration}'    )


    # --------------------------------------------------------------
    # -- Runnable
    # --------------------------------------------------------------
    #
    def runnable(self):
        '''
        Task generator, allowing to iterate on the task list.
        Each time an item is given, it is marked 'runnning' while 
        the previous one is marked 'done'.
        Params:
            None
        Returns:
            Sequence of task_id 
        '''
        # Few monitoring
        chrono = Chrono()
        chrono.start('total')
        self.max_retry      = 0
        self.done_tasks     = 0
        self.total_duration = 0

        # In order not to start all at the same time
        time.sleep(uniform(0, self.sleep_start))

        # Let's go...
        task_id  = ''
        duration = 0
        now      = chrono.now()
        while task_id is not None:

            # ---- Retrieve tasks list
            #
            self.__lock(retry=15)
            self.__load_tasks()

            # ---- Set current task as : done
            #
            self.__set_done(task_id, now, duration)
            
            # ---- Pick a new task
            #
            task_id  = self.__pick_task()

            # ---- Set new task as : running 
            #
            self.__set_running(task_id, now)

            # ---- Save tasks list
            #
            self.__save_tasks()
            self.__unlock()

            # ---- Yield new task
            #
            if task_id is not None :
                if self.verbose>0 :    self.show(f'Task [{task_id}] is starting')
                chrono.start('task')
                yield task_id
                duration = chrono.get_delay('task', format='seconds')
                now      = chrono.now()
                if self.verbose>0 :    self.show(f'Task [{task_id}] is done after {duration}s')
        
        self.total_duration = chrono.get_delay('total', format='seconds')



    # --------------------------------------------------------------
    # -- Lock
    # --------------------------------------------------------------
    #
    def __lock(self, retry=15):
        '''
        Try to take the hand, by creating a lock file.
        Wait and retry if a lock file still exist.
        Params:
            retry : Number of tries (5)
        Return:
            True if lock is created, else False.
        '''
        if self.verbose>1 : self.show("TaskManager - Lock")

        # ---- Still locked
        #
        if self.locked:
            if self.verbose>1 : self.show("    Still locked.. Etonnant, non ?")
            return self.locked

        # ---- No locked, we try to
        #
        n_retry=0
        while (self.locked==False) and (n_retry<retry):

            # ---- Is there a lock file ?
            #
            if not os.path.isfile(self.lock_file): 
                # It's free, so we can create a lockfile
                open(self.lock_file, "w").write(self.whoami)
                if self.verbose>1 : self.show('    No lock file : we try to put one')
                # We wait a moment and we check that we have the hand
                # Maybe someone else was faster!
                if self.verbose>1 : self.show('    Wait and check it')
                time.sleep(self.lock_check_delay)
                try: 
                    locker_id   = open(self.lock_file).readline()
                    self.locked = (locker_id == self.whoami)
                except:
                    if self.verbose>1 : self.show('    We got passed !')
                    self.locked = False

            if not self.locked:
                # The place is not free, we wait a moment and try again
                t = uniform(self.lock_retry_min, self.lock_retry_max) * math.e**(n_retry/self.lock_retry_k)
                if self.verbose>1 : self.show(f'    Lock file exist, wait {t:0.2f}s and retry ({n_retry})...')
                time.sleep(t)
                n_retry += 1
                # for informations
                self.max_retry = max(self.max_retry, n_retry)

        if self.verbose>1 : self.show(f'    Locking is: {self.locked}')
        if not self.locked: 
            raise LockException('Lock failed... (increase the number of retries ?)')
        else:
            if self.verbose>1 : self.show(f'    Nb retry : {n_retry}')
            return self.locked


    # --------------------------------------------------------------
    # -- Unlock
    # --------------------------------------------------------------
    #
    def __unlock(self):
        if self.verbose>1 : self.show('TaskManager - Unlock')
        os.unlink(self.lock_file)
        self.locked = False
        if self.verbose>1 : self.show(f'    Lock file removed ({self.lock_file})')


    # --------------------------------------------------------------
    # -- Load tasks
    # --------------------------------------------------------------
    #
    def __load_tasks(self):
        '''
        Load tasks file. Create the file if it does not exist.
        '''
        if self.verbose>1 : self.show(f'TaskManager - Load tasks')

        # ---- Task file exist : Read and return it
        #
        if os.path.isfile(self.task_file):
            with open(self.task_file) as fp:
                self.task_list = json.load(fp)
            if self.verbose>1 : self.show(f'    Loaded ({self.task_file})')
            return self.task_list

        # ---- Doesn't exist : Save it
        #
        if self.verbose>1 : self.show('    Tasks file does not exist, create it...')
        self.__save_tasks()


    # --------------------------------------------------------------
    # -- Pick task
    # --------------------------------------------------------------
    #
    def __pick_task(self):
        '''
        Pick a task from the list, checking the dependency constraints.
        Task is picked from self.task_list.
        params:
            none
        return:
            picked task_id
        '''
        if self.verbose>1 : self.show('TaskManager - Pick a task')

        # ---- Search a task to run...
        #
        picked_task = None
        for task in self.task_list:
            # Check if status is "ready" 
            if task['status'] != 'ready': continue 
            # Check for dependencies (after)
            if self.__check_dependency(task) is False : continue
            # Ok, this one is runnable
            picked_task = task
            break
        
        # ---- No tasks are available...
        #
        if picked_task is None : 
            if self.verbose>1 : self.show('    Cannot find a new task')
            return None

        # ---- return picked task id
        #
        picked_task_id = picked_task['id']
        if self.verbose>1 : self.show(f"    Selected task is : {picked_task_id}")
        return picked_task_id


    # --------------------------------------------------------------
    # -- Get task
    # --------------------------------------------------------------
    #
    def __get_task(self, task_id):
        for task in self.task_list:
            if task['id']==task_id: return task
        return None

    # --------------------------------------------------------------
    # -- Set running
    # --------------------------------------------------------------
    #
    def __set_running(self, task_id, now):
        '''
        Set given task_id as "running"
        Complete status, runner and start attributes.
        Params:
            task_id : Task id
        Return:
            None
        '''
        if self.verbose>1 :     self.show(f"TaskManager - Set running")
        # ---- Get task by id
        task=self.__get_task(task_id)
        # ---- No task, do noything
        if task is None: 
            if self.verbose>1 : self.show(f'    Task is None, do nothing.')
            return
        # ---- Set task as running
        if self.verbose>1 :     self.show(f'    Task set as running ({task_id})')
        task['status'] = 'running'
        task['runner'] = self.whoami
        task['start' ] = now
        task['end'   ] = ''


    # --------------------------------------------------------------
    # -- Set done
    # --------------------------------------------------------------
    #
    def __set_done(self, task_id, now, duration):
        '''
        Set given task_id as "done"
        Complete status and end attributes.
        Params:
            task_id : Task id
        Return:
            None
        '''
        if self.verbose>1 :     self.show(f"TaskManager - Set done")
        # ---- Get task by id
        task=self.__get_task(task_id)
        # ---- No task, do noything
        if task is None: 
            if self.verbose>1 : self.show(f'    Task is None, do nothing.')
            return
        # ---- Set task as done
        if self.verbose>1 :     self.show(f"    Task is set as done ({task_id})")
        task['status']   = 'done'
        task['end'   ]   = now
        task['duration'] = duration
        self.done_tasks += 1


    # --------------------------------------------------------------
    # -- Save task
    # --------------------------------------------------------------
    #
    def __save_tasks(self):
        if self.verbose>1 :     self.show(f'TaskManager - Save tasks')
        with open(self.task_file, 'w', encoding='utf-8') as fp:
            json.dump(self.task_list, fp, ensure_ascii=False, indent=4)
        if self.verbose>1 :     self.show(f'    Saved as : {self.task_file}')



    # --------------------------------------------------------------
    # -- Check dependency
    # --------------------------------------------------------------
    #
    def __check_dependency(self, task):
        # On va chercher une bonne raison pour refuser...

        # Filter is None : No contrains, no reason...
        if task['after'] is None : 
            return True

        # For each entry in the after table 
        for filter in task['after']:

            # We check each task
            for t in self.task_list:
                # Exclude me and desactivated
                if t['id']     == task['id']        : continue
                if t['status'] == 'desactivated'    : continue
                # Doesn't match : next
                if not re.match(filter, t['id'])    : continue
                # Status is not "done" : return False
                if t['status'] != 'done' : return False

        # Arrived here, we found no reason to refuse
        return True




    def update_dependencies(self): 
        '''
        Check and update dependencies. If a task is needed in an after filter, 
        his status will be forced to "ready" 
        Params:
            None
        Returns:
            List of updated tasks
        '''
        if self.verbose>1 :     self.show(f"Update dependancies")
        self.__updated = []
        for task in self.task_list:
            self.__update_dependencies(task)
        return self.__updated



    def __update_dependencies(self, task):
        # Pas active
        if task['status'] != 'ready' : return
        # Pas de dépendances
        if task['after'] is None     : return
        # For each filter in the after list 
        for filter in task['after']:
            # We check each task
            for t in self.task_list:
                # Exclude me
                if task['id'] == t['id']        : continue
                # Doesn't match : next
                if not re.match(filter, t['id']): continue
                # Status have to be ready
                if t['status']!='ready':
                    if self.verbose>0 : self.show(f"Note : For dependency reasons [{t['id']}] is added.")
                    t['status'] = 'ready'
                    self.__updated.append(t['id'])
                # Set dependancies
                self.__update_dependencies(t)
