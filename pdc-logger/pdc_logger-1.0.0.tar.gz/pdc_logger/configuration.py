from contextvars import ContextVar
import os

from pydantic import BaseModel, Field

configuration_context = ContextVar('configuration context', default=None)

def default_log_level():
    mode = os.environ.get('logmode', 'info').upper()
    
    level = {
        "CRITICAL": 50,
        "ERROR": 40,
        "WARNING": 30,
        "INFO": 20,
        "DEBUG": 10,
        "NOTSET": 0,
    }
    
    return level.get(mode, 20)
    
    


class Configuration(BaseModel):
    application_name: str = 'pdc_logger'
    log_level: int = Field(default_factory=default_log_level)
    log_format: str = '[ %(levelname)s ] %(name)s : %(message)s'
    credentials_path = 'credentials.json'


def set_configuration(config: Configuration = None):
    if not config:
        config = Configuration()
        
    configuration_context.set(config)

def get_configuration() -> Configuration:
    
    config = configuration_context.get()
    if not config:
        set_configuration()
        return get_configuration()
    
    return config
    