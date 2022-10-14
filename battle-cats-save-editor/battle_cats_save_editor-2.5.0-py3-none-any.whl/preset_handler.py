"""Handler for the presets"""
import json
import os
from typing import Any, Optional

from . import helper, user_input_handler


def load_presets() -> dict[str, dict[str, Any]]:
    """
    Load the presets

    Returns:
        dict[str, dict[str, Any]]: The presets
    """
    preset_path = get_presets_path()
    helper.create_dirs(preset_path)
    presets: dict[str, dict[str, Any]] = {}
    for preset in helper.get_files_in_dir(preset_path):
        if preset.endswith(".json"):
            preset_name = os.path.basename(preset.replace(".json", ""))
            presets[preset_name] = helper.load_json(preset)
    return presets


def get_preset_names() -> list[str]:
    """
    Get the names of the presets

    Returns:
        list[str]: The names of the presets
    """
    presets = load_presets()
    return list(presets.keys())


def get_preset(preset_name: str) -> dict[str, Any]:
    """
    Get a preset

    Args:
        preset_name (str): The name of the preset

    Returns:
        dict[str, Any]: The preset
    """
    presets = load_presets()
    return presets[preset_name]


def get_preset_path(preset_name: str) -> str:
    """
    Get the path to a preset

    Args:
        preset_name (str): The name of the preset

    Returns:
        str: The path to the preset
    """
    return os.path.join(get_presets_path(), preset_name + ".json")


def delete_preset(preset_name: str) -> None:
    """
    Delete a preset

    Args:
        preset_name (str): The name of the preset
    """
    preset_path = get_preset_path(preset_name)
    os.remove(preset_path)


def select_preset() -> Optional[str]:
    """
    Select a preset

    Returns:
        str: The name of the preset
    """
    preset_names = get_preset_names()
    if not preset_names:
        helper.colored_text("No presets found", helper.RED)
        return None
    index = user_input_handler.select_single(preset_names, "load", "Select a preset:")
    return preset_names[index - 1]


def load_preset(preset_name: str) -> dict[str, Any]:
    """
    Load a preset

    Args:
        preset_name (str): The name of the preset

    Returns:
        dict[str, Any]: The preset
    """
    presets_data = load_presets()
    return presets_data[preset_name]


def load_preset_into_save_stats(
    preset_name: str, save_stats: dict[str, Any]
) -> dict[str, Any]:
    """
    Load a preset into the save stats

    Args:
        preset_name (str): The name of the preset
        save_stats (dict[str, Any]): The save stats

    Returns:
        dict[str, Any]: The save stats
    """
    preset = load_preset(preset_name)
    for key, value in preset.items():
        save_stats[key] = value

    return save_stats


def load_preset_handler(save_stats: dict[str, Any]) -> dict[str, Any]:
    """
    Load a preset into the save stats

    Args:
        save_stats (dict[str, Any]): The save stats

    Returns:
        dict[str, Any]: The save stats
    """
    preset_name = select_preset()
    if preset_name is None:
        return save_stats
    save_stats = load_preset_into_save_stats(preset_name, save_stats)
    return save_stats


def delete_preset_handler():
    """
    Delete a preset
    """
    preset_name = select_preset()
    if preset_name is None:
        return
    delete_preset(preset_name)
    return


def display_presets() -> None:
    """
    Display the presets
    """
    presets = load_presets()
    print("Loaded presets:")
    for preset_name, preset in presets.items():
        helper.colored_text(f"Preset: &{preset_name}&")
        for key, value in preset.items():
            if (
                not isinstance(value, int)
                and not isinstance(value, float)
                and not isinstance(value, str)
            ):
                helper.colored_text(f"  {key}", helper.DARK_YELLOW)
                continue
            helper.colored_text(f"  {key}: {value}", helper.CYAN)


def create_preset(save_stats: dict[str, Any]) -> dict[str, Any]:
    """
    Create a preset

    Args:
        save_stats (dict[str, Any]): The save stats

    Returns:
        dict[str, Any]: The save stats
    """
    preset_name = input("Enter the name of the preset:")
    preset_data: dict[str, Any] = {}
    while True:
        key = input(
            "Enter the key in the save data to add to the preset (Enter exit to finish):"
        )
        if key == "exit":
            break
        keys = search_keys(save_stats, key)
        if not keys:
            helper.colored_text("No keys found", helper.RED)
            continue
        selected_keys = user_input_handler.select_not_inc(keys, "add")
        for key_index in selected_keys:
            key = keys[key_index]
            preset_data[key] = save_stats[key]
    save_preset(preset_name, preset_data)
    return save_stats


def search_keys(save_stats: dict[str, Any], value: str) -> list[str]:
    """
    Search for keys in the save stats

    Args:
        save_stats (dict[str, Any]): The save stats
        value (str): The value to search for

    Returns:
        list[str]: The keys
    """
    keys: list[str] = []
    for key in save_stats.keys():
        if key.lower() == value.lower().replace(" ", "_"):
            keys.append(key)
    return keys


def preset_manager(save_stats: dict[str, Any]) -> dict[str, Any]:
    """
    Manage the presets

    Args:
        save_stats (dict[str, Any]): The save stats

    Returns:
        dict[str, Any]: The save stats
    """
    display_presets()
    while True:
        options = [
            "Create a preset",
            "Load a preset",
            "Delete a preset",
            "Back",
        ]
        index = (
            user_input_handler.select_single(options, "preset", "Select an option:") - 1
        )
        if index == 0:
            save_stats = create_preset(save_stats)
        elif index == 1:
            save_stats = load_preset_handler(save_stats)
        elif index == 2:
            delete_preset_handler()
        elif index == 3:
            break

    return save_stats


def save_preset(preset_name: str, preset: dict[str, Any]) -> None:
    """
    Save a preset

    Args:
        preset_name (str): The name of the preset
        preset (dict[str, Any]): The preset
    """
    json_data = json.dumps(preset, indent=4)
    preset_path = get_preset_path(preset_name)
    helper.write_file_string(preset_path, json_data)


def get_presets_path() -> str:
    """
    Get the path to the presets

    Returns:
        str: The path to the presets
    """

    return helper.get_file("presets")
