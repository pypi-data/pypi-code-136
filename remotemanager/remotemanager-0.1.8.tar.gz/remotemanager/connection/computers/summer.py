from remotemanager.connection.url import URL
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
        self.pragma = '#PBS'

        self.sourcepath = '/W/$USER/build/bigdft/bigdftvars.sh'

    @property
    def ssh(self):
        """
        Returns (str):
            modified ssh string for Summer avoiding perl error
        """
        return 'LANG=C ' + super().ssh

    def script(self,
               mpi: int,
               omp: int,
               nodes: int,
               name: str,
               queue: str,
               walltime: str,
               shebang: str = '#!/bin/bash',
               outfile: str = None,
               errfile: str = None,
               sourcepath: str = None,
               extra_lines: str = None,
               **kwargs) -> str:
        """
        Takes job arguments and produces a valid Summer jobscript

        Args:
            mpi (int):
                mpi for this job (NCPUs per machine)
            omp (int):
                omp for this job (Threads per task)
            nodes (int):
                number of nodes for this job (NMachines)
            name (str):
                job name for scheduler
            queue (str):
                queue for this job
            walltime (str):
                walltime in HH:MM:SS format
            shebang (str):
                script shebang
                defaults to 'bin/bash'
            outfile (str):
                file to place any scheduler stdout
                defaults to {name}-stdout
            errfile (str):
                file to place any scheduler stderr
                defaults to {name}-stderr
            sourcepath (str):
                path to executable
            extra_lines (str):
                any extra script lines to add
            kwargs:
                required to catch any extra arguments which may not be meant
                for the script

        Returns:
            (str):
                script
        """
        script = [shebang]

        outfile = outfile or f'{name}-stdout'
        errfile = errfile or f'{name}-stderr'
        sourcepath = sourcepath or self.sourcepath

        options = {'-N': name,
                   '-q': queue,
                   '-o': outfile,
                   '-e': errfile,
                   '-l': f'nodes={nodes}:'
                         f'ppn={mpi},'
                         f'walltime={walltime}'}

        modules = ['icc',
                   'impi',
                   'mkl/18',
                   'python/anaconda3']

        for flag, value in options.items():
            script.append(f'{self.pragma} {flag} {value}')

        script.append('')
        for module in modules:
            script.append(f'module load {module}')

        postscript = f"""
cd $PBS_O_WORKDIR
export OMP_NUM_THREADS={omp}

source {sourcepath}
export BIGDFT_MPIRUN='mpirun'
export FUTILE_PROFILING_DEPTH=0
"""

        script.append(postscript)
        if extra_lines is not None:
            script.append(extra_lines)

        return '\n'.join(script)
