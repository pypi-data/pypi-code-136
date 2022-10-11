from unittest import TestCase
from unittest.mock import Mock, call, patch

from handlr.formatter import Formatter


class TestFormatter(TestCase):

    @patch('handlr.formatter.json')
    @patch('handlr.formatter.socket')
    @patch('handlr.formatter.logging')
    @patch('handlr.formatter.traceback')
    @patch('handlr.formatter.datetime')
    def setUp(self, mock_datetime, mock_traceback, mock_logging, mock_socket, mock_json):
        self.mock_datetime = mock_datetime
        self.mock_traceback = mock_traceback
        self.mock_logging = mock_logging
        self.mock_socket = mock_socket
        self.mock_json = mock_json
        self.formatter = Formatter()

    def test___init__(self):
        self.mock_socket.gethostname.assert_called_once_with()
        self.assertEqual('Main', self.formatter.label)
        self.assertEqual([], self.formatter.tags)

    @patch('handlr.formatter.socket')
    def test___init___override(self, mock_socket):
        dummy_label = 'dummy_label'
        dummy_tags = ['dummy_tags']
        formatter = Formatter(dummy_label, dummy_tags)
        mock_socket.gethostname.assert_called_once_with()
        self.assertEqual(dummy_label, formatter.label)
        self.assertEqual(dummy_tags, formatter.tags)

    def test_format(self):
        expected = b'some_serialized_data\n'
        dummy_record = 'dummy_record'
        mock_message = Mock()
        self.formatter.build_dict = Mock(return_value=mock_message)
        self.formatter.add_extra_fields = Mock(return_value='some_extra_fields')
        self.formatter.check_for_exceptions = Mock(return_value='some_message')
        self.formatter.serialize = Mock(return_value=b'some_serialized_data')
        actual = self.formatter.format(dummy_record)
        self.formatter.build_dict.assert_called_once_with(dummy_record)
        self.formatter.add_extra_fields.assert_called_once_with(dummy_record)
        mock_message.update.assert_called_once_with('some_extra_fields')
        self.formatter.check_for_exceptions.assert_called_once_with(dummy_record, mock_message)
        self.formatter.serialize.assert_called_once_with('some_message')
        self.assertEqual(expected, actual)

    def test_build_dict(self):
        mock_record = Mock()
        expected = {
            '@timestamp': 'some_timestamp',
            'message': mock_record.getMessage(),
            'level': mock_record.levelname,
            'name': mock_record.name,
            'host': self.formatter.host,
            'label': self.formatter.label,
            'tags': self.formatter.tags,
        }
        self.formatter.format_timestamp = Mock(return_value='some_timestamp')
        actual = self.formatter.build_dict(mock_record)
        self.formatter.format_timestamp.assert_called_once_with(mock_record.created)
        self.assertEqual(expected, actual)

    @patch('handlr.formatter.datetime')
    def test_format_timestamp(self, mock_datetime):
        expected = 'some_timestamp'
        dummy_time = 'dummy_time'
        mock_datetime.utcfromtimestamp = Mock(return_value=Mock(isoformat=Mock(return_value='some_timestamp')))
        actual = self.formatter.format_timestamp(dummy_time)
        mock_datetime.utcfromtimestamp.assert_called_once_with(dummy_time)
        mock_datetime.utcfromtimestamp().isoformat.assert_called_once_with()
        self.assertEqual(expected, actual)

    def test_add_extra_fields(self):
        expected = {'key_1': 'some_field', 'key_3': 'some_field'}

        class Record(object):
            def __init__(self):
                self.key_1 = 'value_1'
                self.key_2 = 'value_2'
                self.key_3 = 'value_3'

        dummy_record = Record()
        self.formatter.get_known_skips = Mock(return_value=('key_2',))
        self.formatter.add_field = Mock(return_value='some_field')
        actual = self.formatter.add_extra_fields(dummy_record)
        self.formatter.get_known_skips.assert_called_once_with()
        add_field_calls = [call('value_1'), call('value_3')]
        self.formatter.add_field.assert_has_calls(add_field_calls)
        self.assertEqual(expected, actual)

    def test_get_known_skips(self):
        expected = (
            'args', 'asctime', 'created', 'exc_info', 'exc_text', 'filename',
            'funcName', 'id', 'levelname', 'levelno', 'lineno', 'module',
            'msecs', 'msecs', 'message', 'msg', 'name', 'pathname', 'process',
            'processName', 'relativeCreated', 'thread', 'threadName', 'extra',
            'auth_token', 'password', 'stack_info'
        )
        actual = self.formatter.get_known_skips()
        self.assertEqual(expected, actual)

    def test_add_field_easy_type(self):
        expected = 'dummy_value'
        dummy_value = 'dummy_value'
        self.formatter.get_easy_types = Mock(return_value=(str, bool))
        actual = self.formatter.add_field(dummy_value)
        self.formatter.get_easy_types.assert_called_once_with()
        self.assertEqual(expected, actual)

    def test_add_field_not_easy_type(self):
        expected = repr('dummy_value')
        dummy_value = 'dummy_value'
        self.formatter.get_easy_types = Mock(return_value=(bool, int))
        actual = self.formatter.add_field(dummy_value)
        self.formatter.get_easy_types.assert_called_once_with()
        self.assertEqual(expected, actual)

    def test_get_easy_types(self):
        expected = (str, bool, dict, float, int, list, type(None))
        actual = self.formatter.get_easy_types()
        self.assertEqual(expected, actual)

    def test_check_for_exceptions_none(self):
        mock_message = Mock()
        expected = mock_message
        mock_record = Mock(exc_info=None)
        self.formatter.get_debug_fields = Mock()
        actual = self.formatter.check_for_exceptions(mock_record, mock_message)
        self.formatter.get_debug_fields.assert_not_called()
        mock_message.update.assert_not_called()
        self.assertEqual(expected, actual)

    def test_check_for_exceptions_with_exc(self):
        mock_message = Mock()
        expected = mock_message
        mock_record = Mock(exc_info=True)
        self.formatter.get_debug_fields = Mock(return_value='some_debug_fields')
        actual = self.formatter.check_for_exceptions(mock_record, mock_message)
        self.formatter.get_debug_fields.assert_called_once_with(mock_record)
        mock_message.update.assert_called_once_with('some_debug_fields')
        self.assertEqual(expected, actual)

    def test_get_debug_fields_with_additions(self):
        class Record(object):
            def __init__(self):
                self.exc_info = 'some_exc_info'
                self.lineno = 'some_lineno'
                self.process = 'some_process'
                self.threadName = 'some_threadName'
                self.funcName = 'some_funcName'
                self.processName = 'some_processName'

        record = Record()

        expected = {
            'lineno': 'some_lineno',
            'process': 'some_process',
            'stack_trace': 'some_formatted_exception',
            'thread_name': 'some_threadName',
            'funcName': 'some_funcName',
            'processName': 'some_processName'
        }
        self.formatter.format_exception = Mock(return_value='some_formatted_exception')
        actual = self.formatter.get_debug_fields(record)
        self.formatter.format_exception.assert_called_once_with('some_exc_info')
        self.assertEqual(expected, actual)

    def test_get_debug_fields_without_additions(self):
        class Record(object):
            def __init__(self):
                self.exc_info = 'some_exc_info'
                self.lineno = 'some_lineno'
                self.process = 'some_process'
                self.threadName = 'some_threadName'

        record = Record()

        expected = {
            'lineno': 'some_lineno',
            'process': 'some_process',
            'stack_trace': 'some_formatted_exception',
            'thread_name': 'some_threadName'
        }
        self.formatter.format_exception = Mock(return_value='some_formatted_exception')
        actual = self.formatter.get_debug_fields(record)
        self.formatter.format_exception.assert_called_once_with('some_exc_info')
        self.assertEqual(expected, actual)

    @patch('traceback.format_exception', return_value='some_exception')
    def test_format_exception_with_exc_info(self, mock_traceback_format_exception):
        expected = 'some_exception'
        dummy_exc_info = 'dummy_exc_info'
        actual = self.formatter.format_exception(dummy_exc_info)
        mock_traceback_format_exception.assert_called_once_with(*dummy_exc_info)
        self.assertEqual(expected, actual)

    @patch('traceback.format_exception')
    def test_format_exception_without_exc_info(self, mock_traceback_format_exception):
        expected = ""
        dummy_exc_info = None
        actual = self.formatter.format_exception(dummy_exc_info)
        mock_traceback_format_exception.assert_not_called()
        self.assertEqual(expected, actual)

    @patch('handlr.formatter.json')
    @patch('handlr.formatter.bytes', return_value='some_serialized_data')
    def test_serialize(self, mock_bytes, mock_json):
        expected = 'some_serialized_data'
        dummy_message = 'dummy_message'
        mock_json.dumps = Mock(return_value='some_json_dump')
        actual = self.formatter.serialize(dummy_message)
        mock_json.dumps.assert_called_once_with(dummy_message)
        mock_bytes.assert_called_once_with('some_json_dump', encoding='u8')
        self.assertEqual(expected, actual)


# That's all folks...
