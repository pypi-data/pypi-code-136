"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)


class RealTimeMonitoringCFMApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_mp_database_endpoint = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [],
                'endpoint_path': '/device/cfm/mp/database',
                'operation_id': 'get_mp_database',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'device_id',
                ],
                'required': [
                    'device_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'device_id',
                ]
            },
            root_map={
                'validations': {
                    ('device_id',): {

                        'regex': {
                            'pattern': r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'device_id':
                        (str,),
                },
                'attribute_map': {
                    'device_id': 'deviceId',
                },
                'location_map': {
                    'device_id': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_mp_local_mep_endpoint = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [],
                'endpoint_path': '/device/cfm/mp/local/mep',
                'operation_id': 'get_mp_local_mep',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'device_id',
                    'domain',
                    'service',
                    'mep_id',
                ],
                'required': [
                    'device_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'device_id',
                ]
            },
            root_map={
                'validations': {
                    ('device_id',): {

                        'regex': {
                            'pattern': r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'device_id':
                        (str,),
                    'domain':
                        (str,),
                    'service':
                        (str,),
                    'mep_id':
                        (float,),
                },
                'attribute_map': {
                    'device_id': 'deviceId',
                    'domain': 'domain',
                    'service': 'service',
                    'mep_id': 'mep-id',
                },
                'location_map': {
                    'device_id': 'query',
                    'domain': 'query',
                    'service': 'query',
                    'mep_id': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_mp_local_mip_endpoint = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [],
                'endpoint_path': '/device/cfm/mp/local/mip',
                'operation_id': 'get_mp_local_mip',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'device_id',
                    'level',
                    'port',
                    'svc_inst',
                ],
                'required': [
                    'device_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'device_id',
                ]
            },
            root_map={
                'validations': {
                    ('device_id',): {

                        'regex': {
                            'pattern': r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'device_id':
                        (str,),
                    'level':
                        (float,),
                    'port':
                        (str,),
                    'svc_inst':
                        (float,),
                },
                'attribute_map': {
                    'device_id': 'deviceId',
                    'level': 'level',
                    'port': 'port',
                    'svc_inst': 'svc-inst',
                },
                'location_map': {
                    'device_id': 'query',
                    'level': 'query',
                    'port': 'query',
                    'svc_inst': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_mp_remote_mep_endpoint = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [],
                'endpoint_path': '/device/cfm/mp/remotemep',
                'operation_id': 'get_mp_remote_mep',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'device_id',
                    'domain',
                    'service',
                    'local_mep_id',
                    'remote_mep_id',
                ],
                'required': [
                    'device_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'device_id',
                ]
            },
            root_map={
                'validations': {
                    ('device_id',): {

                        'regex': {
                            'pattern': r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?).){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'device_id':
                        (str,),
                    'domain':
                        (str,),
                    'service':
                        (str,),
                    'local_mep_id':
                        (float,),
                    'remote_mep_id':
                        (float,),
                },
                'attribute_map': {
                    'device_id': 'deviceId',
                    'domain': 'domain',
                    'service': 'service',
                    'local_mep_id': 'local-mep-id',
                    'remote_mep_id': 'remote-mep-id',
                },
                'location_map': {
                    'device_id': 'query',
                    'domain': 'query',
                    'service': 'query',
                    'local_mep_id': 'query',
                    'remote_mep_id': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def get_mp_database(
        self,
        device_id,
        **kwargs
    ):
        """get_mp_database  # noqa: E501

        Get mp database from device  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_mp_database(device_id, async_req=True)
        >>> result = thread.get()

        Args:
            device_id (str): Device IP

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['device_id'] = \
            device_id
        return self.get_mp_database_endpoint.call_with_http_info(**kwargs)

    def get_mp_local_mep(
        self,
        device_id,
        **kwargs
    ):
        """get_mp_local_mep  # noqa: E501

        Get mp local mep from device  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_mp_local_mep(device_id, async_req=True)
        >>> result = thread.get()

        Args:
            device_id (str): Device IP

        Keyword Args:
            domain (str): Domain Name. [optional]
            service (str): Service Name. [optional]
            mep_id (float): MEP ID. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['device_id'] = \
            device_id
        return self.get_mp_local_mep_endpoint.call_with_http_info(**kwargs)

    def get_mp_local_mip(
        self,
        device_id,
        **kwargs
    ):
        """get_mp_local_mip  # noqa: E501

        Get mp local mip from device  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_mp_local_mip(device_id, async_req=True)
        >>> result = thread.get()

        Args:
            device_id (str): Device IP

        Keyword Args:
            level (float): Level. [optional]
            port (str): Port. [optional]
            svc_inst (float): Service Instance. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['device_id'] = \
            device_id
        return self.get_mp_local_mip_endpoint.call_with_http_info(**kwargs)

    def get_mp_remote_mep(
        self,
        device_id,
        **kwargs
    ):
        """get_mp_remote_mep  # noqa: E501

        Get mp remote mep from device  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_mp_remote_mep(device_id, async_req=True)
        >>> result = thread.get()

        Args:
            device_id (str): Device IP

        Keyword Args:
            domain (str): Domain Name. [optional]
            service (str): Service Name. [optional]
            local_mep_id (float): Local MEP ID. [optional]
            remote_mep_id (float): Remote MEP ID. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['device_id'] = \
            device_id
        return self.get_mp_remote_mep_endpoint.call_with_http_info(**kwargs)

