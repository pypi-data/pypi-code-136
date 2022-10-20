from abc import ABC
from datetime import datetime

class BasicTheme(ABC):
    
    @staticmethod
    def title(text: str):
        return f"\033[107m\033[30m\033[1m{text}\033[0m\n"

    @staticmethod
    def plain(text: str):
        return f"<print at {datetime.now().isoformat(' ')}> {text}\n"

    @staticmethod
    def complete(text: str):
        return f"\033[92m\033[1m<error at {datetime.now().isoformat(' ')}> {text}\033[0m\n"

    @staticmethod
    def report(text: str):
        return f"\033[37m\033[1m<report at {datetime.now().isoformat(' ')}>\033[0m {text}\n"

    @staticmethod
    def error(text: str):
        return f"\033[91m\033[1m<error at {datetime.now().isoformat(' ')}> {text}\033[0m\n"

    @staticmethod
    def warning(text: str):
        return f"\033[93m\033[1m<warning at {datetime.now().isoformat(' ')}> {text}\033[0m\n"