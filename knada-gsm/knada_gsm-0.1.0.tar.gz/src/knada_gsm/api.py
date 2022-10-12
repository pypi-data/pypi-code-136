import os
from google.cloud import secretmanager

def get_secrets(secret: str=None, version: str="latest") -> dict:
    if not secret:
        secret = os.getenv("KNADA_TEAM_SECRET")

    client = secretmanager.SecretManagerServiceClient()
    secret = client.access_secret_version(name=f"{secret}/versions/{version}")
    return dict([line.split("=") for line in secret.payload.data.decode('UTF-8').splitlines()])

def set_secrets_as_envs(project: str, secret_name: str, version: str) -> None:
    secrets = get_secrets(project=project, secret_name=secret_name, version=version)
    os.environ.update(secrets)
