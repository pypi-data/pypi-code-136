from .Drive import AdroitDrive
from .Constants import *
import can
import numpy as np
from threading import Thread
from .Util import usleep

__all__ = ["AdroitComs"]


class AdroitComs:
    def __init__(self, drives, *args, **kwargs):
        self.bus = can.Bus(*args, **kwargs)
        self.drives = [AdroitDrive(i + 1) for i in range(drives)]
        self.broadcast = AdroitDrive(BROADCAST_ADDR)
        self.tx = []
        self.rx = []
        self.threads = []
        self.run = True
        self.start(self.io_handler)
        self.start(self.telem_handler)

    def start(self, target):
        thread = Thread(target=target)
        thread.daemon = True
        thread.start()
        self.threads.append(thread)

    def send(self, msg):
        self.tx.append(msg)

    def get_drives(self, drive):
        if drive is None:
            return self.drives
        elif drive == "broadcast":
            return [self.broadcast]
        elif isinstance(drive, int):
            if drive >= len(self.drives):
                raise ValueError("drive is larger than the number of conncected drives")
            return [self.drives[drive]]
        else:
            raise ValueError(
                "drive must be either, None, 'broadcast', or a drive number."
            )

    def reset(self):
        self.send(self.broadcast.get_state_cmd(INIT_STATE))
        while len(self.tx):
            pass
        usleep(INIT_WAIT_TIME)
        for drive in self.drives:
            self.send(drive.get_state_cmd(STARTUP_STATE))
        while len(self.tx):
            pass
        usleep(2 * INIT_WAIT_TIME)
        return np.all((STARTUP_STATE < self.state) & (self.state < FAULT_STATE))

    def send_state_cmd(self, state, drive=None):
        for d in self.get_drives(drive):
            self.send(d.get_state_cmd(state))

    def send_control_cmd(self, position, drive=None):
        for d, pos, in zip(self.get_drives(drive), position):
            self.send(d.get_control_cmd(pos))

    def set_max(self, setting, value, drive):
        drives = self.get_drives(drive)
        if isinstance(value, (float, int)):
            value = len(drives) * [value]
        for d, v in zip(drives, value):
            getattr(d, "set_max_" + setting)(v)

    def set_max_velocity(self, velocity, drive=None):
        self.set_max("velocity", velocity, drive)

    def set_max_effort(self, effort, drive=None):
        self.set_max("effort", effort, drive)

    def set_max_motor_current(self, motor_current, drive=None):
        self.set_max("motor_current", motor_current, drive)

    def send_impedance_cmd(self, inertia, damping, stiffness, drive=None):
        for d in self.get_drives(drive):
            self.send(d.get_impedance_cmd(inertia, damping, stiffness))

    def shutdown(self):
        self.run = False

    def io_handler(self):
        while self.run:
            if len(self.tx):
                self.bus.send(self.tx.pop(0), 0)
        self.bus.shutdown()

    def telem_handler(self):
        while self.run:
            recv = self.bus.recv(1)
            if recv is not None:
                self.process_telem(recv)

    def process_telem(self, msg):
        addr = msg.arbitration_id & 0x7F
        if addr == 0:
            self.broadcast.process_telem(msg)
        elif addr <= len(self.drives):
            self.drives[addr - 1].process_telem(msg)

    def get_telem(self, attrib):
        telem = np.zeros((len(self.drives,)))
        for i, drive in enumerate(self.drives):
            telem[i] = getattr(drive, attrib)
        return telem

    @property
    def position(self):
        return self.get_telem("position")

    @property
    def velocity(self):
        return self.get_telem("velocity")

    @property
    def effort(self):
        return self.get_telem("effort")

    @property
    def motor_current(self):
        return self.get_telem("motor_current")

    @property
    def bus_voltage(self):
        return self.get_telem("bus_voltage")

    @property
    def bus_current(self):
        return self.get_telem("bus_current")

    @property
    def temperature(self):
        return self.get_telem("temperature")

    @property
    def state(self):
        return self.get_telem("state")
