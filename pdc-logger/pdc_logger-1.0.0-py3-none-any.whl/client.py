from contextvars import ContextVar
import os
import google.cloud.logging

from .configuration import get_configuration

client_context = ContextVar('Context untuk cloud logging', default=None)


def set_client():
    
    config = get_configuration()
    client = google.cloud.logging.Client.from_service_account_json(config.credentials_path)
    client_context.set(client)
    return client


def get_client():
    
    client = client_context.get()
    if not client:
        set_client()
        
        return get_client()
    
    return client




if __name__ == '__main__':
    get_client()