import aws_cdk
import constructs
import aws_cdk.aws_apigatewayv2_alpha
import aws_cdk.aws_apigatewayv2_integrations_alpha

from . import api
from . import lambda_function
from . import well_architected_construct


class ApiLambda(well_architected_construct.WellArchitected):

    def __init__(
        self, scope: constructs.Construct, id: str,
        create_http_api=False,
        create_rest_api=False,
        proxy=True,
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
        self.create_rest_api = create_rest_api
        self.create_http_api = create_http_api
        self.lambda_construct = lambda_function.LambdaFunction(
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
            lambda_function=self.lambda_function,
            error_topic=error_topic,
            proxy=proxy,
        )

    def create_http_api_method(self, path=None, lambda_function=None):
        return self.api_construct.api.add_routes(
            path=f'/{path}',
            methods=[aws_cdk.aws_apigatewayv2_alpha.HttpMethod.GET],
            integration=aws_cdk.aws_apigatewayv2_integrations_alpha.HttpLambdaIntegration(
                f'HttpApi{path.title()}Integration',
                handler=lambda_function
            ),
        )

    def create_rest_api_method(self, path=None, lambda_function=None):
        return self.api_construct.api.root.resource_for_path(path).add_method(
            'GET', aws_cdk.aws_apigateway.LambdaIntegration(lambda_function)
        )

    def add_method(self, path=None, lambda_function=None):
        if self.create_http_api:
            return self.create_http_api_method(path=path, lambda_function=lambda_function)
        if self.create_rest_api:
            return self.create_rest_api_method(path=path, lambda_function=lambda_function)

    def create_api(self,
        lambda_function=None, error_topic=None, proxy=True,
    ):
        if self.create_http_api:
            return self.create_http_api_lambda(
                lambda_function=lambda_function,
                error_topic=error_topic
            )
        if self.create_rest_api:
            return self.create_rest_api_lambda(
                lambda_function=lambda_function,
                error_topic=error_topic,
                proxy=proxy
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