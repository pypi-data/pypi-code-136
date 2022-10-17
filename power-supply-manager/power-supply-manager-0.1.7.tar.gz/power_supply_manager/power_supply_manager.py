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
import dearpygui.dearpygui as dpg
from datetime import datetime

from power_supply_manager.state import *

state = GuiState()


def app():
    dpg.create_context()
    dpg.create_viewport(
        title="DevBuildZero Power Supply Manager", width=1500, height=800
    )
    dpg.setup_dearpygui()
    dpg.show_viewport()
    _show_gui()
    dpg.set_primary_window("_primary_wnd", True)
    timer = Timer(0.1)
    while dpg.is_dearpygui_running():
        trigger_update = timer.update()
        if trigger_update:
            _update_app_content()
        dpg.render_dearpygui_frame()
    dpg.destroy_context()


def _show_gui():
    with dpg.window(
        on_close=state.on_gui_close,
        pos=(0, 0),
        tag="_primary_wnd",
    ):
        with dpg.theme() as global_theme:
            with dpg.theme_component(dpg.mvAll):
                dpg.add_theme_color(dpg.mvThemeCol_WindowBg, state.theme.bg)
                dpg.add_theme_color(dpg.mvThemeCol_ChildBg, state.theme.bg)
                dpg.add_theme_color(dpg.mvThemeCol_PopupBg, state.theme.bg)
                dpg.add_theme_color(dpg.mvThemeCol_TitleBgCollapsed, state.theme.bg)
                dpg.add_theme_color(dpg.mvThemeCol_Button, state.theme.header)
                dpg.add_theme_color(dpg.mvThemeCol_FrameBg, state.theme.header)
                dpg.add_theme_color(dpg.mvThemeCol_MenuBarBg, state.theme.header)
                dpg.add_theme_color(dpg.mvThemeCol_ScrollbarBg, state.theme.header)
                dpg.add_theme_color(dpg.mvThemeCol_Header, state.theme.header)
                dpg.add_theme_color(
                    dpg.mvThemeCol_ResizeGripHovered, state.theme.header
                )
                dpg.add_theme_color(dpg.mvThemeCol_ResizeGripActive, state.theme.header)
                dpg.add_theme_color(dpg.mvThemeCol_Tab, state.theme.header)
                dpg.add_theme_color(dpg.mvThemeCol_TabUnfocused, state.theme.header)
                dpg.add_theme_color(dpg.mvThemeCol_CheckMark, state.theme.check)
                dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, state.theme.check)
                dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive, state.theme.check)
                dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, state.theme.check)
                dpg.add_theme_color(dpg.mvThemeCol_HeaderActive, state.theme.check)
                dpg.add_theme_color(dpg.mvThemeCol_TabActive, state.theme.check)
                dpg.add_theme_color(
                    dpg.mvThemeCol_TabUnfocusedActive, state.theme.check
                )
                dpg.add_theme_color(dpg.mvThemeCol_PlotLines, state.theme.check)
                dpg.add_theme_color(dpg.mvThemeCol_PlotHistogram, state.theme.check)
                dpg.add_theme_color(dpg.mvThemeCol_TextSelectedBg, state.theme.check)
                dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, state.theme.hover)
                dpg.add_theme_color(dpg.mvThemeCol_SliderGrab, state.theme.hover)
                dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, state.theme.hover)
                dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, state.theme.hover)
                dpg.add_theme_color(dpg.mvThemeCol_TabHovered, state.theme.hover)
                dpg.add_theme_color(dpg.mvThemeCol_PlotLinesHovered, state.theme.hover)
                dpg.add_theme_color(
                    dpg.mvThemeCol_PlotHistogramHovered, state.theme.hover
                )
                dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrab, state.theme.scrollbar)
                dpg.add_theme_color(
                    dpg.mvThemeCol_ScrollbarGrabHovered, state.theme.scrollbar_active
                )
                dpg.add_theme_color(
                    dpg.mvThemeCol_ScrollbarGrabActive, state.theme.scrollbar_active
                )
        dpg.bind_theme(global_theme)

        with dpg.menu_bar():
            with dpg.menu(label="File"):
                dpg.add_menu_item(
                    label="Load Config", callback=lambda: dpg.show_item("file_dialog")
                )
                dpg.add_menu_item(
                    label="Save Config",
                    callback=lambda: dpg.show_item("save_dialog"),
                )
            with dpg.menu(label="Settings"):
                dpg.add_menu_item(
                    label="Toggle Fullscreen",
                    callback=lambda: dpg.toggle_viewport_fullscreen(),
                )
            with dpg.menu(label="Help"):
                dpg.add_menu_item(
                    label="About",
                    callback=lambda: dpg.configure_item("about_tag", show=True),
                )
                dpg.add_menu_item(
                    label="Show Metrics",
                    callback=lambda: dpg.show_tool(dpg.mvTool_Metrics),
                )

        with dpg.file_dialog(
            directory_selector=False,
            show=False,
            callback=state.config_selection,
            tag="file_dialog",
            width=600,
            height=600,
        ):
            dpg.add_file_extension(".json")

        with dpg.file_dialog(
            directory_selector=True,
            show=False,
            callback=state.dump_config,
            tag="save_dialog",
            width=800,
            height=600,
        ):
            with dpg.group():
                dpg.add_text("Choose filename to save config:")
                dpg.add_input_text(
                    default_value="my_config",
                    width=150,
                    callback=state.store_config_filename,
                )

        with dpg.window(
            label="About Power Supply Manager",
            modal=True,
            show=False,
            tag="about_tag",
            no_title_bar=True,
            pos=(200, 200),
        ):
            dpg.add_text(
                "This application was developed by DevBuildZero (devbuildzero.com) and is provided\nfor free under the MIT open source license:"
            )
            dpg.add_separator()
            dpg.add_text(
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
            )
            dpg.add_separator()
            with dpg.group(horizontal=True):
                dpg.add_button(
                    label="Close",
                    width=75,
                    callback=lambda: dpg.configure_item("about_tag", show=False),
                )

        with dpg.collapsing_header(label="Controls", default_open=True):
            btn_on_theme = "btn_on_theme"
            state.theme.set_header_btn_theme(btn_on_theme, state.theme.green)
            btn_off_theme = "btn_off_theme"
            state.theme.set_header_btn_theme(btn_off_theme, state.theme.red)
            btn_new_theme = "btn_new_theme"
            state.theme.set_header_btn_theme(btn_new_theme, state.theme.orange)
            with dpg.group(horizontal=True):
                with dpg.child_window(width=140, height=42):
                    with dpg.group(horizontal=True):
                        dpg.add_text("Supplies:")
                        state.help("Add a new power supply.")
                        dpg.add_button(label=" New ", callback=state.add_ps_header)
                        dpg.bind_item_theme(dpg.last_item(), btn_new_theme)
                with dpg.child_window(width=180, height=42):
                    with dpg.group(horizontal=True):
                        dpg.add_text("Logging:")
                        state.help(
                            "Start/stop logging supply measurements to a CSV file."
                        )
                        dpg.add_button(
                            label="Start",
                            callback=state.start_logging,
                        )
                        dpg.bind_item_theme(dpg.last_item(), btn_on_theme)

                        dpg.add_button(
                            label="Stop",
                            callback=state.stop_logging,
                        )
                        dpg.bind_item_theme(dpg.last_item(), btn_off_theme)
                with dpg.child_window(width=155, height=42):
                    with dpg.group(horizontal=True):
                        dpg.add_text("All:")
                        state.help("Power on/off all supply channels.")

                        dpg.add_button(
                            label=" On ",
                            callback=state.all_on,
                        )
                        dpg.bind_item_theme(dpg.last_item(), btn_on_theme)

                        dpg.add_button(
                            label=" Off ",
                            callback=state.all_off,
                        )
                        dpg.bind_item_theme(dpg.last_item(), btn_off_theme)

                with dpg.child_window(width=165, height=42):
                    with dpg.group(horizontal=True):
                        dpg.add_text("Group:")
                        state.help(
                            "Power on/off all channels that have the Group checkbox selected."
                        )
                        dpg.add_button(
                            label=" On ",
                            callback=state.group_on,
                        )
                        dpg.bind_item_theme(dpg.last_item(), btn_on_theme)
                        dpg.add_button(
                            label=" Off ",
                            callback=state.group_off,
                        )
                        dpg.bind_item_theme(dpg.last_item(), btn_off_theme)

                with dpg.child_window(width=185, height=42):
                    with dpg.group(horizontal=True):
                        dpg.add_text("Sequence:")
                        state.help(
                            "Execute power supply sequence. If a sequence value is set, each channel will turn on/off after <value> seconds. Use this to control the order in which channels are powered."
                        )
                        dpg.add_button(
                            label=" On ",
                            callback=state.sequence_on,
                        )
                        dpg.bind_item_theme(dpg.last_item(), btn_on_theme)
                        dpg.add_button(
                            label=" Off ",
                            callback=state.sequence_off,
                        )
                        dpg.bind_item_theme(dpg.last_item(), btn_off_theme)


def _update_app_content():
    # Build row of data for data logging
    datestamp = str(datetime.now().isoformat()).replace(":", "-")
    data_row = [datestamp]
    for i in range(len(state.supplies)):
        # Only update supplies elements that are not None
        ps = state.supplies[i]
        if ps and ps.channels and ps.init_done:
            for ch in ps.channels:
                # This will error out if we delete a supply during an update
                try:
                    # Set power button appearance based on current power state
                    state.set_power_btn(f"p{ps.num}c{ch.num}_pwr", ch.output_on)

                    # Check for channel values that have changed and update GUI
                    dpg.set_value(f"p{ps.num}c{ch.num}_name", ch.name)
                    dpg.set_value(f"p{ps.num}c{ch.num}_voltage_set", ch.voltage_set)
                    dpg.set_value(
                        f"p{ps.num}c{ch.num}_voltage_meas",
                        f"{format_value(ch.voltage_meas)}V",
                    )
                    dpg.set_value(
                        f"p{ps.num}c{ch.num}_ovp_state", "On" if ch.ovp_on else "Off"
                    )
                    dpg.set_value(f"p{ps.num}c{ch.num}_ovp_set", ch.ovp_set)
                    dpg.set_value(f"p{ps.num}c{ch.num}_current_set", ch.current_set)
                    dpg.set_value(
                        f"p{ps.num}c{ch.num}_current_meas",
                        f"{format_value(ch.current_meas)}A",
                    )
                    dpg.set_value(
                        f"p{ps.num}c{ch.num}_ocp_state", "On" if ch.ocp_on else "Off"
                    )
                    dpg.set_value(f"p{ps.num}c{ch.num}_ocp_set", ch.ocp_set)
                    if ch.seq_on >= 0:
                        dpg.set_value(f"p{ps.num}c{ch.num}_seq_on", ch.seq_on)
                    if ch.seq_off >= 0:
                        dpg.set_value(f"p{ps.num}c{ch.num}_seq_off", ch.seq_off)
                    dpg.set_value(
                        f"p{ps.num}c{ch.num}_v",
                        [np.arange(0, BUF_SIZE), ch.voltage_buffer],
                    )
                    dpg.set_value(
                        f"p{ps.num}c{ch.num}_i",
                        [np.arange(0, BUF_SIZE), ch.current_buffer],
                    )
                    dpg.set_axis_limits(
                        f"p{ps.num}c{ch.num}_y_v",
                        np.min(ch.voltage_buffer) - 0.5,
                        np.max(ch.voltage_buffer) + 0.5,
                    )
                    dpg.set_axis_limits(
                        f"p{ps.num}c{ch.num}_y_i",
                        np.min(ch.current_buffer) - 0.2,
                        np.max(ch.current_buffer) + 0.2,
                    )
                    if ch.name:
                        plot_title = f"Channel {ch.num}: {ch.name}"
                    else:
                        plot_title = f"Channel {ch.num}"
                    dpg.set_value(f"p{ps.num}c{ch.num}_title", plot_title)
                    dpg.configure_item(
                        f"p{ps.num}c{ch.num}_v",
                        label=f"v = {format_value(ch.voltage_meas)}V",
                    )
                    dpg.configure_item(
                        f"p{ps.num}c{ch.num}_i",
                        label=f"i = {format_value(ch.current_meas)}A",
                    )
                    data_row.append(ch.voltage_meas)
                    data_row.append(ch.current_meas)
                except:
                    logger.debug(f"DPG items for PS {ps.num} do not exist.")
    # Log data, if log is open
    if state.csv and len(data_row) > 1:
        state.csv.writerow(data_row)


def format_value(value) -> str:
    """Returns a string of the provided value in a user-friendly format
    (e.g. 350 mV instead of 0.350 V)"""
    if value < 0:
        return f"0.00 m"
    if value < 1:
        return f"{value * 1000:.2f} m"
    return f"{value:.2f} "


if __name__ == "__main__":
    app()
