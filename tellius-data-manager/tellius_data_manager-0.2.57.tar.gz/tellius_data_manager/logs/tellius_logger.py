# Copyright 2022 Tellius, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import inspect
import logging.config
import logging


class TelliusLogger(logging.getLoggerClass()):  # type: ignore
    """Logger with standard logging format specified as JSON with application format requirements."""

    logging.config.dictConfig(
        {
            "version": 1,
            "formatters": {
                "json": {
                    "()": "logging_json.JSONFormatter",
                    "fields": {
                        "level_name": "levelname",
                        "thread_name": "threadName",
                        "process_name": "processName",
                        "module": "module",
                        "function": "funcName",
                        "time": "created",
                    },
                }
            },
            "handlers": {
                "standard_output": {
                    "class": "logging.StreamHandler",
                    "formatter": "json",
                    "stream": "ext://sys.stdout",
                },
            },
            "loggers": {"my_app": {"level": "DEBUG"}},
            "root": {"level": "INFO", "handlers": ["standard_output"]},
        }
    )

    def _log(self, level: str, msg: object, args, exc_info=None, extra=None):
        if extra is None:
            class_info = ""
            for index in range(5,0,-1):
                try:
                    class_info = inspect.stack()[2][0].f_locals["self"].__class__.__name__
                    break
                except:
                    pass
            extra = {"class": class_info}

        super()._log(level, msg, args, exc_info, extra)
