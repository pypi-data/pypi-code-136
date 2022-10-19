import socket
class IoTGreenhouse(object):
    """IoT Greenhouse data object"""
    def __init__(self, id=None, name=None): 
        self.id = id
        host_name = socket.gethostname()
        if "Greenhouse" in host_name:
            self.name = host_name
            self.group = self.name[-4:-2]
            self.number = self.name[-2:]
        elif name:
            self.name = name
            self.group = "xx"
            self.number = "00"
        else:
            self.name = "testGH"
            self.group = "xx"
            self.number = "00"
        #house state
        self.led_red_state = None
        self.led_red_status = None
        self.led_white_state = None
        self.led_white_status = None
        self.led_dual_state = None
        self.led_dual_status = None
        self.switch_pb_state = None
        self.switch_pb_status = None
        self.switch_toggle_state = None
        self.switch_toggle_status = None
        self.fan_state = None
        self.fan_status = None
        self.servo_position = None
        self.servo_status = None
        self.heater_state = None
        self.heater_status = None
        self.buzzer_state = None
        self.buzzer_status = None
        self.ain_pot_raw = None
        self.ain_light_raw = None
        self.ain_aux_raw = None
        self.temp_inside_C = None
        self.temp_inside_F = None
        self.temp_outside_C = None
        self.temp_outside_F = None
        self.last_update = None
        self.message = None

    
