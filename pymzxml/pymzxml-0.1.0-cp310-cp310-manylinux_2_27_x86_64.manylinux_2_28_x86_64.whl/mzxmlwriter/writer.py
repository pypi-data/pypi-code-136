"""Collection of classes for writing mzXML files."""

import base64
import hashlib
import re
import struct
import zlib

import pkg_resources


class MzXml:
    """MzXML class to store a full mzXML file."""

    def __init__(self, filename):
        """Initialize the MzXML class."""
        self.filename = filename
        self.file = open(filename, "w")
        self.ms_runs = []
        self.index = []
        self.index_offset = None
        self.sha1 = None

    def __str__(self):
        """Return the mzXML file as a string."""
        mzxml = self.pre_sha1_string()
        self.calculate_sha1_from_string(mzxml)
        mzxml += self.sha1
        mzxml += "</sha1>\n"
        mzxml += self.close_xml()
        return mzxml

    def save_to_file(self):
        """Save the mzXML file to disk."""
        self.file.write(str(self))
        self.file.close()

    def pre_sha1_string(self):
        """Return the string used for the SHA1 checksum.

        This string is the mzXML file up to and including the <sha1> tag
        without the SHA1 checksum.
        """
        mzxml = self.open_xml()
        for ms_run in self.ms_runs:
            mzxml += str(ms_run)
        self.calculate_index_from_string(mzxml)
        mzxml += self.index_to_xml()
        self.calculate_index_offset_from_string(mzxml)
        mzxml += self.index_offset_to_xml()
        mzxml += " <sha1>"
        return mzxml

    @staticmethod
    def open_xml():
        """Return opening XML for an mzXML file.

        Use this instead of __str__ to write to a file in serially.
        """
        return (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<mzXML xmlns="http://sashimi.sourceforge.net/schema_revision/mzXML_3.2"\n'  # noqa
            ' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n'
            ' xsi:schemaLocation="http://sashimi.sourceforge.net/schema_revision/mzXML_3.2'  # noqa
            ' http://sashimi.sourceforge.net/schema_revision/mzXML_3.2/mzXML_idx_3.2.xsd">\n'  # noqa
        )

    @staticmethod
    def close_xml():
        """Return closing XML for an mzXML file.

        Use this instead of __str__ to write file serially.
        """
        return "</mzXML>"

    def add_ms_run(self, ms_run):
        """Add an MsRun to the mzXML file.

        Each MzXml can have multiple MsRuns.
        """
        self.ms_runs.append(ms_run)

    def calculate_index_from_string(self, mzxml_string):
        """Index the file offsets of the scans in the MzXML file."""
        pattern = re.compile(r'<scan num="(\d+)"')
        self.index = [
            (m.start(), m.group(1)) for m in re.finditer(pattern, mzxml_string)
        ]

    def calculate_index_from_file(self):
        """Index the file offsets of the scans in the MzXML file.

        Use this instead of calculate_index_from_string when writing to
        a file in a serial manner.
        """
        with open(self.filename, "r") as mzxml_file:
            pattern = re.compile(r'<scan num="(\d+)"')
            self.index = [
                (m.start(), m.group(1))
                for m in re.finditer(pattern, mzxml_file.read())
            ]

    def calculate_index_offset_from_string(self, mzxml_string):
        """Calculates the offset of the index in the mzXML file."""
        self.index_offset = mzxml_string.find('<index name="scan">')

    def calculate_index_offset_from_file(self):
        """Calculate the offset of the index in the mzXML file.

        Use this instead of calculate_index_offset_from_string when
        writing to a file in a serial manner.
        """
        with open(self.filename, "r") as mzxml_file:
            self.index_offset = mzxml_file.read().find('<index name="scan">')

    def calculate_sha1_from_string(self, pre_sha1_string):
        """Calculate the SHA1 checksum for the mzXML file."""
        sha1 = hashlib.sha1(pre_sha1_string.encode("utf-8"))
        self.sha1 = sha1.hexdigest()

    def calculate_sha1_from_file(self):
        """Calculate the SHA1 checksum for the mzXML file.

        Use this instead of calculate_index_from_string when writing to
        a file in a serial manner.
        """
        with open(self.filename, "r") as mzxml_file:
            sha1 = hashlib.sha1(mzxml_file.read().encode("utf-8"))
        self.sha1 = sha1.hexdigest()

    def index_to_xml(self):
        """Return the index string for the mzXML file."""
        index_string = ' <index name="scan">\n'
        for offset, scan_num in self.index:
            index_string += '  <offset id="{0}">{1}</offset>\n'.format(
                scan_num, offset
            )
        index_string += " </index>\n"
        return index_string

    def index_offset_to_xml(self):
        """Return the index offset string for the mzXML file."""
        return " <indexOffset>{}</indexOffset>\n".format(self.index_offset)


class MsRun:
    """MsRun class to store the information of a single MS run."""

    def __init__(self, scan_count, start_time, end_time):
        """Initialize the MsRun class."""
        self.scan_count = scan_count
        self.start_time = start_time
        self.end_time = end_time
        self.parent_files = []
        self.ms_instrument = None
        self.data_processings = []
        self.scans = []

    def __str__(self):
        """Return the MsRun as a string."""
        ms_run = self.open_xml()
        for parent_file in self.parent_files:
            ms_run += str(parent_file)
        if self.ms_instrument is not None:
            ms_run += str(self.ms_instrument)
        for data_processing in self.data_processings:
            ms_run += str(data_processing)
        for scan in self.scans:
            ms_run += str(scan)
        ms_run += self.close_xml()
        return ms_run

    def open_xml(self):
        """Return opening XML for an MsRun.

        Use this instead of __str__ to write file serially.
        """
        return (' <msRun scanCount="{}" startTime="{}" endTime="{}">\n').format(
            self.scan_count, self.start_time, self.end_time
        )

    @staticmethod
    def close_xml():
        """Return closing XML for an MsRun.

        Use this instead of __str__ to write to a file in serially.
        """
        return " </msRun>\n"

    def update_scan_count(self):
        """Update the scan count of the MsRun.

        This should be called after adding scans to the MsRun.  Note
        that it is not called automatically when writing an mzXML file
        via __str__ method to allow for adding scans in series.
        """
        self.scan_count = len(self.scans)

    def add_parent_file(self, parent_file):
        """Add a parent file to the MsRun.

        Each MsRun can have multiple parent files.
        """
        self.parent_files.append(parent_file)

    def add_ms_instrument(self, ms_instrument):
        """Add an MsInstrument to the MsRun."""
        self.ms_instrument = ms_instrument

    def add_data_processing(self, data_processing):
        """Add a DataProcessing to the MsRun.

        Each MsRun can have multiple DataProcessings steps.
        """
        self.data_processings.append(data_processing)

    def add_scan(self, scan):
        """Add a Scan to the MsRun.

        Each MsRun can have multiple Scans.
        """
        self.scans.append(scan)

    def renumber_scans(self, start=1):
        """Renumber the scans in the MsRun."""
        i = start
        for scan in self.scans:
            scan.scan_num = i
            i += 1
            i = scan.renumber_scans(i)


class ParentFile:
    """ParentFile class to store the information of a parent file."""

    def __init__(self, filename):
        """Initialize the ParentFile class."""
        self.filename = filename
        self.filetype = self.get_filetype()
        self.sha1 = self.get_sha1()

    def __str__(self):
        """Return the ParentFile as a  string."""
        return (
            '  <parentFile fileName="{}" fileType="{}" fileSha1="{}"/>\n'
        ).format(self.filename, self.filetype, self.sha1)

    def get_filetype(self):
        """Check the filetype of the parent file.

        Currently only supports mzXML and RAW.
        """
        if self.filename.endswith(".mzXML"):
            return "processedData"
        if self.filename.endswith(".RAW"):
            return "RAWData"
        raise ValueError("Filetype not supported.")

    def get_sha1(self):
        """Calculate the SHA1 hash of the parent file."""
        with open(self.filename, "rb") as file:
            data = file.read()
        return hashlib.sha1(data).hexdigest()


class MsInstrument:
    """MsInstrument class to store the information of the MS instrument."""

    def __init__(
        self,
        ms_manufacturer=None,
        ms_model=None,
        ms_ionisation=None,
        ms_mass_analyzer=None,
        ms_detector=None,
    ):
        """Initialize the MsInstrument class."""
        self.ms_manufacturer = ms_manufacturer
        self.ms_model = ms_model
        self.ms_ionisation = ms_ionisation
        self.ms_mass_analyzer = ms_mass_analyzer
        self.ms_detector = ms_detector

    def __str__(self):
        """Return the MsInstrument as a string."""
        ms_instrument = "  <msInstrument>\n"
        if self.ms_manufacturer is not None:
            ms_instrument += (
                '   <msManufacturer category="msManufacturer" value="{}"/>\n'
            ).format(self.ms_manufacturer)
        if self.ms_model is not None:
            ms_instrument += (
                '   <msModel category="msModel" value="{}"/>\n'
            ).format(self.ms_model)
        if self.ms_ionisation is not None:
            ms_instrument += (
                '   <msIonisation category="msIonisation" value="{}"/>\n'
            ).format(self.ms_ionisation)
        if self.ms_mass_analyzer is not None:
            ms_instrument += (
                '   <msMassAnalyzer category="msMassAnalyzer" value="{}"/>\n'
            ).format(self.ms_mass_analyzer)
        if self.ms_detector is not None:
            ms_instrument += (
                '   <msDetector category="msDetector" value="{}"/>\n'
            ).format(self.ms_detector)
        ms_instrument += "  </msInstrument>\n"
        return ms_instrument


class DataProcessing:
    """dataProcessing class to store the information of the data processing."""

    def __init__(
        self,
        software="pymzxml",
        software_version=pkg_resources.get_distribution("pymzxml").version,
        software_type="processing",
    ):
        """Initialize the DataProcessing class."""
        self.software = software
        self.software_version = software_version
        self.software_type = software_type

    def __str__(self):
        """Return the DataProcessing as a string."""
        data_processing = "  <dataProcessing>\n"
        data_processing += (
            '   <software type="{}" name="{}" version="{}"/>\n'
        ).format(self.software, self.software_version, self.software_type)
        data_processing += "  </dataProcessing>\n"
        return data_processing


class Scan:
    """Scan class to store information about a single scan."""

    def __init__(
        self,
        scan_num,
        ms_level,
        retention_time,
        peaks,
        polarity=None,
        scan_type=None,
        filter_line=None,
        injection_time=None,
        precursor=None,
        precursor_intensity=None,
        activation_method=None,
        window_wideness=None,
        precursor_charge=None,
        precision=32,
        compress=False,
    ):
        """Initialize the Scan class."""
        self.scan_num = scan_num
        self.peaks_count = len(peaks) / 2
        self.polarity = polarity
        self.scan_type = scan_type
        self.filter_line = filter_line
        self.injection_time = injection_time
        self.low_mz = min(peaks[::2])
        self.high_mz = max(peaks[::2])
        self.base_peak_mz = peaks[peaks.index(max(peaks[1::2])) - 1]
        self.base_peak_intensity = max(peaks[1::2])
        self.tot_ion_current = sum(peaks[1::2])
        self.ms_level = ms_level
        self.retention_time = retention_time
        self.precursor = precursor
        self.precursor_intensity = precursor_intensity
        self.activation_method = activation_method
        self.window_wideness = window_wideness
        self.precursor_charge = precursor_charge
        self.precision = precision
        self.compression_type = "zlib" if compress else "none"
        self.compressed_len = None
        self.peaks = self.encode_peaks(peaks, precision, compress)
        self.scans = []

    def __str__(self):
        """Return the Scan as a string."""
        scan = self.open_xml()
        for sub_scan in self.scans:
            scan += str(sub_scan)
        scan += self.close_xml()
        return scan

    def open_xml(self):
        """Return the opening XML tags of the Scan.

        Use this instead of __str__ to write to a file serially.
        """
        scan_element = (
            '  <scan num="{}"\n'
            '   msLevel="{}"\n'
            '   peaksCount="{}"\n'
            '   retentionTime="PT{}S"\n'
            '   lowMz="{}"\n'
            '   highMz="{}"\n'
            '   basePeakMz="{}"\n'
            '   basePeakIntensity="{}"\n'
            '   totIonCurrent="{}"'
        ).format(
            self.scan_num,
            self.ms_level,
            self.peaks_count,
            self.retention_time,
            self.low_mz,
            self.high_mz,
            self.base_peak_mz,
            self.base_peak_intensity,
            self.tot_ion_current,
        )
        if self.polarity is not None:
            scan_element += '\n   polarity="{}"'.format(self.polarity)
        if self.scan_type is not None:
            scan_element += '\n   scanType="{}"'.format(self.scan_type)
        if self.filter_line is not None:
            scan_element += '\n   filterLine="{}"'.format(self.filter_line)
        if self.injection_time is not None:
            scan_element += '\n   injectionTime="{}"'.format(
                self.injection_time
            )
        scan_element += ">\n"
        if self.precursor is not None:
            scan_element += "   <precursorMz"
            if self.precursor_intensity is not None:
                scan_element += ' precursorIntensity="{}"'.format(
                    self.precursor_intensity
                )
            if self.activation_method is not None:
                scan_element += ' activationMethod="{}"'.format(
                    self.activation_method
                )
            if self.window_wideness is not None:
                scan_element += ' windowWideness="{}"'.format(
                    self.window_wideness
                )
            if self.precursor_charge is not None:
                scan_element += ' precursorCharge="{}"'.format(
                    self.precursor_charge
                )
            scan_element += ">{}</precursorMz>\n".format(self.precursor)
        scan_element += (
            '   <peaks precision="{}"\n'
            '    byteOrder="network"\n'
            '    compressionType="{}"'
        ).format(self.precision, self.compression_type)
        if self.compressed_len is not None:
            scan_element += '\n    compressedLen="{}"'.format(
                self.compressed_len
            )
        scan_element += ">{}</peaks>\n".format(self.peaks.decode("utf-8"))
        return scan_element

    @staticmethod
    def close_xml():
        """Return the closing XML tags of the Scan.

        Use this instead of __str__ to write to a file serially.
        """
        return "  </scan>\n"

    def encode_peaks(self, peaks, precision=32, compress=False):
        """Encode peaks to network byte order and base64 encode them."""
        binary_writer = struct.Struct(
            ">{}".format("f" if precision == 32 else "d")
        )
        binary_peaks = bytes()
        for value in peaks:
            binary_peaks += binary_writer.pack(value)
        if compress:
            binary_peaks = zlib.compress(binary_peaks)
            self.compressed_len = len(binary_peaks)
        return base64.b64encode(binary_peaks)

    @staticmethod
    def decode_peaks(byte_peaks, precision=32, compress=False):
        """Decode base64 encoded peaks fix endianess and convert them to
        float."""
        binary_reader = struct.Struct(
            ">{}".format("f" if precision == 32 else "d")
        )
        peaks = []
        binary_peaks = base64.b64decode(byte_peaks)
        if compress:
            binary_peaks = zlib.decompress(binary_peaks)
        for _, k in enumerate(binary_reader.iter_unpack(binary_peaks)):
            peaks += [k[0]]
        return peaks

    def add_scan(self, scan):
        """Add a scan to the list of scans."""
        self.scans.append(scan)

    def renumber_scans(self, start=1):
        """Renumber the scans in the list of scans."""
        i = start
        for scan in self.scans:
            scan.scan_num = i
            i += 1
            i = scan.renumber_scans(i)
        return i
