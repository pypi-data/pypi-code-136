import os
import logging

from google.cloud.logging.handlers import CloudLoggingHandler

from nisa_di.inject import get_dependency

from .client import get_client
from .configuration import get_configuration


def create_stream_handler():
    config = get_configuration()
    
    formatter = logging.Formatter(config.log_format)
    
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)

    return handler

def create_cloud_handler():
    client = get_client()
    config = get_configuration()
    
    gcloud_logging_handler = CloudLoggingHandler(
        client, name=config.application_name,
        labels=config.labels.dict(exclude_none=True)
    )
    
    return gcloud_logging_handler

def create_logger(name, sync_cloud=False, stream=True) -> logging.Logger:

    config = get_configuration()
    logger = logging.getLogger(name)
    logger.propagate = False
    logger.setLevel(config.log_level)
    
    try:
        if logger.hasHandlers():
            logger.handlers.clear()
    except AttributeError as e:
        pass 

    
    if sync_cloud:
        if os.path.exists(config.credentials_path):
            cloud_handler = get_dependency(create_cloud_handler)
            logger.addHandler(cloud_handler)
            
        else:
            print('credential logger not exist')
    
    if stream:
        sthandler = get_dependency(create_stream_handler)    
        logger.addHandler(sthandler)

    return logger
    
    
    

if __name__ == '__main__':
    import logging
    
    
    l = create_logger(__name__, sync_cloud=True)
    
    
    
    for i in range(0, 10):
        try:
            raise Exception('test log error')
        except Exception as e:
            l.error(f"{e} {i}", exc_info=True)
    
    