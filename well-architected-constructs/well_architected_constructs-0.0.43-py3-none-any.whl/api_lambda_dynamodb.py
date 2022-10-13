from time import time
import constructs

from . import api_lambda
from . import dynamodb_table
from . import well_architected_construct


class ApiLambdaDynamodbConstruct(api_lambda.ApiLambdaConstruct):

    def __init__(
        self, scope: constructs.Construct, id: str,
        time_to_live_attribute=None,
        sort_key=None,
        partition_key=None,
        **kwargs
    ) -> None:
        super().__init__(
            scope, id,
            **kwargs
        )
        self.dynamodb_construct = dynamodb_table.DynamodbTableConstruct(
            self, 'DynamoDbTable',
            partition_key=partition_key,
            sort_key=sort_key,
            time_to_live_attribute=time_to_live_attribute,
            error_topic=self.error_topic,
        )
        self.dynamodb_table = self.dynamodb_construct.dynamodb_table
        self.lambda_function.add_environment(
            key='DYNAMODB_TABLE_NAME',
            value=self.dynamodb_table.table_name
        )
        self.dynamodb_table.grant_read_write_data(self.lambda_function)
