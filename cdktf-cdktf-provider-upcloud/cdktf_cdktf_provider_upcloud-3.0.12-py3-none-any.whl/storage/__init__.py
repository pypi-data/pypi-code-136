'''
# `upcloud_storage`

Refer to the Terraform Registory for docs: [`upcloud_storage`](https://www.terraform.io/docs/providers/upcloud/r/storage).
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


class Storage(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.storage.Storage",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/upcloud/r/storage upcloud_storage}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        size: jsii.Number,
        title: builtins.str,
        zone: builtins.str,
        backup_rule: typing.Optional[typing.Union["StorageBackupRule", typing.Dict[str, typing.Any]]] = None,
        clone: typing.Optional[typing.Union["StorageClone", typing.Dict[str, typing.Any]]] = None,
        delete_autoresize_backup: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        filesystem_autoresize: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        import_: typing.Optional[typing.Union["StorageImport", typing.Dict[str, typing.Any]]] = None,
        tier: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/upcloud/r/storage upcloud_storage} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param size: The size of the storage in gigabytes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#size Storage#size}
        :param title: A short, informative description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#title Storage#title}
        :param zone: The zone in which the storage will be created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#zone Storage#zone}
        :param backup_rule: backup_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#backup_rule Storage#backup_rule}
        :param clone: clone block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#clone Storage#clone}
        :param delete_autoresize_backup: If set to true, the backup taken before the partition and filesystem resize attempt will be deleted immediately after success. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#delete_autoresize_backup Storage#delete_autoresize_backup}
        :param filesystem_autoresize: If set to true, provider will attempt to resize partition and filesystem when the size of the storage changes. Please note that before the resize attempt is made, backup of the storage will be taken. If the resize attempt fails, the backup will be used to restore the storage and then deleted. If the resize attempt succeeds, backup will be kept (unless delete_autoresize_backup option is set to true). Taking and keeping backups incure costs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#filesystem_autoresize Storage#filesystem_autoresize}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#id Storage#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param import_: import block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#import Storage#import}
        :param tier: The storage tier to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#tier Storage#tier}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Storage.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = StorageConfig(
            size=size,
            title=title,
            zone=zone,
            backup_rule=backup_rule,
            clone=clone,
            delete_autoresize_backup=delete_autoresize_backup,
            filesystem_autoresize=filesystem_autoresize,
            id=id,
            import_=import_,
            tier=tier,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putBackupRule")
    def put_backup_rule(
        self,
        *,
        interval: builtins.str,
        retention: jsii.Number,
        time: builtins.str,
    ) -> None:
        '''
        :param interval: The weekday when the backup is created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#interval Storage#interval}
        :param retention: The number of days before a backup is automatically deleted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#retention Storage#retention}
        :param time: The time of day when the backup is created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#time Storage#time}
        '''
        value = StorageBackupRule(interval=interval, retention=retention, time=time)

        return typing.cast(None, jsii.invoke(self, "putBackupRule", [value]))

    @jsii.member(jsii_name="putClone")
    def put_clone(self, *, id: builtins.str) -> None:
        '''
        :param id: The unique identifier of the storage/template to clone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#id Storage#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        value = StorageClone(id=id)

        return typing.cast(None, jsii.invoke(self, "putClone", [value]))

    @jsii.member(jsii_name="putImport")
    def put_import(
        self,
        *,
        source: builtins.str,
        source_location: builtins.str,
        source_hash: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param source: The mode of the import task. One of ``http_import`` or ``direct_upload``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#source Storage#source}
        :param source_location: The location of the file to import. For ``http_import`` an accessible URL for ``direct_upload`` a local file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#source_location Storage#source_location}
        :param source_hash: For ``direct_upload``; an optional hash of the file to upload. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#source_hash Storage#source_hash}
        '''
        value = StorageImport(
            source=source, source_location=source_location, source_hash=source_hash
        )

        return typing.cast(None, jsii.invoke(self, "putImport", [value]))

    @jsii.member(jsii_name="resetBackupRule")
    def reset_backup_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackupRule", []))

    @jsii.member(jsii_name="resetClone")
    def reset_clone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClone", []))

    @jsii.member(jsii_name="resetDeleteAutoresizeBackup")
    def reset_delete_autoresize_backup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeleteAutoresizeBackup", []))

    @jsii.member(jsii_name="resetFilesystemAutoresize")
    def reset_filesystem_autoresize(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilesystemAutoresize", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetImport")
    def reset_import(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImport", []))

    @jsii.member(jsii_name="resetTier")
    def reset_tier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTier", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="backupRule")
    def backup_rule(self) -> "StorageBackupRuleOutputReference":
        return typing.cast("StorageBackupRuleOutputReference", jsii.get(self, "backupRule"))

    @builtins.property
    @jsii.member(jsii_name="clone")
    def clone(self) -> "StorageCloneOutputReference":
        return typing.cast("StorageCloneOutputReference", jsii.get(self, "clone"))

    @builtins.property
    @jsii.member(jsii_name="import")
    def import_(self) -> "StorageImportOutputReference":
        return typing.cast("StorageImportOutputReference", jsii.get(self, "import"))

    @builtins.property
    @jsii.member(jsii_name="backupRuleInput")
    def backup_rule_input(self) -> typing.Optional["StorageBackupRule"]:
        return typing.cast(typing.Optional["StorageBackupRule"], jsii.get(self, "backupRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="cloneInput")
    def clone_input(self) -> typing.Optional["StorageClone"]:
        return typing.cast(typing.Optional["StorageClone"], jsii.get(self, "cloneInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteAutoresizeBackupInput")
    def delete_autoresize_backup_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deleteAutoresizeBackupInput"))

    @builtins.property
    @jsii.member(jsii_name="filesystemAutoresizeInput")
    def filesystem_autoresize_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "filesystemAutoresizeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="importInput")
    def import_input(self) -> typing.Optional["StorageImport"]:
        return typing.cast(typing.Optional["StorageImport"], jsii.get(self, "importInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeInput")
    def size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeInput"))

    @builtins.property
    @jsii.member(jsii_name="tierInput")
    def tier_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tierInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneInput")
    def zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteAutoresizeBackup")
    def delete_autoresize_backup(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "deleteAutoresizeBackup"))

    @delete_autoresize_backup.setter
    def delete_autoresize_backup(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Storage, "delete_autoresize_backup").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteAutoresizeBackup", value)

    @builtins.property
    @jsii.member(jsii_name="filesystemAutoresize")
    def filesystem_autoresize(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "filesystemAutoresize"))

    @filesystem_autoresize.setter
    def filesystem_autoresize(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Storage, "filesystem_autoresize").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filesystemAutoresize", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Storage, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "size"))

    @size.setter
    def size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Storage, "size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="tier")
    def tier(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tier"))

    @tier.setter
    def tier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Storage, "tier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tier", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Storage, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="zone")
    def zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zone"))

    @zone.setter
    def zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Storage, "zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zone", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.storage.StorageBackupRule",
    jsii_struct_bases=[],
    name_mapping={"interval": "interval", "retention": "retention", "time": "time"},
)
class StorageBackupRule:
    def __init__(
        self,
        *,
        interval: builtins.str,
        retention: jsii.Number,
        time: builtins.str,
    ) -> None:
        '''
        :param interval: The weekday when the backup is created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#interval Storage#interval}
        :param retention: The number of days before a backup is automatically deleted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#retention Storage#retention}
        :param time: The time of day when the backup is created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#time Storage#time}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageBackupRule.__init__)
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument retention", value=retention, expected_type=type_hints["retention"])
            check_type(argname="argument time", value=time, expected_type=type_hints["time"])
        self._values: typing.Dict[str, typing.Any] = {
            "interval": interval,
            "retention": retention,
            "time": time,
        }

    @builtins.property
    def interval(self) -> builtins.str:
        '''The weekday when the backup is created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#interval Storage#interval}
        '''
        result = self._values.get("interval")
        assert result is not None, "Required property 'interval' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def retention(self) -> jsii.Number:
        '''The number of days before a backup is automatically deleted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#retention Storage#retention}
        '''
        result = self._values.get("retention")
        assert result is not None, "Required property 'retention' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def time(self) -> builtins.str:
        '''The time of day when the backup is created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#time Storage#time}
        '''
        result = self._values.get("time")
        assert result is not None, "Required property 'time' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageBackupRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageBackupRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.storage.StorageBackupRuleOutputReference",
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
            type_hints = typing.get_type_hints(StorageBackupRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionInput")
    def retention_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionInput"))

    @builtins.property
    @jsii.member(jsii_name="timeInput")
    def time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "timeInput"))

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageBackupRuleOutputReference, "interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="retention")
    def retention(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retention"))

    @retention.setter
    def retention(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageBackupRuleOutputReference, "retention").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retention", value)

    @builtins.property
    @jsii.member(jsii_name="time")
    def time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "time"))

    @time.setter
    def time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageBackupRuleOutputReference, "time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "time", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[StorageBackupRule]:
        return typing.cast(typing.Optional[StorageBackupRule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[StorageBackupRule]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageBackupRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.storage.StorageClone",
    jsii_struct_bases=[],
    name_mapping={"id": "id"},
)
class StorageClone:
    def __init__(self, *, id: builtins.str) -> None:
        '''
        :param id: The unique identifier of the storage/template to clone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#id Storage#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageClone.__init__)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
        }

    @builtins.property
    def id(self) -> builtins.str:
        '''The unique identifier of the storage/template to clone.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#id Storage#id}

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageClone(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageCloneOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.storage.StorageCloneOutputReference",
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
            type_hints = typing.get_type_hints(StorageCloneOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageCloneOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[StorageClone]:
        return typing.cast(typing.Optional[StorageClone], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[StorageClone]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageCloneOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.storage.StorageConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "size": "size",
        "title": "title",
        "zone": "zone",
        "backup_rule": "backupRule",
        "clone": "clone",
        "delete_autoresize_backup": "deleteAutoresizeBackup",
        "filesystem_autoresize": "filesystemAutoresize",
        "id": "id",
        "import_": "import",
        "tier": "tier",
    },
)
class StorageConfig(cdktf.TerraformMetaArguments):
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
        size: jsii.Number,
        title: builtins.str,
        zone: builtins.str,
        backup_rule: typing.Optional[typing.Union[StorageBackupRule, typing.Dict[str, typing.Any]]] = None,
        clone: typing.Optional[typing.Union[StorageClone, typing.Dict[str, typing.Any]]] = None,
        delete_autoresize_backup: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        filesystem_autoresize: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        import_: typing.Optional[typing.Union["StorageImport", typing.Dict[str, typing.Any]]] = None,
        tier: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param size: The size of the storage in gigabytes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#size Storage#size}
        :param title: A short, informative description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#title Storage#title}
        :param zone: The zone in which the storage will be created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#zone Storage#zone}
        :param backup_rule: backup_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#backup_rule Storage#backup_rule}
        :param clone: clone block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#clone Storage#clone}
        :param delete_autoresize_backup: If set to true, the backup taken before the partition and filesystem resize attempt will be deleted immediately after success. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#delete_autoresize_backup Storage#delete_autoresize_backup}
        :param filesystem_autoresize: If set to true, provider will attempt to resize partition and filesystem when the size of the storage changes. Please note that before the resize attempt is made, backup of the storage will be taken. If the resize attempt fails, the backup will be used to restore the storage and then deleted. If the resize attempt succeeds, backup will be kept (unless delete_autoresize_backup option is set to true). Taking and keeping backups incure costs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#filesystem_autoresize Storage#filesystem_autoresize}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#id Storage#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param import_: import block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#import Storage#import}
        :param tier: The storage tier to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#tier Storage#tier}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(backup_rule, dict):
            backup_rule = StorageBackupRule(**backup_rule)
        if isinstance(clone, dict):
            clone = StorageClone(**clone)
        if isinstance(import_, dict):
            import_ = StorageImport(**import_)
        if __debug__:
            type_hints = typing.get_type_hints(StorageConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
            check_type(argname="argument backup_rule", value=backup_rule, expected_type=type_hints["backup_rule"])
            check_type(argname="argument clone", value=clone, expected_type=type_hints["clone"])
            check_type(argname="argument delete_autoresize_backup", value=delete_autoresize_backup, expected_type=type_hints["delete_autoresize_backup"])
            check_type(argname="argument filesystem_autoresize", value=filesystem_autoresize, expected_type=type_hints["filesystem_autoresize"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument import_", value=import_, expected_type=type_hints["import_"])
            check_type(argname="argument tier", value=tier, expected_type=type_hints["tier"])
        self._values: typing.Dict[str, typing.Any] = {
            "size": size,
            "title": title,
            "zone": zone,
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
        if backup_rule is not None:
            self._values["backup_rule"] = backup_rule
        if clone is not None:
            self._values["clone"] = clone
        if delete_autoresize_backup is not None:
            self._values["delete_autoresize_backup"] = delete_autoresize_backup
        if filesystem_autoresize is not None:
            self._values["filesystem_autoresize"] = filesystem_autoresize
        if id is not None:
            self._values["id"] = id
        if import_ is not None:
            self._values["import_"] = import_
        if tier is not None:
            self._values["tier"] = tier

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
    def size(self) -> jsii.Number:
        '''The size of the storage in gigabytes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#size Storage#size}
        '''
        result = self._values.get("size")
        assert result is not None, "Required property 'size' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def title(self) -> builtins.str:
        '''A short, informative description.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#title Storage#title}
        '''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def zone(self) -> builtins.str:
        '''The zone in which the storage will be created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#zone Storage#zone}
        '''
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def backup_rule(self) -> typing.Optional[StorageBackupRule]:
        '''backup_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#backup_rule Storage#backup_rule}
        '''
        result = self._values.get("backup_rule")
        return typing.cast(typing.Optional[StorageBackupRule], result)

    @builtins.property
    def clone(self) -> typing.Optional[StorageClone]:
        '''clone block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#clone Storage#clone}
        '''
        result = self._values.get("clone")
        return typing.cast(typing.Optional[StorageClone], result)

    @builtins.property
    def delete_autoresize_backup(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If set to true, the backup taken before the partition and filesystem resize attempt will be deleted immediately after success.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#delete_autoresize_backup Storage#delete_autoresize_backup}
        '''
        result = self._values.get("delete_autoresize_backup")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def filesystem_autoresize(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If set to true, provider will attempt to resize partition and filesystem when the size of the storage changes.

        Please note that before the resize attempt is made, backup of the storage will be taken. If the resize attempt fails, the backup will be used
        to restore the storage and then deleted. If the resize attempt succeeds, backup will be kept (unless delete_autoresize_backup option is set to true).
        Taking and keeping backups incure costs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#filesystem_autoresize Storage#filesystem_autoresize}
        '''
        result = self._values.get("filesystem_autoresize")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#id Storage#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def import_(self) -> typing.Optional["StorageImport"]:
        '''import block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#import Storage#import}
        '''
        result = self._values.get("import_")
        return typing.cast(typing.Optional["StorageImport"], result)

    @builtins.property
    def tier(self) -> typing.Optional[builtins.str]:
        '''The storage tier to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#tier Storage#tier}
        '''
        result = self._values.get("tier")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-upcloud.storage.StorageImport",
    jsii_struct_bases=[],
    name_mapping={
        "source": "source",
        "source_location": "sourceLocation",
        "source_hash": "sourceHash",
    },
)
class StorageImport:
    def __init__(
        self,
        *,
        source: builtins.str,
        source_location: builtins.str,
        source_hash: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param source: The mode of the import task. One of ``http_import`` or ``direct_upload``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#source Storage#source}
        :param source_location: The location of the file to import. For ``http_import`` an accessible URL for ``direct_upload`` a local file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#source_location Storage#source_location}
        :param source_hash: For ``direct_upload``; an optional hash of the file to upload. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#source_hash Storage#source_hash}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(StorageImport.__init__)
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument source_location", value=source_location, expected_type=type_hints["source_location"])
            check_type(argname="argument source_hash", value=source_hash, expected_type=type_hints["source_hash"])
        self._values: typing.Dict[str, typing.Any] = {
            "source": source,
            "source_location": source_location,
        }
        if source_hash is not None:
            self._values["source_hash"] = source_hash

    @builtins.property
    def source(self) -> builtins.str:
        '''The mode of the import task. One of ``http_import`` or ``direct_upload``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#source Storage#source}
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_location(self) -> builtins.str:
        '''The location of the file to import. For ``http_import`` an accessible URL for ``direct_upload`` a local file.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#source_location Storage#source_location}
        '''
        result = self._values.get("source_location")
        assert result is not None, "Required property 'source_location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_hash(self) -> typing.Optional[builtins.str]:
        '''For ``direct_upload``; an optional hash of the file to upload.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/upcloud/r/storage#source_hash Storage#source_hash}
        '''
        result = self._values.get("source_hash")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StorageImport(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class StorageImportOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-upcloud.storage.StorageImportOutputReference",
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
            type_hints = typing.get_type_hints(StorageImportOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetSourceHash")
    def reset_source_hash(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceHash", []))

    @builtins.property
    @jsii.member(jsii_name="sha256Sum")
    def sha256_sum(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sha256Sum"))

    @builtins.property
    @jsii.member(jsii_name="writtenBytes")
    def written_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "writtenBytes"))

    @builtins.property
    @jsii.member(jsii_name="sourceHashInput")
    def source_hash_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceHashInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceLocationInput")
    def source_location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageImportOutputReference, "source").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="sourceHash")
    def source_hash(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceHash"))

    @source_hash.setter
    def source_hash(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageImportOutputReference, "source_hash").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceHash", value)

    @builtins.property
    @jsii.member(jsii_name="sourceLocation")
    def source_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceLocation"))

    @source_location.setter
    def source_location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageImportOutputReference, "source_location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceLocation", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[StorageImport]:
        return typing.cast(typing.Optional[StorageImport], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[StorageImport]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(StorageImportOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Storage",
    "StorageBackupRule",
    "StorageBackupRuleOutputReference",
    "StorageClone",
    "StorageCloneOutputReference",
    "StorageConfig",
    "StorageImport",
    "StorageImportOutputReference",
]

publication.publish()
