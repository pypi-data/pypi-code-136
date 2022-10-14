import os
import boto3

def get_local_env_var(var_group: str, var_name: str) -> str:
    """
    Get environment variable from local environment. Local variables must be of the form: GROUP_NAME_VARIABLE_NAME = VARIABLE_VALUE
    """
    env_var = f'{var_group}_{var_name}'
    return os.environ.get(env_var.lower()) or os.environ.get(env_var.upper())

def get_aws_creds() -> dict:
    '''
    Gets local aws env variables for call to PS
    '''
    return {'region_name' : get_local_env_var('aws', 'region_name'),
            'aws_access_key_id' : get_local_env_var('aws', 'access_key_id'),
            'aws_secret_access_key' : get_local_env_var('aws', 'secret_access_key')}

def get_sys_env_var() -> str:
    '''
    Gets local environment name value
    '''
    return get_local_env_var('environment', 'name')

def get_ps_env_var(var_group: str, var_name: str, local_creds: bool = False, prefix: str = None) -> (str, Exception):
    '''
    Gets environment variable from Parameter Store if that fails, it will try to find locally.

    Can specify if you want to use local AWS credentials or default to role-based credentials.

    Ensure the following environment variable is defined locally: ENVIRONMENT_NAME

    If using local AWS credentials, ensure these evnironment variables are also defined locally: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION_NAME

    Returns tuple of: (environment variable value, Exception object)
    '''
    try:
        client = create_client(local_creds)
        prefix = create_prefix(prefix)
        return (client.get_parameter(Name=f'/{prefix}/{var_group.lower()}/{var_name.lower()}')['Parameter']['Value'], None)
    except Exception as err:
        return (get_local_env_var(var_group, var_name), err)

def set_ps_env_var(var_group: str, var_name: str, var_val: str, local_creds: bool = None, prefix: str = None) -> (bool, Exception):
    '''
    Sets variable value in Parameter Store. Supply variable group, name, and new variable value

    Returns (True, None) for success and (False, Exception) for failure
    '''
    try:
        client = create_client(local_creds)
        prefix = create_prefix(prefix)
        client.put_parameter(Name=f'/{prefix}/{var_group.lower()}/{var_name.lower()}', Value=var_val, Overwrite=True)
        return (True, None)
    except Exception as err:
        return (False, err)

def create_client(local_creds: bool):
    '''
    Creates boto3 SSM client. If credentials are provided, the client will connect with credentials.
    '''
    if local_creds:
        creds = get_aws_creds()
        return boto3.client('ssm',
                            aws_access_key_id=creds['aws_access_key_id'],
                            aws_secret_access_key=creds['aws_secret_access_key'],
                            region_name=creds['region_name'])
    return boto3.client('ssm', region_name=get_local_env_var('AWS', 'REGION'))

def create_prefix(prefix: str) -> str:
    '''
    Creates prefix for parameter store name
    '''
    return prefix.rstrip('/').lstrip('/') or f'{get_sys_env_var().capitalize()}/Tpds/'
