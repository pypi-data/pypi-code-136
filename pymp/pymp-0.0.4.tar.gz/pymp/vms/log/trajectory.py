# -*- coding: utf-8 -*-
"""
Copyright (c) 2015 Michael J Tallhamer

Varian Trajectory Log Definitions
Field definitions for Varian trajectory logs as layed out in the "TrueBeam 2.7MR2 Trajectory Log File Specification"
found on the myvarian site (https://varian.force.com/)

@author: Michael J Tallhamer M.Sc DABR (mike.tallhamer@pm.me)
"""

__version__ = 4.0
__specification__ = 'VMSTrajectoryLog_2.7MR2'

# Standard python imports
import io
import os
import struct
import itertools

# Third party imports
import param
import numpy as np
import pandas as pd

# Local imports.
from .header import VMSTrajectoryLogHeader
from .definitions import TXT_PROPERTY_TYPES as TPT
from .definitions import COMPOSITE_FIELDS, SAMPLE_TYPE, TRACKING_TYPE, AXIS
from .subbeam import VMSTrajectoryLogSubbeam

class VMSTrajectoryLog(param.Parameterized):
    """
        An object representing the features of a Varian Trajectory Log file as laid out in the "TrueBeam 2.7MR2
        Trajectory Log File Specification" found on the myvarian site (https://myvarian.com/).

        Uses the binary file path provided to determine if the file is a valid Varian Trajectory Log file and locates
        (if present in the same root directory) the associated .txt file for processing.
    """


    bin_source = param.Parameter(doc="""
    The Varian Trajectory Log '*.bin' source. Can be a file path, series of bytes, or a binary file-like object. The 
    'bin_source' is updated automatically when the 'bin_file' parameter is updated however it can be assigned directly
    in instances where GUI elements are used to retreive trajectory logs directly off of the file system""",
                                 allow_None=True,
                                 default=None
                                 )

    bin_path = param.String(doc="""
    A readonly parameter that is set if a file path (str) or file like object with a 'name' attribute is passed to 
    'bin_source' for parsing. It can be used to easily identify which file is actively being used or viewed when 
    displayed in an interface or accessed from code. If a series of bytes is passed to 'bin_source' this parameter will
    remain set to 'None' as there is no way of knowing exactly how the byes were generated or from where they came""",
                            default="",
                            constant=True
                            )

    txt_source = param.Parameter(doc="""
    The Varian Trajectory Log '*.txt' source. Can be a file path, series of bytes, or a binary file-like object. The 
    'txt_source' is updated automatically when the 'txt_file' parameter is updated however it can be assigned directly
    in instances where GUI elements are used to retreive trajectory logs directly off of the file system""",
                                 allow_None=True,
                                 default=None
                                 )

    txt_path = param.String(doc="""
    A readonly parameter that is set if a file path (str) or file like object with a 'name' attribute is passed to
    'txt_source' for parsing. It can be used to easily identify which file is actively being used or viewed when
    displayed in an interface or accessed from code. If a series of bytes is passed to 'txt_source' this parameter will
    remain set to 'None' as there is no way of knowing exactly how the byes were generated or from where they came""",
                            default="",
                            constant=True
                            )

    header = param.ClassSelector(doc="""
    The VMSTrajectoryLogHeader object representing the header for the trajectory log.""",
                                 class_=VMSTrajectoryLogHeader,
                                 allow_None=True,
                                 default=None,
                                 constant=True
                                 )

    index_map = param.Dict(doc="""
        Dictionary of key (Axis Name) value (Axis Index)pairs where users can access the column index values associated with 
        the given axis name. The index represents the first sample column for the named axis.""",
                           constant=True,
                           allow_None=True,
                           default=None
                           )

    snapshots = param.Array(doc="""
    The (NumberOfSnapshots X 2*samples) numpy array representing the snapshots for all axes in the Varian Trajectory Log 
    .bin file. The 2 * samples comes from the header.samples_per_axis representing both the expected and actual values 
    per sample.""",
                            constant=True,
                            default=None
                            )

    recarray = param.Array(doc="""
    The numpy.recarray view giving you dot '.' access as well as dict type access '[]' to the axis and sample data (i.e. 
    object.recarray.MU.actual or object.recarray['MU']['actual']). The numpy dtype object reresenting the view is 
    constructed using the definitions.AXIS Enum, definitions.COMPOSITE_TYPE dict, and the definitions.SAMPLE_TYPE 
    numpy.dtype.""",
                           constant=True,
                           default=None
                           )

    dataframe = param.DataFrame(doc="""
    The pandas.DataFrame view giving you dot '.' access as well as "fancy indexing" into the trajectory log data 
    columns. The columns are not organized according to the composite column specification in the "TrueBeam 2.7MR2 
    Trajectory Log File Specification" document as the pandas.DataFrame objects (and param and panel objecs) do not 
    support composite and non-composite columns in the same frame. Therefore composite axes like MLC are represented as 
    individual columns and samples (i.e. object.dataframe.LeafA1_expected not object.dataframe.MLC.LeafA1.expected) as 
    in the recarray view and the individual axis objects. If you need this type 0f axis use those views instead""",
                                constant=True,
                                allow_None=True,
                                default=None
                                )

    subbeams = param.List(doc="A list of VMSTrajectoryLogSubbeam objects who's axes are recorded in the log file",
                          item_type=VMSTrajectoryLogSubbeam,
                          default=[],
                          constant=True
                          )

    txt_properties = param.DataFrame(doc="""
    A pandas.Dataframe generated from the associated '*.txt' file (or None). An attempt is made to convert these values 
    to python types and to store them in the DataFrame for easy review and access.""",
                                     constant=True,
                                     allow_None=True,
                                     default=None
                                     )

    crc = param.Integer(doc="The unsigned short int representing the CRC value for the Varian Trajectory Log file.",
                        constant=True,
                        allow_None=True,
                        default=None
                        )

    readonly = param.Boolean(doc="""
        Flag for reading in the snapshot array as readonly (Default = True) or to allow inplace editing of the snappshot 
        values.""",
                             default=True
                             )

    autoload = param.Boolean(doc="""
        Flag used to automatically load either the '*.txt' file when the associated '*.bin' file is assigned to the 
        'bin_source' parameter or vice versa when the '*.txt' file is assigned to the 'txt_source' parameter 
        (Default = False). If no associated file is found the autoloaded parameters for that file are left empty.""",
                             default=False
                             )

    def __init__(self, **params):
        """
            Initialization method for the parameterized VMSTrajectoryLog object.
        """
        super(VMSTrajectoryLog, self).__init__(**params)

        # Create and set the internal __autoload__ flag on this instance (used for haulting infinate loop scenarios)
        self.__allow_autoload__ = True

        # If both a 'bin_sources' and a 'txt_source' is provided AND the user has set the 'autoload' parameter to True
        # set the 'autoload' parameter to False to avoid the possibily of incosistent states resulting from the user
        # providing inconsistent values for the 'bin_source' and 'txt_source'. This allows the user to postentialy setup
        # a situation where the 'txt_source' does not match a 'bin_source' however there is no clean way of preventing
        # this without extensive recursive checking which is rendered useless on future versions of the Varian
        # trajectory log specification which has eliminated the 'txt_source' as of version 4.
        #
        # TODO: Remove this check and all 'txt_source' code when version 3 files are no longer supported
        if (self.bin_source is not None) and (self.txt_source is not None) and self.autoload:
            self.autoload = False

        # If the bin_source was supplied at instantiation parse it
        if self.bin_source is not None:
            self._parse_bin()

        # If the txt_source was supplied at instantiation parse it
        if self.txt_source is not None:
            self._parse_txt()

    def _clear_bin_data(self):
        """
            Clears out the parameters that are populated by the '*.bin' file that makes up the Varian Trajectory Log.
        """
        # print("Clear bin data")
        with param.edit_constant(self):
            with param.discard_events(self):
                self.bin_path = ""

                self.index_map = None

                self.snapshots = None
                self.recarray = None
                self.dataframe = None

                self.subbeams = []
                self.crc = None

    def _clear_txt_data(self):
        """
            Clears out the parameters that are populated by the '*.txt' file that makes up one part of the Varian
            Trajectory Log in versions 3 and earlier.
        """
        # TODO: Remove this method when version 3 files are no longer supported.
        # print("Clear txt data")
        with param.edit_constant(self):
            with param.discard_events(self):
                self.txt_path = ""
                self.txt_properties = None


    @param.depends("bin_source", watch=True)
    def _parse_bin(self):
        """
            Parses the Varian Trajectory Log .bin file describing the delivery into the parameter values.
        """

        # If autoloading is allowed that means this methos has not been called as part of an autoload routine.
        if self.__allow_autoload__:
            # In this case we clear all data from the parameters in preparation for the new data and to keep the object
            # in a consistent state.
            self._clear_bin_data()
            self._clear_txt_data()
        else:
            # If autoloading is not allowed that means this method was called from the '_parse_txt'method as part of an
            # effort to autoload the '*.bin' file. In that case we don't want to clear the new data that was populated
            # as part of that method's activities.
            self._clear_bin_data()

        # Setup the internal _bin_buffer which will be used to read the trajectory data from
        # NOTE: This is set on the class instance so that other objects can access it rather than pass it back and forth
        #       between object methods
        self._bin_buffer = None

        # Set a local flag for later
        # Used for autoloading the txt file if the 'autoload' parameter is set
        txt = None

        # If the parameter holds a string value (i.e. a file path)
        if type(self.bin_source) == str:
            # If the file exists read it into a file object and assign it to the '_bin_buffer instance' attribute
            if os.path.exists(self.bin_source):
                with open(self.bin_source, "rb") as bin:
                    self._bin_buffer = io.BytesIO(bin.read())

                # Set the 'bin_path' parameter value
                with param.edit_constant(self):
                    self.bin_path = os.path.abspath(self.bin_source)

                # Since this is an existing path attempt to locate the associated '*.txt' file path for loading later
                txt = os.path.splitext(os.path.abspath(self.bin_source))[0] + ".txt"

                # If it doesn't exist reset the flag value to None
                if not os.path.exists(txt):
                    txt = None

            else:
                # If the file doesn't exist set the bin_source param to None effectively resetting it
                with param.discard_events(self):
                    self.bin_source = None

        # If the parameter holds a series of bytes convert it to a file like object for parsing
        elif type(self.bin_source) is bytes:
            # Convert it to a file object and assign it to the '_bin_buffer instance' attribute
            self._bin_buffer = io.BytesIO(self.bin_source)

            ### NOTE: No autoload possible because the bytes will not have a file name attribute ###

        # If it already a file like object make sure it is at the beginning before parsing
        elif self.bin_source.seekable():
            self.bin_source.seek(0) # seek tot he begining of the file

            # Assign it to the '_bin_buffer instance' attribute
            self._bin_buffer = io.BytesIO(self.bin_source.read())

            # Since this is a file like object it may have a name attribute that holds the file name of the '*.bin'
            # file. If it dose we will try to locate and potentially matching '*.txt' path for loading later
            if hasattr(self.bin_source, "name"):
                with param.edit_constant(self):
                    self.bin_path = os.path.abspath(self.bin_source.name)

                # Since this is an existing path attempt to locate the associated '*.txt' file path for loading later
                txt = os.path.splitext(os.path.abspath(self.bin_source.name))[0] + ".txt"

                # If it doesn't exist reset the flag value to None
                if not os.path.exists(txt):
                    txt = None

        # If it is none of these set the bin_source param to None effectively resetting it
        else:
            with param.discard_events(self):
                self.bin_source = None

        # Test file signature before parsing out raw bytes.
        sig, = struct.unpack('16s', self._bin_buffer.read(16))
        sig = sig.decode('utf-8')

        with param.edit_constant(self):
            if sig.strip('\x00') == u'VOSTL':
                # reset the file buffer to the '0' position
                self._bin_buffer.seek(0)

                # Only set 'filename_bin' if valid trajectory log
                # self.bin_filename = self._bin_buffer.name if hasattr(self._bin_buffer, 'name') else None

                # Build the VMSTrajectoryLogHeader passing 'self' as the vms_log object.
                self.header = VMSTrajectoryLogHeader()
                with param.edit_constant(self.header):
                    self.header.log_file = self

                # Build the VMSTrajectoryLogSubbeams passing 'self' as the vms_log object.
                for i in range(self.header.num_subbeams):
                    subbeam = VMSTrajectoryLogSubbeam()

                    with param.edit_constant(subbeam):
                        subbeam.log_file = self
                        # Set the parameterized object's name to the beam name
                        subbeam.name = f"Subbeam ({subbeam.header.beam_name})"

                    self.subbeams.append(subbeam)

                # Samples Per Snapshot (SPS) - Total samples for all axes
                SPS = 2 * np.sum(self.header.samples_per_axis)

                # Total Samples (TS)
                TS = SPS * self.header.num_snapshots

                # Read in all samples as a single 1D numpy.array
                #
                # NOTE: The ".copy('A')" at the end of the np.frombuffer method below keeps the snapshots from
                #       being readonly
                if self.readonly:
                    self.snapshots = np.frombuffer(self._bin_buffer.read(TS * 4), dtype='f4')
                else:
                    self.snapshots = np.frombuffer(self._bin_buffer.read(TS * 4), dtype='f4').copy('A')

                # Reshape the array of values to (NumberOfSnapshots X SPS)
                self.snapshots = self.snapshots.reshape(self.header.num_snapshots,
                                                        SPS)

                # Set the recarray view of the snapshots.
                self._set_recarray_view()

                # Generate pandas.DataFrame
                self._set_dataframe_view(self)

                # Assign correct beam axes to subbeams
                self._compile_subbeams()

                # Read in the CRC value
                self.crc, = struct.unpack('H', self._bin_buffer.read(2))

                # Close and clear out the file/buffer. Saves memory and allows other process to access file after
                # all the data is loaded into the VMSTrajectoryLog object.
                self._bin_buffer.close()
                self._bin_buffer = None

                with param.discard_events(self):
                    self.bin_source = None

            # If FILE_SIGNAUTRE not 'VOSTL' raise exception.
            else:
                raise ValueError('Unrecognized signature for trajectory log.')


        # Used only if autoloading is set

        # If we want to autoload an available '*.txt' file
        if self.autoload:
            # If we have the available information about hte '*.txt' file (i.e. txt is not None)
            if txt is not None:
                # Check to see if method should trigger another autoload call (i.e. to _parse_txt)
                if self.__allow_autoload__:
                    # print("Was not called from autoload")
                    # If so set the flag to false so we know not to recall autoload again from _parse_txt
                    self.__allow_autoload__ = False

                    # Set the txt_source param which will trigger the '_parse_txt' method
                    self.txt_source = txt
                else:
                    # print("Was called from autoload")
                    # If this method was call as part of an autoload you are done so reset the __autoload__ flag
                    self.__allow_autoload__ = True

        # print("Final __autoload__ value:", self.__allow_autoload__)

    @param.depends("txt_source", watch=True)
    def _parse_txt(self):
        """
            Parses a Varian Trajectory Log .txt file for additionl properties of the delivery characterized by the
            trajectory log .bin file.
        """
        # If autoloading is allowed that means this methos has not been called as part of an autoload routine.
        if self.__allow_autoload__:
            # In this case we clear all data from the parameters in preparation for the new data and to keep the object
            # in a consistent state.
            self._clear_bin_data()
            self._clear_txt_data()
        else:
            # If autoloading is not allowed that means this method was called from the '_parse_bin'method as part of an
            # effort to autoload the '*.txt' file. In that case we don't want to clear the new data that was populated
            # as part of that method's activities.
            self._clear_txt_data()

        # Setup the local txt_buffer object.
        # NOTE: Not used across objects so no need to store on instance like self._bin_buffer
        txt_buffer = None

        #  Set a flags for later
        # Used for autoloading the bin file
        bin = None

        # If the parameter holds a string value (i.e. file path)
        if type(self.txt_source) == str:
            # If the file exists read it in to a file object
            if os.path.exists(self.txt_source):
                with open(self.txt_source, "rb") as txt:
                    txt_buffer = io.BytesIO(txt.read())

                with param.edit_constant(self):
                    self.txt_path = os.path.abspath(self.txt_source)

                    # Since this is an existing path attempt to locate the associated '*.bin' file path for loading later
                    bin = os.path.splitext(os.path.abspath(self.txt_source))[0] + ".bin"

                    # If it doesn't exist reset the flag value to None
                    if not os.path.exists(bin):
                        bin = None

            # If the file doesn't exist set the set the txt_source param to None effectively resetting it
            else:
                with param.discard_events(self):
                    self.txt_source = None

        # If the parameter holds a series of bytes convert it to a file like object for parsing
        elif type(self.txt_source) is bytes:
            txt_buffer = io.BytesIO(self.txt_source)

        # If it already a file like objdect make sure it is at the beginning before parsing
        elif self.txt_source.seekable():
            self.txt_source.seek(0)
            txt_buffer = io.BytesIO(self.txt_source.read())

            # Since this is a file like object it may have a name attribute that holds the file name of the '*.txt'
            # file so we will try to save the potentially matching '*.bin' path for loading later
            if hasattr(self.txt_source, "name"):
                with param.edit_constant(self):
                    self.txt_path = os.path.abspath(self.txt_source.name)

                # Since this is an existing path attempt to locate the associated '*.bin' file path for loading later
                bin = os.path.splitext(os.path.abspath(self.txt_source.name))[0] + ".bin"

                # If it doesn't exist reset the flag value to None
                if not os.path.exists(bin):
                    bin = None

        # If it is none of these set the txt_source param to None effectively resetting it
        else:
            with param.discard_events(self):
                self.txt_source = None

        if txt_buffer is not None:
            df = pd.DataFrame(columns=['Property', "Value"])
            for line in txt_buffer:
                line = line.decode("utf-8")
                if ':' in line.strip():
                    items = line.split(':')

                    # print(f""" "{items[0].strip()}":{items[1].strip()},""")

                    if items[0].strip():
                        # TODO: This is only for a formatting error in the current txt files for the 'Trim' property.
                        #       Remove if version 3 files are later unsupported or if the error if corrected by Varian.
                        if items[0].strip() == "Trim":
                            items = line.split()

                            # NOTE: pd.DataFrame.append returns a new object so don't forget the reasignment
                            df = df.append({"Property": f"{items[0].strip()} {items[2].strip()}",
                                            "Value": TPT[f"{items[0].strip()} {items[2].strip()}"](items[3].strip())
                                            },
                                           ignore_index=True
                                           )
                        # TODO: You should only need this part without the if/else statement.
                        else:
                            # NOTE: pd.DataFrame.append returns a new object so don't forget the reasignment
                            df = df.append({"Property":items[0].strip(),
                                            "Value":TPT[items[0].strip()](items[1].strip())
                                            },
                                           ignore_index=True
                                           )
            # Set the pd.Dataframe's index tot he property names
            # (makes for easy inspection in interactive coding sessions)
            df = df.set_index("Property")

            with param.edit_constant(self):
                self.txt_properties = df

            # Close and clear out the file/buffer. Saves memory and allows other process to access file after
            # all the data is loaded into the VMSTrajectoryLog object.
            txt_buffer.close()
            txt_buffer = None

            with param.discard_events(self):
                self.txt_source = None

        # Used only if autoloading is set

        # If we want to autoload an available '*.bin' file
        if self.autoload:
            # If we have the available information about the '*.bin' file (i.e. bin is not None)
            if bin is not None:
                # Check to see if method should trigger another autoload call (i.e. to _parse_bin)
                if self.__allow_autoload__:
                    # print("Was not called from autoload")
                    # If so set the flag to false so we know not to recall autoload again from _parse_bin
                    self.__allow_autoload__ = False

                    # Set the txt_source param which will trigger the '_parse_txt' method
                    self.bin_source = bin
                else:
                    # print("Was called from autoload")
                    # If this method was call as part of an autoload you are done so reset the __autoload__ flag
                    self.__allow_autoload__ = True

        # print("Final __autoload__ value:", self.__allow_autoload__)

    def _set_recarray_view(self):
        """
            Constructs the  numpy.recarray view of the 'snapshots' attribute that segments it naturally along its axis
            boundaries.
        """
        # TODO: Re-eval the need for this view after it being in the wild.

        # List that will be passed to numpy.dtype constructor
        dtype_list = []

        index_map = []

        for e, i in enumerate(self.header.axis_enum):
            axis_name = AXIS(i).name  # Grab the axis name

            # Set the DTYPE based on the axis.
            if i in (60, 61, 62, 63, 64):  # One of the Developer Tracking Axes
                DTYPE = TRACKING_TYPE
            else:
                DTYPE = SAMPLE_TYPE

            # Add the name and axis index to the _axis_names list (to be converted to tuple of names dict of indices).
            idx = np.sum(self.header.samples_per_axis[0:e]) * 2
            index_map.append((axis_name, idx))

            # Determine how many samples for this axis
            samples = self.header.samples_per_axis[e]

            # If there is only one sample (i.e. Expected/Actual pair)
            if samples == 1:
                dtype_list.append((axis_name, DTYPE))  # Add dtype tuple
            else:  # More than 1 sample means its a composite type
                # Compile all dtype tuples for composite dtype
                fields = [i for i in \
                          itertools.product(COMPOSITE_FIELDS[axis_name], (DTYPE,))]

                # Append composite axis field names and indexes to axis_names
                index_map.extend([(i, idx + e * 2) \
                                  for e, i in enumerate(COMPOSITE_FIELDS[axis_name])])

                dtype_list.append((axis_name, fields))  # Add composite tuple

        with param.edit_constant(self):
            # Create an axis dict for looking up column index values
            self.index_map = dict(index_map)

            # Create the numpy.dtype
            self.dtype = np.dtype(dtype_list)

            # Set the snapshots.view dtype and type.
            self.recarray = self.snapshots.view(self.dtype, np.recarray)

    def _set_dataframe_view(self, parent):
        """
            Constructs a pandas.DataFrame object view of the VMSTrajectoryLog and/or VMSTrajectoryLogSubbeam 'snapshots'
            attribute.
        """

        CNAMES = []
        for e, i in enumerate(self.header.axis_enum):
            axis_name = AXIS(i).name  # Grab the axis name

            # Set the DTYPE based on the axis.
            if i in (60, 61, 62, 63, 64):  # One of the Developer Tracking Axes
                DTYPE = TRACKING_TYPE
            else:
                DTYPE = SAMPLE_TYPE

            # Determine how many samples for this axis
            samples = self.header.samples_per_axis[e]

            # If there is only one sample (i.e. Expected/Actual pair)
            if samples == 1:
                CNAMES.extend([i for i in \
                               itertools.product((axis_name,), DTYPE.names)])
            else:  # More than 1 sample means its a composite type
                CNAMES.extend([i for i in \
                               itertools.product(COMPOSITE_FIELDS[axis_name],
                                                 DTYPE.names)])

        # Set the pandas.DataFrame column indexs to the column tuples.
        columns = pd.MultiIndex.from_tuples(CNAMES)

        # Set the index to the proper range of indices
        # TODO: Consider changing this to timestamps in (ms) using the header values
        if hasattr(parent, 'start_index'): # <== When parent is a subbeam
            idx = np.arange(parent.start_index, parent.stop_index, dtype=np.int64)
        else:# <== When parent is the main trajectory log file
            idx = np.arange(0, len(parent.snapshots), dtype=np.int64)

        df = pd.DataFrame(parent.snapshots,
                          index=idx,
                          columns=columns
                          )

        # This makes a MultiIndex which is supported in pandas but is not supported in param and panel libraries for
        # dynamic viewing. For the next line of code with compress the MultiIndex columns into a single set of columns
        # with the form 'AxisName_SampleName'
        # TODO: We can set a flag later to use the MultiIndex columns or the flat columns if desired
        # df.columns = ["_".join(col) for col in df.columns]

        with param.edit_constant(parent):
            # Construct the pandas.DataFrame object for the parent object
            parent.dataframe = df

    def _compile_subbeams(self):
        """
            Compiles snapshots, recarray view, and the dataframe view for each of the subbeams. The views do not
            duplicate the data but will allow the user to access the snapshots that correspond to each of the subbeams
            from the subbeam itself without poluting its data with snapshot and views that correspond to the other
            potential subbeams in the file.
        """

        # CONTROL POINT BASED (ONLY) BORDER SEARCH
        # Grab the first snapshot index that is >= each subbeam's 'cp' value. Each snapshot tells you at which control
        # point it is taking place so knowing where each beam starts will allow you to separate the snapshots into
        # contiguous beam chunks
        idx1 = [np.where(self.recarray.ControlPoint.actual >= \
                         beam.header.control_point)[0][0] \
                for beam in self.subbeams]

        for sub in self.subbeams:
            i = sub.header.seq_num

            with param.edit_constant(sub):
                # Set snapshots view
                # For all except the last subbeam
                if sub.header.seq_num + 1 < len(self.subbeams):
                    sub.snapshots = self.snapshots[idx1[i]:idx1[i + 1], ::]
                    sub.start_index = int(idx1[i])
                    sub.stop_index = int(idx1[i + 1])

                # the last one goes from 'cp' (or idx1[i]) through the end of the snaps
                else:
                    sub.snapshots = self.snapshots[idx1[i]::, ::]
                    sub.start_index = int(idx1[i])
                    sub.stop_index = int(len(self.snapshots))

                # Set the subbeam's dtype
                sub.dtype = self.dtype

                # Set the recarray view for the subbeam snapshots
                sub.recarray = sub.snapshots.view(sub.dtype, np.recarray)

                # Set the subbeam's uderlying '_index_map ' property value
                sub.index_map = self.index_map

            # Generate pandas.DataFrame
            self._set_dataframe_view(sub)

    
