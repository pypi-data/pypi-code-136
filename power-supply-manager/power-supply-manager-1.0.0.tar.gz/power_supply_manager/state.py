"""
Copyright 2022 DevBuildZero, LLC

Permission is hereby granted, free of charge, to any person obtaining a copy of 
this software and associated documentation files (the "Software"), to deal in 
the Software without restriction, including without limitation the rights to 
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies 
of the Software, and to permit persons to whom the Software is furnished to do 
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER 
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN 
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import json
import os
import time
import csv
from datetime import datetime
import dearpygui.dearpygui as dpg

from power_supply_manager.device import *
from power_supply_manager.demo_device import *


class GuiState:
    """Stores state variables for the application"""

    def __init__(self):
        self.theme = GuiTheme()
        # Initialize an empty array to hold PowerSupply objects
        self.supplies = [None] * 10
        self.hosts = [None] * 10
        self.config: dict = {}
        self.groups = []
        # Holds value of Channels input box before PS is created
        self.channels_input = []
        # Used for saving config files
        self.config_filename = "my_config"
        # Data logging
        self.file_handle = None
        self.csv = None

    def help(self, message):
        """Creates a GUI tooltip dialog for the last_item"""
        last_item = dpg.last_item()
        group = dpg.add_group(horizontal=True)
        dpg.move_item(last_item, parent=group)
        with dpg.tooltip(last_item):
            dpg.add_text(self._split_message(message))

    def _split_message(self, message: str, max_line_length=50) -> str:
        """Splits a tooltip message into multiple lines"""
        if len(message) > max_line_length:
            message = "\n".join(
                message[i : i + max_line_length]
                for i in range(0, len(message), max_line_length)
            )
        return message

    def load_config(self, filepath: str) -> None:
        """Loads device configuration from file and removes any existing devices"""
        logger.debug(f"Deleting existing supplies...")
        self.channels_input.clear()
        # Delete all existing supplies
        for i in range(1, len(self.supplies) + 1):
            self._delete_supply(i)
            if dpg.does_item_exist(f"ps{i}"):
                dpg.delete_item(f"ps{i}")
        logger.debug(f"Loading configuration state...")
        # Read config from file
        with open(filepath, "r") as json_file:
            config = json.load(json_file)
        self.config = config

        # Create new PS headers
        for i in range(len(self.config)):
            self.hosts[i] = self.config[i].get("host")
            self.add_ps_header()

    def start_logging(self) -> None:
        """Logs measurements to CSV file. Format:
        CSV(timestamp, PS<num> CH<num> <name>, ...
             <time>, <voltage>, <current>
        """
        logger.debug(f"Entering start_logging callback...")
        datestamp = str(datetime.now().isoformat()).replace(":", "-")
        # Close existing handle, if open, and open new one
        self.stop_logging()
        filename = f"{datestamp}.csv"
        self.file_handle = open(filename, "w")
        self.csv = csv.writer(self.file_handle)

        # Write header row
        header_row = ["Datestamp"]
        for ps in self.supplies:
            if ps:
                for ch in ps.channels:
                    prefix = f"PS{ps.num} CH{ch.num} {ch.name}".strip()
                    header_row.append(prefix + " Voltage")
                    header_row.append(prefix + " Current")
        self.csv.writerow(header_row)

    def stop_logging(self) -> None:
        """Stops CSV measurement logging"""
        logger.debug(f"Entering stop_logging callback...")
        if self.file_handle:
            self.file_handle.close()
            self.file_handle = None
            self.csv = None

    def config_selection(self, sender, app_data, user_data) -> None:
        """Callback to select configuration file path to load from"""
        logger.debug(f"Entering config_selection callback...")
        self.load_config(app_data.get("file_path_name"))

    def store_config_filename(self, sender, app_data, user_data) -> None:
        """Call back to select configuration file path to save to"""
        logger.debug(f"Entering store_config_filename callback...")
        self.config_filename = dpg.get_value(sender)

    def dump_config(self, sender, app_data, user_data) -> None:
        """Dumps current configuration of devices in JSON format"""
        logger.debug(f"Entering dump_config callback...")
        filename = self.config_filename
        if not filename.endswith(".json"):
            filename = filename + ".json"
        filepath = os.path.join(app_data.get("file_path_name"), filename)
        config = []
        for ps in self.supplies:
            if ps:
                channels = []
                for ch in ps.channels:
                    channels.append(
                        {
                            "name": ch.name,
                            "voltage": ch.voltage_set,
                            "current": ch.current_set,
                            "ovp": ch.ovp_set,
                            "ocp": ch.ocp_set,
                            "ovp_on": ch.ovp_on,
                            "ocp_on": ch.ocp_on,
                            "seq_on": ch.seq_on,
                            "seq_off": ch.seq_off,
                        }
                    )
                config.append({"host": ps.host, "channels": channels})

        with open(filepath, "w") as json_file:
            json.dump(config, json_file)

    def on_gui_close(self, sender, app_data, user_data) -> None:
        """Callback for closing GUI"""
        logger.debug(f"Entering on_gui_close callback...")
        dpg.delete_item(sender)

    def all_on(self) -> None:
        """Powers on all channels of all supplies"""
        logger.debug(f"Entering all_on callback...")
        for supply in self.supplies:
            if supply:
                supply.group_power_state([ch.num for ch in supply.channels], True)

    def all_off(self) -> None:
        """Power off all channels of all supplies"""
        logger.debug(f"Entering all_off callback...")
        for supply in self.supplies:
            if supply:
                supply.group_power_state([ch.num for ch in supply.channels], False)

    def group_on(self) -> None:
        """Power on all Grouped channels"""
        logger.debug(f"Entering group_on callback...")
        self._group_control(power_on=True)

    def group_off(self) -> None:
        """Power off all Grouped channels"""
        logger.debug(f"Entering group_off callback...")
        self._group_control(power_on=False)

    def _group_control(self, power_on: bool) -> None:
        """Sets power state of all Grouped channels"""
        # Build query strings for each supply
        for supply in self.supplies:
            if supply:
                channels = []
                for t in self.groups:
                    if t[0] == supply.num:
                        channels.append(t[1])
                supply.group_power_state(channels, power_on)

    def sequence_on(self):
        """Begins power on sequence for sequenced channels"""
        logger.debug(f"Entering sequence_on callback...")
        self._sequence_control(power_on=True)

    def sequence_off(self):
        """Begins power off sequence for sequenced channels"""
        logger.debug(f"Entering sequence_off callback...")
        self._sequence_control(power_on=False)

    def _sequence_control(self, power_on: bool):
        """Executes power sequencing for sequenced channels"""
        # Build query strings for each supply
        logger.info(f"Beginning power {'on' if power_on else 'off'} sequence...")
        # Find max sequence delay
        max_delay = 0
        for supply in self.supplies:
            if supply and supply.channels:
                channels = []
                for ch in supply.channels:
                    if power_on and ch.seq_on > 0:
                        max_delay = ch.seq_on if ch.seq_on > max_delay else max_delay
                    elif not power_on and ch.seq_off > 0:
                        max_delay = ch.seq_off if ch.seq_off > max_delay else max_delay
        # Perform power sequence
        for i in range(max_delay + 1):
            for supply in self.supplies:
                if supply:
                    channels = []
                    for ch in supply.channels:
                        if power_on and ch.seq_on == i:
                            channels.append(ch.num)
                        elif not power_on and ch.seq_off == i:
                            channels.append(ch.num)
                    if channels:
                        logger.info(
                            f"Sequence step {i} / {max_delay}: Powering {'on' if power_on else 'off'} supply {supply.num} channels {channels}"
                        )
                        supply.group_power_state(channels, power_on)
            time.sleep(1)

    def add_ps_header(self) -> None:
        """Adds a GUI header for a new supply"""
        logger.debug(f"Entering add_ps_header callback...")
        id = len(self.channels_input) + 1
        # Get num_channels from config if it exists
        if self.config and self.config[id - 1]:
            default_num_channels = len(self.config[id - 1].get("channels"))
        else:
            default_num_channels = 2
        default_host = self.hosts[id - 1] if self.hosts[id - 1] else "demo"
        self.channels_input.append(default_num_channels)
        self.hosts[id - 1] = default_host
        channels_tag = f"ps{id}_num_channels"
        with dpg.collapsing_header(
            label=f"Power Supply {id}",
            default_open=True,
            parent="_primary_wnd",
            tag=f"ps{id}",
        ):
            with dpg.group(horizontal=True):
                dpg.add_text("Host / IP:")
                self.help("Hostname or IP address of the supply.")
                dpg.add_input_text(
                    default_value=default_host,
                    width=150,
                    callback=self.set_host,
                    user_data=id,
                )
                dpg.add_text("Channels:")
                self.help("Number of power supply channels to use.")
                dpg.add_input_text(
                    default_value=str(default_num_channels),
                    width=30,
                    tag=channels_tag,
                    callback=self.set_channels,
                    user_data=id,
                )
                dpg.add_button(
                    label="Connect",
                    callback=self.connect,
                    tag=f"ps{id}_connect",
                )

    def add_channels(self, ps_id: int, num_channels: int) -> None:
        """Add child windows to a power supply header for the provided number of channels"""
        logger.debug(f"Entering add_channels callback...")
        with dpg.tab_bar(parent=f"ps{ps_id}", tag=f"ps{ps_id}_channels"):
            with dpg.tab(label="Configuration"):
                with dpg.group(horizontal=True, width=0):
                    for channel in range(1, num_channels + 1):
                        with dpg.child_window(width=300, height=200):
                            dpg.add_spacer(height=4)
                            with dpg.group(horizontal=True):
                                dpg.add_spacer(width=10)
                                dpg.add_text(f"Channel {channel}")
                                dpg.add_input_text(
                                    hint="Channel Name",
                                    width=130,
                                    tag=f"p{ps_id}c{channel}_name",
                                    callback=self.set_channel_name,
                                    user_data=(ps_id, channel),
                                )
                                button_tag = f"p{ps_id}c{channel}_pwr"
                                theme_tag = button_tag + "_btn"
                                self._create_btn_theme(theme_tag, self.theme.red)
                                dpg.add_button(
                                    tag=button_tag,
                                    label=" Off ",
                                    callback=self.set_output_state,
                                    user_data=(ps_id, channel),
                                )
                                dpg.bind_item_theme(dpg.last_item(), theme_tag)
                            dpg.add_spacer(height=9)
                            with dpg.group(horizontal=True):
                                dpg.add_spacer(width=10)
                                dpg.add_text("Group:")
                                self.help(
                                    "Add/remove channel from Group power control."
                                )
                                dpg.add_checkbox(
                                    label="",
                                    tag=f"p{ps_id}c{channel}_group",
                                    callback=self.manage_power_group,
                                    user_data=(ps_id, channel),
                                )
                                dpg.add_spacer(width=5)
                                dpg.add_text("Seq. On|Off:")
                                self.help(
                                    "Specify the delay (in seconds) for power sequencing for this channel."
                                )
                                dpg.add_input_text(
                                    hint="int",
                                    width=30,
                                    indent=200,
                                    tag=f"p{ps_id}c{channel}_seq_on",
                                    callback=self.set_seq_on,
                                    user_data=(ps_id, channel),
                                )
                                dpg.add_input_text(
                                    hint="int",
                                    width=30,
                                    indent=240,
                                    tag=f"p{ps_id}c{channel}_seq_off",
                                    callback=self.set_seq_off,
                                    user_data=(ps_id, channel),
                                )
                            dpg.add_spacer(height=2)
                            with dpg.group(horizontal=True):
                                dpg.add_spacer(width=10)
                                dpg.add_text("Voltage: ")
                                dpg.add_text(
                                    "0.00 V", tag=f"p{ps_id}c{channel}_voltage_meas"
                                )
                                self.help("Measured voltage")
                                dpg.add_input_text(
                                    default_value="5.0",
                                    width=50,
                                    indent=200,
                                    tag=f"p{ps_id}c{channel}_voltage_set",
                                    callback=self.set_voltage,
                                    user_data=(ps_id, channel),
                                    on_enter=True,
                                )
                                dpg.add_text("V")
                            dpg.add_spacer(height=2)
                            with dpg.group(horizontal=True):
                                dpg.add_spacer(width=10)
                                dpg.add_text("OVP: ")
                                self.help("Over-voltage protection")
                                dpg.add_radio_button(
                                    ["Off", "On"],
                                    horizontal=True,
                                    tag=f"p{ps_id}c{channel}_ovp_state",
                                    callback=self.set_ovp_state,
                                    user_data=(ps_id, channel),
                                )
                                dpg.add_input_text(
                                    default_value="0.0",
                                    width=50,
                                    indent=200,
                                    tag=f"p{ps_id}c{channel}_ovp_set",
                                    callback=self.set_ovp,
                                    user_data=(ps_id, channel),
                                    on_enter=True,
                                )
                                dpg.add_text("V")
                            dpg.add_spacer(height=2)
                            with dpg.group(horizontal=True):
                                dpg.add_spacer(width=10)
                                dpg.add_text("Current: ")
                                dpg.add_text(
                                    "0.00 A", tag=f"p{ps_id}c{channel}_current_meas"
                                )
                                self.help("Measured current")
                                dpg.add_text("")
                                dpg.add_input_text(
                                    default_value="0.5",
                                    width=50,
                                    indent=200,
                                    tag=f"p{ps_id}c{channel}_current_set",
                                    callback=self.set_current,
                                    user_data=(ps_id, channel),
                                    on_enter=True,
                                )
                                dpg.add_text("A")
                            dpg.add_spacer(height=2)
                            with dpg.group(horizontal=True):
                                dpg.add_spacer(width=10)
                                dpg.add_text("OCP: ")
                                self.help("Over-current protection")
                                dpg.add_radio_button(
                                    ["Off", "On"],
                                    horizontal=True,
                                    tag=f"p{ps_id}c{channel}_ocp_state",
                                    callback=self.set_ocp_state,
                                    user_data=(ps_id, channel),
                                )
                                dpg.add_input_text(
                                    default_value="1.0",
                                    width=50,
                                    indent=200,
                                    tag=f"p{ps_id}c{channel}_ocp_set",
                                    callback=self.set_ocp,
                                    user_data=(ps_id, channel),
                                    on_enter=True,
                                )
                                dpg.add_text("A")
            with dpg.tab(label="Monitor"):
                with dpg.group(horizontal=True, width=0):
                    for channel in range(1, num_channels + 1):
                        with dpg.child_window(width=420, height=340):
                            dpg.add_text(
                                f"Channel {channel}", tag=f"p{ps_id}c{channel}_title"
                            )
                            with dpg.plot(no_title=True):
                                dpg.add_plot_legend()
                                dpg.add_plot_axis(
                                    dpg.mvXAxis,
                                    tag=f"p{ps_id}c{channel}_x",
                                )
                                dpg.add_plot_axis(
                                    dpg.mvYAxis,
                                    tag=f"p{ps_id}c{channel}_y_v",
                                    label="Volts",
                                )
                                dpg.add_plot_axis(
                                    dpg.mvYAxis,
                                    tag=f"p{ps_id}c{channel}_y_i",
                                    label="Amps",
                                )
                                dpg.add_line_series(
                                    np.arange(0, BUF_SIZE),
                                    np.zeros(BUF_SIZE),
                                    parent=f"p{ps_id}c{channel}_y_v",
                                    tag=f"p{ps_id}c{channel}_v",
                                    label="v",
                                )
                                dpg.add_line_series(
                                    np.arange(0, BUF_SIZE),
                                    np.zeros(BUF_SIZE),
                                    parent=f"p{ps_id}c{channel}_y_i",
                                    tag=f"p{ps_id}c{channel}_i",
                                    label="i",
                                )

    def manage_power_group(self, sender, app_data, user_data) -> None:
        """Adds/removes channels from Group (based on Group checkbox state)"""
        logger.debug(f"Entering power_group callback...")
        assert len(user_data) == 2
        ps_num = user_data[0]
        channel_num = user_data[1]
        checked = dpg.get_value(sender)
        t = (ps_num, channel_num)
        if checked and t not in self.groups:
            self.groups.append(t)
        elif not checked and t in self.groups:
            self.groups.remove(t)

    def set_seq_on(self, sender, app_data, user_data) -> None:
        """Callback to set the power on sequence time for the provided channel"""
        logger.debug(f"Entering set_seq_on callback...")
        assert len(user_data) == 2
        ps_num = user_data[0]
        channel_num = user_data[1]
        try:
            value = int(dpg.get_value(sender))
            ps = self.supplies[ps_num - 1]
            if ps:
                ps.channels[channel_num - 1].seq_on = value
        except ValueError:
            # Ignore input if not an int
            return

    def set_seq_off(self, sender, app_data, user_data) -> None:
        """Callback to set the power off sequence time for the provided channel"""
        logger.debug(f"Entering set_seq_off callback...")
        assert len(user_data) == 2
        ps_num = user_data[0]
        channel_num = user_data[1]
        value = int(dpg.get_value(sender))
        ps = self.supplies[ps_num - 1]
        if ps:
            ps.channels[channel_num - 1].seq_off = value

    def set_host(self, sender, app_data, user_data) -> None:
        """Callback to set the host / IP of the provided supply"""
        logger.debug(f"Entering set_host callback...")
        ps_num = user_data
        self.hosts[ps_num - 1] = dpg.get_value(sender)
        logger.info(f"Updated host {ps_num - 1}")

    def _create_ps(self, ps_id: int, num_channels: int) -> PowerSupply:
        """Creates and configures a supply object"""
        ps_idx = ps_id - 1
        host = self.hosts[ps_idx]
        if host:
            ps = self._create_supply(ps_id, host, num_channels)

            # Reconfigure PS if we have a config for it
            if self.config and (cfg := self.config[ps_idx]):
                # Wait for PS init
                while not ps.init_done:
                    time.sleep(0.01)
                ps.configure(cfg)
            return ps

    def set_channel_name(self, sender, app_data, user_data) -> None:
        """Callback to set the name of the provided channel"""
        logger.debug(f"Entering set_channel_name callback...")
        assert len(user_data) == 2
        ps_num = user_data[0]
        channel_num = user_data[1]
        ps = self.supplies[ps_num - 1]
        if ps:
            ch = ps.channels[channel_num - 1]
            name = dpg.get_value(sender)
            ch.name = name

    def set_output_state(self, sender, app_data, user_data) -> None:
        """Callback to set the power state of the provided channel"""
        logger.debug(f"Entering set_output_state callback...")
        assert len(user_data) == 2
        ps_num = user_data[0]
        channel_num = user_data[1]
        # Infer desired power state from button color
        if dpg.get_value(sender + "_btn_color") == self.theme.red[0]:
            # Currently off, set state to on
            mode_on = True
        else:
            mode_on = False
        ps = self.supplies[ps_num - 1]
        if ps:
            ps.set_output_state(channel_num, mode_on)

    def set_voltage(self, sender, app_data, user_data) -> None:
        """Callback to set the voltage of the provided channel"""
        logger.debug(f"Entering set_voltage callback...")
        assert len(user_data) == 2
        ps_num = user_data[0]
        channel_num = user_data[1]
        voltage = float(dpg.get_value(sender))
        ps = self.supplies[ps_num - 1]
        if ps:
            ps.set_voltage(channel_num, voltage)

    def set_ovp_state(self, sender, app_data, user_data) -> None:
        """Callback to set the over-voltage protection state of the provided channel"""
        logger.debug(f"Entering set_ovp_state callback...")
        assert len(user_data) == 2
        ps_num = user_data[0]
        channel_num = user_data[1]
        selected_mode = dpg.get_value(sender)
        ps = self.supplies[ps_num - 1]
        if ps:
            ps.set_ovp_state(channel_num, selected_mode == "On")

    def set_ovp(self, sender, app_data, user_data) -> None:
        """Callback to set the over-voltage protection value of the provided channel"""
        logger.debug(f"Entering set_ovp callback...")
        assert len(user_data) == 2
        ps_num = user_data[0]
        channel_num = user_data[1]
        voltage = float(dpg.get_value(sender))
        ps = self.supplies[ps_num - 1]
        if ps:
            ps.set_ovp(channel_num, voltage)

    def set_current(self, sender, app_data, user_data) -> None:
        """Callback to set the current of the provided channel"""
        logger.debug(f"Entering set_current callback...")
        assert len(user_data) == 2
        ps_num = user_data[0]
        channel_num = user_data[1]
        current = float(dpg.get_value(sender))
        ps = self.supplies[ps_num - 1]
        if ps:
            ps.set_current(channel_num, current)

    def set_ocp_state(self, sender, app_data, user_data) -> None:
        """Callback to set the over-current protection value of the provided channel"""
        logger.debug(f"Entering set_ocp_state callback...")
        assert len(user_data) == 2
        ps_num = user_data[0]
        channel_num = user_data[1]
        selected_mode = dpg.get_value(sender)
        ps = self.supplies[ps_num - 1]
        if ps:
            ps.set_ocp_state(channel_num, selected_mode == "On")

    def set_ocp(self, sender, app_data, user_data) -> None:
        """Callback to set the over-current protection value of the provided channel"""
        logger.debug(f"Entering set_ocp callback...")
        assert len(user_data) == 2
        ps_num = user_data[0]
        channel_num = user_data[1]
        current = float(dpg.get_value(sender))
        ps = self.supplies[ps_num - 1]
        if ps:
            ps.set_ocp(channel_num, current)

    def set_power_btn(self, button_tag: str, power_is_on: bool) -> None:
        """Sets the appearance of a channel's power button based
        on the current power state"""
        base_theme_tag = button_tag + "_btn_color"
        if power_is_on == True:
            self._set_btn_colors(base_theme_tag, self.theme.green)
            if dpg.does_item_exist(button_tag):
                dpg.configure_item(button_tag, label=" On ")
        elif power_is_on == False:
            self._set_btn_colors(base_theme_tag, self.theme.red)
            if dpg.does_item_exist(button_tag):
                dpg.configure_item(button_tag, label=" Off ")

    def set_channels(self, sender, app_data, user_data) -> None:
        """Callback to set the number of channels for the provided supply"""
        logger.debug(f"Entering set_channels callback...")
        ps_id = int(user_data)
        try:
            num_channels = int(dpg.get_value(sender))
            self.channels_input[ps_id - 1] = num_channels
        except:
            pass

    def connect(self, sender, app_data, user_data) -> None:
        """Callback to initiate connection to the provided supply"""
        # Get PS ID: Sender is of the form ps{id}_connect
        logger.debug(f"Entering connect callback...")
        id = int(sender.split("_")[0][2:])
        if dpg.get_item_label(sender) == "Connect":
            # Create new PowerSupply
            num_channels = self.channels_input[id - 1]
            ps = self._create_ps(id, num_channels)

            # Create channel content
            self.add_channels(id, num_channels)
            dpg.configure_item(sender, label="Disconnect")

            # Add PS IDN to header label
            dpg.configure_item(f"ps{id}", label=f"Power Supply {id}: {ps.idn}")
        else:
            self._delete_supply(id)
            dpg.configure_item(sender, label="Connect")

    def _create_supply(self, id: int, host: str, num_channels: int) -> PowerSupply:
        """Creates a new PowerSupply object at the specified index"""
        if host == "demo":
            ps = DemoPowerSupply(host, id, num_channels)
        else:
            ps = PowerSupply(host, id, num_channels)
        self.supplies[id - 1] = ps
        return ps

    def _delete_supply(self, id: int) -> None:
        """Deletes a PowerSupply object from the specified index"""
        # Delete PowerSupply object
        if self.supplies[id - 1]:
            ps = self.supplies[id - 1]
            if ps:
                num_channels = len(ps.channels)
                # Delete channel content
                dpg.delete_item(f"ps{id}_channels")
                self.supplies.pop(id - 1)
                self.supplies.insert(id - 1, None)
                for ch in range(1, num_channels + 1):
                    dpg.delete_item(f"p{id}c{ch}_pwr_btn")

    def _set_btn_colors(self, base_tag: str, colors: tuple) -> None:
        """Changes the color of a button theme"""
        if dpg.does_item_exist(base_tag):
            dpg.set_value(base_tag, colors[0])
            dpg.set_value(base_tag + "_act", colors[2])
            dpg.set_value(base_tag + "_hov", colors[1])
        else:
            logger.debug(f"Button theme {base_tag} does not exist.")

    def _create_btn_theme(self, theme_tag: str, colors: tuple) -> None:
        """Defines a DPG button theme for the provided tag"""
        with dpg.theme(tag=theme_tag):
            with dpg.theme_component(dpg.mvButton):
                dpg.add_theme_color(
                    dpg.mvThemeCol_Button,
                    colors[0],
                    tag=theme_tag + "_color",
                )
                dpg.add_theme_color(
                    dpg.mvThemeCol_ButtonActive,
                    colors[2],
                    tag=theme_tag + "_color_act",
                )
                dpg.add_theme_color(
                    dpg.mvThemeCol_ButtonHovered,
                    colors[1],
                    tag=theme_tag + "_color_hov",
                )
                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5)
                dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 3, 3)


class Timer:
    def __init__(self, interval: float):
        self.total_time = dpg.get_total_time()
        self.last_total_time = dpg.get_total_time()
        self.interval: float = interval

    def update(self) -> bool:
        """Timer for GUI render loop"""
        self.total_time = dpg.get_total_time()
        delta_time = dpg.get_total_time() - self.last_total_time
        if delta_time > self.interval:
            self.last_total_time = self.total_time
            return True
        return False


class GuiTheme:
    def __init__(self):
        self.bg = (7, 12, 19)  # darkest color
        self.header = (24, 40, 63)  # lighter than bg
        self.check = (213, 140, 41)  # accent color
        self.tab = (213, 140, 41)  # accent color
        self.hover = (234, 150, 45)  # slightly lighter accent color
        self.scrollbar = (41, 67, 104)
        self.scrollbar_active = (22, 65, 134)

        self.red = ([153, 61, 61, 255], [178, 54, 54, 255], [204, 41, 41, 255])
        self.green = ([80, 153, 61, 255], [79, 179, 54, 255], [73, 204, 41, 255])
        self.orange = ([213, 140, 41, 255], [234, 150, 45, 255], [234, 150, 45, 200])

    def set_header_btn_theme(self, theme_tag: str, colors: tuple) -> None:
        """Sets the theme for the GUI header"""
        with dpg.theme(tag=theme_tag):
            with dpg.theme_component(dpg.mvButton):
                dpg.add_theme_color(
                    dpg.mvThemeCol_Button,
                    colors[0],
                    tag=theme_tag + "_color",
                )
                dpg.add_theme_color(
                    dpg.mvThemeCol_ButtonActive,
                    colors[2],
                    tag=theme_tag + "_color_act",
                )
                dpg.add_theme_color(
                    dpg.mvThemeCol_ButtonHovered,
                    colors[1],
                    tag=theme_tag + "_color_hov",
                )
                dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8)
                dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 6, 6)
