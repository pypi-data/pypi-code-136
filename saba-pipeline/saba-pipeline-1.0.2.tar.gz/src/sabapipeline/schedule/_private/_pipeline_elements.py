import time

from ... import Event, TriggererEventSource
from ..._private._utilities import *


class PeriodicEventSource(TriggererEventSource):
    def __init__(self,
                 generator_function: Callable[[], Event],
                 sec_to_regenerate: int,
                 # TODO add start and end time in the format of cron schedule expression
                 **kwargs):
        super().__init__(**kwargs)
        self.generator_function = generator_function
        self.sec_to_regenerate = sec_to_regenerate
        self.consuming: bool = False

    def start_generating(self) -> None:
        self.consuming = True
        threading.Thread(target=self._repetitively_generate).start()

    def _repetitively_generate(self):
        last_run: float = time.time()
        while self.consuming:
            try:
                time.sleep(0.1)
                now = time.time()
                if (last_run // self.sec_to_regenerate) != (now // self.sec_to_regenerate):
                    event: Event = self.generator_function()
                    last_run = now
                    self.process_generated_event(event)
            except Exception as e:
                self.logger.exception(f'Failed to generate event at time: "{str(e)}"')

    def stop_generating(self) -> None:
        self.consuming = False
