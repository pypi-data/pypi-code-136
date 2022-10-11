from unittest import TestCase
from unittest.mock import Mock, patch

from handlr import Handler


class TestInit(TestCase):

    @patch('handlr.SocketHandler.__init__')
    @patch('handlr.Formatter')
    def setUp(self, mock_formatter, mock_socket_handler___init__):
        self.mock_socket_handler___init__ = mock_socket_handler___init__
        self.mock_formatter = mock_formatter
        self.dummy_host = 'dummy_host'
        self.dummy_port = 5040
        self.handler = Handler(self.dummy_host, self.dummy_port)

    def test___init__(self):
        self.mock_socket_handler___init__.assert_called_once_with(self.dummy_host, self.dummy_port)
        self.mock_formatter.assert_called_once_with(None, None)

    @patch('handlr.SocketHandler.__init__')
    @patch('handlr.Formatter')
    def test___init___override(self, mock_formatter, mock_socket_handler_init):
        dummy_host = 'dummy_host'
        dummy_port = 5040
        dummy_label = 'dummy_label'
        dummy_tags = ['dummy_tags']
        Handler(dummy_host, dummy_port, dummy_label, dummy_tags)
        mock_socket_handler_init.assert_called_once_with(dummy_host, dummy_port)
        mock_formatter.assert_called_once_with(dummy_label, dummy_tags)

    def test_makePickle(self):
        expected = 'some_pickle'
        dummy_record = 'dummy_record'
        self.handler.formatter = Mock(format=Mock(return_value='some_pickle'))
        actual = self.handler.makePickle(dummy_record)
        self.handler.formatter.format.assert_called_once_with(dummy_record)
        self.assertEqual(expected, actual)


# That's all folks...
