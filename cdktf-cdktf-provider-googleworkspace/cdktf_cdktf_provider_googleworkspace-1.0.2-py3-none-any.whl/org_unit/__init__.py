'''
# `googleworkspace_org_unit`

Refer to the Terraform Registory for docs: [`googleworkspace_org_unit`](https://www.terraform.io/docs/providers/googleworkspace/r/org_unit).
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


class OrgUnit(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-googleworkspace.orgUnit.OrgUnit",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/googleworkspace/r/org_unit googleworkspace_org_unit}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        block_inheritance: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        parent_org_unit_id: typing.Optional[builtins.str] = None,
        parent_org_unit_path: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/googleworkspace/r/org_unit googleworkspace_org_unit} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The organizational unit's path name. For example, an organizational unit's name within the /corp/support/sales_support parent path is sales_support. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/org_unit#name OrgUnit#name}
        :param block_inheritance: Defaults to ``false``. Determines if a sub-organizational unit can inherit the settings of the parent organization. False means a sub-organizational unit inherits the settings of the nearest parent organizational unit. For more information on inheritance and users in an organization structure, see the `administration help center <https://support.google.com/a/answer/4352075>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/org_unit#block_inheritance OrgUnit#block_inheritance}
        :param description: Description of the organizational unit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/org_unit#description OrgUnit#description}
        :param parent_org_unit_id: The unique ID of the parent organizational unit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/org_unit#parent_org_unit_id OrgUnit#parent_org_unit_id}
        :param parent_org_unit_path: The organizational unit's parent path. For example, /corp/sales is the parent path for /corp/sales/sales_support organizational unit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/org_unit#parent_org_unit_path OrgUnit#parent_org_unit_path}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(OrgUnit.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = OrgUnitConfig(
            name=name,
            block_inheritance=block_inheritance,
            description=description,
            parent_org_unit_id=parent_org_unit_id,
            parent_org_unit_path=parent_org_unit_path,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetBlockInheritance")
    def reset_block_inheritance(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlockInheritance", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetParentOrgUnitId")
    def reset_parent_org_unit_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParentOrgUnitId", []))

    @jsii.member(jsii_name="resetParentOrgUnitPath")
    def reset_parent_org_unit_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParentOrgUnitPath", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="etag")
    def etag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "etag"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="orgUnitId")
    def org_unit_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "orgUnitId"))

    @builtins.property
    @jsii.member(jsii_name="orgUnitPath")
    def org_unit_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "orgUnitPath"))

    @builtins.property
    @jsii.member(jsii_name="blockInheritanceInput")
    def block_inheritance_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "blockInheritanceInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="parentOrgUnitIdInput")
    def parent_org_unit_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parentOrgUnitIdInput"))

    @builtins.property
    @jsii.member(jsii_name="parentOrgUnitPathInput")
    def parent_org_unit_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parentOrgUnitPathInput"))

    @builtins.property
    @jsii.member(jsii_name="blockInheritance")
    def block_inheritance(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "blockInheritance"))

    @block_inheritance.setter
    def block_inheritance(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OrgUnit, "block_inheritance").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blockInheritance", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OrgUnit, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OrgUnit, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parentOrgUnitId")
    def parent_org_unit_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parentOrgUnitId"))

    @parent_org_unit_id.setter
    def parent_org_unit_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OrgUnit, "parent_org_unit_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parentOrgUnitId", value)

    @builtins.property
    @jsii.member(jsii_name="parentOrgUnitPath")
    def parent_org_unit_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parentOrgUnitPath"))

    @parent_org_unit_path.setter
    def parent_org_unit_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(OrgUnit, "parent_org_unit_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parentOrgUnitPath", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-googleworkspace.orgUnit.OrgUnitConfig",
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
        "block_inheritance": "blockInheritance",
        "description": "description",
        "parent_org_unit_id": "parentOrgUnitId",
        "parent_org_unit_path": "parentOrgUnitPath",
    },
)
class OrgUnitConfig(cdktf.TerraformMetaArguments):
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
        block_inheritance: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        parent_org_unit_id: typing.Optional[builtins.str] = None,
        parent_org_unit_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The organizational unit's path name. For example, an organizational unit's name within the /corp/support/sales_support parent path is sales_support. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/org_unit#name OrgUnit#name}
        :param block_inheritance: Defaults to ``false``. Determines if a sub-organizational unit can inherit the settings of the parent organization. False means a sub-organizational unit inherits the settings of the nearest parent organizational unit. For more information on inheritance and users in an organization structure, see the `administration help center <https://support.google.com/a/answer/4352075>`_. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/org_unit#block_inheritance OrgUnit#block_inheritance}
        :param description: Description of the organizational unit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/org_unit#description OrgUnit#description}
        :param parent_org_unit_id: The unique ID of the parent organizational unit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/org_unit#parent_org_unit_id OrgUnit#parent_org_unit_id}
        :param parent_org_unit_path: The organizational unit's parent path. For example, /corp/sales is the parent path for /corp/sales/sales_support organizational unit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/org_unit#parent_org_unit_path OrgUnit#parent_org_unit_path}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(OrgUnitConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument block_inheritance", value=block_inheritance, expected_type=type_hints["block_inheritance"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument parent_org_unit_id", value=parent_org_unit_id, expected_type=type_hints["parent_org_unit_id"])
            check_type(argname="argument parent_org_unit_path", value=parent_org_unit_path, expected_type=type_hints["parent_org_unit_path"])
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
        if block_inheritance is not None:
            self._values["block_inheritance"] = block_inheritance
        if description is not None:
            self._values["description"] = description
        if parent_org_unit_id is not None:
            self._values["parent_org_unit_id"] = parent_org_unit_id
        if parent_org_unit_path is not None:
            self._values["parent_org_unit_path"] = parent_org_unit_path

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
        '''The organizational unit's path name. For example, an organizational unit's name within the /corp/support/sales_support parent path is sales_support.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/org_unit#name OrgUnit#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def block_inheritance(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defaults to ``false``.

        Determines if a sub-organizational unit can inherit the settings of the parent organization. False means a sub-organizational unit inherits the settings of the nearest parent organizational unit. For more information on inheritance and users in an organization structure, see the `administration help center <https://support.google.com/a/answer/4352075>`_.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/org_unit#block_inheritance OrgUnit#block_inheritance}
        '''
        result = self._values.get("block_inheritance")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of the organizational unit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/org_unit#description OrgUnit#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parent_org_unit_id(self) -> typing.Optional[builtins.str]:
        '''The unique ID of the parent organizational unit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/org_unit#parent_org_unit_id OrgUnit#parent_org_unit_id}
        '''
        result = self._values.get("parent_org_unit_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parent_org_unit_path(self) -> typing.Optional[builtins.str]:
        '''The organizational unit's parent path. For example, /corp/sales is the parent path for /corp/sales/sales_support organizational unit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/googleworkspace/r/org_unit#parent_org_unit_path OrgUnit#parent_org_unit_path}
        '''
        result = self._values.get("parent_org_unit_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OrgUnitConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "OrgUnit",
    "OrgUnitConfig",
]

publication.publish()
