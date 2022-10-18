from logging import Logger
import logging
import inspect
import time
import json
import sys
from json.decoder import JSONDecodeError
import uuid
import traceback

class CustomFormatter(logging.Formatter):
    """Logging colored formatter, adapted from https://stackoverflow.com/a/56944256/3638629"""

    grey = '\x1b[38;21m'
    blue = '\x1b[38;5;39m'
    yellow = '\x1b[38;5;226m'
    red = '\x1b[38;5;196m'
    bold_red = '\x1b[31;1m'
    reset = '\x1b[0m'

    def __init__(self, fmt):
        super().__init__()
        self.fmt = fmt
        self.FORMATS = {
            logging.DEBUG: self.grey + self.fmt + self.reset,
            logging.INFO: self.blue + self.fmt + self.reset,
            logging.WARNING: self.yellow + self.fmt + self.reset,
            logging.ERROR: self.red + self.fmt + self.reset,
            logging.CRITICAL: self.bold_red + self.fmt + self.reset
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

class JSONSuperLogger(Logger):
    def _log(self, level, msg, *args, **kwargs):
        """
        Low-level logging routine which creates a LogRecord and then calls
        all the handlers of this logger to handle the record.
        """
        msg = json.dumps(msg)
        super()._log(level, msg, *args, **kwargs)

class SuperLog:

    def __init__(self, app_name: str, colors = False, debug=False, **kwargs):
        unique_id = str(uuid.uuid4())
        self.debug = logging.DEBUG if debug else logging.INFO
        extra_karguments = ',"id":"{}"'.format(unique_id)
        if len(kwargs):
            for arg in kwargs:
                extra_karguments += ',"%s":"%s"' % (arg, kwargs[arg])
        self._FORMAT = '{"level":"%(levelname)s","thread":%(thread)s,"timestamp":"%(asctime)s","app":"%(name)s","log":%(message)s'+extra_karguments+'}'
        self.time = time.time()
        self.traceback = 0
        self.start_time = time.time()
        self.colors = colors
        self.logger =  self.__getLogger(app_name)



    def __getLogger(self, name: str):
        """
            Function que inicializa el logger
        :param name:
        :return:
        """

        # logger = logging.getLogger(name)
        manager = logging.Manager(JSONSuperLogger.root)
        manager.setLoggerClass(JSONSuperLogger)
        logger = manager.getLogger(name)
        logger.setLevel(self.debug)


        # Create stdout handler for logging to the console (logs all five levels)
        stdout_handler = logging.StreamHandler()
        stdout_handler.setLevel(self.debug)
        if self.colors:
            stdout_handler.setFormatter(CustomFormatter(self._FORMAT))
        else:
            stdout_handler.setFormatter(logging.Formatter(self._FORMAT))
        logger.addHandler(stdout_handler)
        logger.propagate = False
        logging.basicConfig(level=self.debug)
        return logger


    def __exception_error(self,message, execution, i=0):
        """
            Metodo que genera el json con la informacion proveniente del trace de errores
        :param message:
        :param execution:
        :param i:
        :return:
        """

        message = '''{"parameters":%s,"execution":%s,"file":"%s","line": "%s","function":"%s","statement":"%s","error":"%s","text":"%s","manual": false}''' % ( message
                                                            , execution
                                                            , inspect.trace()[i][1].replace('\\','\\\\')
                                                            , inspect.trace()[i][2]
                                                            , inspect.trace()[i][3]
                                                            , str(inspect.trace()[i][4]).replace('"','\'').replace("    ","")
                                                            , str(sys.exc_info()[0]).replace('"','\'')
                                                            , sys.exc_info()[1]
                                                          )
        return message

    def time_func_analyze(self, total_execution=False, *args, **kwargs):
        """
            Metodo decorador que permite calcular el tiempo total de una funcion
        :param total_execution:
        :param args:
        :param kwargs:
        :return:
        """
        def decorator(function):
            def func(*args, **kwargs):
                inicio = time.time()
                try:
                    result = function(*args, **kwargs)
                except:
                    self.print("Error en el codigo", traceback=traceback.print_exc())
                    exit(1)
                if total_execution:
                    message = '{"total_execution":%s}' % (round(time.time() - inicio, 2))
                else:
                    message = '{"total":%s, "function": "%s"}' % (round(time.time() - inicio, 2), function.__name__)
                self.logger.info(json.loads(message))
                return result
            return  func
        return decorator

    def error(self, message, **kwargs):
        """
            Funcion que imprime un error, en caso de no usar try y except se recomienda usar esta funcion
            para imprimir los errores
        :param message:
        :return:
        """
        message = self._format_message(message)
        self._validations(message)
        message = self._extra_arguments(message, kwargs)
        function = inspect.stack()[1].function
        execution = round(time.time() - self.time, 2)
        to_send = '{"message":%s, "execution":%s, "function":"%s", "manual": true}' % (message, execution, function)
        self.logger.error(json.loads(to_send))
        self.time = time.time()

    def info(self, message, **kwargs):
        """
            Funcion que imprime un error, en caso de no usar try y except se recomienda usar esta funcion
            para imprimir los errores
        :param message:
        :return:
        """
        message = self._format_message(message)
        self._validations(message)
        message = self._extra_arguments(message, kwargs)
        function = inspect.stack()[1].function
        execution = round(time.time() - self.time, 2)
        to_send = '{"message":%s, "execution":%s, "function":"%s", "manual": true}' % (message, execution, function)
        self.logger.info(json.loads(to_send))
        self.time = time.time()

    def warning(self, message, **kwargs):
        """
            Funcion que imprime un error, en caso de no usar try y except se recomienda usar esta funcion
            para imprimir los errores
        :param message:
        :return:
        """
        message = self._format_message(message)
        self._validations(message)
        message = self._extra_arguments(message, kwargs)
        function = inspect.stack()[1].function
        execution = round(time.time() - self.time, 2)
        to_send = '{"parameters":%s, "execution":%s, "function":"%s", "manual": true}' % (message, execution, function)
        self.logger.warning(json.loads(to_send))
        self.time = time.time()

    def _validations(self, message):
        try:
            tmp = '{"test": "%s"}' % (message)
            json.loads(tmp)
        except JSONDecodeError:
            raise Exception(f"[SuperLog] [Error transformando el mensaje {message} en JSON]")

    def _format_message(self, message):
        message = str(message).replace('\n', '\\n').replace('\r', '\\r').replace('\t', '\\t').replace('"','\\"')
        return message

    def _format_message_dict(self, message):
        for key in message:
            if type(message[key]) == dict:
                message[key] = self._format_message_dict(message[key])
            else:
                message[key] = str(message[key]).replace('\n', '\\n').replace('\r', '\\r').replace('\t', '\\t')
        return message

    def _extra_arguments(self, message, kwargs):
        params = '"message": "{}"'.format(message)
        for key in kwargs:
            params += ',"{}": "{}"'.format(key, kwargs[key])
        log_params = "{"+params+"}"

        return log_params


    def print(self, message, **kwargs):
        """
            Funcion que imprime informacion adicional de un proceso, adicionalmente reconoce automaticamente un error despues de un try: except:
            imprimiendo el error en el codigo
        :param message:
        :return:
        """
        to_send = '{"parameters":%s, "execution":%s, "function":"%s"}'
        function = inspect.stack()[1].function
        execution = round(time.time() - self.time,2)
        message = str(message)
        message = self._format_message(message)

        #message, to_send = self._validation_format(message)
        message = self._extra_arguments(message, kwargs)

        if len(inspect.trace()) != 0:
            to_send = self.__exception_error(message, execution)
            self.logger.error(json.loads(to_send))
        else:
            to_send = to_send % (message, execution, function)
            self.logger.info(json.loads(to_send))
            self.time = time.time()

