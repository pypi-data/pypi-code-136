# -*- coding: utf-8 -*-
"""
Copyright (c) 2015 Michael J Tallhamer

Varian Trajectory Log Definitions
Field definitions for Varian trajectory logs as layed out in the "TrueBeam 2.7MR2 Trajectory Log File Specification"
found on the myvarian site (https://varian.force.com/)

@author: Michael J Tallhamer M.Sc DABR (mike.tallhamer@pm.me)
"""

# Standard python imports
import struct
import io

# Third party imports
import param
import numpy as np

class MetaData(param.Parameterized):
    """
        Representation of the MetaData Structure outlined in the "TrueBeam 2.7MR2 Trajectory Log File Specification"
        for storage of the metadata. Metadata was added to the reserved section of the VMSTrajectoryLog header in the
        updated 2.7 MR2 specification.
    """
    patient_id = param.String(doc="The utf-8 string for the Patient ID as identified in the MRN from most ROISs",
                              constant=True
                              )
    plan_name = param.String(doc="""
    The utf-8 string for the plan name from which the beams are pulled for the current trajectory log.""",
                             constant=True
                             )
    sop_instance_uid = param.String(doc="""
    The utf-8 string representing the DICOM SOPInstanceUID for the plan being run on the machine.""",
                                    constant=True
                                    )
    planned_mu = param.Number(doc="The planned MU for the plan being run on the machine.",
                              constant=True
                              )
    remaining_mu = param.Number(doc="The remaining MU for the plan being run on the machine.",
                                constant=True
                                )
    energy = param.String(doc="The ASCII representation of the field energy designation.",
                          constant=True
                          )
    beam_name = param.String(doc="The name of the beam being run on the machine.",
                             constant=True
                             )

    def __init__(self, metadata, **params):
        """ Standard initialization function for MetaData object

            Parameters
            ----------
            metadata : bytes
                The series of bytes that represent the metadata pulled from the
                reserved section of the VMSTrajectoryLog header.
        """

        super(MetaData, self).__init__(**params)
        self._parse(metadata)

    def _parse(self, metadata):

        # Convert the metadata series of bytes to an io.BytesIO stream
        metadata = io.BytesIO(metadata)

        with param.edit_constant(self):
            # Grab the patient id by splitting the line on ':' and stripping all whitespace surounding the value
            # (i.e. \t and \r\n)
            _id = metadata.readline().split(b':')[-1].strip()
            self.patient_id = _id.decode('utf-8')

            # Grab the plan name by splitting the line on ':' and stripping all whitespace surounding the value
            # (i.e. \t and \r\n)
            n = metadata.readline().split(b':')[-1].strip()
            self.plan_name = n.decode('utf-8')

            # Grab the SOPInstanceUID by splitting the line on ':' and stripping all whitespace surounding the value
            # (i.e. \t and \r\n)
            uid = metadata.readline().split(b':')[-1].strip()
            self.sop_instance_uid = uid.decode('utf-8')

            # Grab the planned MUs by splitting the line on ':' and stripping all whitespace surounding the value
            # (i.e. \t and \r\n) and convert to float
            self.planned_mu = float(metadata.readline().split(b':')[-1].strip())

            # Grab the remaining MUs by splitting the line on ':' and stripping all whitespace surounding the value
            # (i.e. \t and \r\n) and convert to float
            self.remaining_mu = float(metadata.readline().split(b':')[-1].strip())

            # Grab the energy label by splitting the line on ':' and stripping all whitespace surounding the value
            # (i.e. \t and \r\n)
            e = metadata.readline().split(b':')[-1].strip()
            self.energy = e.decode('ascii')

            # Grab the beamname by splitting the line on ':' and stripping all whitespace surounding the value
            # (i.e. \t and \r\n)
            bn = metadata.readline().split(b':')[-1].strip()
            self.beam_name = bn.decode('utf-8')


class VMSTrajectoryLogHeader(param.Parameterized):
    """
        Simple object that parses out, stores, and provides 'get' access to the 'header' information for a
        VMSTrajectoryLog. The simplistic 'readonly' access provided by the properties is used to discourage setting
        these values by mistake using the simple assignment operator '=' during use. These values are used in a number
        of other parsing fuctions to determine the number of bytes to read in as well as the shape of the resulting
        numpy arrays and dtypes so changing them is not recomended.

        Currently there is no reason to write a trajectory log within the Varian framework as they are very simple
        diagnostic tools. With that in mind assignment to these attributes with the intent to write out later is not
        supported at this time.
    """
    log_file = param.Parameter(doc="The VMSTrajectoryLog object this header refers to.",
                               constant=True
                               )
    signature = param.String(doc="""
    The utf-8 string representing the file signature as described in the "TrueBeam 2.7MR2 Trajectory Log File 
    Specification." The expected value is 'VOSTL' and is used to determine if the file is of the appropriate type.""",
                             constant=True
                             )
    version = param.String(doc="The utf-8 string representing the file version.",
                           constant=True
                           )
    size = param.Integer(doc="An integer representing the size of the header in bytes.",
                         constant=True
                         )
    sample_interval = param.Integer(doc="An integer representing the time interval of the samples in (ms).",
                                    constant=True
                                    )
    num_axes = param.Integer(doc="An integer representing the number of axes reported on.",
                             constant=True
                             )
    axis_enum = param.Array(doc="""
    A numpy.array of interger values representing the enum values of the axes reported on and their order.""",
                            constant=True
                            )
    samples_per_axis = param.Array(doc="""
    A numpy.array of interger values representing the number of samples per axis in the same order as the axis_enum.""",
                                   constant=True
                                   )
    axis_scale = param.Integer(doc="""
    An integer enum value representing the scale used for the log (i.e. Machine Scale or Modified IEC 61217).""",
                               constant=True
                               )
    num_subbeams = param.Integer(doc="An integer indicating the number of subbeams in the log file.",
                                 constant=True
                                 )
    is_truncated = param.Integer(doc="A flag (integer 0 or 1) indicating if the file was truncated.",
                                 constant=True
                                 )
    num_snapshots = param.Integer(doc="An integer indicating the number of snapshots in the log file.",
                                  constant=True
                                  )
    mlc_model = param.Integer(doc="An integer enum value representing the MLC model used during delivery.",
                              constant=True
                              )
    reserved = param.Parameter(doc="The unused portion of the header",
                               constant=True
                               )
    metadata = param.ClassSelector(class_=MetaData, allow_None=True, constant=True, doc="""
    Representation of the MetaData Structure outlined in the "TrueBeam 2.7MR2 Trajectory Log File Specification" for 
    storage of the metadata added to the reserved section of the VMSTrajectoryLog header in the updated 2.7 MR2
    specification."""
                                   )

    @param.depends('log_file', watch=True)
    def _parse(self):
        # print("Parsing Log Header")

        with param.edit_constant(self):
            # File signature
            s, = struct.unpack('16s', self.log_file._bin_buffer.read(16))
            s = s.decode('utf-8')
            self.signature = s.strip('\x00')

            # File version
            v, = struct.unpack('16s', self.log_file._bin_buffer.read(16))
            v = v.decode('utf-8')
            self.version = v.strip('\x00')

            # The size of the header in bytes (shouldbe 1024)
            self.size, = struct.unpack('<i', self.log_file._bin_buffer.read(4))

            # The sample interval in ms
            self.sample_interval, = struct.unpack('<i', self.log_file._bin_buffer.read(4))

            # The number of axes reported on
            self.num_axes, = struct.unpack('<i', self.log_file._bin_buffer.read(4))

            # An array of enum values representing the axes and their order
            self.axis_enum = np.frombuffer(self.log_file._bin_buffer.read(self.num_axes * 4), dtype='i4')

            # An array representing the number of samples for each axis (in order)
            self.samples_per_axis = np.frombuffer(self.log_file._bin_buffer.read(self.num_axes * 4), dtype='i4')

            # The enum representing the scale used for the log (i.e. Machine Scale or Modified IEC 61217)
            self.axis_scale, = struct.unpack('<i', self.log_file._bin_buffer.read(4))

            # The number of subbeams recorded in the file
            self.num_subbeams, = struct.unpack('<i', self.log_file._bin_buffer.read(4))

            # Flag indicating if the file was truncated
            self.is_truncated, = struct.unpack('<i', self.log_file._bin_buffer.read(4))

            # The total number of snapshots in the trajectory log
            self.num_snapshots, = struct.unpack('<i', self.log_file._bin_buffer.read(4))

            # The enum value representing the MLC model used in delivery
            self.mlc_model, = struct.unpack('<i', self.log_file._bin_buffer.read(4))

            if float(self.version) <= 3.0:
                # The unused portion of the header
                self.reserved =  self.log_file._bin_buffer.read(self.size - (64 + (self.num_axes * 8)))
                self.metadata = None  # Only introduced in versions <= 4.0
            else:
                # The unused portion of the header
                self.reserved =  self.log_file._bin_buffer.read(self.size - (64 + (self.num_axes * 8)))

                # Set as BytesIO stream
                raw_bytes = io.BytesIO(self.reserved)

                # Strip off unused reserve space to keep metadata section only
                metadata_section = self.reserved.rstrip(b'\x00')

                # Set the storage object for the metadata in version > 4.0 files
                self.metadata = MetaData(metadata_section)

                # Set the reserved attribute of the header to what is left after the metedata section is read in.
                raw_bytes.seek(len(metadata_section))  # Seek to end of metadata
                self.reserved = raw_bytes.read()  # Read in remaining reserved space


class VMSTrajectoryLogSubbeamHeader(param.Parameterized):
    """
        Simple object that parses out, stores, and provides 'get' access to the subbeam header structure for a
        VMSTrajectoryLogSubbeam. The simplistic 'readonly' access provided by the parameters is used to discourage
        setting these values by mistake using the simple assignment operator '=' during use. These values are used in a
        number of calculation fuctions to determine the accuracy of delivery so changing them is not recomended.

        Currently there is no reason to write a trajectory log within the Varian framework as they are very simple
        diagnostic tools. With that in mind assignment to these attributes with the intent to write out later is not
        supported at this time.
    """
    subbeam = param.Parameter(doc="The VMSTrajectoryLogSubbeam object this header refers to.",
                              constant=True
                              )
    control_point = param.Integer(doc="An integer representing the control point at which the subbeam starts.",
                                  constant=True
                                  )
    monitor_units = param.Number(doc="A float representing number of monitor units planned for the subbeam.",
                                 constant=True
                                 )
    rad_time = param.Number(doc="A float representing the expected irradiation time for the subbeam in seconds.",
                            constant=True
                            )
    seq_num = param.Integer(doc="An integer representing the sequence number of the subbeam.",
                            constant=True
                            )
    beam_name = param.String(doc="The utf-8 string representing the name of the subbeam.",
                             constant=True
                             )
    reserved = param.Parameter(doc="The 32 bytes of unused preallocated space at teh end of the subbeam header.",
                               constant=True
                               )

    # --------------------------------------------------------------------------
    # 'VMSTrajectoryLogSubbeam' Private Methods
    # --------------------------------------------------------------------------
    @param.depends('subbeam', watch=True)
    def _parse(self):
        """
            Method used to parse the Varian Trajectory Log Subbeams headers into their various components.
        """
        # print("Parsing Subbeam Header")

        with param.edit_constant(self):
            # The control point where the subbeam starts
            self.control_point, = struct.unpack('<i', self.subbeam.log_file._bin_buffer.read(4))

            # The number of monitor units planned for the subbeam
            self.monitor_units, = struct.unpack('<f', self.subbeam.log_file._bin_buffer.read(4))

            # Expected irradiation time for the subbeam in seconds
            self.rad_time, = struct.unpack('<f', self.subbeam.log_file._bin_buffer.read(4))

            # Sequence number of the subbeam
            self.seq_num, = struct.unpack('<i', self.subbeam.log_file._bin_buffer.read(4))

            # Subbeam name
            n, = struct.unpack('512s', self.subbeam.log_file._bin_buffer.read(512))
            n = n.decode('utf-8')
            self.beam_name = n.strip('\x00')

            # Unused 32 bytes of the preallocated space for each subbeam
            self.reserved = self.subbeam.log_file._bin_buffer.read(32)
