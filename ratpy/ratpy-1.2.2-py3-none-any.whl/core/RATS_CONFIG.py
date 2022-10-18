"""
This configuration file is used to define the expected structure of the data packets

Contents are defined in order of appearance and have a number of bytes associated with them
"""
import os.path
import pathlib
from enum import Enum, unique


class PlotBanks(Enum):
    def __init__(self, designation, number_of_plot_banks):
        self.designation = designation
        self.number_of_plot_banks = number_of_plot_banks

    """Defines the id prefix for each app's html components and the number of plot banks that each app displays"""
    Error_detection = "error_detection_app_", 2
    Scope = "scope_app_", 10
    Jitter_analysis = "jitter_app_", 10
    Data_management = "data_management_app_", 0  # number_of_plot_banks redundant for this app, yet required for app initialisation


# =====================================================================================================================
#                              PACKET FORMAT CONFIGURATION
# =====================================================================================================================
GDS0 = dict(
    PROTOCOL=1,
    PAYLOAD_SIZE=1,
    PACKET_COUNT=2,
    TIME_STAMP=6,
    SAMPLE_RATE=2,
    LLC_COUNT=4,
    FUNCTION=2,
    SAMPLE=2,
    BARCODE_HASH=4,
    RETENTION_TIME=4,
    RESERVED=2,
    ACTIVE_EDBS=2,
    DATA=2  # signifies the bytes expected per sample, rather than the total number of bytes
)

GDS1 = dict(
    PROTOCOL=1,
    PAYLOAD_SIZE=1,
    PACKET_COUNT=2,
    TIME_STAMP=6,
    SAMPLE_RATE=2,
    LLC_COUNT=4,
    FUNCTION=2,
    SAMPLE=2,
    BARCODE_HASH=4,
    RETENTION_TIME=4,
    RESERVED=2,
    ACTIVE_EDBS=2,
    DATA=4  # signifies the bytes expected per sample, rather than the total number of bytes
)

packet_format_dictionary = {0: GDS0, 1: GDS1}

# These columns will be dropped after parsing to keep dataframes small. We don't use them for anything after parsing,
# at the minute, anyway - now rolled into the gds protocol enums above...
Packet = GDS0

class Packet(Enum):
    # =====================================================================================
    # This is the prototype packet enum and will soon be depracated
    # define modified enum class to handle multiple attribute assignment
    # DO NOT MODIFY
    def __init__(self, field_name, number_of_bytes, keep):
        self.field_name = field_name
        self.number_of_bytes = number_of_bytes
        self.keep = keep  # used to discard colulmns which are ultimately unused in the final file for the visualiser -  values will be kept in metadata rather than the dataframe

    # =====================================================================================
    """
    The order of appearance of these fields should match the expected format of the RATS .txt file
    the Enum property names SHOULD NOT be changed

    Attribute format; PROPERTY = field_name, number_of_bytes

    Required attributes: 
        - LLC_COUNT
        - FUNCTION
        - ACTIVE_EDBS
        - DATA
        - TIME_STAMP
        - SAMPLE_RATE
        - PROTOCOL
    """
    PROTOCOL = "PROTOCOL", 1, False
    PAYLOAD_SIZE = "PAYLOAD_SIZE", 1, False
    PACKET_COUNT = "PACKET_COUNT", 2, True
    TIME_STAMP = "TIME_STAMP", 6, True
    SAMPLE_RATE = "SAMPLE_RATE", 2, True
    LLC_COUNT = "LLC_COUNT", 4, True
    FUNCTION = "FUNCTION", 2, True
    SAMPLE = "SAMPLE", 2, False
    BARCODE_HASH = "BARCODE_HASH", 4, False
    RETENTION_TIME = "RETENTION_TIME", 4, False
    RESERVED = "RESERVED", 2, False
    ACTIVE_EDBS = "ACTIVE_EDBS", 2, True

    # ============================================================
    DATA = "DATA", 2, True  # signifies the bytes expected per sample, rather than the total number of bytes


unused_columns = [Packet.PROTOCOL.field_name,
                  Packet.PAYLOAD_SIZE.field_name,
                  Packet.SAMPLE.field_name,
                  Packet.BARCODE_HASH.field_name,
                  Packet.RETENTION_TIME.field_name,
                  Packet.RESERVED.field_name]  # this also needs reimagining or
# =====================================================================================================================
#                              LLC CONFIGURATION
# =====================================================================================================================

#   ON WHICH EDB (RATS input) DO WE EXPECT TO FIND THE LLC STATES, THIS IS UNLIKELY TO CHANGE, SO DON'T MESS WITH THIS
#   UNLESS YOU REALLY KNOW WHAT YOU'RE DOING
LLCEDB = 0


class LLCEDBFormat(Enum):
    """
    CHANGE THE ENUM PROPERTY NAMES TO DEFINE THE ACTIVE LLCS. ANY PROPERTY WITH 'BIT' IN ITS NAME WILL NOT BE STORED
    BY THE PARSING OPERATION.

    """
    BIT0 = 0
    BIT1 = 1
    BIT2 = 2
    BIT3 = 3
    BIT4 = 4
    BIT5 = 5
    BIT6 = 6
    BIT7 = 7
    BIT8 = 8
    BIT9 = 9
    SIP = 10  # SIP is recorded on bit 10
    BIT11 = 11
    BUFFIS = 12  # BUFFIS is recorded on bit 12
    BIT13 = 13
    BIT14 = 14
    BIT15 = 15


# =====================================================================================================================
#                              FILE PATH CONFIGURATION
# =====================================================================================================================
'''names of the relevant subdirectories under the rats directory'''

packagepath = pathlib.Path(__file__).parent.parent.resolve()
splitchar = os.path.sep
cachepath = 'cache'
dfpath = 'dataframes'
topopath = 'topo'
