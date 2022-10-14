import contextlib
import dataclasses
import io
import sys
import unittest
import unittest.mock
import irisml.core
from irisml.core.job_runner import JobRunner


class FakeTask(irisml.core.TaskBase):
    def execute(self, inputs):
        raise FakeException('fake_exception')


class FakeOnErrorTask(irisml.core.TaskBase):
    @dataclasses.dataclass
    class Inputs:
        exception: Exception

    def execute(self, inputs):
        print("The error is handled.")
        return self.Outputs()


class FakeException(RuntimeError):
    pass


class TestJobRunner(unittest.TestCase):
    def test_error_handler_is_called(self):
        job_dict = {'tasks': [{'task': 'fake_task'}], 'on_error': [{'task': 'error_handler', 'inputs': {'exception': '$env.IRISML_EXCEPTION'}}]}
        runner = JobRunner(job_dict, {})
        with unittest.mock.patch.dict(sys.modules, {'irisml.tasks.fake_task': unittest.mock.MagicMock(Task=FakeTask), 'irisml.tasks.error_handler': unittest.mock.MagicMock(Task=FakeOnErrorTask)}):
            with contextlib.redirect_stdout(io.StringIO()) as f:
                with self.assertRaises(FakeException):
                    runner.run()
            self.assertEqual(f.getvalue().strip(), 'The error is handled.')
