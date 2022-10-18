from logging import exception
import os

class Settings:
    def __init__(self):
        self._base_path
        self._premade_main_code_data
        self._premade_function_code_data
        self._premade_requirements_data
        self._premade_documentation_data
        self._enviroment_name
        self._package_version
        self._base_url
        self._username
        self._token

    ### Base path that will be used by the system to work with the system and work from ###
    @property
    def Base_path(self):
        """
        :type: string
        """
        return self._base_path

    @Base_path.setter
    def Base_path(self, value):
        """
        :type: string
        """
        try:
            isDirectory = os.path.isdir(value)
            if isDirectory == True:
                self._base_path = value
        except Exception as ex:
            print(ex, "Given path is not a directory")

    ### Premade code that can be used when not using custom code ###
    @property
    def Premade_main_code_data(self):
        """
        :type: string
        """
        return self._premade_main_code_data

    @Premade_main_code_data.setter
    def Premade_main_code_data(self, value):
        """
        :type: string
        """
        self._premade_main_code_data = value

    ### Premade function code that can be used when not using custom code ###
    @property
    def Premade_function_code_data(self):
        """
        :type: string
        """
        return self._premade_function_code_data

    @Premade_function_code_data.setter
    def Premade_function_code_data(self, value):
        """
        :type: string
        """
        self._premade_function_code_data = value

    ### Premade requirements list that can be used when not using custom code ###
    @property
    def Premade_requirements_data(self):
        """
        :type: string
        """
        return self._premade_requirements_data

    @Premade_requirements_data.setter
    def Premade_requirements_data(self, value):
        """
        :type: string
        """
        self._premade_requirements_data = value

    ### Premade documentation that can be used when not using custom code ###
    @property
    def Premade_documentation_data(self):
        """
        :type: string
        """
        return self._premade_documentation_data

    @Premade_documentation_data.setter
    def Premade_documentation_data(self, value):
        """
        :type: string
        """
        self._premade_documentation_data = value

    @property
    def Enviroment_name(self):
        """
        :type: string
        """
        return self._enviroment_name

    @Enviroment_name.setter
    def Enviroment_name(self, value):
        """
        :type: string
        """
        self._enviroment_name = value

    @property
    def Package_version(self):
        """
        :type: string
        """
        return self._package_version

    @Package_version.setter
    def Package_version(self, value):
        """
        :type: string
        """
        self._package_version = value

    @property
    def Base_url(self):
        """
        :type: string
        """
        return self._base_url

    @Base_url.setter
    def Base_url(self, value):
        """
        :type: string
        """
        self._base_url = value

    @property
    def Username(self):
        """
        :type: string
        """
        return self._username

    @Username.setter
    def Username(self, value):
        """
        :type: string
        """
        self._username = value

    @property
    def Token(self):
        """
        :type: string
        """
        return self._token

    @Token.setter
    def Token(self, value):
        """
        :type: string
        """
        self._token = value
