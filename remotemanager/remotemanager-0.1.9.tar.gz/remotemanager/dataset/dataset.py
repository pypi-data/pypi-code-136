import gc
import yaml
import logging
import os
import typing
import warnings
from datetime import datetime

from remotemanager.connection.url import URL
from remotemanager.storage.database import Database
from remotemanager.storage.function import Function
from remotemanager.dataset.runner import Runner
import remotemanager.transport as tp
import remotemanager.serialisation as serial
from remotemanager.storage.sendablemixin import SendableMixin
from remotemanager.utils.uuid import generate_uuid
from remotemanager.utils import ensure_list
from remotemanager.logging.utils import format_iterable
from remotemanager.dataset.dependency import Dependency
from remotemanager.logging import LoggingMixin

_logger = logging.getLogger(__name__)


class Dataset(SendableMixin, LoggingMixin):
    """
    Bulk holder for remote runs. The Dataset class handles anything regarding
    the runs as a group. Running, retrieving results, sending to remote, etc.

    Args:
        function (Callable):
            function to run
        url (URL):
            connection to remote (optional)
        transport (tp.transport.Transport):
            transport system to use, if a specific is required. Defaults to
            transport.rsync
        dbfile (str):
            filename for the database file to be associated with this dataset
        script (str):
            callscript required to run the jobs in this dataset
        submitter (str):
            command to exec any scripts with. Defaults to "bash"
        name (str):
            optional name for this dataset. Will be used for runscripts
        extra_files_send(list, str):
            extra files to send with this run
        extra_files_recv(list, str):
            extra files to retrieve with this run
        global_run_args:
            any further (unchanging) arguments to be passed to the runner(s)
    """

    # DEV NOTE: arguments must be None for computer-url override to function
    def __init__(self,
                 function: typing.Callable,
                 url: URL = None,
                 transport: tp.transport.Transport = None,
                 serialiser=None,
                 dbfile: str = None,
                 script: str = None,
                 submitter: str = None,
                 name: str = None,
                 skip: bool = None,
                 block_reinit: bool = False,
                 extra_files_send: list = None,
                 extra_files_recv: list = None,
                 parent = None,
                 dependency: str = None,
                 **global_run_args):
        self._logger.info('dataset initialised')

        self._function = Function(function)

        self._global_run_args = global_run_args

        # dataset uuid is equal to Function uuid for now
        self._name = name or 'dataset'
        self._uuid = generate_uuid(self._function.uuid + 'Dataset' + self.name)
        self._logger.info(f'shortened uuid is {self.short_uuid}')

        self._defaultfile = f'dataset-file-{self.short_uuid}.yaml'
        if dbfile is None:
            dbfile = os.path.join(os.getcwd(), self._defaultfile)

        self._dbfile = dbfile
        self._script = script or '#!/bin/bash'
        self._submitter = submitter or 'bash'
        self._scriptfile = f'run-{self.name}.sh'
        self.skip = skip or False
        self._extra_files = {'send': ensure_list(extra_files_send)
                                if extra_files_send is not None else [],
                             'recv': ensure_list(extra_files_recv)
                                if extra_files_recv is not None else []}

        self._url = None
        self._transport = None
        self._computer = False
        self._serialiser = None

        self.url = url
        self.transport = transport
        self.serialiser = serialiser

        self._dependency = None
        self.apply_dependency(parent, dependency)

        if block_reinit:  # block a reinit on dependent for now
            try:
                os.remove(self._dbfile)
                self._logger.warning(f'deleted database file {self._dbfile}')
            except FileNotFoundError:
                pass

        if os.path.isfile(self._dbfile):
            self._logger.info(f'unpacking database from {self._dbfile}')

            # create a "temporary" database from the found file
            self._database = Database(self._dbfile)
            # update it with any new values
            self.database.update(self.pack())
            # unpack from here to retrieve
            payload = self.database._storage[self.uuid]
            self.inject_payload(payload)

        else:
            self._runs = {}
            self._uuids = []
            self._results = []

        self._run_cmds = []
        # database property creates the database if it does not exist
        self.database.update(self.pack())

    def __hash__(self) -> str:
        return hash(self.uuid)

    def __getattribute__(self, item):
        """
        Redirect Dataset.attribute calls to _global_run_args if possible.
        Allows for run global_run_args to be kept seperate

        Args:
            item:
                attribute to fetch
        """
        # TODO: keep an eye on this, it's hacky and liable to break
        if item != '_global_run_args' \
                and hasattr(self, '_global_run_args') \
                and item in self._global_run_args:
            return self._global_run_args.get(item)
        return object.__getattribute__(self, item)

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        return self.uuid == other.uuid

    @classmethod
    def recreate(cls,
                 raise_if_not_found: bool = False,
                 *args,
                 **kwargs):
        """
        Attempts to extract a dataset matching the given args from the python
        garbage collection interface

        Args:
            raise_if_not_found (bool):
                raise ValueError if the Dataset was not found
            *args:
                args as passed to Dataset
            **kwargs:
                keyword args as passed to Dataset
        Returns:
            Dataset
        """

        for obj in gc.get_objects():
            if type(obj) == cls:

                tmp = cls(*args, **kwargs)
                if obj == tmp:
                    print('returning stored obj')
                    return obj

        if raise_if_not_found:
            raise ValueError('Dataset with args not found!')

        return cls(*args, **kwargs)

    @property
    def database(self):
        """
        Access to the stored database object.
        Creates a connection if none exist.

        Returns (Database):
            Database
        """
        if not hasattr(self, '_database'):
            self._database = Database(file=self._dbfile)
        return self._database

    def apply_dependency(self,
                         parent,
                         mode: str):
        """
        Create and apply a Dependency for this dataset, setting it as a
        dependent

        Args:
            parent (Dataset):
                parent dataset
            mode (string):
                Dependency mode:
                    - one2one: each runner of the parent has a single child
                    - many2one: child dataset runs a single job once all
                        parent runs have completed. Not implemented!
                    - one2many: parent dataset calls multiple children after
                        each runner
        """
        if mode is None and parent is None:
            return

        self._dependency = Dependency(parent, self, mode)
        parent.apply_dependent(self.dependency)

    def apply_dependent(self,
                        dependency):
        """
        Applies a dependency for a parent dataset

        Args:
            dependency (Dependency):
                dependency to be applied
        """
        self._logger.info(f'entering Dependency as parent')
        self._dependency = dependency

    @property
    def dependency(self):
        return self._dependency

    def pack(self, **kwargs):
        """
        Override for the SendableMixin.pack() method, ensuring the dataset is
        always below a uuid

        Args:
            **kwargs:
                Any arguments to be passed onwards to the SendableMixin.pack()

        Returns:
            None
        """
        if len(kwargs) == 0:
            self._logger.info('Dataset override pack called')
        else:
            self._logger.info('Data override pack called with kwargs')
            self._logger.info(f'{format_iterable(kwargs)}')
        return super().pack(uuid=self._uuid, **kwargs)

    def set_run_option(self, key, val):
        """
        Update a glopal run option `key` with value `val`

        Args:
            key (str):
                option to be updated
            val:
                value to set
        """
        self._global_run_args[key] = val

    def append_run(self,
                   args = None,
                   arguments = None,
                   extra_files_send: list = None,
                   extra_files_recv: list = None,
                   dependency_call: bool = False,
                   **run_args):
        """
        Serialise arguments for later runner construction

        Args:
            args (dict):
                dictionary of arguments to be unpacked
            arguments (dict):
                alias for args
            extra_files_send (list, str):
                extra files to send with this run
            extra_files_recv (list, str):
                extra files to retrieve with this run
            dependency_call (bool):
                True if called via the dependency handler
            run_args:
                any extra arguments to pass to runner
        """
        if args is None and arguments is not None:
            args = arguments

        if not dependency_call and self.dependency:
            if self.dependency.is_parent(self.uuid):
                self._logger.info('calling dependency run append method')
                self.dependency.append_runs(args=args,
                                            extra_files_send=extra_files_send,
                                            extra_files_recv=extra_files_recv,
                                            **run_args)
                return
            elif self.dependency.is_child(self.uuid):
                msg = 'cannot append runs to children!'
                self._logger.error(msg)
                raise RuntimeError(msg)

        # first grab global arguments and update them with explicit args
        run_arguments = {k: v for k, v in self._global_run_args.items()}
        run_arguments.update(run_args)

        extra_files_send = ensure_list(extra_files_send) + \
                           self._extra_files['send']

        extra_files_recv = ensure_list(extra_files_recv) + \
                           self._extra_files['recv']

        tmp = Runner(arguments=args,
                     dbfile=self.dbfile,
                     parent_uuid=self.uuid,
                     extra_files_send=extra_files_send,
                     extra_files_recv=extra_files_recv,
                     **run_arguments)

        tmp.result_extension = self.serialiser.extension

        if tmp.uuid not in self._uuids:
            self._logger.debug(f'appending new run with uuid {tmp.uuid}')
            self._runs[f'runner {len(self.runners)}'] = tmp
            self._uuids.append(tmp.uuid)
        else:
            self._logger.debug(f'runner with uuid {tmp.uuid} already exists')

        self.database.update(self.pack())

    @property
    def runner_dict(self):
        """
        Stored runners in dict form, where the keys are the append id
        """
        return self._runs

    @property
    def runners(self):
        """
        Stored runners as a list
        """
        return list(self.runner_dict.values())

    @property
    def runner_list(self):
        """
        Stored runners as a list

        .. deprecated:: 1.5
            use Dataset.runners instead
        """
        warnings.warn('\nDataset.runners is soon to be deprecated, '
                      'replaced by Dataset.runners. If you require the '
                      'dict, use the Dataset.runner_dict property')
        return self.runners

    @property
    def function(self):
        """
        Currently stored Function wrapper
        """
        return self._function

    @property
    def global_run_args(self):
        """
        Global run args to be passed to runners by default
        """
        return self._global_run_args

    def _script_sub(self,
                **sub_args):
        """
        Substitutes run argmuents into the computer script, if it exists

        Args:
            **sub_args:
                jobscript arguments

        Returns:
            (str):
            jobscript
        """
        if not self._computer:
            return self._script
        if 'name' not in sub_args:
            sub_args['name'] = self.name
        return self.url.script(**sub_args)

    @property
    def script(self,
               **sub_args):
        """
        Currently stored run script

        Args:
            sub_args:
                arguments to substitute into the script() method
        """
        sub_args.update(self.global_run_args)
        return self._script_sub(**sub_args)

    @script.setter
    def script(self, script: str) -> None:
        """
        Set the run script
        """
        self._script = script

    @property
    def submitter(self):
        """
        Currently stored submission command
        """
        return self._submitter

    @submitter.setter
    def submitter(self, submitter):
        """
        Set the submission command
        """
        self._submitter = submitter

    @property
    def url(self) -> URL:
        """
        Currently stored URL object
        """
        if not hasattr(self, '_url'):
            self.url = None
        return self._url

    @url.setter
    def url(self, url=None):
        """
        Verifies and sets the URL to be used.
        Will create an empty (local) url connection if url is None

        Args:
            url (URL):
                url to be verified
        """
        self._logger.info(f'new url is being set to {url}')
        if url is None:
            self._logger.warning('no URL specified for this dataset, creating '
                                 'localhost')
            self._url = URL()
        else:
            self._url = url

        if not type(url) == URL and issubclass(type(url), URL):
            try:
                self.submitter = url.submitter
            except AttributeError:
                pass
            self._computer = True

        timeout = self._global_run_args.get('timeout', None)
        max_timeouts = self._global_run_args.get('max_timeouts', None)

        self._url.timeout = timeout
        self._url.max_timeouts = max_timeouts

    @property
    def transport(self):
        """
        Currently stored Transport system
        """
        if not hasattr(self, '_transport'):
            self.transport = None
        return self._transport

    @transport.setter
    def transport(self, transport=None):
        """
        Verifies and sets the Transport to be used.
        Will use rsync if transport is None

        Args:
            transport (Transport):
                transport to be verified
        """
        if transport is None:
            self._logger.warning('no transport specified for this dataset, '
                                 'creating basic rsync')
            self._transport = tp.rsync(self.url)
        else:
            self._transport = transport

    @property
    def serialiser(self):
        if not hasattr(self, '_serialiser'):
            self.serialiser = None
        return self._serialiser

    @serialiser.setter
    def serialiser(self, serialiser=None):
        """
        Verifies and sets the serialiser to be used.
        Will use serialyaml if serialiser is None

        Args:
            serialiser (serialiser):
                serialiser to be verified
        """
        if serialiser is None:
            self._logger.warning('no serialiser specified,'
                                 'creating basic yaml')

            self._serialiser = serial.serialyaml()

        else:
            self._serialiser = serialiser

    @property
    def dbfile(self) -> str:
        """
        Name of the database file
        """
        return self.database.path

    @property
    def extra_files(self) -> dict:
        """
        Extra files to send and recieve
        """
        return self._extra_files

    def remove_database(self):
        """
        Deletes the database file
        """
        os.remove(self.dbfile)

    @property
    def name(self) -> str:
        """
        Name of this dataset
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """
        Sets the dataset name
        """
        if not isinstance(name, str):
            try:
                name = str(name)
            except TypeError:
                raise ValueError('name can only be str type')

        self._name = name

    @property
    def uuid(self) -> str:
        """
        This Dataset's full uuid (64 characcter)
        """
        return self._uuid

    @property
    def short_uuid(self) -> str:
        """
        This Dataset's short format (8 character) uuid
        """
        return self._uuid[:8]

    def set_all_runner_states(self, state: str):
        """
        Update all runner states to `state`

        Args:
            (str) state:
                state to set
        """
        for runner in self.runners:
            runner.state = state

    def get_all_runner_states(self) -> list:
        """
        Check all runner states, returning a list

        Returns (list):
            states
        """
        return [r.state for r in self.runners]

    def check_all_runner_states(self, state: str) -> bool:
        """
        Check all runner states against `state`, returning True if `all`
        runners have this state

        Args:
            state (str):
                state to check for

        Returns (bool):
            all(states)
        """
        return all([r == state for r in self.get_all_runner_states()])

    def run(self,
            force: bool = False,
            dry_run: bool = False,
            **run_args):
        """
        Run the functions

        Args:
            force (bool):
                force all runs to go through, ignoring checks
            dry_run (bool):
                create files, but do not run
            run_args:
                any arguments to pass to the runners during this run.
                will override any "global" arguments set at Dataset init
        """
        if self.dependency and self.dependency.is_parent(self.uuid):
            self._logger.warning(f'dataset {self.short_uuid} is a parent, '
                                 f'skipping run')
            print('this dataset has children, you should run the last dataset '
                  'within the chain')
            return

        if self.dependency:
            self.dependency.run(force,
                                dry_run,
                                **run_args)
            return

        self._run(force,
                  dry_run,
                  **run_args)

    def _run(self,
            force: bool = False,
            dry_run: bool = False,
            **run_args):

        self._run_cmds = []
        # initial run args
        temp_args = {'force': force}
        temp_args.update(run_args)

        master_scripts = {}
        any_file_written = False
        for runner in self.runners:
            written = runner._write_runfile(self.function,
                                            self.serialiser,
                                            **temp_args)
            if not written:
                # runner skipped, move onto the next one
                continue
            any_file_written = True

            if not dry_run:
                runner.state = 'submitted'

            self._logger.info('writing script with run args:')
            self._logger.info(format_iterable(runner.run_args))
            runner._write_script(self.url.python,
                                 self._script_sub(**runner.run_args))

            self.transport.queue_for_push([runner.scriptfile, runner.runfile],
                                          runner.local_dir,
                                          runner.remote_dir)

            runline = f'{self.submitter} {runner.scriptfile}'

            asynchronous = runner.run_option('asynchronous', True)
            if asynchronous and self.submitter == 'bash':
                self._logger.debug('appending "&" for async run')
                runline += ' &'

            if runner.remote_dir not in master_scripts:
                master_scripts[runner.remote_dir] = []
            master_scripts[runner.remote_dir].append(runline)

            for file in runner.extra_files["send"]:
                self.transport.queue_for_push(os.path.split(file)[1],
                                              os.path.split(file)[0],
                                              runner.remote_dir)

        if not any_file_written:
            return

        cmds = []
        i = 0
        for remote, lines in master_scripts.items():
            scriptname = f'{i}-{self._scriptfile}'
            _scriptfile = os.path.join(runner.local_dir,
                                       scriptname)
            with open(_scriptfile, 'w+') as o:
                o.write('\n'.join(lines))
            self.transport.queue_for_push(scriptname,
                                          runner.local_dir,
                                          remote)
            cmd = f'cd {remote} && bash {scriptname}'
            cmds.append(cmd)
            i += 1

        if not dry_run:
            self.transport.transfer()
            for cmd in cmds:
                self._run_cmds.append(
                    self.url.cmd(cmd, asynchronous=asynchronous))
        else:
            self.transport.wipe_transfers()
            for cmds in cmds:
                print(cmd)

    @property
    def run_cmds(self) -> list:
        """
        Access to the storage of CMD objects used to run the scripts

        Returns:
            (list): List of CMD objects
        """
        return self._run_cmds

    def _check_for_resultfiles(self) -> dict:
        """
        Checks for the runfiles dictated by the runners
        """
        self._logger.info('checking for finished runs')
        files_to_check = []
        for runner in self.runners:
            files_to_check.append(runner.resultpath())

        return self.url.utils.file_mtime(files_to_check)

    def fetch_results(self,
                      raise_if_not_finished: bool = False) -> None:
        """
        Collect any scripted run resultfiles and insert them into their runners

        Args:
            raise_if_not_finished (bool):
                raise an error if all calculations not finished

        Returns:
            None
        """
        self._check_run_errors()

        present_runfiles = self._check_for_resultfiles()

        if not any(present_runfiles.values()):
            self._logger.info('no valid results found, exiting early')
            return

        self._logger.info('present result files:')
        self._logger.info(format_iterable(present_runfiles))
        for runner in self.runners:
            if present_runfiles[runner.resultpath()]:
                self.transport.queue_for_pull(os.path.split(
                                              runner.resultpath())[1],
                                              runner.local_dir,
                                              os.path.split(runner.resultpath())[0])

                for file in runner.extra_files['recv']:
                    rmt = runner.run_dir if runner.run_dir is not None \
                        else runner.remote_dir
                    self.transport.queue_for_pull(os.path.split(file)[1],
                                                  runner.local_dir,
                                                  rmt)

        self._logger.info('pulling completed result files')
        self.transport.transfer()
        for runner in self.runners:
            if present_runfiles[runner.resultpath()]:
                pulled = runner.resultpath(local=True)

                result = self.serialiser.load(pulled)

                timestamp = int(os.path.getmtime(pulled))

                if timestamp < runner.last_updated:
                    self._logger.warning('calculation not completed yet')
                    continue

                mtime = datetime.fromtimestamp(timestamp)
                runner.insert_history(mtime, 'resultfile created remotely')

                runner.result = result

        self.database.update(self.pack())

        if not self.all_finished and raise_if_not_finished:
            raise RuntimeError('Calculations not yet completed!')

    def _check_run_errors(self):
        errs = [c.stderr for c in self._run_cmds
                if c.stderr is not None
                and c.stderr != '']

        if len(errs) == 0:
            self._logger.info('no errors found at run')
            return

        print(f'There are {len(errs)} errors, printing:')
        for error in errs:
            self._logger.error(error)
            print(f'stderr from run call:\n{error}')

        from remotemanager import Logger
        raise RuntimeError('There was an issue during running. '
                           f'See printed info or logfile at {Logger.path}')

    @property
    def is_finished(self) -> list:
        """
        Check if the runners have finished

        Returns (list):
            boolean list corresponding to the Runner order
        """
        ret = {r.uuid: None for r in self.runners}
        if self.skip:
            self._logger.info('skip is true, checking runner first')
            for runner in self.runners:
                if runner.is_finished:
                    ret[runner.uuid] = True

        if self.script:
            self._logger.info('scripted run, checking for files')
            # look for the resultfiles
            fin = self._check_for_resultfiles()

            # create a list of the resultfiles that are available
            for runner in self.runners:
                if ret[runner.uuid] is not None:
                    continue

                resultpath = runner.resultpath()
                last_updated = runner.last_updated
                mtime = fin[resultpath]

                self._logger.debug(f'checking file {resultpath}. mtime '
                                   f'{mtime} vs runner time {last_updated}')

                if mtime is None:
                    ret[runner.uuid] = False
                elif mtime >= last_updated:
                    ret[runner.uuid] = True
                else:
                    ret[runner.uuid] = False

            return list(ret.values())

        return [r.is_finished for r in self.runners]

    @property
    def all_finished(self) -> bool:
        """
        Check if `all` runners have finished

        Returns (bool):
            True if all runners have completed their runs
        """
        return all(self.is_finished)

    @property
    def results(self) -> list:
        """
        Access the results of the runners

        Returns (list):
            runner.result for each runner
        """
        return [r.result for r in self.runners]

    def clear_results(self):
        """
        Remove any results from the stored runners and attempt to delete their
        result files.

        .. warning::
            This is a potentially destructive action, be careful with this
            method
        """
        for runner in self.runners:
            runner.clear_result()
