import os
import platform
import subprocess
import pandas as pd
from .settings import Settings
import pickle
import gzip

class vmachine:
    def __init__(self):
        self._dev_platform = platform.system()
        self._dev_platform_vers = platform.version()
        self._dev_platform_release = platform.release()

        print("Platform: " + self._dev_platform)
        print("Platform version: " + self._dev_platform_vers)
        print("Platform release: " + self._dev_platform_release)

    #### GLOBAL VARS ####
    @property
    def Dev_platform(self):
        """
        :type: string
        """
        return self._dev_platform

    @Dev_platform.setter
    def Dev_platform(self, value):
        """
        :type: string
        """
        self._dev_platform = value

    @property
    def Dev_platform_vers(self):
        """
        :type: string
        """
        return self._dev_platform_vers

    @Dev_platform_vers.setter
    def Dev_platform_vers(self, value):
        """
        :type: string
        """
        self._dev_platform_vers = value

    @property
    def Dev_platform_release(self):
        """
        :type: string
        """
        return self._dev_platform_release

    @Dev_platform_release.setter
    def Dev_platform_release(self, value):
        """
        :type: string
        """
        self._dev_platform_release = value
    #### END OF GLOBAL VARS ####

    #### Generates folder structer of the virtual enviroment and copy's data from given locations ####
    def Generate_structure(self, model_localpath="", validation_data_localpath="", validation_control_localpath="", base_path="", model_name = "",
                                requirements_localpath="Development", documentation_localpath="Development", function_code_localpath="Development", main_code_localpath="Development"):

        Settings.Base_path = base_path
        Settings.Enviroment_name = model_name

        # INTERNAL VARS
        validation_content = pd.DataFrame()
        validation_control_content = pd.DataFrame()
        function_content = ""
        requirements_content = ""
        documentation_content = ""
        main_content = ""

        print("Starting folder generation...")

        #### validation set copy ####
        print("Locating and copying validation data set")
        ### Check file type extension ###
        validation_filename, validation_file_extension = os.path.splitext(
            validation_data_localpath)
        print("File extension is: " + str(validation_file_extension))
        if validation_file_extension == ".csv":
            validation_content = pd.read_csv(validation_data_localpath)
        elif validation_file_extension == ".pkl":
            validation_content = pd.read_pickle(validation_data_localpath)
        elif validation_file_extension == ".gzip":
            validation_content = pd.read_parquet(validation_data_localpath)
        print("Validation data collected")

        #### Machine leanring model copy ####
        model_filename, model_file_extension = os.path.splitext(
            model_localpath)
        print("File extension is: " + str(model_file_extension))
        if model_file_extension == ".gz":
            model_file = gzip.open(model_localpath, "rb")
            model_file_content = model_file.read()
        elif model_file_extension == ".pkl":
            model_file = open(model_localpath, 'rb')

        #### validation control copy ####
        print("Locating and copying validation control data set")
        ### Check file type extension ###
        validation_control_filename, validation_control_file_extension = os.path.splitext(
            validation_control_localpath)
        print("File extension is: " + str(validation_control_file_extension))
        if validation_control_file_extension == ".csv":
            validation_control_content = pd.read_csv(validation_control_localpath)
        elif validation_control_file_extension == ".pkl":
            validation_control_content = pd.read_pickle(validation_control_localpath)
        elif validation_control_file_extension == ".gzip":
            validation_control_content = pd.read_parquet(validation_control_localpath)
        print("Validation data collected")

        #### Function code copy ####
        print("Creating function code")
        if function_code_localpath == "Development":
            # Need to replace with globals when in package #
            function_content = Settings.Premade_function_code_data
        else:
            function_content = open(function_code_localpath, "r")

        #### Main code copy ####
        print("Creating Main py code")
        if function_code_localpath == "Development":
            main_content = Settings.Premade_main_code_data  # Need to replace with globals when in package #
        else:
            main_content = open(main_code_localpath, "r")

        #### Requirements copy ####
        print("Creating Requirements file")
        if function_code_localpath == "Development":
            requirements_content = Settings.Premade_requirements_data  # Need to replace with globals when in package #
        else:
            requirements_content = open(requirements_localpath, "r")

        #### Documentation copy ####
        print("Creating documentation file")
        if documentation_localpath == "Development":
            documentation_content = Settings.Premade_documentation_data  # Need to replace with globals when in package #
        else:
            documentation_content = open(documentation_localpath, "r")

        # Folder structure
        print("Generating folder structure with data points")
        folders = [{"path": Settings.Base_path + "virtualenv_" + model_name + "/code/validate.py",
                    "content": function_content},
                {"path": Settings.Base_path + "virtualenv_" + model_name + "/data/data.gzip",
                    "content": "clear"},
                {"path": Settings.Base_path + "virtualenv_" + model_name + "/data/data_control.gzip",
                    "content": "clear"},
                {"path": Settings.Base_path + "virtualenv_" + model_name + "/model/model.pkl",
                    "content": "clear"},
                {"path": Settings.Base_path + "virtualenv_" + model_name + "/requirements.txt",
                    "content": requirements_content},
                {"path": Settings.Base_path + "virtualenv_" + model_name + "/docs/documentation.txt",
                    "content": documentation_content},
                {"path": Settings.Base_path + "virtualenv_" + model_name + "/main.py",
                    "content": main_content}
                ]

        #### Write files and directory's ####
        for item in folders:
            os.makedirs(os.path.dirname(item["path"]), exist_ok=True)
            with open(item["path"], "w") as f:
                if item["content"] != "clear":
                    f.write(item["content"])

        #### Write PD to files ####
        print("Writing data")
        validation_content.to_parquet(
            Settings.Base_path + "virtualenv_" + model_name + "/data/data.gzip")
        validation_control_content.to_parquet(
            Settings.Base_path + "virtualenv_" + model_name + "/data/data_control.gzip")

        ### Copy machine learning model ###
        print("Writing Machine learning model")
        copy_model_file = open(Settings.Base_path + "virtualenv_" + model_name + "/model/model.pkl", "wb")
        pickle.dump(model_file_content, copy_model_file)

        copy_model_file.close()
        model_file.close()

        #### Create files needed for the virtual machine ####
        print("Generating VENV Data")
        cmd = 'python -m venv ' + Settings.Base_path + 'virtualenv_' + model_name
        p = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
        print(p.stdout.decode())

        #### Finish ####
        print("Virtual machine folder structure created on: " +
            Settings.Base_path + "/virtualenv_" + model_name)

    #### This function will start the virtual enviroment on a local machine ####
    def Start_venv(self, localpath="", execution_code=""):
        if self._dev_platform == "Windows":
            print("starting virtual machine for Windows")
            #& python code/' + execution_code + ' .py
            cmd ='pip install virtualenv & cd ' + localpath + ' & virtualenv venv & ' + localpath + '/scripts/activate & cd c:/ & cd ' + localpath + ' & dir & pip install -r requirements.txt & uvicorn main:app'

            # Start the virtual enviroment with the code.
            p = subprocess.run(cmd,shell=True, stdout=subprocess.PIPE)
            print(p.stdout.decode())

        elif self._dev_platform == "Linux":
            print("starting virtual machine for Linux")
            cmd ='pip install virtualenv ; cd ' + localpath + ' ; virtualenv venv ; ' + localpath + '/scripts/activate ; cd c:/ ; cd ' + localpath + ' ; dir ; pip install -r requirements.txt ; python code/' + execution_code + ' ; uvicorn main:app'

            # Start the virtual enviroment with the code.
            p = subprocess.run(cmd,shell=True, stdout=subprocess.PIPE)
            print(p.stdout.decode())

        elif self._dev_platform == "MacOS":
            print("starting virtual machine for Apple")

