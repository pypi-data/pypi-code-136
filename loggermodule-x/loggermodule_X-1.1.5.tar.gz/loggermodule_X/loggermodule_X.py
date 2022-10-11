import logging
from pathlib import Path
import sys
from datetime import datetime
from logging import handlers

LEVEL_LIST = ['NOTSET', 'INFO', 'DEBUG', 'ERROR', 'WARNING', 'CRITICAL']
MODE_LIST = ['split', 'midnight']

class logger_x:
    def __init__(self, file=None, mode=None, console=None, rfile=None, avoid=False):
        self.formatter = logging.Formatter('[%(asctime)s] [PID:%(process)d ThreadID:%(thread)d] [%(levelname)s] [%(name)s.%(funcName)s:%(lineno)d]  %(message)s')
        self.name = Path(file).stem if file else '__main__'
        self.file = Path(file).parent.absolute() if file else None
        self.mode = mode if mode and mode in MODE_LIST else 'midnight'
        self.s_console = console if console and console in LEVEL_LIST else 'NOTSET'
        self.r_file = rfile if rfile and rfile in LEVEL_LIST else 'NOTSET'
        self.log_path = self.file / "log"
        self.log_name = self.name + '.log'
        self.full_path = self.log_path / self.log_name
        self.avoid = avoid

    def namer(self, name):
        return name.replace(".log", "") + ".log"

    def configLogger(self):
        logging.getLogger().setLevel(level=self.s_console)
        logging.getLogger("filelock").setLevel(logging.ERROR) ## Avoid lockfile log
        if self.avoid == False:
            if self.mode == 'midnight':
                self.log_path.mkdir(parents=True, exist_ok=True)
                fileHandler = handlers.TimedRotatingFileHandler(self.full_path, when='midnight', backupCount=0, encoding='utf-8')
            elif self.mode == 'split':
                log_path = self.log_path / datetime.now().strftime("%Y%m%d")
                log_path.mkdir(parents=True, exist_ok=True)
                full_path = log_path / self.log_name
                fileHandler = handlers.RotatingFileHandler(full_path, maxBytes=800000000, backupCount=10, encoding='utf-8')
            # fileHandler.handlers.clear()
            # consoleHandler.handlers.clear()
            consoleHandler = logging.StreamHandler(sys.stdout)
            consoleHandler.setLevel(level=self.s_console)
            consoleHandler.setFormatter(self.formatter)
            logging.getLogger().addHandler(consoleHandler)
            fileHandler.namer = self.namer
            fileHandler.setLevel(level=self.r_file)
            fileHandler.setFormatter(self.formatter)
            logging.getLogger().addHandler(fileHandler)
            log = logging.getLogger("app." + self.name)
        else:
            log = logging.getLogger("app." + self.name)
        return log

if __name__ == '__main__':
    log = logger_x(__file__).configLogger()
    log.info('THIS is info msg !!')
    log.debug('THIS is debug msg !!')
    log.error('THIS is error msg !!')
    log.warning('THIS is warning msg !!')
    log.critical('THIS is critical msg !!')
