import aws_cdk
import aws_cdk.aws_apigatewayv2_alpha
import aws_cdk.aws_apigatewayv2_integrations_alpha
import constructs

from . import api
from . import well_architected_construct


class ApiStepFunctionsConstruct(well_architected_construct.Construct):

    def __init__(
        self, scope: constructs.Construct, id: str,
        error_topic=None,
        state_machine=None,
        api_gateway_service_role=None,
        create_http_api=False,
        create_rest_api=False,
        **kwargs,
    ):
        super().__init__(
            scope, id,
            error_topic=error_topic,
            **kwargs,
        )
        self.api_construct = self.create_api(
            create_http_api=create_http_api,
            create_rest_api=create_rest_api,
            error_topic=error_topic,
            api_gateway_service_role=api_gateway_service_role,
            state_machine=state_machine,
        )
        self.create_http_api_step_functions_route(
            self.create_http_api_stepfunctions_integration(
                state_machine_arn=state_machine.state_machine_arn,
                api_id=self.api_construct.api_id,
                api_gateway_service_role_arn=api_gateway_service_role.role_arn,
            )
        )

    def create_api(self,
        create_http_api=None, create_rest_api=None,
        error_topic=None, api_gateway_service_role=None,
        state_machine=None,
    ):
        if create_http_api:
            return self.create_http_api(
                error_topic=error_topic,
                api_gateway_service_role=api_gateway_service_role,
            )
        if create_rest_api:
            return self.create_rest_api(
                error_topic=error_topic,
                state_machine=state_machine,
                api_gateway_service_role=api_gateway_service_role,
            )

    def create_http_api(self, error_topic=None, api_gateway_service_role=None):
        return api.Api(
            self, 'HttpApiGateway',
            error_topic=error_topic,
            api_gateway_service_role=api_gateway_service_role,
            api=aws_cdk.aws_apigatewayv2_alpha.HttpApi(
                self, 'HttpApi',
                create_default_stage=True,
            ),
        )

    def create_http_api_step_functions_route(self, target):
        return aws_cdk.aws_apigatewayv2.CfnRoute(
            self, 'HttpApiStateMachineDefaultRoute',
            api_id=target.api_id,
            route_key=aws_cdk.aws_apigatewayv2_alpha.HttpRouteKey.DEFAULT.key,
            target=f'integrations/{target.ref}',
        )

    def create_http_api_stepfunctions_integration(
        self, state_machine_arn=None, api_id=None, api_gateway_service_role_arn=None,
    ):
        return aws_cdk.aws_apigatewayv2.CfnIntegration(
            self, 'HttpApiStateMachineIntegration',
            api_id=api_id,
            integration_type='AWS_PROXY',
            connection_type='INTERNET',
            integration_subtype='StepFunctions-StartSyncExecution',
            credentials_arn=api_gateway_service_role_arn,
            request_parameters={
                "Input": "$request.body",
                "StateMachineArn": state_machine_arn,
            },
            payload_format_version="1.0",
            timeout_in_millis=10000
        )

    def create_rest_api(self, error_topic=None, state_machine=None, api_gateway_service_role=None):
        return api.Api(
            self, 'RestApi',
            error_topic=error_topic,
            api_gateway_service_role=api_gateway_service_role,
            api=aws_cdk.aws_apigateway.StepFunctionsRestApi(
                self, 'RestApiStepFunctions',
                state_machine=state_machine,
                deploy=True,
            )
        )
