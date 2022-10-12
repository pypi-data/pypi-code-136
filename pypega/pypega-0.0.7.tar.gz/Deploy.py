import pega_environment.pega_environment as pega_environment    

## Orchestrator initalisation
orchestrator = pega_environment.PegaEnvironment("orchestrator", "https://sleij.pegatsdemo.com/prweb")

orchestrator.set_api_response_logging_level(0)

## OAuth 2.0 authentication for Orchestrator environment
orchestrator.set_authentication_method(
    orchestrator.AUTHENTICATION_METHOD_OAUTH2_CLIENT_CREDENTIALS,
    "10825762515797159851",
    "A65775712FFB4402D9104A822E9D7CD9",
)
##orchestrator.set_api_response_logging_level(1)

## Abort all existing deployments and tigger a new one
orchestrator.abort_all_deployments_for_pipeline(
    "Pipeline-CLX19", "Starting fresh deployments"
)

## Provide values for execution
pipeline_id = "Pipeline-CLX19"
deployment_reason = "Python testing"
triggered_by = "rob.smart@pega.com"
triggered_by_name = "Rob Smart"
branch_name = ""
max_execution_time_in_seconds = 1800
skip_aged_updates = True
max_single_task_retries = 3
auto_retry_task_types = [
    orchestrator.DEPLOYMENT_TASK_TYPE_GENERATE_ARTIFACT
]
auto_skip_task_types = [
    orchestrator.DEPLOYMENT_TASK_TYPE_VERIFY_SECURITY_CHECKLIST,
    orchestrator.DEPLOYMENT_TASK_TYPE_CHECK_GUARDRAIL_COMPLIANCE,
]
auto_approve_task_types = [
    orchestrator.DEPLOYMENT_TASK_TYPE_PERFORM_MANUAL_STEP
]
auto_reject_task_types = [
    
]
abort_on_failure = True

## Run an automated deployment
if not orchestrator.automate_deployment(
    pipeline_id,
    deployment_reason,
    triggered_by,
    triggered_by_name,
    branch_name,
    max_execution_time_in_seconds,
    max_single_task_retries,
    skip_aged_updates,
    auto_retry_task_types,
    auto_skip_task_types,
    auto_approve_task_types,
    auto_reject_task_types,
    abort_on_failure,
):
    sys.exit(1)
else:
    sys.exit(0)
