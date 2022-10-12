'''
# `google_active_directory_domain`

Refer to the Terraform Registory for docs: [`google_active_directory_domain`](https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain).
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


class GoogleActiveDirectoryDomain(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleActiveDirectoryDomain.GoogleActiveDirectoryDomain",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain google_active_directory_domain}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        domain_name: builtins.str,
        locations: typing.Sequence[builtins.str],
        reserved_ip_range: builtins.str,
        admin: typing.Optional[builtins.str] = None,
        authorized_networks: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleActiveDirectoryDomainTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain google_active_directory_domain} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param domain_name: The fully qualified domain name. e.g. mydomain.myorganization.com, with the restrictions, https://cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#domain_name GoogleActiveDirectoryDomain#domain_name}
        :param locations: Locations where domain needs to be provisioned. [regions][compute/docs/regions-zones/] e.g. us-west1 or us-east4 Service supports up to 4 locations at once. Each location will use a /26 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#locations GoogleActiveDirectoryDomain#locations}
        :param reserved_ip_range: The CIDR range of internal addresses that are reserved for this domain. Reserved networks must be /24 or larger. Ranges must be unique and non-overlapping with existing subnets in authorizedNetworks Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#reserved_ip_range GoogleActiveDirectoryDomain#reserved_ip_range}
        :param admin: The name of delegated administrator account used to perform Active Directory operations. If not specified, setupadmin will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#admin GoogleActiveDirectoryDomain#admin}
        :param authorized_networks: The full names of the Google Compute Engine networks the domain instance is connected to. The domain is only available on networks listed in authorizedNetworks. If CIDR subnets overlap between networks, domain creation will fail. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#authorized_networks GoogleActiveDirectoryDomain#authorized_networks}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#id GoogleActiveDirectoryDomain#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Resource labels that can contain user-provided metadata. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#labels GoogleActiveDirectoryDomain#labels}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#project GoogleActiveDirectoryDomain#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#timeouts GoogleActiveDirectoryDomain#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleActiveDirectoryDomain.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleActiveDirectoryDomainConfig(
            domain_name=domain_name,
            locations=locations,
            reserved_ip_range=reserved_ip_range,
            admin=admin,
            authorized_networks=authorized_networks,
            id=id,
            labels=labels,
            project=project,
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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#create GoogleActiveDirectoryDomain#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#delete GoogleActiveDirectoryDomain#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#update GoogleActiveDirectoryDomain#update}.
        '''
        value = GoogleActiveDirectoryDomainTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAdmin")
    def reset_admin(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdmin", []))

    @jsii.member(jsii_name="resetAuthorizedNetworks")
    def reset_authorized_networks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthorizedNetworks", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

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
    @jsii.member(jsii_name="fqdn")
    def fqdn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fqdn"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleActiveDirectoryDomainTimeoutsOutputReference":
        return typing.cast("GoogleActiveDirectoryDomainTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="adminInput")
    def admin_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adminInput"))

    @builtins.property
    @jsii.member(jsii_name="authorizedNetworksInput")
    def authorized_networks_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "authorizedNetworksInput"))

    @builtins.property
    @jsii.member(jsii_name="domainNameInput")
    def domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="locationsInput")
    def locations_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "locationsInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="reservedIpRangeInput")
    def reserved_ip_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "reservedIpRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleActiveDirectoryDomainTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleActiveDirectoryDomainTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="admin")
    def admin(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "admin"))

    @admin.setter
    def admin(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleActiveDirectoryDomain, "admin").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "admin", value)

    @builtins.property
    @jsii.member(jsii_name="authorizedNetworks")
    def authorized_networks(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "authorizedNetworks"))

    @authorized_networks.setter
    def authorized_networks(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleActiveDirectoryDomain, "authorized_networks").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizedNetworks", value)

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleActiveDirectoryDomain, "domain_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleActiveDirectoryDomain, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleActiveDirectoryDomain, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="locations")
    def locations(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "locations"))

    @locations.setter
    def locations(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleActiveDirectoryDomain, "locations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locations", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleActiveDirectoryDomain, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="reservedIpRange")
    def reserved_ip_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "reservedIpRange"))

    @reserved_ip_range.setter
    def reserved_ip_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleActiveDirectoryDomain, "reserved_ip_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reservedIpRange", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleActiveDirectoryDomain.GoogleActiveDirectoryDomainConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "domain_name": "domainName",
        "locations": "locations",
        "reserved_ip_range": "reservedIpRange",
        "admin": "admin",
        "authorized_networks": "authorizedNetworks",
        "id": "id",
        "labels": "labels",
        "project": "project",
        "timeouts": "timeouts",
    },
)
class GoogleActiveDirectoryDomainConfig(cdktf.TerraformMetaArguments):
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
        domain_name: builtins.str,
        locations: typing.Sequence[builtins.str],
        reserved_ip_range: builtins.str,
        admin: typing.Optional[builtins.str] = None,
        authorized_networks: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleActiveDirectoryDomainTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param domain_name: The fully qualified domain name. e.g. mydomain.myorganization.com, with the restrictions, https://cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#domain_name GoogleActiveDirectoryDomain#domain_name}
        :param locations: Locations where domain needs to be provisioned. [regions][compute/docs/regions-zones/] e.g. us-west1 or us-east4 Service supports up to 4 locations at once. Each location will use a /26 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#locations GoogleActiveDirectoryDomain#locations}
        :param reserved_ip_range: The CIDR range of internal addresses that are reserved for this domain. Reserved networks must be /24 or larger. Ranges must be unique and non-overlapping with existing subnets in authorizedNetworks Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#reserved_ip_range GoogleActiveDirectoryDomain#reserved_ip_range}
        :param admin: The name of delegated administrator account used to perform Active Directory operations. If not specified, setupadmin will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#admin GoogleActiveDirectoryDomain#admin}
        :param authorized_networks: The full names of the Google Compute Engine networks the domain instance is connected to. The domain is only available on networks listed in authorizedNetworks. If CIDR subnets overlap between networks, domain creation will fail. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#authorized_networks GoogleActiveDirectoryDomain#authorized_networks}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#id GoogleActiveDirectoryDomain#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Resource labels that can contain user-provided metadata. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#labels GoogleActiveDirectoryDomain#labels}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#project GoogleActiveDirectoryDomain#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#timeouts GoogleActiveDirectoryDomain#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = GoogleActiveDirectoryDomainTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleActiveDirectoryDomainConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument locations", value=locations, expected_type=type_hints["locations"])
            check_type(argname="argument reserved_ip_range", value=reserved_ip_range, expected_type=type_hints["reserved_ip_range"])
            check_type(argname="argument admin", value=admin, expected_type=type_hints["admin"])
            check_type(argname="argument authorized_networks", value=authorized_networks, expected_type=type_hints["authorized_networks"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "domain_name": domain_name,
            "locations": locations,
            "reserved_ip_range": reserved_ip_range,
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
        if admin is not None:
            self._values["admin"] = admin
        if authorized_networks is not None:
            self._values["authorized_networks"] = authorized_networks
        if id is not None:
            self._values["id"] = id
        if labels is not None:
            self._values["labels"] = labels
        if project is not None:
            self._values["project"] = project
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
    def domain_name(self) -> builtins.str:
        '''The fully qualified domain name. e.g. mydomain.myorganization.com, with the restrictions,  https://cloud.google.com/managed-microsoft-ad/reference/rest/v1/projects.locations.global.domains.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#domain_name GoogleActiveDirectoryDomain#domain_name}
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def locations(self) -> typing.List[builtins.str]:
        '''Locations where domain needs to be provisioned.

        [regions][compute/docs/regions-zones/]
        e.g. us-west1 or us-east4 Service supports up to 4 locations at once. Each location will use a /26 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#locations GoogleActiveDirectoryDomain#locations}
        '''
        result = self._values.get("locations")
        assert result is not None, "Required property 'locations' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def reserved_ip_range(self) -> builtins.str:
        '''The CIDR range of internal addresses that are reserved for this domain.

        Reserved networks must be /24 or larger.
        Ranges must be unique and non-overlapping with existing subnets in authorizedNetworks

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#reserved_ip_range GoogleActiveDirectoryDomain#reserved_ip_range}
        '''
        result = self._values.get("reserved_ip_range")
        assert result is not None, "Required property 'reserved_ip_range' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def admin(self) -> typing.Optional[builtins.str]:
        '''The name of delegated administrator account used to perform Active Directory operations.  If not specified, setupadmin will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#admin GoogleActiveDirectoryDomain#admin}
        '''
        result = self._values.get("admin")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def authorized_networks(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The full names of the Google Compute Engine networks the domain instance is connected to.

        The domain is only available on networks listed in authorizedNetworks.
        If CIDR subnets overlap between networks, domain creation will fail.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#authorized_networks GoogleActiveDirectoryDomain#authorized_networks}
        '''
        result = self._values.get("authorized_networks")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#id GoogleActiveDirectoryDomain#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Resource labels that can contain user-provided metadata.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#labels GoogleActiveDirectoryDomain#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#project GoogleActiveDirectoryDomain#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleActiveDirectoryDomainTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#timeouts GoogleActiveDirectoryDomain#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleActiveDirectoryDomainTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleActiveDirectoryDomainConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleActiveDirectoryDomain.GoogleActiveDirectoryDomainTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleActiveDirectoryDomainTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#create GoogleActiveDirectoryDomain#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#delete GoogleActiveDirectoryDomain#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#update GoogleActiveDirectoryDomain#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleActiveDirectoryDomainTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#create GoogleActiveDirectoryDomain#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#delete GoogleActiveDirectoryDomain#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_active_directory_domain#update GoogleActiveDirectoryDomain#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleActiveDirectoryDomainTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleActiveDirectoryDomainTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleActiveDirectoryDomain.GoogleActiveDirectoryDomainTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleActiveDirectoryDomainTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleActiveDirectoryDomainTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleActiveDirectoryDomainTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleActiveDirectoryDomainTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleActiveDirectoryDomainTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleActiveDirectoryDomainTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleActiveDirectoryDomainTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleActiveDirectoryDomainTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleActiveDirectoryDomain",
    "GoogleActiveDirectoryDomainConfig",
    "GoogleActiveDirectoryDomainTimeouts",
    "GoogleActiveDirectoryDomainTimeoutsOutputReference",
]

publication.publish()
