"""CPU usage measuring daemon"""

import configparser
import datetime
import logging
import os
import sys
import time

import daemon
import lockfile
import psutil
import requests
from requests.exceptions import (
    ReadTimeout,
    ConnectTimeout,
    ConnectionError,
    HTTPError
)

PID_FILENAME = "/tmp/cpu_usage.pid"
INTERVAL = 5


class CPUUsageClient:
    """Client for get CPU usage and save it to database using API"""

    CFG_FILENAME = "config.ini"

    def __init__(self):
        """Init client"""
        config = configparser.ConfigParser()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = base_dir + "/log"
        if not os.path.exists(log_dir):
            os.mkdir(log_dir)
        log_filename = (
            log_dir + "/" + str(datetime.date.today()).replace("-", "") + ".log"
        )
        cfg_filename = base_dir + "/" + self.CFG_FILENAME

        # logger init
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter("[%(asctime)s]: %(levelname)s: %(message)s")
        fh = logging.FileHandler(log_filename)  # pylint: disable=invalid-name
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        sh = logging.StreamHandler(stream=sys.stdout)  # pylint: disable=invalid-name
        sh.setFormatter(formatter)
        self.logger.addHandler(sh)

        # Read config file
        self.logger.info("Config file loading...")
        if os.path.isfile(cfg_filename):
            config.read(cfg_filename)
            try:
                self.api_url = config["main"]["api_url"]
            except KeyError:
                self.logger.error("Parameter '%s' not found in config file!", "api_url")
                self.api_url = None
            config.clear()
        else:
            self.logger.error("Config file '%s' not found!", self.CFG_FILENAME)

    @staticmethod
    def get_cpu_usage() -> float:
        """Get current cpu usage"""
        return psutil.cpu_percent()

    def save_cpu_usage(self) -> None:
        """Save cpu usage to database using API"""
        cpu_usage = CPUUsageClient.get_cpu_usage()
        try:
            response = requests.post(
                url=self.api_url,
                data={"cpu_usage": cpu_usage},
                timeout=(3, 3),
            )
            if response.status_code == 201:
                self.logger.info("CPU usage value '%s' was saved", cpu_usage)
            else:
                self.logger.error(
                    "API request error: response status code '%s', response text: '%s'",
                    response.status_code,
                    response.text,
                )
        except (ReadTimeout, ConnectTimeout, ConnectionError, HTTPError) as e:  # pylint: disable=invalid-name
            self.logger.exception(e)

    def start(self, interval: int) -> None:
        """Execute measuring of CPU usage"""
        self.logger.info("Interval: %s", interval)
        while True:
            self.save_cpu_usage()
            time.sleep(interval)


if __name__ == "__main__":
    with daemon.DaemonContext(
        pidfile=lockfile.FileLock(PID_FILENAME)
    ):
        client = CPUUsageClient()
        if client.api_url is not None:
            client.start(interval=INTERVAL)
