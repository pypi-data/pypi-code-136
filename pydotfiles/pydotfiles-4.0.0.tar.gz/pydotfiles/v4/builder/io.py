# General imports
from pathlib import Path
from os import access as os_access
from os import X_OK as IS_EXECUTABLE
from hashlib import sha256 as hashlib_sha256
from logging import getLogger

# Project imports
from pydotfiles.v4.builder.environment import template_dev_env_manager_installation, \
    template_dev_env_manager_plugins_installation, template_dev_env_manager_version_installation
from pydotfiles.v4.common.alpha import Environment, OSName

logger = getLogger(__name__)

##
# Templating functions for helper functions
##


def template_starter_helper_functions() -> str:
    return r"""
    function info () {
        printf "\r  [ \033[00;34m..\033[0m ] %s\n" "$1"
    }

    function user () {
        printf "\r  [ \033[0;33m??\033[0m ] %s " "$1"
    }

    function success () {
        printf "\r\033[2K  [ \033[00;32mOK\033[0m ] %s\n" "$1"
    }

    function warn () {
        printf "\r\033[2K  [\033[0;31mWARN\033[0m] %s\n" "$1"
    }

    function fail () {
        printf "\r\033[2K  [\033[0;31mFAIL\033[0m] %s\n" "$1"
        echo ''
        exit 1
    }
    """

##
# Templating function for dev environment
##


def template_dev_environment_setup(data: Environment, active_os: OSName) -> str:
    dev_environment_installation = ""

    dev_environment_installation += template_dev_env_manager_installation(data, active_os)
    dev_environment_installation += template_dev_env_manager_version_installation(data)
    dev_environment_installation += template_dev_env_manager_plugins_installation(data)

    return dev_environment_installation

##
# Templating functions for actions
##


def template_copy_file(origin: Path, destination: Path) -> str:
    """
    Returns the equivalent bash command in order to copy a file.
    NOTE: origin is a _relative_ path from the root of the dotfiles directory
    NOTE: destination is an _absolute_ path
    NOTE: We removed sudo ability here, but can re-add it in if necessary
    """

    return f"""
    if [[ -f {destination} ]]; then
        info "Copy: File already exists in {destination}"
    else
        if mkdir -p {destination.parent} && cp {origin} {destination} ; then
            success "Copy: Successfully copied file {origin} to {destination}"
        else
            fail "Copy: Failed to copy file {origin} to {destination}"
        fi
    fi
    """


def template_symlink_file(origin: Path, destination: Path, use_sudo: bool) -> str:
    """
    Returns the equivalent bash command in order to symlink a file
    NOTE: origin is a _relative_ path from the root of the dotfiles directory
    NOTE: destination is an _absolute_ path
    """

    return f"""
    if [[ -L {destination} ]]; then
        info "Symlink: File already exists in {destination}"
    else
        if {'sudo ' if use_sudo else ''}mkdir -p {destination.parent} && {'sudo ' if use_sudo else ''}ln -s {origin} {destination} ; then    
            success "Symlink: Successfully symlinked {origin} to {destination}"
        else
            fail "Symlink: Failed to symlink {origin} to {destination}"
        fi
    fi
    """


def template_run_script(script: Path, use_sudo: bool) -> str:
    """
    Returns the equivalent bash command in order to copy a file
    """
    return f"""
    if {'sudo ' if use_sudo else ''}{script}; then
        success "Script file: {script} executed successfully"
    else
        fail "Script file: {script} failed to executed"
    fi
    """


##
# Utility functions
##


def is_moved(origin: Path, destination: Path) -> bool:
    # Enables fast-failing based on existence
    if not destination.is_file():
        return False

    if origin.is_file():
        return False

    return True


def is_broken_link(file: Path) -> bool:
    return file.is_symlink() and not file.exists()


def is_linked(origin: Path, destination: Path) -> bool:
    return destination.is_symlink() and destination.resolve() == origin.resolve()


def is_copied(origin: Path, destination: Path) -> bool:
    # If the file already exists then no need to do anything
    if destination.is_file():
        return True

    # Enables fast-failing based on type
    if destination.is_symlink():
        return False

    # Enables fast-failing based on file size

    origin_file_size = origin.stat().st_size
    destination_file_size = destination.stat().st_size

    if origin_file_size != destination_file_size:
        return False

    # Enables fast-failing based on metadata
    origin_last_modified_time = origin.stat().st_mtime
    destination_last_modified_time = destination.stat().st_mtime

    if origin_last_modified_time != destination_last_modified_time:
        return False

    # Loads in the files and checks that their hashes are the same
    origin_file_hash = hash_file(origin)
    destination_file_hash = hash_file(destination)
    return origin_file_hash == destination_file_hash


def is_executable(file: Path) -> bool:
    return os_access(file, IS_EXECUTABLE)


def hash_file(file_path: Path, block_size=65536) -> str:
    """
    Hashes a given file and returns the digest in hexadecimal
    """
    hasher = hashlib_sha256()
    with file_path.open('rb') as raw_file:
        buf = raw_file.read(block_size)
        while len(buf) > 0:
            hasher.update(buf)
            buf = raw_file.read(block_size)

    return hasher.hexdigest()
