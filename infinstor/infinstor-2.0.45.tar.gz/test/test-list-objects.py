import boto3
from infinstor import infin_boto3
import json
import mlflow

bucket='jaganes-testb'
prefix='working/mlflow/'

mlflow.start_run()
s3 = boto3.client('s3')

marker = None
while True:
    if marker:
        print('Calling list_objects with marker ' + str(marker), flush=True)
        lrv = s3.list_objects(Bucket=bucket, Prefix=prefix,\
                Delimiter='/', MaxKeys=2, Marker=marker)
    else:
        print('Calling list_objects with no marker', flush=True)
        lrv = s3.list_objects(Bucket=bucket, Prefix=prefix,\
                Delimiter='/', MaxKeys=2)
    print('LIST RV=' + str(lrv))
    if 'NextMarker' in lrv:
        marker = lrv['NextMarker']
    else:
        break
