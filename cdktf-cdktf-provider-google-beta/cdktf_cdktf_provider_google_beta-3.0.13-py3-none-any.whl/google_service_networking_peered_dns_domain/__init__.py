'''
# `google_service_networking_peered_dns_domain`

Refer to the Terraform Registory for docs: [`google_service_networking_peered_dns_domain`](https://www.terraform.io/docs/providers/google-beta/r/google_service_networking_peered_dns_domain).
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


class GoogleServiceNetworkingPeeredDnsDomain(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleServiceNetworkingPeeredDnsDomain.GoogleServiceNetworkingPeeredDnsDomain",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_networking_peered_dns_domain google_service_networking_peered_dns_domain}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        dns_suffix: builtins.str,
        name: builtins.str,
        network: builtins.str,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        service: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleServiceNetworkingPeeredDnsDomainTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_networking_peered_dns_domain google_service_networking_peered_dns_domain} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param dns_suffix: The DNS domain name suffix of the peered DNS domain. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_networking_peered_dns_domain#dns_suffix GoogleServiceNetworkingPeeredDnsDomain#dns_suffix}
        :param name: Name of the peered DNS domain. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_networking_peered_dns_domain#name GoogleServiceNetworkingPeeredDnsDomain#name}
        :param network: Network in the consumer project to peer with. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_networking_peered_dns_domain#network GoogleServiceNetworkingPeeredDnsDomain#network}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_networking_peered_dns_domain#id GoogleServiceNetworkingPeeredDnsDomain#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: The ID of the project that the service account will be created in. Defaults to the provider project configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_networking_peered_dns_domain#project GoogleServiceNetworkingPeeredDnsDomain#project}
        :param service: The name of the service to create a peered DNS domain for, e.g. servicenetworking.googleapis.com. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_networking_peered_dns_domain#service GoogleServiceNetworkingPeeredDnsDomain#service}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_networking_peered_dns_domain#timeouts GoogleServiceNetworkingPeeredDnsDomain#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleServiceNetworkingPeeredDnsDomain.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleServiceNetworkingPeeredDnsDomainConfig(
            dns_suffix=dns_suffix,
            name=name,
            network=network,
            id=id,
            project=project,
            service=service,
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
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_networking_peered_dns_domain#create GoogleServiceNetworkingPeeredDnsDomain#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_networking_peered_dns_domain#delete GoogleServiceNetworkingPeeredDnsDomain#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_networking_peered_dns_domain#read GoogleServiceNetworkingPeeredDnsDomain#read}.
        '''
        value = GoogleServiceNetworkingPeeredDnsDomainTimeouts(
            create=create, delete=delete, read=read
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetService")
    def reset_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetService", []))

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
    @jsii.member(jsii_name="parent")
    def parent(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parent"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(
        self,
    ) -> "GoogleServiceNetworkingPeeredDnsDomainTimeoutsOutputReference":
        return typing.cast("GoogleServiceNetworkingPeeredDnsDomainTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="dnsSuffixInput")
    def dns_suffix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dnsSuffixInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInput")
    def network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleServiceNetworkingPeeredDnsDomainTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleServiceNetworkingPeeredDnsDomainTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsSuffix")
    def dns_suffix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dnsSuffix"))

    @dns_suffix.setter
    def dns_suffix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleServiceNetworkingPeeredDnsDomain, "dns_suffix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsSuffix", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleServiceNetworkingPeeredDnsDomain, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleServiceNetworkingPeeredDnsDomain, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "network"))

    @network.setter
    def network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleServiceNetworkingPeeredDnsDomain, "network").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "network", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleServiceNetworkingPeeredDnsDomain, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "service"))

    @service.setter
    def service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleServiceNetworkingPeeredDnsDomain, "service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleServiceNetworkingPeeredDnsDomain.GoogleServiceNetworkingPeeredDnsDomainConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "dns_suffix": "dnsSuffix",
        "name": "name",
        "network": "network",
        "id": "id",
        "project": "project",
        "service": "service",
        "timeouts": "timeouts",
    },
)
class GoogleServiceNetworkingPeeredDnsDomainConfig(cdktf.TerraformMetaArguments):
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
        dns_suffix: builtins.str,
        name: builtins.str,
        network: builtins.str,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        service: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleServiceNetworkingPeeredDnsDomainTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param dns_suffix: The DNS domain name suffix of the peered DNS domain. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_networking_peered_dns_domain#dns_suffix GoogleServiceNetworkingPeeredDnsDomain#dns_suffix}
        :param name: Name of the peered DNS domain. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_networking_peered_dns_domain#name GoogleServiceNetworkingPeeredDnsDomain#name}
        :param network: Network in the consumer project to peer with. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_networking_peered_dns_domain#network GoogleServiceNetworkingPeeredDnsDomain#network}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_networking_peered_dns_domain#id GoogleServiceNetworkingPeeredDnsDomain#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: The ID of the project that the service account will be created in. Defaults to the provider project configuration. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_networking_peered_dns_domain#project GoogleServiceNetworkingPeeredDnsDomain#project}
        :param service: The name of the service to create a peered DNS domain for, e.g. servicenetworking.googleapis.com. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_networking_peered_dns_domain#service GoogleServiceNetworkingPeeredDnsDomain#service}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_networking_peered_dns_domain#timeouts GoogleServiceNetworkingPeeredDnsDomain#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = GoogleServiceNetworkingPeeredDnsDomainTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleServiceNetworkingPeeredDnsDomainConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument dns_suffix", value=dns_suffix, expected_type=type_hints["dns_suffix"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "dns_suffix": dns_suffix,
            "name": name,
            "network": network,
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
        if service is not None:
            self._values["service"] = service
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
    def dns_suffix(self) -> builtins.str:
        '''The DNS domain name suffix of the peered DNS domain.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_networking_peered_dns_domain#dns_suffix GoogleServiceNetworkingPeeredDnsDomain#dns_suffix}
        '''
        result = self._values.get("dns_suffix")
        assert result is not None, "Required property 'dns_suffix' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the peered DNS domain.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_networking_peered_dns_domain#name GoogleServiceNetworkingPeeredDnsDomain#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network(self) -> builtins.str:
        '''Network in the consumer project to peer with.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_networking_peered_dns_domain#network GoogleServiceNetworkingPeeredDnsDomain#network}
        '''
        result = self._values.get("network")
        assert result is not None, "Required property 'network' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_networking_peered_dns_domain#id GoogleServiceNetworkingPeeredDnsDomain#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''The ID of the project that the service account will be created in. Defaults to the provider project configuration.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_networking_peered_dns_domain#project GoogleServiceNetworkingPeeredDnsDomain#project}
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service(self) -> typing.Optional[builtins.str]:
        '''The name of the service to create a peered DNS domain for, e.g. servicenetworking.googleapis.com.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_networking_peered_dns_domain#service GoogleServiceNetworkingPeeredDnsDomain#service}
        '''
        result = self._values.get("service")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(
        self,
    ) -> typing.Optional["GoogleServiceNetworkingPeeredDnsDomainTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_networking_peered_dns_domain#timeouts GoogleServiceNetworkingPeeredDnsDomain#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleServiceNetworkingPeeredDnsDomainTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleServiceNetworkingPeeredDnsDomainConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleServiceNetworkingPeeredDnsDomain.GoogleServiceNetworkingPeeredDnsDomainTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "read": "read"},
)
class GoogleServiceNetworkingPeeredDnsDomainTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_networking_peered_dns_domain#create GoogleServiceNetworkingPeeredDnsDomain#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_networking_peered_dns_domain#delete GoogleServiceNetworkingPeeredDnsDomain#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_networking_peered_dns_domain#read GoogleServiceNetworkingPeeredDnsDomain#read}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleServiceNetworkingPeeredDnsDomainTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if read is not None:
            self._values["read"] = read

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_networking_peered_dns_domain#create GoogleServiceNetworkingPeeredDnsDomain#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_networking_peered_dns_domain#delete GoogleServiceNetworkingPeeredDnsDomain#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_service_networking_peered_dns_domain#read GoogleServiceNetworkingPeeredDnsDomain#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleServiceNetworkingPeeredDnsDomainTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleServiceNetworkingPeeredDnsDomainTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleServiceNetworkingPeeredDnsDomain.GoogleServiceNetworkingPeeredDnsDomainTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleServiceNetworkingPeeredDnsDomainTimeoutsOutputReference.__init__)
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
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleServiceNetworkingPeeredDnsDomainTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleServiceNetworkingPeeredDnsDomainTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleServiceNetworkingPeeredDnsDomainTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleServiceNetworkingPeeredDnsDomainTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleServiceNetworkingPeeredDnsDomainTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleServiceNetworkingPeeredDnsDomainTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleServiceNetworkingPeeredDnsDomainTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleServiceNetworkingPeeredDnsDomain",
    "GoogleServiceNetworkingPeeredDnsDomainConfig",
    "GoogleServiceNetworkingPeeredDnsDomainTimeouts",
    "GoogleServiceNetworkingPeeredDnsDomainTimeoutsOutputReference",
]

publication.publish()
