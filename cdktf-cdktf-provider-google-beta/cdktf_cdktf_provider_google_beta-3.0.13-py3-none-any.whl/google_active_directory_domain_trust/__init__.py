'''
# `google_active_directory_domain_trust`

Refer to the Terraform Registory for docs: [`google_active_directory_domain_trust`](https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust).
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


class GoogleActiveDirectoryDomainTrust(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleActiveDirectoryDomainTrust.GoogleActiveDirectoryDomainTrust",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust google_active_directory_domain_trust}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        domain: builtins.str,
        target_dns_ip_addresses: typing.Sequence[builtins.str],
        target_domain_name: builtins.str,
        trust_direction: builtins.str,
        trust_handshake_secret: builtins.str,
        trust_type: builtins.str,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        selective_authentication: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["GoogleActiveDirectoryDomainTrustTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust google_active_directory_domain_trust} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param domain: The fully qualified domain name. e.g. mydomain.myorganization.com, with the restrictions, https://cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#domain GoogleActiveDirectoryDomainTrust#domain}
        :param target_dns_ip_addresses: The target DNS server IP addresses which can resolve the remote domain involved in the trust. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#target_dns_ip_addresses GoogleActiveDirectoryDomainTrust#target_dns_ip_addresses}
        :param target_domain_name: The fully qualified target domain name which will be in trust with the current domain. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#target_domain_name GoogleActiveDirectoryDomainTrust#target_domain_name}
        :param trust_direction: The trust direction, which decides if the current domain is trusted, trusting, or both. Possible values: ["INBOUND", "OUTBOUND", "BIDIRECTIONAL"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#trust_direction GoogleActiveDirectoryDomainTrust#trust_direction}
        :param trust_handshake_secret: The trust secret used for the handshake with the target domain. This will not be stored. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#trust_handshake_secret GoogleActiveDirectoryDomainTrust#trust_handshake_secret}
        :param trust_type: The type of trust represented by the trust resource. Possible values: ["FOREST", "EXTERNAL"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#trust_type GoogleActiveDirectoryDomainTrust#trust_type}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#id GoogleActiveDirectoryDomainTrust#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#project GoogleActiveDirectoryDomainTrust#project}.
        :param selective_authentication: Whether the trusted side has forest/domain wide access or selective access to an approved set of resources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#selective_authentication GoogleActiveDirectoryDomainTrust#selective_authentication}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#timeouts GoogleActiveDirectoryDomainTrust#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleActiveDirectoryDomainTrust.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleActiveDirectoryDomainTrustConfig(
            domain=domain,
            target_dns_ip_addresses=target_dns_ip_addresses,
            target_domain_name=target_domain_name,
            trust_direction=trust_direction,
            trust_handshake_secret=trust_handshake_secret,
            trust_type=trust_type,
            id=id,
            project=project,
            selective_authentication=selective_authentication,
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
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#create GoogleActiveDirectoryDomainTrust#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#delete GoogleActiveDirectoryDomainTrust#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#update GoogleActiveDirectoryDomainTrust#update}.
        '''
        value = GoogleActiveDirectoryDomainTrustTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetSelectiveAuthentication")
    def reset_selective_authentication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSelectiveAuthentication", []))

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
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleActiveDirectoryDomainTrustTimeoutsOutputReference":
        return typing.cast("GoogleActiveDirectoryDomainTrustTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="domainInput")
    def domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="selectiveAuthenticationInput")
    def selective_authentication_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "selectiveAuthenticationInput"))

    @builtins.property
    @jsii.member(jsii_name="targetDnsIpAddressesInput")
    def target_dns_ip_addresses_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "targetDnsIpAddressesInput"))

    @builtins.property
    @jsii.member(jsii_name="targetDomainNameInput")
    def target_domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetDomainNameInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleActiveDirectoryDomainTrustTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleActiveDirectoryDomainTrustTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="trustDirectionInput")
    def trust_direction_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "trustDirectionInput"))

    @builtins.property
    @jsii.member(jsii_name="trustHandshakeSecretInput")
    def trust_handshake_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "trustHandshakeSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="trustTypeInput")
    def trust_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "trustTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleActiveDirectoryDomainTrust, "domain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleActiveDirectoryDomainTrust, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleActiveDirectoryDomainTrust, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="selectiveAuthentication")
    def selective_authentication(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "selectiveAuthentication"))

    @selective_authentication.setter
    def selective_authentication(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleActiveDirectoryDomainTrust, "selective_authentication").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selectiveAuthentication", value)

    @builtins.property
    @jsii.member(jsii_name="targetDnsIpAddresses")
    def target_dns_ip_addresses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "targetDnsIpAddresses"))

    @target_dns_ip_addresses.setter
    def target_dns_ip_addresses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleActiveDirectoryDomainTrust, "target_dns_ip_addresses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetDnsIpAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="targetDomainName")
    def target_domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetDomainName"))

    @target_domain_name.setter
    def target_domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleActiveDirectoryDomainTrust, "target_domain_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetDomainName", value)

    @builtins.property
    @jsii.member(jsii_name="trustDirection")
    def trust_direction(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "trustDirection"))

    @trust_direction.setter
    def trust_direction(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleActiveDirectoryDomainTrust, "trust_direction").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trustDirection", value)

    @builtins.property
    @jsii.member(jsii_name="trustHandshakeSecret")
    def trust_handshake_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "trustHandshakeSecret"))

    @trust_handshake_secret.setter
    def trust_handshake_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleActiveDirectoryDomainTrust, "trust_handshake_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trustHandshakeSecret", value)

    @builtins.property
    @jsii.member(jsii_name="trustType")
    def trust_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "trustType"))

    @trust_type.setter
    def trust_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleActiveDirectoryDomainTrust, "trust_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trustType", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleActiveDirectoryDomainTrust.GoogleActiveDirectoryDomainTrustConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "domain": "domain",
        "target_dns_ip_addresses": "targetDnsIpAddresses",
        "target_domain_name": "targetDomainName",
        "trust_direction": "trustDirection",
        "trust_handshake_secret": "trustHandshakeSecret",
        "trust_type": "trustType",
        "id": "id",
        "project": "project",
        "selective_authentication": "selectiveAuthentication",
        "timeouts": "timeouts",
    },
)
class GoogleActiveDirectoryDomainTrustConfig(cdktf.TerraformMetaArguments):
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
        domain: builtins.str,
        target_dns_ip_addresses: typing.Sequence[builtins.str],
        target_domain_name: builtins.str,
        trust_direction: builtins.str,
        trust_handshake_secret: builtins.str,
        trust_type: builtins.str,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        selective_authentication: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["GoogleActiveDirectoryDomainTrustTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param domain: The fully qualified domain name. e.g. mydomain.myorganization.com, with the restrictions, https://cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#domain GoogleActiveDirectoryDomainTrust#domain}
        :param target_dns_ip_addresses: The target DNS server IP addresses which can resolve the remote domain involved in the trust. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#target_dns_ip_addresses GoogleActiveDirectoryDomainTrust#target_dns_ip_addresses}
        :param target_domain_name: The fully qualified target domain name which will be in trust with the current domain. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#target_domain_name GoogleActiveDirectoryDomainTrust#target_domain_name}
        :param trust_direction: The trust direction, which decides if the current domain is trusted, trusting, or both. Possible values: ["INBOUND", "OUTBOUND", "BIDIRECTIONAL"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#trust_direction GoogleActiveDirectoryDomainTrust#trust_direction}
        :param trust_handshake_secret: The trust secret used for the handshake with the target domain. This will not be stored. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#trust_handshake_secret GoogleActiveDirectoryDomainTrust#trust_handshake_secret}
        :param trust_type: The type of trust represented by the trust resource. Possible values: ["FOREST", "EXTERNAL"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#trust_type GoogleActiveDirectoryDomainTrust#trust_type}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#id GoogleActiveDirectoryDomainTrust#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#project GoogleActiveDirectoryDomainTrust#project}.
        :param selective_authentication: Whether the trusted side has forest/domain wide access or selective access to an approved set of resources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#selective_authentication GoogleActiveDirectoryDomainTrust#selective_authentication}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#timeouts GoogleActiveDirectoryDomainTrust#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = GoogleActiveDirectoryDomainTrustTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleActiveDirectoryDomainTrustConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument target_dns_ip_addresses", value=target_dns_ip_addresses, expected_type=type_hints["target_dns_ip_addresses"])
            check_type(argname="argument target_domain_name", value=target_domain_name, expected_type=type_hints["target_domain_name"])
            check_type(argname="argument trust_direction", value=trust_direction, expected_type=type_hints["trust_direction"])
            check_type(argname="argument trust_handshake_secret", value=trust_handshake_secret, expected_type=type_hints["trust_handshake_secret"])
            check_type(argname="argument trust_type", value=trust_type, expected_type=type_hints["trust_type"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument selective_authentication", value=selective_authentication, expected_type=type_hints["selective_authentication"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "domain": domain,
            "target_dns_ip_addresses": target_dns_ip_addresses,
            "target_domain_name": target_domain_name,
            "trust_direction": trust_direction,
            "trust_handshake_secret": trust_handshake_secret,
            "trust_type": trust_type,
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
        if id is not None:
            self._values["id"] = id
        if project is not None:
            self._values["project"] = project
        if selective_authentication is not None:
            self._values["selective_authentication"] = selective_authentication
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
    def domain(self) -> builtins.str:
        '''The fully qualified domain name. e.g. mydomain.myorganization.com, with the restrictions,  https://cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#domain GoogleActiveDirectoryDomainTrust#domain}
        '''
        result = self._values.get("domain")
        assert result is not None, "Required property 'domain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_dns_ip_addresses(self) -> typing.List[builtins.str]:
        '''The target DNS server IP addresses which can resolve the remote domain involved in the trust.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#target_dns_ip_addresses GoogleActiveDirectoryDomainTrust#target_dns_ip_addresses}
        '''
        result = self._values.get("target_dns_ip_addresses")
        assert result is not None, "Required property 'target_dns_ip_addresses' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def target_domain_name(self) -> builtins.str:
        '''The fully qualified target domain name which will be in trust with the current domain.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#target_domain_name GoogleActiveDirectoryDomainTrust#target_domain_name}
        '''
        result = self._values.get("target_domain_name")
        assert result is not None, "Required property 'target_domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def trust_direction(self) -> builtins.str:
        '''The trust direction, which decides if the current domain is trusted, trusting, or both. Possible values: ["INBOUND", "OUTBOUND", "BIDIRECTIONAL"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#trust_direction GoogleActiveDirectoryDomainTrust#trust_direction}
        '''
        result = self._values.get("trust_direction")
        assert result is not None, "Required property 'trust_direction' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def trust_handshake_secret(self) -> builtins.str:
        '''The trust secret used for the handshake with the target domain. This will not be stored.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#trust_handshake_secret GoogleActiveDirectoryDomainTrust#trust_handshake_secret}
        '''
        result = self._values.get("trust_handshake_secret")
        assert result is not None, "Required property 'trust_handshake_secret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def trust_type(self) -> builtins.str:
        '''The type of trust represented by the trust resource. Possible values: ["FOREST", "EXTERNAL"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#trust_type GoogleActiveDirectoryDomainTrust#trust_type}
        '''
        result = self._values.get("trust_type")
        assert result is not None, "Required property 'trust_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#id GoogleActiveDirectoryDomainTrust#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#project GoogleActiveDirectoryDomainTrust#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def selective_authentication(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the trusted side has forest/domain wide access or selective access to an approved set of resources.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#selective_authentication GoogleActiveDirectoryDomainTrust#selective_authentication}
        '''
        result = self._values.get("selective_authentication")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleActiveDirectoryDomainTrustTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#timeouts GoogleActiveDirectoryDomainTrust#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleActiveDirectoryDomainTrustTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleActiveDirectoryDomainTrustConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleActiveDirectoryDomainTrust.GoogleActiveDirectoryDomainTrustTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleActiveDirectoryDomainTrustTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#create GoogleActiveDirectoryDomainTrust#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#delete GoogleActiveDirectoryDomainTrust#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#update GoogleActiveDirectoryDomainTrust#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleActiveDirectoryDomainTrustTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#create GoogleActiveDirectoryDomainTrust#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#delete GoogleActiveDirectoryDomainTrust#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain_trust#update GoogleActiveDirectoryDomainTrust#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleActiveDirectoryDomainTrustTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleActiveDirectoryDomainTrustTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleActiveDirectoryDomainTrust.GoogleActiveDirectoryDomainTrustTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleActiveDirectoryDomainTrustTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

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
            type_hints = typing.get_type_hints(getattr(GoogleActiveDirectoryDomainTrustTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleActiveDirectoryDomainTrustTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleActiveDirectoryDomainTrustTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleActiveDirectoryDomainTrustTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleActiveDirectoryDomainTrustTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleActiveDirectoryDomainTrustTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleActiveDirectoryDomainTrustTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleActiveDirectoryDomainTrust",
    "GoogleActiveDirectoryDomainTrustConfig",
    "GoogleActiveDirectoryDomainTrustTimeouts",
    "GoogleActiveDirectoryDomainTrustTimeoutsOutputReference",
]

publication.publish()
