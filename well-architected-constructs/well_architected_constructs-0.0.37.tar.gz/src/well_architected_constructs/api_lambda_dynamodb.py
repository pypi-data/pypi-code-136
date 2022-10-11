from time import time
import constructs

from . import api_lambda
from . import dynamodb_table
from . import well_architected_construct
# from . import lambda_function


class ApiLambdaDynamodbConstruct(well_architected_construct.Construct):

    def __init__(
        self, scope: constructs.Construct, id: str,
        function_name=None,
        partition_key=None,
        error_topic=None,
        lambda_directory=None,
        duration=60,
        event_bridge_rule=None,
        time_to_live_attribute=None,
        sort_key=None,
        create_http_api=False,
        create_rest_api=False,
        **kwargs
    ) -> None:
        super().__init__(
            scope, id,
            error_topic=error_topic,
            **kwargs
        )
        self.dynamodb_construct = dynamodb_table.DynamodbTableConstruct(
            self, 'DynamoDbTable',
            partition_key=partition_key,
            sort_key=sort_key,
            time_to_live_attribute=time_to_live_attribute,
            error_topic=error_topic,
        )
        self.api_lambda_construct = api_lambda.ApiLambdaConstruct(
            self, 'ApiLambda',
            function_name=function_name,
            create_http_api=create_http_api,
            create_rest_api=create_rest_api,
            lambda_directory=lambda_directory,
            duration=duration,
            error_topic=error_topic,
            event_bridge_rule=event_bridge_rule,
            environment_variables={
                'DYNAMODB_TABLE_NAME': self.dynamodb_construct.dynamodb_table.table_name
            },
        )
        self.lambda_construct = self.api_lambda_construct.lambda_construct
        self.api_construct = self.api_lambda_construct.api_construct
        self.api = self.api_construct.api
        self.dynamodb_construct.dynamodb_table.grant_read_write_data(
            self.api_lambda_construct.lambda_function
        )
