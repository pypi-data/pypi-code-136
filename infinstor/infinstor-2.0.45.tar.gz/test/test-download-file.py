import boto3
from infinstor import infin_boto3
import json
import mlflow

bucket='jaganes-testb'
file='working/mlflow/examples/docker/kubernetes_config.json'

mlflow.start_run()
s3 = boto3.client('s3')


tf = '/tmp/local.json'
s3.download_file(bucket, file, tf)
f = open(tf)
j = json.load(f)
print("JSON=" + str(j))
