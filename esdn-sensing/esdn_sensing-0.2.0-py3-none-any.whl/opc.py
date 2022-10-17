"""
`opc`
================================================================================

*Python library for OPC-Nx (2-3) Air Quality Sensor.*

**Author(s):** `Colby Sawyer <https://github.com/ColbySawyer7>`_

Implementation Notes
--------------------
**Hardware:**
`OPC-N3 <https://www.alphasense.com/products/optical-particle-counter/>`_

**Software and Dependencies:**
Utilizing py-opc-ng library based on work from `Fargiolas@Github <https://github.com/fargiolas/py-opc-ng>`_
"""

from time import sleep
import logging
from usbiss.spi import SPI
import opcng as opc
from esdn_sensing.sensor_error import SensorError


def sensor_run(sample_size):
    """Runs the sensor specific operations and collects/summarizes the data.

    Args:
        sample_size (int, mandatory): [Sample size (seconds) of collection]

    Returns:
        [int]: [Returns array of integers mapped to the corresponding values ([avg_pm1, avg_pm25,avg_pm10, temperature, humidity, laser_status])]
    """
    spi = SPI('/dev/ttyACM0')
    spi.mode = 1
    spi.max_speed_hz = 500000
    spi.lsbfirst = False

    dev = opc.detect(spi)

    logging.debug(f'device information: {dev.info()}')
    logging.debug(f'serial: {dev.serial()}')
    logging.debug(f'firmware version: {dev.serial()}')

    total_pm1 = 0
    total_pm25 = 0
    total_pm10 = 0

    # power on fan and laser
    dev.on()

    for i in range(sample_size):
        # query particle mass readings
        sleep(1)
        full_read = dev.pm()
        logging.debug(full_read)
        if i != 0:    
            total_pm1 = total_pm1 + full_read['PM1']
            total_pm25 = total_pm25 + full_read['PM2.5']
            total_pm10 = total_pm10 +  full_read['PM10']

    histogram = dev.histogram()
    temperature = histogram['Temperature']
    humidity = histogram['Relative humidity']
    laser_status = histogram['Laser status']

    # power off fan and laser
    dev.off()

    res = [0] * 6
    avg_pm1 = total_pm1/sample_size
    avg_pm25 = total_pm25/sample_size
    avg_pm10 = total_pm10/sample_size
    
    logging.debug(f'Average PM1: {avg_pm1}')
    logging.debug(f'Average PM2.5: {avg_pm25}')
    logging.debug(f'Average PM10: {avg_pm10}')
    logging.debug(f'Temperature: {temperature}')
    logging.debug(f'Humidity: {humidity}')
    logging.debug(f'Laser Status: {laser_status}')

    res[0] = avg_pm1
    res[1] = avg_pm25
    res[2] = avg_pm10
    res[3] = temperature
    res[4] = humidity
    res[5] = laser_status

    return res

class OPC:
    """Driver class for OPC particulate sensors
    """
    avg_pm1 = 0
    avg_pm25 = 0
    avg_pm10 = 0
    temperature = 0
    humidity = 0
    laser_status= 0

    def init(self, avg_pm1=0, avg_pm25=0,avg_pm10=0, temperature=0, humidity=0, laser_status=0):
        """Initialize instance of sensor

        Args:
            avg_pm1 (int, optional): Average PM1. Defaults to 0.
            avg_pm25 (int, optional): Average PM2.5. Defaults to 0.
            avg_pm10 (int, optional): Average PM10. Defaults to 0.
            temperature (int, optional): Temperature. Defaults to 0.
            humidity (int, optional): Humidity. Defaults to 0.
            laser_status (int, optional): Laser Status Code. Defaults to 0.
        """
        self.avg_pm1= avg_pm1
        self.avg_pm25= avg_pm25
        self.avg_pm10= avg_pm10
        self.temperature = temperature
        self.humidity= humidity
        self.laser_status= laser_status

    def get_data(self, sample_size=10, dec_factor=100):
        """Collects data from the device attached via the sensor_run method

        Args:
            sample_size (int, optional): [Sample size (seconds) of collection]. Defaults to 10.
            dec_factor (int, optional): [Holds the decimal factor to be used for integer conversion]. Defaults to 100.

        Returns:
           [Bytearray]: [Packaged up data to be sent via LoRa driving code]
        """
        try:
            sensor_readings = sensor_run(sample_size)

            self.avg_pm1 = sensor_readings[0]
            self.avg_pm25 = sensor_readings[1] 
            self.avg_pm10 = sensor_readings[2]
            self.temperature = sensor_readings[3]
            self.humidity = sensor_readings[4]
            self.laser_status = sensor_readings[5]


            avg_pm1 = int((self.avg_pm1*dec_factor))
            logging.debug("avg_pm1: %0.1f %%" % avg_pm1)

            avg_pm25 = int((self.avg_pm25*dec_factor))
            logging.debug("avg_pm25: %0.1f %%" % avg_pm25)

            avg_pm10 = int((self.avg_pm10*dec_factor))
            logging.debug("avg_pm10: %0.1f %%" % avg_pm10)

            temperature = int((self.temperature*dec_factor))
            logging.debug("temperature: %0.1f %%" % temperature)

            humidity = int((self.humidity*dec_factor))
            logging.debug("humidity: %0.1f %%" % humidity)

            laser_status = int((self.laser_status*dec_factor))
            logging.debug("laser_status: %0.1f %%" % laser_status)


            sensor_data = bytearray(12)

            sensor_data[0] = (avg_pm1 >> 8) & 0xff
            sensor_data[1]= avg_pm1 & 0xff
            
            sensor_data[2] = (avg_pm25 >> 8) & 0xff
            sensor_data[3] = avg_pm25 & 0xff

            sensor_data[4] = (avg_pm10 >> 8) & 0xff
            sensor_data[5] = avg_pm10 & 0xff

            sensor_data[6] = (temperature >> 8) & 0xff
            sensor_data[7] = temperature & 0xff

            sensor_data[8] = (humidity >> 8) & 0xff
            sensor_data[9] = humidity & 0xff

            sensor_data[10] = (laser_status >> 8) & 0xff
            sensor_data[11] = laser_status & 0xff

            return sensor_data

        except:
            raise SensorError('Unable to connect')
