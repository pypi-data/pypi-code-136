import logging
import json
from datetime import datetime
from acceldata_sdk.initialiser import torch_client_credentials
from acceldata_sdk.models.job import CreateJob, JobMetadata, Node
from acceldata_sdk.models.pipeline import CreatePipeline, PipelineMetadata, PipelineRunResult, PipelineRunStatus
from acceldata_sdk.torch_client import TorchClient
from acceldata_sdk.models.span_context import SpanContext

logging.basicConfig(level=logging.INFO)

# Set up acceldata_sdk_code client
torchClient = TorchClient(url="https://torch.acceldata.local:5443/torch",
                       access_key="P04IM8FNQRUCRTU", secret_key="E6LL9YUPMG4BDTJHT2VZD75HW0B8E5")

# create pipeline object
# pipeline = CreatePipeline(
#     uid='monthly_reporting_airflow_2',
#     name='Monthly reporting Pipeline_airflow_2',
#     description='Pipeline to create monthly reporting tables',
#     meta=PipelineMetadata('vaishvik', 'acceldata_sdk_code', '...'),
#     context={'key1': 'value1'}
# )
# creating pipeline using acceldata_sdk_code client
pipelineResponse = torchClient.get_pipeline(pipeline_identity="torch.airflow.demo.lambda")
print('Newly Created Pipeline Response : ', pipelineResponse)

# create job object
# job = CreateJob(
#     uid='monthly_sales_aggregate-38',
#     name='Monthly Sales Aggregate-38',
#     pipelineSnapshot=pipeline.currentSnapshot,
#     description='Generates the monthly sales aggregate tables for the complete year',
#     inputs=[Dataset('postgres-assembly-5450', 'ad_catalog.ad_catalog.flyway_schema_history')],
#     outputs=[Dataset('postgres-ds', 'ad_catalog.ad_catalog.flyway_schema_history')],
#     meta=JobMetadata('vaishvik', 'backend', 'https://github.com/acme/reporting/reporting.scala'),
#     context={'key21': 'value21'}
# )
# # create a job on newly created pipeline
# jobResponse = pipelineResponse.create_job(job)
# print('Newly Created Job Response : ', jobResponse)

# create a pipeline run of the pipeline
pipelineRunResponse = pipelineResponse.create_pipeline_run()
print('pipeline Run Created :', pipelineRunResponse)

# update a pipeline run of the pipeline
# updatePipelineRunRes = pipelineRunResponse.update_pipeline_run(context_data={'key1': 'value2', 'name': 'backend'},
#                                                                result=PipelineRunResult.SUCCESS,
#                                                                status=PipelineRunStatus.COMPLETED)
# print('pipeline run updated :', updatePipelineRunRes)

# create span in the pipeline run
spanContext = pipelineRunResponse.create_span(uid='span_uid_38')
print('Span Created :', spanContext)
child_span_context = spanContext.create_child_span(
    uid="test.child.span",
    context_data={
        'time': str(datetime.now())
    })
# span_dict = child_span_context.get_dict()
# json = json.dumps(span_dict).encode('UTF-8')
# SpanContext(**span_dict)


# # start span event
# print('Span Start Event Response :', spanContext.start({'k': 'v'}))

# check current span is root or not
# print('span is root or not : ', spanContext.is_root())
#
# # get span
# sc = pipelineRunResponse.get_span(span_uid='span_uid_38')
# print('span con get : ', sc)
#
# sc2 = pipelineRunResponse.get_span(span_uid='span_uid_38')
# print('span con get : ', sc2)
#
# # end the span event
# print('Span End Event Response :', spanContext.end())
#
# # check if the current span has children or not
# print('has child ', spanContext.has_children())

# # create a child span
# childSpanContext = spanContext.create_child_span('span_uid_38_2')
# print('child span is root or not  ', childSpanContext.is_root())
# print('child span abort event : ', childSpanContext.abort())
#
# print('child span has child or not : ', childSpanContext.has_children())
# print('parent span has child or not : ', spanContext.has_children())