'''
# `newrelic_synthetics_monitor`

Refer to the Terraform Registory for docs: [`newrelic_synthetics_monitor`](https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor).
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


class SyntheticsMonitor(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.syntheticsMonitor.SyntheticsMonitor",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor newrelic_synthetics_monitor}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        frequency: jsii.Number,
        locations: typing.Sequence[builtins.str],
        name: builtins.str,
        status: builtins.str,
        type: builtins.str,
        bypass_head_request: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        sla_threshold: typing.Optional[jsii.Number] = None,
        treat_redirect_as_failure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        uri: typing.Optional[builtins.str] = None,
        validation_string: typing.Optional[builtins.str] = None,
        verify_ssl: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor newrelic_synthetics_monitor} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param frequency: The interval (in minutes) at which this monitor should run. Valid values are 1, 5, 10, 15, 30, 60, 360, 720, or 1440. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#frequency SyntheticsMonitor#frequency}
        :param locations: The locations in which this monitor should be run. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#locations SyntheticsMonitor#locations}
        :param name: The title of this monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#name SyntheticsMonitor#name}
        :param status: The monitor status (i.e. ENABLED, MUTED, DISABLED). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#status SyntheticsMonitor#status}
        :param type: The monitor type. Valid values are SIMPLE, BROWSER, SCRIPT_BROWSER, and SCRIPT_API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#type SyntheticsMonitor#type}
        :param bypass_head_request: Bypass HEAD request. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#bypass_head_request SyntheticsMonitor#bypass_head_request}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#id SyntheticsMonitor#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param sla_threshold: The base threshold (in seconds) to calculate the apdex score for use in the SLA report. (Default 7 seconds). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#sla_threshold SyntheticsMonitor#sla_threshold}
        :param treat_redirect_as_failure: Fail the monitor check if redirected. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#treat_redirect_as_failure SyntheticsMonitor#treat_redirect_as_failure}
        :param uri: The URI for the monitor to hit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#uri SyntheticsMonitor#uri}
        :param validation_string: The string to validate against in the response. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#validation_string SyntheticsMonitor#validation_string}
        :param verify_ssl: Verify SSL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#verify_ssl SyntheticsMonitor#verify_ssl}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsMonitor.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = SyntheticsMonitorConfig(
            frequency=frequency,
            locations=locations,
            name=name,
            status=status,
            type=type,
            bypass_head_request=bypass_head_request,
            id=id,
            sla_threshold=sla_threshold,
            treat_redirect_as_failure=treat_redirect_as_failure,
            uri=uri,
            validation_string=validation_string,
            verify_ssl=verify_ssl,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetBypassHeadRequest")
    def reset_bypass_head_request(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBypassHeadRequest", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSlaThreshold")
    def reset_sla_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSlaThreshold", []))

    @jsii.member(jsii_name="resetTreatRedirectAsFailure")
    def reset_treat_redirect_as_failure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTreatRedirectAsFailure", []))

    @jsii.member(jsii_name="resetUri")
    def reset_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUri", []))

    @jsii.member(jsii_name="resetValidationString")
    def reset_validation_string(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValidationString", []))

    @jsii.member(jsii_name="resetVerifySsl")
    def reset_verify_ssl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVerifySsl", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="bypassHeadRequestInput")
    def bypass_head_request_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "bypassHeadRequestInput"))

    @builtins.property
    @jsii.member(jsii_name="frequencyInput")
    def frequency_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "frequencyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationsInput")
    def locations_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "locationsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="slaThresholdInput")
    def sla_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "slaThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="statusInput")
    def status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statusInput"))

    @builtins.property
    @jsii.member(jsii_name="treatRedirectAsFailureInput")
    def treat_redirect_as_failure_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "treatRedirectAsFailureInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="uriInput")
    def uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "uriInput"))

    @builtins.property
    @jsii.member(jsii_name="validationStringInput")
    def validation_string_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "validationStringInput"))

    @builtins.property
    @jsii.member(jsii_name="verifySslInput")
    def verify_ssl_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "verifySslInput"))

    @builtins.property
    @jsii.member(jsii_name="bypassHeadRequest")
    def bypass_head_request(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "bypassHeadRequest"))

    @bypass_head_request.setter
    def bypass_head_request(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsMonitor, "bypass_head_request").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bypassHeadRequest", value)

    @builtins.property
    @jsii.member(jsii_name="frequency")
    def frequency(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "frequency"))

    @frequency.setter
    def frequency(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsMonitor, "frequency").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frequency", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsMonitor, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="locations")
    def locations(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "locations"))

    @locations.setter
    def locations(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsMonitor, "locations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locations", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsMonitor, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="slaThreshold")
    def sla_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "slaThreshold"))

    @sla_threshold.setter
    def sla_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsMonitor, "sla_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "slaThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsMonitor, "status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="treatRedirectAsFailure")
    def treat_redirect_as_failure(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "treatRedirectAsFailure"))

    @treat_redirect_as_failure.setter
    def treat_redirect_as_failure(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsMonitor, "treat_redirect_as_failure").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "treatRedirectAsFailure", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsMonitor, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="uri")
    def uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uri"))

    @uri.setter
    def uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsMonitor, "uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uri", value)

    @builtins.property
    @jsii.member(jsii_name="validationString")
    def validation_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "validationString"))

    @validation_string.setter
    def validation_string(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsMonitor, "validation_string").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validationString", value)

    @builtins.property
    @jsii.member(jsii_name="verifySsl")
    def verify_ssl(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "verifySsl"))

    @verify_ssl.setter
    def verify_ssl(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(SyntheticsMonitor, "verify_ssl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "verifySsl", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.syntheticsMonitor.SyntheticsMonitorConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "frequency": "frequency",
        "locations": "locations",
        "name": "name",
        "status": "status",
        "type": "type",
        "bypass_head_request": "bypassHeadRequest",
        "id": "id",
        "sla_threshold": "slaThreshold",
        "treat_redirect_as_failure": "treatRedirectAsFailure",
        "uri": "uri",
        "validation_string": "validationString",
        "verify_ssl": "verifySsl",
    },
)
class SyntheticsMonitorConfig(cdktf.TerraformMetaArguments):
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
        frequency: jsii.Number,
        locations: typing.Sequence[builtins.str],
        name: builtins.str,
        status: builtins.str,
        type: builtins.str,
        bypass_head_request: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        sla_threshold: typing.Optional[jsii.Number] = None,
        treat_redirect_as_failure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        uri: typing.Optional[builtins.str] = None,
        validation_string: typing.Optional[builtins.str] = None,
        verify_ssl: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param frequency: The interval (in minutes) at which this monitor should run. Valid values are 1, 5, 10, 15, 30, 60, 360, 720, or 1440. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#frequency SyntheticsMonitor#frequency}
        :param locations: The locations in which this monitor should be run. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#locations SyntheticsMonitor#locations}
        :param name: The title of this monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#name SyntheticsMonitor#name}
        :param status: The monitor status (i.e. ENABLED, MUTED, DISABLED). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#status SyntheticsMonitor#status}
        :param type: The monitor type. Valid values are SIMPLE, BROWSER, SCRIPT_BROWSER, and SCRIPT_API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#type SyntheticsMonitor#type}
        :param bypass_head_request: Bypass HEAD request. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#bypass_head_request SyntheticsMonitor#bypass_head_request}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#id SyntheticsMonitor#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param sla_threshold: The base threshold (in seconds) to calculate the apdex score for use in the SLA report. (Default 7 seconds). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#sla_threshold SyntheticsMonitor#sla_threshold}
        :param treat_redirect_as_failure: Fail the monitor check if redirected. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#treat_redirect_as_failure SyntheticsMonitor#treat_redirect_as_failure}
        :param uri: The URI for the monitor to hit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#uri SyntheticsMonitor#uri}
        :param validation_string: The string to validate against in the response. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#validation_string SyntheticsMonitor#validation_string}
        :param verify_ssl: Verify SSL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#verify_ssl SyntheticsMonitor#verify_ssl}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(SyntheticsMonitorConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument frequency", value=frequency, expected_type=type_hints["frequency"])
            check_type(argname="argument locations", value=locations, expected_type=type_hints["locations"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument bypass_head_request", value=bypass_head_request, expected_type=type_hints["bypass_head_request"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument sla_threshold", value=sla_threshold, expected_type=type_hints["sla_threshold"])
            check_type(argname="argument treat_redirect_as_failure", value=treat_redirect_as_failure, expected_type=type_hints["treat_redirect_as_failure"])
            check_type(argname="argument uri", value=uri, expected_type=type_hints["uri"])
            check_type(argname="argument validation_string", value=validation_string, expected_type=type_hints["validation_string"])
            check_type(argname="argument verify_ssl", value=verify_ssl, expected_type=type_hints["verify_ssl"])
        self._values: typing.Dict[str, typing.Any] = {
            "frequency": frequency,
            "locations": locations,
            "name": name,
            "status": status,
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
        if bypass_head_request is not None:
            self._values["bypass_head_request"] = bypass_head_request
        if id is not None:
            self._values["id"] = id
        if sla_threshold is not None:
            self._values["sla_threshold"] = sla_threshold
        if treat_redirect_as_failure is not None:
            self._values["treat_redirect_as_failure"] = treat_redirect_as_failure
        if uri is not None:
            self._values["uri"] = uri
        if validation_string is not None:
            self._values["validation_string"] = validation_string
        if verify_ssl is not None:
            self._values["verify_ssl"] = verify_ssl

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
    def frequency(self) -> jsii.Number:
        '''The interval (in minutes) at which this monitor should run.

        Valid values are 1, 5, 10, 15, 30, 60, 360, 720, or 1440.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#frequency SyntheticsMonitor#frequency}
        '''
        result = self._values.get("frequency")
        assert result is not None, "Required property 'frequency' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def locations(self) -> typing.List[builtins.str]:
        '''The locations in which this monitor should be run.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#locations SyntheticsMonitor#locations}
        '''
        result = self._values.get("locations")
        assert result is not None, "Required property 'locations' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The title of this monitor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#name SyntheticsMonitor#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def status(self) -> builtins.str:
        '''The monitor status (i.e. ENABLED, MUTED, DISABLED).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#status SyntheticsMonitor#status}
        '''
        result = self._values.get("status")
        assert result is not None, "Required property 'status' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The monitor type. Valid values are SIMPLE, BROWSER, SCRIPT_BROWSER, and SCRIPT_API.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#type SyntheticsMonitor#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def bypass_head_request(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Bypass HEAD request.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#bypass_head_request SyntheticsMonitor#bypass_head_request}
        '''
        result = self._values.get("bypass_head_request")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#id SyntheticsMonitor#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sla_threshold(self) -> typing.Optional[jsii.Number]:
        '''The base threshold (in seconds) to calculate the apdex score for use in the SLA report. (Default 7 seconds).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#sla_threshold SyntheticsMonitor#sla_threshold}
        '''
        result = self._values.get("sla_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def treat_redirect_as_failure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Fail the monitor check if redirected.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#treat_redirect_as_failure SyntheticsMonitor#treat_redirect_as_failure}
        '''
        result = self._values.get("treat_redirect_as_failure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def uri(self) -> typing.Optional[builtins.str]:
        '''The URI for the monitor to hit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#uri SyntheticsMonitor#uri}
        '''
        result = self._values.get("uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def validation_string(self) -> typing.Optional[builtins.str]:
        '''The string to validate against in the response.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#validation_string SyntheticsMonitor#validation_string}
        '''
        result = self._values.get("validation_string")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def verify_ssl(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Verify SSL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/synthetics_monitor#verify_ssl SyntheticsMonitor#verify_ssl}
        '''
        result = self._values.get("verify_ssl")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SyntheticsMonitorConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "SyntheticsMonitor",
    "SyntheticsMonitorConfig",
]

publication.publish()
