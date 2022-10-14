import os
from datetime import datetime

from bson import json_util
from cloudstorageio import CloudInterface

from pycognaize import Snapshot
from pycognaize.common.enums import EnvConfigEnum

import boto3
import math

start = datetime.now()



os.environ['SNAPSHOT_PATH'] = "s3://innolytiq-elements/snapshots/62a5cc6aaa8df0000037daf6"
# os.environ['SNAPSHOT_ID'] = ""
os.environ['SNAPSHOT_ID'] = "62a5c9f66db6bd00139fea76"

# from pycognaize import Snapshot


snapshot_dir = os.environ[EnvConfigEnum.SNAPSHOT_PATH.value]
snapshot_id = os.environ[EnvConfigEnum.SNAPSHOT_ID.value]
snapshot_path = os.path.join(snapshot_dir, snapshot_id)

read_CI = []
read_boto = []

# for i in range(20):
#     CI = CloudInterface()
#
#     start = datetime.now()
#     for i in range(10):
#         with CI.open(snapshot_path, 'r') as f:
#             # doc_dict = json_util.loads(f.read())
#             pass
#     end = datetime.now()
#     print(end - start)
#     read_CI.append((end - start).total_seconds())
#
#     # These define the bucket and object to read
#     bucketname = 'innolytiq-elements'
#     file_to_read = 'snapshots/62b461f9f8b46100004ba27f/628f70f056aeff0012e772c8/document.json'
#
#     s3client = boto3.client(
#         's3',
#         region_name='us-east-1'
#     )
#     # Create a file object using the bucket and object key.
#     for i in range(10):
#         fileobj = s3client.get_object(
#             Bucket=bucketname,
#             Key=file_to_read
#         )
#         # open the file object and read it into the variable filedata.
#         filedata = fileobj['Body'].read()
#
#         # file data will be a binary stream.  We have to decode it
#         # contents = filedata.decode('utf-8')
#     end = datetime.now()
#
#     print(end - start)
#     read_boto.append((end - start).total_seconds())
#     # Once decoded, you can treat the file as plain text if appropriate
#     # print(contents)
#
# print(read_CI, read_boto, sep='\n')

start_time = datetime.now()
snapshot = Snapshot.download()
end_time = datetime.now()

print(end_time - start_time)
