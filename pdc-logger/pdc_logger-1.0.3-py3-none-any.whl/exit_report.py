from .logger import create_logger

logger = create_logger(__name__, sync_cloud=True, stream=False)

class ExitReport:
    def __enter__(self):
        return self
    
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_traceback:
            logger.error(exc_value, exc_info=(exc_type, exc_value, exc_traceback))
    
    
if __name__ == '__main__':
    
    class TestException(Exception):
        pass
    
    with ExitReport() as report:
        raise TestException("main error")
