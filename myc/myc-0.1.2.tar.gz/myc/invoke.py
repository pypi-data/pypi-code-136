import os
from typing import Optional

import requests
import dns.resolver

from myc.common import get_current_service
from myc.endpoint import AWSLambdaFunctionEndpoint, Endpoint, PlatformKind
from myc.ledger import LedgerPostEntry, get_ledger
from myc.schema import FunctionSchema, build_default_function_schema
from myc.serialization import serialize, deserialize


class InvokeError(Exception):
    pass


def invoke_endpoint(endpoint_id: str, fn, in_runtime: Optional[bool], args, kwargs):
    """
    Invokes a remote endpoint.
    """
    ledger = get_ledger()
    entry = ledger.get_post().find_entry(endpoint_id)

    if in_runtime:
        # return serialized answer
        return {
            'data': fn(*args, **kwargs)
        }

    if entry.platform_entry.logical_id == get_current_service():
        # this endpoint is hosted on the same service, invoke locally
        return fn(*args, **kwargs)
    else:
        # invoke remote endpoint
        schema = build_default_function_schema(fn)
        return invoke_remote_endpoint(entry, args, kwargs, schema)


async def invoke_endpoint_async(endpoint_id: str, fn, in_runtime: Optional[bool], args, kwargs):
    """
    Invokes a remote endpoint asnychronously.
    """
    ledger = get_ledger()
    entry = ledger.get_post().find_entry(endpoint_id)

    if in_runtime:
        # return serialized answer
        return {
            'data': await fn(*args, **kwargs)
        }

    if entry.platform_entry.logical_id == get_current_service():
        # this endpoint is hosted on the same service, invoke locally
        return await fn(*args, **kwargs)
    else:
        # invoke remote endpoint
        schema = build_default_function_schema(fn)
        return invoke_remote_endpoint(entry, args, kwargs, schema)


def _resolve_ecs_endpoint_url(entry: LedgerPostEntry):
    records = list(dns.resolver.resolve(entry.extra['service'], 'SRV'))
    if len(records) != 1:
        raise NotImplementedError

    host = str(records[0].target).rstrip('.')
    port = records[0].port

    return f'http://{host}:{port}{entry.extra["route"]}'


def invoke_remote_endpoint(entry: LedgerPostEntry, args, kwargs, schema: FunctionSchema):
    """
    Invokes a callable using information given by a ledger entry.
    """
    if entry.protocol == 'http':
        if entry.platform_entry.platform_kind == PlatformKind.AWS_LAMBDA:
            url = entry.extra['function_url']
            return invoke_http_lambda(url, args, kwargs)
        elif entry.platform_entry.platform_kind == PlatformKind.AWS_ECS:
            url = _resolve_ecs_endpoint_url(entry)
            return invoke_http_ecs(url, args, kwargs, schema)
        else:
            raise NotImplementedError

    else:
        raise InvokeError('unsupported protocol')


async def invoke_remote_endpoint_async(entry: LedgerPostEntry, args, kwargs, schema: FunctionSchema):
    """
    Invokes a callable using information given by a ledger entry asynchronously.
    """
    if entry.protocol == 'http':
        if entry.platform_entry.platform_kind == PlatformKind.AWS_LAMBDA:
            url = entry.extra['function_url']
            raise NotImplementedError
            # return invoke_http_lambda(url, args, kwargs)
        elif entry.platform_entry.platform_kind == PlatformKind.AWS_ECS:
            url = _resolve_ecs_endpoint_url(entry)
            return invoke_http_ecs_async(url, args, kwargs, schema)
        else:
            raise NotImplementedError

    else:
        raise InvokeError('unsupported protocol')


def invoke_http_lambda(url: str, args, kwargs):
    assert not kwargs  # TODO: implement keyword arguments
    result = requests.post(url, json={
        'args': [serialize(arg) for arg in args]
    })

    if result.status_code != 200:
        # TODO
        raise InvokeError(f'HTTP request failed with code: {result.status_code}')

    return deserialize(result.json()['data'])


def invoke_http_ecs(url: str, args, kwargs, schema):
    return do_general_http_get(url, args, kwargs, schema)


async def invoke_http_ecs_async(url: str, args, kwargs, schema):
    return await do_general_http_get_async(url, args, kwargs, schema)


def _build_get_params(args, kwargs, schema):
    get_params = {}
    for i, arg in enumerate(args):
        param = schema.get_param_by_index(i)
        if param is None:
            raise InvokeError('Too many positional arguments provided to function')

        get_params[param.name] = arg

    if kwargs:
        raise NotImplementedError

    return get_params


def do_general_http_get(url: str, args, kwargs, schema: FunctionSchema):
    get_params = _build_get_params(args, kwargs, schema)

    result = requests.get(url, params=get_params)
    if result.status_code != 200:
        # TODO
        raise InvokeError(f'HTTP request failed with code: {result.status_code}')

    return deserialize(result.json()['data'])


async def do_general_http_get_async(url: str, args, kwargs, schema: FunctionSchema):
    get_params = _build_get_params(args, kwargs, schema)

    # TODO: turn this into async code
    result = requests.get(url, params=get_params)
    if result.status_code != 200:
        # TODO
        raise InvokeError(f'HTTP request failed with code: {result.status_code}')

    return deserialize(result.json()['data'])
