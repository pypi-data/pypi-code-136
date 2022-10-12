'''
# `azurerm_cdn_frontdoor_custom_domain`

Refer to the Terraform Registory for docs: [`azurerm_cdn_frontdoor_custom_domain`](https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain).
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


class CdnFrontdoorCustomDomain(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorCustomDomain.CdnFrontdoorCustomDomain",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain azurerm_cdn_frontdoor_custom_domain}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        cdn_frontdoor_profile_id: builtins.str,
        host_name: builtins.str,
        name: builtins.str,
        tls: typing.Union["CdnFrontdoorCustomDomainTls", typing.Dict[str, typing.Any]],
        associate_with_cdn_frontdoor_route_id: typing.Optional[builtins.str] = None,
        dns_zone_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["CdnFrontdoorCustomDomainTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain azurerm_cdn_frontdoor_custom_domain} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param cdn_frontdoor_profile_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#cdn_frontdoor_profile_id CdnFrontdoorCustomDomain#cdn_frontdoor_profile_id}.
        :param host_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#host_name CdnFrontdoorCustomDomain#host_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#name CdnFrontdoorCustomDomain#name}.
        :param tls: tls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#tls CdnFrontdoorCustomDomain#tls}
        :param associate_with_cdn_frontdoor_route_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#associate_with_cdn_frontdoor_route_id CdnFrontdoorCustomDomain#associate_with_cdn_frontdoor_route_id}.
        :param dns_zone_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#dns_zone_id CdnFrontdoorCustomDomain#dns_zone_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#id CdnFrontdoorCustomDomain#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#timeouts CdnFrontdoorCustomDomain#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorCustomDomain.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CdnFrontdoorCustomDomainConfig(
            cdn_frontdoor_profile_id=cdn_frontdoor_profile_id,
            host_name=host_name,
            name=name,
            tls=tls,
            associate_with_cdn_frontdoor_route_id=associate_with_cdn_frontdoor_route_id,
            dns_zone_id=dns_zone_id,
            id=id,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#create CdnFrontdoorCustomDomain#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#delete CdnFrontdoorCustomDomain#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#read CdnFrontdoorCustomDomain#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#update CdnFrontdoorCustomDomain#update}.
        '''
        value = CdnFrontdoorCustomDomainTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putTls")
    def put_tls(
        self,
        *,
        cdn_frontdoor_secret_id: typing.Optional[builtins.str] = None,
        certificate_type: typing.Optional[builtins.str] = None,
        minimum_tls_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cdn_frontdoor_secret_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#cdn_frontdoor_secret_id CdnFrontdoorCustomDomain#cdn_frontdoor_secret_id}.
        :param certificate_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#certificate_type CdnFrontdoorCustomDomain#certificate_type}.
        :param minimum_tls_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#minimum_tls_version CdnFrontdoorCustomDomain#minimum_tls_version}.
        '''
        value = CdnFrontdoorCustomDomainTls(
            cdn_frontdoor_secret_id=cdn_frontdoor_secret_id,
            certificate_type=certificate_type,
            minimum_tls_version=minimum_tls_version,
        )

        return typing.cast(None, jsii.invoke(self, "putTls", [value]))

    @jsii.member(jsii_name="resetAssociateWithCdnFrontdoorRouteId")
    def reset_associate_with_cdn_frontdoor_route_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAssociateWithCdnFrontdoorRouteId", []))

    @jsii.member(jsii_name="resetDnsZoneId")
    def reset_dns_zone_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnsZoneId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="expirationDate")
    def expiration_date(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expirationDate"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "CdnFrontdoorCustomDomainTimeoutsOutputReference":
        return typing.cast("CdnFrontdoorCustomDomainTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="tls")
    def tls(self) -> "CdnFrontdoorCustomDomainTlsOutputReference":
        return typing.cast("CdnFrontdoorCustomDomainTlsOutputReference", jsii.get(self, "tls"))

    @builtins.property
    @jsii.member(jsii_name="validationToken")
    def validation_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "validationToken"))

    @builtins.property
    @jsii.member(jsii_name="associateWithCdnFrontdoorRouteIdInput")
    def associate_with_cdn_frontdoor_route_id_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "associateWithCdnFrontdoorRouteIdInput"))

    @builtins.property
    @jsii.member(jsii_name="cdnFrontdoorProfileIdInput")
    def cdn_frontdoor_profile_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cdnFrontdoorProfileIdInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsZoneIdInput")
    def dns_zone_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dnsZoneIdInput"))

    @builtins.property
    @jsii.member(jsii_name="hostNameInput")
    def host_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["CdnFrontdoorCustomDomainTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["CdnFrontdoorCustomDomainTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="tlsInput")
    def tls_input(self) -> typing.Optional["CdnFrontdoorCustomDomainTls"]:
        return typing.cast(typing.Optional["CdnFrontdoorCustomDomainTls"], jsii.get(self, "tlsInput"))

    @builtins.property
    @jsii.member(jsii_name="associateWithCdnFrontdoorRouteId")
    def associate_with_cdn_frontdoor_route_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "associateWithCdnFrontdoorRouteId"))

    @associate_with_cdn_frontdoor_route_id.setter
    def associate_with_cdn_frontdoor_route_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorCustomDomain, "associate_with_cdn_frontdoor_route_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "associateWithCdnFrontdoorRouteId", value)

    @builtins.property
    @jsii.member(jsii_name="cdnFrontdoorProfileId")
    def cdn_frontdoor_profile_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cdnFrontdoorProfileId"))

    @cdn_frontdoor_profile_id.setter
    def cdn_frontdoor_profile_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorCustomDomain, "cdn_frontdoor_profile_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdnFrontdoorProfileId", value)

    @builtins.property
    @jsii.member(jsii_name="dnsZoneId")
    def dns_zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dnsZoneId"))

    @dns_zone_id.setter
    def dns_zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorCustomDomain, "dns_zone_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsZoneId", value)

    @builtins.property
    @jsii.member(jsii_name="hostName")
    def host_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostName"))

    @host_name.setter
    def host_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorCustomDomain, "host_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorCustomDomain, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorCustomDomain, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorCustomDomain.CdnFrontdoorCustomDomainConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "cdn_frontdoor_profile_id": "cdnFrontdoorProfileId",
        "host_name": "hostName",
        "name": "name",
        "tls": "tls",
        "associate_with_cdn_frontdoor_route_id": "associateWithCdnFrontdoorRouteId",
        "dns_zone_id": "dnsZoneId",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class CdnFrontdoorCustomDomainConfig(cdktf.TerraformMetaArguments):
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
        cdn_frontdoor_profile_id: builtins.str,
        host_name: builtins.str,
        name: builtins.str,
        tls: typing.Union["CdnFrontdoorCustomDomainTls", typing.Dict[str, typing.Any]],
        associate_with_cdn_frontdoor_route_id: typing.Optional[builtins.str] = None,
        dns_zone_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["CdnFrontdoorCustomDomainTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param cdn_frontdoor_profile_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#cdn_frontdoor_profile_id CdnFrontdoorCustomDomain#cdn_frontdoor_profile_id}.
        :param host_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#host_name CdnFrontdoorCustomDomain#host_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#name CdnFrontdoorCustomDomain#name}.
        :param tls: tls block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#tls CdnFrontdoorCustomDomain#tls}
        :param associate_with_cdn_frontdoor_route_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#associate_with_cdn_frontdoor_route_id CdnFrontdoorCustomDomain#associate_with_cdn_frontdoor_route_id}.
        :param dns_zone_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#dns_zone_id CdnFrontdoorCustomDomain#dns_zone_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#id CdnFrontdoorCustomDomain#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#timeouts CdnFrontdoorCustomDomain#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(tls, dict):
            tls = CdnFrontdoorCustomDomainTls(**tls)
        if isinstance(timeouts, dict):
            timeouts = CdnFrontdoorCustomDomainTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorCustomDomainConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument cdn_frontdoor_profile_id", value=cdn_frontdoor_profile_id, expected_type=type_hints["cdn_frontdoor_profile_id"])
            check_type(argname="argument host_name", value=host_name, expected_type=type_hints["host_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tls", value=tls, expected_type=type_hints["tls"])
            check_type(argname="argument associate_with_cdn_frontdoor_route_id", value=associate_with_cdn_frontdoor_route_id, expected_type=type_hints["associate_with_cdn_frontdoor_route_id"])
            check_type(argname="argument dns_zone_id", value=dns_zone_id, expected_type=type_hints["dns_zone_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "cdn_frontdoor_profile_id": cdn_frontdoor_profile_id,
            "host_name": host_name,
            "name": name,
            "tls": tls,
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
        if associate_with_cdn_frontdoor_route_id is not None:
            self._values["associate_with_cdn_frontdoor_route_id"] = associate_with_cdn_frontdoor_route_id
        if dns_zone_id is not None:
            self._values["dns_zone_id"] = dns_zone_id
        if id is not None:
            self._values["id"] = id
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
    def cdn_frontdoor_profile_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#cdn_frontdoor_profile_id CdnFrontdoorCustomDomain#cdn_frontdoor_profile_id}.'''
        result = self._values.get("cdn_frontdoor_profile_id")
        assert result is not None, "Required property 'cdn_frontdoor_profile_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#host_name CdnFrontdoorCustomDomain#host_name}.'''
        result = self._values.get("host_name")
        assert result is not None, "Required property 'host_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#name CdnFrontdoorCustomDomain#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tls(self) -> "CdnFrontdoorCustomDomainTls":
        '''tls block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#tls CdnFrontdoorCustomDomain#tls}
        '''
        result = self._values.get("tls")
        assert result is not None, "Required property 'tls' is missing"
        return typing.cast("CdnFrontdoorCustomDomainTls", result)

    @builtins.property
    def associate_with_cdn_frontdoor_route_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#associate_with_cdn_frontdoor_route_id CdnFrontdoorCustomDomain#associate_with_cdn_frontdoor_route_id}.'''
        result = self._values.get("associate_with_cdn_frontdoor_route_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dns_zone_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#dns_zone_id CdnFrontdoorCustomDomain#dns_zone_id}.'''
        result = self._values.get("dns_zone_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#id CdnFrontdoorCustomDomain#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["CdnFrontdoorCustomDomainTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#timeouts CdnFrontdoorCustomDomain#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["CdnFrontdoorCustomDomainTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorCustomDomainConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorCustomDomain.CdnFrontdoorCustomDomainTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class CdnFrontdoorCustomDomainTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#create CdnFrontdoorCustomDomain#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#delete CdnFrontdoorCustomDomain#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#read CdnFrontdoorCustomDomain#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#update CdnFrontdoorCustomDomain#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorCustomDomainTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if read is not None:
            self._values["read"] = read
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#create CdnFrontdoorCustomDomain#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#delete CdnFrontdoorCustomDomain#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#read CdnFrontdoorCustomDomain#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#update CdnFrontdoorCustomDomain#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorCustomDomainTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorCustomDomainTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorCustomDomain.CdnFrontdoorCustomDomainTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorCustomDomainTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetRead")
    def reset_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRead", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="readInput")
    def read_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorCustomDomainTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorCustomDomainTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorCustomDomainTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorCustomDomainTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CdnFrontdoorCustomDomainTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CdnFrontdoorCustomDomainTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CdnFrontdoorCustomDomainTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorCustomDomainTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorCustomDomain.CdnFrontdoorCustomDomainTls",
    jsii_struct_bases=[],
    name_mapping={
        "cdn_frontdoor_secret_id": "cdnFrontdoorSecretId",
        "certificate_type": "certificateType",
        "minimum_tls_version": "minimumTlsVersion",
    },
)
class CdnFrontdoorCustomDomainTls:
    def __init__(
        self,
        *,
        cdn_frontdoor_secret_id: typing.Optional[builtins.str] = None,
        certificate_type: typing.Optional[builtins.str] = None,
        minimum_tls_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cdn_frontdoor_secret_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#cdn_frontdoor_secret_id CdnFrontdoorCustomDomain#cdn_frontdoor_secret_id}.
        :param certificate_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#certificate_type CdnFrontdoorCustomDomain#certificate_type}.
        :param minimum_tls_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#minimum_tls_version CdnFrontdoorCustomDomain#minimum_tls_version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CdnFrontdoorCustomDomainTls.__init__)
            check_type(argname="argument cdn_frontdoor_secret_id", value=cdn_frontdoor_secret_id, expected_type=type_hints["cdn_frontdoor_secret_id"])
            check_type(argname="argument certificate_type", value=certificate_type, expected_type=type_hints["certificate_type"])
            check_type(argname="argument minimum_tls_version", value=minimum_tls_version, expected_type=type_hints["minimum_tls_version"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cdn_frontdoor_secret_id is not None:
            self._values["cdn_frontdoor_secret_id"] = cdn_frontdoor_secret_id
        if certificate_type is not None:
            self._values["certificate_type"] = certificate_type
        if minimum_tls_version is not None:
            self._values["minimum_tls_version"] = minimum_tls_version

    @builtins.property
    def cdn_frontdoor_secret_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#cdn_frontdoor_secret_id CdnFrontdoorCustomDomain#cdn_frontdoor_secret_id}.'''
        result = self._values.get("cdn_frontdoor_secret_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#certificate_type CdnFrontdoorCustomDomain#certificate_type}.'''
        result = self._values.get("certificate_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minimum_tls_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/cdn_frontdoor_custom_domain#minimum_tls_version CdnFrontdoorCustomDomain#minimum_tls_version}.'''
        result = self._values.get("minimum_tls_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CdnFrontdoorCustomDomainTls(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CdnFrontdoorCustomDomainTlsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.cdnFrontdoorCustomDomain.CdnFrontdoorCustomDomainTlsOutputReference",
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
            type_hints = typing.get_type_hints(CdnFrontdoorCustomDomainTlsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCdnFrontdoorSecretId")
    def reset_cdn_frontdoor_secret_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCdnFrontdoorSecretId", []))

    @jsii.member(jsii_name="resetCertificateType")
    def reset_certificate_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateType", []))

    @jsii.member(jsii_name="resetMinimumTlsVersion")
    def reset_minimum_tls_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimumTlsVersion", []))

    @builtins.property
    @jsii.member(jsii_name="cdnFrontdoorSecretIdInput")
    def cdn_frontdoor_secret_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cdnFrontdoorSecretIdInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateTypeInput")
    def certificate_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumTlsVersionInput")
    def minimum_tls_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minimumTlsVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="cdnFrontdoorSecretId")
    def cdn_frontdoor_secret_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cdnFrontdoorSecretId"))

    @cdn_frontdoor_secret_id.setter
    def cdn_frontdoor_secret_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorCustomDomainTlsOutputReference, "cdn_frontdoor_secret_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdnFrontdoorSecretId", value)

    @builtins.property
    @jsii.member(jsii_name="certificateType")
    def certificate_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateType"))

    @certificate_type.setter
    def certificate_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorCustomDomainTlsOutputReference, "certificate_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateType", value)

    @builtins.property
    @jsii.member(jsii_name="minimumTlsVersion")
    def minimum_tls_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minimumTlsVersion"))

    @minimum_tls_version.setter
    def minimum_tls_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorCustomDomainTlsOutputReference, "minimum_tls_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumTlsVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CdnFrontdoorCustomDomainTls]:
        return typing.cast(typing.Optional[CdnFrontdoorCustomDomainTls], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CdnFrontdoorCustomDomainTls],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CdnFrontdoorCustomDomainTlsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CdnFrontdoorCustomDomain",
    "CdnFrontdoorCustomDomainConfig",
    "CdnFrontdoorCustomDomainTimeouts",
    "CdnFrontdoorCustomDomainTimeoutsOutputReference",
    "CdnFrontdoorCustomDomainTls",
    "CdnFrontdoorCustomDomainTlsOutputReference",
]

publication.publish()
