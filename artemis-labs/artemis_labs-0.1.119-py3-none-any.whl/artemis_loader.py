'''
This loads in an Artemis script and generates the artemis version of this script
'''

#pylint: disable=line-too-long
#pylint: disable=anomalous-backslash-in-string
#pylint: disable=consider-using-with
#pylint: disable=trailing-whitespace
#pylint: disable=too-few-public-methods
#pylint: disable=too-many-arguments
#pylint: disable=too-many-locals
#pylint: disable=too-many-branches
#pylint: disable=too-many-statements

from typing import List
import os
import sys
import subprocess

from .artemis_line_transformer import LineTransformer

class ArtemisLoader:
    '''
    This class features static methods to process an Artemis script
    and writes the processed version to file
    '''

    @staticmethod
    def process_script(runner_path : str, launch_command : str, code_path : str, project_files : List[str], is_entry_point=False, project_name="", project_path="", dev=False, launch=True) -> str:
        '''
        This function turns a script into the Artemis version and writes it to file
        :param runner_path: Path to artemis_labs_base
        :param launch_command: Python installation to use. Default: python
        :param code_path: Path to script to process
        :param project_files: List of files to include in the project
        :param dev: Whether to run in dev mode (local or not)
        :param launch: Whether to launch browser (set to false when reloading)
        :return: The path to the Artemis version of the script
        '''

        # Read contents of decorated.py
        try:
            with open(code_path, encoding='utf-8') as file:
                original_contents = file.read()
            original_contents_lines = original_contents.split('\n')
        except Exception as exception: # pylint: disable=broad-except
            print(f'[Artemis] Error: Could not read file: {code_path}')
            print(exception)
            return None

        # Escape code path
        code_path = code_path.replace('\\', '/')

        if dev:
            original_contents_lines.insert(0, 'atexit.register(Artemis.waiter)')
            if not is_entry_point:
                original_contents_lines.insert(0, f'Artemis.init("{runner_path}", "{launch_command}", "{code_path}", "", {launch}, {dev})')
            else:
                original_contents_lines.insert(0, f'Artemis.init("{runner_path}", "{launch_command}", "{code_path}", "{project_path}", {launch}, {dev})')
            original_contents_lines.insert(0, 'import atexit')
            original_contents_lines.insert(0, 'from artemis_labs.artemis_tester import Artemis')
            original_contents_lines.insert(0, 'sys.path.append(\'./artemis_labs/src/\')')
            original_contents_lines.insert(0, 'import sys')
            original_contents_lines.insert(0, 'from time import sleep')
        else:
            original_contents_lines.insert(0, 'atexit.register(Artemis.waiter)')
            if not is_entry_point:
                original_contents_lines.insert(0, f'Artemis.init("{runner_path}", "{launch_command}", "{code_path}", "", {launch}, {dev})')
            else:
                original_contents_lines.insert(0, f'Artemis.init("{runner_path}", "{launch_command}", "{code_path}", "{project_path}", {launch}, {dev})')
            original_contents_lines.insert(0, 'import atexit')
            original_contents_lines.insert(0, 'from artemis_labs.artemis import Artemis')
            original_contents_lines.insert(0, 'from time import sleep')

        # Regular imports
        regular_import_dict = {}
        for project_file in project_files:
            project_file_module_name = os.path.splitext(os.path.basename(project_file))[0]
            regular_import_dict[project_file_module_name] = project_file

        # Process imports
        for i, line in enumerate(original_contents_lines):

            # Store original line
            original_line = line

            # Trim line
            line = line.strip()

            # Check if import
            if line.startswith('import'):

                # Get module name
                module_name = line[line.find('import') + 6:].strip()
                module_name = module_name.split(' ')[0].strip()

                # Get only module name (assuming first part is module)
                if '.' in module_name:
                    if module_name.startswith('.'):
                        module_name = module_name[: module_name[1:].find('.') + 1]
                    else:
                        module_name = module_name[: module_name.find('.')]

                # Check if local import
                if module_name.startswith('.'):
                    continue

                # Handle regular import
                if module_name in regular_import_dict:
                    print('[Artemis] Found regular import: ' + module_name)
                    original_contents_lines[i] = original_line.replace(module_name, module_name + "_artemis", 1)
                    continue

            # Check if from-style import
            if line.startswith('from'):

                # Get module name
                module_name = line[line.find('from') + 4:].strip()
                module_name = module_name.split(' ')[0]

                # Get only module name (assuming first part is module)
                if '.' in module_name:
                    if module_name.startswith('.'):
                        module_name = module_name[: module_name[1:].find('.') + 1]
                    else:
                        module_name = module_name[: module_name.find('.')]

                # Check if local import
                if module_name.startswith('.'):
                    if module_name[1:] in regular_import_dict:
                        original_contents_lines[i] = line.replace(module_name, '.' + module_name + "_artemis", 1)
                    continue

                # Handle regular import
                if module_name in regular_import_dict:
                    original_contents_lines[i] = line.replace(module_name, module_name + "_artemis", 1)
                    continue

        # Transform lines
        transformed_contents_lines = LineTransformer.transform_script(original_contents_lines, is_entry_point=is_entry_point, project_name=project_name, dev=dev)

        # Dump back to file
        new_path = code_path.strip()[:-3] + "_artemis.py"

        # Remove file if it exists
        if os.path.isfile(new_path):
            os.remove(new_path)

        # Write to file
        with open(new_path, 'w', encoding='utf-8') as file:
            for line in transformed_contents_lines:
                file.write(line + '\n')

        # Hide file
        if os.name == 'nt':
            subprocess.check_call(["attrib","+H", new_path])

        return new_path

    @staticmethod
    def load_imports(script_path : str) -> List[str]:
        '''
        This function processes all the @import statements from the provided script,
        and returns the contents of each file in a list
        :param script_path: Path to script to process
        :return: List of contents of each imported file
        '''

        import_files = []
        with open(script_path, 'r', encoding='utf-8') as script_file:

            # Load script
            script_lines = script_file.readlines()

            # Process imports
            for line in script_lines:

                # Get import
                if '@import' in line:

                    # Load import
                    import_file = line[line.find('@import') + 7:].strip()

                    # Escape backslashes
                    import_file = import_file.replace('\\', '\\\\')

                    # Handle relative import
                    if import_file.startswith('./'):
                        import_file = os.path.join(os.getcwd(), import_file[2:])

                    # Report import
                    print(f'[Artemis] Importing {import_file}')

                    # Load import if it exists
                    if os.path.exists(import_file):
                        with open(import_file, 'r', encoding='utf-8') as import_file:

                            # Load import file content
                            try:
                                import_file_content = import_file.read()
                            except Exception as exception: # pylint: disable=broad-except
                                print(f'[Artemis] Failed to import {import_file}: {exception}') # pylint: disable=broad-except
                                continue

                            # Store import file content
                            import_files.append(import_file_content)

        return import_files

    @staticmethod
    def clear_config_files() -> None:
        '''
        This clears old config files
        '''

        # Get directory of this file
        artemis_dir = os.path.dirname(os.path.realpath(__file__))

        # Ensure artemis_labs dir exists
        artemis_labs_dir = os.path.join(artemis_dir, 'temp')
        if not os.path.exists(artemis_labs_dir):
            os.mkdir(artemis_labs_dir)

        # Clear out old config files
        for file in os.listdir(artemis_labs_dir):
            try:
                # Remove if it is a file and name starts with artemis_labs_temp
                if os.path.isfile(os.path.join(artemis_labs_dir, file)) and file.startswith('artemis_labs_temp'):
                    os.remove(os.path.join(artemis_labs_dir, file))
            except OSError:
                print('[Artemis] Failed to remove old config file: ' + file)
                print('[Artemis] Artemis likely already in use...')
                sys.exit(1)

    @staticmethod
    def setup_config_files(config_files : List[str]) -> None:
        '''
        This ensures config temp dir is created and loaded with imports
        :param config_files: List of config files to load
        '''

        # Get directory of this file
        artemis_dir = os.path.dirname(os.path.realpath(__file__))

        # Ensure artemis_labs dir exists
        artemis_labs_dir = os.path.join(artemis_dir, 'temp')
        if not os.path.exists(artemis_labs_dir):
            os.mkdir(artemis_labs_dir)

        # Create temp copies of config files
        for i, config_file_content in enumerate(config_files):
            config_path = os.path.join(artemis_labs_dir, f'artemis_labs_temp_config_{i}.py')
            with open(config_path, 'w', encoding='utf-8') as file:
                file.write(config_file_content)
