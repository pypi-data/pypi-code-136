'''
# `ionoscloud_k8s_cluster`

Refer to the Terraform Registory for docs: [`ionoscloud_k8s_cluster`](https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster).
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


class K8SCluster(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.k8SCluster.K8SCluster",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster ionoscloud_k8s_cluster}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        api_subnet_allow_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        k8_s_version: typing.Optional[builtins.str] = None,
        maintenance_window: typing.Optional[typing.Union["K8SClusterMaintenanceWindow", typing.Dict[str, typing.Any]]] = None,
        s3_buckets: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["K8SClusterS3Buckets", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["K8SClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
        viable_node_pool_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster ionoscloud_k8s_cluster} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The desired name for the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#name K8SCluster#name}
        :param api_subnet_allow_list: Access to the K8s API server is restricted to these CIDRs. Cluster-internal traffic is not affected by this restriction. If no allowlist is specified, access is not restricted. If an IP without subnet mask is provided, the default value will be used: 32 for IPv4 and 128 for IPv6. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#api_subnet_allow_list K8SCluster#api_subnet_allow_list}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#id K8SCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param k8_s_version: The desired kubernetes version. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#k8s_version K8SCluster#k8s_version}
        :param maintenance_window: maintenance_window block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#maintenance_window K8SCluster#maintenance_window}
        :param s3_buckets: s3_buckets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#s3_buckets K8SCluster#s3_buckets}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#timeouts K8SCluster#timeouts}
        :param viable_node_pool_versions: List of versions that may be used for node pools under this cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#viable_node_pool_versions K8SCluster#viable_node_pool_versions}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(K8SCluster.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = K8SClusterConfig(
            name=name,
            api_subnet_allow_list=api_subnet_allow_list,
            id=id,
            k8_s_version=k8_s_version,
            maintenance_window=maintenance_window,
            s3_buckets=s3_buckets,
            timeouts=timeouts,
            viable_node_pool_versions=viable_node_pool_versions,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putMaintenanceWindow")
    def put_maintenance_window(
        self,
        *,
        day_of_the_week: builtins.str,
        time: builtins.str,
    ) -> None:
        '''
        :param day_of_the_week: Day of the week when maintenance is allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#day_of_the_week K8SCluster#day_of_the_week}
        :param time: A clock time in the day when maintenance is allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#time K8SCluster#time}
        '''
        value = K8SClusterMaintenanceWindow(day_of_the_week=day_of_the_week, time=time)

        return typing.cast(None, jsii.invoke(self, "putMaintenanceWindow", [value]))

    @jsii.member(jsii_name="putS3Buckets")
    def put_s3_buckets(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["K8SClusterS3Buckets", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(K8SCluster.put_s3_buckets)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putS3Buckets", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        default: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#create K8SCluster#create}.
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#default K8SCluster#default}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#delete K8SCluster#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#update K8SCluster#update}.
        '''
        value = K8SClusterTimeouts(
            create=create, default=default, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetApiSubnetAllowList")
    def reset_api_subnet_allow_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiSubnetAllowList", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetK8SVersion")
    def reset_k8_s_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetK8SVersion", []))

    @jsii.member(jsii_name="resetMaintenanceWindow")
    def reset_maintenance_window(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaintenanceWindow", []))

    @jsii.member(jsii_name="resetS3Buckets")
    def reset_s3_buckets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3Buckets", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetViableNodePoolVersions")
    def reset_viable_node_pool_versions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetViableNodePoolVersions", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindow")
    def maintenance_window(self) -> "K8SClusterMaintenanceWindowOutputReference":
        return typing.cast("K8SClusterMaintenanceWindowOutputReference", jsii.get(self, "maintenanceWindow"))

    @builtins.property
    @jsii.member(jsii_name="s3Buckets")
    def s3_buckets(self) -> "K8SClusterS3BucketsList":
        return typing.cast("K8SClusterS3BucketsList", jsii.get(self, "s3Buckets"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "K8SClusterTimeoutsOutputReference":
        return typing.cast("K8SClusterTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="apiSubnetAllowListInput")
    def api_subnet_allow_list_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "apiSubnetAllowListInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="k8SVersionInput")
    def k8_s_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "k8SVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="maintenanceWindowInput")
    def maintenance_window_input(
        self,
    ) -> typing.Optional["K8SClusterMaintenanceWindow"]:
        return typing.cast(typing.Optional["K8SClusterMaintenanceWindow"], jsii.get(self, "maintenanceWindowInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="s3BucketsInput")
    def s3_buckets_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["K8SClusterS3Buckets"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["K8SClusterS3Buckets"]]], jsii.get(self, "s3BucketsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["K8SClusterTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["K8SClusterTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="viableNodePoolVersionsInput")
    def viable_node_pool_versions_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "viableNodePoolVersionsInput"))

    @builtins.property
    @jsii.member(jsii_name="apiSubnetAllowList")
    def api_subnet_allow_list(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "apiSubnetAllowList"))

    @api_subnet_allow_list.setter
    def api_subnet_allow_list(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SCluster, "api_subnet_allow_list").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiSubnetAllowList", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SCluster, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="k8SVersion")
    def k8_s_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "k8SVersion"))

    @k8_s_version.setter
    def k8_s_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SCluster, "k8_s_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "k8SVersion", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SCluster, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="viableNodePoolVersions")
    def viable_node_pool_versions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "viableNodePoolVersions"))

    @viable_node_pool_versions.setter
    def viable_node_pool_versions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SCluster, "viable_node_pool_versions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "viableNodePoolVersions", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ionoscloud.k8SCluster.K8SClusterConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "api_subnet_allow_list": "apiSubnetAllowList",
        "id": "id",
        "k8_s_version": "k8SVersion",
        "maintenance_window": "maintenanceWindow",
        "s3_buckets": "s3Buckets",
        "timeouts": "timeouts",
        "viable_node_pool_versions": "viableNodePoolVersions",
    },
)
class K8SClusterConfig(cdktf.TerraformMetaArguments):
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
        name: builtins.str,
        api_subnet_allow_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        k8_s_version: typing.Optional[builtins.str] = None,
        maintenance_window: typing.Optional[typing.Union["K8SClusterMaintenanceWindow", typing.Dict[str, typing.Any]]] = None,
        s3_buckets: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["K8SClusterS3Buckets", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["K8SClusterTimeouts", typing.Dict[str, typing.Any]]] = None,
        viable_node_pool_versions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The desired name for the cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#name K8SCluster#name}
        :param api_subnet_allow_list: Access to the K8s API server is restricted to these CIDRs. Cluster-internal traffic is not affected by this restriction. If no allowlist is specified, access is not restricted. If an IP without subnet mask is provided, the default value will be used: 32 for IPv4 and 128 for IPv6. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#api_subnet_allow_list K8SCluster#api_subnet_allow_list}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#id K8SCluster#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param k8_s_version: The desired kubernetes version. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#k8s_version K8SCluster#k8s_version}
        :param maintenance_window: maintenance_window block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#maintenance_window K8SCluster#maintenance_window}
        :param s3_buckets: s3_buckets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#s3_buckets K8SCluster#s3_buckets}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#timeouts K8SCluster#timeouts}
        :param viable_node_pool_versions: List of versions that may be used for node pools under this cluster. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#viable_node_pool_versions K8SCluster#viable_node_pool_versions}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(maintenance_window, dict):
            maintenance_window = K8SClusterMaintenanceWindow(**maintenance_window)
        if isinstance(timeouts, dict):
            timeouts = K8SClusterTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(K8SClusterConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument api_subnet_allow_list", value=api_subnet_allow_list, expected_type=type_hints["api_subnet_allow_list"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument k8_s_version", value=k8_s_version, expected_type=type_hints["k8_s_version"])
            check_type(argname="argument maintenance_window", value=maintenance_window, expected_type=type_hints["maintenance_window"])
            check_type(argname="argument s3_buckets", value=s3_buckets, expected_type=type_hints["s3_buckets"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument viable_node_pool_versions", value=viable_node_pool_versions, expected_type=type_hints["viable_node_pool_versions"])
        self._values: typing.Dict[str, typing.Any] = {
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
        if api_subnet_allow_list is not None:
            self._values["api_subnet_allow_list"] = api_subnet_allow_list
        if id is not None:
            self._values["id"] = id
        if k8_s_version is not None:
            self._values["k8_s_version"] = k8_s_version
        if maintenance_window is not None:
            self._values["maintenance_window"] = maintenance_window
        if s3_buckets is not None:
            self._values["s3_buckets"] = s3_buckets
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if viable_node_pool_versions is not None:
            self._values["viable_node_pool_versions"] = viable_node_pool_versions

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
    def name(self) -> builtins.str:
        '''The desired name for the cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#name K8SCluster#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_subnet_allow_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Access to the K8s API server is restricted to these CIDRs.

        Cluster-internal traffic is not affected by this restriction. If no allowlist is specified, access is not restricted. If an IP without subnet mask is provided, the default value will be used: 32 for IPv4 and 128 for IPv6.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#api_subnet_allow_list K8SCluster#api_subnet_allow_list}
        '''
        result = self._values.get("api_subnet_allow_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#id K8SCluster#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def k8_s_version(self) -> typing.Optional[builtins.str]:
        '''The desired kubernetes version.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#k8s_version K8SCluster#k8s_version}
        '''
        result = self._values.get("k8_s_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def maintenance_window(self) -> typing.Optional["K8SClusterMaintenanceWindow"]:
        '''maintenance_window block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#maintenance_window K8SCluster#maintenance_window}
        '''
        result = self._values.get("maintenance_window")
        return typing.cast(typing.Optional["K8SClusterMaintenanceWindow"], result)

    @builtins.property
    def s3_buckets(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["K8SClusterS3Buckets"]]]:
        '''s3_buckets block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#s3_buckets K8SCluster#s3_buckets}
        '''
        result = self._values.get("s3_buckets")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["K8SClusterS3Buckets"]]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["K8SClusterTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#timeouts K8SCluster#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["K8SClusterTimeouts"], result)

    @builtins.property
    def viable_node_pool_versions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of versions that may be used for node pools under this cluster.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#viable_node_pool_versions K8SCluster#viable_node_pool_versions}
        '''
        result = self._values.get("viable_node_pool_versions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "K8SClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-ionoscloud.k8SCluster.K8SClusterMaintenanceWindow",
    jsii_struct_bases=[],
    name_mapping={"day_of_the_week": "dayOfTheWeek", "time": "time"},
)
class K8SClusterMaintenanceWindow:
    def __init__(self, *, day_of_the_week: builtins.str, time: builtins.str) -> None:
        '''
        :param day_of_the_week: Day of the week when maintenance is allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#day_of_the_week K8SCluster#day_of_the_week}
        :param time: A clock time in the day when maintenance is allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#time K8SCluster#time}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(K8SClusterMaintenanceWindow.__init__)
            check_type(argname="argument day_of_the_week", value=day_of_the_week, expected_type=type_hints["day_of_the_week"])
            check_type(argname="argument time", value=time, expected_type=type_hints["time"])
        self._values: typing.Dict[str, typing.Any] = {
            "day_of_the_week": day_of_the_week,
            "time": time,
        }

    @builtins.property
    def day_of_the_week(self) -> builtins.str:
        '''Day of the week when maintenance is allowed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#day_of_the_week K8SCluster#day_of_the_week}
        '''
        result = self._values.get("day_of_the_week")
        assert result is not None, "Required property 'day_of_the_week' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def time(self) -> builtins.str:
        '''A clock time in the day when maintenance is allowed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#time K8SCluster#time}
        '''
        result = self._values.get("time")
        assert result is not None, "Required property 'time' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "K8SClusterMaintenanceWindow(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class K8SClusterMaintenanceWindowOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.k8SCluster.K8SClusterMaintenanceWindowOutputReference",
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
            type_hints = typing.get_type_hints(K8SClusterMaintenanceWindowOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="dayOfTheWeekInput")
    def day_of_the_week_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dayOfTheWeekInput"))

    @builtins.property
    @jsii.member(jsii_name="timeInput")
    def time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeInput"))

    @builtins.property
    @jsii.member(jsii_name="dayOfTheWeek")
    def day_of_the_week(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dayOfTheWeek"))

    @day_of_the_week.setter
    def day_of_the_week(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SClusterMaintenanceWindowOutputReference, "day_of_the_week").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dayOfTheWeek", value)

    @builtins.property
    @jsii.member(jsii_name="time")
    def time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "time"))

    @time.setter
    def time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SClusterMaintenanceWindowOutputReference, "time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "time", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[K8SClusterMaintenanceWindow]:
        return typing.cast(typing.Optional[K8SClusterMaintenanceWindow], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[K8SClusterMaintenanceWindow],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SClusterMaintenanceWindowOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ionoscloud.k8SCluster.K8SClusterS3Buckets",
    jsii_struct_bases=[],
    name_mapping={"name": "name"},
)
class K8SClusterS3Buckets:
    def __init__(self, *, name: typing.Optional[builtins.str] = None) -> None:
        '''
        :param name: Name of the S3 bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#name K8SCluster#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(K8SClusterS3Buckets.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the S3 bucket.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#name K8SCluster#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "K8SClusterS3Buckets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class K8SClusterS3BucketsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.k8SCluster.K8SClusterS3BucketsList",
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
            type_hints = typing.get_type_hints(K8SClusterS3BucketsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "K8SClusterS3BucketsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(K8SClusterS3BucketsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("K8SClusterS3BucketsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SClusterS3BucketsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(K8SClusterS3BucketsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(K8SClusterS3BucketsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[K8SClusterS3Buckets]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[K8SClusterS3Buckets]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[K8SClusterS3Buckets]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SClusterS3BucketsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class K8SClusterS3BucketsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.k8SCluster.K8SClusterS3BucketsOutputReference",
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
            type_hints = typing.get_type_hints(K8SClusterS3BucketsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SClusterS3BucketsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[K8SClusterS3Buckets, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[K8SClusterS3Buckets, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[K8SClusterS3Buckets, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SClusterS3BucketsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ionoscloud.k8SCluster.K8SClusterTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "default": "default",
        "delete": "delete",
        "update": "update",
    },
)
class K8SClusterTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        default: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#create K8SCluster#create}.
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#default K8SCluster#default}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#delete K8SCluster#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#update K8SCluster#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(K8SClusterTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if default is not None:
            self._values["default"] = default
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#create K8SCluster#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#default K8SCluster#default}.'''
        result = self._values.get("default")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#delete K8SCluster#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/r/k8s_cluster#update K8SCluster#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "K8SClusterTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class K8SClusterTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.k8SCluster.K8SClusterTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(K8SClusterTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDefault")
    def reset_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefault", []))

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
    @jsii.member(jsii_name="defaultInput")
    def default_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultInput"))

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
            type_hints = typing.get_type_hints(getattr(K8SClusterTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="default")
    def default(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "default"))

    @default.setter
    def default(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SClusterTimeoutsOutputReference, "default").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SClusterTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SClusterTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[K8SClusterTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[K8SClusterTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[K8SClusterTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(K8SClusterTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "K8SCluster",
    "K8SClusterConfig",
    "K8SClusterMaintenanceWindow",
    "K8SClusterMaintenanceWindowOutputReference",
    "K8SClusterS3Buckets",
    "K8SClusterS3BucketsList",
    "K8SClusterS3BucketsOutputReference",
    "K8SClusterTimeouts",
    "K8SClusterTimeoutsOutputReference",
]

publication.publish()
