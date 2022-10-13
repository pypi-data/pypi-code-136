import os
import glob
import re
import yaml
from multiprocessing import Pool, Manager, cpu_count
from yaml.parser import ParserError
from .scheduler import scheduler, Task
from .moment import Moment
from .scheduler import action
from .utils import OhNo, log
from .istarmap import *
import datetime as dt
from rich.progress import Progress, BarColumn, TimeElapsedColumn, TimeRemainingColumn, SpinnerColumn
from itertools import repeat
import __main__


class Meeseeks:
    """Hold the list of tasks to accomplish.

    Call M. Meeseeks to process the tasks you want.
    Tasks to be called are defined with the `@action`
    decorator.

    Please note that you have **two ways** for defining
    an action.

    1. Use `@action` decorators on a function and pass your parameters.
    2. Use a `yaml` configuration file.

    Note
    ----
    You can combine a file with `@action`.
    No seriously, you can.

    Each task will be executed on the list of items
    that have been found, or before the batch,
    or after the batch depending on the `when` attribute
    of your action.

    In your python script, define the actions called
    from the `yaml` file and then call Mr. Meeseeks.

    Note
    ----
    You only have to invoke a Meeseeks to process your jobs.

    Attributes
    ----------
    items : list
       list of items to process
    folders : list
       list of folders to look into to find files, filenames will be appended to `items`
    yaml_file : str
       a YAML string or a path to a YAML file to load configuration from.
    progress : bool
       either to show progress
    log_file : str
       log output into file
    recursive : bool
       when looking for files in folder, set the recursivity
    watch : MeeseeksWatch
       give a watch to you Meeseeks so it can filter items by datetime
    processes : int
       number of processes to use to parallelize the batches
    """
    def __init__(self,
                 items = [],
                 folders = [],
                 yaml_file = None,
                 progress = True,
                 log_file = None,
                 recursive = True,
                 watch=None,
                 processes=cpu_count()):
        """Create the Meeseeks just for you.

        Parameters
        ----------
        file : str
           filename or raw content of the `yaml` job file.
        """
        "Create the Meeseeks just for you."
        self.yaml_file = yaml_file
        self.recursive = recursive
        self.progress = progress
        self.log_file = log_file
        self.watch = watch
        self.items = items
        self.folders = folders
        self.data = None
        self.output = {}
        self.processes = processes

        functions = dict((name, thing) for (name, thing)
                         in locals().items() if callable(thing))

        # Now load the YAML file
        if self.yaml_file:
            self.read_yaml()


        # Start the process
        self.i_am_mr_meeseeks()

    def read_yaml(self):
        # Load the YAML string or file
        self.data = self.load()
        # Interpret the YAML data
        self.look_at_me()

    def load(self):
        "Return the data of the YAML file."
        try:
            if os.path.exists(self.yaml_file):
                with open(self.yaml_file, 'r') as f:
                    return yaml.safe_load(f)
            else:
                return yaml.safe_load(self.yaml_file)
        except ParserError:
            OhNo(f"Unable to parse {self.yaml_file}, an error occured.")

    def look_at_me(self):
        "Init the properties of your Meeseeks from the YAML."
        if 'properties' in self.data:
            if 'progress' in self.data['properties']:
                self.progress = self.data['properties']['progress']
            if 'logfile' in self.data['properties']:
                self.log_file = self.data['properties']['log_file']

        # Now check missing parameters in the actual object
        check_mandatory = {}
        if not self.folders:
            check_mandatory['input'] = ['folders']
        if not scheduler.tasks_list:
            check_mandatory['tasks'] = []

        for entry in check_mandatory:
            if entry not in self.data:
                raise OhNo(f'{entry} not found in configuration file!')
            for subentry in self.data[entry]:
                if subentry not in self.data[entry]:
                    raise OhNo(f'{entry}/{subentry} not found in \
                    configuration file!')

        # Now check them
        if 'input' in self.data:
            if 'folders' in self.data['input']:
                self.folders.extend(self.data['input']['folders'])

            # Now check the optionnal parameters
            if 'recursive' in self.data['input']:
                self.recursive = self.data['input']['recursive']

            if 'date' in self.data['input']:
                begin = end = format_str = regexp = None
                if 'begin' in self.data['input']['date']:
                    begin = self.data['input']['date']['begin']
                if 'end' in self.data['input']['date']:
                    end = self.data['input']['date']['end']
                if 'format_str' in self.data['input']['date']:
                    format_str = self.data['input']['date']['format_str']
                if 'regexp' in self.data['input']['date']:
                    regexp = self.data['input']['date']['regexp']

                self.watch = MeeseeksWatch(begin=begin,
                                           end=end,
                                           format_str=format_str,
                                           regexp=regexp)

        # Now add the actions to the scheduler
        if 'tasks' in self.data:
            for task_name in self.data['tasks']:
                if task_name in self.data:
                    # now create the task
                    task = Task()
                    # action is handled differently
                    if not ('action' in self.data[task_name]):
                        raise OhNo(f'You must defined an `action` name\
                        in your task {task_name}.')

                    # get action
                    a = self.data[task_name]['action']
                    # check the action exists
                    functions = dict((name, thing) for (name, thing)
                                     in locals().items() if callable(thing))
                    if a in functions:
                        task.action = functions[a]
                    else:
                        raise OhNo(f'Action {a} not known in current scope.')
                    fields = [s for s in dir(t) if '__' not in s]
                    for field in fields:
                        if field in self.data[task_name] and field != 'action':
                            setattr(task, field, self.data[task_name][field])
                    scheduler.add(task)
                else:
                    raise OhNo(f'`{task_name}` not found,\
                    in YAML file!')

    def i_am_mr_meeseeks(self):
        "Start the process."
        # Read input items
        self.read_input()

        # schedule
        scheduler.schedule()

        # Execute actions
        if self.progress:
            self.do_it_progress()
        else:
            self.do_it()

    def read_input(self):
        """Process the YAML input tag

        Process the input tag to retrieve the items
        and times. Fill the following values:
        - items
        - time
        - time_correspondence

        Items are added if the first frame is between
        begin and end dates.
        """
        log.info('Reading input files from folders...')
        for folder in self.folders:
            if isinstance(folder, list):  # list of files
                for f in folder:
                    self.items.extend(glob.iglob(f,
                                                 recursive=self.recursive))
            else:
                self.items.extend(glob.iglob(folder,
                                             recursive=self.recursive))

        items_copy = self.items.copy()
        if self.watch:
            with Progress(
                "[progress.description]{task.description}",
                BarColumn(),
                "[progress.percentage]{task.percentage:>3.0f}%",
                TimeRemainingColumn(),
                TimeElapsedColumn(),
                SpinnerColumn()) as progress:
                task_id = progress.add_task("[bold cyan]:right_arrow: Sorting items", total=len(self.items))
                for f in self.items:
                    progress.advance(task_id)
                    if not self.watch.check_watch(f):
                        items_copy.remove(f)
                progress.update(task_id, completed=len(self.items), description = "[bold green]:heavy_check_mark: Sorting items")
        self.items = items_copy
        if len(self.items) == 0:
            log.error('No corresponding file found. Please check your regexp?')
        try:
            self.items = sorted(self.items)
        except TypeError:
            pass
        log.info(f'{len(self.items)} items to process found')

    def do_it_progress(self):
        # Schedule
        scheduler.schedule()

        # Do BEFORE actions
        with Progress(
                "[progress.description]{task.description}",
                BarColumn(),
                "[progress.percentage]{task.percentage:>3.0f}%",
                TimeRemainingColumn(),
                TimeElapsedColumn(),
                SpinnerColumn()) as progress:
            tasks = scheduler.get_task_batches(Moment.BEFORE)
            task_id = progress.add_task("[bold cyan]:right_arrow: Performing step BEFORE", total=len(tasks))
            for task in tasks:
                task_id_step = progress.add_task(f"   [cyan]:diamond_suit: Applying {task}....", total=1)
                task.action()
                progress.update(task_id_step, advance=1, description=f"   [green]:heavy_check_mark: Applying {task}....")
            progress.update(task_id, completed=len(tasks), description = "[bold green]:heavy_check_mark: Performing step BEFORE")

            # batch process
            tasks = scheduler.get_task_batches(Moment.ON_ITEM)
            task_id = progress.add_task("[bold cyan]:right_arrow: Performing step ON_ITEM", total=len(tasks))

            m = Manager()
            sharedtree = m.dict()
            with Pool(processes=self.processes) as pool:
                for task in tasks:
                    task_id_file = progress.add_task(f"   [cyan]:diamond_suit: Applying {task} on each file...", total=len(self.items[::task.rate]))
                    # We need to call the function from the __main__, not the one stored into the task
                    # because the pool won't see it and will raise
                    # "my_action is not the same object as __main__.my_action"
                    # Maybe we should do setattr on __main__ instead?
                    for res in pool.istarmap(getattr(__main__, task.name), zip(self.items[::task.rate], repeat(sharedtree))):
                        progress.update(task_id_file, advance=1)

                    progress.update(task_id, advance=1)
            progress.update(task_id, completed=len(tasks), description="[bold green]:heavy_check_mark: Performing step ON_ITEM")


            # Do AFTER actions
            tasks = scheduler.get_task_batches(Moment.AFTER)
            task_id = progress.add_task("[bold cyan]:right_arrow: Performing step AFTER", total=len(tasks))
            # We change the shared memory to a standard dict
            # It allows to use pickle.dump for instance
            data = dict(sharedtree)
            for task in tasks:
                task_id_step = progress.add_task(f"   [cyan]:right_arrow: Applying {task}....", total=1)
                task.action(data)
                progress.update(task_id_step, advance=1, description=f"   [green]:heavy_check_mark: Applying {task}....")
                progress.update(task_id, advance=1)
            progress.update(task_id, completed=len(tasks), description="[bold green]:heavy_check_mark: Performing step AFTER")

        def do_it(self):
            tasks = scheduler.get_task_batches(Moment.BEFORE)

            for task in tasks:
                task.action()

            # batch process
            tasks = scheduler.get_task_batches(Moment.ON_ITEM)

            with Pool(processes=self.processes) as pool:
                manager = Manager()
                sharedtree = manager.dict()
                for task in tasks:
                    # We need to call the function from the __main__, not the one stored into the task
                    # because the pool won't see it and will raise
                    # "my_action is not the same object as __main__.my_action"
                    # Maybe we should do setattr on __main__ instead?
                    pool.istarmap(getattr(__main__, task.name), zip(self.items[::task.rate], repeat(sharedtree)))

            # Do AFTER actions
            tasks = scheduler.get_task_batches(Moment.AFTER)
            # We change the shared memory to a standard dict
            # It allows to use pickle.dump for instance
            data = dict(sharedtree)
            for task in tasks:
                task.action(data)

    def __str__(self):
        to_show = {
            'File': self.file,
            'Recursive': self.recursive,
            'Log': self.log_file
        }
        string = "Existence is pain!\n"
        for key in to_show:
            string += f'\t{key}: {to_show[key]}\n'
        return string


class MeeseeksWatch():
    """A watch to store date and time.

    This class defines a watch to give to your
    Meeseeks. It enables him to perform tasks
    on a particular range of `datetime`.

    Note
    ----
    Please note that you do not need to provide
    a `begin` and `end` date but you need to provide
    at least one of the two.

    Warning
    -------
    The regexp used to extract the date from the filename
    is mandatory for now because it makes a lot of time improvement.
    The regexp is applied to the bare filename
    (with the extension).

    Note
    ----
    Therefore, the regexp can be used to also sort files
    by extension.


    Attributes
    ----------
    begin : datetime
       date to begin
    end : datetime
       date to end
    format_str : string
       the format to fetch the date from (isoformat by default)
    regexp : string
       a regexp to extract the date from the filename (with its extension)

    Methods
    -------
    get_date_from_file(file)
       Extract the date from the file.
    check_watch(file) : bool
       Make sure that the `file` is in the range of the watch.
    """

    def __init__(self,
                 begin=None,
                 end=None,
                 format_str='%Y-%m-%dT%H:%M:%S',
                 regexp='^.*_(.*).hdf5'):
        "Wind up the watch."
        self.begin = begin
        self.end = end
        self.format_str = format_str
        self.regexp = regexp

        if not(self.begin or self.end):
            raise OhNo('You must provide at least one `begin` or `end`\
            date if you provide `date` field.')

    def get_date_from_file(self, file):
        "Extract the date from the file."
        if m := re.match(self.regexp, file):
            try:
                return dt.datetime.strptime(m.group(1), self.format_str)
            except ValueError:
                log.warning(f'Unable to parse date from {file} with {self.format_str}.')
                return None
        else:
            log.warning(f'Unable to get date from {file}.')
        return None

    def check_watch(self, file):
        "Make sure that the `file` is in the range of the watch"
        if date := self.get_date_from_file(os.path.basename(file)):
            if self.begin and self.end:
                return date >= self.begin and date <= self.end
            elif self.begin:
                return date >= self.begin
            elif self.end:
                return date <= self.end
        return False

    def __str__(self):
        return f'{self.begin} - {self.end}'
