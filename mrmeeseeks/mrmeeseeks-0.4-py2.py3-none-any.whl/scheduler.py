import inspect
from functools import wraps
from .moment import Moment
from .utils import OhNo, log


class Task:
    """Holds a task to be executed at some point.

    A task wraps an action to be performed and
    holds various information about how this action
    should be executed.

    Attributes
    ----------
    action : function
       the action to be executed
    when : Moment (default=Moment.ON_ITEM)
       when to execute the action
    rate : int (default=1)
       the action will be executed on each `n = rate` items
    begin : datetime (default=None)
       minimum date from which to proceed
    end : datetime (default=None)
       maximum date from which to proceed
    depends : list (default=[])
       list of function name on which this task depends on
    skip : bool (default=False)
       either to skip this task
    """

    def __init__(self,
                 action=None,
                 name=None,
                 when=Moment.ON_ITEM,
                 rate=1,
                 begin=None,
                 end=None,
                 skip=False,
                 depends=[]):
        "Create a task."
        self.action = action
        self.name = name
        self.when = when
        self.rate = rate
        self.begin = begin
        self.end = end
        self.depends = depends
        self.skip = skip

    def __str__(self):
        return f"task_{self.name}"


class Scheduler:
    """Handle and organize the Tasks.

    The Scheduler makes organize the different
    tasks by considering their dependencies.

    Attributes
    ----------
    Attributes

    Methods
    -------
    Methods

    """

    def __init__(self):
        "Init the Scheduler."
        self.tasks_list = {}
        self.batches = []

    def add(self, task):
        "Add a task to the scheduler."

        name = task.name
        i = 1
        while name in self.tasks_list:
            name = f'{task.name}_{i}'
            i = i + 1
        self.tasks_list[name] = task

    def check_dependencies(self):
        for task in self.tasks_list:
            t = self.tasks_list[task]
            if t.depends:
                for deps in t.depends:
                    if deps in self.tasks_list:
                        if t.when < self.tasks_list[deps].when:
                            OhNo(f'{t} depends on {self.tasks_list[deps]} but \
                            {self.tasks_list[deps]} is supposed to be executed\
                            after {self.tasks_list[deps]}!')
                    else:
                        OhNo(f'{deps} dependency of {t} is not known.')
        return True

    def get(self, task_name):
        if task_name in self.tasks_list:
            return self.tasks_list[task_name]
        else:
            raise OhNo(f'{task_name} does not exists in scheduler.')

    def schedule(self):
        "Schedule the different tasks based on dependencies."
        self.batches = []
        if self.check_dependencies():
            for step in sorted(Moment):
                self.batches.extend(self.get_task_batches(step))

    def get_batches(self):
        "Return an iterator of the batches."
        for b in self.batches:
            yield b

    def reset(self):
        self.tasks_list = {}
        self.batches = []

    def get_task_batches(self, step):
        step_batches = []
        deps = []
        for task in self.tasks_list:
            t = self.tasks_list[task]
            if t.when == step and not t.skip:
                deps.append((task, set(t.depends)))
        if deps:
            deps = dict(deps)
        while deps:
            # Get all nodes with no dependencies
            ready = {name for name in deps if not deps[name]}
            # If there aren't any, we have a loop in the graph
            if not ready:
                msg = "Circular dependencies found!\n"
                msg += self.__str__()
                raise OhNo(msg)

            # Remove them from the dependency graph
            for name in ready:
                del deps[name]
            for d in deps.values():
                d.difference_update(ready)
            # Add the batch to the list
            step_batches.extend([self.tasks_list[name] for name in ready])
        # Return the list of batches
        return step_batches

    def __str__(self):
        msg = []
        for t in self.batches:
            for parent in t.depends:
                msg.append("%s -> %s" % (t.name, parent))
        return "\n".join(msg)


scheduler = Scheduler()

# Create the action decorator
def action(*args, **kwargs):
    """Defines an action for Mr. Meeseeks.

    This is a decorator that can be used to
    define and execute your batch actions.

    Note
    ----
    All attributes are optionnals.

    Attributes
    ----------
    when : Moment (Moment.ON_ITEM)
       when to execute the action (see `Moment` class)
    rate : int (1)
       if executed on Moment.ON_ITEM, process on each (n = rate) items
    begin : datetime (None)
       minimum date to process from
    end : datetime (None)
       maximum date to process to
    depends : list ([])
       if this should be executed after others actions
    name : str (default: name of function)
       override the default name used by the scheduler
    skip : bool (default: False)
       either to skip this action
    """
    def decorator(func):
        # if func.__name__ not in cache:
        #     cache[func.__name__] = func
        # assign the action
        # Create the task
        task = Task(**kwargs)
        task.action = func
        if not task.name:
            task.name = func.__name__
        # Append to the list of known actions
        scheduler.add(task)

        @wraps(func)
        def wrapper(*arguments, **keywords):
            return func(*arguments, **keywords)
        return wrapper

    # Handle the fact that no parenthesis has
    # been put onto @action
    # then, the args are not empty (it is the `func`)
    if args:
        func = args[0]
        return decorator(func)
    return decorator
