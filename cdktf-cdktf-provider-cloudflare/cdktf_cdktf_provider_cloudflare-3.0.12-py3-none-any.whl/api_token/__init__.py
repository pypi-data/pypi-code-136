'''
# `cloudflare_api_token`

Refer to the Terraform Registory for docs: [`cloudflare_api_token`](https://www.terraform.io/docs/providers/cloudflare/r/api_token).
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


class ApiToken(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.apiToken.ApiToken",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token cloudflare_api_token}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        policy: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiTokenPolicy", typing.Dict[str, typing.Any]]]],
        condition: typing.Optional[typing.Union["ApiTokenCondition", typing.Dict[str, typing.Any]]] = None,
        expires_on: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        not_before: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token cloudflare_api_token} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Name of the API Token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token#name ApiToken#name}
        :param policy: policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token#policy ApiToken#policy}
        :param condition: condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token#condition ApiToken#condition}
        :param expires_on: The expiration time on or after which the token MUST NOT be accepted for processing. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token#expires_on ApiToken#expires_on}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token#id ApiToken#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param not_before: The time before which the token MUST NOT be accepted for processing. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token#not_before ApiToken#not_before}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiToken.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ApiTokenConfig(
            name=name,
            policy=policy,
            condition=condition,
            expires_on=expires_on,
            id=id,
            not_before=not_before,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCondition")
    def put_condition(
        self,
        *,
        request_ip: typing.Optional[typing.Union["ApiTokenConditionRequestIp", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param request_ip: request_ip block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token#request_ip ApiToken#request_ip}
        '''
        value = ApiTokenCondition(request_ip=request_ip)

        return typing.cast(None, jsii.invoke(self, "putCondition", [value]))

    @jsii.member(jsii_name="putPolicy")
    def put_policy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiTokenPolicy", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiToken.put_policy)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPolicy", [value]))

    @jsii.member(jsii_name="resetCondition")
    def reset_condition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCondition", []))

    @jsii.member(jsii_name="resetExpiresOn")
    def reset_expires_on(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpiresOn", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNotBefore")
    def reset_not_before(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotBefore", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="condition")
    def condition(self) -> "ApiTokenConditionOutputReference":
        return typing.cast("ApiTokenConditionOutputReference", jsii.get(self, "condition"))

    @builtins.property
    @jsii.member(jsii_name="issuedOn")
    def issued_on(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issuedOn"))

    @builtins.property
    @jsii.member(jsii_name="modifiedOn")
    def modified_on(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "modifiedOn"))

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> "ApiTokenPolicyList":
        return typing.cast("ApiTokenPolicyList", jsii.get(self, "policy"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @builtins.property
    @jsii.member(jsii_name="conditionInput")
    def condition_input(self) -> typing.Optional["ApiTokenCondition"]:
        return typing.cast(typing.Optional["ApiTokenCondition"], jsii.get(self, "conditionInput"))

    @builtins.property
    @jsii.member(jsii_name="expiresOnInput")
    def expires_on_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expiresOnInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="notBeforeInput")
    def not_before_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notBeforeInput"))

    @builtins.property
    @jsii.member(jsii_name="policyInput")
    def policy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiTokenPolicy"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ApiTokenPolicy"]]], jsii.get(self, "policyInput"))

    @builtins.property
    @jsii.member(jsii_name="expiresOn")
    def expires_on(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expiresOn"))

    @expires_on.setter
    def expires_on(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiToken, "expires_on").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expiresOn", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiToken, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiToken, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="notBefore")
    def not_before(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notBefore"))

    @not_before.setter
    def not_before(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiToken, "not_before").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notBefore", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.apiToken.ApiTokenCondition",
    jsii_struct_bases=[],
    name_mapping={"request_ip": "requestIp"},
)
class ApiTokenCondition:
    def __init__(
        self,
        *,
        request_ip: typing.Optional[typing.Union["ApiTokenConditionRequestIp", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param request_ip: request_ip block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token#request_ip ApiToken#request_ip}
        '''
        if isinstance(request_ip, dict):
            request_ip = ApiTokenConditionRequestIp(**request_ip)
        if __debug__:
            type_hints = typing.get_type_hints(ApiTokenCondition.__init__)
            check_type(argname="argument request_ip", value=request_ip, expected_type=type_hints["request_ip"])
        self._values: typing.Dict[str, typing.Any] = {}
        if request_ip is not None:
            self._values["request_ip"] = request_ip

    @builtins.property
    def request_ip(self) -> typing.Optional["ApiTokenConditionRequestIp"]:
        '''request_ip block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token#request_ip ApiToken#request_ip}
        '''
        result = self._values.get("request_ip")
        return typing.cast(typing.Optional["ApiTokenConditionRequestIp"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiTokenCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiTokenConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.apiToken.ApiTokenConditionOutputReference",
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
            type_hints = typing.get_type_hints(ApiTokenConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRequestIp")
    def put_request_ip(
        self,
        *,
        in_: typing.Optional[typing.Sequence[builtins.str]] = None,
        not_in: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param in_: List of IP addresses or CIDR notation where the token may be used from. If not specified, the token will be valid for all IP addresses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token#in ApiToken#in}
        :param not_in: List of IP addresses or CIDR notation where the token should not be used from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token#not_in ApiToken#not_in}
        '''
        value = ApiTokenConditionRequestIp(in_=in_, not_in=not_in)

        return typing.cast(None, jsii.invoke(self, "putRequestIp", [value]))

    @jsii.member(jsii_name="resetRequestIp")
    def reset_request_ip(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequestIp", []))

    @builtins.property
    @jsii.member(jsii_name="requestIp")
    def request_ip(self) -> "ApiTokenConditionRequestIpOutputReference":
        return typing.cast("ApiTokenConditionRequestIpOutputReference", jsii.get(self, "requestIp"))

    @builtins.property
    @jsii.member(jsii_name="requestIpInput")
    def request_ip_input(self) -> typing.Optional["ApiTokenConditionRequestIp"]:
        return typing.cast(typing.Optional["ApiTokenConditionRequestIp"], jsii.get(self, "requestIpInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApiTokenCondition]:
        return typing.cast(typing.Optional[ApiTokenCondition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ApiTokenCondition]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiTokenConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.apiToken.ApiTokenConditionRequestIp",
    jsii_struct_bases=[],
    name_mapping={"in_": "in", "not_in": "notIn"},
)
class ApiTokenConditionRequestIp:
    def __init__(
        self,
        *,
        in_: typing.Optional[typing.Sequence[builtins.str]] = None,
        not_in: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param in_: List of IP addresses or CIDR notation where the token may be used from. If not specified, the token will be valid for all IP addresses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token#in ApiToken#in}
        :param not_in: List of IP addresses or CIDR notation where the token should not be used from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token#not_in ApiToken#not_in}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiTokenConditionRequestIp.__init__)
            check_type(argname="argument in_", value=in_, expected_type=type_hints["in_"])
            check_type(argname="argument not_in", value=not_in, expected_type=type_hints["not_in"])
        self._values: typing.Dict[str, typing.Any] = {}
        if in_ is not None:
            self._values["in_"] = in_
        if not_in is not None:
            self._values["not_in"] = not_in

    @builtins.property
    def in_(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of IP addresses or CIDR notation where the token may be used from.

        If not specified, the token will be valid for all IP addresses.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token#in ApiToken#in}
        '''
        result = self._values.get("in_")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def not_in(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of IP addresses or CIDR notation where the token should not be used from.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token#not_in ApiToken#not_in}
        '''
        result = self._values.get("not_in")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiTokenConditionRequestIp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiTokenConditionRequestIpOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.apiToken.ApiTokenConditionRequestIpOutputReference",
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
            type_hints = typing.get_type_hints(ApiTokenConditionRequestIpOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIn")
    def reset_in(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIn", []))

    @jsii.member(jsii_name="resetNotIn")
    def reset_not_in(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotIn", []))

    @builtins.property
    @jsii.member(jsii_name="inInput")
    def in_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "inInput"))

    @builtins.property
    @jsii.member(jsii_name="notInInput")
    def not_in_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "notInInput"))

    @builtins.property
    @jsii.member(jsii_name="in")
    def in_(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "in"))

    @in_.setter
    def in_(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiTokenConditionRequestIpOutputReference, "in_").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "in", value)

    @builtins.property
    @jsii.member(jsii_name="notIn")
    def not_in(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "notIn"))

    @not_in.setter
    def not_in(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiTokenConditionRequestIpOutputReference, "not_in").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notIn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ApiTokenConditionRequestIp]:
        return typing.cast(typing.Optional[ApiTokenConditionRequestIp], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ApiTokenConditionRequestIp],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiTokenConditionRequestIpOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.apiToken.ApiTokenConfig",
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
        "policy": "policy",
        "condition": "condition",
        "expires_on": "expiresOn",
        "id": "id",
        "not_before": "notBefore",
    },
)
class ApiTokenConfig(cdktf.TerraformMetaArguments):
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
        policy: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ApiTokenPolicy", typing.Dict[str, typing.Any]]]],
        condition: typing.Optional[typing.Union[ApiTokenCondition, typing.Dict[str, typing.Any]]] = None,
        expires_on: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        not_before: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Name of the API Token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token#name ApiToken#name}
        :param policy: policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token#policy ApiToken#policy}
        :param condition: condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token#condition ApiToken#condition}
        :param expires_on: The expiration time on or after which the token MUST NOT be accepted for processing. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token#expires_on ApiToken#expires_on}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token#id ApiToken#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param not_before: The time before which the token MUST NOT be accepted for processing. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token#not_before ApiToken#not_before}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(condition, dict):
            condition = ApiTokenCondition(**condition)
        if __debug__:
            type_hints = typing.get_type_hints(ApiTokenConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
            check_type(argname="argument expires_on", value=expires_on, expected_type=type_hints["expires_on"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument not_before", value=not_before, expected_type=type_hints["not_before"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "policy": policy,
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
        if condition is not None:
            self._values["condition"] = condition
        if expires_on is not None:
            self._values["expires_on"] = expires_on
        if id is not None:
            self._values["id"] = id
        if not_before is not None:
            self._values["not_before"] = not_before

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
        '''Name of the API Token.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token#name ApiToken#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def policy(self) -> typing.Union[cdktf.IResolvable, typing.List["ApiTokenPolicy"]]:
        '''policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token#policy ApiToken#policy}
        '''
        result = self._values.get("policy")
        assert result is not None, "Required property 'policy' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["ApiTokenPolicy"]], result)

    @builtins.property
    def condition(self) -> typing.Optional[ApiTokenCondition]:
        '''condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token#condition ApiToken#condition}
        '''
        result = self._values.get("condition")
        return typing.cast(typing.Optional[ApiTokenCondition], result)

    @builtins.property
    def expires_on(self) -> typing.Optional[builtins.str]:
        '''The expiration time on or after which the token MUST NOT be accepted for processing.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token#expires_on ApiToken#expires_on}
        '''
        result = self._values.get("expires_on")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token#id ApiToken#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def not_before(self) -> typing.Optional[builtins.str]:
        '''The time before which the token MUST NOT be accepted for processing.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token#not_before ApiToken#not_before}
        '''
        result = self._values.get("not_before")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiTokenConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.apiToken.ApiTokenPolicy",
    jsii_struct_bases=[],
    name_mapping={
        "permission_groups": "permissionGroups",
        "resources": "resources",
        "effect": "effect",
    },
)
class ApiTokenPolicy:
    def __init__(
        self,
        *,
        permission_groups: typing.Sequence[builtins.str],
        resources: typing.Mapping[builtins.str, builtins.str],
        effect: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param permission_groups: List of permissions groups IDs. See `documentation <https://developers.cloudflare.com/api/tokens/create/permissions>`_ for more information. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token#permission_groups ApiToken#permission_groups}
        :param resources: Describes what operations against which resources are allowed or denied. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token#resources ApiToken#resources}
        :param effect: Effect of the policy. Available values: ``allow``, ``deny``. Defaults to ``allow``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token#effect ApiToken#effect}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiTokenPolicy.__init__)
            check_type(argname="argument permission_groups", value=permission_groups, expected_type=type_hints["permission_groups"])
            check_type(argname="argument resources", value=resources, expected_type=type_hints["resources"])
            check_type(argname="argument effect", value=effect, expected_type=type_hints["effect"])
        self._values: typing.Dict[str, typing.Any] = {
            "permission_groups": permission_groups,
            "resources": resources,
        }
        if effect is not None:
            self._values["effect"] = effect

    @builtins.property
    def permission_groups(self) -> typing.List[builtins.str]:
        '''List of permissions groups IDs. See `documentation <https://developers.cloudflare.com/api/tokens/create/permissions>`_ for more information.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token#permission_groups ApiToken#permission_groups}
        '''
        result = self._values.get("permission_groups")
        assert result is not None, "Required property 'permission_groups' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def resources(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''Describes what operations against which resources are allowed or denied.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token#resources ApiToken#resources}
        '''
        result = self._values.get("resources")
        assert result is not None, "Required property 'resources' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    @builtins.property
    def effect(self) -> typing.Optional[builtins.str]:
        '''Effect of the policy. Available values: ``allow``, ``deny``. Defaults to ``allow``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/api_token#effect ApiToken#effect}
        '''
        result = self._values.get("effect")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApiTokenPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ApiTokenPolicyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.apiToken.ApiTokenPolicyList",
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
            type_hints = typing.get_type_hints(ApiTokenPolicyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ApiTokenPolicyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ApiTokenPolicyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ApiTokenPolicyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiTokenPolicyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiTokenPolicyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ApiTokenPolicyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiTokenPolicy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiTokenPolicy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ApiTokenPolicy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiTokenPolicyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ApiTokenPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.apiToken.ApiTokenPolicyOutputReference",
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
            type_hints = typing.get_type_hints(ApiTokenPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEffect")
    def reset_effect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEffect", []))

    @builtins.property
    @jsii.member(jsii_name="effectInput")
    def effect_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "effectInput"))

    @builtins.property
    @jsii.member(jsii_name="permissionGroupsInput")
    def permission_groups_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "permissionGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="resourcesInput")
    def resources_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "resourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="effect")
    def effect(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "effect"))

    @effect.setter
    def effect(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiTokenPolicyOutputReference, "effect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "effect", value)

    @builtins.property
    @jsii.member(jsii_name="permissionGroups")
    def permission_groups(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "permissionGroups"))

    @permission_groups.setter
    def permission_groups(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiTokenPolicyOutputReference, "permission_groups").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionGroups", value)

    @builtins.property
    @jsii.member(jsii_name="resources")
    def resources(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "resources"))

    @resources.setter
    def resources(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiTokenPolicyOutputReference, "resources").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resources", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ApiTokenPolicy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ApiTokenPolicy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ApiTokenPolicy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ApiTokenPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ApiToken",
    "ApiTokenCondition",
    "ApiTokenConditionOutputReference",
    "ApiTokenConditionRequestIp",
    "ApiTokenConditionRequestIpOutputReference",
    "ApiTokenConfig",
    "ApiTokenPolicy",
    "ApiTokenPolicyList",
    "ApiTokenPolicyOutputReference",
]

publication.publish()
