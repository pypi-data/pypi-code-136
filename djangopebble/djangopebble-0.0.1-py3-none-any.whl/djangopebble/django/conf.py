from django.conf import settings


# --- 默认分页器参数设置 PAGINATION_SETTINGS
PAGINATION_SETTINGS = {
    'page_size': 10,       # 每页16个
    'page_size_query_param': 'page_size',       # 前端控制每页数量时使用的参数名, 'page_size'
    'page_query_param': 'p',        # 页码控制参数名"p"
    'max_page_size': 1000,      # 最大1000页
}

if hasattr(settings, 'PAGINATION_SETTINGS'):
    PAGINATION_SETTINGS.update(settings.PAGINATION_SETTINGS)

# 系统运行日志
USE_LOG = 1
LOG_DIR_NAME = 'logs'
if USE_LOG:
    # from concurrent_log_handler import ConcurrentRotatingFileHandler
    MIDDLEWARE.append('shuangTanSuYang_dj2227.public_skills.django.RequestLogMiddleware')
    import datetime as dt
    import time

    t_str = dt.datetime.now().strftime('_%Y%m%d')
    LOG_DIR = os.path.join(BASE_DIR, LOG_DIR_NAME)
    FILE_NAME = f'debu{t_str}.log'

    LOG_FILE = os.path.join(LOG_DIR, FILE_NAME)

    if not os.path.exists(LOG_DIR):
        # os.mkdir(LOG_DIR)
        # ref: https://stackoverflow.com/questions/6004073/how-can-i-create-directories-recursively
        os.makedirs(LOG_DIR, exist_ok=True)

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            # 日志格式
            'standard': {
                'format': '{"time": "%(asctime)s", "level": "%(levelname)s", "method": "%(method)s", '
                          '"username": "%(username)s", "task_id": "%(name)s", "sip": "%(sip)s", "dip": "%(dip)s", "path": "%(path)s",'
                          ' "status_code": "%(status_code)s", "reason_phrase": "%(reason_phrase)s", "path_name": "%(pathname)s", "func": "%(module)s.%(funcName)s:%(lineno)d", "message": "%(message)s"}',
                # 'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s',
                # 'format': '{"time": "%(asctime)s","threadName":%(threadName)s,"thread":%(thread)s,"message":%(message)s:%(thread)d "level": "%(levelname)s","module": "%(module)s,"func":%(funcName)s,"lineno":%(lineno)d}',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            },
            'simple': {  # 简单格式
                'format': '[%(asctime)s] %(levelname)s %(message)s func": "%(module)s.%(funcName)s:%(lineno)d", [path_name: %(pathname)s], [name: %(name)s]'
            },
            'collect': {  # Define a special log format
                'format': '%(message)s'
            }
        },
        # 过滤器
        'filters': {
            'request_info': {'()': 'shuangTanSuYang_dj2227.public_skills.django.RequestLogFilter'},
        },
        'handlers': {
            'file': {
                'level': 'WARNING',
                # 日志保存永久
                'class': 'logging.handlers.TimedRotatingFileHandler',
                # 'class': 'concurrent_log_handler.ConcurrentRotatingFileHandler',
                'when': 'midnight',
                # 调用过滤器
                'filters': ['request_info'],
                # 'backupCount': 30,
                # 'class': 'logging.FileHandler',
                'filename': os.path.join(LOG_DIR, 'debug_{}.log'.format(time.strftime('%Y-%m-%d'))),
                'formatter': 'standard'
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file', 'console'],
                'level': 'INFO',  # 'INFO', 'DEBUG'
                'propagate': True,
            },
            # 'web.log': {
            #     'handlers': ['file', 'console'],
            #     'level': 'INFO',  # 'INFO', 'DEBUG'
            #     'propagate': True,
            # },
        },
    }



