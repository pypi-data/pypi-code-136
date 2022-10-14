import copy
import os
import typing
import weakref

from remotemanager.storage.database import Database
from remotemanager.storage.function import Function
from remotemanager.storage.sendablemixin import SendableMixin
from remotemanager.logging.utils import format_iterable
from remotemanager.utils.uuid import generate_uuid
from remotemanager.utils import ensure_list
from remotemanager.logging import LoggingMixin

from datetime import datetime


class Runner(SendableMixin, LoggingMixin):
    """
    The Runner class stores any info pertaining to this specific run. E.g.
    Arguments, result, run status, files, etc.

    .. warning::
        Interacting with this object directly could cause unstable behaviour.
        It is best to allow Dataset to handle the runners. If you require a
        single run, you should create a Dataset and append just that one run.
    """

    _defaults = {'skip': False}

    _state_direct_remote = 'disconnected - remote direct run'
    _state_script_remote = 'script submitted remotely'
    _state_script_local = 'script submitted locally'

    def __init__(self,
                 arguments: dict,
                 dbfile: str,
                 parent_uuid: str,
                 extra_files_send: list = None,
                 extra_files_recv: list = None,
                 dependency_key: str = None,
                 **kwargs):

        self._run_options = self._set_defaults(kwargs)

        self._args = arguments

        self._extra_files = {'send': extra_files_send
                                if extra_files_send is not None else [],
                             'recv': extra_files_recv
                                if extra_files_recv is not None else []}

        if arguments is not None \
                and not isinstance(arguments, dict):
                raise ValueError(f'runner arguments ({type(arguments)}) '
                                 'must be dict-type')

        self._dependency_info = {}

        uuid_slug = copy.deepcopy(arguments)
        if uuid_slug is None:
            uuid_slug = {}
        uuid_slug.update(kwargs)
        uuid_slug.update(self.extra_files)
        uuid_slug.update({'dependency_key': dependency_key})
        self._uuid = generate_uuid(format_iterable(uuid_slug))
        self._time_format = '%Y-%m-%d %H:%M:%S'
        self._state_time = None
        self._state = None
        self._extension = 'yaml'

        self._dbfile = dbfile
        self._parent_uuid = parent_uuid

        self._logger.info(f'new runner (id {self.uuid}) created')

        self._history = {}
        self.state = 'created'

    def __hash__(self) -> str:
        return hash(self.uuid)

    @property
    def database(self) -> Database:
        """
        Access to the stored database object.
        Creates a connection if none exist.

        Returns:
            Database
        """
        if not hasattr(self, '_database'):
            self._database = Database(file=self._dbfile)
        return self._database

    @staticmethod
    def _set_defaults(kwargs: dict = None) -> dict:
        """
        Sets default arguments as expected. If used as a staticmethod, returns
        the defaults
        """

        if kwargs is None:
            kwargs = {}

        for k, v in Runner._defaults.items():
            if k not in kwargs:
                kwargs[k] = v

        return kwargs

    @property
    def uuid(self):
        """
        The uuid of this runner
        """
        return self._uuid

    @property
    def short_uuid(self):
        """
        A short uuid for filenames
        """
        return self.uuid[:8]

    @property
    def runfile(self):
        """
        Filename of the python runfile
        """
        return f'{self.short_uuid}-run.py'

    def runpath(self, local: bool = False):
        """
        Runfile name

        Args:
            local (bool):
                returns the runfile path prior to sending if True
        """
        if local:
            return os.path.join(self.local_dir, self.runfile)
        paths = [self.remote_dir]
        if self.run_dir != self.remote_dir and self.run_dir is not None:
            paths.append(self.run_dir)
        paths.append(self.runfile)
        return os.path.join(*paths)

    @property
    def scriptfile(self):
        """
        Filename of the run script
        """
        return f'{self.short_uuid}-run.sh'

    def scriptpath(self, local: bool = False):
        """
        Run script path

        Args:
            local (bool):
                returns the run script path prior to sending if True
        """
        if local:
            return os.path.join(self.local_dir, self.scriptfile)
        paths = [self.remote_dir]
        paths.append(self.scriptfile)
        return os.path.join(*paths)

    @property
    def resultfile(self):
        """
        Result file name
        """
        return f'{self.short_uuid}-result.{self.result_extension}'

    def resultpath(self, local: bool = False):
        """
        Path to result file
        """
        if local:
            return os.path.join(self.local_dir, self.resultfile)
        paths = [self.remote_dir]
        if self.run_dir != self.remote_dir and self.run_dir is not None:
            paths.append(self.run_dir)
        paths.append(self.resultfile)
        return os.path.join(*paths)

    @property
    def result_extension(self):
        """
        Resultfile file format extension
        """
        return self._extension

    @result_extension.setter
    def result_extension(self, ext):
        """
        Sets the resultfile format extension

        .. warning::
            This does not change anything aside from the extension that
            the runner looks for when trying to find a result file. If you
            require a different serialisation, you should set the serialiser.
        """
        self._extension = ext.strip('.')

    @property
    def local_dir(self):
        """
        Local staging directory
        """
        return self._run_options.get('local_dir', 'staging')

    @local_dir.setter
    def local_dir(self,
                  path: str) -> None:
        """
        Sets the local_dir
        """
        self._run_options['local_dir'] = path

    @property
    def remote_dir(self):
        """
        Target directory on the remote for transports
        """
        if 'remote_dir' in self._run_options:
            return self._run_options['remote_dir']
        return self._run_options.get('run_dir', 'runner_remote')

    @remote_dir.setter
    def remote_dir(self,
                   path: str) -> None:
        """
        Sets the remote_dir
        """
        self._logger.debug(f'setting remote dir to {path}')
        self._run_options['remote_dir'] = path

    @property
    def run_dir(self):
        """
        Intended running directory. If not set, uses remote_dir

        .. note::
            If both remote_dir and run_dir are set, the files will be
            transferred to remote_dir, and then executed within run_dir
        """
        if 'run_dir' in self._run_options:
            return self._run_options['run_dir']
        return None

    @run_dir.setter
    def run_dir(self,
                dir: str) -> None:
        """
        Sets the run_dir
        """
        self._run_options['run_dir'] = dir

    @property
    def args(self):
        """
        Arguments for the function
        """
        return self._args

    @property
    def extra_files(self):
        """
        Returns the extra files set for this runner
        """
        return self._extra_files

    @property
    def result(self):
        """
        Result (If available)
        """
        if hasattr(self, '_result'):
            return self._result
        return None

    @result.setter
    def result(self, result) -> None:
        """
        Creates and sets the result property, setting the state to "completed"

        Args:
            result:
                run result
        """
        self._result = result
        self.state = 'completed'

    def clear_result(self):
        """
        Removes any results, and sets the state to "result wiped"
        """
        try:
            del self._result
        except AttributeError:
            pass

        def remove_file(path):
            self._logger.info(f'attempting to clear result file {path}')
            try:
                os.remove(path)
                self._logger.info('Done')
            except FileNotFoundError:
                self._logger.info('file not found')

        remove_file(self.resultpath(local=True))
        remove_file(self.resultpath())

        self.state = 'result wiped'

    @property
    def state(self):
        """
        Returns the most recent runner state
        """
        return self._state

    @state.setter
    def state(self,
              newstate: str) -> None:
        """
        Update the state and store within the runner history
        """

        state_time = datetime.now()

        self.insert_history(state_time, newstate)

        self._state_time = int(state_time.strftime('%s'))
        self._state = newstate

    def format_time(self, time: datetime.time) -> str:
        """
        Format the datetime object into a dict key

        Args:
            time (datetime.time):
                time object to be formatted to string

        Returns:
            (str):
                formatted time
        """
        return time.strftime(self._time_format)

    @property
    def history(self) -> dict:
        """
        State history of this runner
        """
        return self._history

    @property
    def status_list(self) -> list:
        """
        Returns a list of status updates
        """
        return list(self._history.values())

    def insert_history(self,
                       time: datetime,
                       newstate: str) -> None:
        """
        Insert a state into this runner's history

        Args:
            time (datetime.time):
                time this state change occurred
            newstate (str):
                status to update
        """
        if not isinstance(time, datetime):
            raise ValueError(f'time of type {type(time)} should be a datetime '
                             f'instance')

        base_timekey = self.format_time(time)
        idx = 0
        timekey = f'{base_timekey}/{idx}'
        while timekey in self._history:
            idx += 1

            timekey = f'{base_timekey}/{idx}'
            self._logger.info(f'timekey updated to {timekey}')

        self._logger.info(f'updating runner {self.short_uuid} state -> '
                          f'{newstate}')
        self._history[timekey] = newstate

    @property
    def last_updated(self):
        """
        Time that this runner state last changed
        """
        return self._state_time

    def run(self,
            dry_run: bool = False,
            **kwargs):
        """
        Perform a manual run

        .. warning::
            This method should be used sparingly, as it creates a Datset
            object within the function from the Database. This is a costly
            process and potentially unstable.

        Args:
            dry_run (bool):
                create files, but do not run
        """

        parent = self.unserialise(self.database.find(self._parent_uuid))

        self._run_options.update(kwargs)
        write_success = self._write_runfile(parent.function,
                                            parent.serialiser,
                                            **self._run_options)
        if not write_success:
            return

        parent.transport.queue_for_push(self.runfile,
                                        self.local_dir,
                                        self.remote_dir)

        script = parent._script_sub(**self.run_args)

        self._write_script(parent.url.python,
                           script)

        parent.transport.queue_for_push(self.scriptfile,
                                        self.local_dir,
                                        self.remote_dir)

        cmd = f'cd {self.remote_dir} && {parent.submitter} {self.scriptfile}'

        if not dry_run:
            parent.transport.transfer()
            parent.url.cmd(cmd, asynchronous=False)
            self.state = 'submitted'
        else:
            parent.transport.wipe_transfers()
            print(cmd)

    def _assess_run(self):
        self._logger.info(f'assessing run for runner {self.short_uuid}')
        self._logger.info('run args:')
        self._logger.info(format_iterable(self.run_args))

        if self.run_option('force', False):
            self._logger.info('force=True, running')
            return True

        if self.state == 'submitted':
            self._logger.info('skipping already submitted run')
            print('already submitted, skipping')
            return False

        # old skip test unpacks a runner from the database
        if self.is_finished and not self.run_option('skip', True):
            self._logger.info('skipping already completed run')
            print('run already completed, skipping')
            return False

        self._logger.info('allowing run')
        return True

    def _write_runfile(self,
                       function,
                       serialiser,
                       write_file: bool = True,
                       **kwargs) -> str:
        """
        Writes the python file which actually runs the function

        Args:
            function (Function):
                stored function object
            serialiser (Serialiser):
                stored serialiser object
            **kwargs:
                run arguments
        """
        self._run_options.update(kwargs)
        allow = self._assess_run()

        if not allow:
            return None

        self._logger.info(f'pre-running function {self.uuid}')

        self.update_run_options(kwargs)

        runscript = [serialiser.importstring,
                    function.dump_to_string(self.args)] + \
                    ['\t' + line for line in
                    serialiser.dumpstring(self.resultfile)]

        if self._dependency_info.get('child', False):
            runscript.insert(1, self._dependency_info["parent_import"])
        if self._dependency_info.get('parent', False):
            runscript.append(self._dependency_info['child_submit'] + '\n')

        output = '\n'.join(runscript)
        if write_file:
            if not os.path.isdir(self.local_dir):
                self._logger.info(f'creating local dir {self.local_dir}')
                os.makedirs(self.local_dir)
            with open(self.runpath(local=True), 'w+') as o:
                o.write(output)

        return output

    def _write_script(self,
                      python: str,
                      script: str,
                      write_file: bool = True) -> str:
        """
        Writes the jobscript for this runner

        Args:
            python (str):
                python command to launch runfile
            script (str):
                script header
        """
        tmp = []
        if isinstance(script, str):
            tmp.append(script)
        else:
            tmp.append(script(**self.run_args))

        if self.run_dir and self.run_dir != self.remote_dir:
            cmd = f'mkdir -p {self.run_dir} && ' \
                  f'cd {self.run_dir} && ' \
                  f'{python} ../{self.runfile}'
        else:
            cmd = f'{python} {self.runfile}'  # run file

        tmp.append(cmd)

        path = self.scriptpath(local=True)
        output = '\n'.join(tmp)
        if write_file:
            self._logger.info(f'writing run script to {path}')
            with open(path, 'w+') as o:
                o.write(output)

        return output

    @property
    def is_finished(self):
        """
        Attempts to determine if this runner has completed its run

        Returns (bool):
            completion status
        """
        self._logger.info(f'checking finished state of runner '
                          f'{self.short_uuid}')
        return hasattr(self, '_result')

    def update_run_options(self,
                           run_args: dict) -> None:
        """
        Update run args with dict `run_args`
        Args:
            run_args (dict):
                new run arguments

        Returns:
            None
        """
        self._logger.info('updating run options with new run args:')
        self._logger.info(format_iterable(run_args))

        self._run_options.update(run_args)

    def run_option(self,
                   option: str,
                   default=None):
        """
        Return a run option

        Args:
            option (str):
                key to search for
            default:
                default argument to provide to get

        Returns:
            option if available, else None
        """
        ret = self._run_options.get(option, default)
        self._logger.debug(f'getting run option {option}: {ret}')
        return ret

    @property
    def run_args(self):
        """
        Display the run arguments

        Returns:
            (dict) run_args
        """
        return self._run_options
