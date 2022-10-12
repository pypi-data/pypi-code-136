'''
# `gitlab_group_cluster`

Refer to the Terraform Registory for docs: [`gitlab_group_cluster`](https://www.terraform.io/docs/providers/gitlab/r/group_cluster).
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


class GroupCluster(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-gitlab.groupCluster.GroupCluster",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster gitlab_group_cluster}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        group: builtins.str,
        kubernetes_api_url: builtins.str,
        kubernetes_token: builtins.str,
        name: builtins.str,
        domain: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        environment_scope: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kubernetes_authorization_type: typing.Optional[builtins.str] = None,
        kubernetes_ca_cert: typing.Optional[builtins.str] = None,
        managed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        management_project_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster gitlab_group_cluster} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param group: The id of the group to add the cluster to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#group GroupCluster#group}
        :param kubernetes_api_url: The URL to access the Kubernetes API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#kubernetes_api_url GroupCluster#kubernetes_api_url}
        :param kubernetes_token: The token to authenticate against Kubernetes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#kubernetes_token GroupCluster#kubernetes_token}
        :param name: The name of cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#name GroupCluster#name}
        :param domain: The base domain of the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#domain GroupCluster#domain}
        :param enabled: Determines if cluster is active or not. Defaults to ``true``. This attribute cannot be read. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#enabled GroupCluster#enabled}
        :param environment_scope: The associated environment to the cluster. Defaults to ``*``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#environment_scope GroupCluster#environment_scope}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#id GroupCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kubernetes_authorization_type: The cluster authorization type. Valid values are ``rbac``, ``abac``, ``unknown_authorization``. Defaults to ``rbac``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#kubernetes_authorization_type GroupCluster#kubernetes_authorization_type}
        :param kubernetes_ca_cert: TLS certificate (needed if API is using a self-signed TLS certificate). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#kubernetes_ca_cert GroupCluster#kubernetes_ca_cert}
        :param managed: Determines if cluster is managed by gitlab or not. Defaults to ``true``. This attribute cannot be read. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#managed GroupCluster#managed}
        :param management_project_id: The ID of the management project for the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#management_project_id GroupCluster#management_project_id}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GroupCluster.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GroupClusterConfig(
            group=group,
            kubernetes_api_url=kubernetes_api_url,
            kubernetes_token=kubernetes_token,
            name=name,
            domain=domain,
            enabled=enabled,
            environment_scope=environment_scope,
            id=id,
            kubernetes_authorization_type=kubernetes_authorization_type,
            kubernetes_ca_cert=kubernetes_ca_cert,
            managed=managed,
            management_project_id=management_project_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetDomain")
    def reset_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDomain", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetEnvironmentScope")
    def reset_environment_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnvironmentScope", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKubernetesAuthorizationType")
    def reset_kubernetes_authorization_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKubernetesAuthorizationType", []))

    @jsii.member(jsii_name="resetKubernetesCaCert")
    def reset_kubernetes_ca_cert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKubernetesCaCert", []))

    @jsii.member(jsii_name="resetManaged")
    def reset_managed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManaged", []))

    @jsii.member(jsii_name="resetManagementProjectId")
    def reset_management_project_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetManagementProjectId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="clusterType")
    def cluster_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterType"))

    @builtins.property
    @jsii.member(jsii_name="createdAt")
    def created_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdAt"))

    @builtins.property
    @jsii.member(jsii_name="platformType")
    def platform_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "platformType"))

    @builtins.property
    @jsii.member(jsii_name="providerType")
    def provider_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "providerType"))

    @builtins.property
    @jsii.member(jsii_name="domainInput")
    def domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domainInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentScopeInput")
    def environment_scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentScopeInput"))

    @builtins.property
    @jsii.member(jsii_name="groupInput")
    def group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kubernetesApiUrlInput")
    def kubernetes_api_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kubernetesApiUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="kubernetesAuthorizationTypeInput")
    def kubernetes_authorization_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kubernetesAuthorizationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="kubernetesCaCertInput")
    def kubernetes_ca_cert_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kubernetesCaCertInput"))

    @builtins.property
    @jsii.member(jsii_name="kubernetesTokenInput")
    def kubernetes_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kubernetesTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="managedInput")
    def managed_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "managedInput"))

    @builtins.property
    @jsii.member(jsii_name="managementProjectIdInput")
    def management_project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "managementProjectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupCluster, "domain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupCluster, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="environmentScope")
    def environment_scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "environmentScope"))

    @environment_scope.setter
    def environment_scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupCluster, "environment_scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentScope", value)

    @builtins.property
    @jsii.member(jsii_name="group")
    def group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "group"))

    @group.setter
    def group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupCluster, "group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "group", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupCluster, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="kubernetesApiUrl")
    def kubernetes_api_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kubernetesApiUrl"))

    @kubernetes_api_url.setter
    def kubernetes_api_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupCluster, "kubernetes_api_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kubernetesApiUrl", value)

    @builtins.property
    @jsii.member(jsii_name="kubernetesAuthorizationType")
    def kubernetes_authorization_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kubernetesAuthorizationType"))

    @kubernetes_authorization_type.setter
    def kubernetes_authorization_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupCluster, "kubernetes_authorization_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kubernetesAuthorizationType", value)

    @builtins.property
    @jsii.member(jsii_name="kubernetesCaCert")
    def kubernetes_ca_cert(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kubernetesCaCert"))

    @kubernetes_ca_cert.setter
    def kubernetes_ca_cert(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupCluster, "kubernetes_ca_cert").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kubernetesCaCert", value)

    @builtins.property
    @jsii.member(jsii_name="kubernetesToken")
    def kubernetes_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kubernetesToken"))

    @kubernetes_token.setter
    def kubernetes_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupCluster, "kubernetes_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kubernetesToken", value)

    @builtins.property
    @jsii.member(jsii_name="managed")
    def managed(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "managed"))

    @managed.setter
    def managed(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupCluster, "managed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managed", value)

    @builtins.property
    @jsii.member(jsii_name="managementProjectId")
    def management_project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "managementProjectId"))

    @management_project_id.setter
    def management_project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupCluster, "management_project_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managementProjectId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GroupCluster, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-gitlab.groupCluster.GroupClusterConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "group": "group",
        "kubernetes_api_url": "kubernetesApiUrl",
        "kubernetes_token": "kubernetesToken",
        "name": "name",
        "domain": "domain",
        "enabled": "enabled",
        "environment_scope": "environmentScope",
        "id": "id",
        "kubernetes_authorization_type": "kubernetesAuthorizationType",
        "kubernetes_ca_cert": "kubernetesCaCert",
        "managed": "managed",
        "management_project_id": "managementProjectId",
    },
)
class GroupClusterConfig(cdktf.TerraformMetaArguments):
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
        group: builtins.str,
        kubernetes_api_url: builtins.str,
        kubernetes_token: builtins.str,
        name: builtins.str,
        domain: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        environment_scope: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        kubernetes_authorization_type: typing.Optional[builtins.str] = None,
        kubernetes_ca_cert: typing.Optional[builtins.str] = None,
        managed: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        management_project_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param group: The id of the group to add the cluster to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#group GroupCluster#group}
        :param kubernetes_api_url: The URL to access the Kubernetes API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#kubernetes_api_url GroupCluster#kubernetes_api_url}
        :param kubernetes_token: The token to authenticate against Kubernetes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#kubernetes_token GroupCluster#kubernetes_token}
        :param name: The name of cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#name GroupCluster#name}
        :param domain: The base domain of the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#domain GroupCluster#domain}
        :param enabled: Determines if cluster is active or not. Defaults to ``true``. This attribute cannot be read. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#enabled GroupCluster#enabled}
        :param environment_scope: The associated environment to the cluster. Defaults to ``*``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#environment_scope GroupCluster#environment_scope}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#id GroupCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kubernetes_authorization_type: The cluster authorization type. Valid values are ``rbac``, ``abac``, ``unknown_authorization``. Defaults to ``rbac``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#kubernetes_authorization_type GroupCluster#kubernetes_authorization_type}
        :param kubernetes_ca_cert: TLS certificate (needed if API is using a self-signed TLS certificate). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#kubernetes_ca_cert GroupCluster#kubernetes_ca_cert}
        :param managed: Determines if cluster is managed by gitlab or not. Defaults to ``true``. This attribute cannot be read. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#managed GroupCluster#managed}
        :param management_project_id: The ID of the management project for the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#management_project_id GroupCluster#management_project_id}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(GroupClusterConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument kubernetes_api_url", value=kubernetes_api_url, expected_type=type_hints["kubernetes_api_url"])
            check_type(argname="argument kubernetes_token", value=kubernetes_token, expected_type=type_hints["kubernetes_token"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument environment_scope", value=environment_scope, expected_type=type_hints["environment_scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument kubernetes_authorization_type", value=kubernetes_authorization_type, expected_type=type_hints["kubernetes_authorization_type"])
            check_type(argname="argument kubernetes_ca_cert", value=kubernetes_ca_cert, expected_type=type_hints["kubernetes_ca_cert"])
            check_type(argname="argument managed", value=managed, expected_type=type_hints["managed"])
            check_type(argname="argument management_project_id", value=management_project_id, expected_type=type_hints["management_project_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "group": group,
            "kubernetes_api_url": kubernetes_api_url,
            "kubernetes_token": kubernetes_token,
            "name": name,
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
        if domain is not None:
            self._values["domain"] = domain
        if enabled is not None:
            self._values["enabled"] = enabled
        if environment_scope is not None:
            self._values["environment_scope"] = environment_scope
        if id is not None:
            self._values["id"] = id
        if kubernetes_authorization_type is not None:
            self._values["kubernetes_authorization_type"] = kubernetes_authorization_type
        if kubernetes_ca_cert is not None:
            self._values["kubernetes_ca_cert"] = kubernetes_ca_cert
        if managed is not None:
            self._values["managed"] = managed
        if management_project_id is not None:
            self._values["management_project_id"] = management_project_id

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
    def group(self) -> builtins.str:
        '''The id of the group to add the cluster to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#group GroupCluster#group}
        '''
        result = self._values.get("group")
        assert result is not None, "Required property 'group' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kubernetes_api_url(self) -> builtins.str:
        '''The URL to access the Kubernetes API.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#kubernetes_api_url GroupCluster#kubernetes_api_url}
        '''
        result = self._values.get("kubernetes_api_url")
        assert result is not None, "Required property 'kubernetes_api_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kubernetes_token(self) -> builtins.str:
        '''The token to authenticate against Kubernetes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#kubernetes_token GroupCluster#kubernetes_token}
        '''
        result = self._values.get("kubernetes_token")
        assert result is not None, "Required property 'kubernetes_token' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#name GroupCluster#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain(self) -> typing.Optional[builtins.str]:
        '''The base domain of the cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#domain GroupCluster#domain}
        '''
        result = self._values.get("domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Determines if cluster is active or not. Defaults to ``true``. This attribute cannot be read.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#enabled GroupCluster#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def environment_scope(self) -> typing.Optional[builtins.str]:
        '''The associated environment to the cluster. Defaults to ``*``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#environment_scope GroupCluster#environment_scope}
        '''
        result = self._values.get("environment_scope")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#id GroupCluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kubernetes_authorization_type(self) -> typing.Optional[builtins.str]:
        '''The cluster authorization type. Valid values are ``rbac``, ``abac``, ``unknown_authorization``. Defaults to ``rbac``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#kubernetes_authorization_type GroupCluster#kubernetes_authorization_type}
        '''
        result = self._values.get("kubernetes_authorization_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kubernetes_ca_cert(self) -> typing.Optional[builtins.str]:
        '''TLS certificate (needed if API is using a self-signed TLS certificate).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#kubernetes_ca_cert GroupCluster#kubernetes_ca_cert}
        '''
        result = self._values.get("kubernetes_ca_cert")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def managed(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Determines if cluster is managed by gitlab or not. Defaults to ``true``. This attribute cannot be read.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#managed GroupCluster#managed}
        '''
        result = self._values.get("managed")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def management_project_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the management project for the cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/gitlab/r/group_cluster#management_project_id GroupCluster#management_project_id}
        '''
        result = self._values.get("management_project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GroupClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "GroupCluster",
    "GroupClusterConfig",
]

publication.publish()
