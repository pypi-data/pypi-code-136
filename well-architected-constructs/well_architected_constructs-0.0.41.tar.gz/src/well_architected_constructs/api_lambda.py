import aws_cdk
import constructs
import aws_cdk.aws_apigatewayv2_alpha
import aws_cdk.aws_apigatewayv2_integrations_alpha

from . import api
from . import lambda_function
from . import well_architected_construct


class ApiLambdaConstruct(well_architected_construct.Construct):

    def __init__(
        self, scope: constructs.Construct, id: str,
        create_http_api=False,
        create_rest_api=False,
        duration=60,
        error_topic=None,
        function_name=None,
        lambda_directory=None,
        event_bridge_rule=None,
        environment_variables=None,
        concurrent_executions=None,
        handler_name='handler',
        layers:list[str]=None,
        on_success=None,
        on_failure=None,
        retry_attempts=None,
        sns_trigger_topic=None,
        sqs_trigger_queue=None,
        vpc=None,
        **kwargs
    ) -> None:
        super().__init__(
            scope, id,
            error_topic=error_topic,
            **kwargs
        )
        self.lambda_construct = lambda_function.LambdaFunctionConstruct(
            self, 'LambdaFunction',
            concurrent_executions=concurrent_executions,
            duration=duration,
            environment_variables=environment_variables,
            error_topic=error_topic,
            event_bridge_rule=event_bridge_rule,
            function_name=function_name,
            handler_name=handler_name,
            lambda_directory=lambda_directory,
            layers=layers,
            on_success=on_success,
            on_failure=on_failure,
            retry_attempts=retry_attempts,
            sns_trigger_topic=sns_trigger_topic,
            sqs_trigger_queue=sqs_trigger_queue,
            vpc=vpc,
        )
        self.lambda_function = self.lambda_construct.lambda_function
        self.api_construct = self.create_api(
            create_http_api=create_http_api,
            create_rest_api=create_rest_api,
            lambda_function=self.lambda_function,
            error_topic=error_topic,
        )

    def create_api(self,
        create_http_api=None, create_rest_api=None,
        lambda_function=None, error_topic=None
    ):
        if create_http_api:
            return self.create_http_api_lambda(
                lambda_function=lambda_function,
                error_topic=error_topic
            )
        if create_rest_api:
            return self.create_rest_api_lambda(
                lambda_function=lambda_function,
                error_topic=error_topic
            )

    def create_http_api_lambda(
        self, error_topic=None, lambda_function=None
    ):
        return api.Api(
            self, 'HttpApiGateway',
            error_topic=error_topic,
            api_gateway_service_role=False,
            api=aws_cdk.aws_apigatewayv2_alpha.HttpApi(
                self, 'HttpApi',
                default_integration=aws_cdk.aws_apigatewayv2_integrations_alpha.HttpLambdaIntegration(
                    'HttpApiLambdaFunction',
                    handler=lambda_function
                ),
            )
        )

    def create_rest_api_lambda(
        self, error_topic=None, lambda_function=None,
        proxy=True
    ):
        return api.Api(
            self, 'RestApiGateway',
            error_topic=error_topic,
            api_gateway_service_role=False,
            api=aws_cdk.aws_apigateway.LambdaRestApi(
                self, 'RestApiLambdaFunction',
                handler=lambda_function,
                proxy=proxy,
            )
        )