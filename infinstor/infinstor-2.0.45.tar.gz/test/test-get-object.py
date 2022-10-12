import boto3
from infinstor import infin_boto3
import json
import mlflow

bucket='jaganes-testb-4'
fn='version-test/file2.json'

mlflow.start_run()
s3 = boto3.client('s3')
rv = s3.get_object(Bucket=bucket, Key=fn)
print('get_object rv=' + str(rv))
j = json.load(rv['Body'])
print("JSON=" + str(j))
