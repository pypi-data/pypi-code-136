#!/usr/bin/env python3

#***********************************************************************//
#******************  DARK HORSE NEURO MED Python API  ******************//
#***********************************************************************//

# Written by Matt Stead and Dan Crepeau
# Copyright Dark Horse Neuro Inc, 2022

# Third party imports
import numpy as np

# Local imports
from .med_file.dhnmed_file import (open_MED, read_MED, close_MED, read_session_info, get_raw_page, sort_channels_by_acq_num)

class MedSession():
    """
    Basic object for reading operations with MED sessions.
    
    The constructor opens the MED session (reads basic metadata and opens data files
    for reading).
    
    The destructor closes open files and frees allocated memory.

    Constructor Parameters
    ----------
    session_path: str
        path to MED session
    password: str (default=None)
        password for MED session
    reference_channel (default=first channel in the session, in alphanumeric ordering)
        since different channels can have different sampling frequencies,
        select a particular channel to be used when indexing by sample sample number.
    """
    
    class OpenSessionException(Exception):
        pass
        
    class ReadSessionException(Exception):
        pass
        
    class InvalidArgumentException(Exception):
        pass
    
    
    # private member __pointers is a tuple that contains 3 pointers:
    #   (globals_m11, globals_d11, session)
    __pointers = None
    
    __valid_filters = ['none', 'antialias', 'lowpass', 'highpass', 'bandpass', 'bandstop']


    def __init__(self, session_path, password=None, reference_channel=None):
    
        if password is not None and reference_channel is not None:
            self.__pointers = open_MED(session_path, password, reference_channel)
        if password is not None and reference_channel is None:
            self.__pointers = open_MED(session_path, password)
        if password is None and reference_channel is None:
            self.__pointers = open_MED(session_path)
        
        if self.__pointers is None:
            raise MedSession.OpenSessionException("Unable to open session: " + str(session_path))
            
        # read channel/session metadata
        self.session_info = read_session_info(self.__pointers)
        
        # to test that the pointers are not being corrupted
        #print(self.__pointers)
        
        # Set defaults for matrix operations
        self.__major_dimension = "channel"
        self.__relative_indexing = True
        self.__filter_type = "antialias"
        self.__detrend = False
        self.__return_records = False
        self.__padding = "none"
        
        return
        

    def read_by_time(self, start_time, end_time):
        """
        Read all active channels of a MED session, by specifying start and end times.
        
        Times are specified in microseconds UTC (uUTC), either relative to the beginning of the session,
        or in absolute epoch terms (since 1 Jan 1970).
        Positive times are considered to be absolute, and negative times are considered to be relative.
        
        Examples of relative times:
            First second of a session:
                start: 0, end: -1000000
            Second minute of a session:
                start: -60000000, end: -120000000
        
        Parameters
        ---------
        start_time: int
            start_time is inclusive.
            see note above on absolute vs. relative times
        end_time: int
            end_time is exclusive, per python conventions.

        Returns
        -------
        MedSession.data: dict
            data structure (member of class) is the output of this function.
        """
    
        if self.__pointers is None:
            raise MedSession.ReadSessionException("Unable to read session!  Session is invalid.")
        
        self.data = read_MED(self.__pointers, int(start_time), int(end_time))
        return
        
    # This will go away - just keep it for now for legacy users
    def readByIndex(self, start_idx, end_idx):
        self.read_by_index(start_idx, end_idx)
        return
        
    def read_by_index(self, start_idx, end_idx):
        """
        Read all active channels of a MED session, by specifying start and end sample numbers.
        
        Sample numbers are relative to a reference channel, which is specified by an optional
        parameter in the constructor.  If no reference channel is specified, then the default is
        the first channel (in alphanumeric channel name).  A reference channel is necessary
        because different channels can have different sampling frequencies, and the same amount
        of time is read for all channels by this function (sample numbers are converted to
        timestamps for the purposes of this function).
        
        Parameters
        ---------
        start_idx: int
            start_idx is inclusive.
        end_idx: int
            end_idx is exclusive, per python conventions.

        Returns
        -------
        MedSession.data: dict
            data structure (member of class) is the output of this function.
        """
    
        if self.__pointers is None:
            raise MedSession.ReadSessionException("Unable to read session!  Session is invalid.")

        self.data = read_MED(self.__pointers, "no_entry", "no_entry", int(start_idx), int(end_idx))
        return
        
    def close(self):
    
        close_MED(self.__pointers)
        self.__pointers = None
        return
        
    def get_matrix_by_time(self, start_time, end_time, n_out_samps):
        """
        Read all active channels of a MED session, by specifying start and end times.
        
        Times are specified in absolute uUTC (micro UTC) time, or negative times can be
        specified to refer to the beginning of the recording.  For example, reading the
        first 10 seconds of a session would look like:
        sess.get_matrix_by_time(0, -10 * 1000000, num_out_samps)
        
        This function returns a "matrix", which includes a "samples" array.  The array is a
        2-dimensional NumPy array, with the axes being channels and samples.  Such an array
        is optimized for viewer purposes.
        
        The default filter setting is 'antialias' which is applied when downsampling occurs.
        
        Parameters
        ---------
        start_time: int
            start_time is inclusive.
        end_time: int
            end_time is exclusive, per python conventions.
        n_out_samps: int
            number of output samples

        Returns
        -------
        MedSession.matrix: dict
            data structure (member of class) is the output of this function.
        """
    
        self.matrix = get_raw_page(self.__pointers, None, None, self.__major_dimension,
            start_time, end_time, n_out_samps, None, self.__relative_indexing, self.__padding,
            self.__filter_type, None, None, self.__detrend, self.__return_records)
            
        return
        
    def get_matrix_by_index(self, start_index, end_index, n_out_samps):
        """
        Read all active channels of a MED session, by specifying start and end sample indices.
        
        This function returns a "matrix", which includes a "samples" array.  The array is a
        2-dimensional NumPy array, with the axes being channels and samples.  Such an array
        is optimized for viewer purposes.
        
        The default filter setting is 'antialias' which is applied when downsampling occurs.
        
        Parameters
        ---------
        start_time: int
            start_time is inclusive.
        end_time: int
            end_time is exclusive, per python conventions.
        n_out_samps: int
            number of output samples

        Returns
        -------
        MedSession.matrix: dict
            data structure (member of class) is the output of this function.
        """
    
        self.matrix = get_raw_page(self.__pointers, start_index, end_index, self.__major_dimension,
            None, None, n_out_samps, None, self.__relative_indexing, self.__padding,
            self.__filter_type, None, None, self.__detrend, self.__return_records)
            
        return
        
    def sort_chans_by_acq_num(self):
        """
        Re-orders channels by acquisition_channel_number, lowest to highest.
        
        Any future reads (read_by_time, read_by_index, get_raw_page) will use this new ordering for
        the channel array.  In addition, the session_info structure of the MedSession is also
        updated with this new ordering.
        
        Returns
        -------
        None
        """
    
        sort_channels_by_acq_num(self.__pointers);
        
        # read channel/session metadata
        self.session_info = read_session_info(self.__pointers)
        
        return
        
    def set_filter(self, filter_type):
        """
        Sets the filter to be used by the "matrix" operations.
        
        This filtering does not affect "read" operations, including read_by_index and read_by_time.
        Filtering is done during get_matrix_by_index and get_matrix_by_time.
        
        The default filter setting is 'antialias', which is the minimum filtering that should be
        used when downsampling data.  In antialias mode, the antialias filter is only applied
        when downsampling occurs.
        
        Parameters
        ---------
        filter_type: str
            'none', 'antialias' are accepted values.
        
        Returns
        -------
        None
        """
        
        if not isinstance(filter_type, str):
            raise MedSession.InvalidArgumentException("Argument must be one of these strings: 'none', 'antialias'")
            
        filter_type_lower = filter_type.casefold()
        
        if filter_type_lower in self.__valid_filters:
            if filter_type_lower == 'none':
                self.__filter_type = 'none';
            elif filter_type_lower == 'antialias':
                self.__filter_type = 'antialias';
            else:
                pass
        else:
            raise MedSession.InvalidArgumentException("Argument must be one of these strings: 'none', 'antialias'")
    
        return
        
        
    def __del__(self):
    
        if self.__pointers is not None:
            self.close()
        return
    
