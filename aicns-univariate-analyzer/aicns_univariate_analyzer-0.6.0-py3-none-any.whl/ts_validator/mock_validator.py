"""

"""

from univariate.ts_validator import Validator
from pyspark.sql import DataFrame
from univariate.analyzer import AnalysisReport


class MockValidator(Validator):
    """
    Mock Validator
    """

    def validate(self, ts: DataFrame, time_col_name: str) -> AnalysisReport:
        """

        :param ts:
        :param time_col_name:
        :return:
        """
        report = AnalysisReport()
        report.parameters["validated_df"] = ts
        return report
