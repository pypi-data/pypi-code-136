import os
import pandas as pd
from datetime import datetime


# def reverse(value):
#     if not isinstance(value, str):
#         return None
#     result = ''
#     for i in reversed(range(len(value))):
#         result += value[i]
#     return result

#S3 configiration
s3_bucket = 'nolk-datalake'
s3_base_path = 'source_systems/anvyl/'
s3_path = 's3://' + s3_bucket + '/' + s3_base_path

# Date
def getDate(pattern):
    now = datetime.utcnow()
    date = now.strftime(pattern)
    return date

# Save Log
def save_log(team_id, job_name, job_subject, status, started_at, finished_at, logged_at, log_description):

    date = datetime.today().strftime('%Y%m%d')
    fields = [
        'team_id',
        'snapshot_date',
        'job_name',
        'job_subject',
        'status',
        'started_at',
        'finished_at',
        'logged_at',
        'log_description'
    ]
    df = pd.DataFrame(columns=fields)
    df = df.append({'team_id': team_id,
                    'snapshot_date': date,
                    'job_name': job_name,
                    'job_subject': job_subject,
                    'status': status,
                    'started_at': started_at,
                    'finished_at': finished_at,
                    'logged_at': logged_at,
                    'log_description': log_description,
                    },ignore_index=True)

    pathOut = os.path.join(s3_path,  job_name + '/Logs/')
    if df.empty == False:
        df.to_csv(pathOut + date + '_' + team_id + '_' + job_subject + job_name + '.csv')


# def main():
#     save_log(team_id='826', job_name='Parts', job_subject='GetList', status='success', started_at='', finished_at='', logged_at='', log_description='')
#
# if __name__ == "__main__":
#     main()