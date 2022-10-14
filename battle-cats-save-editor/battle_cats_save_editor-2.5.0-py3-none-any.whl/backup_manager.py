"""Manage backups"""
import os
import time
from typing import Any
from . import helper, config_manager, serialise_save, patcher


def get_backup_folder() -> str:
    """
    Get the path to the backup folder

    Returns:
        str: The path to the backup folder
    """
    path = os.path.join(config_manager.get_app_data_folder(), "backups")
    helper.create_dirs(path)
    return path


def get_time_formatted() -> str:
    """
    Get the current time formatted

    Returns:
        str: The current time formatted
    """
    return time.strftime("%Y-%m-%d_%H-%M-%S")


def get_all_backups() -> list[str]:
    """
    Get all backups

    Returns:
        list[str]: The backups
    """
    return sort_backups(helper.get_files_in_dir(get_backup_folder()))


def get_backup_name(save_stats: dict[str, Any]) -> str:
    """
    Get the name of the backup

    Returns:
        str: The name of the backup
    """
    return f"{save_stats['inquiry_code']}_{save_stats['version']}_{save_stats['game_version']}: {get_time_formatted()}"


def get_backup_path(backup_name: str) -> str:
    """
    Get the path to a backup

    Args:
        backup_name (str): The name of the backup

    Returns:
        str: The path to the backup
    """
    return os.path.join(get_backup_folder(), backup_name)


def create_backup(save_stats: dict[str, Any]) -> str:
    """
    Create a backup

    Args:
        save_stats (dict[str, Any]): The save stats

    Returns:
        str: The path to the backup
    """
    backup_name = get_backup_name(save_stats)
    backup_path = get_backup_path(backup_name)
    save_data = serialise_save.start_serialize(save_stats)
    save_data = patcher.patch_save_data(save_data, save_stats["version"])
    helper.write_file_bytes(backup_path, save_data)
    return backup_path

def check_backups() -> None:
    """
    Check the backups
    """
    backups = get_all_backups()
    if len(backups) > 10:
        remove_oldest_backup()

def get_latest_backup_path() -> str:
    """
    Get the latest backup

    Returns:
        str: The path to the latest backup
    """
    backups = get_all_backups()
    if backups:
        return backups[-1]
    return ""

def get_latest_backup() -> bytes:
    """
    Get the latest backup

    Returns:
        bytes: The latest backup
    """
    backup_path = get_latest_backup_path()
    if backup_path:
        return helper.read_file_bytes(backup_path)
    return b""

def remove_oldest_backup() -> None:
    """
    Remove the oldest backup
    """
    backups = get_all_backups()
    if backups:
        os.remove(backups[0])


def sort_backups(backups: list[str]) -> list[str]:
    """
    Sort the backups

    Args:
        backups (list[str]): The backups

    Returns:
        list[str]: The sorted backups
    """
    backups_times: list[str] = []
    for backup in backups:
        save_time = backup.split(": ")[1]
        backups_times.append(save_time)
    backups_times.sort()
    sorted_backups: list[str] = []
    for backup_time in backups_times:
        for backup in backups:
            if backup_time in backup:
                sorted_backups.append(backup)
    return sorted_backups
