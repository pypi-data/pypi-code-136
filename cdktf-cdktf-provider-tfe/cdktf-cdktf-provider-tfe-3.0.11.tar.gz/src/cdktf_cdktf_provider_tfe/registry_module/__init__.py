'''
# `tfe_registry_module`

Refer to the Terraform Registory for docs: [`tfe_registry_module`](https://www.terraform.io/docs/providers/tfe/r/registry_module).
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


class RegistryModule(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-tfe.registryModule.RegistryModule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/tfe/r/registry_module tfe_registry_module}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        id: typing.Optional[builtins.str] = None,
        module_provider: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        organization: typing.Optional[builtins.str] = None,
        registry_name: typing.Optional[builtins.str] = None,
        vcs_repo: typing.Optional[typing.Union["RegistryModuleVcsRepo", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/tfe/r/registry_module tfe_registry_module} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/registry_module#id RegistryModule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param module_provider: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/registry_module#module_provider RegistryModule#module_provider}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/registry_module#name RegistryModule#name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/registry_module#namespace RegistryModule#namespace}.
        :param organization: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/registry_module#organization RegistryModule#organization}.
        :param registry_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/registry_module#registry_name RegistryModule#registry_name}.
        :param vcs_repo: vcs_repo block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/registry_module#vcs_repo RegistryModule#vcs_repo}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RegistryModule.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = RegistryModuleConfig(
            id=id,
            module_provider=module_provider,
            name=name,
            namespace=namespace,
            organization=organization,
            registry_name=registry_name,
            vcs_repo=vcs_repo,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putVcsRepo")
    def put_vcs_repo(
        self,
        *,
        display_identifier: builtins.str,
        identifier: builtins.str,
        oauth_token_id: builtins.str,
    ) -> None:
        '''
        :param display_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/registry_module#display_identifier RegistryModule#display_identifier}.
        :param identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/registry_module#identifier RegistryModule#identifier}.
        :param oauth_token_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/registry_module#oauth_token_id RegistryModule#oauth_token_id}.
        '''
        value = RegistryModuleVcsRepo(
            display_identifier=display_identifier,
            identifier=identifier,
            oauth_token_id=oauth_token_id,
        )

        return typing.cast(None, jsii.invoke(self, "putVcsRepo", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetModuleProvider")
    def reset_module_provider(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetModuleProvider", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetOrganization")
    def reset_organization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrganization", []))

    @jsii.member(jsii_name="resetRegistryName")
    def reset_registry_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegistryName", []))

    @jsii.member(jsii_name="resetVcsRepo")
    def reset_vcs_repo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVcsRepo", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="vcsRepo")
    def vcs_repo(self) -> "RegistryModuleVcsRepoOutputReference":
        return typing.cast("RegistryModuleVcsRepoOutputReference", jsii.get(self, "vcsRepo"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="moduleProviderInput")
    def module_provider_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "moduleProviderInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="organizationInput")
    def organization_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "organizationInput"))

    @builtins.property
    @jsii.member(jsii_name="registryNameInput")
    def registry_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "registryNameInput"))

    @builtins.property
    @jsii.member(jsii_name="vcsRepoInput")
    def vcs_repo_input(self) -> typing.Optional["RegistryModuleVcsRepo"]:
        return typing.cast(typing.Optional["RegistryModuleVcsRepo"], jsii.get(self, "vcsRepoInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RegistryModule, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="moduleProvider")
    def module_provider(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "moduleProvider"))

    @module_provider.setter
    def module_provider(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RegistryModule, "module_provider").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "moduleProvider", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RegistryModule, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RegistryModule, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="organization")
    def organization(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organization"))

    @organization.setter
    def organization(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RegistryModule, "organization").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organization", value)

    @builtins.property
    @jsii.member(jsii_name="registryName")
    def registry_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registryName"))

    @registry_name.setter
    def registry_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RegistryModule, "registry_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registryName", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-tfe.registryModule.RegistryModuleConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "id": "id",
        "module_provider": "moduleProvider",
        "name": "name",
        "namespace": "namespace",
        "organization": "organization",
        "registry_name": "registryName",
        "vcs_repo": "vcsRepo",
    },
)
class RegistryModuleConfig(cdktf.TerraformMetaArguments):
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
        id: typing.Optional[builtins.str] = None,
        module_provider: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        organization: typing.Optional[builtins.str] = None,
        registry_name: typing.Optional[builtins.str] = None,
        vcs_repo: typing.Optional[typing.Union["RegistryModuleVcsRepo", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/registry_module#id RegistryModule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param module_provider: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/registry_module#module_provider RegistryModule#module_provider}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/registry_module#name RegistryModule#name}.
        :param namespace: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/registry_module#namespace RegistryModule#namespace}.
        :param organization: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/registry_module#organization RegistryModule#organization}.
        :param registry_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/registry_module#registry_name RegistryModule#registry_name}.
        :param vcs_repo: vcs_repo block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/registry_module#vcs_repo RegistryModule#vcs_repo}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(vcs_repo, dict):
            vcs_repo = RegistryModuleVcsRepo(**vcs_repo)
        if __debug__:
            type_hints = typing.get_type_hints(RegistryModuleConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument module_provider", value=module_provider, expected_type=type_hints["module_provider"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument organization", value=organization, expected_type=type_hints["organization"])
            check_type(argname="argument registry_name", value=registry_name, expected_type=type_hints["registry_name"])
            check_type(argname="argument vcs_repo", value=vcs_repo, expected_type=type_hints["vcs_repo"])
        self._values: typing.Dict[str, typing.Any] = {}
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
        if module_provider is not None:
            self._values["module_provider"] = module_provider
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace
        if organization is not None:
            self._values["organization"] = organization
        if registry_name is not None:
            self._values["registry_name"] = registry_name
        if vcs_repo is not None:
            self._values["vcs_repo"] = vcs_repo

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
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/registry_module#id RegistryModule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def module_provider(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/registry_module#module_provider RegistryModule#module_provider}.'''
        result = self._values.get("module_provider")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/registry_module#name RegistryModule#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/registry_module#namespace RegistryModule#namespace}.'''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def organization(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/registry_module#organization RegistryModule#organization}.'''
        result = self._values.get("organization")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def registry_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/registry_module#registry_name RegistryModule#registry_name}.'''
        result = self._values.get("registry_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vcs_repo(self) -> typing.Optional["RegistryModuleVcsRepo"]:
        '''vcs_repo block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/registry_module#vcs_repo RegistryModule#vcs_repo}
        '''
        result = self._values.get("vcs_repo")
        return typing.cast(typing.Optional["RegistryModuleVcsRepo"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RegistryModuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-tfe.registryModule.RegistryModuleVcsRepo",
    jsii_struct_bases=[],
    name_mapping={
        "display_identifier": "displayIdentifier",
        "identifier": "identifier",
        "oauth_token_id": "oauthTokenId",
    },
)
class RegistryModuleVcsRepo:
    def __init__(
        self,
        *,
        display_identifier: builtins.str,
        identifier: builtins.str,
        oauth_token_id: builtins.str,
    ) -> None:
        '''
        :param display_identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/registry_module#display_identifier RegistryModule#display_identifier}.
        :param identifier: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/registry_module#identifier RegistryModule#identifier}.
        :param oauth_token_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/registry_module#oauth_token_id RegistryModule#oauth_token_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RegistryModuleVcsRepo.__init__)
            check_type(argname="argument display_identifier", value=display_identifier, expected_type=type_hints["display_identifier"])
            check_type(argname="argument identifier", value=identifier, expected_type=type_hints["identifier"])
            check_type(argname="argument oauth_token_id", value=oauth_token_id, expected_type=type_hints["oauth_token_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "display_identifier": display_identifier,
            "identifier": identifier,
            "oauth_token_id": oauth_token_id,
        }

    @builtins.property
    def display_identifier(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/registry_module#display_identifier RegistryModule#display_identifier}.'''
        result = self._values.get("display_identifier")
        assert result is not None, "Required property 'display_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identifier(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/registry_module#identifier RegistryModule#identifier}.'''
        result = self._values.get("identifier")
        assert result is not None, "Required property 'identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def oauth_token_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/tfe/r/registry_module#oauth_token_id RegistryModule#oauth_token_id}.'''
        result = self._values.get("oauth_token_id")
        assert result is not None, "Required property 'oauth_token_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RegistryModuleVcsRepo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RegistryModuleVcsRepoOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-tfe.registryModule.RegistryModuleVcsRepoOutputReference",
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
            type_hints = typing.get_type_hints(RegistryModuleVcsRepoOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="displayIdentifierInput")
    def display_identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayIdentifierInput"))

    @builtins.property
    @jsii.member(jsii_name="identifierInput")
    def identifier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identifierInput"))

    @builtins.property
    @jsii.member(jsii_name="oauthTokenIdInput")
    def oauth_token_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauthTokenIdInput"))

    @builtins.property
    @jsii.member(jsii_name="displayIdentifier")
    def display_identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayIdentifier"))

    @display_identifier.setter
    def display_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RegistryModuleVcsRepoOutputReference, "display_identifier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="identifier")
    def identifier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identifier"))

    @identifier.setter
    def identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RegistryModuleVcsRepoOutputReference, "identifier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identifier", value)

    @builtins.property
    @jsii.member(jsii_name="oauthTokenId")
    def oauth_token_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oauthTokenId"))

    @oauth_token_id.setter
    def oauth_token_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RegistryModuleVcsRepoOutputReference, "oauth_token_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauthTokenId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RegistryModuleVcsRepo]:
        return typing.cast(typing.Optional[RegistryModuleVcsRepo], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[RegistryModuleVcsRepo]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RegistryModuleVcsRepoOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "RegistryModule",
    "RegistryModuleConfig",
    "RegistryModuleVcsRepo",
    "RegistryModuleVcsRepoOutputReference",
]

publication.publish()
