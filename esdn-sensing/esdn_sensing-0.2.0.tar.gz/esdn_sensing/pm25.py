"""
`pm25`
================================================================================

Python library for PM25 Air Quality Sensor.

**Author(s):** `Colby Sawyer <https://github.com/ColbySawyer7>`_

Implementation Notes
--------------------
**Hardware:**
PMSA003I Air Quality `More Information <https://www.adafruit.com/product/4632>`_

**Software and Dependencies:**

"""

# pylint: disable=unused-import
import time
import serial
import logging
import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_pm25.i2c import PM25_I2C
from esdn_sensing import SensorError

def sensor_run(sample_size):
    """Runs the sensor specific operations and collects/summarizes the data.

    Args:
        sample_size (int, mandatory): Sample size (seconds) of collection

    Raises:
        SensorError: Raises error if sensor is unreachable

    Returns:
        [float]: Returns library storing ["pm10 standard", "pm25 standard","pm100 standard","pm10 env","pm25 env","pm100 env","particles 03um","particles 05um","particles 10um","particles 25um","particles 50um","particles 100um"]
    """
    reset_pin = None
    # If you have a GPIO, its not a bad idea to connect it to the RESET pin

    # reset_pin = DigitalInOut(board.G0)
    # reset_pin.direction = Direction.OUTPUT
    # reset_pin.value = False

    # For use with Raspberry Pi/Linux:
    uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.25)


    # Connect to a PM2.5 sensor over UART
    # from adafruit_pm25.uart import PM25_UART
    # pm25 = PM25_UART(uart, reset_pin)

    # Create library object, use 'slow' 100KHz frequency!
    i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)
    # Connect to a PM2.5 sensor over I2C
    pm25 = PM25_I2C(i2c, reset_pin)

    logging.debug("Found PM2.5 sensor, reading data...")

    try:
        aqdata = pm25.read()
        logging.debug("Concentration Units (standard)")
        logging.debug("---------------------------------------")
        logging.debug(
            "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
            % (aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"])
        )
        logging.debug("Concentration Units (environmental)")
        logging.debug("---------------------------------------")
        logging.debug(
            "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
            % (aqdata["pm10 env"], aqdata["pm25 env"], aqdata["pm100 env"])
        )
        logging.debug("---------------------------------------")
        logging.debug("Particles > 0.3um / 0.1L air:", aqdata["particles 03um"])
        logging.debug("Particles > 0.5um / 0.1L air:", aqdata["particles 05um"])
        logging.debug("Particles > 1.0um / 0.1L air:", aqdata["particles 10um"])
        logging.debug("Particles > 2.5um / 0.1L air:", aqdata["particles 25um"])
        logging.debug("Particles > 5.0um / 0.1L air:", aqdata["particles 50um"])
        logging.debug("Particles > 10 um / 0.1L air:", aqdata["particles 100um"])

        return aqdata
    except:
        raise SensorError('Unable to connect')

class PM25:
    """Driver class for PM 2.5 Sensor particulate sensors
    """
    pm10_std= 0
    pm25_std= 0
    pm100_std= 0
    pm10_env= 0
    pm25_env= 0
    pm100_env= 0
    part_03um= 0
    part_05um= 0
    part_10um= 0
    part_25um= 0
    part_50um= 0
    part_100um= 0

    def __init__(self,pm10_std= 0,pm25_std= 0,pm100_std= 0,pm10_env= 0,pm25_env= 0,pm100_env= 0,part_03um= 0,part_05um= 0,part_10um= 0,part_25um= 0,part_50um= 0,part_100um= 0):
        """_summary_

        Args:
            pm10_std (int, optional):  . Defaults to 0.
            pm25_std (int, optional):  . Defaults to 0.
            pm100_std (int, optional):  . Defaults to 0.
            pm10_env (int, optional):  . Defaults to 0.
            pm25_env (int, optional):  . Defaults to 0.
            pm100_env (int, optional):  . Defaults to 0.
            part_03um (int, optional):  . Defaults to 0.
            part_05um (int, optional):  . Defaults to 0.
            part_10um (int, optional):  . Defaults to 0.
            part_25um (int, optional):  . Defaults to 0.
            part_50um (int, optional):  . Defaults to 0.
            part_100um (int, optional):  . Defaults to 0.
        """
    
        self.pm10_std= 0
        self.pm25_std= 0
        self.pm100_std= 0
        self.pm10_env= 0
        self.pm25_env= 0
        self.pm100_env= 0
        self.part_03um= 0
        self.part_05um= 0
        self.part_10um= 0
        self.part_25um= 0
        self.part_50um= 0
        self.part_100um= 0

    def get_data(self, sample_size=10,dec_factor=100):
        """Collects data from PM2.5 Sensor and packages for transmission

        Args:
            sample_size (int, optional): Size of sample in seconds. Defaults to 10.
            dec_factor (int, optional): Holds the decimal factor to be used for integer conversion. Defaults to 100.

        Raises:
            SensorError: Raise error if sensor is unreachable

        Returns:
            bytearray :  Packaged up data to be sent via LoRa driving code
        """

        try:
            aqdata = sensor_run(sample_size)
            self.pm10_std= aqdata["pm10 standard"]
            self.pm25_std= aqdata["pm25 standard"]
            self.pm100_std= aqdata["pm100 standard"]
            self.pm10_env= aqdata["pm10 env"]
            self.pm25_env= aqdata["pm25 env"]
            self.pm100_env= aqdata["pm100 env"]
            self.part_03um= aqdata["particles 03um"]
            self.part_05um= aqdata["particles 05um"]
            self.part_10um= aqdata["particles 10um"]
            self.part_25um= aqdata["particles 25um"]
            self.part_50um= aqdata["particles 50um"]
            self.part_100um= aqdata["particles 100um"]

            pm10_std = int((self.pm10_std*dec_factor))
            logging.debug("pm10 standard: %0.1f %%" % pm10_std)

            pm25_std = int((self.pm25_std*dec_factor))
            logging.debug("pm25 standard: %0.1f %%" % pm25_std)

            pm100_std = int((self.pm100_std*dec_factor))
            logging.debug("pm100 standard: %0.1f %%" % pm100_std)

            pm10_env = int((self.pm10_env*dec_factor))
            logging.debug("pm10 env: %0.1f %%" % pm10_env)

            pm25_env = int((self.pm25_env*dec_factor))
            logging.debug("pm25 env: %0.1f %%" % pm25_env)

            pm100_env = int((self.pm100_env*dec_factor))
            logging.debug("pm100 env: %0.1f %%" % pm100_env)

            part_03um = int((self.part_03um*dec_factor))
            logging.debug("Particles > 0.3um / 0.1L air:: %0.1f %%" % part_03um)

            part_05um = int((self.part_05um*dec_factor))
            logging.debug("Particles > 0.5um / 0.1L air:: %0.1f %%" % part_05um)

            part_10um = int((self.part_10um*dec_factor))
            logging.debug("Particles > 1.0um / 0.1L air:: %0.1f %%" % part_10um)

            part_25um = int((self.part_25um*dec_factor))
            logging.debug("Particles > 2.5um / 0.1L air:: %0.1f %%" % part_25um)

            part_50um = int((self.part_50um*dec_factor))
            logging.debug("Particles > 5.0um / 0.1L air:: %0.1f %%" % part_50um)

            part_100um = int((self.part_100um*dec_factor))
            logging.debug("Particles > 10.0um / 0.1L air:: %0.1f %%" % part_100um)
 
            #print(aqdata)
            sensor_data = bytearray(24)

            sensor_data[0] = (pm10_std >> 8) & 0xff
            sensor_data[1]= pm10_std & 0xff
            
            sensor_data[2] = (pm25_std >> 8) & 0xff
            sensor_data[3] = pm25_std & 0xff
            
            sensor_data[4] = (pm100_std >> 8) & 0xff
            sensor_data[5] = pm100_std & 0xff

            sensor_data[6] = (pm10_env >> 8) & 0xff
            sensor_data[7] = pm10_env & 0xff

            sensor_data[8] = (pm25_env >> 8) & 0xff
            sensor_data[9] = pm25_env & 0xff

            sensor_data[10] = (pm100_env >> 8) & 0xff
            sensor_data[11] = pm100_env & 0xff

            sensor_data[12] = (part_03um >> 8) & 0xff
            sensor_data[13] = part_03um & 0xff

            sensor_data[14] = (part_05um >> 8) & 0xff
            sensor_data[15] = part_05um & 0xff

            sensor_data[16] = (part_10um >> 8) & 0xff
            sensor_data[17] = part_10um & 0xff

            sensor_data[18] = (part_25um >> 8) & 0xff
            sensor_data[19] = part_25um & 0xff

            sensor_data[20] = (part_50um >> 8) & 0xff
            sensor_data[21] = part_50um & 0xff

            sensor_data[22] = (part_100um >> 8) & 0xff
            sensor_data[23] = part_100um & 0xff

            return sensor_data

        except: 
            raise SensorError('Unable to read')
