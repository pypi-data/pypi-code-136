#  Copyright (c) 2021-2022 ETH Zurich, SIS ID and HVL D-ITET
#
"""
Tests for .dev sub-package technix
"""
import logging
from time import sleep

import pytest

from hvl_ccb.dev.technix import (
    Technix,
    TechnixError,
    TechnixTelnetCommunication,
    TechnixSerialCommunication,
    TechnixSerialCommunicationConfig,
)
from hvl_ccb.dev.technix.base import _Status, _GetRegisters
from masked_comm import LocalTechnixServer
from masked_comm.serial import TechnixLoopSerialCommunication
from masked_comm.uitls import get_free_tcp_port

logging.basicConfig(level=logging.DEBUG)


@pytest.fixture(scope="function")
def com_telnet():
    host = "127.0.0.1"
    return {
        "host": host,
        "port": get_free_tcp_port(host),
        "timeout": 0.01,
        "wait_sec_read_text_nonempty": 0.01,
        "default_n_attempts_read_text_nonempty": 2,
    }


@pytest.fixture(scope="module")
def com_serial():
    return {
        "port": "loop://?logging=debug",
        "baudrate": 9600,
        "parity": TechnixSerialCommunicationConfig.Parity.NONE,
        "stopbits": TechnixSerialCommunicationConfig.Stopbits.ONE,
        "bytesize": TechnixSerialCommunicationConfig.Bytesize.EIGHTBITS,
        "timeout": 0.01,
        "wait_sec_read_text_nonempty": 0.01,
        "default_n_attempts_read_text_nonempty": 2,
    }


@pytest.fixture(scope="module")
def dev_config_telnet():
    return {
        "max_voltage": 10000,
        "max_current": 1.5,
        "communication_channel": TechnixTelnetCommunication,
        "post_stop_pause_sec": 0.01,
        "register_pulse_time": 0.01,
        "polling_interval_sec": 1,
    }


@pytest.fixture(scope="module")
def dev_config_serial():
    return {
        "max_voltage": 10000,
        "max_current": 1.5,
        "communication_channel": TechnixSerialCommunication,
        "post_stop_pause_sec": 0.01,
        "register_pulse_time": 0.01,
    }


@pytest.fixture()
def start_technix_telnet(com_telnet, dev_config_telnet):
    ts = LocalTechnixServer(port=com_telnet["port"], timeout=com_telnet["timeout"])
    with ts:
        tex = Technix(com_telnet, dev_config_telnet)
        ts._starting.join()
        with tex:
            tex.query_status()
            yield ts, tex


def test_mockup(start_technix_telnet):
    ts, tex = start_technix_telnet

    tex.query_status()


def test_devices(start_technix_telnet):
    ts, tex = start_technix_telnet
    assert ts is not None
    assert tex.__class__ is Technix

    assert tex.is_started
    tex.start()
    tex.query_status()

    tex.stop()
    assert not tex.is_started


def test_no_properties(start_technix_telnet):
    ts, tex = start_technix_telnet
    """Device is not fully started, statuses are None"""
    tex.stop()

    assert tex.voltage_regulation is None
    assert tex.output is None
    assert tex.remote is None
    assert tex.inhibit is None
    assert tex.open_interlock is None

    assert tex.voltage is None
    assert tex.current is None


def test_wrong_command(start_technix_telnet):
    ts, tex = start_technix_telnet

    listen_and_repeat_backup = ts.listen_and_repeat

    with pytest.raises(TechnixError):
        tex.com.query("no_register")
    with pytest.raises(TechnixError):
        ts.custom_answer = "P7,1"
        ts.listen_and_repeat = ()
        tex.inhibit = True
    with pytest.raises(TechnixError):
        ts.custom_answer = "P7,1"
        ts.listen_and_repeat = ()
        tex._get_register(_GetRegisters.VOLTAGE)

    ts.listen_and_repeat = listen_and_repeat_backup


def test_watchdog(start_technix_telnet):
    ts, tex = start_technix_telnet
    assert tex.is_started

    ts.status = 0b010
    sleep(2)
    assert not tex._status_poller.is_polling()
    assert not tex.is_started


def test_status(start_technix_telnet):
    ts, tex = start_technix_telnet

    # Wrong status byte
    with pytest.raises(ValueError):
        ts.status = 1000
        tex.query_status()

    # Correct status
    value = 38
    assert value == 0b00100110
    ts.status = value
    tex.query_status()
    assert tex.status == _Status(
        False, not False, True, False, False, True, True, False, None, None
    )
    assert tex.inhibit is False
    assert tex.remote is True
    assert tex.output is False
    assert tex.open_interlock is True
    assert tex.voltage_regulation is False

    # Status fault and closed interlock
    with pytest.raises(TechnixError):
        ts.status = 0b010
        tex.query_status()


def test_voltage_current(start_technix_telnet):
    ts, tex = start_technix_telnet

    tex.query_status()

    assert tex.max_voltage == 10000
    assert tex.max_current == 1.5

    ts.custom_answer = "d1,102"
    tex.voltage = 250
    assert ts.last_request == "d1,102"

    ts.custom_answer = "d2,2730"
    tex.current = 1
    assert ts.last_request == "d2,2730"

    ts.custom_answer = "a12048"
    assert int(tex.voltage) == 5001
    assert ts.last_request == "a1"

    ts.custom_answer = "a23000"
    assert int(tex.current * 1000) == 1098
    assert ts.last_request == "a2"

    with pytest.raises(ValueError):
        tex.voltage = 1e6
    with pytest.raises(ValueError):
        tex.current = 1e6


def test_voltage_current_with_status(start_technix_telnet):
    ts, tex = start_technix_telnet

    from hvl_ccb.configuration import _force_value

    _force_value(tex.config, "read_output_while_polling", True)

    ts.voltage = 819
    ts.current = 2730

    tex.query_status()
    assert tex.voltage == 2000
    assert tex.current == 1


def test_hv_remote_inhibit(start_technix_telnet):
    ts, tex = start_technix_telnet

    tex.output = True
    tex.output = False
    tex.remote = True
    tex.remote = False
    tex.inhibit = True
    tex.inhibit = False

    with pytest.raises(TypeError):
        tex.output = 100
    with pytest.raises(TypeError):
        tex.remote = 1
    with pytest.raises(TypeError):
        tex.inhibit = "ON"


def start_serial_devices(com_serial, dev_config_serial):
    com = TechnixLoopSerialCommunication(com_serial)
    com.open()

    tex = Technix(com, dev_config_serial)

    com.put_text("P7,0")
    com.put_text("P6,1")
    com.put_text("P6,0")
    com.put_text("P8,0")
    com.put_text("E0")  # status byte for the polling thread
    tex.start()
    assert com.get_written() == "P7,0"
    assert com.get_written() == "P6,1"
    assert com.get_written() == "P6,0"
    assert com.get_written() == "P8,0"
    sleep(0.1)  # time for the polling thread to start
    assert com.get_written() == "E"
    return com, tex


def test_serial(com_serial, dev_config_serial):
    com, tex = start_serial_devices(com_serial, dev_config_serial)

    com.put_text("P6,1")
    com.put_text("P6,0")
    com.put_text("P7,1")
    tex.stop()
    assert com.get_written() == "P6,1"
    assert com.get_written() == "P6,0"
    assert com.get_written() == "P7,1"

    com.close()
