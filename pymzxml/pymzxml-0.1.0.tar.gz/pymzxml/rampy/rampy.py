"""Python wrapper for RAMP.

Provides access to the high performance mzXML parsing C library RAMP
via Python.

This module is based on code from the Trans Proteomics Pipeline
(https://sf.net/projects/sashimi)
"""

import ctypes
import os
import sysconfig
from pathlib import Path

import numpy as np

off_t = ctypes.c_long
SCAN_TYPE_LENGTH = 32
INSTRUMENT_LENGTH = 2000
CHARGEARRAY_LENGTH = 128
FILTER_LENGTH = 500

# Do some magic to figure out name and location of ramp library and
# load it
thisfolder = Path(__file__).parent.absolute()
suffix = sysconfig.get_config_var("EXT_SUFFIX")
ramp = ctypes.CDLL(thisfolder.joinpath("ramp" + suffix))


def pairwise(iterable):
    """Returns peak list as m/z - intensity pairs.
    s -> (s0,s1), (s2,s3), ..."""
    item = iter(iterable)
    return zip(item, item)


class SCANHEADERSTRUCT(ctypes.Structure):
    """Python implementation of the RAMP ScanHeaderStruct."""

    _fields_ = [
        ("seqNum", ctypes.c_int),
        ("acquisitionNum", ctypes.c_int),
        ("msLevel", ctypes.c_int),
        ("peaksCount", ctypes.c_int),
        ("totIonCurrent", ctypes.c_double),
        ("retentionTime", ctypes.c_double),
        ("basePeakMz", ctypes.c_double),
        ("basePeakIntensity", ctypes.c_double),
        ("collisionEnergy", ctypes.c_double),
        ("compensationVoltage", ctypes.c_double),
        ("ionisationEnergy", ctypes.c_double),
        ("lowMz", ctypes.c_double),
        ("highMz", ctypes.c_double),
        ("precursorScanNum", ctypes.c_int),
        ("precursorMz", ctypes.c_double),
        ("precursorCharge", ctypes.c_int),
        ("precursorIntensity", ctypes.c_double),
        ("scanType", ctypes.c_char * SCAN_TYPE_LENGTH),
        ("activationMethod", ctypes.c_char * SCAN_TYPE_LENGTH),
        ("possibleCharges", ctypes.c_char * SCAN_TYPE_LENGTH),
        ("numPossibleCharges", ctypes.c_int),
        ("possibleChargesArray", ctypes.c_bool * CHARGEARRAY_LENGTH),
        ("mergedScan", ctypes.c_int),
        ("mergedResultScanNum", ctypes.c_int),
        ("mergedResultStartScanNum", ctypes.c_int),
        ("mergedResultEndScanNum", ctypes.c_int),
        ("filterLine", ctypes.c_char * FILTER_LENGTH),
        ("filePosition", ctypes.c_long),
    ]  # Converted to offset in file from actual RAMPFILE


class RUNHEADERSTRUCT(ctypes.Structure):
    """Python implementation of the RAMP RunHeaderStruct."""

    _fields_ = [
        ("scanCount", ctypes.c_int),
        ("lowMz", ctypes.c_double),
        ("highMz", ctypes.c_double),
        ("startMz", ctypes.c_double),
        ("endMz", ctypes.c_double),
        ("dStartTime", ctypes.c_double),
        ("dEndTime", ctypes.c_double),
    ]


class INSTRUMENTSTRUCT(ctypes.Structure):
    """Python implementation of the RAMP InstrumentStruct."""

    _fields_ = [
        ("manufacturer", ctypes.c_char * INSTRUMENT_LENGTH),
        ("model", ctypes.c_char * INSTRUMENT_LENGTH),
        ("ionisation", ctypes.c_char * INSTRUMENT_LENGTH),
        ("analyzer", ctypes.c_char * INSTRUMENT_LENGTH),
        ("detector", ctypes.c_char * INSTRUMENT_LENGTH),
    ]


class Rampy:
    """Wrapper for the RAMP C library."""

    def __init__(self, mzxml_file_name):
        """Initializations:
        - Opens mzXML file
        - Gets the offset of the index
        - Reads the scan index and store it in mzxml_idx"""
        self.mzxml_file_name = mzxml_file_name
        # Open mzXML file
        self.file_descriptor = self.open_file()
        print("File descriptor #: {}".format(self.file_descriptor))
        # Get the offset of the index
        self.index_offset = self.read_index_offset()
        if self.index_offset == -1:
            print("Problems reading index.")
            print(
                "Please re-generate one with index_mzXML {}".format(
                    mzxml_file_name
                )
            )
            exit()
        else:
            print("mzXML index offset found at: {}".format(self.index_offset))
        self.last_scan_num = (
            ctypes.c_int()
        )  # This is set by reference in read_index()
        # Read the scan index and store it in mzxml_idx
        self.mzxml_idx = self.read_index()
        print("done reading mzXML index")

    def open_file(self):
        """Opens a file returns associated file descriptor.

        RETURNS: a file descriptor

        NOTE: For compatibility with python 3 we open the file in
        python and pass a file descriptor to a wrapper for the RAMP C
        API (which will request a FILE* to it). The wrapper API
        functions have the same name as the original RAMP functions
        with Fd appended at the end. In C RAMP relies on FILE pointers
        as arguments, but these can no longer by passed back to python
        after upgrading from 2 to 3.and. For the same reason we do not
        use the C RAMP rampOpenFile API.
        """
        print("opening {}".format(self.mzxml_file_name))
        fd = os.open(self.mzxml_file_name, os.O_RDONLY)
        return fd

    def close_file(self):
        """Closes the mzXML file associated with the instance of this class.

        NOTE: This method must be called once you are done with the instance.
        """
        os.close(self.file_descriptor)

    def read_index_offset(self):
        """Calls RAMP getIndexOffset() method.

        RETURNS: The file offset (64 bits) of the index element.
        """
        ramp.getIndexOffsetFd.argtypes = [ctypes.c_int]
        ramp.getIndexOffsetFd.restype = off_t
        return ramp.getIndexOffsetFd(self.file_descriptor)

    def read_last_scan_num(self):
        """Calls RAMP getLastScan() method.

        RETURNS: The scan number for the last scan in the mzXML file.
        """
        ramp.getLastScanFd.argtypes = [ctypes.c_int]
        ramp.getLastScanFd.restype = ctypes.c_int
        return ramp.getLastScanFd(self.file_descriptor)

    def read_index(self):
        """Calls RAMP readIndex() method.

        RETURNS: An array with the offsets (64 bits) for the scan in the
        mzXML file.  last_scan_num: will contain the scan number for
        the last scan.

        NOTE: as per mzXML format specifications the scan numbering in the
        file is assumed to be sequential
        """
        # TODO: implement freeing of the index
        tot_scans = self.read_last_scan_num()
        ramp.readIndexFd.argtypes = [
            ctypes.c_int,
            off_t,
            ctypes.POINTER(ctypes.c_int),
        ]
        # We add one since the idx array is 0 based, and the scan
        # numbering is 1 based
        ramp.readIndexFd.restype = ctypes.POINTER(off_t * (tot_scans + 1))
        return ramp.readIndexFd(
            self.file_descriptor,
            self.index_offset,
            ctypes.byref(self.last_scan_num),
        )

    # TODO this is missing in TPP ramp
    #
    # def read_filter_line(self, scan_num):
    #     """Calls RAMP readFilterLine() method.

    #     RETURNS: the filter line the scan scan_num

    #     """
    #     ramp.readFilterLine.argtypes = [FILE_ptr, off_t]
    #     ramp.readFilterLine.restype = None
    #     filter_line = ctypes.create_string_buffer('', 1000)
    #     ramp.readFilterLine(self.file_pointer,self.mzxml_idx.contents[scan_num],
    #                         filter_line)
    #     return filter_line.value

    def read_ms_level(self, scan_num):
        """Calls RAMP readMsLevel() method.

        RETURNS: the MS level (1: MS; 2: MS/MS; ...) for the scan
        scan_num
        """
        ramp.readMsLevelFd.argtypes = [ctypes.c_int, off_t]
        ramp.readMsLevelFd.restype = ctypes.c_int
        return ramp.readMsLevelFd(
            self.file_descriptor, self.mzxml_idx.contents[scan_num]
        )

    def read_peaks_count(self, scan_num):
        """Calls RAMP getPeakscount() method.

        RETURNS: the number of peaks in scan scan_num
        """
        ramp.readPeaksCountFd.argtypes = [ctypes.c_int, off_t]
        ramp.readPeaksCountFd.restype = ctypes.c_int
        return ramp.readPeaksCountFd(
            self.file_descriptor, self.mzxml_idx.contents[scan_num]
        )

    def read_start_mz(self, scan_num):
        """Calls RAMP readStartMz() method.

        RETURNS: The value of startMz for scan scan_num.
                 Will return 1E6 if the value was not set in the mzXML file.
                 This is the value set by the user, not the measured one.
        """
        ramp.readStartMzFd.argtypes = [ctypes.c_int, off_t]
        ramp.readStartMzFd.restype = ctypes.c_double
        return ramp.readStartMzFd(
            self.file_descriptor, self.mzxml_idx.contents[scan_num]
        )

    def read_end_mz(self, scan_num):
        """Calls RAMP readEndMz() method.

        RETURNS: The value of endMz for scan scan_num.
                 Will return 0 if the value was not set in the mzXML file.
                 This is the value set by the user, not the measured one.
        """
        ramp.readEndMzFd.argtypes = [ctypes.c_int, off_t]
        ramp.readEndMzFd.restype = ctypes.c_double
        return ramp.readEndMzFd(
            self.file_descriptor, self.mzxml_idx.contents[scan_num]
        )

    # TODO this is missing in TPP ramp
    #
    # def read_low_mz(self, scan_num):
    #     """Calls RAMP readLowMz() method.

    #     RETURNS: The value of lowMz for scan scan_num.
    #              Will return -1 if the value was not set in the mzXML file.
    #              This is the measured value.
    #     """
    #     ramp.readLowMz.argtypes = [FILE_ptr, off_t]
    #     ramp.readLowMz.restype = ctypes.c_double
    #     return ramp.readLowMz(self.file_pointer,
    #                           self.mzxml_idx.contents[scan_num])

    # TODO this is missing in TPP ramp
    #
    # def read_high_mz(self, scan_num):
    #     """Calls RAMP readHighMz() method.

    #     RETURNS: The value of highMz for scan scan_num.
    #              Will return -1 if the value was not set in the mzXML file.
    #              This is the measured value.
    #     """
    #     ramp.readHighMz.argtypes = [FILE_ptr, off_t]
    #     ramp.readHighMz.restype = ctypes.c_double
    #     return ramp.readHighMz(self.file_pointer,
    #                            self.mzxml_idx.contents[scan_num])

    # TODO this is missing in TPP ramp
    #
    # def read_rt(self, scan_num):
    #     """Calls RAMP readRT() method.

    #     RETURNS: The value of RT for scan scan_num in seconds
    #     """
    #     ramp.readRT.argtypes = [FILE_ptr, off_t]
    #     ramp.readRT.restype = ctypes.c_char_p
    #     rt_duration =  ramp.readRT(self.file_pointer,
    #                                self.mzxml_idx.contents[scan_num])
    #     return float(rt_duration[2:-1])

    def read_run_header(self):
        """Calls RAMP readRunHeader() method.

        RETURNS: a dictionary with the run header information
        """
        ramp.readRunHeaderFd.argtypes = [
            ctypes.c_int,
            ctypes.POINTER(off_t * (self.last_scan_num.value + 1)),
            ctypes.POINTER(RUNHEADERSTRUCT),
            ctypes.c_int,
        ]
        ramp.readRunHeaderFd.restype = None
        run_header_struct = RUNHEADERSTRUCT()
        ramp.readRunHeaderFd(
            self.file_descriptor,
            self.mzxml_idx,
            ctypes.byref(run_header_struct),
            self.last_scan_num,
        )
        return self.struct2dict(run_header_struct)

    def read_ms_run(self):
        """Calls RAMP readMSRun() method.

        RETURNS: a dictionary with the MS run information
        """
        ramp.readMSRunFd.argtypes = [
            ctypes.c_int,
            ctypes.POINTER(RUNHEADERSTRUCT),
        ]
        ramp.readMSRunFd.restype = None
        run_header_struct = RUNHEADERSTRUCT()
        ramp.readMSRunFd(self.file_descriptor, ctypes.byref(run_header_struct))
        return self.struct2dict(run_header_struct)

    # TODO this is most likely leaking memory since RAMP allocates the structure
    def read_instrument_info(self):
        """Calls RAMP getInstrumentStruct() method.

        RETURNS: a dictionary with the instrument information
        """
        ramp.getInstrumentStructFd.argtypes = [ctypes.c_int]
        ramp.getInstrumentStructFd.restype = ctypes.POINTER(INSTRUMENTSTRUCT)
        # instrument_structure = INSTRUMENTSTRUCT.from_address(
        #     ramp.getInstrumentStructFd(self.file_descriptor)
        # )
        instrument_structure = ramp.getInstrumentStructFd(self.file_descriptor)
        if instrument_structure:
            instrument_dict = self.struct2dict(instrument_structure.contents)
            self.free_instrument_struct(instrument_structure)
            return instrument_dict
        return None

    def read_scan_header(self, scan_num):
        """Calls the RAMP readScanHeader() method.

        RETURNS: a dictionary with the scan header information
        """
        ramp.readHeaderFd.argtypes = [
            ctypes.c_int,
            off_t,
            ctypes.POINTER(SCANHEADERSTRUCT),
        ]
        ramp.readHeaderFd.restype = None
        scan_header_struct = SCANHEADERSTRUCT()
        ramp.readHeaderFd(
            self.file_descriptor,
            self.mzxml_idx.contents[scan_num],
            ctypes.byref(scan_header_struct),
        )
        return self.struct2dict(scan_header_struct)

    def read_peaks(self, scan_num, deep_copy=True):
        """Calls RAMP readPeaks() method.

        RETURNS: Returns a list array of (mz - intensity) tuples

        If deep_copy is False returns n array of C floats with the m/z
        - intensity pairs and the frees the peaks memory.
        """
        # TODO: Look into adjusting this function in RAMP to support double if
        # required

        # TODO: Add support for zlib compression type in RAMP
        peaks_count = self.read_peaks_count(scan_num)
        ramp.readPeaksFd.argtypes = [ctypes.c_int, off_t]
        ramp.readPeaksFd.restype = ctypes.POINTER(
            ctypes.c_double * (peaks_count * 2)
        )
        peaks_array = ramp.readPeaksFd(
            self.file_descriptor, self.mzxml_idx.contents[scan_num]
        )
        if deep_copy:
            peaks = pairwise(np.array(peaks_array.contents))
            # Conversion to numpy will also perform a deepcopy for us. We can
            # release the memory
            self.free_peaks_memory(peaks_array)
            return peaks
        else:
            return peaks_array

    @staticmethod
    def free_peaks_memory(pointer_peaks):
        """Frees the memory allocated for the peaks during a read_peaks() call.

        NOTE: This must be called once you are done with pointer_peaks
        to avoid leaks!
        """
        ramp.freePeaks.restype = None
        ramp.freePeaks(pointer_peaks)

    @staticmethod
    def free_instrument_struct(pointer_instrument_struct):
        """Frees the memory allocated for the Instrument Structure during a
        read_instrument_info() call."""

        ramp.freeInstrumentStruct.argtypes = [ctypes.POINTER(INSTRUMENTSTRUCT)]
        ramp.freeInstrumentStruct.restype = None
        ramp.freeInstrumentStruct(pointer_instrument_struct)

    def struct2dict(self, struct):
        return dict((f, getattr(struct, f)) for f, _ in struct._fields_)
