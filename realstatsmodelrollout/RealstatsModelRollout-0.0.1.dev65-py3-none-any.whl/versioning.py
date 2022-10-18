import string
from .settings import settings
from .global_functions import globalFunctions
from github import Github
from datetime import date
import os
import json
import subprocess

class Versioning():
    def __init__(self, repo_name="bharkema/model_test", model_version="1", gitaccesstoken="development", model_name="development"):
        self._repo_name = repo_name
        self._model_version = model_version
        self._gitaccesstoken = gitaccesstoken
        self._model_version

    @property
    def repo_name(self):
        """
        :type: string
        """
        return self._repo_name

    @repo_name.setter
    def repo_name(self, value):
        """
        :type: string
        """
        self._repo_name = value

    @property
    def gitaccesstoken(self):
        """
        :type: string
        """
        return self._gitaccesstoken
    
    @gitaccesstoken.setter
    def gitaccesstoken(self, value):
        """
        :type: string
        """
        self._gitaccesstoken = value

    @property
    def model_version(self):
        """
        :type: string
        """
        return self._model_version

    @model_version.setter
    def model_version(self, value):
        """
        :type: string
        """
        self._model_version = value

    @property
    def model_name(self):
        """
        :type: string
        """
        return self._model_name

    @model_name.setter
    def model_name(self, value):
        """
        :type: string
        """
        self._model_name = value


    def Upload_enviroment(self, enviroment_localpath="Development"):
        git = Github(self._gitaccesstoken)
        git_repo = ""
        try:             
            git_repo = git.get_repo(self._repo_name)
        except:
            print("Not able to get given repo: " + self.repo_name)
            return

        git_user = git.get_user()
        git_user_data = git_user.get_emails()

        local_envpath = ""
        ### Get directory ###
        print("Looking for directory")
        if enviroment_localpath != "Development":
            if enviroment_localpath[-1] == '/':
                local_envpath = enviroment_localpath
            else: 
                local_envpath = enviroment_localpath + "/"
        else: 
            local_envpath = settings.base_path + "virtualenv_" + settings.enviroment_name + "/"
        
        isDirectory = os.path.isdir(local_envpath)
        if isDirectory == False:
            return "This is not a correct directory"

        indexes = globalFunctions.find(local_envpath, "/")
        max_count = len(indexes) - 1
        env_name = local_envpath[indexes[max_count - 1] + 1:indexes[max_count]]

        ### Collect all data needed in dir ###
        print("Collecting data")
        requirements_file = open(local_envpath + "requirements.txt", "r")
        requirements_string = requirements_file.read()

        model_file = open(local_envpath + "/model/model.pkl", "rb")
        model_file_data = model_file.read()

        validation_data_file = open(local_envpath + "data/data.gzip", "rb")
        validation_data_file_data = validation_data_file.read()

        validation_data_control_file = open(local_envpath + "data/data_control.gzip", "rb")
        validation_data_control_file_data = validation_data_control_file.read()

        main_py_file = open(local_envpath + "main.py", "r")
        main_py_file_data = main_py_file.read()

        function_py_file = open(local_envpath + "code/validate.py", "r")
        function_py_file_data = function_py_file.read()

        ### Generate date version
        print("Generating version data")
        today = date.today()
        version = today.strftime("%d%m%Y")

        # Check if app with version already exists, if it does, append number
        versionInUse = True
        additional = 1
        while versionInUse:
            try:
                git_repo.get_contents(env_name + "/" + version + "/version_info.json")
                if additional == 1:
                    version = version + "-" + str(additional)
                else:
                    version = version[:-1]
                    version = version + str(additional)
                additional+=1
            except:
                versionInUse = False
                pass
                break


        version_data = {
            "Upload_date": today.strftime("%d/%m/%Y"),
            "Model_name": env_name,
            "Package_version": settings.package_version,
            "Requirements": requirements_string,
            "uploaded_by": git_user_data[0].email
        }

        ### Upload to Git ###
        print("Uploading to Git")
        gitFilePath =  env_name + "/" + version + "/"
        commitMessage = env_name + " - " + version + " published"

        # Create requirements file
        appFilePath =  gitFilePath + "_requirements.txt"
        git_repo.create_file(appFilePath, commitMessage, requirements_string, branch="main")
        print("Requirements... done!")

        # Create main.py file
        appFilePath =  gitFilePath + "main.py"
        git_repo.create_file(appFilePath, commitMessage, main_py_file_data, branch="main")
        print("Main code... done!")

        # Create python custom code file
        appFilePath =  gitFilePath + "function.py"
        git_repo.create_file(appFilePath, commitMessage, function_py_file_data, branch="main")
        print("Custom code... done!")

        # Create Validation data file
        appFilePath =  gitFilePath + "validation_data.gzip"
        git_repo.create_file(appFilePath, commitMessage, validation_data_file_data, branch="main")
        print("Validation data... done!")

        # Create validation control data file
        appFilePath =  gitFilePath + "validation_control_data.gzip"
        git_repo.create_file(appFilePath, commitMessage, validation_data_control_file_data, branch="main")
        print("Validation control data... done!")

        # Create model data file
        appFilePath =  gitFilePath + "model.pkl"
        git_repo.create_file(appFilePath, commitMessage, model_file_data, branch="main")
        print("Model data... done!")

        # Create version data file
        version_info_json = json.dumps(version_data)
        appFilePath =  gitFilePath + "version_info.json"
        git_repo.create_file(appFilePath, commitMessage, version_info_json, branch="main")
        print("Version data... done!")
        return "Saved model data under: " + self._repo_name + "/" + env_name + "/" + version

    def Download_enviroment(self, localpath="", generate_venv=True):
        git = Github(self._gitaccesstoken)
        git_repo = ""
        try:             
            git_repo = git.get_repo(self._repo_name)
        except:
            print("Not able to get given repo: " + self.repo_name)
            return

        local_envpath = ""
        ### Get directory ###
        print("Looking for directory")
        if localpath[-1] == '/':
            local_envpath = localpath
        else: 
            local_envpath = localpath + "/"
            
        isDirectory = os.path.isdir(local_envpath)
        if isDirectory == False:
            return "This is not a correct directory"


        ### Get Files from repo
        print("Downloading files from remote")

        requirements = git_repo.get_contents(self._model_name + '/' + self._model_version + "/_requirements.txt")
        print("Requirements... Done!")

        model_data = git_repo.get_contents(self._model_name + '/' + self._model_version + "/model.pkl")
        print("Model... Done!")

        validation_data = git_repo.get_contents(self._model_name + '/' + self._model_version + "/validation_data.gzip")
        print("Validation data... Done!")

        validation_control_data = git_repo.get_contents(self._model_name + '/' + self._model_version + "/validation_control_data.gzip")
        print("Validation control data... Done!")

        main_code_data = git_repo.get_contents(self._model_name + '/' + self._model_version + "/main.py")
        print("Main python code... Done!")

        function_code_data = git_repo.get_contents(self._model_name + '/' + self._model_version + "/function.py")
        print("Function python code... Done!")

        version_info_data = git_repo.get_contents(self._model_name + '/' + self._model_version + "/version_info.json")
        print("Version info... Done!")

        ### Generate folder ###
        # Folder structure
        print("Generating folder structure with data points")
        folders = [{"path": local_envpath  + self._model_name + "/" + self._model_version + "/code/validate.py",
                    "content": function_code_data.decoded_content.decode("utf-8")},
                {"path": local_envpath + self._model_name + "/" + self._model_version + "/data/data.gzip",
                    "content": validation_data.decoded_content},
                {"path": local_envpath + self._model_name + "/" + self._model_version + "/data/data_control.gzip",
                    "content": validation_control_data.decoded_content},
                {"path": local_envpath + self._model_name + "/" + self._model_version + "/model/model.pkl",
                    "content": model_data.decoded_content},
                {"path": local_envpath + self._model_name + "/" + self._model_version + "/requirements.txt",
                    "content": requirements.decoded_content.decode("utf-8")},
                {"path": local_envpath + self._model_name + "/" + self._model_version + "/docs/documentation.txt",
                    "content": version_info_data.decoded_content.decode("utf-8")},
                {"path": local_envpath + self._model_name + "/" + self._model_version + "/main.py",
                    "content": main_code_data.decoded_content.decode("utf-8")}
                ]

        #### Write files and directory's ####
        for item in folders:
            os.makedirs(os.path.dirname(item["path"]), exist_ok=True)
            with open(item["path"], "w") as f:
                if isinstance(item["content"], string):
                    f.write(item["content"])
                elif isinstance(item["content"], bytes): 
                    fb = open(item["path"], "wb")
                    fb.write([item["content"]])
                else:
                    return "Not able to write file: " + item["path"]

        if generate_venv:
            print("Generating VENV Data")
            cmd = 'python -m venv ' + local_envpath + self._model_name + "/" + self._model_version
            p = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
            print(p.stdout.decode())
        else:
            return "Finished downloading"
    

            