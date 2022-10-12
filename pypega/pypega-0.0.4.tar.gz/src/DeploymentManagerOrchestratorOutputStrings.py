## Placeholder
OS_PIPELINE_ARCHIVED = "Pipeline '{pipeline_id}' archived"
OS_UNABLE_TO_ARCHIVE_PIPELINE = "Unable to archive pipeline '{pipeline_id}'"

OS_PIPELINE_ACTIVATED = "Pipeline '{pipeline_id}' activated"
OS_UNABLE_TO_ACTIVATE_PIPELINE = "Unable to activate pipeline '{pipeline_id}'"

OS_PIPELINE_DISABLED = "Pipeline '{pipeline_id}' disabled"
OS_UNABLE_TO_DISABLE_PIPELINE = "Unable to disable pipeline '{pipeline_id}'"

OS_PIPELINE_ENABLED = "Pipeline '{pipeline_id}' enabled"
OS_UNABLE_TO_ENABLE_PIPELINE = "Unable to enable pipeline '{pipeline_id}'"

OS_PIPELINE_DELETED = "Pipeline '{pipeline_id}' deleted"
OS_UNABLE_TO_DELETE_PIPELINE = "Unable to delete pipeline '{pipeline_id}'"

OS_DEPLOYMENT_TRIGGERED = "Deployment '{deployment_id}' triggered for pipeline '{pipeline_id}' and has a status of '{deployment_status}'"

OS_DEPLOYMENT_ABORTED = "Deployment '{deployment_id}' aborted"

OS_DEPLOYMENT_PAUSED = "Deployment '{deployment_id}' paused"
OS_UNABLE_TO_PAUSE_DEPLOYMENT = "Deployment '{deployment_id}' could not be paused"

OS_DEPLOYMENT_RESUMED = "Deployment '{deployment_id}' resumed"
OS_UNABLE_TO_RESUME_DEPLOYMENT = "Deployment '{deployment_id}' could not be resumed"

OS_DEPLOYMENT_RETRIED = "Deployment '{deployment_id}' retried"
OS_UNABLE_TO_RETRY_DEPLOYMENT = "Deployment '{deployment_id}' could not be retried"

OS_DEPLOYMENT_PROMOTED = "Deployment '{deployment_id}' promoted"
OS_UNABLE_TO_PROMOTE_DEPLOYMENT = "Deployment '{deployment_id}' could not be promoted"

OS_DEPLOYMENT_TASK_SKIPPED = "Deployment task for deployment '{deployment_id}' skipped"
OS_UNABLE_TO_SKIP_DEPLOYMENT_TASK = "Could not skip deployment task for deployment '{deployment_id}'"

OS_WAITING_FOR_DEPLOYMENT_STATUS = "Waiting for deployment '{deployment_id}' status to be one of: {status_watch_list}"
OS_WAITING_FOR_DEPLOYMENT_STATUS_FOUND = "Deployment '{deployment_id}' status is '{deployment_status}' succesfully found match list: '{status_watch_list}'"
OS_WAITING_FOR_DEPLOYMENT_STATUS_NOT_FOUND = "Reached maximum wait time and deployment '{deployment_id}' status '{deployment_status}' is still not in match list '{status_watch_list}'"
OS_WAITING_FOR_DEPLOYMENT_STATUS_PAUSING = "Waiting {poll_frequency_in_seconds} seconds as deployment '{deployment_id}' status '{deployment_status}' is not in must-match list '{status_watch_list}'"

OS_NOT_WAITING_FOR_DEPLOYMENT_STATUS = "Waiting until deployment '{deployment_id}' status changes to something other than: '{status_watch_list}'"
OS_NOT_WAITING_FOR_DEPLOYMENT_STATUS_FOUND = "Deployment '{deployment_id}' status is '{deployment_status}' has succesfully change from: '{status_watch_list}'"
OS_NOT_WAITING_FOR_DEPLOYMENT_STATUS_NOT_FOUND = "Reached maximum wait time and deployment '{deployment_id}' status '{deployment_status}' is still one of: '{status_watch_list}'"
OS_NOT_WAITING_FOR_DEPLOYMENT_STATUS_PAUSING = "Waiting {poll_frequency_in_seconds} seconds as deployment '{deployment_id}' status '{deployment_status}' is present in must-not-match list '{status_watch_list}'"

OS_DEPLOYMENT_TASK_UPDATED = "Task '{task_id}' updated"
OS_UNABLE_TO_UPDATE_DEPLOYMENT_TASK = "Task '{task_id}' could not be updated"

OS_WAITING_FOR_DEPLOYMENT_TASK_STATUS = "Waiting for task '{task_id}' status to be present in must-match list '{status_watch_list}'"
OS_WAITING_FOR_DEPLOYMENT_TASK_STATUS_FOUND = "Task '{task_id}' status is '{task_status}' which is in present in must-match list '{status_watch_list}'"
OS_WAITING_FOR_DEPLOYMENT_TASK_STATUS_NOT_FOUND = "Reached maximum wait time and task '{task_id}' status '{task_status}' is not in must-match list '{status_watch_list}'"
OS_WAITING_FOR_DEPLOYMENT_TASK_STATUS_PAUSING = "Waiting {poll_frequency_in_seconds} seconds as task '{task_id}' status '{task_status}' is not in must-match list {status_watch_list}"

OS_NOT_WAITING_FOR_DEPLOYMENT_TASK_STATUS = "Waiting for task '{task_id}' status to not equal: '{status_watch_list}'"
OS_NOT_WAITING_FOR_DEPLOYMENT_TASK_STATUS_FOUND = "Task '{task_id}' status is '{task_status}' does not equal '{status_watch_list}'"
OS_NOT_WAITING_FOR_DEPLOYMENT_TASK_STATUS_NOT_FOUND = "Reached maximum wait time and task '{task_id}' status '{task_status}' is still present in list: '{status_watch_list}'"
OS_NOT_WAITING_FOR_DEPLOYMENT_TASK_STATUS_PAUSING = "Waiting {poll_frequency_in_seconds} seconds as task '{task_id}' status '{task_status}' is still present in must-not-match list '{status_watch_list}'"

OS_AUTO_DEPLOY_TRIGGER_DEPLOYMENT_FAILED = "Unable to trigger deployment for pipeline '{pipeline_id}', deployment failed"
OS_AUTO_DEPLOY_GET_LATEST_DEPLOYMENT_TASK_FAILED = "Unable to retrieve latest task information, deployment failed"
ES_AUTO_DEPLOY_GET_DEPLOYMENT_TASK_FAILED = "Unable to retrieve task information, deployment failed"
OS_AUTO_DEPLOY_WAITING_STATUS_NOT_OPEN_QUEUED = "Deployment '{task_id}; is queued, waiting for a maximum {max_execution_time_in_seconds} seconds  until it's no longer queued"
OS_AUTO_DEPLOY_WAITING_STATUS_NOT_OPEN_READY = "Current task is ready for background processing, will await pipeline status change"
OS_AUTO_DEPLOY_WAITING_STATUS_NOT_OPEN_INPROGRESS = "Current task still in progress, will await pipeline status change"
OS_AUTO_DEPLOY_TASK_STATUS_RESOLVED_COMPLETED = "Current task is completed, will await pipeline status change"
OS_AUTO_DEPLOY_TASK_AUTO_SKIPPED = "Auto-Skipping task '{task_id}' of type '{task_type}' as requested"
OS_AUTO_DEPLOY_UNABLE_TO_AUTO_SKIP_TASK = "Unable to auto-skip task '{task_id}' of type '{task_type} as requested, deployment failed"
OS_AUTO_DEPLOY_TASK_MAX_RETRIES_REACHED = "Task '{task_id}' has been retried the maximum number of {retries} retries, deployment failed"
OS_AUTO_DEPLOY_TASK_AUTO_RETRIED = "Task in pipeline has failed, attempting automatic rety {retry} of {retries}"
OS_AUTO_DEPLOY_UNABLE_TO_AUTO_RETRY_TASK = "Unable to retry task, deployment failed"
OS_AUTO_DEPLOY_UNKNOWN_ERROR_TASK_TYPE = "Deployment task '{task_type}' has not been configured as an auto-skip or auto-retry task type, awaiting manual progression until timeout"
OS_AUTO_DEPLOY_TASK_AUTO_SKIP_AGED_UPDATES = "Auto-Skipping aged updates task '{task_id}' of type '{task_type}' as requested"
OS_AUTO_DEPLOY_UNABLE_TO_AUTO_SKIP_AGED_UPDATES_TASK = "Unable to auto-skip task '{task_id}' of type '{task_type} as requested, deployment failed"
OS_AUTO_DEPLOY_TASK_AUTO_OVERRIDE_UPDATES = "Auto-Overriding aged updates task '{task_id}' of type '{task_type}' as requested"
OS_AUTO_DEPLOY_UNABLE_TO_AUTO_OVERRIDE_AGED_UPDATES_TASK = "Unable to auto-overrides aged updates for '{task_id}' of type '{task_type} as requested, deployment failed"
OS_AUTO_DEPLOY_TASK_AUTO_REJECT = "Auto-Rejecting task '{task_id}' of type '{task_type}' as requested"
OS_AUTO_DEPLOY_UNABLE_TO_AUTO_REJECT_TASK = "Unable to auto-reject task '{task_id}' of type '{task_type} as requested, deployment failed"
OS_AUTO_DEPLOY_TASK_AUTO_APPROVE = "Auto-Approving task '{task_id}' of type '{task_type}' as requested"
OS_AUTO_DEPLOY_UNABLE_TO_AUTO_APPROVE_TASK = "Unable to auto-approve task '{task_id}' of type '{task_type} as requested, deployment failed"
OS_AUTO_DEPLOY_UNKNOWN_INPUT_TASK_TYPE = "Deployment task '{task_type}' has not been configured as an auto-approve or auto-reject task type, awaiting manual progression until timeout"
OS_AUTO_DEPLOY_UNKNOWN_TASK_STATUS = "Unrecognised task status '{task_status}' so unable to proceed, deployment failed"
OS_AUTO_DEPLOY_SUCCESS = "Deployment has been succesfully completed"
OS_AUTO_DEPLOY_RESOLVED_WITH_ERROR = "Deployment has failed with an error"
OS_AUTO_DEPLOY_UNKNOWN_DEPLOYMENT_STATUS = "Unrecognised deployment status {deployment_status}"
OS_AUTO_DEPLOY_MAX_EXECUTION_TIME_EXCEEDED = "Max execution time exceeded and pipeline not resolved, deployment failed"