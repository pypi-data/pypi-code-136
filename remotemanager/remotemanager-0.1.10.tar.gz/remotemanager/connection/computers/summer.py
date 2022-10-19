from remotemanager.connection.url import URL
from remotemanager.connection.computers.options import required, optional
from remotemanager.utils import safe_divide


class Summer(URL):
    """
    subclassed URL specialising in connecting to the CEA Summer HPC
    """

    def __init__(self, **kwargs):

        if kwargs.get('host', None) is not None:
            raise ValueError('cannot change host of dedicated URL')

        kwargs['host'] = 'summer.intra.cea.fr'
        # count of np attribute of pbsnodes
        self._nodes = {8: 60,
                       12: 16,
                       16: 76,
                       32: 52,
                       40: 44}

        super().__init__(**kwargs)

        self.submitter = 'qsub'
        self.shebang = '#!/bin/bash'
        self.pragma = '#PBS'

        self._options = {'mpi': required,
                         'omp': required,
                         'nodes': required,
                         'jobname': 'remote-run',
                         'queue': required,
                         'walltime': required,
                         'outfile': optional,
                         'errfile': optional}

        self.modules = ['python3']
        self.extra = None

    @property
    def ssh(self):
        """
        Returns (str):
            modified ssh string for Summer avoiding perl error
        """
        return 'LANG=C ' + super().ssh

    @property
    def required(self):
        """
        Returns the required arguments
        """
        return [k for k, v in self._options.items() if v == required]

    @property
    def arguments(self):
        return list(self._options.keys())

    def parse_resources(self, **kwargs):
        """
        Set any user given arguments, using defaults where not available

        Args:
            **kwargs:
                arguments for script generation

        Returns:
            None
        """
        for argument in self.arguments:
            val = kwargs.get(argument, None)

            if val is None:
                val = self._options.get(argument)

            # only set if val has a value, or is a non-required placeholder
            if val != required:
                self.__setattr__(argument, val)
                self._logger.info(f'set arg {argument}: {val}')

    def resources_block(self, **kwargs):
        self.parse_resources(**kwargs)

        outfile = self.outfile or f'{self.jobname}-stdout'
        errfile = self.errfile or f'{self.jobname}-stderr'

        options = {'-N': self.jobname,
                   '-q': self.queue,
                   '-o': outfile,
                   '-e': errfile,
                   '-l': f'nodes={self.nodes}:'
                         f'ppn={self.mpi},'
                         f'walltime={self.walltime}'}

        return [f'{self.pragma} {k} {v}' for k, v in options.items()]

    def modules_block(self):
        return [''] + [f'module load {m}' for m in self.modules]

    def script(self,
               **kwargs) -> str:
        """
        Takes job arguments and produces a valid jobscript

        Returns:
            (str):
                script
        """
        script = [self.shebang]

        script += self.resources_block(**kwargs)
        script += self.modules_block()

        postscript = f"""
cd $PBS_O_WORKDIR
export OMP_NUM_THREADS={self.omp}
"""

        script.append(postscript)

        if self.extra is not None:
            script.append(self.extra)

        return '\n'.join(script)
