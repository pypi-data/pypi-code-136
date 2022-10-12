'''
# `google_access_context_manager_access_levels`

Refer to the Terraform Registory for docs: [`google_access_context_manager_access_levels`](https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels).
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


class GoogleAccessContextManagerAccessLevels(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerAccessLevels.GoogleAccessContextManagerAccessLevels",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels google_access_context_manager_access_levels}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        parent: builtins.str,
        access_levels: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAccessContextManagerAccessLevelsAccessLevels", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleAccessContextManagerAccessLevelsTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels google_access_context_manager_access_levels} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param parent: The AccessPolicy this AccessLevel lives in. Format: accessPolicies/{policy_id}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#parent GoogleAccessContextManagerAccessLevels#parent}
        :param access_levels: access_levels block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#access_levels GoogleAccessContextManagerAccessLevels#access_levels}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#id GoogleAccessContextManagerAccessLevels#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#timeouts GoogleAccessContextManagerAccessLevels#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerAccessLevels.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleAccessContextManagerAccessLevelsConfig(
            parent=parent,
            access_levels=access_levels,
            id=id,
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

    @jsii.member(jsii_name="putAccessLevels")
    def put_access_levels(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAccessContextManagerAccessLevelsAccessLevels", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerAccessLevels.put_access_levels)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAccessLevels", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#create GoogleAccessContextManagerAccessLevels#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#delete GoogleAccessContextManagerAccessLevels#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#update GoogleAccessContextManagerAccessLevels#update}.
        '''
        value = GoogleAccessContextManagerAccessLevelsTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAccessLevels")
    def reset_access_levels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessLevels", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="accessLevels")
    def access_levels(self) -> "GoogleAccessContextManagerAccessLevelsAccessLevelsList":
        return typing.cast("GoogleAccessContextManagerAccessLevelsAccessLevelsList", jsii.get(self, "accessLevels"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(
        self,
    ) -> "GoogleAccessContextManagerAccessLevelsTimeoutsOutputReference":
        return typing.cast("GoogleAccessContextManagerAccessLevelsTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="accessLevelsInput")
    def access_levels_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerAccessLevelsAccessLevels"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerAccessLevelsAccessLevels"]]], jsii.get(self, "accessLevelsInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="parentInput")
    def parent_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parentInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleAccessContextManagerAccessLevelsTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleAccessContextManagerAccessLevelsTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevels, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="parent")
    def parent(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parent"))

    @parent.setter
    def parent(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevels, "parent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parent", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerAccessLevels.GoogleAccessContextManagerAccessLevelsAccessLevels",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "title": "title",
        "basic": "basic",
        "custom": "custom",
        "description": "description",
    },
)
class GoogleAccessContextManagerAccessLevelsAccessLevels:
    def __init__(
        self,
        *,
        name: builtins.str,
        title: builtins.str,
        basic: typing.Optional[typing.Union["GoogleAccessContextManagerAccessLevelsAccessLevelsBasic", typing.Dict[str, typing.Any]]] = None,
        custom: typing.Optional[typing.Union["GoogleAccessContextManagerAccessLevelsAccessLevelsCustom", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Resource name for the Access Level. The short_name component must begin with a letter and only include alphanumeric and '_'. Format: accessPolicies/{policy_id}/accessLevels/{short_name} Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#name GoogleAccessContextManagerAccessLevels#name}
        :param title: Human readable title. Must be unique within the Policy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#title GoogleAccessContextManagerAccessLevels#title}
        :param basic: basic block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#basic GoogleAccessContextManagerAccessLevels#basic}
        :param custom: custom block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#custom GoogleAccessContextManagerAccessLevels#custom}
        :param description: Description of the AccessLevel and its use. Does not affect behavior. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#description GoogleAccessContextManagerAccessLevels#description}
        '''
        if isinstance(basic, dict):
            basic = GoogleAccessContextManagerAccessLevelsAccessLevelsBasic(**basic)
        if isinstance(custom, dict):
            custom = GoogleAccessContextManagerAccessLevelsAccessLevelsCustom(**custom)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerAccessLevelsAccessLevels.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
            check_type(argname="argument basic", value=basic, expected_type=type_hints["basic"])
            check_type(argname="argument custom", value=custom, expected_type=type_hints["custom"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "title": title,
        }
        if basic is not None:
            self._values["basic"] = basic
        if custom is not None:
            self._values["custom"] = custom
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def name(self) -> builtins.str:
        '''Resource name for the Access Level.

        The short_name component must begin
        with a letter and only include alphanumeric and '_'.
        Format: accessPolicies/{policy_id}/accessLevels/{short_name}

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#name GoogleAccessContextManagerAccessLevels#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def title(self) -> builtins.str:
        '''Human readable title. Must be unique within the Policy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#title GoogleAccessContextManagerAccessLevels#title}
        '''
        result = self._values.get("title")
        assert result is not None, "Required property 'title' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def basic(
        self,
    ) -> typing.Optional["GoogleAccessContextManagerAccessLevelsAccessLevelsBasic"]:
        '''basic block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#basic GoogleAccessContextManagerAccessLevels#basic}
        '''
        result = self._values.get("basic")
        return typing.cast(typing.Optional["GoogleAccessContextManagerAccessLevelsAccessLevelsBasic"], result)

    @builtins.property
    def custom(
        self,
    ) -> typing.Optional["GoogleAccessContextManagerAccessLevelsAccessLevelsCustom"]:
        '''custom block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#custom GoogleAccessContextManagerAccessLevels#custom}
        '''
        result = self._values.get("custom")
        return typing.cast(typing.Optional["GoogleAccessContextManagerAccessLevelsAccessLevelsCustom"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of the AccessLevel and its use. Does not affect behavior.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#description GoogleAccessContextManagerAccessLevels#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerAccessLevelsAccessLevels(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerAccessLevels.GoogleAccessContextManagerAccessLevelsAccessLevelsBasic",
    jsii_struct_bases=[],
    name_mapping={
        "conditions": "conditions",
        "combining_function": "combiningFunction",
    },
)
class GoogleAccessContextManagerAccessLevelsAccessLevelsBasic:
    def __init__(
        self,
        *,
        conditions: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditions", typing.Dict[str, typing.Any]]]],
        combining_function: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param conditions: conditions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#conditions GoogleAccessContextManagerAccessLevels#conditions}
        :param combining_function: How the conditions list should be combined to determine if a request is granted this AccessLevel. If AND is used, each Condition in conditions must be satisfied for the AccessLevel to be applied. If OR is used, at least one Condition in conditions must be satisfied for the AccessLevel to be applied. Default value: "AND" Possible values: ["AND", "OR"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#combining_function GoogleAccessContextManagerAccessLevels#combining_function}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerAccessLevelsAccessLevelsBasic.__init__)
            check_type(argname="argument conditions", value=conditions, expected_type=type_hints["conditions"])
            check_type(argname="argument combining_function", value=combining_function, expected_type=type_hints["combining_function"])
        self._values: typing.Dict[str, typing.Any] = {
            "conditions": conditions,
        }
        if combining_function is not None:
            self._values["combining_function"] = combining_function

    @builtins.property
    def conditions(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditions"]]:
        '''conditions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#conditions GoogleAccessContextManagerAccessLevels#conditions}
        '''
        result = self._values.get("conditions")
        assert result is not None, "Required property 'conditions' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditions"]], result)

    @builtins.property
    def combining_function(self) -> typing.Optional[builtins.str]:
        '''How the conditions list should be combined to determine if a request is granted this AccessLevel.

        If AND is used, each Condition in
        conditions must be satisfied for the AccessLevel to be applied. If
        OR is used, at least one Condition in conditions must be satisfied
        for the AccessLevel to be applied. Default value: "AND" Possible values: ["AND", "OR"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#combining_function GoogleAccessContextManagerAccessLevels#combining_function}
        '''
        result = self._values.get("combining_function")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerAccessLevelsAccessLevelsBasic(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerAccessLevels.GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditions",
    jsii_struct_bases=[],
    name_mapping={
        "device_policy": "devicePolicy",
        "ip_subnetworks": "ipSubnetworks",
        "members": "members",
        "negate": "negate",
        "regions": "regions",
        "required_access_levels": "requiredAccessLevels",
    },
)
class GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditions:
    def __init__(
        self,
        *,
        device_policy: typing.Optional[typing.Union["GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicy", typing.Dict[str, typing.Any]]] = None,
        ip_subnetworks: typing.Optional[typing.Sequence[builtins.str]] = None,
        members: typing.Optional[typing.Sequence[builtins.str]] = None,
        negate: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        required_access_levels: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param device_policy: device_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#device_policy GoogleAccessContextManagerAccessLevels#device_policy}
        :param ip_subnetworks: A list of CIDR block IP subnetwork specification. May be IPv4 or IPv6. Note that for a CIDR IP address block, the specified IP address portion must be properly truncated (i.e. all the host bits must be zero) or the input is considered malformed. For example, "192.0.2.0/24" is accepted but "192.0.2.1/24" is not. Similarly, for IPv6, "2001:db8::/32" is accepted whereas "2001:db8::1/32" is not. The originating IP of a request must be in one of the listed subnets in order for this Condition to be true. If empty, all IP addresses are allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#ip_subnetworks GoogleAccessContextManagerAccessLevels#ip_subnetworks}
        :param members: An allowed list of members (users, service accounts). Using groups is not supported yet. The signed-in user originating the request must be a part of one of the provided members. If not specified, a request may come from any user (logged in/not logged in, not present in any groups, etc.). Formats: 'user:{emailid}', 'serviceAccount:{emailid}' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#members GoogleAccessContextManagerAccessLevels#members}
        :param negate: Whether to negate the Condition. If true, the Condition becomes a NAND over its non-empty fields, each field must be false for the Condition overall to be satisfied. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#negate GoogleAccessContextManagerAccessLevels#negate}
        :param regions: The request must originate from one of the provided countries/regions. Format: A valid ISO 3166-1 alpha-2 code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#regions GoogleAccessContextManagerAccessLevels#regions}
        :param required_access_levels: A list of other access levels defined in the same Policy, referenced by resource name. Referencing an AccessLevel which does not exist is an error. All access levels listed must be granted for the Condition to be true. Format: accessPolicies/{policy_id}/accessLevels/{short_name} Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#required_access_levels GoogleAccessContextManagerAccessLevels#required_access_levels}
        '''
        if isinstance(device_policy, dict):
            device_policy = GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicy(**device_policy)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditions.__init__)
            check_type(argname="argument device_policy", value=device_policy, expected_type=type_hints["device_policy"])
            check_type(argname="argument ip_subnetworks", value=ip_subnetworks, expected_type=type_hints["ip_subnetworks"])
            check_type(argname="argument members", value=members, expected_type=type_hints["members"])
            check_type(argname="argument negate", value=negate, expected_type=type_hints["negate"])
            check_type(argname="argument regions", value=regions, expected_type=type_hints["regions"])
            check_type(argname="argument required_access_levels", value=required_access_levels, expected_type=type_hints["required_access_levels"])
        self._values: typing.Dict[str, typing.Any] = {}
        if device_policy is not None:
            self._values["device_policy"] = device_policy
        if ip_subnetworks is not None:
            self._values["ip_subnetworks"] = ip_subnetworks
        if members is not None:
            self._values["members"] = members
        if negate is not None:
            self._values["negate"] = negate
        if regions is not None:
            self._values["regions"] = regions
        if required_access_levels is not None:
            self._values["required_access_levels"] = required_access_levels

    @builtins.property
    def device_policy(
        self,
    ) -> typing.Optional["GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicy"]:
        '''device_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#device_policy GoogleAccessContextManagerAccessLevels#device_policy}
        '''
        result = self._values.get("device_policy")
        return typing.cast(typing.Optional["GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicy"], result)

    @builtins.property
    def ip_subnetworks(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of CIDR block IP subnetwork specification.

        May be IPv4
        or IPv6.
        Note that for a CIDR IP address block, the specified IP address
        portion must be properly truncated (i.e. all the host bits must
        be zero) or the input is considered malformed. For example,
        "192.0.2.0/24" is accepted but "192.0.2.1/24" is not. Similarly,
        for IPv6, "2001:db8::/32" is accepted whereas "2001:db8::1/32"
        is not. The originating IP of a request must be in one of the
        listed subnets in order for this Condition to be true.
        If empty, all IP addresses are allowed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#ip_subnetworks GoogleAccessContextManagerAccessLevels#ip_subnetworks}
        '''
        result = self._values.get("ip_subnetworks")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def members(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An allowed list of members (users, service accounts). Using groups is not supported yet.

        The signed-in user originating the request must be a part of one
        of the provided members. If not specified, a request may come
        from any user (logged in/not logged in, not present in any
        groups, etc.).
        Formats: 'user:{emailid}', 'serviceAccount:{emailid}'

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#members GoogleAccessContextManagerAccessLevels#members}
        '''
        result = self._values.get("members")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def negate(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to negate the Condition.

        If true, the Condition becomes
        a NAND over its non-empty fields, each field must be false for
        the Condition overall to be satisfied. Defaults to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#negate GoogleAccessContextManagerAccessLevels#negate}
        '''
        result = self._values.get("negate")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The request must originate from one of the provided countries/regions. Format: A valid ISO 3166-1 alpha-2 code.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#regions GoogleAccessContextManagerAccessLevels#regions}
        '''
        result = self._values.get("regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def required_access_levels(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of other access levels defined in the same Policy, referenced by resource name.

        Referencing an AccessLevel which
        does not exist is an error. All access levels listed must be
        granted for the Condition to be true.
        Format: accessPolicies/{policy_id}/accessLevels/{short_name}

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#required_access_levels GoogleAccessContextManagerAccessLevels#required_access_levels}
        '''
        result = self._values.get("required_access_levels")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerAccessLevels.GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicy",
    jsii_struct_bases=[],
    name_mapping={
        "allowed_device_management_levels": "allowedDeviceManagementLevels",
        "allowed_encryption_statuses": "allowedEncryptionStatuses",
        "os_constraints": "osConstraints",
        "require_admin_approval": "requireAdminApproval",
        "require_corp_owned": "requireCorpOwned",
        "require_screen_lock": "requireScreenLock",
    },
)
class GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicy:
    def __init__(
        self,
        *,
        allowed_device_management_levels: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_encryption_statuses: typing.Optional[typing.Sequence[builtins.str]] = None,
        os_constraints: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraints", typing.Dict[str, typing.Any]]]]] = None,
        require_admin_approval: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        require_corp_owned: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        require_screen_lock: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param allowed_device_management_levels: A list of allowed device management levels. An empty list allows all management levels. Possible values: ["MANAGEMENT_UNSPECIFIED", "NONE", "BASIC", "COMPLETE"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#allowed_device_management_levels GoogleAccessContextManagerAccessLevels#allowed_device_management_levels}
        :param allowed_encryption_statuses: A list of allowed encryptions statuses. An empty list allows all statuses. Possible values: ["ENCRYPTION_UNSPECIFIED", "ENCRYPTION_UNSUPPORTED", "UNENCRYPTED", "ENCRYPTED"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#allowed_encryption_statuses GoogleAccessContextManagerAccessLevels#allowed_encryption_statuses}
        :param os_constraints: os_constraints block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#os_constraints GoogleAccessContextManagerAccessLevels#os_constraints}
        :param require_admin_approval: Whether the device needs to be approved by the customer admin. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#require_admin_approval GoogleAccessContextManagerAccessLevels#require_admin_approval}
        :param require_corp_owned: Whether the device needs to be corp owned. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#require_corp_owned GoogleAccessContextManagerAccessLevels#require_corp_owned}
        :param require_screen_lock: Whether or not screenlock is required for the DevicePolicy to be true. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#require_screen_lock GoogleAccessContextManagerAccessLevels#require_screen_lock}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicy.__init__)
            check_type(argname="argument allowed_device_management_levels", value=allowed_device_management_levels, expected_type=type_hints["allowed_device_management_levels"])
            check_type(argname="argument allowed_encryption_statuses", value=allowed_encryption_statuses, expected_type=type_hints["allowed_encryption_statuses"])
            check_type(argname="argument os_constraints", value=os_constraints, expected_type=type_hints["os_constraints"])
            check_type(argname="argument require_admin_approval", value=require_admin_approval, expected_type=type_hints["require_admin_approval"])
            check_type(argname="argument require_corp_owned", value=require_corp_owned, expected_type=type_hints["require_corp_owned"])
            check_type(argname="argument require_screen_lock", value=require_screen_lock, expected_type=type_hints["require_screen_lock"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allowed_device_management_levels is not None:
            self._values["allowed_device_management_levels"] = allowed_device_management_levels
        if allowed_encryption_statuses is not None:
            self._values["allowed_encryption_statuses"] = allowed_encryption_statuses
        if os_constraints is not None:
            self._values["os_constraints"] = os_constraints
        if require_admin_approval is not None:
            self._values["require_admin_approval"] = require_admin_approval
        if require_corp_owned is not None:
            self._values["require_corp_owned"] = require_corp_owned
        if require_screen_lock is not None:
            self._values["require_screen_lock"] = require_screen_lock

    @builtins.property
    def allowed_device_management_levels(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of allowed device management levels. An empty list allows all management levels. Possible values: ["MANAGEMENT_UNSPECIFIED", "NONE", "BASIC", "COMPLETE"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#allowed_device_management_levels GoogleAccessContextManagerAccessLevels#allowed_device_management_levels}
        '''
        result = self._values.get("allowed_device_management_levels")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allowed_encryption_statuses(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of allowed encryptions statuses. An empty list allows all statuses. Possible values: ["ENCRYPTION_UNSPECIFIED", "ENCRYPTION_UNSUPPORTED", "UNENCRYPTED", "ENCRYPTED"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#allowed_encryption_statuses GoogleAccessContextManagerAccessLevels#allowed_encryption_statuses}
        '''
        result = self._values.get("allowed_encryption_statuses")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def os_constraints(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraints"]]]:
        '''os_constraints block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#os_constraints GoogleAccessContextManagerAccessLevels#os_constraints}
        '''
        result = self._values.get("os_constraints")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraints"]]], result)

    @builtins.property
    def require_admin_approval(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the device needs to be approved by the customer admin.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#require_admin_approval GoogleAccessContextManagerAccessLevels#require_admin_approval}
        '''
        result = self._values.get("require_admin_approval")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def require_corp_owned(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether the device needs to be corp owned.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#require_corp_owned GoogleAccessContextManagerAccessLevels#require_corp_owned}
        '''
        result = self._values.get("require_corp_owned")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def require_screen_lock(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether or not screenlock is required for the DevicePolicy to be true. Defaults to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#require_screen_lock GoogleAccessContextManagerAccessLevels#require_screen_lock}
        '''
        result = self._values.get("require_screen_lock")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerAccessLevels.GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraints",
    jsii_struct_bases=[],
    name_mapping={"os_type": "osType", "minimum_version": "minimumVersion"},
)
class GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraints:
    def __init__(
        self,
        *,
        os_type: builtins.str,
        minimum_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param os_type: The operating system type of the device. Possible values: ["OS_UNSPECIFIED", "DESKTOP_MAC", "DESKTOP_WINDOWS", "DESKTOP_LINUX", "DESKTOP_CHROME_OS", "ANDROID", "IOS"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#os_type GoogleAccessContextManagerAccessLevels#os_type}
        :param minimum_version: The minimum allowed OS version. If not set, any version of this OS satisfies the constraint. Format: "major.minor.patch" such as "10.5.301", "9.2.1". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#minimum_version GoogleAccessContextManagerAccessLevels#minimum_version}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraints.__init__)
            check_type(argname="argument os_type", value=os_type, expected_type=type_hints["os_type"])
            check_type(argname="argument minimum_version", value=minimum_version, expected_type=type_hints["minimum_version"])
        self._values: typing.Dict[str, typing.Any] = {
            "os_type": os_type,
        }
        if minimum_version is not None:
            self._values["minimum_version"] = minimum_version

    @builtins.property
    def os_type(self) -> builtins.str:
        '''The operating system type of the device. Possible values: ["OS_UNSPECIFIED", "DESKTOP_MAC", "DESKTOP_WINDOWS", "DESKTOP_LINUX", "DESKTOP_CHROME_OS", "ANDROID", "IOS"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#os_type GoogleAccessContextManagerAccessLevels#os_type}
        '''
        result = self._values.get("os_type")
        assert result is not None, "Required property 'os_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def minimum_version(self) -> typing.Optional[builtins.str]:
        '''The minimum allowed OS version.

        If not set, any version
        of this OS satisfies the constraint.
        Format: "major.minor.patch" such as "10.5.301", "9.2.1".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#minimum_version GoogleAccessContextManagerAccessLevels#minimum_version}
        '''
        result = self._values.get("minimum_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraints(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraintsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerAccessLevels.GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraintsList",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraintsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraintsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraintsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraintsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraintsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraintsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraintsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraints]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraints]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraints]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraintsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraintsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerAccessLevels.GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraintsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraintsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMinimumVersion")
    def reset_minimum_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinimumVersion", []))

    @builtins.property
    @jsii.member(jsii_name="minimumVersionInput")
    def minimum_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "minimumVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="osTypeInput")
    def os_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "osTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="minimumVersion")
    def minimum_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "minimumVersion"))

    @minimum_version.setter
    def minimum_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraintsOutputReference, "minimum_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumVersion", value)

    @builtins.property
    @jsii.member(jsii_name="osType")
    def os_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "osType"))

    @os_type.setter
    def os_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraintsOutputReference, "os_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "osType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraints, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraints, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraints, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraintsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerAccessLevels.GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putOsConstraints")
    def put_os_constraints(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraints, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOutputReference.put_os_constraints)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putOsConstraints", [value]))

    @jsii.member(jsii_name="resetAllowedDeviceManagementLevels")
    def reset_allowed_device_management_levels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedDeviceManagementLevels", []))

    @jsii.member(jsii_name="resetAllowedEncryptionStatuses")
    def reset_allowed_encryption_statuses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedEncryptionStatuses", []))

    @jsii.member(jsii_name="resetOsConstraints")
    def reset_os_constraints(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOsConstraints", []))

    @jsii.member(jsii_name="resetRequireAdminApproval")
    def reset_require_admin_approval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequireAdminApproval", []))

    @jsii.member(jsii_name="resetRequireCorpOwned")
    def reset_require_corp_owned(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequireCorpOwned", []))

    @jsii.member(jsii_name="resetRequireScreenLock")
    def reset_require_screen_lock(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequireScreenLock", []))

    @builtins.property
    @jsii.member(jsii_name="osConstraints")
    def os_constraints(
        self,
    ) -> GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraintsList:
        return typing.cast(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraintsList, jsii.get(self, "osConstraints"))

    @builtins.property
    @jsii.member(jsii_name="allowedDeviceManagementLevelsInput")
    def allowed_device_management_levels_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedDeviceManagementLevelsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedEncryptionStatusesInput")
    def allowed_encryption_statuses_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedEncryptionStatusesInput"))

    @builtins.property
    @jsii.member(jsii_name="osConstraintsInput")
    def os_constraints_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraints]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraints]]], jsii.get(self, "osConstraintsInput"))

    @builtins.property
    @jsii.member(jsii_name="requireAdminApprovalInput")
    def require_admin_approval_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requireAdminApprovalInput"))

    @builtins.property
    @jsii.member(jsii_name="requireCorpOwnedInput")
    def require_corp_owned_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requireCorpOwnedInput"))

    @builtins.property
    @jsii.member(jsii_name="requireScreenLockInput")
    def require_screen_lock_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requireScreenLockInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedDeviceManagementLevels")
    def allowed_device_management_levels(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedDeviceManagementLevels"))

    @allowed_device_management_levels.setter
    def allowed_device_management_levels(
        self,
        value: typing.List[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOutputReference, "allowed_device_management_levels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedDeviceManagementLevels", value)

    @builtins.property
    @jsii.member(jsii_name="allowedEncryptionStatuses")
    def allowed_encryption_statuses(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedEncryptionStatuses"))

    @allowed_encryption_statuses.setter
    def allowed_encryption_statuses(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOutputReference, "allowed_encryption_statuses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedEncryptionStatuses", value)

    @builtins.property
    @jsii.member(jsii_name="requireAdminApproval")
    def require_admin_approval(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "requireAdminApproval"))

    @require_admin_approval.setter
    def require_admin_approval(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOutputReference, "require_admin_approval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requireAdminApproval", value)

    @builtins.property
    @jsii.member(jsii_name="requireCorpOwned")
    def require_corp_owned(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "requireCorpOwned"))

    @require_corp_owned.setter
    def require_corp_owned(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOutputReference, "require_corp_owned").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requireCorpOwned", value)

    @builtins.property
    @jsii.member(jsii_name="requireScreenLock")
    def require_screen_lock(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "requireScreenLock"))

    @require_screen_lock.setter
    def require_screen_lock(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOutputReference, "require_screen_lock").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requireScreenLock", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicy]:
        return typing.cast(typing.Optional[GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerAccessLevels.GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsList",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerAccessLevels.GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDevicePolicy")
    def put_device_policy(
        self,
        *,
        allowed_device_management_levels: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_encryption_statuses: typing.Optional[typing.Sequence[builtins.str]] = None,
        os_constraints: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraints, typing.Dict[str, typing.Any]]]]] = None,
        require_admin_approval: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        require_corp_owned: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        require_screen_lock: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param allowed_device_management_levels: A list of allowed device management levels. An empty list allows all management levels. Possible values: ["MANAGEMENT_UNSPECIFIED", "NONE", "BASIC", "COMPLETE"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#allowed_device_management_levels GoogleAccessContextManagerAccessLevels#allowed_device_management_levels}
        :param allowed_encryption_statuses: A list of allowed encryptions statuses. An empty list allows all statuses. Possible values: ["ENCRYPTION_UNSPECIFIED", "ENCRYPTION_UNSUPPORTED", "UNENCRYPTED", "ENCRYPTED"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#allowed_encryption_statuses GoogleAccessContextManagerAccessLevels#allowed_encryption_statuses}
        :param os_constraints: os_constraints block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#os_constraints GoogleAccessContextManagerAccessLevels#os_constraints}
        :param require_admin_approval: Whether the device needs to be approved by the customer admin. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#require_admin_approval GoogleAccessContextManagerAccessLevels#require_admin_approval}
        :param require_corp_owned: Whether the device needs to be corp owned. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#require_corp_owned GoogleAccessContextManagerAccessLevels#require_corp_owned}
        :param require_screen_lock: Whether or not screenlock is required for the DevicePolicy to be true. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#require_screen_lock GoogleAccessContextManagerAccessLevels#require_screen_lock}
        '''
        value = GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicy(
            allowed_device_management_levels=allowed_device_management_levels,
            allowed_encryption_statuses=allowed_encryption_statuses,
            os_constraints=os_constraints,
            require_admin_approval=require_admin_approval,
            require_corp_owned=require_corp_owned,
            require_screen_lock=require_screen_lock,
        )

        return typing.cast(None, jsii.invoke(self, "putDevicePolicy", [value]))

    @jsii.member(jsii_name="resetDevicePolicy")
    def reset_device_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDevicePolicy", []))

    @jsii.member(jsii_name="resetIpSubnetworks")
    def reset_ip_subnetworks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIpSubnetworks", []))

    @jsii.member(jsii_name="resetMembers")
    def reset_members(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMembers", []))

    @jsii.member(jsii_name="resetNegate")
    def reset_negate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNegate", []))

    @jsii.member(jsii_name="resetRegions")
    def reset_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegions", []))

    @jsii.member(jsii_name="resetRequiredAccessLevels")
    def reset_required_access_levels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequiredAccessLevels", []))

    @builtins.property
    @jsii.member(jsii_name="devicePolicy")
    def device_policy(
        self,
    ) -> GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOutputReference:
        return typing.cast(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOutputReference, jsii.get(self, "devicePolicy"))

    @builtins.property
    @jsii.member(jsii_name="devicePolicyInput")
    def device_policy_input(
        self,
    ) -> typing.Optional[GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicy]:
        return typing.cast(typing.Optional[GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicy], jsii.get(self, "devicePolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="ipSubnetworksInput")
    def ip_subnetworks_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ipSubnetworksInput"))

    @builtins.property
    @jsii.member(jsii_name="membersInput")
    def members_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "membersInput"))

    @builtins.property
    @jsii.member(jsii_name="negateInput")
    def negate_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "negateInput"))

    @builtins.property
    @jsii.member(jsii_name="regionsInput")
    def regions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "regionsInput"))

    @builtins.property
    @jsii.member(jsii_name="requiredAccessLevelsInput")
    def required_access_levels_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "requiredAccessLevelsInput"))

    @builtins.property
    @jsii.member(jsii_name="ipSubnetworks")
    def ip_subnetworks(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ipSubnetworks"))

    @ip_subnetworks.setter
    def ip_subnetworks(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsOutputReference, "ip_subnetworks").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipSubnetworks", value)

    @builtins.property
    @jsii.member(jsii_name="members")
    def members(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "members"))

    @members.setter
    def members(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsOutputReference, "members").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "members", value)

    @builtins.property
    @jsii.member(jsii_name="negate")
    def negate(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "negate"))

    @negate.setter
    def negate(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsOutputReference, "negate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "negate", value)

    @builtins.property
    @jsii.member(jsii_name="regions")
    def regions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "regions"))

    @regions.setter
    def regions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsOutputReference, "regions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regions", value)

    @builtins.property
    @jsii.member(jsii_name="requiredAccessLevels")
    def required_access_levels(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "requiredAccessLevels"))

    @required_access_levels.setter
    def required_access_levels(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsOutputReference, "required_access_levels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requiredAccessLevels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditions, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditions, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditions, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAccessContextManagerAccessLevelsAccessLevelsBasicOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerAccessLevels.GoogleAccessContextManagerAccessLevelsAccessLevelsBasicOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putConditions")
    def put_conditions(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditions, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicOutputReference.put_conditions)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putConditions", [value]))

    @jsii.member(jsii_name="resetCombiningFunction")
    def reset_combining_function(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCombiningFunction", []))

    @builtins.property
    @jsii.member(jsii_name="conditions")
    def conditions(
        self,
    ) -> GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsList:
        return typing.cast(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsList, jsii.get(self, "conditions"))

    @builtins.property
    @jsii.member(jsii_name="combiningFunctionInput")
    def combining_function_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "combiningFunctionInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionsInput")
    def conditions_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditions]]], jsii.get(self, "conditionsInput"))

    @builtins.property
    @jsii.member(jsii_name="combiningFunction")
    def combining_function(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "combiningFunction"))

    @combining_function.setter
    def combining_function(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicOutputReference, "combining_function").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "combiningFunction", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAccessContextManagerAccessLevelsAccessLevelsBasic]:
        return typing.cast(typing.Optional[GoogleAccessContextManagerAccessLevelsAccessLevelsBasic], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAccessContextManagerAccessLevelsAccessLevelsBasic],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerAccessLevels.GoogleAccessContextManagerAccessLevelsAccessLevelsCustom",
    jsii_struct_bases=[],
    name_mapping={"expr": "expr"},
)
class GoogleAccessContextManagerAccessLevelsAccessLevelsCustom:
    def __init__(
        self,
        *,
        expr: typing.Union["GoogleAccessContextManagerAccessLevelsAccessLevelsCustomExpr", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param expr: expr block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#expr GoogleAccessContextManagerAccessLevels#expr}
        '''
        if isinstance(expr, dict):
            expr = GoogleAccessContextManagerAccessLevelsAccessLevelsCustomExpr(**expr)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerAccessLevelsAccessLevelsCustom.__init__)
            check_type(argname="argument expr", value=expr, expected_type=type_hints["expr"])
        self._values: typing.Dict[str, typing.Any] = {
            "expr": expr,
        }

    @builtins.property
    def expr(self) -> "GoogleAccessContextManagerAccessLevelsAccessLevelsCustomExpr":
        '''expr block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#expr GoogleAccessContextManagerAccessLevels#expr}
        '''
        result = self._values.get("expr")
        assert result is not None, "Required property 'expr' is missing"
        return typing.cast("GoogleAccessContextManagerAccessLevelsAccessLevelsCustomExpr", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerAccessLevelsAccessLevelsCustom(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerAccessLevels.GoogleAccessContextManagerAccessLevelsAccessLevelsCustomExpr",
    jsii_struct_bases=[],
    name_mapping={
        "expression": "expression",
        "description": "description",
        "location": "location",
        "title": "title",
    },
)
class GoogleAccessContextManagerAccessLevelsAccessLevelsCustomExpr:
    def __init__(
        self,
        *,
        expression: builtins.str,
        description: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: Textual representation of an expression in Common Expression Language syntax. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#expression GoogleAccessContextManagerAccessLevels#expression}
        :param description: Description of the expression. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#description GoogleAccessContextManagerAccessLevels#description}
        :param location: String indicating the location of the expression for error reporting, e.g. a file name and a position in the file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#location GoogleAccessContextManagerAccessLevels#location}
        :param title: Title for the expression, i.e. a short string describing its purpose. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#title GoogleAccessContextManagerAccessLevels#title}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerAccessLevelsAccessLevelsCustomExpr.__init__)
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument title", value=title, expected_type=type_hints["title"])
        self._values: typing.Dict[str, typing.Any] = {
            "expression": expression,
        }
        if description is not None:
            self._values["description"] = description
        if location is not None:
            self._values["location"] = location
        if title is not None:
            self._values["title"] = title

    @builtins.property
    def expression(self) -> builtins.str:
        '''Textual representation of an expression in Common Expression Language syntax.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#expression GoogleAccessContextManagerAccessLevels#expression}
        '''
        result = self._values.get("expression")
        assert result is not None, "Required property 'expression' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of the expression.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#description GoogleAccessContextManagerAccessLevels#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''String indicating the location of the expression for error reporting, e.g. a file name and a position in the file.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#location GoogleAccessContextManagerAccessLevels#location}
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def title(self) -> typing.Optional[builtins.str]:
        '''Title for the expression, i.e. a short string describing its purpose.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#title GoogleAccessContextManagerAccessLevels#title}
        '''
        result = self._values.get("title")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerAccessLevelsAccessLevelsCustomExpr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAccessContextManagerAccessLevelsAccessLevelsCustomExprOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerAccessLevels.GoogleAccessContextManagerAccessLevelsAccessLevelsCustomExprOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerAccessLevelsAccessLevelsCustomExprOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetTitle")
    def reset_title(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTitle", []))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="expressionInput")
    def expression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expressionInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsCustomExprOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="expression")
    def expression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expression"))

    @expression.setter
    def expression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsCustomExprOutputReference, "expression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expression", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsCustomExprOutputReference, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsCustomExprOutputReference, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAccessContextManagerAccessLevelsAccessLevelsCustomExpr]:
        return typing.cast(typing.Optional[GoogleAccessContextManagerAccessLevelsAccessLevelsCustomExpr], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAccessContextManagerAccessLevelsAccessLevelsCustomExpr],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsCustomExprOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAccessContextManagerAccessLevelsAccessLevelsCustomOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerAccessLevels.GoogleAccessContextManagerAccessLevelsAccessLevelsCustomOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerAccessLevelsAccessLevelsCustomOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putExpr")
    def put_expr(
        self,
        *,
        expression: builtins.str,
        description: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
        title: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param expression: Textual representation of an expression in Common Expression Language syntax. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#expression GoogleAccessContextManagerAccessLevels#expression}
        :param description: Description of the expression. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#description GoogleAccessContextManagerAccessLevels#description}
        :param location: String indicating the location of the expression for error reporting, e.g. a file name and a position in the file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#location GoogleAccessContextManagerAccessLevels#location}
        :param title: Title for the expression, i.e. a short string describing its purpose. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#title GoogleAccessContextManagerAccessLevels#title}
        '''
        value = GoogleAccessContextManagerAccessLevelsAccessLevelsCustomExpr(
            expression=expression,
            description=description,
            location=location,
            title=title,
        )

        return typing.cast(None, jsii.invoke(self, "putExpr", [value]))

    @builtins.property
    @jsii.member(jsii_name="expr")
    def expr(
        self,
    ) -> GoogleAccessContextManagerAccessLevelsAccessLevelsCustomExprOutputReference:
        return typing.cast(GoogleAccessContextManagerAccessLevelsAccessLevelsCustomExprOutputReference, jsii.get(self, "expr"))

    @builtins.property
    @jsii.member(jsii_name="exprInput")
    def expr_input(
        self,
    ) -> typing.Optional[GoogleAccessContextManagerAccessLevelsAccessLevelsCustomExpr]:
        return typing.cast(typing.Optional[GoogleAccessContextManagerAccessLevelsAccessLevelsCustomExpr], jsii.get(self, "exprInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAccessContextManagerAccessLevelsAccessLevelsCustom]:
        return typing.cast(typing.Optional[GoogleAccessContextManagerAccessLevelsAccessLevelsCustom], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAccessContextManagerAccessLevelsAccessLevelsCustom],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsCustomOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAccessContextManagerAccessLevelsAccessLevelsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerAccessLevels.GoogleAccessContextManagerAccessLevelsAccessLevelsList",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerAccessLevelsAccessLevelsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleAccessContextManagerAccessLevelsAccessLevelsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerAccessLevelsAccessLevelsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleAccessContextManagerAccessLevelsAccessLevelsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerAccessLevelsAccessLevels]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerAccessLevelsAccessLevels]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerAccessLevelsAccessLevels]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAccessContextManagerAccessLevelsAccessLevelsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerAccessLevels.GoogleAccessContextManagerAccessLevelsAccessLevelsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerAccessLevelsAccessLevelsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putBasic")
    def put_basic(
        self,
        *,
        conditions: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditions, typing.Dict[str, typing.Any]]]],
        combining_function: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param conditions: conditions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#conditions GoogleAccessContextManagerAccessLevels#conditions}
        :param combining_function: How the conditions list should be combined to determine if a request is granted this AccessLevel. If AND is used, each Condition in conditions must be satisfied for the AccessLevel to be applied. If OR is used, at least one Condition in conditions must be satisfied for the AccessLevel to be applied. Default value: "AND" Possible values: ["AND", "OR"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#combining_function GoogleAccessContextManagerAccessLevels#combining_function}
        '''
        value = GoogleAccessContextManagerAccessLevelsAccessLevelsBasic(
            conditions=conditions, combining_function=combining_function
        )

        return typing.cast(None, jsii.invoke(self, "putBasic", [value]))

    @jsii.member(jsii_name="putCustom")
    def put_custom(
        self,
        *,
        expr: typing.Union[GoogleAccessContextManagerAccessLevelsAccessLevelsCustomExpr, typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param expr: expr block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#expr GoogleAccessContextManagerAccessLevels#expr}
        '''
        value = GoogleAccessContextManagerAccessLevelsAccessLevelsCustom(expr=expr)

        return typing.cast(None, jsii.invoke(self, "putCustom", [value]))

    @jsii.member(jsii_name="resetBasic")
    def reset_basic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBasic", []))

    @jsii.member(jsii_name="resetCustom")
    def reset_custom(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustom", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @builtins.property
    @jsii.member(jsii_name="basic")
    def basic(
        self,
    ) -> GoogleAccessContextManagerAccessLevelsAccessLevelsBasicOutputReference:
        return typing.cast(GoogleAccessContextManagerAccessLevelsAccessLevelsBasicOutputReference, jsii.get(self, "basic"))

    @builtins.property
    @jsii.member(jsii_name="custom")
    def custom(
        self,
    ) -> GoogleAccessContextManagerAccessLevelsAccessLevelsCustomOutputReference:
        return typing.cast(GoogleAccessContextManagerAccessLevelsAccessLevelsCustomOutputReference, jsii.get(self, "custom"))

    @builtins.property
    @jsii.member(jsii_name="basicInput")
    def basic_input(
        self,
    ) -> typing.Optional[GoogleAccessContextManagerAccessLevelsAccessLevelsBasic]:
        return typing.cast(typing.Optional[GoogleAccessContextManagerAccessLevelsAccessLevelsBasic], jsii.get(self, "basicInput"))

    @builtins.property
    @jsii.member(jsii_name="customInput")
    def custom_input(
        self,
    ) -> typing.Optional[GoogleAccessContextManagerAccessLevelsAccessLevelsCustom]:
        return typing.cast(typing.Optional[GoogleAccessContextManagerAccessLevelsAccessLevelsCustom], jsii.get(self, "customInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="titleInput")
    def title_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "titleInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsOutputReference, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="title")
    def title(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "title"))

    @title.setter
    def title(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsOutputReference, "title").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "title", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleAccessContextManagerAccessLevelsAccessLevels, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleAccessContextManagerAccessLevelsAccessLevels, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleAccessContextManagerAccessLevelsAccessLevels, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsAccessLevelsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerAccessLevels.GoogleAccessContextManagerAccessLevelsConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "parent": "parent",
        "access_levels": "accessLevels",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class GoogleAccessContextManagerAccessLevelsConfig(cdktf.TerraformMetaArguments):
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
        parent: builtins.str,
        access_levels: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleAccessContextManagerAccessLevelsAccessLevels, typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleAccessContextManagerAccessLevelsTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param parent: The AccessPolicy this AccessLevel lives in. Format: accessPolicies/{policy_id}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#parent GoogleAccessContextManagerAccessLevels#parent}
        :param access_levels: access_levels block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#access_levels GoogleAccessContextManagerAccessLevels#access_levels}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#id GoogleAccessContextManagerAccessLevels#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#timeouts GoogleAccessContextManagerAccessLevels#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = GoogleAccessContextManagerAccessLevelsTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerAccessLevelsConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument parent", value=parent, expected_type=type_hints["parent"])
            check_type(argname="argument access_levels", value=access_levels, expected_type=type_hints["access_levels"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "parent": parent,
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
        if access_levels is not None:
            self._values["access_levels"] = access_levels
        if id is not None:
            self._values["id"] = id
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
    def parent(self) -> builtins.str:
        '''The AccessPolicy this AccessLevel lives in. Format: accessPolicies/{policy_id}.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#parent GoogleAccessContextManagerAccessLevels#parent}
        '''
        result = self._values.get("parent")
        assert result is not None, "Required property 'parent' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_levels(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerAccessLevelsAccessLevels]]]:
        '''access_levels block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#access_levels GoogleAccessContextManagerAccessLevels#access_levels}
        '''
        result = self._values.get("access_levels")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAccessContextManagerAccessLevelsAccessLevels]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#id GoogleAccessContextManagerAccessLevels#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(
        self,
    ) -> typing.Optional["GoogleAccessContextManagerAccessLevelsTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#timeouts GoogleAccessContextManagerAccessLevels#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleAccessContextManagerAccessLevelsTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerAccessLevelsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerAccessLevels.GoogleAccessContextManagerAccessLevelsTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleAccessContextManagerAccessLevelsTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#create GoogleAccessContextManagerAccessLevels#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#delete GoogleAccessContextManagerAccessLevels#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#update GoogleAccessContextManagerAccessLevels#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAccessContextManagerAccessLevelsTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#create GoogleAccessContextManagerAccessLevels#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#delete GoogleAccessContextManagerAccessLevels#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_access_context_manager_access_levels#update GoogleAccessContextManagerAccessLevels#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAccessContextManagerAccessLevelsTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAccessContextManagerAccessLevelsTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAccessContextManagerAccessLevels.GoogleAccessContextManagerAccessLevelsTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAccessContextManagerAccessLevelsTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleAccessContextManagerAccessLevelsTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleAccessContextManagerAccessLevelsTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleAccessContextManagerAccessLevelsTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAccessContextManagerAccessLevelsTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleAccessContextManagerAccessLevels",
    "GoogleAccessContextManagerAccessLevelsAccessLevels",
    "GoogleAccessContextManagerAccessLevelsAccessLevelsBasic",
    "GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditions",
    "GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicy",
    "GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraints",
    "GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraintsList",
    "GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOsConstraintsOutputReference",
    "GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsDevicePolicyOutputReference",
    "GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsList",
    "GoogleAccessContextManagerAccessLevelsAccessLevelsBasicConditionsOutputReference",
    "GoogleAccessContextManagerAccessLevelsAccessLevelsBasicOutputReference",
    "GoogleAccessContextManagerAccessLevelsAccessLevelsCustom",
    "GoogleAccessContextManagerAccessLevelsAccessLevelsCustomExpr",
    "GoogleAccessContextManagerAccessLevelsAccessLevelsCustomExprOutputReference",
    "GoogleAccessContextManagerAccessLevelsAccessLevelsCustomOutputReference",
    "GoogleAccessContextManagerAccessLevelsAccessLevelsList",
    "GoogleAccessContextManagerAccessLevelsAccessLevelsOutputReference",
    "GoogleAccessContextManagerAccessLevelsConfig",
    "GoogleAccessContextManagerAccessLevelsTimeouts",
    "GoogleAccessContextManagerAccessLevelsTimeoutsOutputReference",
]

publication.publish()
