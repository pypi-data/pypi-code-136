"""
    Delphix DCT API

    Delphix DCT API  # noqa: E501

    The version of the OpenAPI document: 2.2.0
    Contact: support@delphix.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from delphix.api.gateway.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from delphix.api.gateway.exceptions import ApiAttributeError



class Domain(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('username_pattern',): {
            'max_length': 4000,
            'min_length': 1,
        },
        ('search_base',): {
            'max_length': 4000,
            'min_length': 1,
        },
        ('group_attr',): {
            'max_length': 4000,
            'min_length': 1,
        },
        ('email_attr',): {
            'max_length': 4000,
            'min_length': 1,
        },
        ('first_name_attr',): {
            'max_length': 4000,
            'min_length': 1,
        },
        ('last_name_attr',): {
            'max_length': 4000,
            'min_length': 1,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'msad_domain_name': (str,),  # noqa: E501
            'username_pattern': (str,),  # noqa: E501
            'search_base': (str,),  # noqa: E501
            'group_attr': (str,),  # noqa: E501
            'email_attr': (str,),  # noqa: E501
            'first_name_attr': (str,),  # noqa: E501
            'last_name_attr': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'msad_domain_name': 'msad_domain_name',  # noqa: E501
        'username_pattern': 'username_pattern',  # noqa: E501
        'search_base': 'search_base',  # noqa: E501
        'group_attr': 'group_attr',  # noqa: E501
        'email_attr': 'email_attr',  # noqa: E501
        'first_name_attr': 'first_name_attr',  # noqa: E501
        'last_name_attr': 'last_name_attr',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Domain - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            msad_domain_name (str): This is used to get full DN for authentication and lookup. Provide this value only if server is microsoft AD.. [optional]  # noqa: E501
            username_pattern (str): The username_patterns can be used to avoid providing full-dn during login. This will also be used for lookup of groups,email, first name and last name. For non microsoft AD servers a full pattern can be provided,and search_base attribute can be left empty.. [optional] if omitted the server will use the default value of "cn={0},cn=users"  # noqa: E501
            search_base (str): Search base used to search for ldap user groups. Leave this field empty if a full username_pattern is provided and server is non microsoft AD.. [optional]  # noqa: E501
            group_attr (str): Group mapped attribute on ldap side used for user group search.. [optional] if omitted the server will use the default value of "memberOf"  # noqa: E501
            email_attr (str): Email mapped attribute on ldap side used for mapping on DCT side account.. [optional] if omitted the server will use the default value of "userPrincipalName"  # noqa: E501
            first_name_attr (str): First name attribute mapped on ldap side used for mapping on DCT side account.. [optional] if omitted the server will use the default value of "ln"  # noqa: E501
            last_name_attr (str): Last name attribute mapped on ldap side used for mapping on DCT side account.. [optional] if omitted the server will use the default value of "sn"  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Domain - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            msad_domain_name (str): This is used to get full DN for authentication and lookup. Provide this value only if server is microsoft AD.. [optional]  # noqa: E501
            username_pattern (str): The username_patterns can be used to avoid providing full-dn during login. This will also be used for lookup of groups,email, first name and last name. For non microsoft AD servers a full pattern can be provided,and search_base attribute can be left empty.. [optional] if omitted the server will use the default value of "cn={0},cn=users"  # noqa: E501
            search_base (str): Search base used to search for ldap user groups. Leave this field empty if a full username_pattern is provided and server is non microsoft AD.. [optional]  # noqa: E501
            group_attr (str): Group mapped attribute on ldap side used for user group search.. [optional] if omitted the server will use the default value of "memberOf"  # noqa: E501
            email_attr (str): Email mapped attribute on ldap side used for mapping on DCT side account.. [optional] if omitted the server will use the default value of "userPrincipalName"  # noqa: E501
            first_name_attr (str): First name attribute mapped on ldap side used for mapping on DCT side account.. [optional] if omitted the server will use the default value of "ln"  # noqa: E501
            last_name_attr (str): Last name attribute mapped on ldap side used for mapping on DCT side account.. [optional] if omitted the server will use the default value of "sn"  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
