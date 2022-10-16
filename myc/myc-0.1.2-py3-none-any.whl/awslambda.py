import functools
import inspect
import json

from myc.endpoint import EndpointRegistry
from myc.invoke import invoke_endpoint
from myc.serialization import deserialize

try:
    # import AWS' runtime library
    import awslambdaric
    from awslambdaric.lambda_context import LambdaContext as aws_lambda_context_cls
    have_aws_lambda_runtime = True
except ImportError:
    have_aws_lambda_runtime = False
    aws_lambda_context_cls = None


def invoke_aws_lambda_by_runtime(endpoint_id, fn, event, context):
    if 'body' in event:
        body = json.loads(event['body'])
        args = [deserialize(arg) for arg in body['args']] if 'args' in body else []
    else:
        args = []

    # TODO: support keyword arguments for AWS lambda invocations
    kwargs = {}

    return invoke_endpoint(endpoint_id, fn, True, args, kwargs)


def invoke_aws_lambda_by_user(endpoint_id, fn, args, kwargs):
    return invoke_endpoint(endpoint_id, fn, False, args, kwargs)


def create_aws_lambda_function_wrapper(fn, ep_registry: EndpointRegistry):
    """
    Wraps a function with a wrapper that can be then called by AWS' runtime.
    """

    if not have_aws_lambda_runtime:
        return fn

    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        if len(args) == 2 and isinstance(args[1], aws_lambda_context_cls):
            # called directly by AWS' runtime
            return invoke_aws_lambda_by_runtime(endpoint_id, fn, args[0], args[1])
        else:
            # called by the user
            endpoint_id = ep_registry.get_callable_id(fn)
            return invoke_aws_lambda_by_user(endpoint_id, fn, args, kwargs)

    return wrapper
