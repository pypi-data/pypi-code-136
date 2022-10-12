'''
# `vsphere_vapp_entity`

Refer to the Terraform Registory for docs: [`vsphere_vapp_entity`](https://www.terraform.io/docs/providers/vsphere/r/vapp_entity).
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


class VappEntity(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vsphere.vappEntity.VappEntity",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity vsphere_vapp_entity}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        container_id: builtins.str,
        target_id: builtins.str,
        custom_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        start_action: typing.Optional[builtins.str] = None,
        start_delay: typing.Optional[jsii.Number] = None,
        start_order: typing.Optional[jsii.Number] = None,
        stop_action: typing.Optional[builtins.str] = None,
        stop_delay: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        wait_for_guest: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity vsphere_vapp_entity} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param container_id: Managed object ID of the vApp container the entity is a member of. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity#container_id VappEntity#container_id}
        :param target_id: Managed object ID of the entity to power on or power off. This can be a virtual machine or a vApp. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity#target_id VappEntity#target_id}
        :param custom_attributes: A list of custom attributes to set on this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity#custom_attributes VappEntity#custom_attributes}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity#id VappEntity#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param start_action: How to start the entity. Valid settings are none or powerOn. If set to none, then the entity does not participate in auto-start. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity#start_action VappEntity#start_action}
        :param start_delay: Delay in seconds before continuing with the next entity in the order of entities to be started. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity#start_delay VappEntity#start_delay}
        :param start_order: Order to start and stop target in vApp. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity#start_order VappEntity#start_order}
        :param stop_action: Defines the stop action for the entity. Can be set to none, powerOff, guestShutdown, or suspend. If set to none, then the entity does not participate in auto-stop. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity#stop_action VappEntity#stop_action}
        :param stop_delay: Delay in seconds before continuing with the next entity in the order of entities to be stopped. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity#stop_delay VappEntity#stop_delay}
        :param tags: A list of tag IDs to apply to this object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity#tags VappEntity#tags}
        :param wait_for_guest: Determines if the VM should be marked as being started when VMware Tools are ready instead of waiting for start_delay. This property has no effect for vApps. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity#wait_for_guest VappEntity#wait_for_guest}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(VappEntity.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = VappEntityConfig(
            container_id=container_id,
            target_id=target_id,
            custom_attributes=custom_attributes,
            id=id,
            start_action=start_action,
            start_delay=start_delay,
            start_order=start_order,
            stop_action=stop_action,
            stop_delay=stop_delay,
            tags=tags,
            wait_for_guest=wait_for_guest,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetCustomAttributes")
    def reset_custom_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomAttributes", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetStartAction")
    def reset_start_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartAction", []))

    @jsii.member(jsii_name="resetStartDelay")
    def reset_start_delay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartDelay", []))

    @jsii.member(jsii_name="resetStartOrder")
    def reset_start_order(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartOrder", []))

    @jsii.member(jsii_name="resetStopAction")
    def reset_stop_action(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStopAction", []))

    @jsii.member(jsii_name="resetStopDelay")
    def reset_stop_delay(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStopDelay", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetWaitForGuest")
    def reset_wait_for_guest(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitForGuest", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="containerIdInput")
    def container_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerIdInput"))

    @builtins.property
    @jsii.member(jsii_name="customAttributesInput")
    def custom_attributes_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "customAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="startActionInput")
    def start_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "startActionInput"))

    @builtins.property
    @jsii.member(jsii_name="startDelayInput")
    def start_delay_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startDelayInput"))

    @builtins.property
    @jsii.member(jsii_name="startOrderInput")
    def start_order_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startOrderInput"))

    @builtins.property
    @jsii.member(jsii_name="stopActionInput")
    def stop_action_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stopActionInput"))

    @builtins.property
    @jsii.member(jsii_name="stopDelayInput")
    def stop_delay_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "stopDelayInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="targetIdInput")
    def target_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="waitForGuestInput")
    def wait_for_guest_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "waitForGuestInput"))

    @builtins.property
    @jsii.member(jsii_name="containerId")
    def container_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerId"))

    @container_id.setter
    def container_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VappEntity, "container_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerId", value)

    @builtins.property
    @jsii.member(jsii_name="customAttributes")
    def custom_attributes(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "customAttributes"))

    @custom_attributes.setter
    def custom_attributes(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VappEntity, "custom_attributes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VappEntity, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="startAction")
    def start_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "startAction"))

    @start_action.setter
    def start_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VappEntity, "start_action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startAction", value)

    @builtins.property
    @jsii.member(jsii_name="startDelay")
    def start_delay(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "startDelay"))

    @start_delay.setter
    def start_delay(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VappEntity, "start_delay").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startDelay", value)

    @builtins.property
    @jsii.member(jsii_name="startOrder")
    def start_order(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "startOrder"))

    @start_order.setter
    def start_order(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VappEntity, "start_order").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "startOrder", value)

    @builtins.property
    @jsii.member(jsii_name="stopAction")
    def stop_action(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stopAction"))

    @stop_action.setter
    def stop_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VappEntity, "stop_action").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stopAction", value)

    @builtins.property
    @jsii.member(jsii_name="stopDelay")
    def stop_delay(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "stopDelay"))

    @stop_delay.setter
    def stop_delay(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VappEntity, "stop_delay").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stopDelay", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VappEntity, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="targetId")
    def target_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetId"))

    @target_id.setter
    def target_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VappEntity, "target_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetId", value)

    @builtins.property
    @jsii.member(jsii_name="waitForGuest")
    def wait_for_guest(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "waitForGuest"))

    @wait_for_guest.setter
    def wait_for_guest(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(VappEntity, "wait_for_guest").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitForGuest", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vsphere.vappEntity.VappEntityConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "container_id": "containerId",
        "target_id": "targetId",
        "custom_attributes": "customAttributes",
        "id": "id",
        "start_action": "startAction",
        "start_delay": "startDelay",
        "start_order": "startOrder",
        "stop_action": "stopAction",
        "stop_delay": "stopDelay",
        "tags": "tags",
        "wait_for_guest": "waitForGuest",
    },
)
class VappEntityConfig(cdktf.TerraformMetaArguments):
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
        container_id: builtins.str,
        target_id: builtins.str,
        custom_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        id: typing.Optional[builtins.str] = None,
        start_action: typing.Optional[builtins.str] = None,
        start_delay: typing.Optional[jsii.Number] = None,
        start_order: typing.Optional[jsii.Number] = None,
        stop_action: typing.Optional[builtins.str] = None,
        stop_delay: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        wait_for_guest: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param container_id: Managed object ID of the vApp container the entity is a member of. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity#container_id VappEntity#container_id}
        :param target_id: Managed object ID of the entity to power on or power off. This can be a virtual machine or a vApp. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity#target_id VappEntity#target_id}
        :param custom_attributes: A list of custom attributes to set on this resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity#custom_attributes VappEntity#custom_attributes}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity#id VappEntity#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param start_action: How to start the entity. Valid settings are none or powerOn. If set to none, then the entity does not participate in auto-start. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity#start_action VappEntity#start_action}
        :param start_delay: Delay in seconds before continuing with the next entity in the order of entities to be started. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity#start_delay VappEntity#start_delay}
        :param start_order: Order to start and stop target in vApp. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity#start_order VappEntity#start_order}
        :param stop_action: Defines the stop action for the entity. Can be set to none, powerOff, guestShutdown, or suspend. If set to none, then the entity does not participate in auto-stop. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity#stop_action VappEntity#stop_action}
        :param stop_delay: Delay in seconds before continuing with the next entity in the order of entities to be stopped. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity#stop_delay VappEntity#stop_delay}
        :param tags: A list of tag IDs to apply to this object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity#tags VappEntity#tags}
        :param wait_for_guest: Determines if the VM should be marked as being started when VMware Tools are ready instead of waiting for start_delay. This property has no effect for vApps. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity#wait_for_guest VappEntity#wait_for_guest}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(VappEntityConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument container_id", value=container_id, expected_type=type_hints["container_id"])
            check_type(argname="argument target_id", value=target_id, expected_type=type_hints["target_id"])
            check_type(argname="argument custom_attributes", value=custom_attributes, expected_type=type_hints["custom_attributes"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument start_action", value=start_action, expected_type=type_hints["start_action"])
            check_type(argname="argument start_delay", value=start_delay, expected_type=type_hints["start_delay"])
            check_type(argname="argument start_order", value=start_order, expected_type=type_hints["start_order"])
            check_type(argname="argument stop_action", value=stop_action, expected_type=type_hints["stop_action"])
            check_type(argname="argument stop_delay", value=stop_delay, expected_type=type_hints["stop_delay"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument wait_for_guest", value=wait_for_guest, expected_type=type_hints["wait_for_guest"])
        self._values: typing.Dict[str, typing.Any] = {
            "container_id": container_id,
            "target_id": target_id,
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
        if custom_attributes is not None:
            self._values["custom_attributes"] = custom_attributes
        if id is not None:
            self._values["id"] = id
        if start_action is not None:
            self._values["start_action"] = start_action
        if start_delay is not None:
            self._values["start_delay"] = start_delay
        if start_order is not None:
            self._values["start_order"] = start_order
        if stop_action is not None:
            self._values["stop_action"] = stop_action
        if stop_delay is not None:
            self._values["stop_delay"] = stop_delay
        if tags is not None:
            self._values["tags"] = tags
        if wait_for_guest is not None:
            self._values["wait_for_guest"] = wait_for_guest

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
    def container_id(self) -> builtins.str:
        '''Managed object ID of the vApp container the entity is a member of.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity#container_id VappEntity#container_id}
        '''
        result = self._values.get("container_id")
        assert result is not None, "Required property 'container_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_id(self) -> builtins.str:
        '''Managed object ID of the entity to power on or power off.

        This can be a virtual machine or a vApp.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity#target_id VappEntity#target_id}
        '''
        result = self._values.get("target_id")
        assert result is not None, "Required property 'target_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_attributes(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of custom attributes to set on this resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity#custom_attributes VappEntity#custom_attributes}
        '''
        result = self._values.get("custom_attributes")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity#id VappEntity#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_action(self) -> typing.Optional[builtins.str]:
        '''How to start the entity.

        Valid settings are none or powerOn. If set to none, then the entity does not participate in auto-start.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity#start_action VappEntity#start_action}
        '''
        result = self._values.get("start_action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_delay(self) -> typing.Optional[jsii.Number]:
        '''Delay in seconds before continuing with the next entity in the order of entities to be started.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity#start_delay VappEntity#start_delay}
        '''
        result = self._values.get("start_delay")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def start_order(self) -> typing.Optional[jsii.Number]:
        '''Order to start and stop target in vApp.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity#start_order VappEntity#start_order}
        '''
        result = self._values.get("start_order")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def stop_action(self) -> typing.Optional[builtins.str]:
        '''Defines the stop action for the entity.

        Can be set to none, powerOff, guestShutdown, or suspend. If set to none, then the entity does not participate in auto-stop.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity#stop_action VappEntity#stop_action}
        '''
        result = self._values.get("stop_action")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stop_delay(self) -> typing.Optional[jsii.Number]:
        '''Delay in seconds before continuing with the next entity in the order of entities to be stopped.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity#stop_delay VappEntity#stop_delay}
        '''
        result = self._values.get("stop_delay")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of tag IDs to apply to this object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity#tags VappEntity#tags}
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def wait_for_guest(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Determines if the VM should be marked as being started when VMware Tools are ready instead of waiting for start_delay.

        This property has no effect for vApps.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/vapp_entity#wait_for_guest VappEntity#wait_for_guest}
        '''
        result = self._values.get("wait_for_guest")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VappEntityConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "VappEntity",
    "VappEntityConfig",
]

publication.publish()
