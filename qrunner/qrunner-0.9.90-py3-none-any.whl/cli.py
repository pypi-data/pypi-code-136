import argparse
from qrunner import __version__, __description__, logger
from qrunner.scaffold import create_scaffold
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from qrunner.utils.webdriver_manager_extend import ChromeDriverManager


def main():
    """ API test: parse command line options and run commands.
    """
    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument("-v", "--version", dest="version", action='store_true', help="show version")
    parser.add_argument("-p", "--project", dest="project", help="create demo project")
    parser.add_argument("-i", "--install", dest="install", help="Install the browser driver.")

    args = parser.parse_args()
    version = args.version
    project = args.project
    install = args.install

    if version:
        print(__version__)
        return 0
    if project:
        create_scaffold(project)
        return 0
    if install:
        install_driver(install)
        return 0


def install_driver(browser: str) -> None:
    """
    Download and install the browser driver
    :param browser: The Driver to download. Pass as `chrome/firefox/ie/edge`. Default Chrome.
    :return:
    """

    if browser == "chrome":
        driver_path = ChromeDriverManager().install()
        logger.info(f"Chrome Driver[==>] {driver_path}")
    elif browser == "firefox":
        driver_path = GeckoDriverManager().install()
        logger.info(f"Firefox Driver[==>] {driver_path}")
    elif browser == "ie":
        driver_path = IEDriverManager().install()
        logger.info(f"IE Driver[==>] {driver_path}")
    elif browser == "edge":
        driver_path = EdgeChromiumDriverManager().install()
        logger.info(f"Edge Driver[==>] {driver_path}")
    else:
        raise NameError(f"Not found '{browser}' browser driver.")

