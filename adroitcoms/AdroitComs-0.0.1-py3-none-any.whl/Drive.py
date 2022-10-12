from .Constants import *
from can import Message


class AdroitDrive:
    def __init__(self, address):
        self.addr = address
        self.position = 0
        self.velocity = 0
        self.effort = 0
        self.motor_current = 0
        self.bus_voltage = 0
        self.bus_current = 0
        self.temperature = 0
        self.max_velocity = DEFAULT_DRIVE_VEL
        self.max_effort = 0
        self.max_motor_current = MAX_DRIVE_CURRENT
        self.state = NO_STATE

    def set_max_velocity(self, velocity):
        self.max_velocity = velocity

    def set_max_effort(self, effort):
        self.max_effort = effort

    def set_max_motor_current(self, motor_current):
        self.max_motor_current = motor_current

    def get_state_cmd(self, state):
        if state < NO_STATE or state > NUM_STATES:
            raise ValueError("Invalid state {}".format(state))
        return Message(
            arbitration_id=(STATE_CHANGE_CMD << 7) | (self.addr & 0x7F),
            is_extended_id=False,
            data=[state],
        )

    def get_control_cmd(
        self, position,
    ):
        position_fp = int(position * INT16_MAX / POSITION_CONV)
        velocity_fp = int(self.max_velocity * INT16_MAX / VELOCITY_CONV)
        effort_fp = int(self.max_effort * INT16_MAX / EFFORT_CONV)
        motor_current_fp = int(self.max_motor_current * INT16_MAX / CURRENT_CONV)
        return Message(
            arbitration_id=(CONTROL_CMD << 7) | (self.addr & 0x7F),
            is_extended_id=False,
            data=[
                position_fp & 0xFF,
                (position_fp >> 8) & 0xFF,
                velocity_fp & 0xFF,
                (velocity_fp >> 8) & 0xFF,
                effort_fp & 0xFF,
                (effort_fp >> 8) & 0xFF,
                motor_current_fp & 0xFF,
                (motor_current_fp >> 8) & 0xFF,
            ],
        )

    def get_impedance_cmd(self, inertia, damping, stiffness):
        # INT16_MAX may need to be cast to a float
        inertia_fp = int(inertia * INT16_MAX / INERTIA_CONV)
        damping_fp = int(damping * INT16_MAX / DAMPING_CONV)
        stiffness_fp = int(stiffness * INT16_MAX / STIFFNESS_CONV)
        return Message(
            arbitration_id=(IMPEDANCE_CMD << 7) | (self.addr & 0x7F),
            is_extended_id=False,
            data=[
                inertia_fp & 0xFF,
                (inertia_fp >> 8) & 0xFF,
                damping_fp & 0xFF,
                (damping_fp >> 8) & 0xFF,
                stiffness_fp & 0xFF,
                (stiffness_fp >> 8) & 0xFF,
            ],
        )

    def process_telem(self, msg):
        msg_id = (msg.arbitration_id >> 7) & 0x0F
        if msg_id == ERROR_TELEM:
            self.process_error_telem(msg)
        elif msg_id == HIGH_SPEED_TELEM:
            self.process_hs_telem(msg)
        elif msg_id == MEDIUM_SPEED_TELEM:
            self.process_ms_telem(msg)
        elif msg_id == LOW_SPEED_TELEM:
            self.process_ls_telem(msg)
        elif msg_id == DEBUG_TELEM:
            self.process_debug_telem(msg)
        elif msg_id == PARAMETER_TELEM:
            self.process_parameter_telem(msg)
        elif msg_id == STATUS_TELEM:
            self.process_status_telem(msg)
        elif msg_id == CONTROL_CMD:
            self.process_control_cmd(msg)

    def process_error_telem(self, msg):
        print("Recieved error message:")
        print(msg)

    def process_hs_telem(self, msg):
        if msg.dlc == 8:
            position_fp = int.from_bytes(msg.data[:2], 'little', signed=True)
            velocity_fp = int.from_bytes(msg.data[2:4], 'little', signed=True)
            effort_fp = int.from_bytes(msg.data[4:6], 'little', signed=True)
            motor_current_fp = int.from_bytes(msg.data[6:], 'little', signed=True)
            self.position = position_fp / INT16_MAX * POSITION_CONV
            self.velocity = velocity_fp / INT16_MAX * VELOCITY_CONV
            self.effort = effort_fp / INT16_MAX * EFFORT_CONV
            self.motor_current = motor_current_fp / INT16_MAX * CURRENT_CONV

    def process_ms_telem(self, msg):
        pass

    def process_ls_telem(self, msg):
        if msg.dlc == 6:
            bus_voltage_fp = int.from_bytes(msg.data[:2], 'little', signed=True)
            bus_current_fp = int.from_bytes(msg.data[2:4], 'little', signed=True)
            temperature_fp = int.from_bytes(msg.data[4:], 'little', signed=True)
            self.bus_voltage = bus_voltage_fp / INT16_MAX * VOLTAGE_CONV
            self.bus_current = bus_current_fp / INT16_MAX * CURRENT_CONV
            self.temperature = temperature_fp / INT16_MAX * TEMPERATURE_CONV

    def process_debug_telem(self, msg):
        print("Recieved debug message:")
        print(msg)

    def process_parameter_telem(self, msg):
        print("Recieved parameter message:")
        print(msg)

    def process_status_telem(self, msg):
        if msg.dlc == 1:
            self.state = msg.data[0]

    def process_control_cmd(self, msg):
        print("Recieved control message:")
        print(msg)
