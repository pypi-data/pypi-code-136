'''
This is the core Artemis code which executes Artemis commands and
connects Artemis via websocket to the browser
'''
# pylint: disable=line-too-long
# pylint: disable=wildcard-import
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-arguments
# pylint: disable=too-many-public-methods
# pylint: disable=too-many-statements
# pylint: disable=broad-except
# pylint: disable=consider-using-with
# pylint: disable=too-many-branches
# pylint: disable=too-many-locals
# pylint: disable=bare-except
# pylint: disable=protected-access
# pylint: disable=import-error
# pylint: disable=duplicate-code
# pylint: disable=trailing-whitespace

import json
from time import sleep
import os
import subprocess
from collections.abc import Callable
import time
import inspect

from typing import Any
from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from .artemis_socket import ArtemisSocket
from .artemis_config_manager import ArtemisConfigManager
from .artemis_converter import ArtemisConverter
from .config import * # pylint: disable=unused-wildcard-import
from .artemis_token_parser import TokenParser
from .artemis_helper import ArtemisHelper

# Insert current dir into sys.path
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)))

class Artemis:
    '''
    This class is spawned inside the user's code and is the API
    to communicate with the browser
    '''

    PORT = 8081
    APP_PATH = "app.json"
    initialized = False

    @staticmethod
    def init(runner_path="", launch_command = "", code_path="", project_path="", launch=True, dev=False):
        '''
        Initialize Artemis class, establish websocket, and start app
        :param runner_path: Path to artemis_labs_base
        :param launch_command: How they launched their program. Example: python
        :param code_path: Path to their script
        :param launch: Whether or not we're spawning a new browser
        :param dev: Whether or not we're in dev mode
        '''

        print("Initializing Artemis Tester")
        # Only init if we've already init
        if Artemis.initialized:
            code_path = os.path.join(Artemis.cur_dir, code_path)
            with open(code_path, 'r', encoding='utf-8') as file:
                init_packet = { 'type' : 'init', 'file_name' : os.path.basename(code_path), 'state' : file.read(), 'settings' : json.dumps(Artemis.settings) }
                out_str = json.dumps(init_packet)
                out_str  = out_str.replace("<", "&lt;").replace(">", "&gt;")
                Artemis.artemis_socket.send(out_str)
            return

        Artemis.project_path = project_path
        Artemis.initialized = True

        # Load config modules
        initialize_config()

        # Command line paths
        Artemis.runner_path = runner_path
        Artemis.launch_command = launch_command
        Artemis.dev = dev

        # Regular execution lock -> wait for continue
        Artemis.on_lock = False
        Artemis.on_lock_content = ''

        # Query lock -> synchronous queries
        Artemis.query_lock = False
        Artemis.query_lock_content = ''

        # Submit lock -> wait for submit
        Artemis.submit_lock = False
        Artemis.submit_content = ''

        # Fast Forward
        Artemis.fast_forward = False

        # Next lock -> wait for reload
        Artemis.next_lock = False

        # Registered callbacks
        Artemis.callback_map = {}

        # Async queries
        Artemis.query_callback_queue = []

        # Execution mode -> "code" = comment based mode
        Artemis.mode = "code"

        # Critical paths
        Artemis.code_path = code_path
        Artemis.cur_dir = ""

        # Socket connection
        Artemis.artemis_socket = ArtemisSocket(Artemis.callback_handler)

        # Load runtime settings
        Artemis.runtime_settings = get_settings()

        # Load settings
        Artemis.settings = {}
        try:
            base_folder = os.path.dirname(os.path.realpath(__file__))
            config_path = os.path.join(base_folder, "artemis_settings.json")
            with open(config_path, "r", encoding='utf-8') as file:
                Artemis.settings = json.load(file)
        except Exception as exception:
            print(exception)
            print('[Artemis] Exception: Unable to load artemis_settings.json')
            os._exit(1)

        # JSON GUI dump
        Artemis.app = {}

        # Load GUI dump
        if Artemis.mode == 'gui':
            try:
                with open(Artemis.APP_PATH, "r", encoding='utf-8') as file:
                    Artemis.app = json.load(file)
            except Exception as exception:
                print(exception)
                print('[Artemis] Exception: Unable to load app.json')
                Artemis.app = {}

        # Launch Artemis
        Artemis.run(launch)

    @staticmethod
    def callback_handler(message : str) -> None:
        '''
        Process message from websocket
        :param message: Text form of JSON packet sent over websocket
        :return: None
        '''
        # Skip pings
        message = json.loads(message)
        if message['type'] != 'ping':

            # Handle query and callback responses separately
            if message['type'] == 'query':
                if len(Artemis.query_callback_queue) > 0:
                    Artemis.query_callback_queue[0](message)
                    Artemis.query_callback_queue.pop(0)
            elif message['type'] == 'submit':
                try:
                    Artemis.submit_content = message['content']
                    Artemis.submit_lock = False
                except Exception as exception:
                    print('[Artemis] Exception: Unable to parse submit message: ')
                    print(message)
                    print('[Artemis] Error: ')
                    print(exception)
                    return
            elif message['type'] == 'next':
                Artemis.next_lock = False
            elif message['type'] == 'fast-forward':
                Artemis.fast_forward = True
            elif message['type'] == 'exit':
                os._exit(1) # pylint: disable=W0212
            elif message['type'] == 'archive':
                archive_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'htdocs/launcher_code_archive.html')
                archive = open(archive_path, 'r', encoding='utf8', errors='ignore').read()
                script = "<script>\n" + "archive = " + json.dumps(message['archive']) + ";\n</script>"
                archive = archive.replace("<!-- CODE ARCHIVE GOES HERE -->", script).replace("let archiveMode = false;", "let archiveMode = true;").replace("let archive = [];", "")
                cur_time = time.time()
                cur_time_ms = int(cur_time * 1000)
                with open(os.path.join(os.getcwd(), f'archive_{cur_time_ms}.html'), 'w', errors='ignore', encoding='utf-8') as file:
                    file.write(archive)
            elif message['type'] == 'reload':
                dev_arg = ''
                if Artemis.dev:
                    dev_arg = ' dev'
                if Artemis.cur_dir != '':
                    os.chdir(Artemis.cur_dir)
                subprocess.Popen(['artemis_labs', Artemis.project_path, Artemis.launch_command , dev_arg, 'nolaunch'], creationflags=subprocess.CREATE_NO_WINDOW)
                os._exit(1) # pylint: disable=W0212
            elif message['type'] == 'open-file':

                # Fix local file
                if message['content'].startswith('./'):
                    message["content"] = os.path.join(Artemis.cur_dir, message["content"][2:])

                # Fix space char
                message["content"] = message["content"].replace("%20", " ")

                # Check if we have a file or a folder
                is_dir = os.path.isdir(message['content'])
                is_file = os.path.isfile(message['content'])

                if os.name == 'nt':

                    # Open file or folder
                    if is_file:
                        print('[Artemis] Opening file: ' + message['content'])
                        message['content'] = message['content'].replace('%20', ' ')
                        if message['content'].startswith('./'):
                            message['content'] = message['content'][2:]
                            message['content'] = os.path.join(Artemis.cur_dir, message['content'])
                        open_file_command = "\"" + message["content"].replace("\\","\\\\").strip() + "\""

                        os.popen(open_file_command, 'r')
                    elif is_dir:
                        print('[Artemis] Opening dir: ' + 'start \"\" "' + message["content"] + '"')
                        os.system('start \"\" "' + message["content"] + '" /MAX')
                else:
                    print("[Artemis] File open not supported on Linux")
            else:
                callback_tag = message["type"] + "-" + message["attribute"] + "-" + message["name"]
                if callback_tag in Artemis.callback_map:
                    Artemis.callback_map[callback_tag](json.loads(message["state"]))
                else:
                    print('Callback not found: ', message)

    @staticmethod
    def is_connected() -> bool:
        '''
        Check if Artemis websocket is alive
        :return: If Artemis websocket is alive
        '''
        return Artemis.artemis_socket.is_connected()

    @staticmethod
    def on_event(action : str, name : str, callback : Callable[[Dict], None]) -> None:
        '''
        Enqueue callback to receive message when certain callback is triggered
        :param action:
        :param name:
        :param callback:
        :return:
        '''
        on_packet = {}
        on_packet["type"] = "callback"
        on_packet["attribute"] = action
        on_packet["name"] = name
        callback_tag = on_packet["type"] + "-" + on_packet["attribute"] + "-" + on_packet["name"]
        Artemis.callback_map[callback_tag] = callback
        Artemis.artemis_socket.send(json.dumps(on_packet))

    @staticmethod
    def update(element_name : str, new_value : str) -> None:
        '''
        Send update message to update element with name element_name with new_value
        :param element_name: Name of element to update
        :param new_value: Value to update element with
        :return: None
        '''
        update_packet = {}
        update_packet["type"] = "update"
        update_packet['name'] = element_name
        update_packet['value'] = new_value
        Artemis.artemis_socket.send(json.dumps(update_packet))

    @staticmethod
    def navigate(page_name : str) -> None:
        '''
        Change GUI to page page_name
        :param page_name: Page to change GUI to
        :return: None
        '''
        navigate_packet = {}
        navigate_packet["type"] = "navigate"
        navigate_packet['pageName'] = page_name
        Artemis.artemis_socket.send(json.dumps(navigate_packet))

    @staticmethod
    def query(callback : Callable[[Dict], None]) -> None:
        '''
        Send request to browser GUI for query, and append calllback
        to query_callback_queue so that this function gets called once
        we receive the query response
        :param callback: Async func to call when we get the callback
        :return:
        '''
        query_packet = {}
        query_packet["type"] = "query"
        Artemis.query_callback_queue.append(callback)
        Artemis.artemis_socket.send(json.dumps(query_packet))

    @staticmethod
    def query_unlock(content : Dict) -> None:
        '''
        Unlock query_lock, which suspends program while wiating for async query
        :param content: Dictionary response from browser containing GUI state
        :return: None
        '''
        Artemis.query_lock_content = content
        Artemis.query_lock = False

    @staticmethod
    def query_wait() -> Dict:
        '''
        Synchronously query GUI. This sends query request to browser,
        and then waits for response. When response is received, it will
        unlock the query_lock and fetch the response from query_lock_content
        :return: Dictionary containing the GUI state
        '''
        Artemis.query_lock = True
        Artemis.query(Artemis.query_unlock)
        while Artemis.query_lock:
            sleep(0.1)
        return_content = Artemis.query_lock_content
        Artemis.query_lock_content = ''
        return return_content

    @staticmethod
    def on_unlock(content : Dict) -> None:
        '''
        Unlock the generic on_lock lock and store the content of the GUI
        response. This is called when a synchronous wait is placed, locking the
        GUI until a certain callback is tripped
        :param content: Dictionary containing GUI state
        :return: None
        '''
        Artemis.on_lock_content = content
        Artemis.on_lock = False

    @staticmethod
    def wait(action : str, name : str) -> Dict:
        '''
        Place callback on GUI and synchronously wait until it occurs.
        Once it occurs, the on_unlock function will unlock on_lock,
        allowing it to proceed and return the GUI response
        :param action:
        :param name:
        :return:
        '''
        Artemis.on_lock = True
        Artemis.on_event(action, name, Artemis.on_unlock)
        while Artemis.on_lock:
            sleep(0.1)
        return_content = Artemis.on_lock_content
        Artemis.on_lock_content = ''
        return return_content

    @staticmethod
    def create_input(line_start : int, line_end : int, name : str, comment : str) -> None:
        '''
        Send request to GUI to create an input element
        :param line_start: Line where the input element starts in code
        :param line_end: Line where the input element ends in the code
        :param name: Name of the input element
        :param comment: Extra data
        :return: None
        '''
        caller_module = os.path.basename(inspect.stack()[1].filename)[:-11] + ".py"
        input_packet = json.dumps(
        {
                "type": "create",
                "element": "input",
                'line_start' : line_start,
                'line_end': line_end,
                'name' : name,
                'comment': comment,
                'caller_module': caller_module
        }
        )

        Artemis.artemis_socket.send(input_packet)
        Artemis.submit_lock = True
        Artemis.runtime_delay()

    @staticmethod
    def hide_input() -> None:
        '''
        Send request to GUI to hide the submit button associated with the input
        and to make the input readonly
        :return:  None
        '''
        Artemis.fast_forward = False
        Artemis.artemis_socket.send(json.dumps({'type': 'hide', "element": "input"}))

    @staticmethod
    def wait_for_input() -> Dict:
        '''
        Synchronously wait until response from input is received. Then return that response
        :return: Dictionary containing GUI response after input submitted
        '''
        Artemis.artemis_socket.send(json.dumps({"type" : "wait-for-input"}))
        while Artemis.submit_lock:
            sleep(0.1)
        return Artemis.submit_content

    @staticmethod
    def preprocess(value : Any, component_type : str, named_args=[]) -> Tuple: # pylint: disable=dangerous-default-value
        '''
        This function applies custom logic to the decorated element
        to create something from it, such as graphs, tables, etc, and
        serializes that data in a string form which may be transmitted to
        the browser
        :param value: Value of decorated element
        :param component_type: Component type of decorator
        :param named_args: Named args supplied with decorator
        :return: None
        '''

        # Skip for built-in types
        built_in_types = ['number', 'heading', 'table', 'image', 'doc', 'markdown', 'card', 'samecard']
        if component_type in built_in_types:
            return value, component_type

        # Convert named args into a dictionary
        named_args_dict = {}
        for named_arg in named_args:
            named_args_dict[named_arg[0]] = named_arg[1]

        # Call custom callback function
        try:

            # Get custom function
            func = ArtemisConfigManager.get_function(component_type)

            # Call custom function
            evaluated_resp = func(value, named_args_dict)
            if evaluated_resp is None:
                return (None, "")
            component_type = evaluated_resp[0]
            value = evaluated_resp[1]
        except Exception as exception:
            print(exception)
            return (None, "")

        return value, component_type

    @staticmethod
    def runtime_delay():
        '''
        Delays based on runtime settings.
        This is called after creating outputs or inputs
        '''
        if 'delay' in Artemis.runtime_settings:
            try:
                sleep(float(Artemis.runtime_settings['delay']))
            except Exception as exception:
                print('[Artemis] Error: Delay must be a number')
                print('[Artemis] Exception: ', exception)

    @staticmethod
    def create_output(line_start : int, line_end : int, name : str, value : Any, component_type : str, comment : str, named_args=[]) -> None: # pylint: disable=dangerous-default-value
        '''
        Creates output element from value.
        :param line_start: Start line of output
        :param line_end: End line of output
        :param name: Name of output variable
        :param value: Value of output variable
        :param component_type: Component type of output
        :param comment: Extra data
        :param named_args: Supplied named_args
        :return: None
        '''
        caller_module = os.path.basename(inspect.stack()[1].filename)[:-11] + ".py"
        value = ArtemisConverter.convert_type(value, component_type)
        value, component_type = Artemis.preprocess(value, component_type, named_args)

        if value is None:
            return

        try:
            test = json.dumps({ 'test' : value }) # pylint: disable=unused-variable
        except Exception as exception: # pylint: disable=unused-variable
            value = str(value)

        value = json.dumps({
            "type": "create",
            "element": "output",
            'line_start': line_start,
            'line_end': line_end,
            'name' : name,
            'value': value,
            "componentType" : component_type,
            "comment" : comment,
            'caller_module' : caller_module
        })
        Artemis.artemis_socket.send(value)
        if component_type != 'card':
            Artemis.runtime_delay()

    @staticmethod
    def wait_for_next(line_number=-1) -> None:
        '''
        Synchonrously wait until continue button pressed
        :return: None
        '''
        Artemis.next_lock = True
        Artemis.artemis_socket.send(json.dumps({"type" : "wait-for-next", "line-number" : line_number }))
        while Artemis.next_lock and not Artemis.fast_forward:
            sleep(0.1)

    @staticmethod
    def delay(delay_time=1) -> None:
        '''
        Synchonrously wait for delay
        :return: None
        '''
        sleep(delay_time)

    # Test thread
    @staticmethod
    def tester() -> None:
        '''
        Test thread
        :return: None
        '''

        # Get working directory
        working_directory = os.getcwd()
        testing_script_path = os.path.join(working_directory, Artemis.launch_command)

        # Check to ensure test script exists
        if not os.path.exists(testing_script_path):
            print(testing_script_path)
            print("[Artemis] Error: Test script not found")
            return

        # Get test script name
        test_script_name = os.path.basename(testing_script_path).split('.')[0]

        # Create test script directory
        test_script_directory = os.path.join(working_directory, test_script_name + "_artemis")
        if not os.path.exists(test_script_directory):
            os.mkdir(test_script_directory)

        # Clear test script directory
        for file in os.listdir(test_script_directory):
            os.remove(os.path.join(test_script_directory, file))

        # Read test script
        with open(testing_script_path, 'r', encoding='utf-8') as file:
            script_lines = file.readlines()

        # Output log
        output_log = []
        def log_output(output):
            output_log.append(output + '\n')
            #print(output)

        # Run Test
        save_ctr = 0
        item = None
        item_selector = ''
        for i, line in enumerate(script_lines):

            # Preprocess line
            line = line.strip()

            # SKip empty lines or comments
            if line == '' or line.startswith('#'):
                continue

            # Tokenize line
            tokens = TokenParser.tokenify_line(line)
            tokens = [token.strip() for token in tokens]
            tokens[0] = tokens[0].lower()

            # Preprocess tokens
            command = tokens[0]
            arg = ''
            if len(tokens) > 1:
                arg = tokens[1]
            extra_arg = ''
            if len(tokens) > 2:
                for j in range(2, len(tokens)):
                    extra_arg += tokens[j] + ' '

            # Check for sleep command
            if command == 'sleep':
                log_output(f'[Success] Slept for {arg} seconds')
                sleep(float(arg))
                continue

            # Check for get command
            if command == 'select':
                item_selector = arg
                try:
                    item = WebDriverWait(Artemis.driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, item_selector))
                    )
                    log_output(f'[Success] Found element: {item_selector}')
                except:
                    log_output(f'[Error] Command {command} failed - Line {i} - Element not found: {item_selector}')
                continue

            # Check in case print, type, click, or screenshot used second arg
            second_arg_commands = ['print', 'click', 'rightclick', 'doubleclick', 'screenshot', 'clickat', 'moveto']
            if command in second_arg_commands and arg != '':
                item_selector = arg + ' '  + extra_arg
                item_selector = item_selector.rstrip()
                try:
                    item = WebDriverWait(Artemis.driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, item_selector))
                    )
                    log_output(f'[Success] Found element: {item_selector}')
                except:
                    log_output(f'[Error] Command {command} failed - Line {i} - Element not found: {item_selector}')

            # Check in case type used extra_arg
            if command == 'type' and extra_arg != '':
                item_selector = extra_arg
                try:
                    item = WebDriverWait(Artemis.driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, item_selector))
                    )
                    log_output(f'[Success] Found element: {item_selector}')
                except:
                    log_output(f'[Error] Command {command} failed - Line {i} - Element not found: {item_selector}')

            # Check for print command
            if command == 'print' and item is not None:
                try:
                    log_output(f'[Success] Source for {item_selector} : {item.get_attribute("outerHTML")}')
                except Exception as exception:
                    exception_text = str(exception).replace("\n", ' ')
                    exception_text = exception_text[:exception_text.find('(Session info')].strip()
                    log_output(f'[Error] Command {command} failed - Line {i} - Exception: {exception_text}')
                continue
            if item is None:
                log_output(f'[Error] Command {command} failed - Line {i}: No item selected')
                continue

            # Check for click command
            if command == 'click' and item is not None:
                try:
                    item.click()
                    sleep(0.05)
                except Exception as exception:
                    exception_text = str(exception).replace("\n", ' ')
                    exception_text = exception_text[:exception_text.find('(Session info')].strip()
                    log_output(f'[Error] Command {command} failed - Line {i} - Exception: {exception_text}')
                log_output(f'[Success] Clicked item {item_selector}')
                continue
            if item is None:
                log_output(f'[Error] Command {command} failed - Line {i}: No item selected')
                continue

            # Check for rightclick command
            if command == 'rightclick' and item is not None:
                try:
                    action = ActionChains(Artemis.driver)
                    action.context_click(item).perform()
                    sleep(0.05)
                except Exception as exception:
                    exception_text = str(exception).replace("\n", ' ')
                    exception_text = exception_text[:exception_text.find('(Session info')].strip()
                    log_output(f'[Error] Command {command} failed - Line {i} - Exception: {exception_text}')
                log_output(f'[Success] Clicked item {item_selector}')
                continue

             # Check for doubleclick command
            if command == 'doubleclick' and item is not None:
                try:
                    action = ActionChains(Artemis.driver)
                    action.double_click(item).perform()
                    sleep(0.05)
                except Exception as exception:
                    exception_text = str(exception).replace("\n", ' ')
                    exception_text = exception_text[:exception_text.find('(Session info')].strip()
                    log_output(f'[Error] Command {command} failed - Line {i} - Exception: {exception_text}')
                log_output(f'[Success] Clicked item {item_selector}')
                continue

            # Check for clickat command
            if command == 'clickat' and item is not None:
                try:
                    action = ActionChains(Artemis.driver)
                    action.move_to_element(item).click().perform()
                    sleep(0.05)
                except Exception as exception:
                    exception_text = str(exception).replace("\n", ' ')
                    exception_text = exception_text[:exception_text.find('(Session info')].strip()
                    log_output(f'[Error] Command {command} failed - Line {i} - Exception: {exception_text}')
                log_output(f'[Success] Clicked item {item_selector}')
                continue

            # Check for moveto command
            if command == 'moveto' and item is not None:
                try:
                    action = ActionChains(Artemis.driver)
                    action.move_to_element(item).perform()
                    sleep(0.05)
                except Exception as exception:
                    exception_text = str(exception).replace("\n", ' ')
                    exception_text = exception_text[:exception_text.find('(Session info')].strip()
                    log_output(f'[Error] Command {command} failed - Line {i} - Exception: {exception_text}')
                log_output(f'[Success] Move to item {item_selector}')
                continue

            # Check for type command
            if command == 'type' and item is not None:

                log_output(f'[Success] Typed {arg} in item {item_selector}')
                try:
                    item.send_keys(arg)
                    sleep(0.05)
                except Exception as exception:
                    exception_text = str(exception).replace("\n", ' ')
                    exception_text = exception_text[:exception_text.find('(Session info')].strip()
                    log_output(f'[Error] Command {command} failed - Line {i} - Exception: {exception_text}')
                continue
            if item is None:
                log_output(f'[Error] Command {command} failed - Line {i}: No item selected')
                continue

            # Check for screenshot
            if command == 'screenshot' and item is not None:
                sleep(0.15)
                log_output(f'[Info] Saving screenshot of item {item_selector} - screenshot {save_ctr}')
                item.screenshot(os.path.join(test_script_directory, f'{save_ctr}.png'))
                while not os.path.exists(os.path.join(test_script_directory, f'{save_ctr}.png')):
                    sleep(0.05)
                save_ctr += 1
                continue

            # Check for scroll
            if command == 'scroll' and arg.strip() != '' and extra_arg.strip() != '':
                scroll_dist = float(extra_arg)
                arg = arg.strip()
                Artemis.driver.execute_script(f'qs("{arg}").scrollTop += {scroll_dist};')
                sleep(0.05)
                continue

            # Check for wait for
            if command == 'wait' and arg.strip() != '':
                arg = arg.strip()
                item_selector = arg
                try:
                    item = WebDriverWait(Artemis.driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, arg))
                    )
                    log_output(f'[Success] Found element: {arg}')
                except:
                    log_output(f'[Error] Command {command} failed - Line {i} - Element not found: {arg}')
                continue


            # Check for break
            if command == 'exit':
                break

            # Unknown command
            log_output(f'[Error] Line {i}: Unknown command!')
            log_output(f'[Error] Line {i}: command = {command}')
            log_output(f'[Error] Line {i}: arg = {arg}')
            log_output(f'[Error] Line {i}: extra_arg = {extra_arg}')


        # Dump log
        with open(os.path.join(test_script_directory, 'log.txt'), 'w', encoding='utf-8') as file:
            file.writelines(output_log)

        # Exit
        print('Done!')
        Artemis.driver.quit()
        os._exit(0)

    # Waiter at exit
    @staticmethod
    def waiter():
        '''
        Waiter at exit
        :return: None
        '''
        value = json.dumps({
            "type": "complete",
        })
        Artemis.artemis_socket.send(value)
        while True:
            sleep(1)

    # Launch server
    @staticmethod
    def run(launch=True) -> None:
        '''
        Start web socket and launch browser if in launch mode
        :param launch: Whether or not we launch browser
        :return: None
        '''

        print('Starting Artemis Socket...')
        Artemis.artemis_socket.run()

        sleep(1)

        print('Launching browser...')
        if launch:
            if os.name == 'nt':
                if Artemis.mode == "code":

                    # Start up server
                    Artemis.cur_dir = os.getcwd()

                    # Get file directory
                    file_dir = os.path.dirname(os.path.abspath(__file__))
                    html_path = f'{file_dir}/htdocs/launcher_code.html'

                    # Spawn selenium webdriver
                    print('Starting Selenium Webdriver')
                    driver_path = "C:\\Program Files (x86)\\chromedriver.exe"
                    chrome_options = webdriver.chrome.options.Options()
                    #chrome_options.add_argument("--disable-extensions")
                    #chrome_options.add_argument("--disable-gpu")
                    #chrome_options.add_argument("--no-sandbox") # linux only
                    chrome_options.add_argument("--headless")
                    Artemis.driver = webdriver.Chrome(driver_path, service_log_path='NUL', options=chrome_options)
                    Artemis.driver.set_window_size(1920, 1080)
                    Artemis.driver.get(f'file://{html_path.replace(" ", "%20")}')
                else:
                    os.system("start chrome /new-window https://artemisardesignerdev.com/launcher_local.html")
            else:
                print('[Artemis] Please open Chrome and navigate to https://artemisardesignerdev.com/launcher_local.html')

        while not Artemis.artemis_socket.is_connected():
            sleep(0.1)

        code_path = os.path.join(Artemis.cur_dir, Artemis.code_path)
        with open(code_path, 'r', encoding='utf-8') as file:
            init_packet = { 'type' : 'init', 'state' : file.read(), 'file_name' : os.path.basename(code_path), 'settings' : json.dumps(Artemis.settings) }
            out_str = json.dumps(init_packet)
            out_str  = out_str.replace("<", "&lt;").replace(">", "&gt;")
            Artemis.artemis_socket.send(out_str)

        # Start test thread
        if Artemis.dev:
            thread = Thread(target=Artemis.tester)
            thread.start()

    @staticmethod
    def load_image(image_path : str) -> None:
        '''
        Pass-through to helper function
        : return str: Base64 encoded image
        '''
        return ArtemisHelper.load_image(image_path)
