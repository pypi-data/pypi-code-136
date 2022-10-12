from remotemanager.logging import LoggingMixin

from IPython.core.magic import (Magics, magics_class,
                                cell_magic, needs_local_scope)


@magics_class
class RCell(Magics, LoggingMixin):
    """
    Magic function that allows running an ipython cell on a remote machine
    with minimal lines of code.
    """
    @cell_magic 
    @needs_local_scope
    def execute_remotely(self, line, cell, local_ns):
        from remotemanager import Dataset
        import time

        self._logger.info(f'creating magic cell with line {line}')
        # Extract arguments from the line
        args = {}
        fargs = {}
        foundc = False
        for token in line.split():
            if token == ":":
                foundc = True
                continue
            k, v = token.split("=")
            if foundc:
                fargs[k] = local_ns[v]
            else:
                args[k] = local_ns[v]

        # Build function string
        fstr = "def f("
        if fargs:
            fstr += ", ".join(list(fargs)) + ", "
        fstr += "):\n"
        for c in cell.split("\n"):
            fstr += "  " + c + "\n"

        self._logger.info(f'generated function string {fstr}')
        # Build the runner and run
        ds = Dataset(function=fstr, **args)
        ds.append_run(args=fargs)
        ds.run()

        for cmd in ds.run_cmds:
            if cmd.stderr:
                raise RuntimeError(f'error detected in magic run: '
                                   f'{cmd.stderr}')
        while not ds.all_finished:
            time.sleep(1)
        ds.fetch_results()
