'''
# `databricks_mount`

Refer to the Terraform Registory for docs: [`databricks_mount`](https://www.terraform.io/docs/providers/databricks/r/mount).
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


class Mount(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.mount.Mount",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/mount databricks_mount}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        abfs: typing.Optional[typing.Union["MountAbfs", typing.Dict[str, typing.Any]]] = None,
        adl: typing.Optional[typing.Union["MountAdl", typing.Dict[str, typing.Any]]] = None,
        cluster_id: typing.Optional[builtins.str] = None,
        encryption_type: typing.Optional[builtins.str] = None,
        extra_configs: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        gs: typing.Optional[typing.Union["MountGs", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        resource_id: typing.Optional[builtins.str] = None,
        s3: typing.Optional[typing.Union["MountS3", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["MountTimeouts", typing.Dict[str, typing.Any]]] = None,
        uri: typing.Optional[builtins.str] = None,
        wasb: typing.Optional[typing.Union["MountWasb", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/mount databricks_mount} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param abfs: abfs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#abfs Mount#abfs}
        :param adl: adl block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#adl Mount#adl}
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#cluster_id Mount#cluster_id}.
        :param encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#encryption_type Mount#encryption_type}.
        :param extra_configs: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#extra_configs Mount#extra_configs}.
        :param gs: gs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#gs Mount#gs}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#id Mount#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#name Mount#name}.
        :param resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#resource_id Mount#resource_id}.
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#s3 Mount#s3}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#timeouts Mount#timeouts}
        :param uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#uri Mount#uri}.
        :param wasb: wasb block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#wasb Mount#wasb}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Mount.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MountConfig(
            abfs=abfs,
            adl=adl,
            cluster_id=cluster_id,
            encryption_type=encryption_type,
            extra_configs=extra_configs,
            gs=gs,
            id=id,
            name=name,
            resource_id=resource_id,
            s3=s3,
            timeouts=timeouts,
            uri=uri,
            wasb=wasb,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAbfs")
    def put_abfs(
        self,
        *,
        client_id: builtins.str,
        client_secret_key: builtins.str,
        client_secret_scope: builtins.str,
        initialize_file_system: typing.Union[builtins.bool, cdktf.IResolvable],
        container_name: typing.Optional[builtins.str] = None,
        directory: typing.Optional[builtins.str] = None,
        storage_account_name: typing.Optional[builtins.str] = None,
        tenant_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_id Mount#client_id}.
        :param client_secret_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_secret_key Mount#client_secret_key}.
        :param client_secret_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_secret_scope Mount#client_secret_scope}.
        :param initialize_file_system: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#initialize_file_system Mount#initialize_file_system}.
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#container_name Mount#container_name}.
        :param directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#directory Mount#directory}.
        :param storage_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#storage_account_name Mount#storage_account_name}.
        :param tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#tenant_id Mount#tenant_id}.
        '''
        value = MountAbfs(
            client_id=client_id,
            client_secret_key=client_secret_key,
            client_secret_scope=client_secret_scope,
            initialize_file_system=initialize_file_system,
            container_name=container_name,
            directory=directory,
            storage_account_name=storage_account_name,
            tenant_id=tenant_id,
        )

        return typing.cast(None, jsii.invoke(self, "putAbfs", [value]))

    @jsii.member(jsii_name="putAdl")
    def put_adl(
        self,
        *,
        client_id: builtins.str,
        client_secret_key: builtins.str,
        client_secret_scope: builtins.str,
        directory: typing.Optional[builtins.str] = None,
        spark_conf_prefix: typing.Optional[builtins.str] = None,
        storage_resource_name: typing.Optional[builtins.str] = None,
        tenant_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_id Mount#client_id}.
        :param client_secret_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_secret_key Mount#client_secret_key}.
        :param client_secret_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_secret_scope Mount#client_secret_scope}.
        :param directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#directory Mount#directory}.
        :param spark_conf_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#spark_conf_prefix Mount#spark_conf_prefix}.
        :param storage_resource_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#storage_resource_name Mount#storage_resource_name}.
        :param tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#tenant_id Mount#tenant_id}.
        '''
        value = MountAdl(
            client_id=client_id,
            client_secret_key=client_secret_key,
            client_secret_scope=client_secret_scope,
            directory=directory,
            spark_conf_prefix=spark_conf_prefix,
            storage_resource_name=storage_resource_name,
            tenant_id=tenant_id,
        )

        return typing.cast(None, jsii.invoke(self, "putAdl", [value]))

    @jsii.member(jsii_name="putGs")
    def put_gs(
        self,
        *,
        bucket_name: builtins.str,
        service_account: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#bucket_name Mount#bucket_name}.
        :param service_account: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#service_account Mount#service_account}.
        '''
        value = MountGs(bucket_name=bucket_name, service_account=service_account)

        return typing.cast(None, jsii.invoke(self, "putGs", [value]))

    @jsii.member(jsii_name="putS3")
    def put_s3(
        self,
        *,
        bucket_name: builtins.str,
        instance_profile: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#bucket_name Mount#bucket_name}.
        :param instance_profile: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#instance_profile Mount#instance_profile}.
        '''
        value = MountS3(bucket_name=bucket_name, instance_profile=instance_profile)

        return typing.cast(None, jsii.invoke(self, "putS3", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, default: typing.Optional[builtins.str] = None) -> None:
        '''
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#default Mount#default}.
        '''
        value = MountTimeouts(default=default)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putWasb")
    def put_wasb(
        self,
        *,
        auth_type: builtins.str,
        token_secret_key: builtins.str,
        token_secret_scope: builtins.str,
        container_name: typing.Optional[builtins.str] = None,
        directory: typing.Optional[builtins.str] = None,
        storage_account_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#auth_type Mount#auth_type}.
        :param token_secret_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#token_secret_key Mount#token_secret_key}.
        :param token_secret_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#token_secret_scope Mount#token_secret_scope}.
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#container_name Mount#container_name}.
        :param directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#directory Mount#directory}.
        :param storage_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#storage_account_name Mount#storage_account_name}.
        '''
        value = MountWasb(
            auth_type=auth_type,
            token_secret_key=token_secret_key,
            token_secret_scope=token_secret_scope,
            container_name=container_name,
            directory=directory,
            storage_account_name=storage_account_name,
        )

        return typing.cast(None, jsii.invoke(self, "putWasb", [value]))

    @jsii.member(jsii_name="resetAbfs")
    def reset_abfs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAbfs", []))

    @jsii.member(jsii_name="resetAdl")
    def reset_adl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdl", []))

    @jsii.member(jsii_name="resetClusterId")
    def reset_cluster_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterId", []))

    @jsii.member(jsii_name="resetEncryptionType")
    def reset_encryption_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionType", []))

    @jsii.member(jsii_name="resetExtraConfigs")
    def reset_extra_configs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtraConfigs", []))

    @jsii.member(jsii_name="resetGs")
    def reset_gs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGs", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetResourceId")
    def reset_resource_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceId", []))

    @jsii.member(jsii_name="resetS3")
    def reset_s3(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetUri")
    def reset_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUri", []))

    @jsii.member(jsii_name="resetWasb")
    def reset_wasb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWasb", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="abfs")
    def abfs(self) -> "MountAbfsOutputReference":
        return typing.cast("MountAbfsOutputReference", jsii.get(self, "abfs"))

    @builtins.property
    @jsii.member(jsii_name="adl")
    def adl(self) -> "MountAdlOutputReference":
        return typing.cast("MountAdlOutputReference", jsii.get(self, "adl"))

    @builtins.property
    @jsii.member(jsii_name="gs")
    def gs(self) -> "MountGsOutputReference":
        return typing.cast("MountGsOutputReference", jsii.get(self, "gs"))

    @builtins.property
    @jsii.member(jsii_name="s3")
    def s3(self) -> "MountS3OutputReference":
        return typing.cast("MountS3OutputReference", jsii.get(self, "s3"))

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "MountTimeoutsOutputReference":
        return typing.cast("MountTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="wasb")
    def wasb(self) -> "MountWasbOutputReference":
        return typing.cast("MountWasbOutputReference", jsii.get(self, "wasb"))

    @builtins.property
    @jsii.member(jsii_name="abfsInput")
    def abfs_input(self) -> typing.Optional["MountAbfs"]:
        return typing.cast(typing.Optional["MountAbfs"], jsii.get(self, "abfsInput"))

    @builtins.property
    @jsii.member(jsii_name="adlInput")
    def adl_input(self) -> typing.Optional["MountAdl"]:
        return typing.cast(typing.Optional["MountAdl"], jsii.get(self, "adlInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterIdInput")
    def cluster_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionTypeInput")
    def encryption_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="extraConfigsInput")
    def extra_configs_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "extraConfigsInput"))

    @builtins.property
    @jsii.member(jsii_name="gsInput")
    def gs_input(self) -> typing.Optional["MountGs"]:
        return typing.cast(typing.Optional["MountGs"], jsii.get(self, "gsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceIdInput")
    def resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="s3Input")
    def s3_input(self) -> typing.Optional["MountS3"]:
        return typing.cast(typing.Optional["MountS3"], jsii.get(self, "s3Input"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["MountTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["MountTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="uriInput")
    def uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uriInput"))

    @builtins.property
    @jsii.member(jsii_name="wasbInput")
    def wasb_input(self) -> typing.Optional["MountWasb"]:
        return typing.cast(typing.Optional["MountWasb"], jsii.get(self, "wasbInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterId")
    def cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterId"))

    @cluster_id.setter
    def cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Mount, "cluster_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterId", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionType")
    def encryption_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encryptionType"))

    @encryption_type.setter
    def encryption_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Mount, "encryption_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionType", value)

    @builtins.property
    @jsii.member(jsii_name="extraConfigs")
    def extra_configs(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "extraConfigs"))

    @extra_configs.setter
    def extra_configs(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Mount, "extra_configs").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extraConfigs", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Mount, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Mount, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceId"))

    @resource_id.setter
    def resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Mount, "resource_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceId", value)

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Mount, "uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.mount.MountAbfs",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret_key": "clientSecretKey",
        "client_secret_scope": "clientSecretScope",
        "initialize_file_system": "initializeFileSystem",
        "container_name": "containerName",
        "directory": "directory",
        "storage_account_name": "storageAccountName",
        "tenant_id": "tenantId",
    },
)
class MountAbfs:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret_key: builtins.str,
        client_secret_scope: builtins.str,
        initialize_file_system: typing.Union[builtins.bool, cdktf.IResolvable],
        container_name: typing.Optional[builtins.str] = None,
        directory: typing.Optional[builtins.str] = None,
        storage_account_name: typing.Optional[builtins.str] = None,
        tenant_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_id Mount#client_id}.
        :param client_secret_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_secret_key Mount#client_secret_key}.
        :param client_secret_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_secret_scope Mount#client_secret_scope}.
        :param initialize_file_system: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#initialize_file_system Mount#initialize_file_system}.
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#container_name Mount#container_name}.
        :param directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#directory Mount#directory}.
        :param storage_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#storage_account_name Mount#storage_account_name}.
        :param tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#tenant_id Mount#tenant_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MountAbfs.__init__)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret_key", value=client_secret_key, expected_type=type_hints["client_secret_key"])
            check_type(argname="argument client_secret_scope", value=client_secret_scope, expected_type=type_hints["client_secret_scope"])
            check_type(argname="argument initialize_file_system", value=initialize_file_system, expected_type=type_hints["initialize_file_system"])
            check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
            check_type(argname="argument directory", value=directory, expected_type=type_hints["directory"])
            check_type(argname="argument storage_account_name", value=storage_account_name, expected_type=type_hints["storage_account_name"])
            check_type(argname="argument tenant_id", value=tenant_id, expected_type=type_hints["tenant_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "client_id": client_id,
            "client_secret_key": client_secret_key,
            "client_secret_scope": client_secret_scope,
            "initialize_file_system": initialize_file_system,
        }
        if container_name is not None:
            self._values["container_name"] = container_name
        if directory is not None:
            self._values["directory"] = directory
        if storage_account_name is not None:
            self._values["storage_account_name"] = storage_account_name
        if tenant_id is not None:
            self._values["tenant_id"] = tenant_id

    @builtins.property
    def client_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_id Mount#client_id}.'''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_secret_key Mount#client_secret_key}.'''
        result = self._values.get("client_secret_key")
        assert result is not None, "Required property 'client_secret_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret_scope(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_secret_scope Mount#client_secret_scope}.'''
        result = self._values.get("client_secret_scope")
        assert result is not None, "Required property 'client_secret_scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def initialize_file_system(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#initialize_file_system Mount#initialize_file_system}.'''
        result = self._values.get("initialize_file_system")
        assert result is not None, "Required property 'initialize_file_system' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def container_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#container_name Mount#container_name}.'''
        result = self._values.get("container_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def directory(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#directory Mount#directory}.'''
        result = self._values.get("directory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_account_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#storage_account_name Mount#storage_account_name}.'''
        result = self._values.get("storage_account_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tenant_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#tenant_id Mount#tenant_id}.'''
        result = self._values.get("tenant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MountAbfs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MountAbfsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.mount.MountAbfsOutputReference",
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
            type_hints = typing.get_type_hints(MountAbfsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetContainerName")
    def reset_container_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerName", []))

    @jsii.member(jsii_name="resetDirectory")
    def reset_directory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDirectory", []))

    @jsii.member(jsii_name="resetStorageAccountName")
    def reset_storage_account_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageAccountName", []))

    @jsii.member(jsii_name="resetTenantId")
    def reset_tenant_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTenantId", []))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretKeyInput")
    def client_secret_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretScopeInput")
    def client_secret_scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretScopeInput"))

    @builtins.property
    @jsii.member(jsii_name="containerNameInput")
    def container_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="directoryInput")
    def directory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directoryInput"))

    @builtins.property
    @jsii.member(jsii_name="initializeFileSystemInput")
    def initialize_file_system_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "initializeFileSystemInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountNameInput")
    def storage_account_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tenantIdInput")
    def tenant_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenantIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MountAbfsOutputReference, "client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretKey")
    def client_secret_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretKey"))

    @client_secret_key.setter
    def client_secret_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MountAbfsOutputReference, "client_secret_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretKey", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretScope")
    def client_secret_scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretScope"))

    @client_secret_scope.setter
    def client_secret_scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MountAbfsOutputReference, "client_secret_scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretScope", value)

    @builtins.property
    @jsii.member(jsii_name="containerName")
    def container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerName"))

    @container_name.setter
    def container_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MountAbfsOutputReference, "container_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerName", value)

    @builtins.property
    @jsii.member(jsii_name="directory")
    def directory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directory"))

    @directory.setter
    def directory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MountAbfsOutputReference, "directory").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directory", value)

    @builtins.property
    @jsii.member(jsii_name="initializeFileSystem")
    def initialize_file_system(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "initializeFileSystem"))

    @initialize_file_system.setter
    def initialize_file_system(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MountAbfsOutputReference, "initialize_file_system").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initializeFileSystem", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountName")
    def storage_account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountName"))

    @storage_account_name.setter
    def storage_account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MountAbfsOutputReference, "storage_account_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountName", value)

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @tenant_id.setter
    def tenant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MountAbfsOutputReference, "tenant_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenantId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MountAbfs]:
        return typing.cast(typing.Optional[MountAbfs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MountAbfs]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MountAbfsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.mount.MountAdl",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret_key": "clientSecretKey",
        "client_secret_scope": "clientSecretScope",
        "directory": "directory",
        "spark_conf_prefix": "sparkConfPrefix",
        "storage_resource_name": "storageResourceName",
        "tenant_id": "tenantId",
    },
)
class MountAdl:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret_key: builtins.str,
        client_secret_scope: builtins.str,
        directory: typing.Optional[builtins.str] = None,
        spark_conf_prefix: typing.Optional[builtins.str] = None,
        storage_resource_name: typing.Optional[builtins.str] = None,
        tenant_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_id Mount#client_id}.
        :param client_secret_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_secret_key Mount#client_secret_key}.
        :param client_secret_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_secret_scope Mount#client_secret_scope}.
        :param directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#directory Mount#directory}.
        :param spark_conf_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#spark_conf_prefix Mount#spark_conf_prefix}.
        :param storage_resource_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#storage_resource_name Mount#storage_resource_name}.
        :param tenant_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#tenant_id Mount#tenant_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MountAdl.__init__)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret_key", value=client_secret_key, expected_type=type_hints["client_secret_key"])
            check_type(argname="argument client_secret_scope", value=client_secret_scope, expected_type=type_hints["client_secret_scope"])
            check_type(argname="argument directory", value=directory, expected_type=type_hints["directory"])
            check_type(argname="argument spark_conf_prefix", value=spark_conf_prefix, expected_type=type_hints["spark_conf_prefix"])
            check_type(argname="argument storage_resource_name", value=storage_resource_name, expected_type=type_hints["storage_resource_name"])
            check_type(argname="argument tenant_id", value=tenant_id, expected_type=type_hints["tenant_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "client_id": client_id,
            "client_secret_key": client_secret_key,
            "client_secret_scope": client_secret_scope,
        }
        if directory is not None:
            self._values["directory"] = directory
        if spark_conf_prefix is not None:
            self._values["spark_conf_prefix"] = spark_conf_prefix
        if storage_resource_name is not None:
            self._values["storage_resource_name"] = storage_resource_name
        if tenant_id is not None:
            self._values["tenant_id"] = tenant_id

    @builtins.property
    def client_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_id Mount#client_id}.'''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_secret_key Mount#client_secret_key}.'''
        result = self._values.get("client_secret_key")
        assert result is not None, "Required property 'client_secret_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret_scope(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#client_secret_scope Mount#client_secret_scope}.'''
        result = self._values.get("client_secret_scope")
        assert result is not None, "Required property 'client_secret_scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def directory(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#directory Mount#directory}.'''
        result = self._values.get("directory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spark_conf_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#spark_conf_prefix Mount#spark_conf_prefix}.'''
        result = self._values.get("spark_conf_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_resource_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#storage_resource_name Mount#storage_resource_name}.'''
        result = self._values.get("storage_resource_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tenant_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#tenant_id Mount#tenant_id}.'''
        result = self._values.get("tenant_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MountAdl(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MountAdlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.mount.MountAdlOutputReference",
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
            type_hints = typing.get_type_hints(MountAdlOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDirectory")
    def reset_directory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDirectory", []))

    @jsii.member(jsii_name="resetSparkConfPrefix")
    def reset_spark_conf_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSparkConfPrefix", []))

    @jsii.member(jsii_name="resetStorageResourceName")
    def reset_storage_resource_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageResourceName", []))

    @jsii.member(jsii_name="resetTenantId")
    def reset_tenant_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTenantId", []))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretKeyInput")
    def client_secret_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretScopeInput")
    def client_secret_scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretScopeInput"))

    @builtins.property
    @jsii.member(jsii_name="directoryInput")
    def directory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directoryInput"))

    @builtins.property
    @jsii.member(jsii_name="sparkConfPrefixInput")
    def spark_conf_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sparkConfPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="storageResourceNameInput")
    def storage_resource_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageResourceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tenantIdInput")
    def tenant_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenantIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MountAdlOutputReference, "client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretKey")
    def client_secret_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretKey"))

    @client_secret_key.setter
    def client_secret_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MountAdlOutputReference, "client_secret_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretKey", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecretScope")
    def client_secret_scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecretScope"))

    @client_secret_scope.setter
    def client_secret_scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MountAdlOutputReference, "client_secret_scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecretScope", value)

    @builtins.property
    @jsii.member(jsii_name="directory")
    def directory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directory"))

    @directory.setter
    def directory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MountAdlOutputReference, "directory").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directory", value)

    @builtins.property
    @jsii.member(jsii_name="sparkConfPrefix")
    def spark_conf_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sparkConfPrefix"))

    @spark_conf_prefix.setter
    def spark_conf_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MountAdlOutputReference, "spark_conf_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sparkConfPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="storageResourceName")
    def storage_resource_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageResourceName"))

    @storage_resource_name.setter
    def storage_resource_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MountAdlOutputReference, "storage_resource_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageResourceName", value)

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @tenant_id.setter
    def tenant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MountAdlOutputReference, "tenant_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenantId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MountAdl]:
        return typing.cast(typing.Optional[MountAdl], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MountAdl]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MountAdlOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.mount.MountConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "abfs": "abfs",
        "adl": "adl",
        "cluster_id": "clusterId",
        "encryption_type": "encryptionType",
        "extra_configs": "extraConfigs",
        "gs": "gs",
        "id": "id",
        "name": "name",
        "resource_id": "resourceId",
        "s3": "s3",
        "timeouts": "timeouts",
        "uri": "uri",
        "wasb": "wasb",
    },
)
class MountConfig(cdktf.TerraformMetaArguments):
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
        abfs: typing.Optional[typing.Union[MountAbfs, typing.Dict[str, typing.Any]]] = None,
        adl: typing.Optional[typing.Union[MountAdl, typing.Dict[str, typing.Any]]] = None,
        cluster_id: typing.Optional[builtins.str] = None,
        encryption_type: typing.Optional[builtins.str] = None,
        extra_configs: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        gs: typing.Optional[typing.Union["MountGs", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        resource_id: typing.Optional[builtins.str] = None,
        s3: typing.Optional[typing.Union["MountS3", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["MountTimeouts", typing.Dict[str, typing.Any]]] = None,
        uri: typing.Optional[builtins.str] = None,
        wasb: typing.Optional[typing.Union["MountWasb", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param abfs: abfs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#abfs Mount#abfs}
        :param adl: adl block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#adl Mount#adl}
        :param cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#cluster_id Mount#cluster_id}.
        :param encryption_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#encryption_type Mount#encryption_type}.
        :param extra_configs: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#extra_configs Mount#extra_configs}.
        :param gs: gs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#gs Mount#gs}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#id Mount#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#name Mount#name}.
        :param resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#resource_id Mount#resource_id}.
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#s3 Mount#s3}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#timeouts Mount#timeouts}
        :param uri: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#uri Mount#uri}.
        :param wasb: wasb block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#wasb Mount#wasb}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(abfs, dict):
            abfs = MountAbfs(**abfs)
        if isinstance(adl, dict):
            adl = MountAdl(**adl)
        if isinstance(gs, dict):
            gs = MountGs(**gs)
        if isinstance(s3, dict):
            s3 = MountS3(**s3)
        if isinstance(timeouts, dict):
            timeouts = MountTimeouts(**timeouts)
        if isinstance(wasb, dict):
            wasb = MountWasb(**wasb)
        if __debug__:
            type_hints = typing.get_type_hints(MountConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument abfs", value=abfs, expected_type=type_hints["abfs"])
            check_type(argname="argument adl", value=adl, expected_type=type_hints["adl"])
            check_type(argname="argument cluster_id", value=cluster_id, expected_type=type_hints["cluster_id"])
            check_type(argname="argument encryption_type", value=encryption_type, expected_type=type_hints["encryption_type"])
            check_type(argname="argument extra_configs", value=extra_configs, expected_type=type_hints["extra_configs"])
            check_type(argname="argument gs", value=gs, expected_type=type_hints["gs"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
            check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
            check_type(argname="argument wasb", value=wasb, expected_type=type_hints["wasb"])
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
        if abfs is not None:
            self._values["abfs"] = abfs
        if adl is not None:
            self._values["adl"] = adl
        if cluster_id is not None:
            self._values["cluster_id"] = cluster_id
        if encryption_type is not None:
            self._values["encryption_type"] = encryption_type
        if extra_configs is not None:
            self._values["extra_configs"] = extra_configs
        if gs is not None:
            self._values["gs"] = gs
        if id is not None:
            self._values["id"] = id
        if name is not None:
            self._values["name"] = name
        if resource_id is not None:
            self._values["resource_id"] = resource_id
        if s3 is not None:
            self._values["s3"] = s3
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if uri is not None:
            self._values["uri"] = uri
        if wasb is not None:
            self._values["wasb"] = wasb

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
    def abfs(self) -> typing.Optional[MountAbfs]:
        '''abfs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#abfs Mount#abfs}
        '''
        result = self._values.get("abfs")
        return typing.cast(typing.Optional[MountAbfs], result)

    @builtins.property
    def adl(self) -> typing.Optional[MountAdl]:
        '''adl block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#adl Mount#adl}
        '''
        result = self._values.get("adl")
        return typing.cast(typing.Optional[MountAdl], result)

    @builtins.property
    def cluster_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#cluster_id Mount#cluster_id}.'''
        result = self._values.get("cluster_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#encryption_type Mount#encryption_type}.'''
        result = self._values.get("encryption_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extra_configs(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#extra_configs Mount#extra_configs}.'''
        result = self._values.get("extra_configs")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def gs(self) -> typing.Optional["MountGs"]:
        '''gs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#gs Mount#gs}
        '''
        result = self._values.get("gs")
        return typing.cast(typing.Optional["MountGs"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#id Mount#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#name Mount#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#resource_id Mount#resource_id}.'''
        result = self._values.get("resource_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3(self) -> typing.Optional["MountS3"]:
        '''s3 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#s3 Mount#s3}
        '''
        result = self._values.get("s3")
        return typing.cast(typing.Optional["MountS3"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["MountTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#timeouts Mount#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["MountTimeouts"], result)

    @builtins.property
    def uri(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#uri Mount#uri}.'''
        result = self._values.get("uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wasb(self) -> typing.Optional["MountWasb"]:
        '''wasb block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#wasb Mount#wasb}
        '''
        result = self._values.get("wasb")
        return typing.cast(typing.Optional["MountWasb"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MountConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.mount.MountGs",
    jsii_struct_bases=[],
    name_mapping={"bucket_name": "bucketName", "service_account": "serviceAccount"},
)
class MountGs:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        service_account: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#bucket_name Mount#bucket_name}.
        :param service_account: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#service_account Mount#service_account}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MountGs.__init__)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument service_account", value=service_account, expected_type=type_hints["service_account"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket_name": bucket_name,
        }
        if service_account is not None:
            self._values["service_account"] = service_account

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#bucket_name Mount#bucket_name}.'''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_account(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#service_account Mount#service_account}.'''
        result = self._values.get("service_account")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MountGs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MountGsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.mount.MountGsOutputReference",
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
            type_hints = typing.get_type_hints(MountGsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetServiceAccount")
    def reset_service_account(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceAccount", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceAccountInput")
    def service_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MountGsOutputReference, "bucket_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="serviceAccount")
    def service_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccount"))

    @service_account.setter
    def service_account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MountGsOutputReference, "service_account").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceAccount", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MountGs]:
        return typing.cast(typing.Optional[MountGs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MountGs]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MountGsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.mount.MountS3",
    jsii_struct_bases=[],
    name_mapping={"bucket_name": "bucketName", "instance_profile": "instanceProfile"},
)
class MountS3:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        instance_profile: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#bucket_name Mount#bucket_name}.
        :param instance_profile: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#instance_profile Mount#instance_profile}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MountS3.__init__)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument instance_profile", value=instance_profile, expected_type=type_hints["instance_profile"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket_name": bucket_name,
        }
        if instance_profile is not None:
            self._values["instance_profile"] = instance_profile

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#bucket_name Mount#bucket_name}.'''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_profile(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#instance_profile Mount#instance_profile}.'''
        result = self._values.get("instance_profile")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MountS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MountS3OutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.mount.MountS3OutputReference",
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
            type_hints = typing.get_type_hints(MountS3OutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetInstanceProfile")
    def reset_instance_profile(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceProfile", []))

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceProfileInput")
    def instance_profile_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceProfileInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MountS3OutputReference, "bucket_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="instanceProfile")
    def instance_profile(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceProfile"))

    @instance_profile.setter
    def instance_profile(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MountS3OutputReference, "instance_profile").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceProfile", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MountS3]:
        return typing.cast(typing.Optional[MountS3], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MountS3]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MountS3OutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.mount.MountTimeouts",
    jsii_struct_bases=[],
    name_mapping={"default": "default"},
)
class MountTimeouts:
    def __init__(self, *, default: typing.Optional[builtins.str] = None) -> None:
        '''
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#default Mount#default}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MountTimeouts.__init__)
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
        self._values: typing.Dict[str, typing.Any] = {}
        if default is not None:
            self._values["default"] = default

    @builtins.property
    def default(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#default Mount#default}.'''
        result = self._values.get("default")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MountTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MountTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.mount.MountTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(MountTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDefault")
    def reset_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefault", []))

    @builtins.property
    @jsii.member(jsii_name="defaultInput")
    def default_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultInput"))

    @builtins.property
    @jsii.member(jsii_name="default")
    def default(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "default"))

    @default.setter
    def default(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MountTimeoutsOutputReference, "default").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[MountTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[MountTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[MountTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MountTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.mount.MountWasb",
    jsii_struct_bases=[],
    name_mapping={
        "auth_type": "authType",
        "token_secret_key": "tokenSecretKey",
        "token_secret_scope": "tokenSecretScope",
        "container_name": "containerName",
        "directory": "directory",
        "storage_account_name": "storageAccountName",
    },
)
class MountWasb:
    def __init__(
        self,
        *,
        auth_type: builtins.str,
        token_secret_key: builtins.str,
        token_secret_scope: builtins.str,
        container_name: typing.Optional[builtins.str] = None,
        directory: typing.Optional[builtins.str] = None,
        storage_account_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auth_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#auth_type Mount#auth_type}.
        :param token_secret_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#token_secret_key Mount#token_secret_key}.
        :param token_secret_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#token_secret_scope Mount#token_secret_scope}.
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#container_name Mount#container_name}.
        :param directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#directory Mount#directory}.
        :param storage_account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#storage_account_name Mount#storage_account_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MountWasb.__init__)
            check_type(argname="argument auth_type", value=auth_type, expected_type=type_hints["auth_type"])
            check_type(argname="argument token_secret_key", value=token_secret_key, expected_type=type_hints["token_secret_key"])
            check_type(argname="argument token_secret_scope", value=token_secret_scope, expected_type=type_hints["token_secret_scope"])
            check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
            check_type(argname="argument directory", value=directory, expected_type=type_hints["directory"])
            check_type(argname="argument storage_account_name", value=storage_account_name, expected_type=type_hints["storage_account_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "auth_type": auth_type,
            "token_secret_key": token_secret_key,
            "token_secret_scope": token_secret_scope,
        }
        if container_name is not None:
            self._values["container_name"] = container_name
        if directory is not None:
            self._values["directory"] = directory
        if storage_account_name is not None:
            self._values["storage_account_name"] = storage_account_name

    @builtins.property
    def auth_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#auth_type Mount#auth_type}.'''
        result = self._values.get("auth_type")
        assert result is not None, "Required property 'auth_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def token_secret_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#token_secret_key Mount#token_secret_key}.'''
        result = self._values.get("token_secret_key")
        assert result is not None, "Required property 'token_secret_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def token_secret_scope(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#token_secret_scope Mount#token_secret_scope}.'''
        result = self._values.get("token_secret_scope")
        assert result is not None, "Required property 'token_secret_scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#container_name Mount#container_name}.'''
        result = self._values.get("container_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def directory(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#directory Mount#directory}.'''
        result = self._values.get("directory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_account_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/mount#storage_account_name Mount#storage_account_name}.'''
        result = self._values.get("storage_account_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MountWasb(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MountWasbOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.mount.MountWasbOutputReference",
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
            type_hints = typing.get_type_hints(MountWasbOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetContainerName")
    def reset_container_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerName", []))

    @jsii.member(jsii_name="resetDirectory")
    def reset_directory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDirectory", []))

    @jsii.member(jsii_name="resetStorageAccountName")
    def reset_storage_account_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageAccountName", []))

    @builtins.property
    @jsii.member(jsii_name="authTypeInput")
    def auth_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="containerNameInput")
    def container_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="directoryInput")
    def directory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directoryInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountNameInput")
    def storage_account_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountNameInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenSecretKeyInput")
    def token_secret_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenSecretKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenSecretScopeInput")
    def token_secret_scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenSecretScopeInput"))

    @builtins.property
    @jsii.member(jsii_name="authType")
    def auth_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authType"))

    @auth_type.setter
    def auth_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MountWasbOutputReference, "auth_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authType", value)

    @builtins.property
    @jsii.member(jsii_name="containerName")
    def container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerName"))

    @container_name.setter
    def container_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MountWasbOutputReference, "container_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerName", value)

    @builtins.property
    @jsii.member(jsii_name="directory")
    def directory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directory"))

    @directory.setter
    def directory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MountWasbOutputReference, "directory").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directory", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountName")
    def storage_account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountName"))

    @storage_account_name.setter
    def storage_account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MountWasbOutputReference, "storage_account_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountName", value)

    @builtins.property
    @jsii.member(jsii_name="tokenSecretKey")
    def token_secret_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenSecretKey"))

    @token_secret_key.setter
    def token_secret_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MountWasbOutputReference, "token_secret_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenSecretKey", value)

    @builtins.property
    @jsii.member(jsii_name="tokenSecretScope")
    def token_secret_scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenSecretScope"))

    @token_secret_scope.setter
    def token_secret_scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MountWasbOutputReference, "token_secret_scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenSecretScope", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MountWasb]:
        return typing.cast(typing.Optional[MountWasb], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[MountWasb]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MountWasbOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Mount",
    "MountAbfs",
    "MountAbfsOutputReference",
    "MountAdl",
    "MountAdlOutputReference",
    "MountConfig",
    "MountGs",
    "MountGsOutputReference",
    "MountS3",
    "MountS3OutputReference",
    "MountTimeouts",
    "MountTimeoutsOutputReference",
    "MountWasb",
    "MountWasbOutputReference",
]

publication.publish()
