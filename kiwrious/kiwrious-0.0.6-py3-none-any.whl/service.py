from serial.tools import list_ports
from .sensor import KiwriousSensor
from .utility import *

import threading
import time

class KiwriousService:
    '''Responsible for identifying and connecting sensors'''

    UV = 11
    CONDUCTIVITY = 4
    AIR_QUALITY = 6
    HUMIDITY = 7
    TEMPERATURE = 9
    HEART_RATE = 10
    
    class ServiceThread(threading.Thread):
        '''ServiceThread for maintaining list of connected sensors'''

        def __init__(self, service, thread_type, conclude, method, *args):
            threading.Thread.__init__(self)
            if isinstance(service, KiwriousService):
                self.service = service
                self.thread_type = thread_type
                self.conclude = conclude
                self.method = method
                self.args = args
            else:
                raise
            self.running = True

        def run(self):
            try:
                if self.thread_type == 'persistent':
                    while self.running:
                        self.method(*self.args)
                elif self.thread_type == 'single':
                    self.method(*self.args)
                    if self.conclude: self.service.stop_service()
                self.service = None
            except:
                self.running = False
                self.service = None
                raise

    def __init__(self):
        '''Initialise KiwriousService object'''
        self.connected_sensors = {}
        self.type_map = {
            1: [],
            4: [],
            6: [],
            7: [],
            9: [],
            10: [],
            11: []
        }
        self.service_threads = {}

        self.on_sensor_connection_callback = None
        self.on_sensor_connection_args = None

        self.on_sensor_disconnection_callback = None
        self.on_sensor_disconnection_args = None

    def start_service(self):
        '''Start ServiceThread'''
        if self.service_threads: 
            if self.service_threads['UpdateThread'].running:
                raise
        
        self.service_threads['UpdateThread'] = KiwriousService.ServiceThread(self, 'persistent', False, self.update_connected_sensors)
        self.service_threads['UpdateThread'].start()

        time.sleep(1)

    def stop_service(self):
        '''Stop ServiceThread'''
        time.sleep(1)
        if self.service_threads:
            for thread in self.service_threads.values():
                thread.running = False

        remove_devs = list(self.connected_sensors.keys())
        
        for dev in remove_devs:
            self.connected_sensors.pop(dev, None).terminate_thread()

    def update_connected_sensors(self):
        '''Update the list of connected sensors'''
        connected_devices = set(list_ports.comports())
        registered_devices = set(self.connected_sensors.keys())

        disconnected_devices = registered_devices - connected_devices
        for dev in disconnected_devices:
            '''On sensor connect callback function'''
            if self.on_sensor_disconnection_callback != None and (
                self.on_sensor_disconnection_callback['type'] == 0 or 
                self.on_sensor_disconnection_callback['type'] == self.connected_sensors[dev].sensor_type
            ):
                time.sleep(0.1)
                self.service_threads['OnDisconnectionThread'] = KiwriousService.ServiceThread(
                    self, 
                    'single',
                    self.on_sensor_disconnection_callback['conclude'],
                    self.on_sensor_disconnection_callback['callback'],
                    *self.on_sensor_disconnection_callback['args']
                )
                self.service_threads['OnDisconnectionThread'].start()
                self.on_sensor_disconnection_callback = None

            self.type_map[self.connected_sensors[dev].sensor_type].remove(self.connected_sensors[dev])
            self.connected_sensors.pop(dev, None).terminate_thread()

        new_devices = connected_devices - registered_devices
        for dev in new_devices:
            if dev.pid == 60441 and dev.vid == 1240:
                time.sleep(0.1)
                self.connected_sensors[dev] = KiwriousSensor(dev, self)
                time.sleep(0.1)
                self.type_map[self.connected_sensors[dev].sensor_type] += [self.connected_sensors[dev]]

                '''On sensor connect callback function'''
                if self.on_sensor_connection_callback != None and (
                    self.on_sensor_connection_callback['type'] == 0 or 
                    self.on_sensor_connection_callback['type'] == self.connected_sensors[dev].sensor_type
                ):
                    time.sleep(0.1)
                    self.service_threads['OnConnectionThread'] = KiwriousService.ServiceThread(
                        self, 
                        'single',
                        self.on_sensor_connection_callback['conclude'],
                        self.on_sensor_connection_callback['callback'],
                        *self.on_sensor_connection_callback['args']
                    )
                    self.service_threads['OnConnectionThread'].start()
                    self.on_sensor_connection_callback = None
        
        time.sleep(0.1) # NOTE: breaks when removed

    def get_raw_data(self, sensor_type):
        '''Return a list of raw packet data as a byte string'''
        return [sensor.sensor_packet for sensor in self.type_map[sensor_type]] 

    def get_connected_sensors(self):
        '''Return a list of connected sensors as KiwriousSensor objects'''
        return [self.connected_sensors[sensor] for sensor in self.connected_sensors.keys()]

    def get_sensor_reading(self, sensor_type = None):
        '''Return a list of SensorData objects for the requested sensor if available'''
        if sensor_type != None: return [sensor.sensor_data for sensor in self.type_map[sensor_type]]
        return [sensor.sensor_data for sensor in self.connected_sensors.values()]

    def on_sensor_connection(self, callback, sensor_type = 0, timeout = 0, close_on_completion = False, *args):
        '''Set a user-defined callback for on sensor connection'''
        self.on_sensor_connection_callback = {'callback': callback, 'args': args, 'type': sensor_type, 'conclude': close_on_completion}

        while (self.on_sensor_connection_callback != None) and timeout != 0:
            time.sleep(1)
            timeout -= 1
            if timeout == 0: raise Exception('Sensor connect timed out')

    def on_sensor_disconnection(self, callback, sensor_type = 0, timeout = 0, close_on_completion = False, *args):
        '''Set a user-defined callback for on sensor disconnection'''
        self.on_sensor_disconnection_callback = {'callback': callback, 'args': args, 'type': sensor_type, 'conclude': close_on_completion}

        while (self.on_sensor_disconnection_callback != None) and timeout != 0:
            time.sleep(1)
            timeout -= 1
            if timeout == 0: raise Exception('Sensor disconnect timed out')