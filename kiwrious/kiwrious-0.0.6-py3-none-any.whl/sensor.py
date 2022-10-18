from .sensordata import SensorData
from .utility import *

from serial import Serial, serialutil
import time
import threading


class KiwriousSensor:
    '''Responsible for data decoding and presentation'''

    sensor_names = {
        1: 'UV',
        4: 'CONDUCTIVITY',
        6: 'AIR_QUALITY',
        7: 'HUMIDITY',
        9: 'TEMPERATURE',
        10: 'HEART_RATE',
        11: 'UV'
    }

    class SensorThread(threading.Thread):
        '''SensorThread for updateing sensors values'''

        def __init__(self, sensor):
            threading.Thread.__init__(self)
            if isinstance(sensor, KiwriousSensor):
                self.sensor = sensor
            else:
                raise
            self.running = True

        def run(self):
            try:
                while self.running:
                    self.sensor.update_data()
                self.sensor = None
            except:
                self.running = False
                self.sensor = None
                raise


    def __init__(self, sensor, service):
        

        self.sensor = sensor
        self.service = service
        self.sensor_packet = None
        self.sensor_data_method = None

        try:
            self.__comm_port = Serial(self.sensor.device, 115200)

            self.__read_data(self.__comm_port.read(26))
            
            self.sensor_type = int(self.sensor_packet[4:6], 16)

        except:
            self.service.stop_service()
            raise

        self.sensor_data = None
        self.sensor_thread = None
        
        if (self.sensor_type == 1) or (self.sensor_type == 11):
            '''Initilise value as UV'''
            lux = SensorData(self.sensor_type, to_float32(self.sensor_packet[12:20]), 0)
            uv_index = SensorData(self.sensor_type, to_float32(self.sensor_packet[20:28]), 1)
            self.sensor_data = (lux, uv_index)
            self.sensor_data_method = self.__get_uv_data

        elif self.sensor_type == 4:
            '''Initilise value as Conductance'''
            resistance_value = round(to_int16_r(self.sensor_packet[12:16]) * to_int16_r(self.sensor_packet[16:20]),2)
            resistance = SensorData(self.sensor_type, round(resistance_value, 2), 0)
            conductance = SensorData(self.sensor_type, round((1/resistance_value) * 1000000, 2) if resistance_value else 0, 1)
            self.sensor_data = (resistance, conductance)
            self.sensor_data_method = self.__get_conductivity_data

        elif self.sensor_type == 6:
            '''Initilise value as Air Quality'''
            voc = SensorData(self.sensor_type, to_unsigned_int16(self.sensor_packet[12:16]), 0)
            co2 = SensorData(self.sensor_type, to_unsigned_int16(self.sensor_packet[16:20]), 1)
            self.sensor_data = (voc, co2)
            self.sensor_data_method = self.__get_air_quality_data

        elif self.sensor_type == 7:
            '''Initilise value as Humidity'''
            ambient_temperature = SensorData(self.sensor_type, to_int16(self.sensor_packet[12:16]) / 100, 0)
            humidity = SensorData(self.sensor_type, to_int16(self.sensor_packet[16:20]) / 100, 1)
            self.sensor_data = (ambient_temperature, humidity)
            self.sensor_data_method = self.__get_humidity_data

        elif self.sensor_type == 9:
            '''Initilise value as Temperature'''
            ir_temperature = SensorData(self.sensor_type, ir_calc(self.sensor_packet[16:44]), 0)
            ambient_temperature = SensorData(self.sensor_type, to_int16(self.sensor_packet[12:16]) / 100, 1)
            self.sensor_data = (ir_temperature, ambient_temperature)
            self.sensor_data_method = self.__get_temperature_data

        elif self.sensor_type == 10:
            '''Initilise value as Heart Rate'''
            heartrate1 = SensorData(self.sensor_type, 0, 0)
            heartrate2 = SensorData(self.sensor_type, 1, 1)
            self.sensor_data = (heartrate1, heartrate2)
            self.sensor_data_method = self.__get_heartrate_data

        else:
            raise IndexError('sensor type not valid')

        self.sensor_thread = KiwriousSensor.SensorThread(self)
        self.sensor_thread.start()

    def __str__(self):
        return 'KiwriousSensor' + str(self.sensor_names[self.sensor_type])

    def __repr__(self):
        return 'KiwriousSensor' + str(self.sensor_names[self.sensor_type])

    def terminate_thread(self):
        '''Stop SensorThread and close comm_port'''
        if self.sensor_thread is not None:
            self.sensor_thread.running = False

        while not self.sensor_thread.sensor == None:
            time.sleep(0.1)

        if not self.__comm_port.closed:
            self.__comm_port.close()

    def update_data(self):
        '''Updates SensorData object'''

        try:
            r = self.__comm_port.read(26)

            '''If comm port reponds with none'''
            if r == b'':
                raise Exception('closed comm port')
            
            self.__read_data(r)
            
            self.sensor_data_method()

        except serialutil.SerialException:
            pass
        except:
            if self.sensor_thread.running:
                self.terminate_thread()

    def __get_uv_data(self):
        '''Update the SensorData objects using light protocol'''
        self.sensor_data[0].data_value = (to_float32(self.sensor_packet[12:20]))
        self.sensor_data[1].data_value = (to_float32(self.sensor_packet[20:28]))
    
    def __get_conductivity_data(self):
        '''Update the SensorData objects using conductivity protocol'''
        resistance_value = round(to_int16_r(self.sensor_packet[12:16]) * to_int16_r(self.sensor_packet[16:20]),2)

        self.sensor_data[0].data_value = resistance_value
        self.sensor_data[1].data_value = (round((1/resistance_value) * 1000000, 2)) if resistance_value else 0

    def __get_air_quality_data(self):
        '''Update the SensorData objects using air quality protocol'''
        self.sensor_data[0].data_value = (to_unsigned_int16(self.sensor_packet[12:16]))
        self.sensor_data[1].data_value = (to_unsigned_int16(self.sensor_packet[16:20]))

    def __get_humidity_data(self):
        '''Update the SensorData objects using humidity protocol'''
        self.sensor_data[0].data_value = to_int16(self.sensor_packet[12:16]) / 100
        self.sensor_data[1].data_value = to_int16(self.sensor_packet[16:20]) / 100

    def __get_temperature_data(self):
        '''Update the SensorData objects using temperature protocol'''
        self.sensor_data[0].data_value = ir_calc(self.sensor_packet[16:44])
        self.sensor_data[1].data_value = to_int16(self.sensor_packet[12:16]) / 100
    
    def __get_heartrate_data(self):
        '''Update the SensorData objects using heartrate protocol'''
        self.sensor_data[0].data_value = (0)
        self.sensor_data[1].data_value = (1)

    def __read_data(self, r):
        '''Validate packet data and convert to hex string'''
        r = r.hex()

        if r == '':
            raise ValueError('ERROR: Empty packet')

        if r[0:4] != '0a0a':
            self.terminate_thread()
            raise ValueError('ERROR: Invalid packet header')

        if r[48:52] != '0b0b':
            self.terminate_thread()
            raise ValueError('ERROR: Invalid packet footer')

        self.sensor_packet = r
