'''
    lmautomation.py
    
    Version:: 1.0.22
 
    Helper functions extending radkit_helpers to support DDR usecase file transfers
    to the devices using RADKit
'''

from enum import Enum
from os import path
from typing import Optional, Union, List, Dict

from radkit_common.nglog import debug, warning, info, error, basicConfig, DEBUG
from radkit_client.device import DeviceDict, Device
import radkit_client.helpers as lmerrors

def scp_upload_from_buffer(
    target_dev: Union[DeviceDict, Device, lmerrors.DeviceFlow],
    target_filename: str,
    chmod: str,
    data: bytes,
) -> None:
    """
        This function uses radkit_client to upload files to the device using scp
    
            :param target_dev: Individual device name or list of devices (names from service.inventory)
            :param target_filename: Name for the file in /bootflash/guest-share/ddr/USECASE_NAME on device
            :param chmod: Set the permissions for the files copied to the device
            :data: File content 
        
        Usage::

              pi = mlmddr.Automation.read_from_file(USECASE_NAME, HOMEPATH + "/files/(clips-files or py-files)/USECASE_NAME")

        :raises none:
    
    """    
    if isinstance(target_dev, Device):
        target_dev = target_dev.singleton()
    elif isinstance(target_dev, lmerrors.DeviceFlow):
        target_dev = target_dev.active_devices

    for device in target_dev.values():
        debug(f"  target device: {device.name}")
        scp = device.scp_upload_from_stream(target_filename, len(data)).wait()
        debug("  SCP ready")
        scp.result.write(data)
        scp.wait()
        debug("  Write done")
        scp.result.close()

def _read_file(filename: str) -> bytes:

    with open(filename, "r") as f:
        return f.read().encode()
#
# Model value controls operations in mlmddr when deploying DDR-python and DDR-clips usecases
#
class Model(Enum):
    CLIPS = 0
    PYTHON = 1
#
# Files used to control DDR-clips usecase behavior.  ddr- is added to these elements 
#
CLIPS_COMPONENTS = ["devices", "facts", "flags", "rules", "control", "sim", "parsers"]

class Automation:
    """
        The Automation class creates and returns an Automation object with the
        information required to run the usecase.  This includes the names of files to transfer
        to the device using RADKit and the type of usecase CLIPS or PYTHON
    
            :param USECASE_NAME: Name of the directory in ddr-lm/files containing usecase definition
            :param usecase: Absolute path to the usecase directory 
        
        Usage::

              pi = mlmddr.Automation.read_from_file(USECASE_NAME, HOMEPATH + "/files/(clips-files or py-files)/USECASE_NAME")

        :raises none:
    
    """
    def __init__(
        self, name: str, model: Optional[Model] = None, elements: Optional[dict] = None
    ) -> None:
        self.name = name.strip()
        self.model = model
        if elements is None:
            self.elements = {}
        else:
            self.elements = elements

    @classmethod
    def read_from_file(cls, name: str, filename: str) -> "Automation":
        ddr_components = {}
        if path.isdir(filename):
            model = Model.CLIPS
            for component in CLIPS_COMPONENTS:
                file_component = path.join(filename, f"ddr-{component}")
                debug(f"Loading '{file_component}'")
                try:
                    ddr_components[component] = _read_file(file_component)
                except:
                    pass
        elif path.isfile(filename) and filename[-3:] == ".py":
            model = Model.PYTHON
            ddr_components["script"] = _read_file(filename)
        else:
            return

        return cls(name, model, ddr_components)
