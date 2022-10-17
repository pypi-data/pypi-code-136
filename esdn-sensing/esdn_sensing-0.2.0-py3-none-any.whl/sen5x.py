"""
`sen5x`
================================================================================

*Python library for Sensirion SEN5xAir Quality Sensor.*

**Author(s):** `Colby Sawyer <https://github.com/ColbySawyer7>`_

Implementation Notes
--------------------
**Hardware:**
`Sensirion SEN-5x <https://sensirion.com/products/catalog/SEN54/>`_

**Software and Dependencies:**
Utilizing Sensirion provided libraries. `More Information <https://sensirion.github.io/python-i2c-driver/>`_

"""


import time
import logging
from sensirion_i2c_driver import I2cConnection, LinuxI2cTransceiver
from sensirion_i2c_sen5x import Sen5xI2cDevice
from esdn_sensing.sensor_error import SensorError

def sensor_run(sample_size):
    """Runs the sensor specific operations and collects/summarizes the data.

    Args:
        sample_size (int, mandatory): Sample size (seconds) of collection

    Returns:
        [int]: Returns array of integers mapped to the corresponding values ([avg_pm1, avg_pm25,avg_pm10, temperature, humidity, laser_status])
    """
    with LinuxI2cTransceiver('/dev/i2c-1') as i2c_transceiver:
        device = Sen5xI2cDevice(I2cConnection(i2c_transceiver))

        # Print some device information
        logging.debug("Version: {}".format(device.get_version()))
        logging.debug("Product Name: {}".format(device.get_product_name()))
        logging.debug("Serial Number: {}".format(device.get_serial_number()))

        # Perform a device reset (reboot firmware)
        device.device_reset()

        sum_mc_1p0 = 0
        sum_mc_2p5 = 0
        sum_mc_4p0 = 0
        sum_mc_10p0 = 0
        sum_ambient_rh = 0
        sum_ambient_t = 0
        sum_voc_index = 0
        #sum_nox_index = 0

        # Start measurement
        device.start_measurement()
        for i in range(sample_size):
            # Wait until next result is available
            logging.debug("Waiting for new data...")
            while device.read_data_ready() is False:
                time.sleep(0.1)

            # Read measured values -> clears the "data ready" flag
            values = device.read_measured_values()
            logging.debug(values)

            mc_1p0 = values.mass_concentration_1p0.physical
            mc_2p5 = values.mass_concentration_2p5.physical
            mc_4p0 = values.mass_concentration_4p0.physical
            mc_10p0 = values.mass_concentration_10p0.physical
            ambient_rh = values.ambient_humidity.percent_rh
            ambient_t = values.ambient_temperature.degrees_celsius
            voc_index = values.voc_index.scaled
            #nox_index = values.nox_index.scaled

            sum_mc_1p0 = sum_mc_1p0 + mc_1p0
            sum_mc_2p5 = sum_mc_2p5 + mc_2p5
            sum_mc_4p0 = sum_mc_4p0 + mc_4p0
            sum_mc_10p0 = sum_mc_10p0 + mc_10p0
            sum_ambient_rh = sum_ambient_rh + ambient_rh
            sum_ambient_t = sum_ambient_t + ambient_t
            sum_voc_index = sum_voc_index + voc_index
            #sum_nox_index = sum_nox_index + nox_index

            # Read device status
            status = device.read_device_status()
            logging.debug("Device Status: {}\n".format(status))

        # Stop measurement
        device.stop_measurement()
        logging.debug("Measurement stopped.")

        avg_mc_1p0 = sum_mc_1p0 /sample_size
        avg_mc_2p5 = sum_mc_2p5 /sample_size
        avg_mc_4p0 = sum_mc_4p0 /sample_size
        avg_mc_10p0 = sum_mc_10p0 /sample_size
        avg_ambient_rh = sum_ambient_rh /sample_size
        avg_ambient_t = sum_ambient_t /sample_size
        avg_voc_index = sum_voc_index /sample_size
        #avg_nox_index = sum_nox_index /sample_size

        return [avg_mc_1p0, avg_mc_2p5, avg_mc_4p0, avg_mc_10p0, avg_ambient_rh, avg_ambient_t, avg_voc_index]

class SEN5x:
    """Driver class for SEN5x particulate sensors
    """
    mc_1p0= 0
    mc_2p5= 0
    mc_4p0= 0
    mc_10p0= 0
    ambient_rh= 0
    ambient_t= 0
    voc_index= 0
    nox_index= 0


    def __init__(self,mc_1p0= 0,mc_2p5= 0,mc_4p0= 0,mc_10p0= 0,ambient_rh= 0,ambient_t= 0,voc_index= 0):
        """_summary_

        Args:
            mc_1p0 (int, optional):  . Defaults to 0.
            mc_2p5 (int, optional):  . Defaults to 0.
            mc_4p0 (int, optional):  . Defaults to 0.
            mc_10p0 (int, optional):  . Defaults to 0.
            ambient_rh (int, optional):  . Defaults to 0.
            ambient_t (int, optional):  . Defaults to 0.
            voc_index (int, optional):  . Defaults to 0.
            nox_index (int, optional):  . Defaults to 0.
        """
    
        self.mc_1p0= mc_1p0
        self.mc_2p5= mc_2p5
        self.mc_4p0= mc_4p0
        self.mc_10p0= mc_10p0
        self.ambient_rh= ambient_rh
        self.ambient_t= ambient_t
        self.voc_index= voc_index
        #self.nox_index= nox_index

    def get_data(self, sample_size=10, dec_factor=100):
        """Collects data from SEN5x device

        Args:
            sample_size (int, optional): _description_. Defaults to 10.
            dec_factor (int, optional): _description_. Defaults to 100.

        Raises:
            SensorError: Raise error if sensor is unreachable

        Returns:
            bytearray :  Packaged up data to be sent via LoRa driving code
        """
        try:
            sensor_readings = sensor_run(sample_size)
            #[mc_1p0, mc_2p5,mc_4p0, mc_10p0, ambient_rh, ambient_t, voc_index, nox_index]

            self.mc_1p0= sensor_readings[0]
            self.mc_2p5= sensor_readings[1]
            self.mc_4p0= sensor_readings[2]
            self.mc_10p0= sensor_readings[3]
            self.ambient_rh= sensor_readings[4]
            self.ambient_t= sensor_readings[5]
            self.voc_index= sensor_readings[6]
            #self.nox_index= sensor_readings[7]


            mc_1p0 = int((self.mc_1p0*dec_factor))
            logging.debug("mc_1p0: %0.1f %%" % mc_1p0)

            mc_2p5 = int((self.mc_2p5*dec_factor))
            logging.debug("mc_2p5: %0.1f %%" % mc_2p5)

            mc_4p0 = int((self.mc_4p0*dec_factor))
            logging.debug("mc_4p0: %0.1f %%" % mc_4p0)

            mc_10p0 = int((self.mc_10p0*dec_factor))
            logging.debug("mc_10p0: %0.1f %%" % mc_10p0)

            ambient_rh = int((self.ambient_rh*dec_factor))
            logging.debug("ambient_rh: %0.1f %%" % ambient_rh)

            ambient_t = int((self.ambient_t*dec_factor))
            logging.debug("ambient_t: %0.1f %%" % ambient_t)

            voc_index = int((self.voc_index*dec_factor))
            logging.debug("voc_index: %0.1f %%" % voc_index)

            #nox_index = int((self.nox_index*dec_factor))
            #logging.info("nox_index: %0.1f %%" % nox_index)

            sensor_data = bytearray(14)

            sensor_data[0] = (mc_1p0 >> 8) & 0xff
            sensor_data[1]= mc_1p0 & 0xff
            
            sensor_data[2] = (mc_2p5 >> 8) & 0xff
            sensor_data[3] = mc_2p5 & 0xff
            
            sensor_data[4] = (mc_4p0 >> 8) & 0xff
            sensor_data[5] = mc_4p0 & 0xff

            sensor_data[6] = (mc_10p0 >> 8) & 0xff
            sensor_data[7] = mc_10p0 & 0xff

            sensor_data[8] = (ambient_rh >> 8) & 0xff
            sensor_data[9] = ambient_rh & 0xff

            sensor_data[10] = (ambient_t >> 8) & 0xff
            sensor_data[11] = ambient_t & 0xff

            sensor_data[12] = (voc_index >> 8) & 0xff
            sensor_data[13] = voc_index & 0xff

            #sensor_data[14] = (nox_index >> 8) & 0xff
            #sensor_data[15] = nox_index & 0xff

            return sensor_data

        except:
            raise SensorError('Unable to connect')
