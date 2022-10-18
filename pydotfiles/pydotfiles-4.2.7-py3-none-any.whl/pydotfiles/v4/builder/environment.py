# General imports
from logging import getLogger

# Project imports
from pydotfiles.v4.common.alpha import Environment, OSName
from pydotfiles.v4.common.alpha.environment import Plugin

logger = getLogger(__name__)

##
# Developer environment manager installation
##


def template_dev_env_manager_installation(data: Environment, active_os: OSName) -> str:
    environment_managers = {
        'pyenv': get_pyenv_installation_template,
        'jenv': get_jenv_installation_template
    }
    return environment_managers.get(data.environment_manager.name, lambda: "")(active_os)


def get_pyenv_installation_template(active_os: OSName) -> str:
    pyenv_dispatcher = {
        OSName.linux: get_pyenv_linux_installation_template,
        OSName.macos: get_pyenv_macos_installation_template,
    }

    return pyenv_dispatcher.get(active_os)()


def get_pyenv_linux_installation_template() -> str:
    return r"""

    ##
    # Installs pyenv if it's not yet installed
    ##
    function linux_setup() {
        linux_install_pyenv_dependencies
        linux_install_pyenv
        linux_install_pyenv_environment
    }
    
    function linux_install_pyenv_dependencies() {
        # Grabbed from https://www.liquidweb.com/kb/how-to-install-pyenv-on-ubuntu-18-04/
        apt update -y
        apt install -y make build-essential libssl-dev zlib1g-dev \
        libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
        libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl \
        git
    }
    
    function linux_install_pyenv() {
        git clone https://github.com/pyenv/pyenv.git ~/.pyenv
    }
    
    function linux_install_pyenv_environment() {
        info "Pyenv Environment: Checking for correct pyenv environment variable setup"
        if [[ -z "${PYENV_ROOT}" ]]; then
            info "Pyenv Environment: Missing pyenv environment variables"
            {
                echo "# Pydotfiles: Automatically set pyenv settings"
                echo "export PYENV_ROOT=$HOME/.pyenv"
                echo "if which pyenv > /dev/null; then eval \"\$(pyenv init -)\"; fi"
                echo "if which pyenv-virtualenv-init > /dev/null; then eval \"\$(pyenv virtualenv-init -)\"; fi"
            } >> ~/.bash_profile

            # shellcheck disable=SC1090
            source "${HOME}/.bash_profile"
            success "Pyenv Environment: Successfully added in pyenv environment variables"
        else
            success "Pyenv Environment: Already have set pyenv environment variables"
        fi
    }
    linux_setup
    """


def get_pyenv_macos_installation_template() -> str:
    return r"""

    ##
    # Installs pyenv if it's not yet installed
    ##

    function mac_setup() {
        mac_install_xcode
        mac_install_homebrew
        mac_install_pyenv
        mac_install_pyenv_environment
    }

    function mac_install_xcode() {
        # Installs xcode command line tools and accepts the license
        if xcode-select -p &> /dev/null ; then
            success "Xcode: MacOS command-line tools are already installed"
        else
            info "Xcode: MacOS command-line tools were not installed, installing now"
            if install_xcode ; then
                success "Xcode: Successfully installed macOS command-line tools"
            else
                fail "Xcode: Failed to install macOS command-line tools"
            fi
        fi
    }

    function mac_install_homebrew() {
        info "Package Manager: Checking for the existance of Homebrew"
        if [[ $(command -v brew) == "" ]]; then
            info "Package Manager: Homebrew was not found, installing now"

            # shellcheck disable=SC2028,SC1117
            if echo "\r" | /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" ; then
                success "Package Manager: Successfully installed Homebrew"
            else
                fail "Package Manager: Failed to install Homebrew"
            fi
        else
            success "Package Manager: Homebrew is already installed"
        fi
    }

    function mac_install_pyenv() {
        info "Pyenv: Checking for pyenv installation"
        if [[ $(command -v pyenv | grep pyenv) == "" ]]; then
            info "Pyenv: Missing pyenv package, installing now"
            if brew install pyenv ; then
                success "Pyenv: Successfully installed pyenv"
            else
                fail "Pyenv: Failed to install pyenv"
            fi
        else
            success "Pyenv: Pyenv is already installed"
        fi
    }

    function mac_install_pyenv_environment() {
        info "Pyenv Environment: Checking for correct pyenv environment variable setup"
            if [[ -z "${PYENV_ROOT}" ]]; then
            info "Pyenv Environment: Missing pyenv environment variables"
            {
                echo "# Pydotfiles: Automatically set pyenv settings"
                echo "export PYENV_ROOT=$HOME/.pyenv"
                echo "if which pyenv > /dev/null; then eval \"\$(pyenv init -)\"; fi"
                echo "if which pyenv-virtualenv-init > /dev/null; then eval \"\$(pyenv virtualenv-init -)\"; fi"
            } >> ~/.bash_profile

            # shellcheck disable=SC1090
            source "${HOME}/.bash_profile"
            success "Pyenv Environment: Successfully added in pyenv environment variables"
        else
            success "Pyenv Environment: Already have set pyenv environment variables"
        fi
    }
    mac_setup

    """


def get_jenv_installation_template(active_os: OSName) -> str:
    jenv_installer_dispatcher = {
        OSName.linux: get_jenv_linux_installation_template,
        OSName.macos: get_jenv_macos_installation_template
    }
    return jenv_installer_dispatcher.get(active_os)()


def get_jenv_linux_installation_template() -> str:
    return r"""
    git clone https://github.com/jenv/jenv.git ~/.jenv
    """


def get_jenv_macos_installation_template() -> str:
    return r"""
    # brew install jenv
    """

##
# Developer environment manager plugin installation
##


def template_dev_env_manager_plugins_installation(data: Environment) -> str:
    environment_manager_plugins = {
        'pyenv-virtualenv': get_pyenv_virtualenv_installation_template,
    }

    plugins_template = ""
    for plugin in data.environment_manager.plugins:
        plugins_template += environment_manager_plugins.get(plugin.name, lambda: "")()
        plugins_template += environment_manager_plugin_setup(plugin)
    return plugins_template


def get_pyenv_virtualenv_installation_template() -> str:
    return r"""
    function pyenv_install_pyenv_virtualenv() {
        info "Pyenv-virtualenv: Checking for pyenv-virtualenv installation"
        if [[ $(brew list | grep "pyenv-virtualenv") == "" ]]; then
            info "Pyenv-virtualenv: Missing pyenv-virtualenv package, installing now"
            if brew install pyenv-virtualenv ; then
                success "Pyenv-virtualenv: Successfully installed pyenv-virtualenv"
            else
                fail "Pyenv-virtualenv: Failed to install pyenv-virtualenv"
            fi
        else
            success "Pyenv-virtualenv: Pyenv-virtualenv is already installed"
        fi
    }
    pyenv_install_pyenv_virtualenv
    """


def environment_manager_plugin_setup(data: Plugin) -> str:
    environment_manager_plugin_setup_methods = {
        'pyenv-virtualenv': get_pyenv_virtualenv_virtual_env_setup
    }
    return environment_manager_plugin_setup_methods.get(data.name, lambda x: "")(data)


def get_pyenv_virtualenv_virtual_env_setup(data: Plugin) -> str:
    versions_to_install = f"python_base_versions=({' '.join([virtual_env.version for virtual_env in data.virtual_environments])})\n"
    virtual_envs_to_install = f"python_virtual_env_aliases=({' '.join([virtual_env.name for virtual_env in data.virtual_environments])})\n"
    driver_function = r"""
    function pyenv_install_virtual_envs() {
        info "Pyenv Virtualenv: Checking that all pyenv virtual environments are installed"

        # We choose not to use an associative array in case bash versions used are below Bash 4,
        # which is when associative arrays were introduced
        for index in "${!python_base_versions[@]}"; do
            pyenv_install_single_virtualenv "${python_base_versions[$index]}" "${python_virtual_env_aliases[$index]}"
        done
        success "Pyenv Virtualenv: All pyenv global environments are installed"
    }

    function pyenv_install_single_virtualenv() {
        version=$1
        alias_name=$2

        if [[ $(pyenv versions | grep "${alias_name}") == "" ]]; then
            info "Pyenv Virtualenv: The virtual env '${alias_name}' was not found, installing now"
            if pyenv virtualenv "${version}" "${alias_name}" &> /dev/null ; then
                success "Pyenv Virtualenv: Successfully installed the virtual env '${alias_name}'"
            else
                fail "Pyenv Virtualenv: Failed to install the virtual env '${alias_name}'"
            fi
        else
            success "Pyenv Virtualenv: The virtual env '${alias_name}' is already installed"
        fi
    }
    pyenv_install_virtual_envs
    """
    return versions_to_install + virtual_envs_to_install + driver_function

##
# Developer environment manager version installation
##


def template_dev_env_manager_version_installation(data: Environment) -> str:
    environment_manager_version_installer = {
        'pyenv': get_pyenv_version_install_template
    }
    return environment_manager_version_installer.get(data.environment_manager.name, lambda x: "")(data)


def get_pyenv_version_install_template(data: Environment) -> str:
    versions_to_install = f"python_base_versions=({' '.join(data.versions)})\n"
    base_installation_driver = r"""
    function pyenv_install_base_environments() {
        info "Pyenv Base Environment: Checking that all pyenv base environments are installed"
        for version in "${python_base_versions[@]}"; do
            pyenv_install_single_base_environment "${version}"
        done
        success "Pyenv Base Environment: All pyenv base environments look good"
    }
    pyenv_install_base_environments
    """

    pyenv_installation_functions = r"""
    function pyenv_install_single_base_environment() {
        version=$1
        if [[ $(pyenv versions | grep "${version}") == "" ]]; then
            info "Pyenv: Python version ${version} is not installed yet, installing now"
    
            # Checks if pyenv has the correct version first
            info "Pyenv: Checking for python version ${version}"
            if [[ $(pyenv install --list | grep "${version}") == "" ]]; then
                fail "Pyenv: Python version ${version} was not found, please check it is valid and pyenv is up to date"
            else
                success "Pyenv: Python version ${version} was found"
            fi
    
            # Runs through normal install if possible, using CFlag if not
            info "Pyenv: Attempting normal install (might take a few minutes)"
            if pyenv install "${version}" &> /dev/null ; then
                success "Pyenv: Python version ${version} is now installed"
            else
                warn "Pyenv: Python version ${version} failed to install, attempting to run with CFlags"
                pyenv_install_base_environment_fallback "${version}"
            fi
        else
            success "Pyenv: Python version ${version} is already installed"
        fi
    }
    
    function pyenv_install_base_environment_fallback() {
        version=$1
    
        if CFLAGS="-I$(xcrun --show-sdk-path)/usr/include" pyenv install "${version}" &> /dev/null ; then
            success "Pyenv: Python version ${version} is now installed"
        else
            warn "Pyenv: CFlag setting when installing ${version} failed, attempting to install with CFlags and LDFlags"
            if CFLAGS="-I$(brew --prefix openssl)/include" LDFLAGS="-L$(brew --prefix openssl)/lib" pyenv install "${version}" &> /dev/null ; then
                success "Pyenv: Python version ${version} is now installed"
            else
                fail "Pyenv: Python version ${version} failed to install"
            fi
        fi
    }
    """

    return versions_to_install + pyenv_installation_functions + base_installation_driver
