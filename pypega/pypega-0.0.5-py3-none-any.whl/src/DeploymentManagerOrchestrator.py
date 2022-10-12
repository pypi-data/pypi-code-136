import PegaEnvironment
import time
import datetime
import time
import json
from datetime import datetime
from datetime import timedelta

## Standard Orchestrator class
class Orchestrator(PegaEnvironment.PegaEnvironment):
    import DeploymentManagerOrchestratorEndpoints as ENDPOINTS
    import DeploymentManagerOrchestratorOutputStrings as OUTPUTSTRINGS

    ## PDM Orchestrator Constants - Deployment Statuses
    DEPLOYMENT_STATUS_OPEN_QUEUED = "Open-Queued"
    DEPLOYMENT_STATUS_OPEN_ERROR = "Open-Error"
    DEPLOYMENT_STATUS_OPEN_INPROGRESS = "Open-InProgress"
    DEPLOYMENT_STATUS_RESOLVED_COMPLETED = "Resolved-Completed"
    DEPLOYMENT_STATUS_RESOLVED_ERROR = "Resolved-Error"

    ## PDM Orchestrator Constants - Deployment Task Types
    DEPLOYMENT_TASK_TYPE_DEPLOY_APPLICATION = "DeployApplication"
    DEPLOYMENT_TASK_TYPE_PERFORM_MANUAL_STEP = "PerformManualStep"
    DEPLOYMENT_TASK_TYPE_CHECK_GUARDRAIL_COMPLIANCE = "CheckGuardrailCompliance"
    DEPLOYMENT_TASK_TYPE_VERIFY_SECURITY_CHECKLIST = "VerifySecurityChecklist"
    DEPLOYMENT_TASK_TYPE_GENERATE_ARTIFACT = "GenerateArtifact"

    ## PDM Orchestrator Constants - Deployment Task Statuses
    DEPLOYMENT_TASK_STATUS_OPEN_READY = "Open-Ready"
    DEPLOYMENT_TASK_STATUS_OPEN_INPROGRESS = "Open-Inprogress"
    DEPLOYMENT_TASK_STATUS_OPEN_RESOLVED_COMPLETED = "Resolved-Completed"
    DEPLOYMENT_TASK_STATUS_RESOLVED_REJECTED = "Resolved-Rejected"
    DEPLOYMENT_TASK_STATUS_PENDING_INPUT = "Pending-Input"
    DEPLOYMENT_TASK_STATUS_RESOLVED_COMPLETED = "Resolved-Completed"

    ## PDM Orchestrator Constants - Deployment JSON elementds
    DEPLOYMENT_JSON_ELEMENT_DATA = "data"
    DEPLOYMENT_JSON_ELEMENT_DEPLOYMENTID = "deploymentID"
    DEPLOYMENT_JSON_ELEMENT_STATUS = "status"

    ## PDM Orchestrator Constants - Deployment Task JSON elements
    DEPLOYMENT_TASK_JSON_ELEMENT_DATA = "data"
    DEPLOYMENT_TASK_JSON_ELEMENT_TASKID = "taskID"
    DEPLOYMENT_TASK_JSON_ELEMENT_TASKSTATUS = "taskInfo"
    DEPLOYMENT_TASK_JSON_ELEMENT_TASKSTATUS = "taskStatus"
    DEPLOYMENT_TASK_JSON_ELEMENT_TASKINFO = "taskInfo"
    DEPLOYMENT_TASK_JSON_ELEMENT_TASKINFO_TASKTYPE = "taskType"
    DEPLOYMENT_TASK_JSON_ELEMENT_TASKINFO_TASKLABEL = "taskLabel"

    ## PDM Orchestrator Constants - Reasons pased to APIs for auto deploy actions
    AUTO_DEPLOY_SKIP_REASON = "Script configured to auto-skip tasks of type '{task_type}'"
    AUTO_DEPLOY_RETRY_REASON = "Script configured to auto-retry tasks of type '{task_type}'"
    AUTO_DEPLOY_SKIP_AGED_UPDATOS_REASON = "Script configured to auto-skip aged updates"
    AUTO_DEPLOY_OVERRIDE_AGED_UPDATOS_REASON = "Script configured to auto-override aged updates"
    AUTO_DEPLOY_REJECT_REASON = "Script configured to auto-reject tasks of type '{task_type}'"
    AUTO_DEPLOY_APPROVE_REASON = "Script configured to auto-approve tasks of type '{task_type}'"
    AUTO_DEPLOY_ABORT_REASON = "Script configured to auto-abort when encountering fatal error"

    def __init__(self, system_name:str, environment_url:str):
        PegaEnvironment.PegaEnvironment.__init__(self, system_name, environment_url)

    def get_pipelines(self):
        response = self.api_request_get(self.ENDPOINTS.API_ENDPOINT_ORCHESTRATOR_GET_PIPELINES)
        if response.ok:
            return json.loads(response.content)
        else:
            return None

    def get_pipeline(self, pipeline_id:str):
        response = self.api_request_get(self.ENDPOINTS.API_ENDPOINT_ORCHESTRATOR_GET_PIPELINE.format(pipelineid=pipeline_id))
        if response.ok:
            return json.loads(response.content)
        else:
            return None

    def archive_pipeline(self, pipeline_id:str):
        response = self.api_request_put(self.ENDPOINTS.API_ENDPOINT_ORCHESTRATOR_ARCHIVE_PIPELINE.format(pipelineid=pipeline_id), "")
        if response.ok:
            self.print(self.OUTPUTSTRINGS.OS_PIPELINE_ARCHIVED.format(pipeline_id=pipeline_id))
            return True
        else:
            self.print(self.OUTPUTSTRINGS.OS_UNABLE_TO_ARCHIVE_PIPELINE.format(pipeline_id=pipeline_id))
            return False

    def activate_pipeline(self, pipeline_id:str):
        response = self.api_request_put(self.ENDPOINTS.API_ENDPOINT_ORCHESTRATOR_ACTIVATE_PIPELINE.format(pipelineid=pipeline_id), "")
        if response.ok:
            self.print(self.OUTPUTSTRINGS.OS_PIPELINE_ACTIVATED.format(pipeline_id=pipeline_id))
            return True
        else:
            self.print(self.OUTPUTSTRINGS.OS_UNABLE_TO_ACTIVATE_PIPELINE.format(pipeline_id=pipeline_id))
            return False

    def disable_pipeline(self, pipeline_id:str):
        response = self.api_request_put(self.ENDPOINTS.API_ENDPOINT_ORCHESTRATOR_ARCHIVE_PIPELINE.format(pipelineid=pipeline_id), "")
        if response.ok:
            self.print(self.OUTPUTSTRINGS.OS_PIPELINE_DISABLED.format(pipeline_id=pipeline_id))
            return True
        else:
            self.print(self.OUTPUTSTRINGS.OS_UNABLE_TO_DISABLE_PIPELINE.format(pipeline_id=pipeline_id))
            return False

    def enable_pipeline(self, pipeline_id:str):
        response = self.api_request_put(self.ENDPOINTS.API_ENDPOINT_ORCHESTRATOR_ACTIVATE_PIPELINE.format(pipelineid=pipeline_id), "")
        if response.ok:
            self.print(self.OUTPUTSTRINGS.OS_PIPELINE_ENABLED.format(pipeline_id=pipeline_id))
            return True
        else:
            self.print(self.OUTPUTSTRINGS.OS_UNABLE_TO_ENABLE_PIPELINE.format(pipeline_id=pipeline_id))
            return False

    def delete_pipeline(self, pipeline_id:str):
        response = self.api_request_delete(self.ENDPOINTS.API_ENDPOINT_ORCHESTRATOR_DELETE_PIPELINE.format(pipelineid=pipeline_id))
        if response.ok:
            self.print(self.OUTPUTSTRINGS.OS_PIPELINE_DELETED.format(pipeline_id=pipeline_id))
            return True
        else:
            self.print(self.OUTPUTSTRINGS.OS_UNABLE_TO_DELETE_PIPELINE.format(pipeline_id=pipeline_id))
            return False

    def get_deployments(self, pipeline_id:str):
        response = self.api_request_get(self.ENDPOINTS.API_ENDPOINT_ORCHESTRATOR_GET_DEPLOYMENTS.format(pipelineid=pipeline_id))
        if response.ok:
            return json.loads(response.content)
        else:
            return None

    def get_open_and_pending_promotion_deployments(self, pipeline_id:str):
        response = self.api_request_get((self.ENDPOINTS.API_ENDPOINT_ORCHESTRATOR_GET_DEPLOYMENTS_OPEN_AND_PENDING_PROMOTION).format(pipelineid=pipeline_id))
        if response.ok:
            return json.loads(response.content)
        else:
            return None

    def has_open_and_pending_promotion_deployments(self, pipeline_id:str):
        response = self.get_open_and_pending_promotion_deployments(pipeline_id)
        if response != None:
            return (len(response[self.DEPLOYMENT_JSON_ELEMENT_DATA]) > 0)
        else:
            return False

    def get_pending_promotion_deployments(self, pipeline_id:str):
        response = self.api_request_get((self.ENDPOINTS.API_ENDPOINT_ORCHESTRATOR_GET_DEPLOYMENTS_PENDING_PROMOTION).format(pipelineid=pipeline_id))
        if response.ok:
            return json.loads(response.content)
        else:
            return None

    def has_pending_promotion_deployments(self, pipeline_id:str):
        response = self.get_pending_promotion_deployments(pipeline_id)
        if response != None:
            return (len(response[self.DEPLOYMENT_JSON_ELEMENT_DATA]) > 0)
        else:
            return False
            
    def get_deployment(self, deployment_id:str):
        response = self.api_request_get(self.ENDPOINTS.API_ENDPOINT_ORCHESTRATOR_GET_DEPLOYMENT.format(id=deployment_id))
        if response.ok:
            return json.loads(response.content)
        else:
            return None

    def get_deployment_status(self, deployment_id:str):
        deployment = self.get_deployment(deployment_id)
        if deployment != None:
            return deployment[self.DEPLOYMENT_JSON_ELEMENT_STATUS ]
        else:
            return ""

    def get_latest_deployment(self, pipeline_id:str):
        response = self.api_request_get(self.ENDPOINTS.API_ENDPOINT_ORCHESTRATOR_GET_DEPLOYMENTS_LATEST.format(pipelineid=pipeline_id))
        if response.ok:
            return json.loads(response.content)[self.DEPLOYMENT_JSON_ELEMENT_DATA][0]
        else:
            return None

    def get_latest_deployment_id(self, pipeline_id:str):
        deployment = self.get_latest_deployment(pipeline_id)
        if deployment != "":
            return deployment[self.DEPLOYMENT_JSON_ELEMENT_DEPLOYMENTID]
        else:
            return ""

    def get_latest_deployment_status(self, pipeline_id:str):
        deployment = self.get_latest_deployment(pipeline_id)
        if deployment != "":
            return deployment[self.DEPLOYMENT_JSON_ELEMENT_STATUS]
        else:
            return ""

    def trigger_deployment(self, pipeline_id:str, description:str, triggered_by:str, triggered_by_operator_name:str, branch_name:str=""):
        data = {
            "description": description,
            "triggeredBy": triggered_by,
            "triggeredByOperatorName": triggered_by_operator_name,
            "branchName": branch_name
        }

        response = self.api_request_post(self.ENDPOINTS.API_ENDPOINT_ORCHESTRATOR_TRIGGER_DEPLOYMENT.format(pipelineid=pipeline_id), json.dumps(data))
        if response.ok:
            deployment = json.loads(response.content)
            deployment_id = deployment[self.DEPLOYMENT_JSON_ELEMENT_DEPLOYMENTID]
            self.print(self.OUTPUTSTRINGS.OS_DEPLOYMENT_TRIGGERED.format(pipeline_id=pipeline_id, deployment_id=deployment_id, deployment_status=deployment[self.DEPLOYMENT_JSON_ELEMENT_STATUS]))
            return deployment_id
        else:
            return ""

    def abort_deployment(self, deployment_id:str, reason_for_abort:str):
        data = {
            "reasonForAbort": reason_for_abort
        }
        response = self.api_request_put(self.ENDPOINTS.API_ENDPOINT_ORCHESTRATOR_ABORT_DEPLOYMENT.format(id=deployment_id), json.dumps(data))
        if response.ok:
            self.print(self.OUTPUTSTRINGS.OS_DEPLOYMENT_ABORTED.format(deployment_id=deployment_id))
            return True
        else:
            self.raise_exception(self.OUTPUTSTRINGS.OS_DEPLOYMENT_ABORTED.format(deployment_id=deployment_id))
            return False

    def abort_all_deployments_for_pipeline(self, pipeline_id:str, reason_for_abort:str):
        data = {
            "reasonForAbort": reason_for_abort
        }
        deployments = self.get_open_and_pending_promotion_deployments(pipeline_id)
        if deployments is not None:
            for deployment in deployments[self.DEPLOYMENT_JSON_ELEMENT_DATA]:
                self.abort_deployment(deployment[self.DEPLOYMENT_JSON_ELEMENT_DEPLOYMENTID], reason_for_abort)
        else:
            return False

    def pause_deployment(self, deployment_id:str, reason_for_pause:str):
        data = {
            "reasonForPause": reason_for_pause
        }
        response = self.api_request_put(self.ENDPOINTS.API_ENDPOINT_ORCHESTRATOR_PAUSE_DEPLOYMENT.format(id=deployment_id), json.dumps(data))
        if response.ok:
            self.print(self.OUTPUTSTRINGS.OS_DEPLOYMENT_PAUSED.format(deployment_id=deployment_id))
            return True
        else:
            self.raise_exception(self.OUTPUTSTRINGS.OS_UNABLE_TO_PAUSE_DEPLOYMENT.format(deployment_id=deployment_id))
            return False

    def resume_deployment(self, deployment_id:str, reason_for_resume:str):
        data = {
            "reasonForPause": reason_for_resume
        }
        response = self.api_request_put(self.ENDPOINTS.API_ENDPOINT_ORCHESTRATOR_RESUME_DEPLOYMENT.format(id=deployment_id), json.dumps(data))
        if response.ok:
            self.print(self.OUTPUTSTRINGS.OS_DEPLOYMENT_RESUMED.format(deployment_id=deployment_id))
            return True
        else:
            self.print(self.OUTPUTSTRINGS.OS_UNABLE_TO_RESUME_DEPLOYMENT.format(deployment_id=deployment_id)) 

    def retry_deployment(self, deployment_id:str, reason_for_retry:str):
        data = {
            "reasonForRetry": reason_for_retry
        }
        response = self.api_request_put(self.ENDPOINTS.API_ENDPOINT_ORCHESTRATOR_RETRY_DEPLOYMENT.format(id=deployment_id), json.dumps(data))
        if response.ok:
            self.print(self.OUTPUTSTRINGS.OS_DEPLOYMENT_RETRIED.format(deployment_id=deployment_id))
            return True
        else:
            self.print(self.OUTPUTSTRINGS.OS_UNABLE_TO_RETRY_DEPLOYMENT.format(deployment_id=deployment_id)) 

    def promote_deployment(self, deployment_id:str):
        response = self.api_request_put(self.ENDPOINTS.API_ENDPOINT_ORCHESTRATOR_PROMOTE_DEPLOYMENT.format(id=deployment_id))
        if response.ok:
            self.print(self.OUTPUTSTRINGS.OS_DEPLOYMENT_PROMOTED.format(deployment_id=deployment_id))
            return True
        else:
            self.raise_exception(self.OUTPUTSTRINGS.OS_UNABLE_TO_PROMOTE_DEPLOYMENT.format(deployment_id=deployment_id)) 
            return False

    def skip_deployment_task(self, deployment_id:str, reason_for_skip:str):
        data = {
            "reasonForSkip": reason_for_skip
        }
        response = self.api_request_put(self.ENDPOINTS.API_ENDPOINT_ORCHESTRATOR_SKIP_DEPLOYMENT_TASK.format(id=deployment_id), json.dumps(data))
        if response.ok:
            self.print(self.OUTPUTSTRINGS.OS_DEPLOYMENT_TASK_SKIPPED.format(deployment_id=deployment_id))
            return True
        else:
            self.raise_exception(self.OUTPUTSTRINGS.OS_UNABLE_TO_SKIP_DEPLOYMENT_TASK.format(deployment_id=deployment_id))
            return False

    def wait_for_deployment_status(self, deployment_id:str, poll_frequency_in_seconds:int, max_wait_in_seconds:int, status_watch_list:str = []):
        from datetime import timedelta
        start_time = datetime.now()
        self.print(self.OUTPUTSTRINGS.OS_WAITING_FOR_DEPLOYMENT_STATUS.format(deployment_id=deployment_id, status_watch_list=status_watch_list))
 
        while True:
            current_deployment_status = self.get_deployment_status(deployment_id)
            if current_deployment_status in status_watch_list:
                self.print(self.OUTPUTSTRINGS.OS_WAITING_FOR_DEPLOYMENT_STATUS_FOUND.format(deployment_id=deployment_id, deployment_status=current_deployment_status, status_watch_list=status_watch_list))
                return True
            elif datetime.now() > (start_time + timedelta(seconds=max_wait_in_seconds)):
                self.print(self.OUTPUTSTRINGS.OS_WAITING_FOR_DEPLOYMENT_STATUS_NOT_FOUND.format(deployment_id=deployment_id, deployment_status=current_deployment_status, status_watch_list=status_watch_list))
                return False
            else:
                ##self.print(self.OUTPUTSTRINGS.OS_WAITING_FOR_DEPLOYMENT_STATUS_PAUSING.format(poll_frequency_in_seconds=poll_frequency_in_seconds, deployment_id=deployment_id, deployment_status=current_deployment_status, status_watch_list=status_watch_list))
                time.sleep(poll_frequency_in_seconds)
        return False

    def wait_for_deployment_status_not(self, deployment_id:str, poll_frequency_in_seconds:int, max_wait_in_seconds:int, status_watch_list:str = []):
        from datetime import timedelta
        start_time = datetime.now()
        self.print(self.OUTPUTSTRINGS.OS_NOT_WAITING_FOR_DEPLOYMENT_STATUS.format(deployment_id=deployment_id, status_watch_list=status_watch_list))
 
        while True:
            current_deployment_status = self.get_deployment_status(deployment_id)
            if current_deployment_status not in status_watch_list:
                self.print(self.OUTPUTSTRINGS.OS_NOT_WAITING_FOR_DEPLOYMENT_STATUS_FOUND.format(deployment_id=deployment_id, deployment_status=current_deployment_status, status_watch_list=status_watch_list))
                return True
            elif datetime.now() > (start_time + timedelta(seconds=max_wait_in_seconds)):
                self.print(self.OUTPUTSTRINGS.OS_NOT_WAITING_FOR_DEPLOYMENT_STATUS_NOT_FOUND.format(deployment_id=deployment_id, deployment_status=current_deployment_status, status_watch_list=status_watch_list))
                return False
            else:
                ##self.print(self.OUTPUTSTRINGS.OS_NOT_WAITING_FOR_DEPLOYMENT_STATUS_PAUSING.format(poll_frequency_in_seconds=poll_frequency_in_seconds, deployment_id=deployment_id, deployment_status=current_deployment_status, status_watch_list=status_watch_list))
                time.sleep(poll_frequency_in_seconds)
        return False

    def wait_for_deployment_status_change(self, deployment_id:str, poll_frequency_in_seconds:int, max_wait_in_seconds:int):
        current_deployment_status = self.get_deployment_status(deployment_id)
        if current_deployment_status != "":
            return self.wait_for_deployment_status_not(deployment_id, poll_frequency_in_seconds, max_wait_in_seconds, current_deployment_status)
        else:
            return False

    def wait_for_deployment_status_resolved(self, deployment_id:str, poll_frequency_in_seconds:int, max_wait_in_seconds:int):
        status_watch_list = list((self.DEPLOYMENT_STATUS_RESOLVED_COMPLETED, self.DEPLOYMENT_STATUS_RESOLVED_ERROR))
        return self.wait_for_deployment_status(deployment_id, poll_frequency_in_seconds, max_wait_in_seconds, status_watch_list)

    def wait_for_deployment_status_error(self, deployment_id:str, poll_frequency_in_seconds:int, max_wait_in_seconds:int):
        return self.wait_for_deployment_status(self, deployment_id, poll_frequency_in_seconds, max_wait_in_seconds, status_watch_list = [self.DEPLOYMENT_STATUS_OPEN_ERROR])

    def get_pipeline_tasks(self, pipeline_id:str, environment_id:str=""):
        url = self.ENDPOINTS.API_ENDPOINT_ORCHESTRATOR_GET_DEPLOYMENT_TASKS_PIPELINE.format(pipeline_id=pipeline_id)
        if environment_id != "": url += self.ENDPOINTS.API_ENDPOINT_ORCHESTRATOR_QS_ENVIRONMENT_ID + environment_id
        response = self.api_request_get(url)
        if response.ok:
            return json.loads(response.content)
        else:
            return None

    def get_deployment_tasks(self, deployment_id:str, environment_id:str=""):
        url = self.ENDPOINTS.API_ENDPOINT_ORCHESTRATOR_GET_DEPLOYMENT_TASKS_DEPLOYMENT.format(deployment_id=deployment_id)
        if environment_id != "": url += self.ENDPOINTS.API_ENDPOINT_ORCHESTRATOR_QS_ENVIRONMENT_ID + environment_id
        response = self.api_request_get(url)
        if response.ok:
            return json.loads(response.content)
        else:
            return None

    def get_deployment_tasks_ready(self, deployment_id:str, environment_id:str=""):
        url = self.ENDPOINTS.API_ENDPOINT_ORCHESTRATOR_GET_DEPLOYMENT_TASKS_DEPLOYMENT_STATUS.format(deployment_id=deployment_id, task_status=self.DEPLOYMENT_TASK_STATUS_OPEN_READY)
        if environment_id != "": url += self.ENDPOINTS.API_ENDPOINT_ORCHESTRATOR_QS_ENVIRONMENT_ID + environment_id
        response = self.api_request_get(url)
        if response.ok:
            return json.loads(response.content)
        else:
            return None

    def has_deployment_tasks_ready(self, deployment_id:str, environment_id:str=""):
        response = self.get_deployment_tasks_ready(deployment_id, environment_id)
        if response != None:
            return (len(response[self.DEPLOYMENT_TASK_JSON_ELEMENT_DATA]) > 0)
        else:
            return False

    def get_deployment_tasks_pending_input(self, deployment_id:str, environment_id:str=""):
        url = self.ENDPOINTS.API_ENDPOINT_ORCHESTRATOR_GET_DEPLOYMENT_TASKS_DEPLOYMENT_STATUS.format(deployment_id=deployment_id, task_status=self.DEPLOYMENT_TASK_STATUS_PENDING_INPUT)
        if environment_id != "": url += self.ENDPOINTS.API_ENDPOINT_ORCHESTRATOR_QS_ENVIRONMENT_ID + environment_id
        response = self.api_request_get(url)
        if response.ok:
            return json.loads(response.content)
        else:
            return None

    def has_deployment_tasks_pending_input(self, deployment_id:str, environment_id:str=""):
        response = self.get_deployment_tasks_pending_input(deployment_id, environment_id)
        if response != None:
            return (len(response[self.DEPLOYMENT_TASK_JSON_ELEMENT_DATA]) > 0)
        else:
            return False

    def get_deployment_tasks_in_progress(self, deployment_id:str, environment_id:str=""):
        url = self.ENDPOINTS.API_ENDPOINT_ORCHESTRATOR_GET_DEPLOYMENT_TASKS_DEPLOYMENT_STATUS.format(deployment_id=deployment_id, task_status=self.DEPLOYMENT_TASK_STATUS_OPEN_INPROGRESS)
        if environment_id != "": url += self.ENDPOINTS.API_ENDPOINT_ORCHESTRATOR_QS_ENVIRONMENT_ID + environment_id
        response = self.api_request_get(url)        
        if response.ok:
            return json.loads(response.content)
        else:
            return None

    def has_deployment_tasks_in_progress(self, deployment_id:str, environment_id:str=""):
        response = self.get_deployment_tasks_in_progress(deployment_id, environment_id)
        if response != None:
            return (len(response[self.DEPLOYMENT_TASK_JSON_ELEMENT_DATA]) > 0)
        else:
            return False

    def get_deployment_latest_task(self, deployment_id:str, environment_id:str=""):
        url = self.ENDPOINTS.API_ENDPOINT_ORCHESTRATOR_GET_DEPLOYMENT_TASKS_LATEST.format(deployment_id=deployment_id)
        if environment_id != "": url += self.ENDPOINTS.API_ENDPOINT_ORCHESTRATOR_QS_ENVIRONMENT_ID + environment_id
        response = self.api_request_get(url)
        if response.ok:
            return json.loads(response.content)[self.DEPLOYMENT_TASK_JSON_ELEMENT_DATA][0]
        else:
            return None

    def get_deployment_latest_task_status(self, deployment_id:str, environment_id:str=""):
        task = self.get_deployment_latest_task(deployment_id, environment_id="")
        if task != None:
            return task[self.DEPLOYMENT_TASK_JSON_ELEMENT_TASKSTATUS]
        else:
            return ""

    def get_deployment_latest_task_id(self, deployment_id:str, environment_id:str=""):
        task = self.get_deployment_latest_task(deployment_id, environment_id="")
        if task != None:
            return task[self.DEPLOYMENT_TASK_JSON_ELEMENT_TASKID]
        else:
            return ""

    def get_deployment_task(self, task_id:str):
        url = self.ENDPOINTS.API_ENDPOINT_ORCHESTRATOR_GET_DEPLOYMENT_TASK.format(id=task_id)
        response = self.api_request_get(url)
        if response.ok:
            return json.loads(response.content)
        else:
            return None

    def get_deployment_task_id(self, task_id:str):
        task = self.get_deployment_task(task_id)
        if task != None:
            return task[self.DEPLOYMENT_TASK_JSON_ELEMENT_TASKID]
        else:
            return ""

    def get_deployment_task_status(self, task_id:str):
        task = self.get_deployment_task(task_id)
        if task != None:
            return task[self.DEPLOYMENT_TASK_JSON_ELEMENT_TASKSTATUS]
        else:
            return ""

    def get_deployment_task_type(self, task_id:str):
        task = self.get_deployment_task(task_id)
        if task != None:
            return task[self.DEPLOYMENT_TASK_JSON_ELEMENT_TASKINFO][self.DEPLOYMENT_TASK_JSON_ELEMENT_TASKINFO_TASKTYPE]
        else:
            return ""

    def get_deployment_task_label(self, task_id:str):
        task = self.get_deployment_task(task_id)
        if task != None:
            return task[self.DEPLOYMENT_TASK_JSON_ELEMENT_TASKINFO][self.DEPLOYMENT_TASK_JSON_ELEMENT_TASKINFO_TASKLABEL]
        else:
            return ""

    def reject_deployment_task(self, task_id:str, action_note:str):
        data = { 
            "actionNote": action_note, 
            "intermediateInput":"REJECTTASK",
            "isNotificationRequired":"true" ,
            "pxObjClass":"PegaDevOps-Int-Task",
            "taskStatus":"Resolved-Completed" 
        }  
        return self.update_deployment_task(task_id, data)

    def approve_deployment_task(self, task_id:str, action_note:str):
        data = { 
            "actionNote": action_note, 
            "intermediateInput":"APPROVETASK",
            "isNotificationRequired":"true" ,
            "pxObjClass":"PegaDevOps-Int-Task",
            "taskStatus":"Resolved-Completed" 
        }  
        return self.update_deployment_task(task_id, data)

    def override_aged_updatOS_deployment_task(self, task_id:str, action_note:str):
        data = { 
            "actionNote": action_note, 
            "intermediateInput":"OVERRIDEAGEDUPDATES",
            "isNotificationRequired":"true" ,
            "pxObjClass":"PegaDevOps-Int-Task",
            "taskStatus":"Resolved-Completed" 
        }  
        return self.update_deployment_task(task_id, data)

    def skip_aged_updatOS_deployment_task(self, task_id:str, action_note:str):
        data = { 
            "actionNote": action_note, 
            "intermediateInput":"SKIPAGEDUPDATES",
            "isNotificationRequired":"true" ,
            "pxObjClass":"PegaDevOps-Int-Task",
            "taskStatus":"Resolved-Completed" 
        }  
        return self.update_deployment_task(task_id, data)

    def update_deployment_task(self, task_id:str, data:str):
        url = self.ENDPOINTS.API_ENDPOINT_ORCHESTRATOR_GET_DEPLOYMENT_TASK.format(id=task_id)
        response = self.api_request_put(url, json.dumps(data))
        if response.ok:
            self.print(self.OUTPUTSTRINGS.OS_DEPLOYMENT_TASK_UPDATED.format(task_id=task_id))
            return True
        else:
            self.raise_exception(self.OUTPUTSTRINGS.OS_UNABLE_TO_UPDATE_DEPLOYMENT_TASK.format(task_id=task_id))
            return False
    
    def wait_for_deployment_task_status(self, task_id:str, poll_frequency_in_seconds:int, max_wait_in_seconds:int, status_watch_list:str = []):
        from datetime import timedelta
        start_time = datetime.now()
        self.print(self.OUTPUTSTRINGS.OS_WAITING_FOR_DEPLOYMENT_TASK_STATUS.format(task_id=task_id, status_watch_list=status_watch_list))
 
        while True:
            current_task_status = self.get_deployment_task_status(task_id)
            if current_task_status in status_watch_list:
                self.print(self.OUTPUTSTRINGS.OS_WAITING_FOR_DEPLOYMENT_TASK_STATUS_FOUND.format(task_id=task_id, task_status=current_task_status, status_watch_list=status_watch_list))
                return True
            elif datetime.now() > (start_time + timedelta(seconds=max_wait_in_seconds)):
                self.print(self.OUTPUTSTRINGS.OS_WAITING_FOR_DEPLOYMENT_TASK_STATUS_NOT_FOUND.format(task_id=task_id, task_status=current_task_status, status_watch_list=status_watch_list))
                return False
            else:
                ##self.print(self.OUTPUTSTRINGS.OS_WAITING_FOR_DEPLOYMENT_TASK_STATUS_PAUSING.format(poll_frequency_in_seconds=poll_frequency_in_seconds, task_id=task_id, task_status=current_task_status, status_watch_list=status_watch_list))
                time.sleep(poll_frequency_in_seconds)
        return False

    def wait_for_deployment_task_status_not(self, task_id:str, poll_frequency_in_seconds:int, max_wait_in_seconds:int, status_watch_list:str = []):
        from datetime import timedelta
        start_time = datetime.now()
        self.print(self.OUTPUTSTRINGS.OS_NOT_WAITING_FOR_DEPLOYMENT_TASK_STATUS.format(task_id=task_id, status_watch_list=status_watch_list))
 
        while True:
            current_task_status = self.get_deployment_task_status(task_id)
            if current_task_status not in status_watch_list:
                self.print(self.OUTPUTSTRINGS.OS_NOT_WAITING_FOR_DEPLOYMENT_TASK_STATUS_FOUND.format(task_id=task_id, task_status=current_task_status, status_watch_list=status_watch_list))
                return True
            elif datetime.now() > (start_time + timedelta(seconds=max_wait_in_seconds)):
                self.print(self.OUTPUTSTRINGS.OS_NOT_WAITING_FOR_DEPLOYMENT_TASK_STATUS_NOT_FOUND.format(task_id=task_id, task_status=current_task_status, status_watch_list=status_watch_list))
                return False
            else:
                ##self.print(self.OUTPUTSTRINGS.OS_NOT_WAITING_FOR_DEPLOYMENT_TASK_PAUSING.format(poll_frequency_in_seconds=poll_frequency_in_seconds, task_id=task_id, task_status=current_task_status, status_watch_list=status_watch_list))
                time.sleep(poll_frequency_in_seconds)
        return False

    def wait_for_deployment_task_status_change(self, task_id:str, poll_frequency_in_seconds:int, max_wait_in_seconds:int):
        current_task_status = self.get_deployment_task_status(task_id)
        if current_task_status != "":
            return self.wait_for_deployment_task_status_not(task_id, poll_frequency_in_seconds, max_wait_in_seconds, current_task_status)
        else:
            return False

    def automate_deployment(self, pipeline_id:str, deployment_reason:str, triggered_by:str, triggered_by_name:str, branch_name:str = "", max_execution_time_in_seconds:int = 1800, max_single_task_retries:int =3, skip_aged_updates:bool = False, auto_retry_task_types:str = [], auto_skip_task_types:str = [], auto_approve_task_types:str = [], auto_reject_task_types = [], abort_on_failure:bool = False):
        ## Initiate local variables
        start_time = datetime.now()
        task_retry_id = ""
        task_retry_type = ""
        task_retry_counter = 0
        deployment_failed = False

        ## Trigger a new deployment
        deployment_id = deployment_id = self.trigger_deployment(pipeline_id, deployment_reason, triggered_by, triggered_by_name, branch_name)
        if deployment_id == "":
            self.print(self.OUTPUTSTRINGS.OS_AUTO_DEPLOY_TRIGGER_DEPLOYMENT_FAILED.format(pipeline_id=pipeline_id))
            deployment_failed = True

        ## Enter a loop until the status is resolved or we reach a timeout
        while not deployment_failed:    
            ## Get the latest deployment and task id and status
            deployment_status = self.get_deployment_status(deployment_id)
            task = self.get_deployment_latest_task(deployment_id)
            if task is None:
                self.print(self.OUTPUTSTRINGS.OS_AUTO_DEPLOY_GET_LATEST_DEPLOYMENT_TASK_FAILED)
                deployment_failed = True
                break

            ## Retrieve task details
            try:
                task_id = task[self.DEPLOYMENT_TASK_JSON_ELEMENT_TASKID]
                task_status = task[self.DEPLOYMENT_TASK_JSON_ELEMENT_TASKSTATUS]
                task_type = task[self.DEPLOYMENT_TASK_JSON_ELEMENT_TASKINFO][self.DEPLOYMENT_TASK_JSON_ELEMENT_TASKINFO_TASKTYPE]
            except:
                self.raise_exception(self.OUTPUTSTRINGS.OS_AUTO_DEPLOY_GET_DEPLOYMENT_TASK_FAILED)

            ## Handle deployment status of Open-Queued
            if deployment_status == self.DEPLOYMENT_STATUS_OPEN_QUEUED:
                self.print(self.OUTPUTSTRINGS.OS_AUTO_DEPLOY_WAITING_STATUS_NOT_OPEN_QUEUED.format(task_id=task_id, max_execution_time_in_seconds=max_execution_time_in_seconds))
                self.wait_for_deployment_status_change(deployment_id, 5, max_execution_time_in_seconds)

            # Handle deployment status of Open-Error
            elif (deployment_status == self.DEPLOYMENT_STATUS_OPEN_ERROR or deployment_status == self.DEPLOYMENT_STATUS_OPEN_INPROGRESS):
                ## Reset retry counter if task status is not pending-input (still)
                if task_type != task_retry_type:  task_retry_counter = 0
        
                # Handle tasks status of Open-Ready
                if task_status == self.DEPLOYMENT_TASK_STATUS_OPEN_READY:
                    ##self.print(self.OUTPUTSTRINGS.OS_AUTO_DEPLOY_WAITING_STATUS_NOT_OPEN_READY)
                    self.wait_for_deployment_task_status_not(task_id, 5, max_execution_time_in_seconds, self.DEPLOYMENT_TASK_STATUS_OPEN_READY)

                # Handle tasks status of Open-Inprogress
                elif task_status == self.DEPLOYMENT_TASK_STATUS_OPEN_INPROGRESS:
                    ##self.print(self.OUTPUTSTRINGS.OS_AUTO_DEPLOY_WAITING_STATUS_NOT_OPEN_INPROGRESS)            
                    self.wait_for_deployment_task_status_not(task_id, 5, max_execution_time_in_seconds, self.DEPLOYMENT_TASK_STATUS_OPEN_INPROGRESS)

                # Handle tasks status of Resolved-Completed
                elif task_status == self.DEPLOYMENT_TASK_STATUS_RESOLVED_COMPLETED:   
                    self.print(self.OUTPUTSTRINGS.OS_AUTO_DEPLOY_TASK_STATUS_RESOLVED_COMPLETED) 

                # Handle tasks status of Resolved-Rejected
                elif task_status == self.DEPLOYMENT_TASK_STATUS_RESOLVED_REJECTED:            
                    if task_type in auto_skip_task_types:
                         self.print(self.OUTPUTSTRINGS.OS_AUTO_DEPLOY_TASK_AUTO_SKIPPED.format(task_id=task_id, task_type=task_type))
                         if not self.skip_deployment_task(deployment_id, self.AUTO_DEPLOY_SKIP_REASON.format(task_type=task_type)):
                            self.print(self.OUTPUTSTRINGS.OS_AUTO_DEPLOY_UNABLE_TO_AUTO_SKIP_TASK.format(task_id=task_id, task_type=task_type))

                    ## Retry if configured as an auto retry task
                    elif task_type in auto_retry_task_types:
                        if task_retry_counter >= max_single_task_retries:
                            self.print(self.OUTPUTSTRINGS.OS_AUTO_DEPLOY_TASK_MAX_RETRIES_REACHED.format(task_id=task_id, retries=max_single_task_retries)) 
                            deployment_failed = True
                            break      

                        ## Set retry variables
                        task_retry_counter += 1
                        task_retry_id = task_id
                        task_retry_type = task_type
                        self.print(self.OUTPUTSTRINGS.OS_AUTO_DEPLOY_TASK_AUTO_RETRIED.format(task_id=task_id, retry=task_retry_counter, retries=max_single_task_retries))
                        
                        ## Attempt retry, exit if fails
                        if self.retry_deployment(deployment_id, self.AUTO_DEPLOY_RETRY_REASON) == False:
                            self.print(self.OUTPUTSTRINGS.OS_AUTO_DEPLOY_UNABLE_TO_AUTO_RETRY_TASK)
                            deployment_failed = True
                            break

                    ## Handle any other known error task types
                    else:
                        self.print(self.OUTPUTSTRINGS.OS_AUTO_DEPLOY_UNKNOWN_ERROR_TASK_TYPE.format(task_type=task_type))
                        self.wait_for_deployment_status_change(deployment_id, 5, max_execution_time_in_seconds)

                # Handle tasks status of Pending-Input
                elif task_status == self.DEPLOYMENT_TASK_STATUS_PENDING_INPUT:

                    # Handle deploy application task types
                    if task_type == self.DEPLOYMENT_TASK_TYPE_DEPLOY_APPLICATION:
                        if skip_aged_updates:
                            self.print(self.OUTPUTSTRINGS.OS_AUTO_DEPLOY_TASK_AUTO_SKIP_AGED_UPDATES.format(task_id=task_id, task_type=task_type))
                            if not self.skip_aged_updatOS_deployment_task(task_id, self.AUTO_DEPLOY_SKIP_AGED_UPDATOS_REASON):
                                self.print(self.OUTPUTSTRINGS.OS_AUTO_DEPLOY_UNABLE_TO_AUTO_SKIP_AGED_UPDATES_TASK.format(task_id=task_id, task_type=task_type))

                        else:
                            self.print(self.OUTPUTSTRINGS.OS_AUTO_DEPLOY_TASK_AUTO_OVERRIDE_UPDATES.format(task_id=task_id, task_type=task_type))
                            if not self.override_aged_updatOS_deployment_task(task_id, self.AUTO_DEPLOY_OVERRIDE_AGED_UPDATOS_REASON ):
                                self.print(self.OUTPUTSTRINGS.OS_AUTO_DEPLOY_UNABLE_TO_AUTO_OVERRIDE_AGED_UPDATES_TASK.format(task_id=task_id, task_type=task_type))

                    # Handle any other task types
                    else:
                        if task_type in auto_reject_task_types:
                            self.print(self.OUTPUTSTRINGS.OS_AUTO_DEPLOY_TASK_AUTO_REJECT.format(task_id=task_id, task_type=task_type))
                            if not self.reject_deployment_task(task_id, self.AUTO_DEPLOY_REJECT_REASON.format(task_type=task_type)):
                                self.print(self.OUTPUTSTRINGS.OS_AUTO_DEPLOY_UNABLE_TO_AUTO_REJECT_TASK.format(task_id=task_id, task_type=task_type))
                        
                        elif task_type in auto_approve_task_types:
                            self.print(self.OUTPUTSTRINGS.OS_AUTO_DEPLOY_TASK_AUTO_APPROVE.format(task_id=task_id, task_type=task_type))
                            if not self.approve_deployment_task(task_id, self.AUTO_DEPLOY_APPROVE_REASON.format(task_type=task_type)):
                                self.print(self.OUTPUTSTRINGS.OS_AUTO_DEPLOY_UNABLE_TO_AUTO_APPROVE_TASK.format(task_id=task_id, task_type=task_type))
                                    
                        else:
                            self.print(self.OUTPUTSTRINGS.OS_AUTO_DEPLOY_UNKNOWN_INPUT_TASK_TYPE.format(task_type=task_type))
                            self.wait_for_deployment_status_change(deployment_id, 5, max_execution_time_in_seconds)

                # Handle any unrecognised task status
                else:
                    self.print(self.OUTPUTSTRINGS.OS_AUTO_DEPLOY_UNKNOWN_TASK_STATUS.format(task_status=task_status))
                    deployment_failed = True
                    break

            # Handle deployment status of Resolved-Completed
            elif deployment_status == self.DEPLOYMENT_STATUS_RESOLVED_COMPLETED:
                self.print(self.OUTPUTSTRINGS.OS_AUTO_DEPLOY_SUCCESS)
                break

            # Handle deployment status of Resolved-Error
            elif deployment_status == self.DEPLOYMENT_STATUS_RESOLVED_ERROR:
                self.print(self.OUTPUTSTRINGS.OS_AUTO_DEPLOY_RESOLVED_WITH_ERROR)
                deployment_failed = True
                break

            # Handle any unrecognised deployment status
            else:
                self.raise_exception(self.OUTPUTSTRINGS.OS_AUTO_DEPLOY_UNKNOWN_DEPLOYMENT_STATUS.format(deployment_status=deployment_status))
                deployment_failed = True
                break

            ## Abort if we exit loop (as maximum execution time reached)
            if datetime.now() > (start_time + timedelta(seconds=max_execution_time_in_seconds)):
                self.print(self.OUTPUTSTRINGS.OS_AUTO_DEPLOY_MAX_EXECUTION_TIME_EXCEEDED)
                deployment_failed = True
                break

        ## Handle deployment failure
        if deployment_failed:   
            if abort_on_failure:
                self.abort_deployment(deployment_id, self.AUTO_DEPLOY_ABORT_REASON)
        
        return deployment_failed