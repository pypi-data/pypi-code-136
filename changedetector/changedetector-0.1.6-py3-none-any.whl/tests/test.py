import os
import sys
import unittest
from unittest.mock import patch
from unittest.mock import MagicMock

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__))))

from detectchange import _Watcher
from detectchange import activate
from wro import WroHandler
from wrs import WrsHandler

class TestDetectChange(unittest.TestCase):
    def setUp(self):
        self.watcher1 = _Watcher(WrsHandler)
        self.watcher2 = _Watcher(WroHandler)

    def test_on_any_event(self):
        event = MagicMock()
        self.watcher1.on_any_event(event)
        self.watcher2.on_any_event(event)

    def test_run(self):
        with patch('detectchange._Watcher.on_any_event') as mock_on_any_event:
            self.watcher1.run()
            mock_on_any_event.assert_called_once()

    def test_activate(self):
        with patch('detectchange._Watcher.run') as mock_run:
            activate()
            mock_run.assert_called_once()

if __name__ == '__main__':
    unittest.main()
