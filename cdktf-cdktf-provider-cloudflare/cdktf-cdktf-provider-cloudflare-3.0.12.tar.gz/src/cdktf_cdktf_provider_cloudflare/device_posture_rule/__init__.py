'''
# `cloudflare_device_posture_rule`

Refer to the Terraform Registory for docs: [`cloudflare_device_posture_rule`](https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule).
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


class DevicePostureRule(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.devicePostureRule.DevicePostureRule",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule cloudflare_device_posture_rule}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        account_id: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        expiration: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        input: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DevicePostureRuleInput", typing.Dict[str, typing.Any]]]]] = None,
        match: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DevicePostureRuleMatch", typing.Dict[str, typing.Any]]]]] = None,
        name: typing.Optional[builtins.str] = None,
        schedule: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule cloudflare_device_posture_rule} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param account_id: The account identifier to target for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#account_id DevicePostureRule#account_id}
        :param type: The device posture rule type. Available values: ``serial_number``, ``file``, ``application``, ``gateway``, ``warp``, ``domain_joined``, ``os_version``, ``disk_encryption``, ``firewall``, ``workspace_one``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#type DevicePostureRule#type}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#description DevicePostureRule#description}.
        :param expiration: Expire posture results after the specified amount of time. Must be in the format ``1h`` or ``30m``. Valid units are ``h`` and ``m``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#expiration DevicePostureRule#expiration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#id DevicePostureRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param input: input block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#input DevicePostureRule#input}
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#match DevicePostureRule#match}
        :param name: Name of the device posture rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#name DevicePostureRule#name}
        :param schedule: Tells the client when to run the device posture check. Must be in the format ``1h`` or ``30m``. Valid units are ``h`` and ``m``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#schedule DevicePostureRule#schedule}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DevicePostureRule.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DevicePostureRuleConfig(
            account_id=account_id,
            type=type,
            description=description,
            expiration=expiration,
            id=id,
            input=input,
            match=match,
            name=name,
            schedule=schedule,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putInput")
    def put_input(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DevicePostureRuleInput", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DevicePostureRule.put_input)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putInput", [value]))

    @jsii.member(jsii_name="putMatch")
    def put_match(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DevicePostureRuleMatch", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DevicePostureRule.put_match)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatch", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetExpiration")
    def reset_expiration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpiration", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInput")
    def reset_input(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInput", []))

    @jsii.member(jsii_name="resetMatch")
    def reset_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatch", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetSchedule")
    def reset_schedule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchedule", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="input")
    def input(self) -> "DevicePostureRuleInputList":
        return typing.cast("DevicePostureRuleInputList", jsii.get(self, "input"))

    @builtins.property
    @jsii.member(jsii_name="match")
    def match(self) -> "DevicePostureRuleMatchList":
        return typing.cast("DevicePostureRuleMatchList", jsii.get(self, "match"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="expirationInput")
    def expiration_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expirationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="inputInput")
    def input_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DevicePostureRuleInput"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DevicePostureRuleInput"]]], jsii.get(self, "inputInput"))

    @builtins.property
    @jsii.member(jsii_name="matchInput")
    def match_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DevicePostureRuleMatch"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DevicePostureRuleMatch"]]], jsii.get(self, "matchInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="scheduleInput")
    def schedule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scheduleInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevicePostureRule, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevicePostureRule, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="expiration")
    def expiration(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expiration"))

    @expiration.setter
    def expiration(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevicePostureRule, "expiration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expiration", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevicePostureRule, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevicePostureRule, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevicePostureRule, "schedule").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedule", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevicePostureRule, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.devicePostureRule.DevicePostureRuleConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "account_id": "accountId",
        "type": "type",
        "description": "description",
        "expiration": "expiration",
        "id": "id",
        "input": "input",
        "match": "match",
        "name": "name",
        "schedule": "schedule",
    },
)
class DevicePostureRuleConfig(cdktf.TerraformMetaArguments):
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
        account_id: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        expiration: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        input: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DevicePostureRuleInput", typing.Dict[str, typing.Any]]]]] = None,
        match: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["DevicePostureRuleMatch", typing.Dict[str, typing.Any]]]]] = None,
        name: typing.Optional[builtins.str] = None,
        schedule: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param account_id: The account identifier to target for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#account_id DevicePostureRule#account_id}
        :param type: The device posture rule type. Available values: ``serial_number``, ``file``, ``application``, ``gateway``, ``warp``, ``domain_joined``, ``os_version``, ``disk_encryption``, ``firewall``, ``workspace_one``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#type DevicePostureRule#type}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#description DevicePostureRule#description}.
        :param expiration: Expire posture results after the specified amount of time. Must be in the format ``1h`` or ``30m``. Valid units are ``h`` and ``m``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#expiration DevicePostureRule#expiration}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#id DevicePostureRule#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param input: input block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#input DevicePostureRule#input}
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#match DevicePostureRule#match}
        :param name: Name of the device posture rule. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#name DevicePostureRule#name}
        :param schedule: Tells the client when to run the device posture check. Must be in the format ``1h`` or ``30m``. Valid units are ``h`` and ``m``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#schedule DevicePostureRule#schedule}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(DevicePostureRuleConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument expiration", value=expiration, expected_type=type_hints["expiration"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument input", value=input, expected_type=type_hints["input"])
            check_type(argname="argument match", value=match, expected_type=type_hints["match"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
        self._values: typing.Dict[str, typing.Any] = {
            "account_id": account_id,
            "type": type,
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
        if expiration is not None:
            self._values["expiration"] = expiration
        if id is not None:
            self._values["id"] = id
        if input is not None:
            self._values["input"] = input
        if match is not None:
            self._values["match"] = match
        if name is not None:
            self._values["name"] = name
        if schedule is not None:
            self._values["schedule"] = schedule

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
    def account_id(self) -> builtins.str:
        '''The account identifier to target for the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#account_id DevicePostureRule#account_id}
        '''
        result = self._values.get("account_id")
        assert result is not None, "Required property 'account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The device posture rule type. Available values: ``serial_number``, ``file``, ``application``, ``gateway``, ``warp``, ``domain_joined``, ``os_version``, ``disk_encryption``, ``firewall``, ``workspace_one``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#type DevicePostureRule#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#description DevicePostureRule#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def expiration(self) -> typing.Optional[builtins.str]:
        '''Expire posture results after the specified amount of time.

        Must be in the format ``1h`` or ``30m``. Valid units are ``h`` and ``m``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#expiration DevicePostureRule#expiration}
        '''
        result = self._values.get("expiration")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#id DevicePostureRule#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DevicePostureRuleInput"]]]:
        '''input block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#input DevicePostureRule#input}
        '''
        result = self._values.get("input")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DevicePostureRuleInput"]]], result)

    @builtins.property
    def match(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DevicePostureRuleMatch"]]]:
        '''match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#match DevicePostureRule#match}
        '''
        result = self._values.get("match")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["DevicePostureRuleMatch"]]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the device posture rule.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#name DevicePostureRule#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedule(self) -> typing.Optional[builtins.str]:
        '''Tells the client when to run the device posture check.

        Must be in the format ``1h`` or ``30m``. Valid units are ``h`` and ``m``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#schedule DevicePostureRule#schedule}
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DevicePostureRuleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.devicePostureRule.DevicePostureRuleInput",
    jsii_struct_bases=[],
    name_mapping={
        "compliance_status": "complianceStatus",
        "connection_id": "connectionId",
        "domain": "domain",
        "enabled": "enabled",
        "exists": "exists",
        "id": "id",
        "operator": "operator",
        "os_distro_name": "osDistroName",
        "os_distro_revision": "osDistroRevision",
        "path": "path",
        "require_all": "requireAll",
        "running": "running",
        "sha256": "sha256",
        "thumbprint": "thumbprint",
        "version": "version",
    },
)
class DevicePostureRuleInput:
    def __init__(
        self,
        *,
        compliance_status: typing.Optional[builtins.str] = None,
        connection_id: typing.Optional[builtins.str] = None,
        domain: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        exists: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        operator: typing.Optional[builtins.str] = None,
        os_distro_name: typing.Optional[builtins.str] = None,
        os_distro_revision: typing.Optional[builtins.str] = None,
        path: typing.Optional[builtins.str] = None,
        require_all: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        running: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        sha256: typing.Optional[builtins.str] = None,
        thumbprint: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param compliance_status: The workspace one device compliance status. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#compliance_status DevicePostureRule#compliance_status}
        :param connection_id: The workspace one connection id. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#connection_id DevicePostureRule#connection_id}
        :param domain: The domain that the client must join. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#domain DevicePostureRule#domain}
        :param enabled: True if the firewall must be enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#enabled DevicePostureRule#enabled}
        :param exists: Checks if the file should exist. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#exists DevicePostureRule#exists}
        :param id: The Teams List id. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#id DevicePostureRule#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param operator: The version comparison operator. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#operator DevicePostureRule#operator}
        :param os_distro_name: The operating system excluding version information. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#os_distro_name DevicePostureRule#os_distro_name}
        :param os_distro_revision: The operating system version excluding OS name information or release name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#os_distro_revision DevicePostureRule#os_distro_revision}
        :param path: The path to the file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#path DevicePostureRule#path}
        :param require_all: True if all drives must be encrypted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#require_all DevicePostureRule#require_all}
        :param running: Checks if the application should be running. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#running DevicePostureRule#running}
        :param sha256: The sha256 hash of the file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#sha256 DevicePostureRule#sha256}
        :param thumbprint: The thumbprint of the file certificate. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#thumbprint DevicePostureRule#thumbprint}
        :param version: The operating system semantic version. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#version DevicePostureRule#version}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DevicePostureRuleInput.__init__)
            check_type(argname="argument compliance_status", value=compliance_status, expected_type=type_hints["compliance_status"])
            check_type(argname="argument connection_id", value=connection_id, expected_type=type_hints["connection_id"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument exists", value=exists, expected_type=type_hints["exists"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument os_distro_name", value=os_distro_name, expected_type=type_hints["os_distro_name"])
            check_type(argname="argument os_distro_revision", value=os_distro_revision, expected_type=type_hints["os_distro_revision"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument require_all", value=require_all, expected_type=type_hints["require_all"])
            check_type(argname="argument running", value=running, expected_type=type_hints["running"])
            check_type(argname="argument sha256", value=sha256, expected_type=type_hints["sha256"])
            check_type(argname="argument thumbprint", value=thumbprint, expected_type=type_hints["thumbprint"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {}
        if compliance_status is not None:
            self._values["compliance_status"] = compliance_status
        if connection_id is not None:
            self._values["connection_id"] = connection_id
        if domain is not None:
            self._values["domain"] = domain
        if enabled is not None:
            self._values["enabled"] = enabled
        if exists is not None:
            self._values["exists"] = exists
        if id is not None:
            self._values["id"] = id
        if operator is not None:
            self._values["operator"] = operator
        if os_distro_name is not None:
            self._values["os_distro_name"] = os_distro_name
        if os_distro_revision is not None:
            self._values["os_distro_revision"] = os_distro_revision
        if path is not None:
            self._values["path"] = path
        if require_all is not None:
            self._values["require_all"] = require_all
        if running is not None:
            self._values["running"] = running
        if sha256 is not None:
            self._values["sha256"] = sha256
        if thumbprint is not None:
            self._values["thumbprint"] = thumbprint
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def compliance_status(self) -> typing.Optional[builtins.str]:
        '''The workspace one device compliance status.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#compliance_status DevicePostureRule#compliance_status}
        '''
        result = self._values.get("compliance_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connection_id(self) -> typing.Optional[builtins.str]:
        '''The workspace one connection id.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#connection_id DevicePostureRule#connection_id}
        '''
        result = self._values.get("connection_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain(self) -> typing.Optional[builtins.str]:
        '''The domain that the client must join.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#domain DevicePostureRule#domain}
        '''
        result = self._values.get("domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''True if the firewall must be enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#enabled DevicePostureRule#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def exists(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Checks if the file should exist.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#exists DevicePostureRule#exists}
        '''
        result = self._values.get("exists")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''The Teams List id.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#id DevicePostureRule#id}

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''The version comparison operator.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#operator DevicePostureRule#operator}
        '''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def os_distro_name(self) -> typing.Optional[builtins.str]:
        '''The operating system excluding version information.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#os_distro_name DevicePostureRule#os_distro_name}
        '''
        result = self._values.get("os_distro_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def os_distro_revision(self) -> typing.Optional[builtins.str]:
        '''The operating system version excluding OS name information or release name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#os_distro_revision DevicePostureRule#os_distro_revision}
        '''
        result = self._values.get("os_distro_revision")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''The path to the file.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#path DevicePostureRule#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def require_all(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''True if all drives must be encrypted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#require_all DevicePostureRule#require_all}
        '''
        result = self._values.get("require_all")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def running(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Checks if the application should be running.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#running DevicePostureRule#running}
        '''
        result = self._values.get("running")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def sha256(self) -> typing.Optional[builtins.str]:
        '''The sha256 hash of the file.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#sha256 DevicePostureRule#sha256}
        '''
        result = self._values.get("sha256")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def thumbprint(self) -> typing.Optional[builtins.str]:
        '''The thumbprint of the file certificate.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#thumbprint DevicePostureRule#thumbprint}
        '''
        result = self._values.get("thumbprint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''The operating system semantic version.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#version DevicePostureRule#version}
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DevicePostureRuleInput(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DevicePostureRuleInputList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.devicePostureRule.DevicePostureRuleInputList",
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
            type_hints = typing.get_type_hints(DevicePostureRuleInputList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DevicePostureRuleInputOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DevicePostureRuleInputList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DevicePostureRuleInputOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevicePostureRuleInputList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DevicePostureRuleInputList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DevicePostureRuleInputList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DevicePostureRuleInput]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DevicePostureRuleInput]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DevicePostureRuleInput]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevicePostureRuleInputList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DevicePostureRuleInputOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.devicePostureRule.DevicePostureRuleInputOutputReference",
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
            type_hints = typing.get_type_hints(DevicePostureRuleInputOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetComplianceStatus")
    def reset_compliance_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetComplianceStatus", []))

    @jsii.member(jsii_name="resetConnectionId")
    def reset_connection_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionId", []))

    @jsii.member(jsii_name="resetDomain")
    def reset_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDomain", []))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetExists")
    def reset_exists(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExists", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

    @jsii.member(jsii_name="resetOsDistroName")
    def reset_os_distro_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOsDistroName", []))

    @jsii.member(jsii_name="resetOsDistroRevision")
    def reset_os_distro_revision(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOsDistroRevision", []))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetRequireAll")
    def reset_require_all(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequireAll", []))

    @jsii.member(jsii_name="resetRunning")
    def reset_running(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRunning", []))

    @jsii.member(jsii_name="resetSha256")
    def reset_sha256(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSha256", []))

    @jsii.member(jsii_name="resetThumbprint")
    def reset_thumbprint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThumbprint", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @builtins.property
    @jsii.member(jsii_name="complianceStatusInput")
    def compliance_status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "complianceStatusInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionIdInput")
    def connection_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionIdInput"))

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
    @jsii.member(jsii_name="existsInput")
    def exists_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "existsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="osDistroNameInput")
    def os_distro_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "osDistroNameInput"))

    @builtins.property
    @jsii.member(jsii_name="osDistroRevisionInput")
    def os_distro_revision_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "osDistroRevisionInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="requireAllInput")
    def require_all_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requireAllInput"))

    @builtins.property
    @jsii.member(jsii_name="runningInput")
    def running_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "runningInput"))

    @builtins.property
    @jsii.member(jsii_name="sha256Input")
    def sha256_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sha256Input"))

    @builtins.property
    @jsii.member(jsii_name="thumbprintInput")
    def thumbprint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "thumbprintInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="complianceStatus")
    def compliance_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "complianceStatus"))

    @compliance_status.setter
    def compliance_status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevicePostureRuleInputOutputReference, "compliance_status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "complianceStatus", value)

    @builtins.property
    @jsii.member(jsii_name="connectionId")
    def connection_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionId"))

    @connection_id.setter
    def connection_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevicePostureRuleInputOutputReference, "connection_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionId", value)

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevicePostureRuleInputOutputReference, "domain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevicePostureRuleInputOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="exists")
    def exists(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "exists"))

    @exists.setter
    def exists(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevicePostureRuleInputOutputReference, "exists").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exists", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevicePostureRuleInputOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevicePostureRuleInputOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="osDistroName")
    def os_distro_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "osDistroName"))

    @os_distro_name.setter
    def os_distro_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevicePostureRuleInputOutputReference, "os_distro_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "osDistroName", value)

    @builtins.property
    @jsii.member(jsii_name="osDistroRevision")
    def os_distro_revision(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "osDistroRevision"))

    @os_distro_revision.setter
    def os_distro_revision(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevicePostureRuleInputOutputReference, "os_distro_revision").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "osDistroRevision", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevicePostureRuleInputOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="requireAll")
    def require_all(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "requireAll"))

    @require_all.setter
    def require_all(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevicePostureRuleInputOutputReference, "require_all").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requireAll", value)

    @builtins.property
    @jsii.member(jsii_name="running")
    def running(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "running"))

    @running.setter
    def running(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevicePostureRuleInputOutputReference, "running").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "running", value)

    @builtins.property
    @jsii.member(jsii_name="sha256")
    def sha256(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sha256"))

    @sha256.setter
    def sha256(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevicePostureRuleInputOutputReference, "sha256").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sha256", value)

    @builtins.property
    @jsii.member(jsii_name="thumbprint")
    def thumbprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "thumbprint"))

    @thumbprint.setter
    def thumbprint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevicePostureRuleInputOutputReference, "thumbprint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "thumbprint", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevicePostureRuleInputOutputReference, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DevicePostureRuleInput, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DevicePostureRuleInput, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DevicePostureRuleInput, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevicePostureRuleInputOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.devicePostureRule.DevicePostureRuleMatch",
    jsii_struct_bases=[],
    name_mapping={"platform": "platform"},
)
class DevicePostureRuleMatch:
    def __init__(self, *, platform: typing.Optional[builtins.str] = None) -> None:
        '''
        :param platform: The platform of the device. Available values: ``windows``, ``mac``, ``linux``, ``android``, ``ios``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#platform DevicePostureRule#platform}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DevicePostureRuleMatch.__init__)
            check_type(argname="argument platform", value=platform, expected_type=type_hints["platform"])
        self._values: typing.Dict[str, typing.Any] = {}
        if platform is not None:
            self._values["platform"] = platform

    @builtins.property
    def platform(self) -> typing.Optional[builtins.str]:
        '''The platform of the device. Available values: ``windows``, ``mac``, ``linux``, ``android``, ``ios``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/device_posture_rule#platform DevicePostureRule#platform}
        '''
        result = self._values.get("platform")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DevicePostureRuleMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DevicePostureRuleMatchList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.devicePostureRule.DevicePostureRuleMatchList",
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
            type_hints = typing.get_type_hints(DevicePostureRuleMatchList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "DevicePostureRuleMatchOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DevicePostureRuleMatchList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("DevicePostureRuleMatchOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevicePostureRuleMatchList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(DevicePostureRuleMatchList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(DevicePostureRuleMatchList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DevicePostureRuleMatch]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DevicePostureRuleMatch]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[DevicePostureRuleMatch]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevicePostureRuleMatchList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class DevicePostureRuleMatchOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.devicePostureRule.DevicePostureRuleMatchOutputReference",
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
            type_hints = typing.get_type_hints(DevicePostureRuleMatchOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPlatform")
    def reset_platform(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlatform", []))

    @builtins.property
    @jsii.member(jsii_name="platformInput")
    def platform_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "platformInput"))

    @builtins.property
    @jsii.member(jsii_name="platform")
    def platform(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "platform"))

    @platform.setter
    def platform(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevicePostureRuleMatchOutputReference, "platform").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "platform", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DevicePostureRuleMatch, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DevicePostureRuleMatch, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DevicePostureRuleMatch, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DevicePostureRuleMatchOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DevicePostureRule",
    "DevicePostureRuleConfig",
    "DevicePostureRuleInput",
    "DevicePostureRuleInputList",
    "DevicePostureRuleInputOutputReference",
    "DevicePostureRuleMatch",
    "DevicePostureRuleMatchList",
    "DevicePostureRuleMatchOutputReference",
]

publication.publish()
