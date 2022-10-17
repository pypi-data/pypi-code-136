from typing import Optional, Tuple, Dict, List
import os
import sys
import logging
import inspect


def get_backup_num(filedir: str, filename: str) -> int:
    """Get a max integer suffix for a prefix.

    Args:
        filedir: Directory of files
        filename: Prefix filename

    """
    backup_files = [x for x in os.listdir(filedir) if x.startswith(filename)]
    backup_maybe_nums = [b.split('.')[-1] for b in backup_files]
    backup_nums = [int(x) for x in backup_maybe_nums
                   if any([_ in x for _ in list(map(str, range(10)))])]
    if backup_nums:
        cur_backup_num = max(backup_nums) + 1
    else:
        cur_backup_num = 0
    return cur_backup_num


def get_file_and_stream_logger(logdir: Optional[str], logger_name: str,
                               log_file_name: Optional[str],
                               stream_log_level: Optional[str] = "info",
                               file_log_level: Optional[str] = "debug",
                               logger_level: Optional[str] = "debug",
                               new_file: Optional[bool] = True,
                               datefmt: Optional[str] = None,
                               fmt: Optional[str] = None,
                               no_file_logger: bool = False,
                               no_stream_logger: bool = False) -> Tuple[str, logging.Logger]:
    """Get a Logger with sensible defaults.

    Args:
        logdir: Directory in which to write the log file
        logger_name: Name of the logger
        log_file_name: Name of the log file. If it doesn't end with ".log" it's appended
        stream_log_level: Log level for stream logger
        file_log_level: Log level for file logger
        logger_level: Log level of logger
        new_file: Should we create a new file or append to existing log file?
        datefmt: Timestamp format
        fmt: Logger format
        no_file_logger: Don't create a file logger
        no_stream_logger: Don't create a stream logger

    Returns:
        A tuple of filename and the logger instance
    """
    if not datefmt:
        datefmt = '%Y/%m/%d %I:%M:%S %p'
    if not fmt:
        '%(asctime)s %(message)s'
    logger = logging.getLogger(logger_name)
    formatter = logging.Formatter(datefmt=datefmt, fmt=fmt)
    if not no_file_logger and logdir and log_file_name:
        if not os.path.exists(logdir):
            os.mkdir(logdir)
        if not log_file_name.endswith('.log'):
            log_file_name += '.log'
        log_file = os.path.abspath(os.path.join(logdir, log_file_name))
        if new_file and os.path.exists(log_file):
            backup_num = get_backup_num(logdir, log_file_name)
            os.rename(log_file, log_file + '.' + str(backup_num))
        file_handler = logging.FileHandler(log_file)
    else:
        log_file = ""
    if not no_stream_logger:
        stream_handler = logging.StreamHandler(sys.stdout)
        if stream_log_level is not None and hasattr(logging, stream_log_level.upper()):
            stream_handler.setLevel(getattr(logging, stream_log_level.upper()))
        else:
            stream_handler.setLevel(logging.INFO)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
    if not no_file_logger:
        if file_log_level is not None and hasattr(logging, file_log_level.upper()):
            file_handler.setLevel(getattr(logging, file_log_level.upper()))
        else:
            file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    if logger_level is not None and hasattr(logging, logger_level.upper()):
        logger.setLevel(getattr(logging, logger_level.upper()))
    else:
        logger.setLevel(logging.DEBUG)
    return log_file, logger


def get_file_logger(logdir, logger_name: str,
                    log_file_name: str,
                    log_level: Optional[str] = "debug",
                    logger_level: Optional[str] = "debug",
                    new_file: Optional[bool] = True,
                    datefmt: Optional[str] = None,
                    fmt: Optional[str] = None) -> Tuple[str, logging.Logger]:
    return get_file_and_stream_logger(logdir, logger_name, log_file_name,
                                      file_log_level=log_level,
                                      logger_level=logger_level,
                                      new_file=new_file,
                                      no_stream_logger=True,
                                      datefmt=datefmt,
                                      fmt=fmt)


def get_stream_logger(logger_name: str,
                      log_level: Optional[str] = "debug",
                      logger_level: Optional[str] = "debug",
                      new_file: Optional[bool] = True,
                      datefmt: Optional[str] = None,
                      fmt: Optional[str] = None) -> logging.Logger:
    return get_file_and_stream_logger(None, logger_name, None,
                                      stream_log_level=log_level,
                                      logger_level=logger_level,
                                      no_file_logger=True,
                                      datefmt=datefmt,
                                      fmt=fmt)[1]


# Utility functions to ease logging
# These are hacky functions and should not be used in production code
# Perhaps a wrapper would be better, or a function class
def _logi(logger: logging.Logger, x: str) -> str:
    "Log to INFO and return string with name of calling function"
    f = inspect.currentframe()
    if f and f.f_back:
        prev_func = inspect.getframeinfo(f.f_back).function
        x = f"[{prev_func}()] " + x
        logger.info(x)
        return x
    else:
        return ""


def _logd(logger: logging.Logger, x: str) -> str:
    "Log to DEBUG and return string with name of calling function"
    f = inspect.currentframe()
    if f and f.f_back:
        prev_func = inspect.getframeinfo(f.f_back).function
        x = f"[{prev_func}()] " + x
        logger.debug(x)
        return x
    else:
        return ""


def _logw(logger: logging.Logger, x: str) -> str:
    "Log to WARN and return string with name of calling function"
    f = inspect.currentframe()
    if f and f.f_back:
        prev_func = inspect.getframeinfo(f.f_back).function
        x = f"[{prev_func}()] " + x
        logger.warn(x)
        return x
    else:
        return ""


def _loge(logger: logging.Logger, x: str) -> str:
    "Log to ERROR and return string with name of calling function"
    f = inspect.currentframe()
    if f and f.f_back:
        prev_func = inspect.getframeinfo(f.f_back).function
        x = f"[{prev_func}()] " + x
        logger.error(x)
        return x
    else:
        return ""
