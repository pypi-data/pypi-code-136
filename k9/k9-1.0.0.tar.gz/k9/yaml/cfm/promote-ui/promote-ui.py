import subprocess
import os

builds_bucket = 's3://' + os.environ.get('BUILDS_BUCKET')
prd_bucket = 's3://' + os.environ.get('PRD_BUCKET')
sat_bucket = 's3://' + os.environ.get('SAT_BUCKET')
region = os.environ.get('REGION')


def run_command(command):
    print(f'Running: {command}')
    command_list = command.split(' ')
    result = subprocess.run(command_list, stdout=subprocess.PIPE, check=True)
    return result


def handler(event, context):
    print(f'Received event" {event}')
    version = event['Version']
    env = event['TargetEnv']

    is_prd = env == 'prd'

    s3_bucket = prd_bucket if is_prd else sat_bucket
    sub_folder = 'prod' if is_prd else 'test'

    run_command(f'/opt/aws s3 sync {builds_bucket}/{sub_folder}/{version}/ {s3_bucket} --region {region}')
