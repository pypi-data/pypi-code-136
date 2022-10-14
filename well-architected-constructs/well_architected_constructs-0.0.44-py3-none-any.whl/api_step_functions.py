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
        state_machine_definition=None,
        create_http_api=False,
        create_rest_api=False,
        **kwargs,
    ):
        super().__init__(
            scope, id,
            error_topic=error_topic,
            **kwargs,
        )
        self.state_machine = self.create_express_state_machine(
            state_machine_definition
        )
        self.api_gateway_service_role = self.create_api_gateway_service_role(
            self.state_machine.state_machine_arn
        )
        self.api_construct = self.create_api(
            create_http_api=create_http_api,
            create_rest_api=create_rest_api,
            error_topic=error_topic,
            api_gateway_service_role=self.api_gateway_service_role,
            state_machine=self.state_machine,
        )

    def create_express_state_machine(self, state_machine_definition=None, timeout=None, ):
        return aws_cdk.aws_stepfunctions.StateMachine(
            self, 'StateMachine',
            definition=state_machine_definition,
            timeout=timeout,
            tracing_enabled=True,
            state_machine_type=aws_cdk.aws_stepfunctions.StateMachineType.EXPRESS,
        )

    @staticmethod
    def state_machine_execution_permissions(state_machine_arn):
        return aws_cdk.aws_iam.PolicyDocument(
            statements=[
                aws_cdk.aws_iam.PolicyStatement(
                    actions=["states:StartSyncExecution"],
                    effect=aws_cdk.aws_iam.Effect.ALLOW,
                    resources=[state_machine_arn]
                )
            ]
        )

    def create_api_gateway_service_role(self, state_machine_arn):
        return aws_cdk.aws_iam.Role(
            self, 'StateMachineApiGatewayIamServiceRole',
            assumed_by=aws_cdk.aws_iam.ServicePrincipal('apigateway.amazonaws.com'),
            inline_policies={
                "AllowSFNExec": self.state_machine_execution_permissions(state_machine_arn)
            }
        )

    def create_http_api(
        self, error_topic=None, api_gateway_service_role=None, state_machine=None,
    ):
        api_construct = api.Api(
            self, 'HttpApiGateway',
            error_topic=error_topic,
            api_gateway_service_role=api_gateway_service_role,
            api=aws_cdk.aws_apigatewayv2_alpha.HttpApi(
                self, 'HttpApi',
                create_default_stage=True,
            ),
        )
        self.create_http_api_step_functions_route(
            self.create_http_api_stepfunctions_integration(
                state_machine_arn=state_machine.state_machine_arn,
                api_id=api_construct.api_id,
                api_gateway_service_role_arn=api_gateway_service_role.role_arn,
            )
        )
        return api_construct

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

    def create_api(self,
        create_http_api=None, create_rest_api=None,
        error_topic=None, api_gateway_service_role=None,
        state_machine=None,
    ):
        if create_http_api:
            return self.create_http_api(
                error_topic=error_topic,
                state_machine=state_machine,
                api_gateway_service_role=api_gateway_service_role,
            )
        if create_rest_api:
            return self.create_rest_api(
                error_topic=error_topic,
                state_machine=state_machine,
                api_gateway_service_role=api_gateway_service_role,
            )
