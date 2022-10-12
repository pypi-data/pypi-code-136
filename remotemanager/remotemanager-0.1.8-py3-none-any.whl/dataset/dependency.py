import gc

from remotemanager.storage.sendablemixin import SendableMixin


class Dependency(SendableMixin):

    _valid_modes = ['one2one']

    def __init__(self,
                 parent,
                 child,
                 mode):

        if parent == child:
            raise ValueError('parent and child are the same!')

        self._uuids = {parent.uuid: 'parent',
                       child.uuid: 'child'}
        self._parent = parent
        self._child = child

        self._mode = None
        self.mode = mode

        self._network = {}

    @property
    def child(self):
        if not hasattr(self, '_child'):
            c_uuid = [k for k, v in self._uuids.items()
                      if v == 'child'][0]
            self._child = _dataset_from_uuid(c_uuid)
        return self._child

    @property
    def parent(self):
        if not hasattr(self, '_parent'):
            p_uuid = [k for k, v in self._uuids.items()
                      if v == 'parent'][0]
            self._parent = _dataset_from_uuid(p_uuid)
        return self._parent

    def is_child(self,
                 uuid: str) -> bool:
        """
        Returns True if uuid is a child Dataset
        """
        return self._uuids[uuid] == 'child'

    def is_parent(self,
                  uuid: str) -> bool:
        """
        Returns True if uuid is a parent Dataset
        """
        return self._uuids[uuid] == 'parent'

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, mode):
        if mode not in Dependency._valid_modes:
            raise ValueError(f'mode {mode} must be one of '
                             f'{Dependency._valid_modes}')

        self._mode = mode

    def append_runs(self, *args, **kwargs):
        key = self.next_dependency_key

        # must append children first to access their scripts within the parent

        func_args = kwargs.pop('args')

        self.child.append_run(*args,
                              dependency_call=True,
                              dependency_key=key,
                              **kwargs)
        self.parent.append_run(*args,
                               arguments=func_args,
                               dependency_call=True,
                               dependency_key=key,
                               **kwargs)

        # create any dependency info
        prv_resultfile = self.parent.runners[-1].resultfile
        import_results = [f'# importing from {prv_resultfile}',
                          '\n'.join(self.parent.serialiser.loadstring(prv_resultfile))]
        self.child.runners[-1]._dependency_info['child'] = True,
        self.child.runners[-1]._dependency_info['parent_import'] = '\n'.join(import_results)

        submit_child = ['import subprocess',
                        f'cmd = "{self.parent.submitter} {self.child.runners[-1].scriptfile}"',
                        'subprocess.Popen(cmd, shell=True, executable="/bin/bash")']
        self.parent.runners[-1]._dependency_info['parent'] = True,
        self.parent.runners[-1]._dependency_info['child_submit'] = '\n'.join(submit_child)

        self.network[key] = (self.parent.runners[-1],
                             self.child.runners[-1])

    @property
    def next_dependency_key(self):
        return f'{len(self._network)+1}'.rjust(5, '0')

    @property
    def network(self):
        return self._network

    def run(self,
            force,
            dry_run,
            **run_args):
        """
        Submit the parent and child datasets.

        Arguments are the same as the Dataset.run() function
        """

        self.parent._run(force,
                         dry_run,
                         **run_args)
        self.child._run()


def _dataset_from_uuid(uuid):

    for obj in gc.get_objects():
        if obj.__class__.__name__ == 'Dataset':
            if obj.uuid == uuid:
                return obj

    raise ValueError(
        f'could not find Dataset in memory with UUID {uuid}')
