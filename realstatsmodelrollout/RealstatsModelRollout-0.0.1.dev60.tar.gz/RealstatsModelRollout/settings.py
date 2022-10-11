from logging import exception
import os

class settings:
    def __init__(self):
        self._base_path
        self._premade_main_code_data
        self._premade_function_code_data
        self._premade_requirements_data
        self._premade_documentation_data
        self._enviroment_name
        self._package_version

    ### Base path that will be used by the system to work with the system and work from ###
    @property
    def base_path(self):
        """
        :type: string
        """
        return self._base_path
    
    @base_path.setter
    def base_path(self, value):
        """
        :type: string
        """
        try:
            isDirectory = os.path.isdir(value)
            if isDirectory == True:
                self._base_path = value
        except Exception as ex:
            print(ex, "Given path is not correct")

    ### Premade code that can be used when not using custom code ###
    @property
    def premade_main_code_data(self):
        """
        :type: string
        """
        return self._premade_main_code_data
    
    @premade_main_code_data.setter
    def premade_main_code_data(self, value):
        """
        :type: string
        """
        self._premade_main_code_data = value

    ### Premade function code that can be used when not using custom code ###
    @property
    def premade_function_code_data(self):
        """
        :type: string
        """
        return self._premade_function_code_data
    
    @premade_function_code_data.setter
    def premade_function_code_data(self, value):
        """
        :type: string
        """
        self._premade_function_code_data = value

    ### Premade requirements list that can be used when not using custom code ###
    @property
    def premade_requirements_data(self):
        """
        :type: string
        """
        return self._premade_requirements_data
    
    @premade_requirements_data.setter
    def premade_requirements_data(self, value):
        """
        :type: string
        """
        self._premade_requirements_data = value

    ### Premade documentation that can be used when not using custom code ###
    @property
    def premade_documentation_data(self):
        """
        :type: string
        """
        return self._premade_documentation_data
    
    @premade_documentation_data.setter
    def premade_documentation_data(self, value):
        """
        :type: string
        """
        self._premade_documentation_data = value


    @property
    def enviroment_name(self):
        """
        :type: string
        """
        return self._enviroment_name
    
    @enviroment_name.setter
    def enviroment_name(self, value):
        """
        :type: string
        """
        self._enviroment_name = value

    @property
    def package_version(self):
        """
        :type: string
        """
        return self._package_version
    
    @package_version.setter
    def package_version(self, value):
        """
        :type: string
        """
        self._package_version = value
