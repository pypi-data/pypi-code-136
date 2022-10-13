import logging
import os
from logging import config
import yaml


class CC_LOG:
    def __init__(self, configPath='log.yaml'):
        self.path = os.path.join(os.path.dirname(__file__), configPath)
        self.create_logdirs()
        self.use_yaml_config()
        self.CC_Log = logging.getLogger("CC_Log")

    def debug(self, string):
        self.CC_Log.debug(string)

    def info(self, string):
        self.CC_Log.info(string)

    def warning(self, string):
        self.CC_Log.warning(string)

    def error(self, string):
        self.CC_Log.error(string)

    def critical(self, string):
        self.CC_Log.critical(string)

    def create_logdirs(self):
        # mkpath = os.path.join(os.path.dirname(__file__), 'CC_Log')
        mkpath = os.path.join('CC_Log')
        if not os.path.exists(mkpath):
            os.mkdir(mkpath)
        print('CC_LOG自己的简易日志配置 Dir Created!')
        for i in ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']:
            if not os.path.exists(os.path.join(mkpath, f'{i}.log')):
                f = open(os.path.join(mkpath, f'{i}.log'), 'a')
                f.close()
        print('CC_LOG自己的简易日志配置 Files Created!')

    def use_yaml_config(self):
        print(self.path)
        if os.path.exists(self.path):
            with open(self.path, 'r', encoding='utf-8') as f:
                config = yaml.load(stream=f, Loader=yaml.FullLoader)
                # import pdb
                # pdb.set_trace()
                config['handlers']['debug_file_handler']['filename'] = str(os.path.join('CC_Log', 'DEBUG.log'))
                config['handlers']['info_file_handler']['filename'] = str(os.path.join('CC_Log', 'INFO.log'))
                config['handlers']['warning_file_handler']['filename'] = str(os.path.join('CC_Log', 'WARNING.log'))
                config['handlers']['error_file_handler']['filename'] = str(os.path.join('CC_Log', 'ERROR.log'))
                config['handlers']['critical_file_handler']['filename'] = str(os.path.join('CC_Log', 'CRITICAL.log'))

            logging.config.dictConfig(config)
        else:
            print("缺少日志配置文件")


if '__main__' == __name__:
    log = CC_LOG()
    log.debug('debug')
    log.info('info ')
    log.warning('warning')
    log.error('error')
    log.critical('critical')
