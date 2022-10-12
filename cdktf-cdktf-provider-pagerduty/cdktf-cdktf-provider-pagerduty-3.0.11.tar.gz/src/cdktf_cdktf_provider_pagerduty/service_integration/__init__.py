'''
# `pagerduty_service_integration`

Refer to the Terraform Registory for docs: [`pagerduty_service_integration`](https://www.terraform.io/docs/providers/pagerduty/r/service_integration).
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf
import constructs


class ServiceIntegration(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceIntegration.ServiceIntegration",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration pagerduty_service_integration}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        service: builtins.str,
        email_filter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceIntegrationEmailFilter", typing.Dict[str, typing.Any]]]]] = None,
        email_filter_mode: typing.Optional[builtins.str] = None,
        email_incident_creation: typing.Optional[builtins.str] = None,
        email_parser: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceIntegrationEmailParser", typing.Dict[str, typing.Any]]]]] = None,
        email_parsing_fallback: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        integration_email: typing.Optional[builtins.str] = None,
        integration_key: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        vendor: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration pagerduty_service_integration} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param service: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#service ServiceIntegration#service}.
        :param email_filter: email_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#email_filter ServiceIntegration#email_filter}
        :param email_filter_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#email_filter_mode ServiceIntegration#email_filter_mode}.
        :param email_incident_creation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#email_incident_creation ServiceIntegration#email_incident_creation}.
        :param email_parser: email_parser block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#email_parser ServiceIntegration#email_parser}
        :param email_parsing_fallback: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#email_parsing_fallback ServiceIntegration#email_parsing_fallback}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#id ServiceIntegration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param integration_email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#integration_email ServiceIntegration#integration_email}.
        :param integration_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#integration_key ServiceIntegration#integration_key}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#name ServiceIntegration#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#type ServiceIntegration#type}.
        :param vendor: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#vendor ServiceIntegration#vendor}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceIntegration.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ServiceIntegrationConfig(
            service=service,
            email_filter=email_filter,
            email_filter_mode=email_filter_mode,
            email_incident_creation=email_incident_creation,
            email_parser=email_parser,
            email_parsing_fallback=email_parsing_fallback,
            id=id,
            integration_email=integration_email,
            integration_key=integration_key,
            name=name,
            type=type,
            vendor=vendor,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putEmailFilter")
    def put_email_filter(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceIntegrationEmailFilter", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceIntegration.put_email_filter)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEmailFilter", [value]))

    @jsii.member(jsii_name="putEmailParser")
    def put_email_parser(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceIntegrationEmailParser", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceIntegration.put_email_parser)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEmailParser", [value]))

    @jsii.member(jsii_name="resetEmailFilter")
    def reset_email_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailFilter", []))

    @jsii.member(jsii_name="resetEmailFilterMode")
    def reset_email_filter_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailFilterMode", []))

    @jsii.member(jsii_name="resetEmailIncidentCreation")
    def reset_email_incident_creation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailIncidentCreation", []))

    @jsii.member(jsii_name="resetEmailParser")
    def reset_email_parser(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailParser", []))

    @jsii.member(jsii_name="resetEmailParsingFallback")
    def reset_email_parsing_fallback(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailParsingFallback", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIntegrationEmail")
    def reset_integration_email(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIntegrationEmail", []))

    @jsii.member(jsii_name="resetIntegrationKey")
    def reset_integration_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIntegrationKey", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetVendor")
    def reset_vendor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVendor", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="emailFilter")
    def email_filter(self) -> "ServiceIntegrationEmailFilterList":
        return typing.cast("ServiceIntegrationEmailFilterList", jsii.get(self, "emailFilter"))

    @builtins.property
    @jsii.member(jsii_name="emailParser")
    def email_parser(self) -> "ServiceIntegrationEmailParserList":
        return typing.cast("ServiceIntegrationEmailParserList", jsii.get(self, "emailParser"))

    @builtins.property
    @jsii.member(jsii_name="htmlUrl")
    def html_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "htmlUrl"))

    @builtins.property
    @jsii.member(jsii_name="emailFilterInput")
    def email_filter_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceIntegrationEmailFilter"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceIntegrationEmailFilter"]]], jsii.get(self, "emailFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="emailFilterModeInput")
    def email_filter_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailFilterModeInput"))

    @builtins.property
    @jsii.member(jsii_name="emailIncidentCreationInput")
    def email_incident_creation_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailIncidentCreationInput"))

    @builtins.property
    @jsii.member(jsii_name="emailParserInput")
    def email_parser_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceIntegrationEmailParser"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceIntegrationEmailParser"]]], jsii.get(self, "emailParserInput"))

    @builtins.property
    @jsii.member(jsii_name="emailParsingFallbackInput")
    def email_parsing_fallback_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailParsingFallbackInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="integrationEmailInput")
    def integration_email_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "integrationEmailInput"))

    @builtins.property
    @jsii.member(jsii_name="integrationKeyInput")
    def integration_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "integrationKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="vendorInput")
    def vendor_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vendorInput"))

    @builtins.property
    @jsii.member(jsii_name="emailFilterMode")
    def email_filter_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emailFilterMode"))

    @email_filter_mode.setter
    def email_filter_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegration, "email_filter_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailFilterMode", value)

    @builtins.property
    @jsii.member(jsii_name="emailIncidentCreation")
    def email_incident_creation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emailIncidentCreation"))

    @email_incident_creation.setter
    def email_incident_creation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegration, "email_incident_creation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailIncidentCreation", value)

    @builtins.property
    @jsii.member(jsii_name="emailParsingFallback")
    def email_parsing_fallback(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emailParsingFallback"))

    @email_parsing_fallback.setter
    def email_parsing_fallback(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegration, "email_parsing_fallback").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailParsingFallback", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegration, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="integrationEmail")
    def integration_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "integrationEmail"))

    @integration_email.setter
    def integration_email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegration, "integration_email").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "integrationEmail", value)

    @builtins.property
    @jsii.member(jsii_name="integrationKey")
    def integration_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "integrationKey"))

    @integration_key.setter
    def integration_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegration, "integration_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "integrationKey", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegration, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "service"))

    @service.setter
    def service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegration, "service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegration, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="vendor")
    def vendor(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vendor"))

    @vendor.setter
    def vendor(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegration, "vendor").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vendor", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.serviceIntegration.ServiceIntegrationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "service": "service",
        "email_filter": "emailFilter",
        "email_filter_mode": "emailFilterMode",
        "email_incident_creation": "emailIncidentCreation",
        "email_parser": "emailParser",
        "email_parsing_fallback": "emailParsingFallback",
        "id": "id",
        "integration_email": "integrationEmail",
        "integration_key": "integrationKey",
        "name": "name",
        "type": "type",
        "vendor": "vendor",
    },
)
class ServiceIntegrationConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
        service: builtins.str,
        email_filter: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceIntegrationEmailFilter", typing.Dict[str, typing.Any]]]]] = None,
        email_filter_mode: typing.Optional[builtins.str] = None,
        email_incident_creation: typing.Optional[builtins.str] = None,
        email_parser: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceIntegrationEmailParser", typing.Dict[str, typing.Any]]]]] = None,
        email_parsing_fallback: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        integration_email: typing.Optional[builtins.str] = None,
        integration_key: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        vendor: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param service: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#service ServiceIntegration#service}.
        :param email_filter: email_filter block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#email_filter ServiceIntegration#email_filter}
        :param email_filter_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#email_filter_mode ServiceIntegration#email_filter_mode}.
        :param email_incident_creation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#email_incident_creation ServiceIntegration#email_incident_creation}.
        :param email_parser: email_parser block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#email_parser ServiceIntegration#email_parser}
        :param email_parsing_fallback: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#email_parsing_fallback ServiceIntegration#email_parsing_fallback}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#id ServiceIntegration#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param integration_email: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#integration_email ServiceIntegration#integration_email}.
        :param integration_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#integration_key ServiceIntegration#integration_key}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#name ServiceIntegration#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#type ServiceIntegration#type}.
        :param vendor: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#vendor ServiceIntegration#vendor}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(ServiceIntegrationConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument email_filter", value=email_filter, expected_type=type_hints["email_filter"])
            check_type(argname="argument email_filter_mode", value=email_filter_mode, expected_type=type_hints["email_filter_mode"])
            check_type(argname="argument email_incident_creation", value=email_incident_creation, expected_type=type_hints["email_incident_creation"])
            check_type(argname="argument email_parser", value=email_parser, expected_type=type_hints["email_parser"])
            check_type(argname="argument email_parsing_fallback", value=email_parsing_fallback, expected_type=type_hints["email_parsing_fallback"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument integration_email", value=integration_email, expected_type=type_hints["integration_email"])
            check_type(argname="argument integration_key", value=integration_key, expected_type=type_hints["integration_key"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument vendor", value=vendor, expected_type=type_hints["vendor"])
        self._values: typing.Dict[str, typing.Any] = {
            "service": service,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if email_filter is not None:
            self._values["email_filter"] = email_filter
        if email_filter_mode is not None:
            self._values["email_filter_mode"] = email_filter_mode
        if email_incident_creation is not None:
            self._values["email_incident_creation"] = email_incident_creation
        if email_parser is not None:
            self._values["email_parser"] = email_parser
        if email_parsing_fallback is not None:
            self._values["email_parsing_fallback"] = email_parsing_fallback
        if id is not None:
            self._values["id"] = id
        if integration_email is not None:
            self._values["integration_email"] = integration_email
        if integration_key is not None:
            self._values["integration_key"] = integration_key
        if name is not None:
            self._values["name"] = name
        if type is not None:
            self._values["type"] = type
        if vendor is not None:
            self._values["vendor"] = vendor

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]], result)

    @builtins.property
    def service(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#service ServiceIntegration#service}.'''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def email_filter(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceIntegrationEmailFilter"]]]:
        '''email_filter block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#email_filter ServiceIntegration#email_filter}
        '''
        result = self._values.get("email_filter")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceIntegrationEmailFilter"]]], result)

    @builtins.property
    def email_filter_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#email_filter_mode ServiceIntegration#email_filter_mode}.'''
        result = self._values.get("email_filter_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def email_incident_creation(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#email_incident_creation ServiceIntegration#email_incident_creation}.'''
        result = self._values.get("email_incident_creation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def email_parser(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceIntegrationEmailParser"]]]:
        '''email_parser block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#email_parser ServiceIntegration#email_parser}
        '''
        result = self._values.get("email_parser")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceIntegrationEmailParser"]]], result)

    @builtins.property
    def email_parsing_fallback(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#email_parsing_fallback ServiceIntegration#email_parsing_fallback}.'''
        result = self._values.get("email_parsing_fallback")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#id ServiceIntegration#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def integration_email(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#integration_email ServiceIntegration#integration_email}.'''
        result = self._values.get("integration_email")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def integration_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#integration_key ServiceIntegration#integration_key}.'''
        result = self._values.get("integration_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#name ServiceIntegration#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#type ServiceIntegration#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vendor(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#vendor ServiceIntegration#vendor}.'''
        result = self._values.get("vendor")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceIntegrationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.serviceIntegration.ServiceIntegrationEmailFilter",
    jsii_struct_bases=[],
    name_mapping={
        "body_mode": "bodyMode",
        "body_regex": "bodyRegex",
        "from_email_mode": "fromEmailMode",
        "from_email_regex": "fromEmailRegex",
        "subject_mode": "subjectMode",
        "subject_regex": "subjectRegex",
    },
)
class ServiceIntegrationEmailFilter:
    def __init__(
        self,
        *,
        body_mode: typing.Optional[builtins.str] = None,
        body_regex: typing.Optional[builtins.str] = None,
        from_email_mode: typing.Optional[builtins.str] = None,
        from_email_regex: typing.Optional[builtins.str] = None,
        subject_mode: typing.Optional[builtins.str] = None,
        subject_regex: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param body_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#body_mode ServiceIntegration#body_mode}.
        :param body_regex: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#body_regex ServiceIntegration#body_regex}.
        :param from_email_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#from_email_mode ServiceIntegration#from_email_mode}.
        :param from_email_regex: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#from_email_regex ServiceIntegration#from_email_regex}.
        :param subject_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#subject_mode ServiceIntegration#subject_mode}.
        :param subject_regex: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#subject_regex ServiceIntegration#subject_regex}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceIntegrationEmailFilter.__init__)
            check_type(argname="argument body_mode", value=body_mode, expected_type=type_hints["body_mode"])
            check_type(argname="argument body_regex", value=body_regex, expected_type=type_hints["body_regex"])
            check_type(argname="argument from_email_mode", value=from_email_mode, expected_type=type_hints["from_email_mode"])
            check_type(argname="argument from_email_regex", value=from_email_regex, expected_type=type_hints["from_email_regex"])
            check_type(argname="argument subject_mode", value=subject_mode, expected_type=type_hints["subject_mode"])
            check_type(argname="argument subject_regex", value=subject_regex, expected_type=type_hints["subject_regex"])
        self._values: typing.Dict[str, typing.Any] = {}
        if body_mode is not None:
            self._values["body_mode"] = body_mode
        if body_regex is not None:
            self._values["body_regex"] = body_regex
        if from_email_mode is not None:
            self._values["from_email_mode"] = from_email_mode
        if from_email_regex is not None:
            self._values["from_email_regex"] = from_email_regex
        if subject_mode is not None:
            self._values["subject_mode"] = subject_mode
        if subject_regex is not None:
            self._values["subject_regex"] = subject_regex

    @builtins.property
    def body_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#body_mode ServiceIntegration#body_mode}.'''
        result = self._values.get("body_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def body_regex(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#body_regex ServiceIntegration#body_regex}.'''
        result = self._values.get("body_regex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def from_email_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#from_email_mode ServiceIntegration#from_email_mode}.'''
        result = self._values.get("from_email_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def from_email_regex(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#from_email_regex ServiceIntegration#from_email_regex}.'''
        result = self._values.get("from_email_regex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subject_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#subject_mode ServiceIntegration#subject_mode}.'''
        result = self._values.get("subject_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subject_regex(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#subject_regex ServiceIntegration#subject_regex}.'''
        result = self._values.get("subject_regex")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceIntegrationEmailFilter(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceIntegrationEmailFilterList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceIntegration.ServiceIntegrationEmailFilterList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceIntegrationEmailFilterList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ServiceIntegrationEmailFilterOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceIntegrationEmailFilterList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceIntegrationEmailFilterOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailFilterList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailFilterList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailFilterList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceIntegrationEmailFilter]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceIntegrationEmailFilter]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceIntegrationEmailFilter]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailFilterList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceIntegrationEmailFilterOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceIntegration.ServiceIntegrationEmailFilterOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceIntegrationEmailFilterOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetBodyMode")
    def reset_body_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBodyMode", []))

    @jsii.member(jsii_name="resetBodyRegex")
    def reset_body_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBodyRegex", []))

    @jsii.member(jsii_name="resetFromEmailMode")
    def reset_from_email_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFromEmailMode", []))

    @jsii.member(jsii_name="resetFromEmailRegex")
    def reset_from_email_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFromEmailRegex", []))

    @jsii.member(jsii_name="resetSubjectMode")
    def reset_subject_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubjectMode", []))

    @jsii.member(jsii_name="resetSubjectRegex")
    def reset_subject_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubjectRegex", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="bodyModeInput")
    def body_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bodyModeInput"))

    @builtins.property
    @jsii.member(jsii_name="bodyRegexInput")
    def body_regex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bodyRegexInput"))

    @builtins.property
    @jsii.member(jsii_name="fromEmailModeInput")
    def from_email_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fromEmailModeInput"))

    @builtins.property
    @jsii.member(jsii_name="fromEmailRegexInput")
    def from_email_regex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fromEmailRegexInput"))

    @builtins.property
    @jsii.member(jsii_name="subjectModeInput")
    def subject_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subjectModeInput"))

    @builtins.property
    @jsii.member(jsii_name="subjectRegexInput")
    def subject_regex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subjectRegexInput"))

    @builtins.property
    @jsii.member(jsii_name="bodyMode")
    def body_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bodyMode"))

    @body_mode.setter
    def body_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailFilterOutputReference, "body_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bodyMode", value)

    @builtins.property
    @jsii.member(jsii_name="bodyRegex")
    def body_regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bodyRegex"))

    @body_regex.setter
    def body_regex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailFilterOutputReference, "body_regex").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bodyRegex", value)

    @builtins.property
    @jsii.member(jsii_name="fromEmailMode")
    def from_email_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fromEmailMode"))

    @from_email_mode.setter
    def from_email_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailFilterOutputReference, "from_email_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fromEmailMode", value)

    @builtins.property
    @jsii.member(jsii_name="fromEmailRegex")
    def from_email_regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fromEmailRegex"))

    @from_email_regex.setter
    def from_email_regex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailFilterOutputReference, "from_email_regex").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fromEmailRegex", value)

    @builtins.property
    @jsii.member(jsii_name="subjectMode")
    def subject_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subjectMode"))

    @subject_mode.setter
    def subject_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailFilterOutputReference, "subject_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subjectMode", value)

    @builtins.property
    @jsii.member(jsii_name="subjectRegex")
    def subject_regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subjectRegex"))

    @subject_regex.setter
    def subject_regex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailFilterOutputReference, "subject_regex").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subjectRegex", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceIntegrationEmailFilter, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceIntegrationEmailFilter, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceIntegrationEmailFilter, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailFilterOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.serviceIntegration.ServiceIntegrationEmailParser",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "match_predicate": "matchPredicate",
        "value_extractor": "valueExtractor",
    },
)
class ServiceIntegrationEmailParser:
    def __init__(
        self,
        *,
        action: builtins.str,
        match_predicate: typing.Union["ServiceIntegrationEmailParserMatchPredicate", typing.Dict[str, typing.Any]],
        value_extractor: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceIntegrationEmailParserValueExtractor", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param action: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#action ServiceIntegration#action}.
        :param match_predicate: match_predicate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#match_predicate ServiceIntegration#match_predicate}
        :param value_extractor: value_extractor block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#value_extractor ServiceIntegration#value_extractor}
        '''
        if isinstance(match_predicate, dict):
            match_predicate = ServiceIntegrationEmailParserMatchPredicate(**match_predicate)
        if __debug__:
            type_hints = typing.get_type_hints(ServiceIntegrationEmailParser.__init__)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument match_predicate", value=match_predicate, expected_type=type_hints["match_predicate"])
            check_type(argname="argument value_extractor", value=value_extractor, expected_type=type_hints["value_extractor"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "match_predicate": match_predicate,
        }
        if value_extractor is not None:
            self._values["value_extractor"] = value_extractor

    @builtins.property
    def action(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#action ServiceIntegration#action}.'''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def match_predicate(self) -> "ServiceIntegrationEmailParserMatchPredicate":
        '''match_predicate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#match_predicate ServiceIntegration#match_predicate}
        '''
        result = self._values.get("match_predicate")
        assert result is not None, "Required property 'match_predicate' is missing"
        return typing.cast("ServiceIntegrationEmailParserMatchPredicate", result)

    @builtins.property
    def value_extractor(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceIntegrationEmailParserValueExtractor"]]]:
        '''value_extractor block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#value_extractor ServiceIntegration#value_extractor}
        '''
        result = self._values.get("value_extractor")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceIntegrationEmailParserValueExtractor"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceIntegrationEmailParser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceIntegrationEmailParserList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceIntegration.ServiceIntegrationEmailParserList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceIntegrationEmailParserList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ServiceIntegrationEmailParserOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceIntegrationEmailParserList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceIntegrationEmailParserOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceIntegrationEmailParser]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceIntegrationEmailParser]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceIntegrationEmailParser]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.serviceIntegration.ServiceIntegrationEmailParserMatchPredicate",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "predicate": "predicate"},
)
class ServiceIntegrationEmailParserMatchPredicate:
    def __init__(
        self,
        *,
        type: builtins.str,
        predicate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceIntegrationEmailParserMatchPredicatePredicate", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#type ServiceIntegration#type}.
        :param predicate: predicate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#predicate ServiceIntegration#predicate}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceIntegrationEmailParserMatchPredicate.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument predicate", value=predicate, expected_type=type_hints["predicate"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if predicate is not None:
            self._values["predicate"] = predicate

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#type ServiceIntegration#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def predicate(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceIntegrationEmailParserMatchPredicatePredicate"]]]:
        '''predicate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#predicate ServiceIntegration#predicate}
        '''
        result = self._values.get("predicate")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceIntegrationEmailParserMatchPredicatePredicate"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceIntegrationEmailParserMatchPredicate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceIntegrationEmailParserMatchPredicateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceIntegration.ServiceIntegrationEmailParserMatchPredicateOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceIntegrationEmailParserMatchPredicateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putPredicate")
    def put_predicate(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceIntegrationEmailParserMatchPredicatePredicate", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceIntegrationEmailParserMatchPredicateOutputReference.put_predicate)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPredicate", [value]))

    @jsii.member(jsii_name="resetPredicate")
    def reset_predicate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPredicate", []))

    @builtins.property
    @jsii.member(jsii_name="predicate")
    def predicate(self) -> "ServiceIntegrationEmailParserMatchPredicatePredicateList":
        return typing.cast("ServiceIntegrationEmailParserMatchPredicatePredicateList", jsii.get(self, "predicate"))

    @builtins.property
    @jsii.member(jsii_name="predicateInput")
    def predicate_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceIntegrationEmailParserMatchPredicatePredicate"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceIntegrationEmailParserMatchPredicatePredicate"]]], jsii.get(self, "predicateInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserMatchPredicateOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[ServiceIntegrationEmailParserMatchPredicate]:
        return typing.cast(typing.Optional[ServiceIntegrationEmailParserMatchPredicate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ServiceIntegrationEmailParserMatchPredicate],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserMatchPredicateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.serviceIntegration.ServiceIntegrationEmailParserMatchPredicatePredicate",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "matcher": "matcher",
        "part": "part",
        "predicate": "predicate",
    },
)
class ServiceIntegrationEmailParserMatchPredicatePredicate:
    def __init__(
        self,
        *,
        type: builtins.str,
        matcher: typing.Optional[builtins.str] = None,
        part: typing.Optional[builtins.str] = None,
        predicate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceIntegrationEmailParserMatchPredicatePredicatePredicate", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#type ServiceIntegration#type}.
        :param matcher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#matcher ServiceIntegration#matcher}.
        :param part: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#part ServiceIntegration#part}.
        :param predicate: predicate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#predicate ServiceIntegration#predicate}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceIntegrationEmailParserMatchPredicatePredicate.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument matcher", value=matcher, expected_type=type_hints["matcher"])
            check_type(argname="argument part", value=part, expected_type=type_hints["part"])
            check_type(argname="argument predicate", value=predicate, expected_type=type_hints["predicate"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if matcher is not None:
            self._values["matcher"] = matcher
        if part is not None:
            self._values["part"] = part
        if predicate is not None:
            self._values["predicate"] = predicate

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#type ServiceIntegration#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def matcher(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#matcher ServiceIntegration#matcher}.'''
        result = self._values.get("matcher")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def part(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#part ServiceIntegration#part}.'''
        result = self._values.get("part")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def predicate(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceIntegrationEmailParserMatchPredicatePredicatePredicate"]]]:
        '''predicate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#predicate ServiceIntegration#predicate}
        '''
        result = self._values.get("predicate")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceIntegrationEmailParserMatchPredicatePredicatePredicate"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceIntegrationEmailParserMatchPredicatePredicate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceIntegrationEmailParserMatchPredicatePredicateList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceIntegration.ServiceIntegrationEmailParserMatchPredicatePredicateList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceIntegrationEmailParserMatchPredicatePredicateList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceIntegrationEmailParserMatchPredicatePredicateOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceIntegrationEmailParserMatchPredicatePredicateList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceIntegrationEmailParserMatchPredicatePredicateOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserMatchPredicatePredicateList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserMatchPredicatePredicateList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserMatchPredicatePredicateList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceIntegrationEmailParserMatchPredicatePredicate]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceIntegrationEmailParserMatchPredicatePredicate]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceIntegrationEmailParserMatchPredicatePredicate]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserMatchPredicatePredicateList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceIntegrationEmailParserMatchPredicatePredicateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceIntegration.ServiceIntegrationEmailParserMatchPredicatePredicateOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceIntegrationEmailParserMatchPredicatePredicateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putPredicate")
    def put_predicate(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceIntegrationEmailParserMatchPredicatePredicatePredicate", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceIntegrationEmailParserMatchPredicatePredicateOutputReference.put_predicate)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPredicate", [value]))

    @jsii.member(jsii_name="resetMatcher")
    def reset_matcher(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatcher", []))

    @jsii.member(jsii_name="resetPart")
    def reset_part(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPart", []))

    @jsii.member(jsii_name="resetPredicate")
    def reset_predicate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPredicate", []))

    @builtins.property
    @jsii.member(jsii_name="predicate")
    def predicate(
        self,
    ) -> "ServiceIntegrationEmailParserMatchPredicatePredicatePredicateList":
        return typing.cast("ServiceIntegrationEmailParserMatchPredicatePredicatePredicateList", jsii.get(self, "predicate"))

    @builtins.property
    @jsii.member(jsii_name="matcherInput")
    def matcher_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "matcherInput"))

    @builtins.property
    @jsii.member(jsii_name="partInput")
    def part_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "partInput"))

    @builtins.property
    @jsii.member(jsii_name="predicateInput")
    def predicate_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceIntegrationEmailParserMatchPredicatePredicatePredicate"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceIntegrationEmailParserMatchPredicatePredicatePredicate"]]], jsii.get(self, "predicateInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="matcher")
    def matcher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matcher"))

    @matcher.setter
    def matcher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserMatchPredicatePredicateOutputReference, "matcher").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matcher", value)

    @builtins.property
    @jsii.member(jsii_name="part")
    def part(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "part"))

    @part.setter
    def part(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserMatchPredicatePredicateOutputReference, "part").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "part", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserMatchPredicatePredicateOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceIntegrationEmailParserMatchPredicatePredicate, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceIntegrationEmailParserMatchPredicatePredicate, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceIntegrationEmailParserMatchPredicatePredicate, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserMatchPredicatePredicateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.serviceIntegration.ServiceIntegrationEmailParserMatchPredicatePredicatePredicate",
    jsii_struct_bases=[],
    name_mapping={"matcher": "matcher", "part": "part", "type": "type"},
)
class ServiceIntegrationEmailParserMatchPredicatePredicatePredicate:
    def __init__(
        self,
        *,
        matcher: builtins.str,
        part: builtins.str,
        type: builtins.str,
    ) -> None:
        '''
        :param matcher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#matcher ServiceIntegration#matcher}.
        :param part: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#part ServiceIntegration#part}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#type ServiceIntegration#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceIntegrationEmailParserMatchPredicatePredicatePredicate.__init__)
            check_type(argname="argument matcher", value=matcher, expected_type=type_hints["matcher"])
            check_type(argname="argument part", value=part, expected_type=type_hints["part"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "matcher": matcher,
            "part": part,
            "type": type,
        }

    @builtins.property
    def matcher(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#matcher ServiceIntegration#matcher}.'''
        result = self._values.get("matcher")
        assert result is not None, "Required property 'matcher' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def part(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#part ServiceIntegration#part}.'''
        result = self._values.get("part")
        assert result is not None, "Required property 'part' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#type ServiceIntegration#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceIntegrationEmailParserMatchPredicatePredicatePredicate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceIntegrationEmailParserMatchPredicatePredicatePredicateList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceIntegration.ServiceIntegrationEmailParserMatchPredicatePredicatePredicateList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceIntegrationEmailParserMatchPredicatePredicatePredicateList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceIntegrationEmailParserMatchPredicatePredicatePredicateOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceIntegrationEmailParserMatchPredicatePredicatePredicateList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceIntegrationEmailParserMatchPredicatePredicatePredicateOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserMatchPredicatePredicatePredicateList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserMatchPredicatePredicatePredicateList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserMatchPredicatePredicatePredicateList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceIntegrationEmailParserMatchPredicatePredicatePredicate]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceIntegrationEmailParserMatchPredicatePredicatePredicate]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceIntegrationEmailParserMatchPredicatePredicatePredicate]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserMatchPredicatePredicatePredicateList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceIntegrationEmailParserMatchPredicatePredicatePredicateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceIntegration.ServiceIntegrationEmailParserMatchPredicatePredicatePredicateOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceIntegrationEmailParserMatchPredicatePredicatePredicateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="matcherInput")
    def matcher_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "matcherInput"))

    @builtins.property
    @jsii.member(jsii_name="partInput")
    def part_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "partInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="matcher")
    def matcher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "matcher"))

    @matcher.setter
    def matcher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserMatchPredicatePredicatePredicateOutputReference, "matcher").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matcher", value)

    @builtins.property
    @jsii.member(jsii_name="part")
    def part(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "part"))

    @part.setter
    def part(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserMatchPredicatePredicatePredicateOutputReference, "part").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "part", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserMatchPredicatePredicatePredicateOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceIntegrationEmailParserMatchPredicatePredicatePredicate, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceIntegrationEmailParserMatchPredicatePredicatePredicate, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceIntegrationEmailParserMatchPredicatePredicatePredicate, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserMatchPredicatePredicatePredicateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceIntegrationEmailParserOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceIntegration.ServiceIntegrationEmailParserOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceIntegrationEmailParserOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMatchPredicate")
    def put_match_predicate(
        self,
        *,
        type: builtins.str,
        predicate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ServiceIntegrationEmailParserMatchPredicatePredicate, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#type ServiceIntegration#type}.
        :param predicate: predicate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#predicate ServiceIntegration#predicate}
        '''
        value = ServiceIntegrationEmailParserMatchPredicate(
            type=type, predicate=predicate
        )

        return typing.cast(None, jsii.invoke(self, "putMatchPredicate", [value]))

    @jsii.member(jsii_name="putValueExtractor")
    def put_value_extractor(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ServiceIntegrationEmailParserValueExtractor", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceIntegrationEmailParserOutputReference.put_value_extractor)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putValueExtractor", [value]))

    @jsii.member(jsii_name="resetValueExtractor")
    def reset_value_extractor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValueExtractor", []))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="matchPredicate")
    def match_predicate(
        self,
    ) -> ServiceIntegrationEmailParserMatchPredicateOutputReference:
        return typing.cast(ServiceIntegrationEmailParserMatchPredicateOutputReference, jsii.get(self, "matchPredicate"))

    @builtins.property
    @jsii.member(jsii_name="valueExtractor")
    def value_extractor(self) -> "ServiceIntegrationEmailParserValueExtractorList":
        return typing.cast("ServiceIntegrationEmailParserValueExtractorList", jsii.get(self, "valueExtractor"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="matchPredicateInput")
    def match_predicate_input(
        self,
    ) -> typing.Optional[ServiceIntegrationEmailParserMatchPredicate]:
        return typing.cast(typing.Optional[ServiceIntegrationEmailParserMatchPredicate], jsii.get(self, "matchPredicateInput"))

    @builtins.property
    @jsii.member(jsii_name="valueExtractorInput")
    def value_extractor_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceIntegrationEmailParserValueExtractor"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ServiceIntegrationEmailParserValueExtractor"]]], jsii.get(self, "valueExtractorInput"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserOutputReference, "action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceIntegrationEmailParser, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceIntegrationEmailParser, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceIntegrationEmailParser, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-pagerduty.serviceIntegration.ServiceIntegrationEmailParserValueExtractor",
    jsii_struct_bases=[],
    name_mapping={
        "part": "part",
        "type": "type",
        "value_name": "valueName",
        "ends_before": "endsBefore",
        "regex": "regex",
        "starts_after": "startsAfter",
    },
)
class ServiceIntegrationEmailParserValueExtractor:
    def __init__(
        self,
        *,
        part: builtins.str,
        type: builtins.str,
        value_name: builtins.str,
        ends_before: typing.Optional[builtins.str] = None,
        regex: typing.Optional[builtins.str] = None,
        starts_after: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param part: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#part ServiceIntegration#part}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#type ServiceIntegration#type}.
        :param value_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#value_name ServiceIntegration#value_name}.
        :param ends_before: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#ends_before ServiceIntegration#ends_before}.
        :param regex: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#regex ServiceIntegration#regex}.
        :param starts_after: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#starts_after ServiceIntegration#starts_after}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceIntegrationEmailParserValueExtractor.__init__)
            check_type(argname="argument part", value=part, expected_type=type_hints["part"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value_name", value=value_name, expected_type=type_hints["value_name"])
            check_type(argname="argument ends_before", value=ends_before, expected_type=type_hints["ends_before"])
            check_type(argname="argument regex", value=regex, expected_type=type_hints["regex"])
            check_type(argname="argument starts_after", value=starts_after, expected_type=type_hints["starts_after"])
        self._values: typing.Dict[str, typing.Any] = {
            "part": part,
            "type": type,
            "value_name": value_name,
        }
        if ends_before is not None:
            self._values["ends_before"] = ends_before
        if regex is not None:
            self._values["regex"] = regex
        if starts_after is not None:
            self._values["starts_after"] = starts_after

    @builtins.property
    def part(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#part ServiceIntegration#part}.'''
        result = self._values.get("part")
        assert result is not None, "Required property 'part' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#type ServiceIntegration#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#value_name ServiceIntegration#value_name}.'''
        result = self._values.get("value_name")
        assert result is not None, "Required property 'value_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ends_before(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#ends_before ServiceIntegration#ends_before}.'''
        result = self._values.get("ends_before")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def regex(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#regex ServiceIntegration#regex}.'''
        result = self._values.get("regex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def starts_after(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/pagerduty/r/service_integration#starts_after ServiceIntegration#starts_after}.'''
        result = self._values.get("starts_after")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServiceIntegrationEmailParserValueExtractor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ServiceIntegrationEmailParserValueExtractorList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceIntegration.ServiceIntegrationEmailParserValueExtractorList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceIntegrationEmailParserValueExtractorList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ServiceIntegrationEmailParserValueExtractorOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceIntegrationEmailParserValueExtractorList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ServiceIntegrationEmailParserValueExtractorOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserValueExtractorList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserValueExtractorList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserValueExtractorList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceIntegrationEmailParserValueExtractor]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceIntegrationEmailParserValueExtractor]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ServiceIntegrationEmailParserValueExtractor]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserValueExtractorList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ServiceIntegrationEmailParserValueExtractorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-pagerduty.serviceIntegration.ServiceIntegrationEmailParserValueExtractorOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ServiceIntegrationEmailParserValueExtractorOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEndsBefore")
    def reset_ends_before(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndsBefore", []))

    @jsii.member(jsii_name="resetRegex")
    def reset_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegex", []))

    @jsii.member(jsii_name="resetStartsAfter")
    def reset_starts_after(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartsAfter", []))

    @builtins.property
    @jsii.member(jsii_name="endsBeforeInput")
    def ends_before_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endsBeforeInput"))

    @builtins.property
    @jsii.member(jsii_name="partInput")
    def part_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "partInput"))

    @builtins.property
    @jsii.member(jsii_name="regexInput")
    def regex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regexInput"))

    @builtins.property
    @jsii.member(jsii_name="startsAfterInput")
    def starts_after_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startsAfterInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueNameInput")
    def value_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueNameInput"))

    @builtins.property
    @jsii.member(jsii_name="endsBefore")
    def ends_before(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endsBefore"))

    @ends_before.setter
    def ends_before(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserValueExtractorOutputReference, "ends_before").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endsBefore", value)

    @builtins.property
    @jsii.member(jsii_name="part")
    def part(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "part"))

    @part.setter
    def part(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserValueExtractorOutputReference, "part").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "part", value)

    @builtins.property
    @jsii.member(jsii_name="regex")
    def regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regex"))

    @regex.setter
    def regex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserValueExtractorOutputReference, "regex").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regex", value)

    @builtins.property
    @jsii.member(jsii_name="startsAfter")
    def starts_after(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startsAfter"))

    @starts_after.setter
    def starts_after(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserValueExtractorOutputReference, "starts_after").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startsAfter", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserValueExtractorOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="valueName")
    def value_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "valueName"))

    @value_name.setter
    def value_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserValueExtractorOutputReference, "value_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "valueName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ServiceIntegrationEmailParserValueExtractor, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ServiceIntegrationEmailParserValueExtractor, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ServiceIntegrationEmailParserValueExtractor, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ServiceIntegrationEmailParserValueExtractorOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ServiceIntegration",
    "ServiceIntegrationConfig",
    "ServiceIntegrationEmailFilter",
    "ServiceIntegrationEmailFilterList",
    "ServiceIntegrationEmailFilterOutputReference",
    "ServiceIntegrationEmailParser",
    "ServiceIntegrationEmailParserList",
    "ServiceIntegrationEmailParserMatchPredicate",
    "ServiceIntegrationEmailParserMatchPredicateOutputReference",
    "ServiceIntegrationEmailParserMatchPredicatePredicate",
    "ServiceIntegrationEmailParserMatchPredicatePredicateList",
    "ServiceIntegrationEmailParserMatchPredicatePredicateOutputReference",
    "ServiceIntegrationEmailParserMatchPredicatePredicatePredicate",
    "ServiceIntegrationEmailParserMatchPredicatePredicatePredicateList",
    "ServiceIntegrationEmailParserMatchPredicatePredicatePredicateOutputReference",
    "ServiceIntegrationEmailParserOutputReference",
    "ServiceIntegrationEmailParserValueExtractor",
    "ServiceIntegrationEmailParserValueExtractorList",
    "ServiceIntegrationEmailParserValueExtractorOutputReference",
]

publication.publish()
