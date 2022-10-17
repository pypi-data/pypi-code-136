import time
from AppKit import NSObject, NSWorkspace

from common import _Listener

class MacOsSleepListener(NSObject):

    def __init__(self, callback):
        self.callback = callback
        NSWorkspace.sharedWorkspace().notificationCenter().addObserver_selector_name_object_(
            self, self.sleepNotification_, "NSWorkspaceWillSleepNotification", None)

    def sleepNotification_(self, notification):
        print(notification)
        self.callback()

class Listener(_Listener):

    def _event_thread(self):
        self._nsobj = MacOsSleepListener(self.on_sleep)
        while True:
            time.sleep(1)