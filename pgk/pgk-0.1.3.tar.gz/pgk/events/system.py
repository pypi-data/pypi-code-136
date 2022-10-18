from .event import Event


class System(Event):
    def __init__(self) -> None:
        super().__init__()
        self.__exit = False

    def request_exit(self):
        self.__exit = True

    def get_exit_requested(self):
        return self.__exit
