'''
# `opc_compute_orchestrated_instance`

Refer to the Terraform Registory for docs: [`opc_compute_orchestrated_instance`](https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance).
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


class ComputeOrchestratedInstance(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.computeOrchestratedInstance.ComputeOrchestratedInstance",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance opc_compute_orchestrated_instance}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        desired_state: builtins.str,
        instance: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeOrchestratedInstanceInstance", typing.Dict[str, typing.Any]]]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ComputeOrchestratedInstanceTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance opc_compute_orchestrated_instance} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param desired_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#desired_state ComputeOrchestratedInstance#desired_state}.
        :param instance: instance block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#instance ComputeOrchestratedInstance#instance}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#name ComputeOrchestratedInstance#name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#description ComputeOrchestratedInstance#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#id ComputeOrchestratedInstance#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#tags ComputeOrchestratedInstance#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#timeouts ComputeOrchestratedInstance#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeOrchestratedInstance.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ComputeOrchestratedInstanceConfig(
            desired_state=desired_state,
            instance=instance,
            name=name,
            description=description,
            id=id,
            tags=tags,
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

    @jsii.member(jsii_name="putInstance")
    def put_instance(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeOrchestratedInstanceInstance", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeOrchestratedInstance.put_instance)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInstance", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#create ComputeOrchestratedInstance#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#delete ComputeOrchestratedInstance#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#update ComputeOrchestratedInstance#update}.
        '''
        value = ComputeOrchestratedInstanceTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

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
    @jsii.member(jsii_name="instance")
    def instance(self) -> "ComputeOrchestratedInstanceInstanceList":
        return typing.cast("ComputeOrchestratedInstanceInstanceList", jsii.get(self, "instance"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "ComputeOrchestratedInstanceTimeoutsOutputReference":
        return typing.cast("ComputeOrchestratedInstanceTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "version"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="desiredStateInput")
    def desired_state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "desiredStateInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceInput")
    def instance_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeOrchestratedInstanceInstance"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeOrchestratedInstanceInstance"]]], jsii.get(self, "instanceInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["ComputeOrchestratedInstanceTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["ComputeOrchestratedInstanceTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstance, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="desiredState")
    def desired_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "desiredState"))

    @desired_state.setter
    def desired_state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstance, "desired_state").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredState", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstance, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstance, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstance, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.computeOrchestratedInstance.ComputeOrchestratedInstanceConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "desired_state": "desiredState",
        "instance": "instance",
        "name": "name",
        "description": "description",
        "id": "id",
        "tags": "tags",
        "timeouts": "timeouts",
    },
)
class ComputeOrchestratedInstanceConfig(cdktf.TerraformMetaArguments):
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
        desired_state: builtins.str,
        instance: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeOrchestratedInstanceInstance", typing.Dict[str, typing.Any]]]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["ComputeOrchestratedInstanceTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param desired_state: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#desired_state ComputeOrchestratedInstance#desired_state}.
        :param instance: instance block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#instance ComputeOrchestratedInstance#instance}
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#name ComputeOrchestratedInstance#name}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#description ComputeOrchestratedInstance#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#id ComputeOrchestratedInstance#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#tags ComputeOrchestratedInstance#tags}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#timeouts ComputeOrchestratedInstance#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = ComputeOrchestratedInstanceTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(ComputeOrchestratedInstanceConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument desired_state", value=desired_state, expected_type=type_hints["desired_state"])
            check_type(argname="argument instance", value=instance, expected_type=type_hints["instance"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "desired_state": desired_state,
            "instance": instance,
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
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if tags is not None:
            self._values["tags"] = tags
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
    def desired_state(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#desired_state ComputeOrchestratedInstance#desired_state}.'''
        result = self._values.get("desired_state")
        assert result is not None, "Required property 'desired_state' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["ComputeOrchestratedInstanceInstance"]]:
        '''instance block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#instance ComputeOrchestratedInstance#instance}
        '''
        result = self._values.get("instance")
        assert result is not None, "Required property 'instance' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["ComputeOrchestratedInstanceInstance"]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#name ComputeOrchestratedInstance#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#description ComputeOrchestratedInstance#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#id ComputeOrchestratedInstance#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#tags ComputeOrchestratedInstance#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["ComputeOrchestratedInstanceTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#timeouts ComputeOrchestratedInstance#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["ComputeOrchestratedInstanceTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeOrchestratedInstanceConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.computeOrchestratedInstance.ComputeOrchestratedInstanceInstance",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "shape": "shape",
        "boot_order": "bootOrder",
        "hostname": "hostname",
        "image_list": "imageList",
        "instance_attributes": "instanceAttributes",
        "label": "label",
        "networking_info": "networkingInfo",
        "persistent": "persistent",
        "reverse_dns": "reverseDns",
        "ssh_keys": "sshKeys",
        "storage": "storage",
        "tags": "tags",
    },
)
class ComputeOrchestratedInstanceInstance:
    def __init__(
        self,
        *,
        name: builtins.str,
        shape: builtins.str,
        boot_order: typing.Optional[typing.Sequence[jsii.Number]] = None,
        hostname: typing.Optional[builtins.str] = None,
        image_list: typing.Optional[builtins.str] = None,
        instance_attributes: typing.Optional[builtins.str] = None,
        label: typing.Optional[builtins.str] = None,
        networking_info: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeOrchestratedInstanceInstanceNetworkingInfo", typing.Dict[str, typing.Any]]]]] = None,
        persistent: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        reverse_dns: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        ssh_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        storage: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeOrchestratedInstanceInstanceStorage", typing.Dict[str, typing.Any]]]]] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#name ComputeOrchestratedInstance#name}.
        :param shape: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#shape ComputeOrchestratedInstance#shape}.
        :param boot_order: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#boot_order ComputeOrchestratedInstance#boot_order}.
        :param hostname: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#hostname ComputeOrchestratedInstance#hostname}.
        :param image_list: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#image_list ComputeOrchestratedInstance#image_list}.
        :param instance_attributes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#instance_attributes ComputeOrchestratedInstance#instance_attributes}.
        :param label: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#label ComputeOrchestratedInstance#label}.
        :param networking_info: networking_info block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#networking_info ComputeOrchestratedInstance#networking_info}
        :param persistent: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#persistent ComputeOrchestratedInstance#persistent}.
        :param reverse_dns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#reverse_dns ComputeOrchestratedInstance#reverse_dns}.
        :param ssh_keys: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#ssh_keys ComputeOrchestratedInstance#ssh_keys}.
        :param storage: storage block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#storage ComputeOrchestratedInstance#storage}
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#tags ComputeOrchestratedInstance#tags}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeOrchestratedInstanceInstance.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument shape", value=shape, expected_type=type_hints["shape"])
            check_type(argname="argument boot_order", value=boot_order, expected_type=type_hints["boot_order"])
            check_type(argname="argument hostname", value=hostname, expected_type=type_hints["hostname"])
            check_type(argname="argument image_list", value=image_list, expected_type=type_hints["image_list"])
            check_type(argname="argument instance_attributes", value=instance_attributes, expected_type=type_hints["instance_attributes"])
            check_type(argname="argument label", value=label, expected_type=type_hints["label"])
            check_type(argname="argument networking_info", value=networking_info, expected_type=type_hints["networking_info"])
            check_type(argname="argument persistent", value=persistent, expected_type=type_hints["persistent"])
            check_type(argname="argument reverse_dns", value=reverse_dns, expected_type=type_hints["reverse_dns"])
            check_type(argname="argument ssh_keys", value=ssh_keys, expected_type=type_hints["ssh_keys"])
            check_type(argname="argument storage", value=storage, expected_type=type_hints["storage"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "shape": shape,
        }
        if boot_order is not None:
            self._values["boot_order"] = boot_order
        if hostname is not None:
            self._values["hostname"] = hostname
        if image_list is not None:
            self._values["image_list"] = image_list
        if instance_attributes is not None:
            self._values["instance_attributes"] = instance_attributes
        if label is not None:
            self._values["label"] = label
        if networking_info is not None:
            self._values["networking_info"] = networking_info
        if persistent is not None:
            self._values["persistent"] = persistent
        if reverse_dns is not None:
            self._values["reverse_dns"] = reverse_dns
        if ssh_keys is not None:
            self._values["ssh_keys"] = ssh_keys
        if storage is not None:
            self._values["storage"] = storage
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#name ComputeOrchestratedInstance#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def shape(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#shape ComputeOrchestratedInstance#shape}.'''
        result = self._values.get("shape")
        assert result is not None, "Required property 'shape' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def boot_order(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#boot_order ComputeOrchestratedInstance#boot_order}.'''
        result = self._values.get("boot_order")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def hostname(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#hostname ComputeOrchestratedInstance#hostname}.'''
        result = self._values.get("hostname")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_list(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#image_list ComputeOrchestratedInstance#image_list}.'''
        result = self._values.get("image_list")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_attributes(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#instance_attributes ComputeOrchestratedInstance#instance_attributes}.'''
        result = self._values.get("instance_attributes")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def label(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#label ComputeOrchestratedInstance#label}.'''
        result = self._values.get("label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def networking_info(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeOrchestratedInstanceInstanceNetworkingInfo"]]]:
        '''networking_info block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#networking_info ComputeOrchestratedInstance#networking_info}
        '''
        result = self._values.get("networking_info")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeOrchestratedInstanceInstanceNetworkingInfo"]]], result)

    @builtins.property
    def persistent(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#persistent ComputeOrchestratedInstance#persistent}.'''
        result = self._values.get("persistent")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def reverse_dns(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#reverse_dns ComputeOrchestratedInstance#reverse_dns}.'''
        result = self._values.get("reverse_dns")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def ssh_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#ssh_keys ComputeOrchestratedInstance#ssh_keys}.'''
        result = self._values.get("ssh_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def storage(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeOrchestratedInstanceInstanceStorage"]]]:
        '''storage block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#storage ComputeOrchestratedInstance#storage}
        '''
        result = self._values.get("storage")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeOrchestratedInstanceInstanceStorage"]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#tags ComputeOrchestratedInstance#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeOrchestratedInstanceInstance(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeOrchestratedInstanceInstanceList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.computeOrchestratedInstance.ComputeOrchestratedInstanceInstanceList",
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
            type_hints = typing.get_type_hints(ComputeOrchestratedInstanceInstanceList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ComputeOrchestratedInstanceInstanceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeOrchestratedInstanceInstanceList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ComputeOrchestratedInstanceInstanceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeOrchestratedInstanceInstance]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeOrchestratedInstanceInstance]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeOrchestratedInstanceInstance]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.computeOrchestratedInstance.ComputeOrchestratedInstanceInstanceNetworkingInfo",
    jsii_struct_bases=[],
    name_mapping={
        "index": "index",
        "dns": "dns",
        "ip_address": "ipAddress",
        "ip_network": "ipNetwork",
        "is_default_gateway": "isDefaultGateway",
        "mac_address": "macAddress",
        "name_servers": "nameServers",
        "nat": "nat",
        "search_domains": "searchDomains",
        "sec_lists": "secLists",
        "shared_network": "sharedNetwork",
        "vnic": "vnic",
        "vnic_sets": "vnicSets",
    },
)
class ComputeOrchestratedInstanceInstanceNetworkingInfo:
    def __init__(
        self,
        *,
        index: jsii.Number,
        dns: typing.Optional[typing.Sequence[builtins.str]] = None,
        ip_address: typing.Optional[builtins.str] = None,
        ip_network: typing.Optional[builtins.str] = None,
        is_default_gateway: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        mac_address: typing.Optional[builtins.str] = None,
        name_servers: typing.Optional[typing.Sequence[builtins.str]] = None,
        nat: typing.Optional[typing.Sequence[builtins.str]] = None,
        search_domains: typing.Optional[typing.Sequence[builtins.str]] = None,
        sec_lists: typing.Optional[typing.Sequence[builtins.str]] = None,
        shared_network: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        vnic: typing.Optional[builtins.str] = None,
        vnic_sets: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param index: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#index ComputeOrchestratedInstance#index}.
        :param dns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#dns ComputeOrchestratedInstance#dns}.
        :param ip_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#ip_address ComputeOrchestratedInstance#ip_address}.
        :param ip_network: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#ip_network ComputeOrchestratedInstance#ip_network}.
        :param is_default_gateway: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#is_default_gateway ComputeOrchestratedInstance#is_default_gateway}.
        :param mac_address: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#mac_address ComputeOrchestratedInstance#mac_address}.
        :param name_servers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#name_servers ComputeOrchestratedInstance#name_servers}.
        :param nat: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#nat ComputeOrchestratedInstance#nat}.
        :param search_domains: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#search_domains ComputeOrchestratedInstance#search_domains}.
        :param sec_lists: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#sec_lists ComputeOrchestratedInstance#sec_lists}.
        :param shared_network: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#shared_network ComputeOrchestratedInstance#shared_network}.
        :param vnic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#vnic ComputeOrchestratedInstance#vnic}.
        :param vnic_sets: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#vnic_sets ComputeOrchestratedInstance#vnic_sets}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeOrchestratedInstanceInstanceNetworkingInfo.__init__)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
            check_type(argname="argument dns", value=dns, expected_type=type_hints["dns"])
            check_type(argname="argument ip_address", value=ip_address, expected_type=type_hints["ip_address"])
            check_type(argname="argument ip_network", value=ip_network, expected_type=type_hints["ip_network"])
            check_type(argname="argument is_default_gateway", value=is_default_gateway, expected_type=type_hints["is_default_gateway"])
            check_type(argname="argument mac_address", value=mac_address, expected_type=type_hints["mac_address"])
            check_type(argname="argument name_servers", value=name_servers, expected_type=type_hints["name_servers"])
            check_type(argname="argument nat", value=nat, expected_type=type_hints["nat"])
            check_type(argname="argument search_domains", value=search_domains, expected_type=type_hints["search_domains"])
            check_type(argname="argument sec_lists", value=sec_lists, expected_type=type_hints["sec_lists"])
            check_type(argname="argument shared_network", value=shared_network, expected_type=type_hints["shared_network"])
            check_type(argname="argument vnic", value=vnic, expected_type=type_hints["vnic"])
            check_type(argname="argument vnic_sets", value=vnic_sets, expected_type=type_hints["vnic_sets"])
        self._values: typing.Dict[str, typing.Any] = {
            "index": index,
        }
        if dns is not None:
            self._values["dns"] = dns
        if ip_address is not None:
            self._values["ip_address"] = ip_address
        if ip_network is not None:
            self._values["ip_network"] = ip_network
        if is_default_gateway is not None:
            self._values["is_default_gateway"] = is_default_gateway
        if mac_address is not None:
            self._values["mac_address"] = mac_address
        if name_servers is not None:
            self._values["name_servers"] = name_servers
        if nat is not None:
            self._values["nat"] = nat
        if search_domains is not None:
            self._values["search_domains"] = search_domains
        if sec_lists is not None:
            self._values["sec_lists"] = sec_lists
        if shared_network is not None:
            self._values["shared_network"] = shared_network
        if vnic is not None:
            self._values["vnic"] = vnic
        if vnic_sets is not None:
            self._values["vnic_sets"] = vnic_sets

    @builtins.property
    def index(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#index ComputeOrchestratedInstance#index}.'''
        result = self._values.get("index")
        assert result is not None, "Required property 'index' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def dns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#dns ComputeOrchestratedInstance#dns}.'''
        result = self._values.get("dns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def ip_address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#ip_address ComputeOrchestratedInstance#ip_address}.'''
        result = self._values.get("ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_network(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#ip_network ComputeOrchestratedInstance#ip_network}.'''
        result = self._values.get("ip_network")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_default_gateway(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#is_default_gateway ComputeOrchestratedInstance#is_default_gateway}.'''
        result = self._values.get("is_default_gateway")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def mac_address(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#mac_address ComputeOrchestratedInstance#mac_address}.'''
        result = self._values.get("mac_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name_servers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#name_servers ComputeOrchestratedInstance#name_servers}.'''
        result = self._values.get("name_servers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def nat(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#nat ComputeOrchestratedInstance#nat}.'''
        result = self._values.get("nat")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def search_domains(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#search_domains ComputeOrchestratedInstance#search_domains}.'''
        result = self._values.get("search_domains")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def sec_lists(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#sec_lists ComputeOrchestratedInstance#sec_lists}.'''
        result = self._values.get("sec_lists")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def shared_network(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#shared_network ComputeOrchestratedInstance#shared_network}.'''
        result = self._values.get("shared_network")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def vnic(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#vnic ComputeOrchestratedInstance#vnic}.'''
        result = self._values.get("vnic")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vnic_sets(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#vnic_sets ComputeOrchestratedInstance#vnic_sets}.'''
        result = self._values.get("vnic_sets")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeOrchestratedInstanceInstanceNetworkingInfo(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeOrchestratedInstanceInstanceNetworkingInfoList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.computeOrchestratedInstance.ComputeOrchestratedInstanceInstanceNetworkingInfoList",
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
            type_hints = typing.get_type_hints(ComputeOrchestratedInstanceInstanceNetworkingInfoList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ComputeOrchestratedInstanceInstanceNetworkingInfoOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeOrchestratedInstanceInstanceNetworkingInfoList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ComputeOrchestratedInstanceInstanceNetworkingInfoOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceNetworkingInfoList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceNetworkingInfoList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceNetworkingInfoList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeOrchestratedInstanceInstanceNetworkingInfo]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeOrchestratedInstanceInstanceNetworkingInfo]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeOrchestratedInstanceInstanceNetworkingInfo]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceNetworkingInfoList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeOrchestratedInstanceInstanceNetworkingInfoOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.computeOrchestratedInstance.ComputeOrchestratedInstanceInstanceNetworkingInfoOutputReference",
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
            type_hints = typing.get_type_hints(ComputeOrchestratedInstanceInstanceNetworkingInfoOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDns")
    def reset_dns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDns", []))

    @jsii.member(jsii_name="resetIpAddress")
    def reset_ip_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpAddress", []))

    @jsii.member(jsii_name="resetIpNetwork")
    def reset_ip_network(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpNetwork", []))

    @jsii.member(jsii_name="resetIsDefaultGateway")
    def reset_is_default_gateway(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsDefaultGateway", []))

    @jsii.member(jsii_name="resetMacAddress")
    def reset_mac_address(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMacAddress", []))

    @jsii.member(jsii_name="resetNameServers")
    def reset_name_servers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNameServers", []))

    @jsii.member(jsii_name="resetNat")
    def reset_nat(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNat", []))

    @jsii.member(jsii_name="resetSearchDomains")
    def reset_search_domains(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSearchDomains", []))

    @jsii.member(jsii_name="resetSecLists")
    def reset_sec_lists(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecLists", []))

    @jsii.member(jsii_name="resetSharedNetwork")
    def reset_shared_network(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSharedNetwork", []))

    @jsii.member(jsii_name="resetVnic")
    def reset_vnic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVnic", []))

    @jsii.member(jsii_name="resetVnicSets")
    def reset_vnic_sets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVnicSets", []))

    @builtins.property
    @jsii.member(jsii_name="dnsInput")
    def dns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dnsInput"))

    @builtins.property
    @jsii.member(jsii_name="indexInput")
    def index_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "indexInput"))

    @builtins.property
    @jsii.member(jsii_name="ipAddressInput")
    def ip_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="ipNetworkInput")
    def ip_network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipNetworkInput"))

    @builtins.property
    @jsii.member(jsii_name="isDefaultGatewayInput")
    def is_default_gateway_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isDefaultGatewayInput"))

    @builtins.property
    @jsii.member(jsii_name="macAddressInput")
    def mac_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "macAddressInput"))

    @builtins.property
    @jsii.member(jsii_name="nameServersInput")
    def name_servers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "nameServersInput"))

    @builtins.property
    @jsii.member(jsii_name="natInput")
    def nat_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "natInput"))

    @builtins.property
    @jsii.member(jsii_name="searchDomainsInput")
    def search_domains_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "searchDomainsInput"))

    @builtins.property
    @jsii.member(jsii_name="secListsInput")
    def sec_lists_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "secListsInput"))

    @builtins.property
    @jsii.member(jsii_name="sharedNetworkInput")
    def shared_network_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "sharedNetworkInput"))

    @builtins.property
    @jsii.member(jsii_name="vnicInput")
    def vnic_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vnicInput"))

    @builtins.property
    @jsii.member(jsii_name="vnicSetsInput")
    def vnic_sets_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vnicSetsInput"))

    @builtins.property
    @jsii.member(jsii_name="dns")
    def dns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dns"))

    @dns.setter
    def dns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceNetworkingInfoOutputReference, "dns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dns", value)

    @builtins.property
    @jsii.member(jsii_name="index")
    def index(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "index"))

    @index.setter
    def index(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceNetworkingInfoOutputReference, "index").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "index", value)

    @builtins.property
    @jsii.member(jsii_name="ipAddress")
    def ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddress"))

    @ip_address.setter
    def ip_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceNetworkingInfoOutputReference, "ip_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAddress", value)

    @builtins.property
    @jsii.member(jsii_name="ipNetwork")
    def ip_network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipNetwork"))

    @ip_network.setter
    def ip_network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceNetworkingInfoOutputReference, "ip_network").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipNetwork", value)

    @builtins.property
    @jsii.member(jsii_name="isDefaultGateway")
    def is_default_gateway(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isDefaultGateway"))

    @is_default_gateway.setter
    def is_default_gateway(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceNetworkingInfoOutputReference, "is_default_gateway").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isDefaultGateway", value)

    @builtins.property
    @jsii.member(jsii_name="macAddress")
    def mac_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "macAddress"))

    @mac_address.setter
    def mac_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceNetworkingInfoOutputReference, "mac_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "macAddress", value)

    @builtins.property
    @jsii.member(jsii_name="nameServers")
    def name_servers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "nameServers"))

    @name_servers.setter
    def name_servers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceNetworkingInfoOutputReference, "name_servers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nameServers", value)

    @builtins.property
    @jsii.member(jsii_name="nat")
    def nat(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "nat"))

    @nat.setter
    def nat(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceNetworkingInfoOutputReference, "nat").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nat", value)

    @builtins.property
    @jsii.member(jsii_name="searchDomains")
    def search_domains(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "searchDomains"))

    @search_domains.setter
    def search_domains(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceNetworkingInfoOutputReference, "search_domains").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "searchDomains", value)

    @builtins.property
    @jsii.member(jsii_name="secLists")
    def sec_lists(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "secLists"))

    @sec_lists.setter
    def sec_lists(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceNetworkingInfoOutputReference, "sec_lists").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secLists", value)

    @builtins.property
    @jsii.member(jsii_name="sharedNetwork")
    def shared_network(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "sharedNetwork"))

    @shared_network.setter
    def shared_network(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceNetworkingInfoOutputReference, "shared_network").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sharedNetwork", value)

    @builtins.property
    @jsii.member(jsii_name="vnic")
    def vnic(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vnic"))

    @vnic.setter
    def vnic(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceNetworkingInfoOutputReference, "vnic").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vnic", value)

    @builtins.property
    @jsii.member(jsii_name="vnicSets")
    def vnic_sets(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "vnicSets"))

    @vnic_sets.setter
    def vnic_sets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceNetworkingInfoOutputReference, "vnic_sets").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vnicSets", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComputeOrchestratedInstanceInstanceNetworkingInfo, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComputeOrchestratedInstanceInstanceNetworkingInfo, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComputeOrchestratedInstanceInstanceNetworkingInfo, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceNetworkingInfoOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeOrchestratedInstanceInstanceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.computeOrchestratedInstance.ComputeOrchestratedInstanceInstanceOutputReference",
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
            type_hints = typing.get_type_hints(ComputeOrchestratedInstanceInstanceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putNetworkingInfo")
    def put_networking_info(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ComputeOrchestratedInstanceInstanceNetworkingInfo, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeOrchestratedInstanceInstanceOutputReference.put_networking_info)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNetworkingInfo", [value]))

    @jsii.member(jsii_name="putStorage")
    def put_storage(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ComputeOrchestratedInstanceInstanceStorage", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeOrchestratedInstanceInstanceOutputReference.put_storage)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStorage", [value]))

    @jsii.member(jsii_name="resetBootOrder")
    def reset_boot_order(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBootOrder", []))

    @jsii.member(jsii_name="resetHostname")
    def reset_hostname(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostname", []))

    @jsii.member(jsii_name="resetImageList")
    def reset_image_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImageList", []))

    @jsii.member(jsii_name="resetInstanceAttributes")
    def reset_instance_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceAttributes", []))

    @jsii.member(jsii_name="resetLabel")
    def reset_label(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabel", []))

    @jsii.member(jsii_name="resetNetworkingInfo")
    def reset_networking_info(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkingInfo", []))

    @jsii.member(jsii_name="resetPersistent")
    def reset_persistent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPersistent", []))

    @jsii.member(jsii_name="resetReverseDns")
    def reset_reverse_dns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReverseDns", []))

    @jsii.member(jsii_name="resetSshKeys")
    def reset_ssh_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSshKeys", []))

    @jsii.member(jsii_name="resetStorage")
    def reset_storage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorage", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @builtins.property
    @jsii.member(jsii_name="attributes")
    def attributes(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "attributes"))

    @builtins.property
    @jsii.member(jsii_name="availabilityDomain")
    def availability_domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "availabilityDomain"))

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @builtins.property
    @jsii.member(jsii_name="entry")
    def entry(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "entry"))

    @builtins.property
    @jsii.member(jsii_name="fingerprint")
    def fingerprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fingerprint"))

    @builtins.property
    @jsii.member(jsii_name="fqdn")
    def fqdn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fqdn"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="imageFormat")
    def image_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageFormat"))

    @builtins.property
    @jsii.member(jsii_name="ipAddress")
    def ip_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipAddress"))

    @builtins.property
    @jsii.member(jsii_name="networkingInfo")
    def networking_info(self) -> ComputeOrchestratedInstanceInstanceNetworkingInfoList:
        return typing.cast(ComputeOrchestratedInstanceInstanceNetworkingInfoList, jsii.get(self, "networkingInfo"))

    @builtins.property
    @jsii.member(jsii_name="placementRequirements")
    def placement_requirements(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "placementRequirements"))

    @builtins.property
    @jsii.member(jsii_name="platform")
    def platform(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "platform"))

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "priority"))

    @builtins.property
    @jsii.member(jsii_name="quotaReservation")
    def quota_reservation(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "quotaReservation"))

    @builtins.property
    @jsii.member(jsii_name="relationships")
    def relationships(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "relationships"))

    @builtins.property
    @jsii.member(jsii_name="resolvers")
    def resolvers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "resolvers"))

    @builtins.property
    @jsii.member(jsii_name="site")
    def site(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "site"))

    @builtins.property
    @jsii.member(jsii_name="startTime")
    def start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startTime"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="storage")
    def storage(self) -> "ComputeOrchestratedInstanceInstanceStorageList":
        return typing.cast("ComputeOrchestratedInstanceInstanceStorageList", jsii.get(self, "storage"))

    @builtins.property
    @jsii.member(jsii_name="vcable")
    def vcable(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vcable"))

    @builtins.property
    @jsii.member(jsii_name="virtio")
    def virtio(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "virtio"))

    @builtins.property
    @jsii.member(jsii_name="vncAddress")
    def vnc_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vncAddress"))

    @builtins.property
    @jsii.member(jsii_name="bootOrderInput")
    def boot_order_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "bootOrderInput"))

    @builtins.property
    @jsii.member(jsii_name="hostnameInput")
    def hostname_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostnameInput"))

    @builtins.property
    @jsii.member(jsii_name="imageListInput")
    def image_list_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageListInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceAttributesInput")
    def instance_attributes_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="labelInput")
    def label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "labelInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkingInfoInput")
    def networking_info_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeOrchestratedInstanceInstanceNetworkingInfo]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeOrchestratedInstanceInstanceNetworkingInfo]]], jsii.get(self, "networkingInfoInput"))

    @builtins.property
    @jsii.member(jsii_name="persistentInput")
    def persistent_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "persistentInput"))

    @builtins.property
    @jsii.member(jsii_name="reverseDnsInput")
    def reverse_dns_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "reverseDnsInput"))

    @builtins.property
    @jsii.member(jsii_name="shapeInput")
    def shape_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shapeInput"))

    @builtins.property
    @jsii.member(jsii_name="sshKeysInput")
    def ssh_keys_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sshKeysInput"))

    @builtins.property
    @jsii.member(jsii_name="storageInput")
    def storage_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeOrchestratedInstanceInstanceStorage"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ComputeOrchestratedInstanceInstanceStorage"]]], jsii.get(self, "storageInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="bootOrder")
    def boot_order(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "bootOrder"))

    @boot_order.setter
    def boot_order(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceOutputReference, "boot_order").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bootOrder", value)

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @hostname.setter
    def hostname(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceOutputReference, "hostname").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostname", value)

    @builtins.property
    @jsii.member(jsii_name="imageList")
    def image_list(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageList"))

    @image_list.setter
    def image_list(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceOutputReference, "image_list").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageList", value)

    @builtins.property
    @jsii.member(jsii_name="instanceAttributes")
    def instance_attributes(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceAttributes"))

    @instance_attributes.setter
    def instance_attributes(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceOutputReference, "instance_attributes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="label")
    def label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "label"))

    @label.setter
    def label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceOutputReference, "label").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "label", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="persistent")
    def persistent(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "persistent"))

    @persistent.setter
    def persistent(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceOutputReference, "persistent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "persistent", value)

    @builtins.property
    @jsii.member(jsii_name="reverseDns")
    def reverse_dns(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "reverseDns"))

    @reverse_dns.setter
    def reverse_dns(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceOutputReference, "reverse_dns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reverseDns", value)

    @builtins.property
    @jsii.member(jsii_name="shape")
    def shape(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "shape"))

    @shape.setter
    def shape(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceOutputReference, "shape").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shape", value)

    @builtins.property
    @jsii.member(jsii_name="sshKeys")
    def ssh_keys(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sshKeys"))

    @ssh_keys.setter
    def ssh_keys(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceOutputReference, "ssh_keys").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sshKeys", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceOutputReference, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComputeOrchestratedInstanceInstance, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComputeOrchestratedInstanceInstance, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComputeOrchestratedInstanceInstance, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.computeOrchestratedInstance.ComputeOrchestratedInstanceInstanceStorage",
    jsii_struct_bases=[],
    name_mapping={"index": "index", "volume": "volume"},
)
class ComputeOrchestratedInstanceInstanceStorage:
    def __init__(self, *, index: jsii.Number, volume: builtins.str) -> None:
        '''
        :param index: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#index ComputeOrchestratedInstance#index}.
        :param volume: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#volume ComputeOrchestratedInstance#volume}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeOrchestratedInstanceInstanceStorage.__init__)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
            check_type(argname="argument volume", value=volume, expected_type=type_hints["volume"])
        self._values: typing.Dict[str, typing.Any] = {
            "index": index,
            "volume": volume,
        }

    @builtins.property
    def index(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#index ComputeOrchestratedInstance#index}.'''
        result = self._values.get("index")
        assert result is not None, "Required property 'index' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def volume(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#volume ComputeOrchestratedInstance#volume}.'''
        result = self._values.get("volume")
        assert result is not None, "Required property 'volume' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeOrchestratedInstanceInstanceStorage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeOrchestratedInstanceInstanceStorageList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.computeOrchestratedInstance.ComputeOrchestratedInstanceInstanceStorageList",
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
            type_hints = typing.get_type_hints(ComputeOrchestratedInstanceInstanceStorageList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "ComputeOrchestratedInstanceInstanceStorageOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeOrchestratedInstanceInstanceStorageList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ComputeOrchestratedInstanceInstanceStorageOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceStorageList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceStorageList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceStorageList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeOrchestratedInstanceInstanceStorage]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeOrchestratedInstanceInstanceStorage]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ComputeOrchestratedInstanceInstanceStorage]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceStorageList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ComputeOrchestratedInstanceInstanceStorageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.computeOrchestratedInstance.ComputeOrchestratedInstanceInstanceStorageOutputReference",
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
            type_hints = typing.get_type_hints(ComputeOrchestratedInstanceInstanceStorageOutputReference.__init__)
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
    @jsii.member(jsii_name="indexInput")
    def index_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "indexInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeInput")
    def volume_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeInput"))

    @builtins.property
    @jsii.member(jsii_name="index")
    def index(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "index"))

    @index.setter
    def index(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceStorageOutputReference, "index").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "index", value)

    @builtins.property
    @jsii.member(jsii_name="volume")
    def volume(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volume"))

    @volume.setter
    def volume(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceStorageOutputReference, "volume").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volume", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComputeOrchestratedInstanceInstanceStorage, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComputeOrchestratedInstanceInstanceStorage, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComputeOrchestratedInstanceInstanceStorage, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceInstanceStorageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-opc.computeOrchestratedInstance.ComputeOrchestratedInstanceTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class ComputeOrchestratedInstanceTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#create ComputeOrchestratedInstance#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#delete ComputeOrchestratedInstance#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#update ComputeOrchestratedInstance#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ComputeOrchestratedInstanceTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#create ComputeOrchestratedInstance#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#delete ComputeOrchestratedInstance#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/opc/r/compute_orchestrated_instance#update ComputeOrchestratedInstance#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ComputeOrchestratedInstanceTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ComputeOrchestratedInstanceTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-opc.computeOrchestratedInstance.ComputeOrchestratedInstanceTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(ComputeOrchestratedInstanceTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ComputeOrchestratedInstanceTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ComputeOrchestratedInstanceTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ComputeOrchestratedInstanceTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ComputeOrchestratedInstanceTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ComputeOrchestratedInstance",
    "ComputeOrchestratedInstanceConfig",
    "ComputeOrchestratedInstanceInstance",
    "ComputeOrchestratedInstanceInstanceList",
    "ComputeOrchestratedInstanceInstanceNetworkingInfo",
    "ComputeOrchestratedInstanceInstanceNetworkingInfoList",
    "ComputeOrchestratedInstanceInstanceNetworkingInfoOutputReference",
    "ComputeOrchestratedInstanceInstanceOutputReference",
    "ComputeOrchestratedInstanceInstanceStorage",
    "ComputeOrchestratedInstanceInstanceStorageList",
    "ComputeOrchestratedInstanceInstanceStorageOutputReference",
    "ComputeOrchestratedInstanceTimeouts",
    "ComputeOrchestratedInstanceTimeoutsOutputReference",
]

publication.publish()
