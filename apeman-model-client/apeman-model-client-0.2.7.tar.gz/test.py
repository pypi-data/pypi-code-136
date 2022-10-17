import os

from apeman.model.openapi import apeman_open_api_client
from apeman.model.openapi.model_instance_task_status import TaskStatus

apeman_meta_grpc_server = os.getenv("apeman_meta_server_addr")
print(apeman_meta_grpc_server)

# report status of the model instance task
# apeman_open_api_client.report(task_id='xxxx', status=TaskStatus.RUNNING, progress=0.1, message='test', token='')
# get endpoint of the model instance
# apeman_open_api_client.get_endpoint(model_instance_id='test')

# apeman_open_api_client.cancel_task(task_id='xxxx', force_delete=True, token='xxxxxxxxx')

res = apeman_open_api_client.get_instance(model_instance_id='xxxxx')
print(res)