class SensorData:

    DATA_UNITS = {
        1: ('Lux', 'λ'),
        4: ('Ω', 'G'),
        6: ('tVOC', 'ppb'),
        7: ('°C', '%'),
        9: ('°C', '°C'),
        10: ('bpm', 'bpm'),
        11: ('Lux', 'λ'),
    }

    DATA_DESC = {
        1: ('Lux', 'UV Index'),
        4: ('Resistance', 'Conductance'),
        6: ('VOC', 'CO2'),
        7: ('Ambient Temperature', 'Humidity'),
        9: ('IR Temperature', 'Ambient Temperature'),
        10: ('Heartrate', 'Heartrate'),
        11: ('Lux', 'UV Index'),
    }
    
    def __init__(self, sensor_type, data_value, unit_type = 0):
        self.sensor_type = sensor_type
        self.data_value = data_value
        self.data_unit = self.DATA_UNITS[sensor_type][unit_type]
        self.desc = self.DATA_DESC[sensor_type][unit_type]
    
    def __str__(self):
        return 'SensorData(sensor_type = {}, data_value = {}, data_unit = {}, desc = {})'.format(
            self.sensor_type, 
            self.data_value, 
            self.data_unit,
            self.desc
        )
    
    def __repr__(self):
        return 'SensorData(sensor_type = {}, data_value = {}, data_unit = {}, desc = {})'.format(
            self.sensor_type, 
            self.data_value, 
            self.data_unit,
            self.desc
        )

    def __round__(self, dp = 2):
        if (self.data_value != None) or (self.data_value != ''):
            self.data_value = round(self.data_value, dp)