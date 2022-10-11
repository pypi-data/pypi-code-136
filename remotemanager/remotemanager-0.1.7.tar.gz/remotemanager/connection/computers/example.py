from remotemanager.connection.url import URL
from remotemanager.utils import safe_divide


class Example_Computer(URL):
    """
    example class for connecting to a remote computer
    """

    def __init__(self, **kwargs):

        if kwargs.get('host', None) is not None:
            raise ValueError('cannot change host of dedicated URL')

        kwargs['host'] = 'remote.address.for.connection'

        super().__init__(**kwargs)

        self.submitter = 'submit_command'
        self.pragma = '#PBS'

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
               shebang: str = '/bin/bash',
               outfile: str = None,
               errfile: str = None,
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
"""

        script.append(postscript)
        if extra_lines is not None:
            script.append(extra_lines)

        return '\n'.join(script)
