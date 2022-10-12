import boto3
#from infinstor import infin_boto3
import json
import mlflow

bucket='jaganes-testb-4'
#prefix='many-files/'
#prefix='single-file/'
prefix='single-dir/'

mlflow.start_run()
s3 = boto3.client('s3')

continuation_token = None
while True:
    if continuation_token:
        print('Calling list_objects with continuation_token ' + str(continuation_token), flush=True)
        lrv = s3.list_objects_v2(Bucket=bucket, Prefix=prefix,\
                Delimiter='/', MaxKeys=2, ContinuationToken=continuation_token)
    else:
        print('Calling list_objects with no continuation_token', flush=True)
        lrv = s3.list_objects_v2(Bucket=bucket, Prefix=prefix,\
                Delimiter='/', MaxKeys=2)
    print('LIST RV=' + str(lrv))
    if 'NextContinuationToken' in lrv:
        continuation_token = lrv['NextContinuationToken']
    else:
        break
