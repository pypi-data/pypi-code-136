import logging
import os
from typing import Dict, Any, List, Tuple, Callable as Function
from threading import Thread
from ..colors import green, end, red, purple, blue, bold_blue


class BasicEventEmitter:
    def __init__(self):
        self._events = {}
        Thread(target=self._resolve).start()

    def on(self, name: str, func: Function[..., Any]) -> None:
        if name not in self._events:
            self._events[name] = {"input_args": [], "input_kwargs": [], "resolved": 0}
        self._events[name].update({"func": func, "once": False})
        logging.info(
            f'{green}[FILE] Utils/EventEmitter.py{end}\n{green}[INFO]{end} tied event "{name}" to function "{func}"\n{purple}[ONCE]{end} False'
        )

    def once(self, name: str, func: Function[..., Any]) -> None:
        if name not in self._events:
            self._events[name] = {"input_args": [], "input_kwargs": [], "resolved": 0}

        self._events[name].update({"func": func, "once": True})
        logging.info(
            f'{green}[FILE] Utils/EventEmitter.py{end}\n{green}[INFO]{end} tied event "{name}" to function "{func}"\n{purple}[ONCE]{end} True'
        )

    def emit(self, name: str, *args, **kwargs) -> None:
        if name not in self._events:
            self._events[name] = {
                "input_args": [],
                "input_kwargs": [],
                "resolved": 0,
            }
        self._events[name]["resolved"] += 1
        self._events[name]["input_args"].append(args)
        self._events[name]["input_kwargs"].append(kwargs)
        logging.info(
            f'{green}[FILE] Utils/EventEmitter.py{end}\n{green}[INFO]{end} Emitted event "{name}"\n\t{blue}[SUMMARY]{end} emitted event "name" with following parameters\n\t{purple}[EXTRA]{end}\n\t\t{bold_blue}[*ARGS]{end} {args}\n\t\t{bold_blue}[**KWARGS]{end} {kwargs}'
        )

    def _resolve(self):
        while True:
            once = []
            current = None
            try:
                for i in self._events:
                    if (
                        self._events[i]["resolved"] > 0
                        and "func" in self._events[i]
                        and "input_args" in self._events[i]
                        and "input_kwargs" in self._events[i]
                        and len(self._events[i]["input_args"]) > 0
                        and len(self._events[i]["input_kwargs"]) > 0
                    ):
                        logging.info(
                            f"{green}[FILE] Utils/EventEmitter.py{end}\n{green}[INFO]{end} Resolved Event \"{i}\"\n\t{blue}[SUMMARY]{end} successfully called and executed event \"{i}\" with the following parameters.\n\t{purple}[EXTRA]{end}\n\t\t{bold_blue}[FUNC]{end} {self._events[i]['func']}\n\t\t{bold_blue}[INPUT ARGS]{end} {self._events[i]['input_args'][-1]}\n\t\t{bold_blue}[INPUT KWARGS]{end} {self._events[i]['input_kwargs'][-1]}"
                        )
                        if self._events[i]["once"]:
                            once.append(i)
                        current_args = self._events[i]["input_args"][-1]
                        current_kwargs = self._events[i]["input_kwargs"][-1]
                        current = i
                        self._events[i]["func"](*current_args, **current_kwargs)
                        self._events[i]["resolved"] -= 1
                        self._events[i]["input_args"].pop()
                        self._events[i]["input_kwargs"].pop()

                    elif (
                        len(self._events[i]["input_args"]) == 0
                        or len(self._events[i]["input_kwargs"]) == 0
                    ):
                        self._events[i]["resolved"] = 0
                for i in once:
                    del self._events[i]
            except Exception as e:
                if type(e) in (RuntimeError, IndexError):
                    continue
                logging.error(
                    f"{green}[FILE] Utils/EventEmitter.py{end}\n{red}[EXCEPTION]{end}",
                    exc_info=True,
                )
                print("-" * os.get_terminal_size().columns)
                self._events[current]["resolved"] -= 1
                self._events[current]["input_args"].pop()
                self._events[current]["input_kwargs"].pop()
