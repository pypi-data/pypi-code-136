import pickle
import shutil, os
import inspect
import json
from pymongo import MongoClient
from itertools import repeat
from datetime import datetime
import csv
import sys
import pandas as pd
from pathlib import Path
from itertools import repeat

#Path to niraapad
file_path = os.path.dirname(os.path.abspath(__file__))
niraapad_path = os.path.dirname(os.path.dirname(file_path))
sys.path.append(niraapad_path)

import niraapad.backends
import niraapad.protos.niraapad_pb2 as niraapad_pb2
import niraapad.protos.niraapad_pb2_grpc as niraapad_pb2_grpc
from niraapad.backends import DirectUR3Arm
from niraapad.backends import DirectFtdiDevice, DirectPySerialDevice
from niraapad.backends import DirectArduinoAugmentedQuantos
from niraapad.shared.tracing import Tracer

from niraapad.data_processing.commands import magneticstirrer_commands, tecancavro_commands, controller_commands

class RuntimeCurator:
    """Provides methods for runtime conversion of commands and arguments."""


    def __init__(self):

        self.backend_instance_id_magstr = []
        self.backend_instance_id_cavro = []
        self.backend_instance_id_c9 = []
        self.backend_instance_id_arduino = []
        self.backend_instance_id_ur = []
        self.backend_instance_id_thermo = []

    def convert_to_commands(self, method_name, field, value,
                            backend_instance_id):
        commands = {}

        #Return magnetic stirrer commands
        if backend_instance_id in self.backend_instance_id_magstr:
            magstr = magneticstirrer_commands()
            if method_name == "write":
                commands = magstr.write_ika(value, commands)
            elif method_name == "read":
                commands = magstr.read_ika(value, commands)
        #Return C9 commands
        elif backend_instance_id in self.backend_instance_id_c9:
            c9 = controller_commands()
            if method_name == "write":
                commands = c9.write_c9(value, commands)
            elif method_name == "read" or method_name == "read_line":
                commands = c9.read_c9(value, commands)
        #Return tecan cavro commands
        elif backend_instance_id in self.backend_instance_id_cavro:
            t_cavro = tecancavro_commands()
            if method_name == "write":
                commands = t_cavro.write_cavro(value, commands)
            elif method_name == "read":
                commands = t_cavro.read_cavro(value, commands)
        else:
            commands[field] = str(value)

        return commands

    def convert_args(self, trace_msg_type, trace_msg, args, kwargs,
                     backend_instance_id):
          
        
        try:
            # Get the argspec of the Initialization and other functions
            if trace_msg_type != "InitializeReq":
                argspecs = inspect.getfullargspec(
                    eval(trace_msg.backend_type + "." +
                        trace_msg.method_name))
            else:
                argspecs = inspect.getfullargspec(
                    eval(trace_msg.backend_type + ".__init__"))

            arg_val = {}
            check = 'o'
            
            

            # Get the default values of the function
            if argspecs.defaults == None:
                defaults = argspecs.defaults
            elif len(argspecs.args) != len(argspecs.defaults):
                empty_spaces = tuple(
                    repeat(None,
                        len(argspecs.args) - len(argspecs.defaults)))
                defaults = empty_spaces + argspecs.defaults
            else:
                defaults = argspecs.defaults
            
            #Adding the kwargs of the function to the dictionary arg_val
            for val in kwargs:
                if isinstance(kwargs[val], bytes):
                    if val == "data":
                        arg_val[val] = self.convert_to_commands(
                            trace_msg.method_name, val, kwargs[val],
                            backend_instance_id)
                    else:
                        arg_val[val] = kwargs[val].decode()
                else:
                    arg_val[val] = str(kwargs[val])


            #Adding the args and the default values to the dictionary arg_val
            
            counter = 0
            i = 0
            while counter != len(argspecs.args)-1:
                if argspecs.args[counter] == "self":
                    counter = counter + 1
                    continue     
                else:
                    if check == 'o':
                        check = 'a'
                        for val in args:
                            if isinstance(val, bytes):
                                if (argspecs.args[counter] == "data"):
                                    arg_val[argspecs.args[counter]] = self.convert_to_commands(
                                        trace_msg.method_name, argspecs.args[counter], val,
                                        backend_instance_id)
                                else:
                                    arg_val[argspecs.args[counter]] = val.decode()
                            else:
                                arg_val[argspecs.args[counter]] = str(val)
                            counter = counter + 1
                    elif check == 'a':
                        if argspecs.args[counter] not in arg_val.keys():
                            try:
                                arg_val[argspecs.args[counter]] = str(defaults[i])
                            except:
                                pass
                        counter = counter + 1
                
                i = i + 1

            return arg_val

        except:
            # Get the argspec of the Initialization and other functions
            if trace_msg_type != "InitializeTraceMsg":
                argspecs = inspect.getfullargspec(
                    eval(trace_msg.req.backend_type + "." +
                        trace_msg.req.method_name))
            else:
                argspecs = inspect.getfullargspec(
                    eval(trace_msg.req.backend_type + ".__init__"))

            arg_val = {}
            check = 'o'

            # Get the default values of the function
            if argspecs.defaults == None:
                defaults = argspecs.defaults
            elif len(argspecs.args) != len(argspecs.defaults):
                empty_spaces = tuple(
                    repeat(None,
                        len(argspecs.args) - len(argspecs.defaults)))
                defaults = empty_spaces + argspecs.defaults
            else:
                defaults = argspecs.defaults

            #Adding the kwargs of the function to the dictionary arg_val
            for val in kwargs:
                if isinstance(kwargs[val], bytes):
                    if val == "data":
                        arg_val[val] = self.convert_to_commands(
                            trace_msg.req.method_name, val, kwargs[val],
                            backend_instance_id)
                    else:
                        arg_val[val] = kwargs[val].decode()
                else:
                    arg_val[val] = str(kwargs[val])

            #Adding the args and the default values to the dictionary arg_val
            counter = 0
            i = 0
            while counter != len(argspecs.args):
                if argspecs.args[counter] == "self":
                    counter = counter + 1
                    continue
                else:
                    if check == 'o':
                        check = 'a'
                        for val in args:
                            if isinstance(val, bytes):
                                if (argspecs.args[counter] == "data"):
                                    arg_val[argspecs.args[counter]] = self.convert_to_commands(
                                        trace_msg.method_name, argspecs.args[counter], val,
                                        backend_instance_id)
                                else:
                                    arg_val[argspecs.args[counter]] = val.decode()
                            else:
                                arg_val[argspecs.args[counter]] = str(val)
                            counter = counter + 1
                    elif check == 'a':
                        if argspecs.args[counter] not in arg_val.keys():
                            try:
                                arg_val[argspecs.args[counter]] = str(defaults[i])
                            except:
                                pass
                        counter = counter + 1
                i = i + 1

            return arg_val

    def run_time_process(self, trace_msg):

        trace_msg_type = (str(type(trace_msg))).split("'")[1].split(".")[-1]

        trace_msg_parse = {}
        msg_sub_field = {}

        cmd = ""
        args = ""
        
       
        for sub_field, value in trace_msg.ListFields():


                        #Merge args and kwargs, conversion to json format

                        if str(sub_field.name) == "args":
                            args = pickle.loads(value)
                        elif str(sub_field.name) == "kwargs":
                            msg_sub_field['args'] = self.convert_args(
                                trace_msg_type, trace_msg, args,
                                pickle.loads(value),
                                trace_msg.backend_instance_id)
                        elif isinstance(value, bytes):
                            #Checking for read commands for the modules or exceptions
                            try:
                                if isinstance(
                                        pickle.loads(value),
                                        bytes) and pickle.loads(value) != None:
                                    msg_sub_field[str(
                                        sub_field.name
                                    )] = self.convert_to_commands(
                                        trace_msg.method_name,
                                        sub_field.name, pickle.loads(value),
                                        trace_msg.backend_instance_id)
                                else:
                                    msg_sub_field[str(sub_field.name)] = str(
                                        pickle.loads(value))
                            except:
                               msg_sub_field[str(sub_field.name)] = str(value)
                        else:
                            msg_sub_field[str(sub_field.name)] = value
       
        trace_msg_parse['req'] = msg_sub_field
        

        #Append backend instance of each module
        if trace_msg_type == "InitializeReq":
                stacktrace = trace_msg_parse['req']['stacktrace']

                if "magnetic_stirrer.py" and "thermoshaker.py" in stacktrace:
                    self.backend_instance_id_magstr.append(
                        trace_msg_parse['req']['backend_instance_id'])
                elif "controller.py" in stacktrace:
                    self.backend_instance_id_c9.append(
                        trace_msg_parse['req']['backend_instance_id'])
                elif "controller.py" not in stacktrace and trace_msg_parse[
                        'req']['backend_type'] == "DirectFtdiDevice":
                    self.backend_instance_id_cavro.append(
                        trace_msg_parse['req']['backend_instance_id'])
                else:
                    module = trace_msg_parse['req']['backend_type'].replace(
                        "Direct", "")
                    if module == "UR3Arm":
                        self.backend_instance_id_ur.append(
                            trace_msg_parse['req']['backend_instance_id'])
                    else:
                        self.backend_instance_id_arduino.append(
                            trace_msg_parse['req']['backend_instance_id'])

            
                cmd = "_init_" 
                args = trace_msg_parse['req']['args']

                
        elif trace_msg_type == "GenericMethodReq" or trace_msg_type == "GenericSetterReq":

                    if trace_msg_parse['req']['backend_instance_id'] in self.backend_instance_id_magstr:
                        if 'data' in trace_msg_parse['req']['args'].keys(
                        ) and trace_msg_parse['req']['args']['data'][
                                'command_name']:

                            cmd = trace_msg_parse['req']['args']['data']['command_name']
                            args = trace_msg_parse['req']['args']['data']['value']


                    elif trace_msg_parse['req'][
                            'backend_instance_id'] in self.backend_instance_id_c9:
                        if "data" in trace_msg_parse['req']['args'].keys(
                        ) and trace_msg_parse['req']['args']['data'][
                                'command_name']:
                            if "args" in trace_msg_parse['req']['args'][
                                    'data'].keys():
                                
                                cmd = trace_msg_parse['req']['args']['data']['command_name']
                                args = {**trace_msg_parse['req']['args']['data']['args'],
                                        **trace_msg_parse['req']
                                            ['args']['data']['flags']}


                            elif trace_msg_parse['req'][
                                    'args']['data'].keys():
                                cmd = trace_msg_parse['req']['args']['data']['command_name']
                                args = trace_msg_parse['req']['args']['data']['flags']
                            else:
                                cmd = trace_msg_parse['req']['args']['data']['command_name']
                                args = None
                                

                    elif trace_msg_parse['req'][
                            'backend_instance_id'] in self.backend_instance_id_cavro:
                        if 'data' in trace_msg_parse['req']['args'].keys(
                        ) and 'command_name_0' in trace_msg_parse['req'][
                                'args']['data'].keys(
                                ) and trace_msg_parse['req']['args'][
                                    'data']['command_name_0']:

                            commands_values = list(trace_msg_parse['req']
                                                   ['args']['data'].keys())
                            i = 0
                            while (i < len(commands_values)):
                                if i + 1 < len(
                                        trace_msg_parse['req']['args']
                                    ['data'].keys()
                                ) and "command" not in commands_values[i + 1]:

                                    cmd = trace_msg_parse['req']['args']['data'][commands_values[i]]

                                    args[commands_values[i + 1]] = trace_msg_parse['req'] ['args']['data'][commands_values[i + 1]]
                                    
                                    i = i + 2
                                else:

                                    cmd = trace_msg_parse['req']['args']['data'][commands_values[i]]
                                    args = trace_msg_parse['resp']['resp']
                                    
                                    i = i + 1
                    else:
                        if trace_msg_parse['req']['backend_type'].replace("Direct", "") == "UR3Arm":
                            try:
                                cmd = trace_msg_parse['req']['method_name']
                                args = trace_msg_parse['req']['args']
                            except:
                                cmd = trace_msg_parse['req']['property_name']
                                args = ast.literal_eval('value: ' + str(trace_msg_parse['req']['value']))
                            
                        elif trace_msg_parse['req'][
                            'backend_type'].replace("Direct", "") == "ArduinoAugmentedQuantos":
                            try:
                                cmd = trace_msg_parse['req']['method_name']
                                args = trace_msg_parse['req']['args']
                            except:
                                cmd = trace_msg_parse['req']['property_name']
                                args = ast.literal_eval('value: ' + str(trace_msg_parse['req']['value']))
                        else:
                            cmd = ""
                            args = ""
                        
                        
        else:
            cmd = ""
            args = ""
        return cmd, args

