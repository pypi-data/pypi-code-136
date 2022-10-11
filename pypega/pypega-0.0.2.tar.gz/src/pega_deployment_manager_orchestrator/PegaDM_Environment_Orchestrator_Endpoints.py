## Orchestrator - Pipeline endpoints
API_ENDPOINT_ORCHESTRATOR_GET_PIPELINE = "/api/DeploymentManager/v1/pipelines/{pipelineid}"
API_ENDPOINT_ORCHESTRATOR_GET_PIPELINES = "/api/DeploymentManager/v1/pipelines/{pipelineid}"
API_ENDPOINT_ORCHESTRATOR_ACTIVATE_PIPELINE = "/api/DeploymentManager/v1/pipelines/{pipelineid}/activate"
API_ENDPOINT_ORCHESTRATOR_ARCHIVE_PIPELINE = "/api/DeploymentManager/v1/pipelines/{pipelineid}/archive"
API_ENDPOINT_ORCHESTRATOR_DISABLE_PIPELINE = "/api/DeploymentManager/v1/pipelines/{pipelineid}/disable"
API_ENDPOINT_ORCHESTRATOR_ENABLE_PIPELINE = "/api/DeploymentManager/v1/pipelines/{pipelineid}/enable"
API_ENDPOINT_ORCHESTRATOR_UPDATE_PIPELINE = "/api/DeploymentManager/v1/pipelines/{pipelineid}"
API_ENDPOINT_ORCHESTRATOR_DELETE_PIPELINE = "/api/DeploymentManager/v1/pipelines/{pipelineid}"

## Orchestrator - Deployment endpoints
API_ENDPOINT_ORCHESTRATOR_GET_DEPLOYMENTS = "/api/DeploymentManager/v1/pipelines/{pipelineid}/deployments"
API_ENDPOINT_ORCHESTRATOR_GET_DEPLOYMENTS_LATEST = "/api/DeploymentManager/v1/pipelines/{pipelineid}/deployments?latest=true"
API_ENDPOINT_ORCHESTRATOR_GET_DEPLOYMENTS_PENDING_PROMOTION = "/api/DeploymentManager/v1/pipelines/{pipelineid}/deployments?fetchDeploymentsInPendingPromotion=true"
API_ENDPOINT_ORCHESTRATOR_GET_DEPLOYMENTS_OPEN_AND_PENDING_PROMOTION = "/api/DeploymentManager/v1/pipelines/{pipelineid}/deployments?fetchOpenAndPendingPromotionDeployments=true"
API_ENDPOINT_ORCHESTRATOR_TRIGGER_DEPLOYMENT = "/api/DeploymentManager/v1/pipelines/{pipelineid}/deployments"
API_ENDPOINT_ORCHESTRATOR_ABORT_DEPLOYMENT = "/api/DeploymentManager/v1/deployments/{id}/abort"
API_ENDPOINT_ORCHESTRATOR_PAUSE_DEPLOYMENT = "/api/DeploymentManager/v1/deployments/{id}/pause"
API_ENDPOINT_ORCHESTRATOR_RESUME_DEPLOYMENT = "/api/DeploymentManager/v1/deployments/{id}/resume"
API_ENDPOINT_ORCHESTRATOR_PROMOTE_DEPLOYMENT = "/api/DeploymentManager/v1/deployments/{id}/promote"
API_ENDPOINT_ORCHESTRATOR_RETRY_DEPLOYMENT = "/api/DeploymentManager/v1/deployments/{id}/retry"
API_ENDPOINT_ORCHESTRATOR_SKIP_DEPLOYMENT_TASK = "/api/DeploymentManager/v1/deployments/{id}/skip"
API_ENDPOINT_ORCHESTRATOR_GET_DEPLOYMENT = "/api/DeploymentManager/v1/deployments/{id}"
API_ENDPOINT_ORCHESTRATOR_GET_DEPLOYMENT_TASKS = "/api/DeploymentManager/v1/tasks"
API_ENDPOINT_ORCHESTRATOR_GET_DEPLOYMENT_TASKS_PIPELINE = "/api/DeploymentManager/v1/tasks?PipelineID={pipeline_id}"
API_ENDPOINT_ORCHESTRATOR_GET_DEPLOYMENT_TASKS_DEPLOYMENT = "/api/DeploymentManager/v1/tasks?DeploymentID={deployment_id}"
API_ENDPOINT_ORCHESTRATOR_GET_DEPLOYMENT_TASKS_LATEST = "/api/DeploymentManager/v1/tasks?latest=true"
API_ENDPOINT_ORCHESTRATOR_GET_DEPLOYMENT_TASKS_DEPLOYMENT_STATUS = "/api/DeploymentManager/v1/tasks?DeploymentID={deployment_id}&TaskStatus={task_status}"
API_ENDPOINT_ORCHESTRATOR_GET_DEPLOYMENT_TASK = "/api/DeploymentManager/v1/tasks/{id}"
API_ENDPOINT_ORCHESTRATOR_UPDATE_DEPLOYMENT_TASK = "/api/DeploymentManager/v1/tasks/{id}"
API_ENDPOINT_ORCHESTRATOR_QS_ENVIRONMENT_ID = '&EnvironmentID='
