from abc import ABC, abstractmethod
from runfalconbuildtools.env_utils import get_env_variable
from runfalconbuildtools.file_utils import create_file, add_execution_permission_to_file, create_dir_if_not_exists
from runfalconbuildtools.command_line_executor import CommandLineExecutor
from runfalconbuildtools.logger import Logger

class BaseBuilder(ABC):

    executor:CommandLineExecutor = CommandLineExecutor()
    working_dir:str = get_env_variable('WORKING_DIR', './working_dir')

    def get_app_directory(self):
        return self.working_dir + '/' + self.get_app_name()

    def get_build_file_dir(self) -> str:
        return self.working_dir + '/scripts'

    def get_build_file_full_name(self) -> str:
        return self.get_build_file_dir() + '/' + self.get_script_file_name()

    def create_build_script(self):
        build_script:str = self.get_build_script()
        script_file:str = self.get_build_file_full_name()
        create_dir_if_not_exists(self.get_build_file_dir())
        create_file(script_file, build_script)
        add_execution_permission_to_file(script_file)

    def __is_error_output__(self, output:str) -> bool:
        return output != None and output.find('\n => ERROR ') >= 0

    def __extract_error__(self, output:str) -> str:
        index:int = output.find('\n => ERROR ')
        if index >= 0:
            return output[index:len(output)]
        return None

    def __run_build__(self):
        self.create_build_script()
        
        self.executor.execute(self.get_build_file_full_name())
        if self.executor.return_code != 0 or self.__is_error_output__(self.executor.stdout):
            output_error:str = self.__extract_error__(self.executor.stdout)
            if output_error != None:
                raise Exception('Error running build script [1].\n{}'.format(output_error))
            else:
                raise Exception('Error running build script [2].\nCODE:{code}\nERROR\n{error}\nOUTPUT\n{output}'.format( \
                    code = self.executor.return_code, \
                    error = self.executor.stderr + ('\n' + output_error if output_error != None else ''), \
                    output = self.executor.stdout[len(self.executor.stdout) - 5000:len(self.executor.stdout)] if self.executor.stdout != None else 'None'\
                ))

        self.get_loger().info(self.executor.stdout)

    def build(self):
        self.get_loger().info("Validating ...")
        self.validate()
        self.get_loger().info("Build started ...")
        self.clean_output_directories()
        self.get_loger().info("Getting source artifacts ...")
        self.get_source_artifacts()
        self.get_loger().info("Running build ...")
        self.__run_build__()
        self.get_loger().info("Build ended.")

    @abstractmethod
    def get_app_name(self) -> str:
        pass

    @abstractmethod
    def validate(self) -> str:
        pass

    @abstractmethod
    def get_script_file_name(self) -> str:
        pass

    @abstractmethod
    def get_build_script(self) -> str:
        pass
  
    @abstractmethod
    def clean_output_directories(self):
        pass

    @abstractmethod
    def get_source_artifacts(self):
        pass

    @abstractmethod
    def get_loger(self) -> Logger:
        pass
