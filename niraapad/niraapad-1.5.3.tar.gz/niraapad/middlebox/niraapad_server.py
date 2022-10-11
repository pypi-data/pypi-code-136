from math import isnan
import os
from socket import timeout
import sys
import time
import grpc
import pickle
import inspect
import importlib
import csv
import pandas as pd
import numpy as np

from concurrent import futures
from datetime import datetime
from timeit import default_timer
from datetime import datetime

from ftdi_serial import Device
from ftdi_serial import FtdiDevice
from ftdi_serial import PySerialDevice

file_path = os.path.dirname(os.path.abspath(__file__))
niraapad_path = os.path.dirname(file_path)
sys.path.append(niraapad_path)
print(niraapad_path)

import niraapad.protos.niraapad_pb2 as niraapad_pb2
import niraapad.protos.niraapad_pb2_grpc as niraapad_pb2_grpc

from niraapad.shared.tracing import Tracer
import niraapad.shared.utils as utils

import ast
import json

from configparser import ConfigParser


from niraapad.data_processing.curation import RuntimeCurator
from niraapad.detective.detector import Detective

curation = RuntimeCurator()

niraapad_backends_module = importlib.import_module("niraapad.backends")


class NiraapadServicer(niraapad_pb2_grpc.NiraapadServicer):
    """Provides methods that implement functionality of n9 server."""

    trace_metadata_length = 132  # bytes

    def __init__(self, tracedir, ids, configdir):
        print("Initializing NiraapadServicer", flush=True)
        self.backend_instances = {}
        self.tracer = Tracer(tracedir)

        trace_msg = niraapad_pb2.StartServerTraceMsg()
        self.tracer.write_to_file(trace_msg)

        self.configdir = configdir

        self.ids = ids
        
        

    def stop_tracing(self):
        print("NiraapadServicer::stop_tracing", flush=True)
        trace_msg = niraapad_pb2.StopServerTraceMsg()
        self.tracer.write_to_file(trace_msg)
        self.tracer.stop_tracing()

    def check_for_intrusion(self, trace_msg):
        if self.ids == '1':
            cmd, args = curation.run_time_process(trace_msg)
            if cmd != "":
                activity, rule, pre_state, state = self.detector.alarm(cmd, args)
                self.file_testing.writerow([datetime.now().strftime("%Y:%m:%d:%H:%M:%S.%f"), activity, rule, cmd, args, str(pre_state), str(state)])
            #if state == 'malicious':
            #     raise Exception(str(datetime.now()) + ': TRIGGER ALARM: Observed Malicious Activity. ' + rule + ' is violated.)
           
        

    def log_trace_msg(self, trace_msg, elapsed=0):
        self.tracer.write_to_file(trace_msg)
        
    
    def delete_context(self):
        print("NiraapadServicer::delete_context", flush=True)
        for backend_type in self.backend_instances:
            for backend_instance_id in self.backend_instances[backend_type]:
                if backend_type == utils.BACKENDS.DEVICE \
                    or backend_type == utils.BACKENDS.MOCK_DEVICE \
                    or backend_type == utils.BACKENDS.FTDI_DEVICE \
                    or backend_type == utils.BACKENDS.PY_SERIAL_DEVICE:
                    self.backend_instances[backend_type][
                        backend_instance_id].close()
                elif backend_type == utils.BACKENDS.ROBOT_ARM \
                    or backend_type == utils.BACKENDS.UR3_ARM:
                    if self.backend_instances[backend_type][
                            backend_instance_id].connected:
                        self.backend_instances[backend_type][
                            backend_instance_id].disconnect()
                elif backend_type == utils.BACKENDS.BALANCE \
                    or backend_type == utils.BACKENDS.QUANTOS \
                    or backend_type == utils.BACKENDS.ARDUINO_AUGMENT \
                    or backend_type == utils.BACKENDS.ARDUINO_AUGMENTED_QUANTOS:
                    pass
        del self.backend_instances
        self.backend_instances = {}

    def BatchedTrace(self, batched_trace_msg, context):
        trace_msgs = pickle.loads(batched_trace_msg.trace_msgs)
        for trace_msg in trace_msgs:
            print("(trace) %s.%s" %
                  (trace_msg.req.backend_type, Tracer.get_msg_type(trace_msg)))
            self.log_trace_msg(trace_msg)
        return niraapad_pb2.EmptyMsg()

    def InitializeConnection(self, req, context):
        print("NiraapadClientHelper.__init__", flush=True)
        
        if self.ids == '1':
            self.detector = Detective(self.configdir)
            dir_exist = os.path.exists(niraapad_path + '\\test\\testing_files')
            if dir_exist == False:
                os.mkdir(niraapad_path + '\\test\\testing_files')
            self.file_name = open(niraapad_path + '\\test\\testing_files\\logging_activity_'+ datetime.now().strftime("%Y%m%d%H%M%S") +'.csv', 'w', newline='')
            self.file_testing = csv.writer(self.file_name)
            self.file_testing.writerow(['Timestamp', 'Activity', 'Rule', 'Command', 'Arguments', 'Pre_State', 'State'])
            
        self.check_for_intrusion(req)
        
        resp = None
        exception = None

        resp = niraapad_pb2.InitializeConnectionResp(
            exception=pickle.dumps(exception))

        trace_msg = niraapad_pb2.InitializeConnectionTraceMsg(req=req,
                                                              resp=resp)
        self.log_trace_msg(trace_msg)

        return resp

    def DeleteConnection(self, req, context):
        print("NiraapadClientHelper.__del__", flush=True)
        
        self.check_for_intrusion(req)


        exception = None

        try:
            self.delete_context()
        except Exception as e:
            NiraapadServicer.print_exception(e)
            exception = e

        resp = niraapad_pb2.DeleteConnectionResp(
            exception=pickle.dumps(exception))

        trace_msg = niraapad_pb2.DeleteConnectionTraceMsg(req=req, resp=resp)
        self.log_trace_msg(trace_msg)
    

        return resp

    def StaticMethod(self, req, context):
        print("%s.%s" % (req.backend_type, req.method_name), flush=True)

        self.check_for_intrusion(req)

        args = pickle.loads(req.args)
        kwargs = pickle.loads(req.kwargs)

        resp = None
        exception = None

        start = default_timer()
        try:
            class_name = getattr(niraapad_backends_module, req.backend_type)
            resp = getattr(class_name, req.method_name)(*args, **kwargs)
        except Exception as e:
            NiraapadServicer.print_exception(e)
            exception = e
        end = default_timer()

        resp = utils.sanitize_resp(req.method_name, resp)

        resp = niraapad_pb2.StaticMethodResp(exception=pickle.dumps(exception),
                                             resp=pickle.dumps(resp))

        profile = niraapad_pb2.CommandProfile(mo=int(utils.MO.VIA_MIDDLEBOX),
                                              exec_time_sec=(end - start))

        trace_msg = niraapad_pb2.StaticMethodTraceMsg(req=req,
                                                      resp=resp,
                                                      profile=profile)
        self.log_trace_msg(trace_msg)

        return resp

    def StaticGetter(self, req, context):
        print("%s.get_%s" % (req.backend_type, req.property_name), flush=True)
        
        self.check_for_intrusion(req)

        resp = None
        exception = None

        start = default_timer()
        try:
            class_name = getattr(niraapad_backends_module, req.backend_type)
            resp = getattr(class_name, req.property_name)
        except Exception as e:
            NiraapadServicer.print_exception(e)
            exception = e
        end = default_timer()

        resp = niraapad_pb2.StaticGetterResp(exception=pickle.dumps(exception),
                                             resp=pickle.dumps(resp))

        profile = niraapad_pb2.CommandProfile(mo=int(utils.MO.VIA_MIDDLEBOX),
                                              exec_time_sec=(end - start))

        trace_msg = niraapad_pb2.StaticGetterTraceMsg(req=req,
                                                      resp=resp,
                                                      profile=profile)
        self.log_trace_msg(trace_msg)

        return resp

    def StaticSetter(self, req, context):
        print("%s.set_%s" % (req.backend_type, req.property_name), flush=True)

        self.check_for_intrusion(req)

        value = pickle.loads(req.value)

        resp = None
        exception = None

        start = default_timer()
        try:
            class_name = getattr(niraapad_backends_module, req.backend_type)
            setattr(class_name, req.property_name, value)
        except Exception as e:
            NiraapadServicer.print_exception(e)
            exception = e
        end = default_timer()

        resp = niraapad_pb2.StaticSetterResp(exception=pickle.dumps(exception))

        profile = niraapad_pb2.CommandProfile(mo=int(utils.MO.VIA_MIDDLEBOX),
                                              exec_time_sec=(end - start))

        trace_msg = niraapad_pb2.StaticSetterTraceMsg(req=req,
                                                      resp=resp,
                                                      profile=profile)
        self.log_trace_msg(trace_msg)

        return resp

    def Initialize(self, req, context):
        print("%s.__init__" % (req.backend_type), flush=True)

        # Since the __init__ function is invoked similar to static methods,
        # that is, it is invoked using the class name, this function is
        # analogous to the static_method function above, except that we do not
        # need a variable for the method name, which is known to be "__init__"
        # in this case.

        self.check_for_intrusion(req)

        args = pickle.loads(req.args)
        kwargs = pickle.loads(req.kwargs)

        if req.backend_type not in self.backend_instances:
            self.backend_instances[req.backend_type] = {}

        exception = None

        start = default_timer()
        try:
            class_name = getattr(niraapad_backends_module, req.backend_type)
            self.backend_instances[req.backend_type][req.backend_instance_id] = \
                class_name(*args, **kwargs)
        except Exception as e:
            NiraapadServicer.print_exception(e)
            exception = e
        end = default_timer()

        resp = niraapad_pb2.InitializeResp(exception=pickle.dumps(exception))

        profile = niraapad_pb2.CommandProfile(mo=int(utils.MO.VIA_MIDDLEBOX),
                                              exec_time_sec=(end - start))

        trace_msg = niraapad_pb2.InitializeTraceMsg(req=req,
                                                    resp=resp,
                                                    profile=profile)
        self.log_trace_msg(trace_msg)

        return resp

    def Uninitialize(self, req, context):
        print("%s.__del__" % (req.backend_type), flush=True)

        #self.check_for_intrusion(req)

        exception = None

        backend_type = req.backend_type
        backend_instance_id = req.backend_instance_id

        start = default_timer()
        try:
            if backend_type in self.backend_instances:
                if backend_instance_id in self.backend_instances[backend_type]:
                    del self.backend_instances[backend_type][
                        backend_instance_id]

        except Exception as e:
            NiraapadServicer.print_exception(e)
            exception = e
        end = default_timer()

        resp = niraapad_pb2.UninitializeResp(exception=pickle.dumps(exception))

        profile = niraapad_pb2.CommandProfile(mo=int(utils.MO.VIA_MIDDLEBOX),
                                              exec_time_sec=(end - start))

        trace_msg = niraapad_pb2.UninitializeTraceMsg(req=req,
                                                      resp=resp,
                                                      profile=profile)
        self.log_trace_msg(trace_msg)

        return resp

    def GenericMethod(self, req, context):
        print("%s.%s" % (req.backend_type, req.method_name), flush=True)

        # For any generic class instance method, the logic is similar to that
        # of any generic static method, except that the method is invoked using
        # the class instance name and not directly using the class name.
        # Thus, the following set of statements is analogous to the function
        # definition of the static_methods function above, except that we deal
        # with specific class instances identified using their unique
        # identifiers ("backend_instance_id"), which were set during
        # initialization.

        self.check_for_intrusion(req)

        args = pickle.loads(req.args)
        kwargs = pickle.loads(req.kwargs)

        resp = None
        exception = None
        start = default_timer()
        try:
            resp = getattr(
                self.backend_instances[req.backend_type][
                    req.backend_instance_id], req.method_name)(*args, **kwargs)
        except Exception as e:
            NiraapadServicer.print_exception(e)
            exception = e
        end = default_timer()

        resp = niraapad_pb2.GenericMethodResp(exception=pickle.dumps(exception),
                                              resp=pickle.dumps(resp))

        profile = niraapad_pb2.CommandProfile(mo=int(utils.MO.VIA_MIDDLEBOX),
                                              exec_time_sec=(end - start))

        trace_msg = niraapad_pb2.GenericMethodTraceMsg(req=req,
                                                       resp=resp,
                                                       profile=profile)
        self.log_trace_msg(trace_msg)
        return resp

    def GenericGetter(self, req, context):
        print("%s.get_%s" % (req.backend_type, req.property_name), flush=True)

        self.check_for_intrusion(req)

        # Getter functions are an extremely simplified version of GenericMethod
        # since they are interpreted not as functions but as variables, which
        # may be used in an expression; in this case, we simply return the
        # variable value.

        resp = None
        exception = None

        start = default_timer()
        try:
            resp = getattr(
                self.backend_instances[req.backend_type][
                    req.backend_instance_id], req.property_name)
        except Exception as e:
            NiraapadServicer.print_exception(e)
            exception = e
        end = default_timer()

        resp = utils.sanitize_resp(req.property_name, resp)

        resp = niraapad_pb2.GenericGetterResp(exception=pickle.dumps(exception),
                                              resp=pickle.dumps(resp))

        profile = niraapad_pb2.CommandProfile(mo=int(utils.MO.VIA_MIDDLEBOX),
                                              exec_time_sec=(end - start))

        trace_msg = niraapad_pb2.GenericGetterTraceMsg(req=req,
                                                       resp=resp,
                                                       profile=profile)
        self.log_trace_msg(trace_msg)

        return resp

    def GenericSetter(self, req, context):
        print("%s.set_%s" % (req.backend_type, req.property_name), flush=True)
   
        self.check_for_intrusion(req)

        # Setter functions are the opposite of getter functions. They simply
        # assign the provided value to the specified property.

        value = pickle.loads(req.value)

        resp = None
        exception = None

        start = default_timer()
        try:
            setattr(
                self.backend_instances[req.backend_type][
                    req.backend_instance_id], req.property_name, value)
        except Exception as e:
            NiraapadServicer.print_exception(e)
            exception = e
        end = default_timer()

        resp = niraapad_pb2.GenericSetterResp(exception=pickle.dumps(exception))

        profile = niraapad_pb2.CommandProfile(mo=int(utils.MO.VIA_MIDDLEBOX),
                                              exec_time_sec=(end - start))

        trace_msg = niraapad_pb2.GenericSetterTraceMsg(req=req,
                                                       resp=resp,
                                                       profile=profile)
        self.log_trace_msg(trace_msg)

        return resp

    def ConfigSetter(self, req, context):

        config_object = ConfigParser()
        args = pickle.loads(req.args)

        if args[0] == 1:
            
            list_of_predicates = pd.DataFrame(args[1], columns = ['List of Predicates'])
            init_state_table = pd.DataFrame(args[2], columns = ['Predicate', 'Define', 'Initial Command', 'Initial Conditions'])
            transit_table = pd.DataFrame(args[3], columns = ['Preconditions', 'Command', 'Conditions'] + args[1])
            rule_table = pd.DataFrame(args[4], columns = args[1])
            
            writer = pd.ExcelWriter(self.configdir, engine='xlsxwriter')

            list_of_predicates.to_excel(writer, sheet_name='list_of_predicates', index=False)
            init_state_table.to_excel(writer, sheet_name='init_state_table', index=False)
            transit_table.to_excel(writer, sheet_name='transit_table', index=False)
            rule_table.to_excel(writer, sheet_name='rule_table', index=False)

            writer.save()

            print("Created New File")

        elif args[0] == 2:

            list_of_predicates = pd.read_excel(self.configdir, sheet_name='list_of_predicates',  engine='openpyxl')['List of Predicates'].tolist()
            init_state_table = pd.read_excel(self.configdir, sheet_name='init_state_table',  engine='openpyxl').replace(np.nan, '').values.tolist()
            rule_table = pd.read_excel(self.configdir, sheet_name='rule_table',  engine='openpyxl').values.tolist()

            
           
            list_of_predicates = list_of_predicates + args[1]
            init_state_table = init_state_table + args[2]



            
            updated_rule_table = []
            for i in range(0, len(rule_table)):
                for j in range(0,len(args[1])):
                    rule_table[i].append('x')
           

            
            init_state_table = pd.DataFrame(init_state_table, columns = ['Predicate', 'Define', 'Initial Command', 'Initial Conditions'])
            transit_table = pd.DataFrame(args[3], columns = ['Preconditions', 'Command', 'Conditions'] + list_of_predicates)
            rule_table = pd.DataFrame(rule_table, columns = list_of_predicates)
            list_of_predicates = pd.DataFrame(list_of_predicates, columns = ['List of Predicates'])

            writer = pd.ExcelWriter(self.configdir, engine='xlsxwriter')
            list_of_predicates.to_excel(writer, sheet_name='list_of_predicates', index=False)
            init_state_table.to_excel(writer, sheet_name='init_state_table', index=False)
            transit_table.to_excel(writer, sheet_name='transit_table', index=False)
            rule_table.to_excel(writer, sheet_name='rule_table', index=False)

            writer.save()

        
        elif args[0] == 3:


            remove_preds = args[1]

            list_of_predicates = pd.read_excel(self.configdir, sheet_name='list_of_predicates',  engine='openpyxl')['List of Predicates'].tolist()
            init_state_table = pd.read_excel(self.configdir, sheet_name='init_state_table',  engine='openpyxl').replace(np.nan, '').values.tolist()
            transit_table = pd.read_excel(self.configdir, sheet_name='transit_table',  engine='openpyxl')
            rule_table = pd.read_excel(self.configdir, sheet_name='rule_table',  engine='openpyxl').values.tolist()


            iter = len(list_of_predicates)*2 - 1
            index = len(list_of_predicates) - 1
            indexes = []
            for key, value in remove_preds.items():
                if value == True:
                    list_of_predicates.remove(key)
                    a = init_state_table.pop(iter)
                    b = init_state_table.pop(iter-1)
                    print(index)
                    transit_table = transit_table.drop(transit_table.columns[index+3],axis=1)
                    for i in range(0, len(rule_table)):
                        rule_table[i].pop(index)
                iter = iter - 2
                index = index - 1


            init_state_table = pd.DataFrame(init_state_table, columns = ['Predicate', 'Define', 'Initial Command', 'Initial Conditions'])
            transit_table = pd.DataFrame(transit_table, columns = ['Preconditions', 'Command', 'Conditions'] + list_of_predicates)
            rule_table = pd.DataFrame(rule_table, columns = list_of_predicates)
            list_of_predicates = pd.DataFrame(list_of_predicates, columns = ['List of Predicates'])


            writer = pd.ExcelWriter(self.configdir, engine='xlsxwriter')
            list_of_predicates.to_excel(writer, sheet_name='list_of_predicates', index=False)
            init_state_table.to_excel(writer, sheet_name='init_state_table', index=False)
            transit_table.to_excel(writer, sheet_name='transit_table', index=False)
            rule_table.to_excel(writer, sheet_name='rule_table', index=False)

            writer.save()
                
        elif args[0] == 4:

            list_of_predicates = pd.read_excel(self.configdir, sheet_name='list_of_predicates',  engine='openpyxl')
            init_state_table = pd.DataFrame(args[1], columns = ['State', 'Define', 'Initial Command', 'Initial Conditions'])
            transit_table = pd.read_excel(self.configdir, sheet_name='transit_table',  engine='openpyxl')
            rule_table = pd.read_excel(self.configdir, sheet_name='rule_table',  engine='openpyxl')

            writer = pd.ExcelWriter(self.configdir, engine='xlsxwriter')
            list_of_predicates.to_excel(writer, sheet_name='list_of_predicates', index=False)
            init_state_table.to_excel(writer, sheet_name='init_state_table', index=False)
            transit_table.to_excel(writer, sheet_name='transit_table', index=False)
            rule_table.to_excel(writer, sheet_name='rule_table', index=False)


            writer.save()

        elif args[0] == 5:

            list_of_predicates = pd.read_excel(self.configdir, sheet_name='list_of_predicates',  engine='openpyxl')
            predicate_list = list_of_predicates['List of Predicates'].tolist()
            init_state_table = pd.read_excel(self.configdir, sheet_name='init_state_table',  engine='openpyxl')
            transit_table = pd.DataFrame(args[1], columns = ['Preconditions', 'Command', 'Conditions'] + predicate_list)
            rule_table = pd.read_excel(self.configdir, sheet_name='rule_table',  engine='openpyxl')

            writer = pd.ExcelWriter(self.configdir, engine='xlsxwriter')
            list_of_predicates.to_excel(writer, sheet_name='list_of_predicates', index=False)
            init_state_table.to_excel(writer, sheet_name='init_state_table', index=False)
            transit_table.to_excel(writer, sheet_name='transit_table', index=False)
            rule_table.to_excel(writer, sheet_name='rule_table', index=False)

            writer.save()
        
        elif args[0] == 6:
 
            list_of_predicates = pd.read_excel(self.configdir, sheet_name='list_of_predicates',  engine='openpyxl')
            predicate_list = list_of_predicates['List of Predicates'].tolist()
            init_state_table = pd.read_excel(self.configdir,  sheet_name='init_state_table',  engine='openpyxl')
            transit_table = pd.read_excel(self.configdir, sheet_name='transit_table',  engine='openpyxl')
            rule_table = pd.DataFrame(args[1], columns = predicate_list)

            writer = pd.ExcelWriter(self.configdir, engine='xlsxwriter')
            list_of_predicates.to_excel(writer, sheet_name='list_of_predicates', index=False)
            init_state_table.to_excel(writer, sheet_name='init_state_table', index=False)
            transit_table.to_excel(writer, sheet_name='transit_table', index=False)
            rule_table.to_excel(writer, sheet_name='rule_table', index=False)

            writer.save()
           
        elif args[0] == 7:

            list_of_predicates = pd.read_excel(self.configdir, sheet_name='list_of_predicates',  engine='openpyxl')
            predicate_list = list_of_predicates['List of Predicates'].tolist()
            init_state_table = pd.read_excel(self.configdir,  sheet_name='init_state_table',  engine='openpyxl')
            transit_table = pd.read_excel(self.configdir, sheet_name='transit_table',  engine='openpyxl')
            rules_table = pd.read_excel(self.configdir, sheet_name='rule_table',  engine='openpyxl').values.tolist()

            remove_rules = args[1]
            for key, value in remove_rules.items():
                if value == True:
                    a = rules_table.pop(int(key) - 1)

            
            rules_table = pd.DataFrame(rules_table, columns = predicate_list)

            writer = pd.ExcelWriter(self.configdir, engine='xlsxwriter')
            list_of_predicates.to_excel(writer, sheet_name='list_of_predicates', index=False)
            init_state_table.to_excel(writer, sheet_name='init_state_table', index=False)
            transit_table.to_excel(writer, sheet_name='transit_table', index=False)
            rules_table.to_excel(writer, sheet_name='rule_table', index=False)

            writer.save()


        return niraapad_pb2.ConfigSetterResp()
    
    def ConfigGetter(self, req, context):

        args = pickle.loads(req.args)

        if args[0] == 1:
            list_of_predicates = pd.read_excel(self.configdir, sheet_name='list_of_predicates',  engine='openpyxl')['List of Predicates'].tolist()
            resp = niraapad_pb2.ConfigGetterResp(resp=str(list_of_predicates))
        elif args[0] == 2:
            transit_table = pd.read_excel(self.configdir, sheet_name='transit_table',  engine='openpyxl')
            transit_table = transit_table.replace(np.nan, '', regex=True).values.tolist()
            resp = niraapad_pb2.ConfigGetterResp(resp=str(transit_table))
        elif args[0] == 3:
            rule_table = pd.read_excel(self.configdir, sheet_name='rule_table',  engine='openpyxl')
            rule_table = rule_table.replace(np.nan, '', regex=True).values.tolist()
            resp = niraapad_pb2.ConfigGetterResp(resp=str(rule_table))
        elif args[0] == 4:
            init_state_table = pd.read_excel(self.configdir, sheet_name='init_state_table',  engine='openpyxl')
            init_state_table = init_state_table.replace(np.nan, '', regex=True).values.tolist()
            resp = niraapad_pb2.ConfigGetterResp(resp=str(init_state_table))
        
        return resp


    @staticmethod
    def print_exception(e):
        print(">>>>>")
        print("Exception:")
        print(e)
        print("<<<<<", flush=True)


class NiraapadReplayServicerExact(niraapad_pb2_grpc.NiraapadServicer):
    """Provides methods that implement functionality of n9 server."""

    trace_metadata_length = 132  # bytes

    def __init__(self, tracedir):
        print("Initializing NiraapadReplayServicerExact", flush=True)
        self.tracedir = tracedir

        self.backend_instances = {}
        self.tracer = Tracer(tracedir)

        trace_msg = niraapad_pb2.StartServerTraceMsg()
        self.tracer.write_to_file(trace_msg)

    def sim_trace(self, start, id):
        resp = self.trace_dict[id].resp
        while default_timer(
        ) - start < self.trace_dict[id].profile.exec_time_sec:
            continue
        return resp

    def LoadTrace(self, req, context):
        try:
            self.trace_dict = Tracer.get_trace_dict(
                os.path.join(self.tracedir, req.trace_file))
            return niraapad_pb2.LoadTraceResp(status=True)
        except Exception as e:
            print("Error: LoadTrace failed with exception: %s" % e)
            return niraapad_pb2.LoadTraceResp(status=False)

    def stop_tracing(self):
        trace_msg = niraapad_pb2.StopServerTraceMsg()
        self.tracer.write_to_file(trace_msg)
        self.tracer.stop_tracing()

    def log_trace_msg(self, trace_msg, elapsed=0):
        self.tracer.write_to_file(trace_msg)

    def BatchedTrace(self, batched_trace_msg, context):
        trace_msgs = pickle.loads(batched_trace_msg.trace_msgs)
        for trace_msg in trace_msgs:
            print("(trace) %s.%s" %
                  (trace_msg.req.backend_type, Tracer.get_msg_type(trace_msg)))
            self.log_trace_msg(trace_msg)
        return niraapad_pb2.EmptyMsg()

    def StaticMethod(self, req, context):
        print("%s.%s" % (req.backend_type, req.method_name), flush=True)


        args = pickle.loads(req.args)
        kwargs = pickle.loads(req.kwargs)

        resp = None
        exception = None

        start = default_timer()
        resp = self.sim_trace(start, req.id)
        end = default_timer()

        profile = niraapad_pb2.CommandProfile(mo=int(utils.MO.VIA_MIDDLEBOX),
                                              exec_time_sec=(end - start))

        trace_msg = niraapad_pb2.StaticMethodTraceMsg(req=req,
                                                      resp=resp,
                                                      profile=profile)
        self.log_trace_msg(trace_msg)

        return resp

    def StaticGetter(self, req, context):
        print("%s.get_%s" % (req.backend_type, req.property_name), flush=True)


        resp = None
        exception = None

        start = default_timer()
        resp = self.sim_trace(start, req.id)
        end = default_timer()

        profile = niraapad_pb2.CommandProfile(mo=int(utils.MO.VIA_MIDDLEBOX),
                                              exec_time_sec=(end - start))

        trace_msg = niraapad_pb2.StaticGetterTraceMsg(req=req,
                                                      resp=resp,
                                                      profile=profile)

        self.log_trace_msg(trace_msg)

        return resp

    def StaticSetter(self, req, context):
        print("%s.set_%s" % (req.backend_type, req.property_name), flush=True)


        value = pickle.loads(req.value)

        resp = None
        exception = None

        start = default_timer()
        resp = self.sim_trace(start, req.id)
        end = default_timer()

        profile = niraapad_pb2.CommandProfile(mo=int(utils.MO.VIA_MIDDLEBOX),
                                              exec_time_sec=(end - start))

        trace_msg = niraapad_pb2.StaticSetterTraceMsg(req=req,
                                                      resp=resp,
                                                      profile=profile)
        self.log_trace_msg(trace_msg)

        return resp

    def Initialize(self, req, context):
        print("%s.__init__" % (req.backend_type), flush=True)

        # Since the __init__ function is invoked similar to static methods,
        # that is, it is invoked using the class name, this function is
        # analogous to the static_method function above, except that we do not
        # need a variable for the method name, which is known to be "__init__"
        # in this case.


        args = pickle.loads(req.args)
        kwargs = pickle.loads(req.kwargs)

        if req.backend_type not in self.backend_instances:
            self.backend_instances[req.backend_type] = {}

        exception = None

        start = default_timer()
        resp = self.sim_trace(start, req.id)
        end = default_timer()

        profile = niraapad_pb2.CommandProfile(mo=int(utils.MO.VIA_MIDDLEBOX),
                                              exec_time_sec=(end - start))

        trace_msg = niraapad_pb2.InitializeTraceMsg(req=req,
                                                    resp=resp,
                                                    profile=profile)
        self.log_trace_msg(trace_msg)

        return resp

    def Uninitialize(self, req, context):
        print("%s.__del__" % (req.backend_type), flush=True)


        exception = None

        backend_type = req.backend_type
        backend_instance_id = req.backend_instance_id

        start = default_timer()
        resp = self.sim_trace(start, req.id)
        end = default_timer()

        profile = niraapad_pb2.CommandProfile(mo=int(utils.MO.VIA_MIDDLEBOX),
                                              exec_time_sec=(end - start))

        trace_msg = niraapad_pb2.UninitializeTraceMsg(req=req,
                                                      resp=resp,
                                                      profile=profile)
        self.log_trace_msg(trace_msg)

        return resp

    def GenericMethod(self, req, context):
        print("%s.%s" % (req.backend_type, req.method_name), flush=True)

        # For any generic class instance method, the logic is similar to that
        # of any generic static method, except that the method is invoked using
        # the class instance name and not directly using the class name.
        # Thus, the following set of statements is analogous to the function
        # definition of the static_methods function above, except that we deal
        # with specific class instances identified using their unique
        # identifiers ("backend_instance_id"), which were set during
        # initialization.


        args = pickle.loads(req.args)
        kwargs = pickle.loads(req.kwargs)

        resp = None
        exception = None

        start = default_timer()
        resp = self.sim_trace(start, req.id)
        end = default_timer()

        profile = niraapad_pb2.CommandProfile(mo=int(utils.MO.VIA_MIDDLEBOX),
                                              exec_time_sec=(end - start))

        trace_msg = niraapad_pb2.GenericMethodTraceMsg(req=req,
                                                       resp=resp,
                                                       profile=profile)
        self.log_trace_msg(trace_msg)

        return resp

    def GenericGetter(self, req, context):
        print("%s.get_%s" % (req.backend_type, req.property_name), flush=True)


        # Getter functions are an extremely simplified version of GenericMethod
        # since they are interpreted not as functions but as variables, which
        # may be used in an expression; in this case, we simply return the
        # variable value.

        resp = None
        exception = None

        start = default_timer()
        resp = self.sim_trace(start, req.id)
        end = default_timer()

        profile = niraapad_pb2.CommandProfile(mo=int(utils.MO.VIA_MIDDLEBOX),
                                              exec_time_sec=(end - start))

        trace_msg = niraapad_pb2.GenericGetterTraceMsg(req=req,
                                                       resp=resp,
                                                       profile=profile)
        self.log_trace_msg(trace_msg)

        return resp

    def GenericSetter(self, req, context):
        print("%s.set_%s" % (req.backend_type, req.property_name), flush=True)


        # Setter functions are the opposite of getter functions. They simply
        # assign the provided value to the specified property.

        value = pickle.loads(req.value)

        resp = None
        exception = None

        start = default_timer()
        resp = self.sim_trace(start, req.id)
        end = default_timer()

        profile = niraapad_pb2.CommandProfile(mo=int(utils.MO.VIA_MIDDLEBOX),
                                              exec_time_sec=(end - start))

        trace_msg = niraapad_pb2.GenericSetterTraceMsg(req=req,
                                                       resp=resp,
                                                       profile=profile)
        self.log_trace_msg(trace_msg)

        return resp
    


# class NiraapadReplayServicer(niraapad_pb2_grpc.NiraapadServicer):
#     """Provides methods that implement functionality of n9 replay server."""

#     def __init__(self, tracedir):
#         print("Initializing NiraapadReplayServicer", flush=True)
#         self.tracedir = tracedir

#     def sim_trace(self, id):
#         try:
#             start = default_timer()
#             resp = self.trace_dict[id].resp
#             while default_timer(
#             ) - start < self.trace_dict[id].profile.exec_time_sec:
#                 continue
#             return resp
#         except Exception as e:
#             print("Error: sim_trace failed with exception: %s" % e)
#             exit(1)

#     def LoadTrace(self, req, context):
#         try:
#             self.trace_dict = Tracer.get_trace_dict(
#                 os.path.join(self.tracedir, req.trace_file))
#             return niraapad_pb2.LoadTraceResp(status=True)
#         except Exception as e:
#             print("Error: LoadTrace failed with exception: %s" % e)
#             return niraapad_pb2.LoadTraceResp(status=False)

#     def StaticMethod(self, req, context):
#         print("%s.%s" % (req.backend_type, req.method_name), flush=True)
#         return self.sim_trace(req.id)

#     def StaticGetter(self, req, context):
#         print("%s.get_%s" % (req.backend_type, req.property_name), flush=True)
#         return self.sim_trace(req.id)

#     def StaticSetter(self, req, context):
#         print("%s.set_%s" % (req.backend_type, req.property_name), flush=True)
#         return self.sim_trace(req.id)

#     def Initialize(self, req, context):
#         print("%s.__init__" % (req.backend_type), flush=True)
#         return self.sim_trace(req.id)

#     def Uninitialize(self, req, context):
#         print("%s.__del__" % (req.backend_type), flush=True)
#         return self.sim_trace(req.id)

#     def GenericMethod(self, req, context):
#         print("%s.%s" % (req.backend_type, req.method_name), flush=True)
#         return self.sim_trace(req.id)

#     def GenericGetter(self, req, context):
#         print("%s.get_%s" % (req.backend_type, req.property_name), flush=True)
#         return self.sim_trace(req.id)

#     def GenericSetter(self, req, context):
#         print("%s.get_%s" % (req.backend_type, req.property_name), flush=True)
#         return self.sim_trace(req.id)

#     def stop_tracing(self):
#         pass


class NiraapadServer:

    def __init__(self, port, tracedir, configdir, keysdir=None, replay=False, ids = '0'):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        self.ids = ids

        if keysdir == None:
            self.server.add_insecure_port('[::]:' + str(port))

        else:
            self.keysdir = keysdir
            server_key_path = os.path.join(self.keysdir, "server.key")
            server_crt_path = os.path.join(self.keysdir, "server.crt")

            with open(server_key_path, 'rb') as f:
                private_key = f.read()
            with open(server_crt_path, 'rb') as f:
                certificate_chain = f.read()
            server_credentials = grpc.ssl_server_credentials(
                ((private_key, certificate_chain),))
            self.server.add_secure_port('[::]:' + str(port), server_credentials)

        if replay == True:
            self.niraapad_servicer = NiraapadReplayServicerExact(tracedir=tracedir)
        else:
            self.niraapad_servicer = NiraapadServicer(tracedir=tracedir, ids=ids, configdir=configdir)

        niraapad_pb2_grpc.add_NiraapadServicer_to_server(
            self.niraapad_servicer, self.server)

        

    def start(self,  wait=False):
        print("NiraapadServer::start", flush=True)
        self.server.start()

        # cleanly blocks the calling thread until the server terminates
        if wait:
            print("NiraapadServer::start waiting for termination", flush=True)
            self.server.wait_for_termination()

    def stop(self):
        print("NiraapadServer::stop", flush=True)
        if self.ids == '1':
            self.niraapad_servicer.file_name.close()
        self.niraapad_servicer.stop_tracing()
        self.niraapad_servicer.delete_context()
        print("Stop gRPC server", flush=True)
        
        timeout_sec = 10
        event = self.server.stop(timeout_sec)
        event.wait(timeout_sec)
        print("Stopped gRPC server (or timed out)", flush=True)
        sys.exit()

    def stop_tracing(self):
        print("NiraapadServer::stop_tracing", flush=True)
        self.niraapad_servicer.stop_tracing()

    def get_trace_file(self):
        return self.niraapad_servicer.tracer.trace_file
