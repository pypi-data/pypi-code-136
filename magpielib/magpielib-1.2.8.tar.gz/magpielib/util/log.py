import logging
import logging.config
import os

log_base_name = None
#  log 相关配置如下：
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            'format': '%(asctime)s [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s',
            'datefmt': '%m/%d/%Y %I:%M:%S %p'
        },
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s',
            'datefmt': '%m/%d/%Y %I:%M:%S %p'
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },
        # "file": {
        #     "class": "logging.handlers.RotatingFileHandler",
        #     "level": "INFO",  #
        #     "formatter": "simple",
        #     "filename": None,
        #     'mode': 'w+',
        #     "maxBytes": 1024*1024*5,  # 5 MB
        #     "backupCount": 20,
        #     "encoding": "utf8"
        # }
    },
    "loggers": {
        "console": {
            "level": "DEBUG",  # 这个地方不控制，交给具体的handler控制级别
            "handlers": ["console"],
            "propagate": "no"
        }
    }
}


def init_logger(log_name, is_debug=False, log_path=None):
    """ 获取logger
    :param log_name: 根据不同的service 获取不同的logger，在启动的时候初始化
    :param is_debug: 这个控制文件中是否记录debug，控制台始终会有debuglog
    :param log_path: log日志文件存储路径
    :return:
    """
    global log_base_name
    if log_base_name is not None:
        raise Exception("log name cannot empty...")
    a_log = {
        "level": "DEBUG" if is_debug else "INFO",
        "handlers": ["console"],
        "propagate": "no"
    }
    LOGGING.get("handlers")["console"]["level"] = "DEBUG" if is_debug else "INFO"
    if log_path:
        a_log["handlers"] = ["console", "file"]
        file_name = os.path.join(log_path, '{}.log'.format(log_name))
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        LOGGING.get("handlers")["file"] = {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG" if is_debug else "INFO",  #
            "formatter": "simple",
            "filename": file_name,
            'mode': 'w+',
            "maxBytes": 1024*1024*20,  # 20 MB
            "backupCount": 10,
            "encoding": "utf8"
        }
    LOGGING.get('loggers')[log_name] = a_log  # 设置log实例配置
    logging.config.dictConfig(LOGGING)
    log_base_name = log_name


def get_logger(name):
    """
    获取对应log名字
    :param name:
    :return:
    """
    log = logging.getLogger("{}.{}".format(log_base_name, name))
    return log
