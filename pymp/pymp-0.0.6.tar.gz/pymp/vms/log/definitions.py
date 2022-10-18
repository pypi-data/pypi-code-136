# -*- coding: utf-8 -*-
"""
Copyright (c) 2015 Michael J Tallhamer

Varian Trajectory Log Definitions
Field definitions for Varian trajectory logs as layed out in the "TrueBeam 2.7MR2 Trajectory Log File Specification"
found on the myvarian site (https://varian.force.com/)

@author: Michael J Tallhamer M.Sc DABR (mike.tallhamer@pm.me)
"""
# Standard python imports
from enum import Enum

# Third party imports
import numpy as np

# Local imports.

# Maping between the defined version and the  "TrueBeam Trajectory Log File 
# Specification standard. Will be updated when new specifications are supported.
SPECIFICATION_MAP = {3.0: 'VMSTrajectoryLog_2.5',   # TrueBeam 2.5
                     4.0: 'VMSTrajectoryLog_2.7MR2' # TrueBeam 2.7 MR2 
                     }

# Defined in "TrueBeam 2.7MR2 Trajectory Log File Specification" Header section in table on page 8.
class AXIS(Enum):
    CollRtn = 0
    GantryRtn = 1
    Y1 = 2
    Y2 = 3
    X1 = 4
    X2 = 5
    CouchVert = 6
    CouchLng = 7
    CouchLat = 8
    CouchRtn = 9
    CouchPitch = 10
    CouchRoll = 11
    MU = 40
    BeamHold = 41
    ControlPoint = 42
    MLC = 50
    TargetPosition = 60             # Tracking Developer Mode Only
    TrackingTarget = 61             # Tracking Developer Mode Only
    TrackingBase = 62               # Tracking Developer Mode Only
    TrackingPhase = 63              # Tracking Developer Mode Only
    TrackingConformityIndex = 64    # Tracking Developer Mode Only

# Log Scale Enum defined in "TrueBeam 2.7MR2 Trajectory Log File Specification"
class AXIS_SCALE(Enum):
    MACHINE = 1
    MODIFIED_IEC_61217 = 2
             
# Defined in "TrueBeam 2.7MR2 Trajectory Log File Specification" Dose Servo States section.
class DOSE_SERVO_STATE(Enum):
    NORMAL = 0
    FREEZE = 1
    HOLD = 2
    DISABLED = 3
                     
# Defined in "TrueBeam 2.7MR2 Trajectory Log File Specification" Header section in table on page 8.
class MLC(Enum):
    NDS_80 = 0 # Added in TrueBeam v2.5 Specification
    NDS_120 = 2
    NDS_120_HD = 3

TXT_PROPERTY_TYPES = {"Patient ID":str,
                      "Plan Name":str,
                      "Plan UID":str,
                      "Beam Number":str,
                      "Beam Name":str,
                      "Original MU":float,
                      "Logging Scale":str,
                      "X1 (Cms)":float,
                      "X2 (Cms)":float,
                      "Y1 (Cms)":float,
                      "Y2 (Cms)":float,
                      "Gantry Rotation Angle (deg)":float,
                      "Energy":str,
                      "MU1":float,
                      "MU2":float,
                      "Radiation Time (mins)":float,
                      "DoseRate (MU/min)":float,
                      "PFN High Voltage Power Supply Current (A)":float,
                      "PFN Actual Voltage (KV)":float,
                      "RF Driver Voltage (V)":float,
                      "RF Forward Power (W)":float,
                      "AFC Error (V)":float,
                      "Gun Current (A)":float,
                      "Gun High Voltage (V)":float,
                      "Gun Grid Voltage (V)":float,
                      "Gun Filament Step Voltage (V)":float,
                      "Gun Filament Voltage (V)":float,
                      "Bend Magnet Current (A)":float,
                      "Bend Magnet Voltage (V)":float,
                      "Accelerator Solenoid Current (A)":float,
                      "Klystron Solenoid Current (A)":float,
                      "Radial Symmetry (%)":float,
                      "Transverse Symmetry (%)":float,
                      "Target Current (nC)":float,
                      "Buncher Radial Current (A)":float,
                      "Buncher Transverse Current (A)":float,
                      "Angle Radial Current (A)":float,
                      "Angle Transverse Current (A)":float,
                      "Position Radial Current (A)":float,
                      "Position Transverse Current (A)":float,
                      "Trim (A)":float,
                      "Accelerator Vacion Current (uA)":float,
                      "Positive 5V dc":float,
                      "Positive 24V dc":float,
                      "Analog Negative 5V dc":float,
                      "Analog Positive 5V dc":float,
                      "Negative 12V dc":float,
                      "Positive 3V dc":float,
                      "Node Power Supply Voltage (V)":float,
                      "Water Level":str,
                      "City Water Temperature (deg C)":float,
                      "Internal Water Supply Temperature (deg C)":float,
                      "Gas Pressure (PSI)":float
                      }

# Composite fields represent axis objects that have more than 1 sample per axis. For example the MLC axis has 122
# samples per axis representing the 2 carriages and the 120 individual leaves. The COMPOSITE_FIELDS dict allows you to
# define the root axis name as well as the axis names for each of the sub-samples as a tuple which will in turn be used
# to create the numpy.dtype object which is then used to construct the views for the axes.
COMPOSITE_FIELDS = {'MLC': ('CarrA',
                            'CarrB',
                            'LeafA1',
                            'LeafA2',
                            'LeafA3',
                            'LeafA4',
                            'LeafA5',
                            'LeafA6',
                            'LeafA7',
                            'LeafA8',
                            'LeafA9',
                            'LeafA10',
                            'LeafA11',
                            'LeafA12',
                            'LeafA13',
                            'LeafA14',
                            'LeafA15',
                            'LeafA16',
                            'LeafA17',
                            'LeafA18',
                            'LeafA19',
                            'LeafA20',
                            'LeafA21',
                            'LeafA22',
                            'LeafA23',
                            'LeafA24',
                            'LeafA25',
                            'LeafA26',
                            'LeafA27',
                            'LeafA28',
                            'LeafA29',
                            'LeafA30',
                            'LeafA31',
                            'LeafA32',
                            'LeafA33',
                            'LeafA34',
                            'LeafA35',
                            'LeafA36',
                            'LeafA37',
                            'LeafA38',
                            'LeafA39',
                            'LeafA40',
                            'LeafA41',
                            'LeafA42',
                            'LeafA43',
                            'LeafA44',
                            'LeafA45',
                            'LeafA46',
                            'LeafA47',
                            'LeafA48',
                            'LeafA49',
                            'LeafA50',
                            'LeafA51',
                            'LeafA52',
                            'LeafA53',
                            'LeafA54',
                            'LeafA55',
                            'LeafA56',
                            'LeafA57',
                            'LeafA58',
                            'LeafA59',
                            'LeafA60',
                            'LeafB1',
                            'LeafB2',
                            'LeafB3',
                            'LeafB4',
                            'LeafB5',
                            'LeafB6',
                            'LeafB7',
                            'LeafB8',
                            'LeafB9',
                            'LeafB10',
                            'LeafB11',
                            'LeafB12',
                            'LeafB13',
                            'LeafB14',
                            'LeafB15',
                            'LeafB16',
                            'LeafB17',
                            'LeafB18',
                            'LeafB19',
                            'LeafB20',
                            'LeafB21',
                            'LeafB22',
                            'LeafB23',
                            'LeafB24',
                            'LeafB25',
                            'LeafB26',
                            'LeafB27',
                            'LeafB28',
                            'LeafB29',
                            'LeafB30',
                            'LeafB31',
                            'LeafB32',
                            'LeafB33',
                            'LeafB34',
                            'LeafB35',
                            'LeafB36',
                            'LeafB37',
                            'LeafB38',
                            'LeafB39',
                            'LeafB40',
                            'LeafB41',
                            'LeafB42',
                            'LeafB43',
                            'LeafB44',
                            'LeafB45',
                            'LeafB46',
                            'LeafB47',
                            'LeafB48',
                            'LeafB49',
                            'LeafB50',
                            'LeafB51',
                            'LeafB52',
                            'LeafB53',
                            'LeafB54',
                            'LeafB55',
                            'LeafB56',
                            'LeafB57',
                            'LeafB58',
                            'LeafB59',
                            'LeafB60'),
                    'TargetPosition' : ('X', 'Y', 'Z'),
                    'TrackingTarget' : ('X', 'Y', 'Z'),
                    'TrackingBase' :  ('X', 'Y', 'Z'),
                    'TrackingConformityIndex' : ('Overexposed', 'Underexposed')
                    }

# Samples consist of 'expected' and 'actual' values.
SAMPLE_TYPE = np.dtype([('expected', 'f4'), ('actual', 'f4')])

# Tracking Samples consist of 'order' and 'status' values.
TRACKING_TYPE = np.dtype([('order', 'f4'), ('status', 'f4')])
