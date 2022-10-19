
import os
import platform
import sys
from utils import log


class FirmwareBinPath(object):

    def __init__(self):
        self.linux_path = "/home/share/release/redtail"
        self.windows_path = r"\\172.29.190.4\share\release\redtail"
        self.auto_build_folder = "nightly"

    def get_default_base_path(self):
        if "win" in sys.platform.lower():
            base_path = self.windows_path
        else:
            base_path = self.linux_path
        return base_path

    def get_image_path(self, base_path, volume, commit_id, nand):
        if os.path.exists(base_path):
            commit_6bit = commit_id[0:6]
            nand = "ALL" if volume.lower() == "all" else nand
            nand = nand.lower()
            volume = volume.lower()
            _files = os.listdir(base_path)
            for item in _files:
                item_path = os.path.join(base_path, item)
                if os.path.isdir(item_path) and commit_6bit in item:
                    ret = self.get_image_path(item_path, volume, commit_id, nand)
                    if ret is not None:
                        return ret
                elif ("_{}_".format(volume) in item.lower()) and ("preBootloader".lower() not in item.lower()) and \
                        item.endswith(".bin") and ("_{}_".format(nand) in item.lower()):
                    return os.path.join(base_path, item)

    def get_fw_path_from_parameter(self, parameters, base_path=""):
        volume = parameters.get("volume", "ALL")
        nand = parameters.get("nand", "ALL")
        commit = parameters.get("commit", "")
        fw_path = parameters.get("fw_path", base_path) if base_path == "" else base_path
        if os.path.isfile(fw_path):
            fw_bin_path = fw_path
        else:
            volume = "ALL" if volume == "" else volume
            nand = "ALL" if nand == "" else nand
            log.INFO("fw path {} volume {} commit {} nand {}".format(fw_path, volume, commit, nand))
            fw_bin_path = self.get_image_path(fw_path, volume, commit, nand)
        log.INFO("Get path from parameters: {}".format(fw_bin_path))
        return fw_bin_path

    @staticmethod
    def change_path_win_2_linux(win_path):
        if win_path is not None:
            path_temp = win_path.replace("\\\\172.29.190.4", "/home")
            linux_path = path_temp.replace("\\", "/")
            log.INFO("Get linux path: {}".format(linux_path))
        else:
            linux_path = "not_find_linux_path"
        return linux_path

    @staticmethod
    def change_path_linux_2_win(linux_path):
        if linux_path is not None:
            linux_path = linux_path.replace("//", "/")
            path_temp = linux_path.replace("/home", "\\\\172.29.190.4")
            win_path = path_temp.replace("/", "\\")
            log.INFO("Get win path: {}".format(win_path))
        else:
            win_path = "not_find_win_path"
        return win_path

    def get_default_base_path_enhance(self, parameters):
        if "base_path" in parameters.keys():  # for oakgate
            return parameters["base_path"]
        if "fw_path" in parameters.keys():   # for perses
            temp_path = parameters["fw_path"]
            if "172.29.190.4" in temp_path:
                if "win" in sys.platform.lower():
                    base_path = temp_path
                else:
                    base_path = self.change_path_win_2_linux(temp_path)
            else:
                base_path = temp_path
        else:
            base_path = self.get_default_base_path()
        log.INFO("Get base path: {}".format(base_path))
        return base_path

    def generate_oakgate_images(self, parameters):
        output_parm = dict()
        volume = parameters.get("volume", "ALL")
        nand = parameters.get("nand", "ALL")
        base_path = self.get_default_base_path_enhance(parameters)
        if "image1" not in parameters.keys() and "base_version" in parameters.keys():
            ret = self.get_image_path(base_path, volume, parameters["base_version"], nand)
            if ret is not None:
                output_parm["image1"] = ret
                output_parm["base_version"] = parameters["base_version"]
        if "image2" not in parameters.keys():
            if "target_version" in parameters.keys():
                ret = self.get_image_path(base_path, volume, parameters["target_version"], nand)
                if ret is not None:
                    output_parm["image2"] = ret
                    output_parm["target_version"] = parameters["target_version"]
            else:
                if "image1" in output_parm.keys():
                    output_parm["image2"] = output_parm["image1"]
                    output_parm["target_version"] = output_parm["base_version"]
        return output_parm

    def update_perses_fw_path(self, parameters):
        if "fw_path" in parameters.keys():
            if "win" in platform.system().lower():
                temp_path = self.change_path_linux_2_win(parameters["fw_path"])
            else:
                temp_path = self.change_path_win_2_linux(parameters["fw_path"])
        else:
            temp_path = self.get_default_base_path_enhance(parameters)
        fw_path = self.get_fw_path_from_parameter(parameters, temp_path)
        if fw_path is not None:
            log.INFO("update_perses_fw_path: {}".format(fw_path))
            parameters["fw_path"] = fw_path
            os.environ["fw_path"] = fw_path
        else:
            log.WARN("Not find path: perses_fw_path")
        print(parameters)
        return parameters
