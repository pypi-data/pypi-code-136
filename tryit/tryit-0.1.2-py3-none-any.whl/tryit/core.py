import typing
import logging
from functools import wraps

logger = logging.getLogger("tryit")
logger.setLevel(logging.INFO)



class ExceptionTarget(typing.NamedTuple):
    
    exception: typing.Type[Exception]
    callback: typing.Callable[[Exception], typing.Any]


ExceptionTargets = typing.List[ExceptionTarget]



def tryit(exceptions: ExceptionTargets = [], default_callback=None) -> typing.Callable:
    
    registry = {
        item.exception: item.callback
        for item in exceptions
    }

    def inner(fn: typing.Callable)-> typing.Callable:

        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                return_value = fn(*args, **kwargs)
            except Exception as err:
                handler = registry.get(type(err))
                logger.info(f"Caught Exception {err.__class__.__name__}")
               
                if handler:
                    logger.info("Using dedicated handler")
                    return handler(err)

                if default_callback:
                    logger.info("Using default handler")
                    return default_callback(err)
              
                logger.error("Raising unmanaged expection")
                raise err
        
            return return_value

        return wrapper

    return inner
    
            

