'''
# `cloudflare_rate_limit`

Refer to the Terraform Registory for docs: [`cloudflare_rate_limit`](https://www.terraform.io/docs/providers/cloudflare/r/rate_limit).
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


class RateLimit(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.rateLimit.RateLimit",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit cloudflare_rate_limit}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        action: typing.Union["RateLimitAction", typing.Dict[str, typing.Any]],
        period: jsii.Number,
        threshold: jsii.Number,
        zone_id: builtins.str,
        bypass_url_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        correlate: typing.Optional[typing.Union["RateLimitCorrelate", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        match: typing.Optional[typing.Union["RateLimitMatch", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit cloudflare_rate_limit} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#action RateLimit#action}
        :param period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#period RateLimit#period}.
        :param threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#threshold RateLimit#threshold}.
        :param zone_id: The zone identifier to target for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#zone_id RateLimit#zone_id}
        :param bypass_url_patterns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#bypass_url_patterns RateLimit#bypass_url_patterns}.
        :param correlate: correlate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#correlate RateLimit#correlate}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#description RateLimit#description}.
        :param disabled: Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#disabled RateLimit#disabled}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#id RateLimit#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#match RateLimit#match}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RateLimit.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = RateLimitConfig(
            action=action,
            period=period,
            threshold=threshold,
            zone_id=zone_id,
            bypass_url_patterns=bypass_url_patterns,
            correlate=correlate,
            description=description,
            disabled=disabled,
            id=id,
            match=match,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAction")
    def put_action(
        self,
        *,
        mode: builtins.str,
        response: typing.Optional[typing.Union["RateLimitActionResponse", typing.Dict[str, typing.Any]]] = None,
        timeout: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#mode RateLimit#mode}.
        :param response: response block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#response RateLimit#response}
        :param timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#timeout RateLimit#timeout}.
        '''
        value = RateLimitAction(mode=mode, response=response, timeout=timeout)

        return typing.cast(None, jsii.invoke(self, "putAction", [value]))

    @jsii.member(jsii_name="putCorrelate")
    def put_correlate(self, *, by: typing.Optional[builtins.str] = None) -> None:
        '''
        :param by: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#by RateLimit#by}.
        '''
        value = RateLimitCorrelate(by=by)

        return typing.cast(None, jsii.invoke(self, "putCorrelate", [value]))

    @jsii.member(jsii_name="putMatch")
    def put_match(
        self,
        *,
        request: typing.Optional[typing.Union["RateLimitMatchRequest", typing.Dict[str, typing.Any]]] = None,
        response: typing.Optional[typing.Union["RateLimitMatchResponse", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param request: request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#request RateLimit#request}
        :param response: response block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#response RateLimit#response}
        '''
        value = RateLimitMatch(request=request, response=response)

        return typing.cast(None, jsii.invoke(self, "putMatch", [value]))

    @jsii.member(jsii_name="resetBypassUrlPatterns")
    def reset_bypass_url_patterns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBypassUrlPatterns", []))

    @jsii.member(jsii_name="resetCorrelate")
    def reset_correlate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCorrelate", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDisabled")
    def reset_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisabled", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetMatch")
    def reset_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatch", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> "RateLimitActionOutputReference":
        return typing.cast("RateLimitActionOutputReference", jsii.get(self, "action"))

    @builtins.property
    @jsii.member(jsii_name="correlate")
    def correlate(self) -> "RateLimitCorrelateOutputReference":
        return typing.cast("RateLimitCorrelateOutputReference", jsii.get(self, "correlate"))

    @builtins.property
    @jsii.member(jsii_name="match")
    def match(self) -> "RateLimitMatchOutputReference":
        return typing.cast("RateLimitMatchOutputReference", jsii.get(self, "match"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional["RateLimitAction"]:
        return typing.cast(typing.Optional["RateLimitAction"], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="bypassUrlPatternsInput")
    def bypass_url_patterns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "bypassUrlPatternsInput"))

    @builtins.property
    @jsii.member(jsii_name="correlateInput")
    def correlate_input(self) -> typing.Optional["RateLimitCorrelate"]:
        return typing.cast(typing.Optional["RateLimitCorrelate"], jsii.get(self, "correlateInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="disabledInput")
    def disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disabledInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="matchInput")
    def match_input(self) -> typing.Optional["RateLimitMatch"]:
        return typing.cast(typing.Optional["RateLimitMatch"], jsii.get(self, "matchInput"))

    @builtins.property
    @jsii.member(jsii_name="periodInput")
    def period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "periodInput"))

    @builtins.property
    @jsii.member(jsii_name="thresholdInput")
    def threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "thresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneIdInput")
    def zone_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneIdInput"))

    @builtins.property
    @jsii.member(jsii_name="bypassUrlPatterns")
    def bypass_url_patterns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "bypassUrlPatterns"))

    @bypass_url_patterns.setter
    def bypass_url_patterns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RateLimit, "bypass_url_patterns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bypassUrlPatterns", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RateLimit, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="disabled")
    def disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disabled"))

    @disabled.setter
    def disabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RateLimit, "disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RateLimit, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="period")
    def period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "period"))

    @period.setter
    def period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RateLimit, "period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "period", value)

    @builtins.property
    @jsii.member(jsii_name="threshold")
    def threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "threshold"))

    @threshold.setter
    def threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RateLimit, "threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "threshold", value)

    @builtins.property
    @jsii.member(jsii_name="zoneId")
    def zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zoneId"))

    @zone_id.setter
    def zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RateLimit, "zone_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.rateLimit.RateLimitAction",
    jsii_struct_bases=[],
    name_mapping={"mode": "mode", "response": "response", "timeout": "timeout"},
)
class RateLimitAction:
    def __init__(
        self,
        *,
        mode: builtins.str,
        response: typing.Optional[typing.Union["RateLimitActionResponse", typing.Dict[str, typing.Any]]] = None,
        timeout: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#mode RateLimit#mode}.
        :param response: response block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#response RateLimit#response}
        :param timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#timeout RateLimit#timeout}.
        '''
        if isinstance(response, dict):
            response = RateLimitActionResponse(**response)
        if __debug__:
            type_hints = typing.get_type_hints(RateLimitAction.__init__)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument response", value=response, expected_type=type_hints["response"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
        self._values: typing.Dict[str, typing.Any] = {
            "mode": mode,
        }
        if response is not None:
            self._values["response"] = response
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#mode RateLimit#mode}.'''
        result = self._values.get("mode")
        assert result is not None, "Required property 'mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def response(self) -> typing.Optional["RateLimitActionResponse"]:
        '''response block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#response RateLimit#response}
        '''
        result = self._values.get("response")
        return typing.cast(typing.Optional["RateLimitActionResponse"], result)

    @builtins.property
    def timeout(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#timeout RateLimit#timeout}.'''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RateLimitAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RateLimitActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.rateLimit.RateLimitActionOutputReference",
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
            type_hints = typing.get_type_hints(RateLimitActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putResponse")
    def put_response(self, *, body: builtins.str, content_type: builtins.str) -> None:
        '''
        :param body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#body RateLimit#body}.
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#content_type RateLimit#content_type}.
        '''
        value = RateLimitActionResponse(body=body, content_type=content_type)

        return typing.cast(None, jsii.invoke(self, "putResponse", [value]))

    @jsii.member(jsii_name="resetResponse")
    def reset_response(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponse", []))

    @jsii.member(jsii_name="resetTimeout")
    def reset_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeout", []))

    @builtins.property
    @jsii.member(jsii_name="response")
    def response(self) -> "RateLimitActionResponseOutputReference":
        return typing.cast("RateLimitActionResponseOutputReference", jsii.get(self, "response"))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="responseInput")
    def response_input(self) -> typing.Optional["RateLimitActionResponse"]:
        return typing.cast(typing.Optional["RateLimitActionResponse"], jsii.get(self, "responseInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutInput")
    def timeout_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RateLimitActionOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RateLimitActionOutputReference, "timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RateLimitAction]:
        return typing.cast(typing.Optional[RateLimitAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[RateLimitAction]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RateLimitActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.rateLimit.RateLimitActionResponse",
    jsii_struct_bases=[],
    name_mapping={"body": "body", "content_type": "contentType"},
)
class RateLimitActionResponse:
    def __init__(self, *, body: builtins.str, content_type: builtins.str) -> None:
        '''
        :param body: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#body RateLimit#body}.
        :param content_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#content_type RateLimit#content_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RateLimitActionResponse.__init__)
            check_type(argname="argument body", value=body, expected_type=type_hints["body"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "body": body,
            "content_type": content_type,
        }

    @builtins.property
    def body(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#body RateLimit#body}.'''
        result = self._values.get("body")
        assert result is not None, "Required property 'body' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#content_type RateLimit#content_type}.'''
        result = self._values.get("content_type")
        assert result is not None, "Required property 'content_type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RateLimitActionResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RateLimitActionResponseOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.rateLimit.RateLimitActionResponseOutputReference",
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
            type_hints = typing.get_type_hints(RateLimitActionResponseOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="bodyInput")
    def body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bodyInput"))

    @builtins.property
    @jsii.member(jsii_name="contentTypeInput")
    def content_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="body")
    def body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "body"))

    @body.setter
    def body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RateLimitActionResponseOutputReference, "body").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "body", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RateLimitActionResponseOutputReference, "content_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RateLimitActionResponse]:
        return typing.cast(typing.Optional[RateLimitActionResponse], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[RateLimitActionResponse]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RateLimitActionResponseOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.rateLimit.RateLimitConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "action": "action",
        "period": "period",
        "threshold": "threshold",
        "zone_id": "zoneId",
        "bypass_url_patterns": "bypassUrlPatterns",
        "correlate": "correlate",
        "description": "description",
        "disabled": "disabled",
        "id": "id",
        "match": "match",
    },
)
class RateLimitConfig(cdktf.TerraformMetaArguments):
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
        action: typing.Union[RateLimitAction, typing.Dict[str, typing.Any]],
        period: jsii.Number,
        threshold: jsii.Number,
        zone_id: builtins.str,
        bypass_url_patterns: typing.Optional[typing.Sequence[builtins.str]] = None,
        correlate: typing.Optional[typing.Union["RateLimitCorrelate", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        match: typing.Optional[typing.Union["RateLimitMatch", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#action RateLimit#action}
        :param period: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#period RateLimit#period}.
        :param threshold: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#threshold RateLimit#threshold}.
        :param zone_id: The zone identifier to target for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#zone_id RateLimit#zone_id}
        :param bypass_url_patterns: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#bypass_url_patterns RateLimit#bypass_url_patterns}.
        :param correlate: correlate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#correlate RateLimit#correlate}
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#description RateLimit#description}.
        :param disabled: Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#disabled RateLimit#disabled}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#id RateLimit#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param match: match block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#match RateLimit#match}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(action, dict):
            action = RateLimitAction(**action)
        if isinstance(correlate, dict):
            correlate = RateLimitCorrelate(**correlate)
        if isinstance(match, dict):
            match = RateLimitMatch(**match)
        if __debug__:
            type_hints = typing.get_type_hints(RateLimitConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument period", value=period, expected_type=type_hints["period"])
            check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
            check_type(argname="argument zone_id", value=zone_id, expected_type=type_hints["zone_id"])
            check_type(argname="argument bypass_url_patterns", value=bypass_url_patterns, expected_type=type_hints["bypass_url_patterns"])
            check_type(argname="argument correlate", value=correlate, expected_type=type_hints["correlate"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument match", value=match, expected_type=type_hints["match"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "period": period,
            "threshold": threshold,
            "zone_id": zone_id,
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
        if bypass_url_patterns is not None:
            self._values["bypass_url_patterns"] = bypass_url_patterns
        if correlate is not None:
            self._values["correlate"] = correlate
        if description is not None:
            self._values["description"] = description
        if disabled is not None:
            self._values["disabled"] = disabled
        if id is not None:
            self._values["id"] = id
        if match is not None:
            self._values["match"] = match

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
    def action(self) -> RateLimitAction:
        '''action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#action RateLimit#action}
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(RateLimitAction, result)

    @builtins.property
    def period(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#period RateLimit#period}.'''
        result = self._values.get("period")
        assert result is not None, "Required property 'period' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def threshold(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#threshold RateLimit#threshold}.'''
        result = self._values.get("threshold")
        assert result is not None, "Required property 'threshold' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def zone_id(self) -> builtins.str:
        '''The zone identifier to target for the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#zone_id RateLimit#zone_id}
        '''
        result = self._values.get("zone_id")
        assert result is not None, "Required property 'zone_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bypass_url_patterns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#bypass_url_patterns RateLimit#bypass_url_patterns}.'''
        result = self._values.get("bypass_url_patterns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def correlate(self) -> typing.Optional["RateLimitCorrelate"]:
        '''correlate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#correlate RateLimit#correlate}
        '''
        result = self._values.get("correlate")
        return typing.cast(typing.Optional["RateLimitCorrelate"], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#description RateLimit#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#disabled RateLimit#disabled}
        '''
        result = self._values.get("disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#id RateLimit#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def match(self) -> typing.Optional["RateLimitMatch"]:
        '''match block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#match RateLimit#match}
        '''
        result = self._values.get("match")
        return typing.cast(typing.Optional["RateLimitMatch"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RateLimitConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.rateLimit.RateLimitCorrelate",
    jsii_struct_bases=[],
    name_mapping={"by": "by"},
)
class RateLimitCorrelate:
    def __init__(self, *, by: typing.Optional[builtins.str] = None) -> None:
        '''
        :param by: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#by RateLimit#by}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RateLimitCorrelate.__init__)
            check_type(argname="argument by", value=by, expected_type=type_hints["by"])
        self._values: typing.Dict[str, typing.Any] = {}
        if by is not None:
            self._values["by"] = by

    @builtins.property
    def by(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#by RateLimit#by}.'''
        result = self._values.get("by")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RateLimitCorrelate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RateLimitCorrelateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.rateLimit.RateLimitCorrelateOutputReference",
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
            type_hints = typing.get_type_hints(RateLimitCorrelateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBy")
    def reset_by(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBy", []))

    @builtins.property
    @jsii.member(jsii_name="byInput")
    def by_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "byInput"))

    @builtins.property
    @jsii.member(jsii_name="by")
    def by(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "by"))

    @by.setter
    def by(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RateLimitCorrelateOutputReference, "by").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "by", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RateLimitCorrelate]:
        return typing.cast(typing.Optional[RateLimitCorrelate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[RateLimitCorrelate]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RateLimitCorrelateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.rateLimit.RateLimitMatch",
    jsii_struct_bases=[],
    name_mapping={"request": "request", "response": "response"},
)
class RateLimitMatch:
    def __init__(
        self,
        *,
        request: typing.Optional[typing.Union["RateLimitMatchRequest", typing.Dict[str, typing.Any]]] = None,
        response: typing.Optional[typing.Union["RateLimitMatchResponse", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param request: request block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#request RateLimit#request}
        :param response: response block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#response RateLimit#response}
        '''
        if isinstance(request, dict):
            request = RateLimitMatchRequest(**request)
        if isinstance(response, dict):
            response = RateLimitMatchResponse(**response)
        if __debug__:
            type_hints = typing.get_type_hints(RateLimitMatch.__init__)
            check_type(argname="argument request", value=request, expected_type=type_hints["request"])
            check_type(argname="argument response", value=response, expected_type=type_hints["response"])
        self._values: typing.Dict[str, typing.Any] = {}
        if request is not None:
            self._values["request"] = request
        if response is not None:
            self._values["response"] = response

    @builtins.property
    def request(self) -> typing.Optional["RateLimitMatchRequest"]:
        '''request block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#request RateLimit#request}
        '''
        result = self._values.get("request")
        return typing.cast(typing.Optional["RateLimitMatchRequest"], result)

    @builtins.property
    def response(self) -> typing.Optional["RateLimitMatchResponse"]:
        '''response block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#response RateLimit#response}
        '''
        result = self._values.get("response")
        return typing.cast(typing.Optional["RateLimitMatchResponse"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RateLimitMatch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RateLimitMatchOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.rateLimit.RateLimitMatchOutputReference",
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
            type_hints = typing.get_type_hints(RateLimitMatchOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRequest")
    def put_request(
        self,
        *,
        methods: typing.Optional[typing.Sequence[builtins.str]] = None,
        schemes: typing.Optional[typing.Sequence[builtins.str]] = None,
        url_pattern: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param methods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#methods RateLimit#methods}.
        :param schemes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#schemes RateLimit#schemes}.
        :param url_pattern: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#url_pattern RateLimit#url_pattern}.
        '''
        value = RateLimitMatchRequest(
            methods=methods, schemes=schemes, url_pattern=url_pattern
        )

        return typing.cast(None, jsii.invoke(self, "putRequest", [value]))

    @jsii.member(jsii_name="putResponse")
    def put_response(
        self,
        *,
        headers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
        origin_traffic: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        statuses: typing.Optional[typing.Sequence[jsii.Number]] = None,
    ) -> None:
        '''
        :param headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#headers RateLimit#headers}.
        :param origin_traffic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#origin_traffic RateLimit#origin_traffic}.
        :param statuses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#statuses RateLimit#statuses}.
        '''
        value = RateLimitMatchResponse(
            headers=headers, origin_traffic=origin_traffic, statuses=statuses
        )

        return typing.cast(None, jsii.invoke(self, "putResponse", [value]))

    @jsii.member(jsii_name="resetRequest")
    def reset_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequest", []))

    @jsii.member(jsii_name="resetResponse")
    def reset_response(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponse", []))

    @builtins.property
    @jsii.member(jsii_name="request")
    def request(self) -> "RateLimitMatchRequestOutputReference":
        return typing.cast("RateLimitMatchRequestOutputReference", jsii.get(self, "request"))

    @builtins.property
    @jsii.member(jsii_name="response")
    def response(self) -> "RateLimitMatchResponseOutputReference":
        return typing.cast("RateLimitMatchResponseOutputReference", jsii.get(self, "response"))

    @builtins.property
    @jsii.member(jsii_name="requestInput")
    def request_input(self) -> typing.Optional["RateLimitMatchRequest"]:
        return typing.cast(typing.Optional["RateLimitMatchRequest"], jsii.get(self, "requestInput"))

    @builtins.property
    @jsii.member(jsii_name="responseInput")
    def response_input(self) -> typing.Optional["RateLimitMatchResponse"]:
        return typing.cast(typing.Optional["RateLimitMatchResponse"], jsii.get(self, "responseInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RateLimitMatch]:
        return typing.cast(typing.Optional[RateLimitMatch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[RateLimitMatch]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RateLimitMatchOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.rateLimit.RateLimitMatchRequest",
    jsii_struct_bases=[],
    name_mapping={
        "methods": "methods",
        "schemes": "schemes",
        "url_pattern": "urlPattern",
    },
)
class RateLimitMatchRequest:
    def __init__(
        self,
        *,
        methods: typing.Optional[typing.Sequence[builtins.str]] = None,
        schemes: typing.Optional[typing.Sequence[builtins.str]] = None,
        url_pattern: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param methods: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#methods RateLimit#methods}.
        :param schemes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#schemes RateLimit#schemes}.
        :param url_pattern: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#url_pattern RateLimit#url_pattern}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RateLimitMatchRequest.__init__)
            check_type(argname="argument methods", value=methods, expected_type=type_hints["methods"])
            check_type(argname="argument schemes", value=schemes, expected_type=type_hints["schemes"])
            check_type(argname="argument url_pattern", value=url_pattern, expected_type=type_hints["url_pattern"])
        self._values: typing.Dict[str, typing.Any] = {}
        if methods is not None:
            self._values["methods"] = methods
        if schemes is not None:
            self._values["schemes"] = schemes
        if url_pattern is not None:
            self._values["url_pattern"] = url_pattern

    @builtins.property
    def methods(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#methods RateLimit#methods}.'''
        result = self._values.get("methods")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def schemes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#schemes RateLimit#schemes}.'''
        result = self._values.get("schemes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def url_pattern(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#url_pattern RateLimit#url_pattern}.'''
        result = self._values.get("url_pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RateLimitMatchRequest(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RateLimitMatchRequestOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.rateLimit.RateLimitMatchRequestOutputReference",
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
            type_hints = typing.get_type_hints(RateLimitMatchRequestOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMethods")
    def reset_methods(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMethods", []))

    @jsii.member(jsii_name="resetSchemes")
    def reset_schemes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchemes", []))

    @jsii.member(jsii_name="resetUrlPattern")
    def reset_url_pattern(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUrlPattern", []))

    @builtins.property
    @jsii.member(jsii_name="methodsInput")
    def methods_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "methodsInput"))

    @builtins.property
    @jsii.member(jsii_name="schemesInput")
    def schemes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "schemesInput"))

    @builtins.property
    @jsii.member(jsii_name="urlPatternInput")
    def url_pattern_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "urlPatternInput"))

    @builtins.property
    @jsii.member(jsii_name="methods")
    def methods(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "methods"))

    @methods.setter
    def methods(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RateLimitMatchRequestOutputReference, "methods").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "methods", value)

    @builtins.property
    @jsii.member(jsii_name="schemes")
    def schemes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "schemes"))

    @schemes.setter
    def schemes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RateLimitMatchRequestOutputReference, "schemes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemes", value)

    @builtins.property
    @jsii.member(jsii_name="urlPattern")
    def url_pattern(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "urlPattern"))

    @url_pattern.setter
    def url_pattern(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RateLimitMatchRequestOutputReference, "url_pattern").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "urlPattern", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RateLimitMatchRequest]:
        return typing.cast(typing.Optional[RateLimitMatchRequest], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[RateLimitMatchRequest]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RateLimitMatchRequestOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.rateLimit.RateLimitMatchResponse",
    jsii_struct_bases=[],
    name_mapping={
        "headers": "headers",
        "origin_traffic": "originTraffic",
        "statuses": "statuses",
    },
)
class RateLimitMatchResponse:
    def __init__(
        self,
        *,
        headers: typing.Optional[typing.Union[cdktf.IResolvable, typing.Mapping[builtins.str, builtins.str]]] = None,
        origin_traffic: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        statuses: typing.Optional[typing.Sequence[jsii.Number]] = None,
    ) -> None:
        '''
        :param headers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#headers RateLimit#headers}.
        :param origin_traffic: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#origin_traffic RateLimit#origin_traffic}.
        :param statuses: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#statuses RateLimit#statuses}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RateLimitMatchResponse.__init__)
            check_type(argname="argument headers", value=headers, expected_type=type_hints["headers"])
            check_type(argname="argument origin_traffic", value=origin_traffic, expected_type=type_hints["origin_traffic"])
            check_type(argname="argument statuses", value=statuses, expected_type=type_hints["statuses"])
        self._values: typing.Dict[str, typing.Any] = {}
        if headers is not None:
            self._values["headers"] = headers
        if origin_traffic is not None:
            self._values["origin_traffic"] = origin_traffic
        if statuses is not None:
            self._values["statuses"] = statuses

    @builtins.property
    def headers(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#headers RateLimit#headers}.'''
        result = self._values.get("headers")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def origin_traffic(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#origin_traffic RateLimit#origin_traffic}.'''
        result = self._values.get("origin_traffic")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def statuses(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/rate_limit#statuses RateLimit#statuses}.'''
        result = self._values.get("statuses")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RateLimitMatchResponse(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RateLimitMatchResponseOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.rateLimit.RateLimitMatchResponseOutputReference",
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
            type_hints = typing.get_type_hints(RateLimitMatchResponseOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetHeaders")
    def reset_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHeaders", []))

    @jsii.member(jsii_name="resetOriginTraffic")
    def reset_origin_traffic(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOriginTraffic", []))

    @jsii.member(jsii_name="resetStatuses")
    def reset_statuses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatuses", []))

    @builtins.property
    @jsii.member(jsii_name="headersInput")
    def headers_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.Mapping[builtins.str, builtins.str]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "headersInput"))

    @builtins.property
    @jsii.member(jsii_name="originTrafficInput")
    def origin_traffic_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "originTrafficInput"))

    @builtins.property
    @jsii.member(jsii_name="statusesInput")
    def statuses_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "statusesInput"))

    @builtins.property
    @jsii.member(jsii_name="headers")
    def headers(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Union[cdktf.IResolvable, typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "headers"))

    @headers.setter
    def headers(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RateLimitMatchResponseOutputReference, "headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "headers", value)

    @builtins.property
    @jsii.member(jsii_name="originTraffic")
    def origin_traffic(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "originTraffic"))

    @origin_traffic.setter
    def origin_traffic(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RateLimitMatchResponseOutputReference, "origin_traffic").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "originTraffic", value)

    @builtins.property
    @jsii.member(jsii_name="statuses")
    def statuses(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "statuses"))

    @statuses.setter
    def statuses(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RateLimitMatchResponseOutputReference, "statuses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statuses", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RateLimitMatchResponse]:
        return typing.cast(typing.Optional[RateLimitMatchResponse], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[RateLimitMatchResponse]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RateLimitMatchResponseOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "RateLimit",
    "RateLimitAction",
    "RateLimitActionOutputReference",
    "RateLimitActionResponse",
    "RateLimitActionResponseOutputReference",
    "RateLimitConfig",
    "RateLimitCorrelate",
    "RateLimitCorrelateOutputReference",
    "RateLimitMatch",
    "RateLimitMatchOutputReference",
    "RateLimitMatchRequest",
    "RateLimitMatchRequestOutputReference",
    "RateLimitMatchResponse",
    "RateLimitMatchResponseOutputReference",
]

publication.publish()
