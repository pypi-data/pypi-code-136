#===============================================================================
# tempfifo.py
#===============================================================================

# Imports ======================================================================

import os
import tempfile




# Classes ======================================================================

class NamedTemporaryFIFO():
    """Create and return a temporary named pipe. The name of the pipe is
    accessible as the returned object's 'name' attribute. Can be used as a
    context manager. For example:
    
        with NamedTemporaryFIFO() as pipe:
            print(pipe.name)
    
    Upon exiting the context, the named pipe is removed unless the 'delete'
    parameter is set to False.

    Parameters
    ----------
    suffix : str or bytes
        as for tempfile.mkstemp
    prefix : sty or bytes
        as for tempfile.mkstemp
    dir : str or bytesq
        as for tempfile.mkstemp
    delete : bool
        whether the named pipe is deleted on exiting context (default True)
    open_read_end : bool
        whether the read end should be opened
    open_write_end : bool
        whetherthe write end should be opened

    Attributes
    ----------
    name : str
        filename of the temporary named pipe
    delete : bool
        whether the named pipe is deleted on exiting context (default True)
    read_end
        if open_read_end is True, the file descriptor of the read end of the
        pipe. Otherwise, None
    write_end
        if open_write_end is True, the file descriptor of the write end of the
        pipe. Otherwise, None
    """

    def __init__(self, suffix=None, prefix=None, dir=None, delete: bool = True,
        open_read_end: bool = False, open_write_end: bool = False):
        with tempfile.NamedTemporaryFile(
            suffix=suffix, prefix=prefix, dir=dir
        ) as t:
            self.name = t.name
        self.delete = delete
        os.mkfifo(self.name)
        if open_read_end:
            self.read_end = os.open(self.name, os.O_RDONLY | os.O_NONBLOCK)
        else:
            self.read_end = None
        if open_write_end:
            self.write_end = os.open(self.name, os.O_WRONLY)
        else:
            self.write_end = None
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.read_end is not None:
            self.close_read_end()
        if self.write_end is not None:
            self.close_write_end()
        if self.delete:
            os.unlink(self.name)

        return False

    def close_read_end(self):
        """Close the file descriptor representing the pipe's read end
        """
        
        os.close(self.read_end)
        self.read_end = None
    
    def close_write_end(self):
        """Close the file descriptor representing the pipe's write end
        """

        os.close(self.write_end)
        self.write_end = None
    
    def close(self):
        """Close the file descriptors representing both ends of the pipe
        """

        self.close_read_end()
        self.close_write_end()
