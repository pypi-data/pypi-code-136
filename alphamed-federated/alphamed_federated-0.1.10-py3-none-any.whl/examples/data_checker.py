"""A simple examlple for DataChecker."""

from alphafed.scheduler import DataChecker


class DemoDataChecker(DataChecker):

    def verify_data(self) -> bool:
        return True


checker = DemoDataChecker(task_id='TASK_ID')
checker.execute_verification()
