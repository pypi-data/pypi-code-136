import aws_cdk
import constructs

from . import lambda_function
from . import well_architected_construct


class SnsLambda(well_architected_construct.WellArchitected):

    def __init__(
        self, scope: constructs.Construct, id: str,
        sns_topic: aws_cdk.aws_sns.Topic=None,
        error_topic=None,
        function_name=None,
        environment_variables=None,
        lambda_directory=None,
        **kwargs
    ) -> None:
        super().__init__(
            scope, id,
            error_topic=error_topic,
            **kwargs
        )

        self.lambda_construct = lambda_function.create_python_lambda_function(
            scope,
            function_name=function_name,
            error_topic=error_topic,
            lambda_directory=lambda_directory,
            environment_variables=environment_variables,
        )
        self.lambda_function = self.lambda_construct.lambda_function
        sns_topic.add_subscription(
            aws_cdk.aws_sns_subscriptions.LambdaSubscription(
                self.lambda_function
            )
        )