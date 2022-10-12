'''
# `google_app_engine_domain_mapping`

Refer to the Terraform Registory for docs: [`google_app_engine_domain_mapping`](https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping).
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


class GoogleAppEngineDomainMapping(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineDomainMapping.GoogleAppEngineDomainMapping",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping google_app_engine_domain_mapping}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        domain_name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        override_strategy: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        ssl_settings: typing.Optional[typing.Union["GoogleAppEngineDomainMappingSslSettings", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleAppEngineDomainMappingTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping google_app_engine_domain_mapping} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param domain_name: Relative name of the domain serving the application. Example: example.com. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping#domain_name GoogleAppEngineDomainMapping#domain_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping#id GoogleAppEngineDomainMapping#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param override_strategy: Whether the domain creation should override any existing mappings for this domain. By default, overrides are rejected. Default value: "STRICT" Possible values: ["STRICT", "OVERRIDE"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping#override_strategy GoogleAppEngineDomainMapping#override_strategy}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping#project GoogleAppEngineDomainMapping#project}.
        :param ssl_settings: ssl_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping#ssl_settings GoogleAppEngineDomainMapping#ssl_settings}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping#timeouts GoogleAppEngineDomainMapping#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineDomainMapping.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleAppEngineDomainMappingConfig(
            domain_name=domain_name,
            id=id,
            override_strategy=override_strategy,
            project=project,
            ssl_settings=ssl_settings,
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

    @jsii.member(jsii_name="putSslSettings")
    def put_ssl_settings(
        self,
        *,
        ssl_management_type: builtins.str,
        certificate_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ssl_management_type: SSL management type for this domain. If 'AUTOMATIC', a managed certificate is automatically provisioned. If 'MANUAL', 'certificateId' must be manually specified in order to configure SSL for this domain. Possible values: ["AUTOMATIC", "MANUAL"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping#ssl_management_type GoogleAppEngineDomainMapping#ssl_management_type}
        :param certificate_id: ID of the AuthorizedCertificate resource configuring SSL for the application. Clearing this field will remove SSL support. By default, a managed certificate is automatically created for every domain mapping. To omit SSL support or to configure SSL manually, specify 'SslManagementType.MANUAL' on a 'CREATE' or 'UPDATE' request. You must be authorized to administer the 'AuthorizedCertificate' resource to manually map it to a DomainMapping resource. Example: 12345. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping#certificate_id GoogleAppEngineDomainMapping#certificate_id}
        '''
        value = GoogleAppEngineDomainMappingSslSettings(
            ssl_management_type=ssl_management_type, certificate_id=certificate_id
        )

        return typing.cast(None, jsii.invoke(self, "putSslSettings", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping#create GoogleAppEngineDomainMapping#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping#delete GoogleAppEngineDomainMapping#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping#update GoogleAppEngineDomainMapping#update}.
        '''
        value = GoogleAppEngineDomainMappingTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOverrideStrategy")
    def reset_override_strategy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOverrideStrategy", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetSslSettings")
    def reset_ssl_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSslSettings", []))

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="resourceRecords")
    def resource_records(self) -> "GoogleAppEngineDomainMappingResourceRecordsList":
        return typing.cast("GoogleAppEngineDomainMappingResourceRecordsList", jsii.get(self, "resourceRecords"))

    @builtins.property
    @jsii.member(jsii_name="sslSettings")
    def ssl_settings(self) -> "GoogleAppEngineDomainMappingSslSettingsOutputReference":
        return typing.cast("GoogleAppEngineDomainMappingSslSettingsOutputReference", jsii.get(self, "sslSettings"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleAppEngineDomainMappingTimeoutsOutputReference":
        return typing.cast("GoogleAppEngineDomainMappingTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="domainNameInput")
    def domain_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="overrideStrategyInput")
    def override_strategy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "overrideStrategyInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="sslSettingsInput")
    def ssl_settings_input(
        self,
    ) -> typing.Optional["GoogleAppEngineDomainMappingSslSettings"]:
        return typing.cast(typing.Optional["GoogleAppEngineDomainMappingSslSettings"], jsii.get(self, "sslSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleAppEngineDomainMappingTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleAppEngineDomainMappingTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineDomainMapping, "domain_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineDomainMapping, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="overrideStrategy")
    def override_strategy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "overrideStrategy"))

    @override_strategy.setter
    def override_strategy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineDomainMapping, "override_strategy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "overrideStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineDomainMapping, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineDomainMapping.GoogleAppEngineDomainMappingConfig",
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
        "id": "id",
        "override_strategy": "overrideStrategy",
        "project": "project",
        "ssl_settings": "sslSettings",
        "timeouts": "timeouts",
    },
)
class GoogleAppEngineDomainMappingConfig(cdktf.TerraformMetaArguments):
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
        id: typing.Optional[builtins.str] = None,
        override_strategy: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        ssl_settings: typing.Optional[typing.Union["GoogleAppEngineDomainMappingSslSettings", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleAppEngineDomainMappingTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param domain_name: Relative name of the domain serving the application. Example: example.com. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping#domain_name GoogleAppEngineDomainMapping#domain_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping#id GoogleAppEngineDomainMapping#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param override_strategy: Whether the domain creation should override any existing mappings for this domain. By default, overrides are rejected. Default value: "STRICT" Possible values: ["STRICT", "OVERRIDE"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping#override_strategy GoogleAppEngineDomainMapping#override_strategy}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping#project GoogleAppEngineDomainMapping#project}.
        :param ssl_settings: ssl_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping#ssl_settings GoogleAppEngineDomainMapping#ssl_settings}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping#timeouts GoogleAppEngineDomainMapping#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(ssl_settings, dict):
            ssl_settings = GoogleAppEngineDomainMappingSslSettings(**ssl_settings)
        if isinstance(timeouts, dict):
            timeouts = GoogleAppEngineDomainMappingTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineDomainMappingConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument override_strategy", value=override_strategy, expected_type=type_hints["override_strategy"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument ssl_settings", value=ssl_settings, expected_type=type_hints["ssl_settings"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "domain_name": domain_name,
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
        if override_strategy is not None:
            self._values["override_strategy"] = override_strategy
        if project is not None:
            self._values["project"] = project
        if ssl_settings is not None:
            self._values["ssl_settings"] = ssl_settings
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
        '''Relative name of the domain serving the application. Example: example.com.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping#domain_name GoogleAppEngineDomainMapping#domain_name}
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping#id GoogleAppEngineDomainMapping#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def override_strategy(self) -> typing.Optional[builtins.str]:
        '''Whether the domain creation should override any existing mappings for this domain.

        By default, overrides are rejected. Default value: "STRICT" Possible values: ["STRICT", "OVERRIDE"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping#override_strategy GoogleAppEngineDomainMapping#override_strategy}
        '''
        result = self._values.get("override_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping#project GoogleAppEngineDomainMapping#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssl_settings(
        self,
    ) -> typing.Optional["GoogleAppEngineDomainMappingSslSettings"]:
        '''ssl_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping#ssl_settings GoogleAppEngineDomainMapping#ssl_settings}
        '''
        result = self._values.get("ssl_settings")
        return typing.cast(typing.Optional["GoogleAppEngineDomainMappingSslSettings"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleAppEngineDomainMappingTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping#timeouts GoogleAppEngineDomainMapping#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleAppEngineDomainMappingTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineDomainMappingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineDomainMapping.GoogleAppEngineDomainMappingResourceRecords",
    jsii_struct_bases=[],
    name_mapping={},
)
class GoogleAppEngineDomainMappingResourceRecords:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineDomainMappingResourceRecords(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAppEngineDomainMappingResourceRecordsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineDomainMapping.GoogleAppEngineDomainMappingResourceRecordsList",
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
            type_hints = typing.get_type_hints(GoogleAppEngineDomainMappingResourceRecordsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleAppEngineDomainMappingResourceRecordsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineDomainMappingResourceRecordsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleAppEngineDomainMappingResourceRecordsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineDomainMappingResourceRecordsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineDomainMappingResourceRecordsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineDomainMappingResourceRecordsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GoogleAppEngineDomainMappingResourceRecordsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineDomainMapping.GoogleAppEngineDomainMappingResourceRecordsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAppEngineDomainMappingResourceRecordsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="rrdata")
    def rrdata(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rrdata"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAppEngineDomainMappingResourceRecords]:
        return typing.cast(typing.Optional[GoogleAppEngineDomainMappingResourceRecords], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAppEngineDomainMappingResourceRecords],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineDomainMappingResourceRecordsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineDomainMapping.GoogleAppEngineDomainMappingSslSettings",
    jsii_struct_bases=[],
    name_mapping={
        "ssl_management_type": "sslManagementType",
        "certificate_id": "certificateId",
    },
)
class GoogleAppEngineDomainMappingSslSettings:
    def __init__(
        self,
        *,
        ssl_management_type: builtins.str,
        certificate_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ssl_management_type: SSL management type for this domain. If 'AUTOMATIC', a managed certificate is automatically provisioned. If 'MANUAL', 'certificateId' must be manually specified in order to configure SSL for this domain. Possible values: ["AUTOMATIC", "MANUAL"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping#ssl_management_type GoogleAppEngineDomainMapping#ssl_management_type}
        :param certificate_id: ID of the AuthorizedCertificate resource configuring SSL for the application. Clearing this field will remove SSL support. By default, a managed certificate is automatically created for every domain mapping. To omit SSL support or to configure SSL manually, specify 'SslManagementType.MANUAL' on a 'CREATE' or 'UPDATE' request. You must be authorized to administer the 'AuthorizedCertificate' resource to manually map it to a DomainMapping resource. Example: 12345. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping#certificate_id GoogleAppEngineDomainMapping#certificate_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineDomainMappingSslSettings.__init__)
            check_type(argname="argument ssl_management_type", value=ssl_management_type, expected_type=type_hints["ssl_management_type"])
            check_type(argname="argument certificate_id", value=certificate_id, expected_type=type_hints["certificate_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "ssl_management_type": ssl_management_type,
        }
        if certificate_id is not None:
            self._values["certificate_id"] = certificate_id

    @builtins.property
    def ssl_management_type(self) -> builtins.str:
        '''SSL management type for this domain.

        If 'AUTOMATIC', a managed certificate is automatically provisioned.
        If 'MANUAL', 'certificateId' must be manually specified in order to configure SSL for this domain. Possible values: ["AUTOMATIC", "MANUAL"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping#ssl_management_type GoogleAppEngineDomainMapping#ssl_management_type}
        '''
        result = self._values.get("ssl_management_type")
        assert result is not None, "Required property 'ssl_management_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_id(self) -> typing.Optional[builtins.str]:
        '''ID of the AuthorizedCertificate resource configuring SSL for the application.

        Clearing this field will
        remove SSL support.
        By default, a managed certificate is automatically created for every domain mapping. To omit SSL support
        or to configure SSL manually, specify 'SslManagementType.MANUAL' on a 'CREATE' or 'UPDATE' request. You must be
        authorized to administer the 'AuthorizedCertificate' resource to manually map it to a DomainMapping resource.
        Example: 12345.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping#certificate_id GoogleAppEngineDomainMapping#certificate_id}
        '''
        result = self._values.get("certificate_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineDomainMappingSslSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAppEngineDomainMappingSslSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineDomainMapping.GoogleAppEngineDomainMappingSslSettingsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAppEngineDomainMappingSslSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCertificateId")
    def reset_certificate_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificateId", []))

    @builtins.property
    @jsii.member(jsii_name="pendingManagedCertificateId")
    def pending_managed_certificate_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pendingManagedCertificateId"))

    @builtins.property
    @jsii.member(jsii_name="certificateIdInput")
    def certificate_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateIdInput"))

    @builtins.property
    @jsii.member(jsii_name="sslManagementTypeInput")
    def ssl_management_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslManagementTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateId")
    def certificate_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificateId"))

    @certificate_id.setter
    def certificate_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineDomainMappingSslSettingsOutputReference, "certificate_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateId", value)

    @builtins.property
    @jsii.member(jsii_name="sslManagementType")
    def ssl_management_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sslManagementType"))

    @ssl_management_type.setter
    def ssl_management_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineDomainMappingSslSettingsOutputReference, "ssl_management_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslManagementType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAppEngineDomainMappingSslSettings]:
        return typing.cast(typing.Optional[GoogleAppEngineDomainMappingSslSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAppEngineDomainMappingSslSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineDomainMappingSslSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineDomainMapping.GoogleAppEngineDomainMappingTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleAppEngineDomainMappingTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping#create GoogleAppEngineDomainMapping#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping#delete GoogleAppEngineDomainMapping#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping#update GoogleAppEngineDomainMapping#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineDomainMappingTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping#create GoogleAppEngineDomainMapping#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping#delete GoogleAppEngineDomainMapping#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_domain_mapping#update GoogleAppEngineDomainMapping#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineDomainMappingTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAppEngineDomainMappingTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineDomainMapping.GoogleAppEngineDomainMappingTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAppEngineDomainMappingTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineDomainMappingTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineDomainMappingTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineDomainMappingTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleAppEngineDomainMappingTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleAppEngineDomainMappingTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleAppEngineDomainMappingTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineDomainMappingTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleAppEngineDomainMapping",
    "GoogleAppEngineDomainMappingConfig",
    "GoogleAppEngineDomainMappingResourceRecords",
    "GoogleAppEngineDomainMappingResourceRecordsList",
    "GoogleAppEngineDomainMappingResourceRecordsOutputReference",
    "GoogleAppEngineDomainMappingSslSettings",
    "GoogleAppEngineDomainMappingSslSettingsOutputReference",
    "GoogleAppEngineDomainMappingTimeouts",
    "GoogleAppEngineDomainMappingTimeoutsOutputReference",
]

publication.publish()
