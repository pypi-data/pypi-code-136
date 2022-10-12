'''
# `newrelic_cloud_aws_integrations`

Refer to the Terraform Registory for docs: [`newrelic_cloud_aws_integrations`](https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations).
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


class CloudAwsIntegrations(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrations",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations newrelic_cloud_aws_integrations}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        linked_account_id: jsii.Number,
        account_id: typing.Optional[jsii.Number] = None,
        billing: typing.Optional[typing.Union["CloudAwsIntegrationsBilling", typing.Dict[str, typing.Any]]] = None,
        cloudtrail: typing.Optional[typing.Union["CloudAwsIntegrationsCloudtrail", typing.Dict[str, typing.Any]]] = None,
        health: typing.Optional[typing.Union["CloudAwsIntegrationsHealth", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        trusted_advisor: typing.Optional[typing.Union["CloudAwsIntegrationsTrustedAdvisor", typing.Dict[str, typing.Any]]] = None,
        vpc: typing.Optional[typing.Union["CloudAwsIntegrationsVpc", typing.Dict[str, typing.Any]]] = None,
        x_ray: typing.Optional[typing.Union["CloudAwsIntegrationsXRay", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations newrelic_cloud_aws_integrations} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param linked_account_id: The ID of the linked AWS account in New Relic. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#linked_account_id CloudAwsIntegrations#linked_account_id}
        :param account_id: The ID of the account in New Relic. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#account_id CloudAwsIntegrations#account_id}
        :param billing: billing block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#billing CloudAwsIntegrations#billing}
        :param cloudtrail: cloudtrail block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#cloudtrail CloudAwsIntegrations#cloudtrail}
        :param health: health block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#health CloudAwsIntegrations#health}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#id CloudAwsIntegrations#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param trusted_advisor: trusted_advisor block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#trusted_advisor CloudAwsIntegrations#trusted_advisor}
        :param vpc: vpc block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#vpc CloudAwsIntegrations#vpc}
        :param x_ray: x_ray block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#x_ray CloudAwsIntegrations#x_ray}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAwsIntegrations.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CloudAwsIntegrationsConfig(
            linked_account_id=linked_account_id,
            account_id=account_id,
            billing=billing,
            cloudtrail=cloudtrail,
            health=health,
            id=id,
            trusted_advisor=trusted_advisor,
            vpc=vpc,
            x_ray=x_ray,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putBilling")
    def put_billing(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        value = CloudAwsIntegrationsBilling(
            metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putBilling", [value]))

    @jsii.member(jsii_name="putCloudtrail")
    def put_cloudtrail(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        value = CloudAwsIntegrationsCloudtrail(
            aws_regions=aws_regions, metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putCloudtrail", [value]))

    @jsii.member(jsii_name="putHealth")
    def put_health(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        value = CloudAwsIntegrationsHealth(
            metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putHealth", [value]))

    @jsii.member(jsii_name="putTrustedAdvisor")
    def put_trusted_advisor(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        value = CloudAwsIntegrationsTrustedAdvisor(
            metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putTrustedAdvisor", [value]))

    @jsii.member(jsii_name="putVpc")
    def put_vpc(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        fetch_nat_gateway: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        fetch_vpn: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param fetch_nat_gateway: Specify if NAT gateway should be monitored. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#fetch_nat_gateway CloudAwsIntegrations#fetch_nat_gateway}
        :param fetch_vpn: Specify if VPN should be monitored. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#fetch_vpn CloudAwsIntegrations#fetch_vpn}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#tag_key CloudAwsIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#tag_value CloudAwsIntegrations#tag_value}
        '''
        value = CloudAwsIntegrationsVpc(
            aws_regions=aws_regions,
            fetch_nat_gateway=fetch_nat_gateway,
            fetch_vpn=fetch_vpn,
            metrics_polling_interval=metrics_polling_interval,
            tag_key=tag_key,
            tag_value=tag_value,
        )

        return typing.cast(None, jsii.invoke(self, "putVpc", [value]))

    @jsii.member(jsii_name="putXRay")
    def put_x_ray(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        value = CloudAwsIntegrationsXRay(
            aws_regions=aws_regions, metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putXRay", [value]))

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetBilling")
    def reset_billing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBilling", []))

    @jsii.member(jsii_name="resetCloudtrail")
    def reset_cloudtrail(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudtrail", []))

    @jsii.member(jsii_name="resetHealth")
    def reset_health(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealth", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetTrustedAdvisor")
    def reset_trusted_advisor(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTrustedAdvisor", []))

    @jsii.member(jsii_name="resetVpc")
    def reset_vpc(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVpc", []))

    @jsii.member(jsii_name="resetXRay")
    def reset_x_ray(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetXRay", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="billing")
    def billing(self) -> "CloudAwsIntegrationsBillingOutputReference":
        return typing.cast("CloudAwsIntegrationsBillingOutputReference", jsii.get(self, "billing"))

    @builtins.property
    @jsii.member(jsii_name="cloudtrail")
    def cloudtrail(self) -> "CloudAwsIntegrationsCloudtrailOutputReference":
        return typing.cast("CloudAwsIntegrationsCloudtrailOutputReference", jsii.get(self, "cloudtrail"))

    @builtins.property
    @jsii.member(jsii_name="health")
    def health(self) -> "CloudAwsIntegrationsHealthOutputReference":
        return typing.cast("CloudAwsIntegrationsHealthOutputReference", jsii.get(self, "health"))

    @builtins.property
    @jsii.member(jsii_name="trustedAdvisor")
    def trusted_advisor(self) -> "CloudAwsIntegrationsTrustedAdvisorOutputReference":
        return typing.cast("CloudAwsIntegrationsTrustedAdvisorOutputReference", jsii.get(self, "trustedAdvisor"))

    @builtins.property
    @jsii.member(jsii_name="vpc")
    def vpc(self) -> "CloudAwsIntegrationsVpcOutputReference":
        return typing.cast("CloudAwsIntegrationsVpcOutputReference", jsii.get(self, "vpc"))

    @builtins.property
    @jsii.member(jsii_name="xRay")
    def x_ray(self) -> "CloudAwsIntegrationsXRayOutputReference":
        return typing.cast("CloudAwsIntegrationsXRayOutputReference", jsii.get(self, "xRay"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="billingInput")
    def billing_input(self) -> typing.Optional["CloudAwsIntegrationsBilling"]:
        return typing.cast(typing.Optional["CloudAwsIntegrationsBilling"], jsii.get(self, "billingInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudtrailInput")
    def cloudtrail_input(self) -> typing.Optional["CloudAwsIntegrationsCloudtrail"]:
        return typing.cast(typing.Optional["CloudAwsIntegrationsCloudtrail"], jsii.get(self, "cloudtrailInput"))

    @builtins.property
    @jsii.member(jsii_name="healthInput")
    def health_input(self) -> typing.Optional["CloudAwsIntegrationsHealth"]:
        return typing.cast(typing.Optional["CloudAwsIntegrationsHealth"], jsii.get(self, "healthInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="linkedAccountIdInput")
    def linked_account_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "linkedAccountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="trustedAdvisorInput")
    def trusted_advisor_input(
        self,
    ) -> typing.Optional["CloudAwsIntegrationsTrustedAdvisor"]:
        return typing.cast(typing.Optional["CloudAwsIntegrationsTrustedAdvisor"], jsii.get(self, "trustedAdvisorInput"))

    @builtins.property
    @jsii.member(jsii_name="vpcInput")
    def vpc_input(self) -> typing.Optional["CloudAwsIntegrationsVpc"]:
        return typing.cast(typing.Optional["CloudAwsIntegrationsVpc"], jsii.get(self, "vpcInput"))

    @builtins.property
    @jsii.member(jsii_name="xRayInput")
    def x_ray_input(self) -> typing.Optional["CloudAwsIntegrationsXRay"]:
        return typing.cast(typing.Optional["CloudAwsIntegrationsXRay"], jsii.get(self, "xRayInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsIntegrations, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsIntegrations, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="linkedAccountId")
    def linked_account_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "linkedAccountId"))

    @linked_account_id.setter
    def linked_account_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsIntegrations, "linked_account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "linkedAccountId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsBilling",
    jsii_struct_bases=[],
    name_mapping={"metrics_polling_interval": "metricsPollingInterval"},
)
class CloudAwsIntegrationsBilling:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAwsIntegrationsBilling.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsIntegrationsBilling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsIntegrationsBillingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsBillingOutputReference",
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
            type_hints = typing.get_type_hints(CloudAwsIntegrationsBillingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsIntegrationsBillingOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsIntegrationsBilling]:
        return typing.cast(typing.Optional[CloudAwsIntegrationsBilling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsIntegrationsBilling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsIntegrationsBillingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsCloudtrail",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "metrics_polling_interval": "metricsPollingInterval",
    },
)
class CloudAwsIntegrationsCloudtrail:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAwsIntegrationsCloudtrail.__init__)
            check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if aws_regions is not None:
            self._values["aws_regions"] = aws_regions
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each AWS region that includes the resources that you want to monitor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsIntegrationsCloudtrail(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsIntegrationsCloudtrailOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsCloudtrailOutputReference",
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
            type_hints = typing.get_type_hints(CloudAwsIntegrationsCloudtrailOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAwsRegions")
    def reset_aws_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegions", []))

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="awsRegionsInput")
    def aws_regions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "awsRegionsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="awsRegions")
    def aws_regions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "awsRegions"))

    @aws_regions.setter
    def aws_regions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsIntegrationsCloudtrailOutputReference, "aws_regions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsIntegrationsCloudtrailOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsIntegrationsCloudtrail]:
        return typing.cast(typing.Optional[CloudAwsIntegrationsCloudtrail], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsIntegrationsCloudtrail],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsIntegrationsCloudtrailOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "linked_account_id": "linkedAccountId",
        "account_id": "accountId",
        "billing": "billing",
        "cloudtrail": "cloudtrail",
        "health": "health",
        "id": "id",
        "trusted_advisor": "trustedAdvisor",
        "vpc": "vpc",
        "x_ray": "xRay",
    },
)
class CloudAwsIntegrationsConfig(cdktf.TerraformMetaArguments):
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
        linked_account_id: jsii.Number,
        account_id: typing.Optional[jsii.Number] = None,
        billing: typing.Optional[typing.Union[CloudAwsIntegrationsBilling, typing.Dict[str, typing.Any]]] = None,
        cloudtrail: typing.Optional[typing.Union[CloudAwsIntegrationsCloudtrail, typing.Dict[str, typing.Any]]] = None,
        health: typing.Optional[typing.Union["CloudAwsIntegrationsHealth", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        trusted_advisor: typing.Optional[typing.Union["CloudAwsIntegrationsTrustedAdvisor", typing.Dict[str, typing.Any]]] = None,
        vpc: typing.Optional[typing.Union["CloudAwsIntegrationsVpc", typing.Dict[str, typing.Any]]] = None,
        x_ray: typing.Optional[typing.Union["CloudAwsIntegrationsXRay", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param linked_account_id: The ID of the linked AWS account in New Relic. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#linked_account_id CloudAwsIntegrations#linked_account_id}
        :param account_id: The ID of the account in New Relic. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#account_id CloudAwsIntegrations#account_id}
        :param billing: billing block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#billing CloudAwsIntegrations#billing}
        :param cloudtrail: cloudtrail block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#cloudtrail CloudAwsIntegrations#cloudtrail}
        :param health: health block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#health CloudAwsIntegrations#health}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#id CloudAwsIntegrations#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param trusted_advisor: trusted_advisor block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#trusted_advisor CloudAwsIntegrations#trusted_advisor}
        :param vpc: vpc block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#vpc CloudAwsIntegrations#vpc}
        :param x_ray: x_ray block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#x_ray CloudAwsIntegrations#x_ray}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(billing, dict):
            billing = CloudAwsIntegrationsBilling(**billing)
        if isinstance(cloudtrail, dict):
            cloudtrail = CloudAwsIntegrationsCloudtrail(**cloudtrail)
        if isinstance(health, dict):
            health = CloudAwsIntegrationsHealth(**health)
        if isinstance(trusted_advisor, dict):
            trusted_advisor = CloudAwsIntegrationsTrustedAdvisor(**trusted_advisor)
        if isinstance(vpc, dict):
            vpc = CloudAwsIntegrationsVpc(**vpc)
        if isinstance(x_ray, dict):
            x_ray = CloudAwsIntegrationsXRay(**x_ray)
        if __debug__:
            type_hints = typing.get_type_hints(CloudAwsIntegrationsConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument linked_account_id", value=linked_account_id, expected_type=type_hints["linked_account_id"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument billing", value=billing, expected_type=type_hints["billing"])
            check_type(argname="argument cloudtrail", value=cloudtrail, expected_type=type_hints["cloudtrail"])
            check_type(argname="argument health", value=health, expected_type=type_hints["health"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument trusted_advisor", value=trusted_advisor, expected_type=type_hints["trusted_advisor"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument x_ray", value=x_ray, expected_type=type_hints["x_ray"])
        self._values: typing.Dict[str, typing.Any] = {
            "linked_account_id": linked_account_id,
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
        if account_id is not None:
            self._values["account_id"] = account_id
        if billing is not None:
            self._values["billing"] = billing
        if cloudtrail is not None:
            self._values["cloudtrail"] = cloudtrail
        if health is not None:
            self._values["health"] = health
        if id is not None:
            self._values["id"] = id
        if trusted_advisor is not None:
            self._values["trusted_advisor"] = trusted_advisor
        if vpc is not None:
            self._values["vpc"] = vpc
        if x_ray is not None:
            self._values["x_ray"] = x_ray

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
    def linked_account_id(self) -> jsii.Number:
        '''The ID of the linked AWS account in New Relic.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#linked_account_id CloudAwsIntegrations#linked_account_id}
        '''
        result = self._values.get("linked_account_id")
        assert result is not None, "Required property 'linked_account_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def account_id(self) -> typing.Optional[jsii.Number]:
        '''The ID of the account in New Relic.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#account_id CloudAwsIntegrations#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def billing(self) -> typing.Optional[CloudAwsIntegrationsBilling]:
        '''billing block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#billing CloudAwsIntegrations#billing}
        '''
        result = self._values.get("billing")
        return typing.cast(typing.Optional[CloudAwsIntegrationsBilling], result)

    @builtins.property
    def cloudtrail(self) -> typing.Optional[CloudAwsIntegrationsCloudtrail]:
        '''cloudtrail block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#cloudtrail CloudAwsIntegrations#cloudtrail}
        '''
        result = self._values.get("cloudtrail")
        return typing.cast(typing.Optional[CloudAwsIntegrationsCloudtrail], result)

    @builtins.property
    def health(self) -> typing.Optional["CloudAwsIntegrationsHealth"]:
        '''health block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#health CloudAwsIntegrations#health}
        '''
        result = self._values.get("health")
        return typing.cast(typing.Optional["CloudAwsIntegrationsHealth"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#id CloudAwsIntegrations#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def trusted_advisor(self) -> typing.Optional["CloudAwsIntegrationsTrustedAdvisor"]:
        '''trusted_advisor block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#trusted_advisor CloudAwsIntegrations#trusted_advisor}
        '''
        result = self._values.get("trusted_advisor")
        return typing.cast(typing.Optional["CloudAwsIntegrationsTrustedAdvisor"], result)

    @builtins.property
    def vpc(self) -> typing.Optional["CloudAwsIntegrationsVpc"]:
        '''vpc block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#vpc CloudAwsIntegrations#vpc}
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional["CloudAwsIntegrationsVpc"], result)

    @builtins.property
    def x_ray(self) -> typing.Optional["CloudAwsIntegrationsXRay"]:
        '''x_ray block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#x_ray CloudAwsIntegrations#x_ray}
        '''
        result = self._values.get("x_ray")
        return typing.cast(typing.Optional["CloudAwsIntegrationsXRay"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsIntegrationsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsHealth",
    jsii_struct_bases=[],
    name_mapping={"metrics_polling_interval": "metricsPollingInterval"},
)
class CloudAwsIntegrationsHealth:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAwsIntegrationsHealth.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsIntegrationsHealth(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsIntegrationsHealthOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsHealthOutputReference",
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
            type_hints = typing.get_type_hints(CloudAwsIntegrationsHealthOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsIntegrationsHealthOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsIntegrationsHealth]:
        return typing.cast(typing.Optional[CloudAwsIntegrationsHealth], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsIntegrationsHealth],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsIntegrationsHealthOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsTrustedAdvisor",
    jsii_struct_bases=[],
    name_mapping={"metrics_polling_interval": "metricsPollingInterval"},
)
class CloudAwsIntegrationsTrustedAdvisor:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAwsIntegrationsTrustedAdvisor.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsIntegrationsTrustedAdvisor(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsIntegrationsTrustedAdvisorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsTrustedAdvisorOutputReference",
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
            type_hints = typing.get_type_hints(CloudAwsIntegrationsTrustedAdvisorOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsIntegrationsTrustedAdvisorOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsIntegrationsTrustedAdvisor]:
        return typing.cast(typing.Optional[CloudAwsIntegrationsTrustedAdvisor], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsIntegrationsTrustedAdvisor],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsIntegrationsTrustedAdvisorOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsVpc",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "fetch_nat_gateway": "fetchNatGateway",
        "fetch_vpn": "fetchVpn",
        "metrics_polling_interval": "metricsPollingInterval",
        "tag_key": "tagKey",
        "tag_value": "tagValue",
    },
)
class CloudAwsIntegrationsVpc:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        fetch_nat_gateway: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        fetch_vpn: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param fetch_nat_gateway: Specify if NAT gateway should be monitored. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#fetch_nat_gateway CloudAwsIntegrations#fetch_nat_gateway}
        :param fetch_vpn: Specify if VPN should be monitored. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#fetch_vpn CloudAwsIntegrations#fetch_vpn}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#tag_key CloudAwsIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#tag_value CloudAwsIntegrations#tag_value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAwsIntegrationsVpc.__init__)
            check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            check_type(argname="argument fetch_nat_gateway", value=fetch_nat_gateway, expected_type=type_hints["fetch_nat_gateway"])
            check_type(argname="argument fetch_vpn", value=fetch_vpn, expected_type=type_hints["fetch_vpn"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
            check_type(argname="argument tag_value", value=tag_value, expected_type=type_hints["tag_value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if aws_regions is not None:
            self._values["aws_regions"] = aws_regions
        if fetch_nat_gateway is not None:
            self._values["fetch_nat_gateway"] = fetch_nat_gateway
        if fetch_vpn is not None:
            self._values["fetch_vpn"] = fetch_vpn
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if tag_key is not None:
            self._values["tag_key"] = tag_key
        if tag_value is not None:
            self._values["tag_value"] = tag_value

    @builtins.property
    def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each AWS region that includes the resources that you want to monitor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def fetch_nat_gateway(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specify if NAT gateway should be monitored.

        May affect total data collection time and contribute to the Cloud provider API rate limit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#fetch_nat_gateway CloudAwsIntegrations#fetch_nat_gateway}
        '''
        result = self._values.get("fetch_nat_gateway")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def fetch_vpn(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specify if VPN should be monitored.

        May affect total data collection time and contribute to the Cloud provider API rate limit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#fetch_vpn CloudAwsIntegrations#fetch_vpn}
        '''
        result = self._values.get("fetch_vpn")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tag_key(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#tag_key CloudAwsIntegrations#tag_key}
        '''
        result = self._values.get("tag_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_value(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#tag_value CloudAwsIntegrations#tag_value}
        '''
        result = self._values.get("tag_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsIntegrationsVpc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsIntegrationsVpcOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsVpcOutputReference",
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
            type_hints = typing.get_type_hints(CloudAwsIntegrationsVpcOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAwsRegions")
    def reset_aws_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegions", []))

    @jsii.member(jsii_name="resetFetchNatGateway")
    def reset_fetch_nat_gateway(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchNatGateway", []))

    @jsii.member(jsii_name="resetFetchVpn")
    def reset_fetch_vpn(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchVpn", []))

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetTagKey")
    def reset_tag_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagKey", []))

    @jsii.member(jsii_name="resetTagValue")
    def reset_tag_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTagValue", []))

    @builtins.property
    @jsii.member(jsii_name="awsRegionsInput")
    def aws_regions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "awsRegionsInput"))

    @builtins.property
    @jsii.member(jsii_name="fetchNatGatewayInput")
    def fetch_nat_gateway_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fetchNatGatewayInput"))

    @builtins.property
    @jsii.member(jsii_name="fetchVpnInput")
    def fetch_vpn_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fetchVpnInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="tagKeyInput")
    def tag_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="tagValueInput")
    def tag_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagValueInput"))

    @builtins.property
    @jsii.member(jsii_name="awsRegions")
    def aws_regions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "awsRegions"))

    @aws_regions.setter
    def aws_regions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsIntegrationsVpcOutputReference, "aws_regions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="fetchNatGateway")
    def fetch_nat_gateway(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "fetchNatGateway"))

    @fetch_nat_gateway.setter
    def fetch_nat_gateway(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsIntegrationsVpcOutputReference, "fetch_nat_gateway").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchNatGateway", value)

    @builtins.property
    @jsii.member(jsii_name="fetchVpn")
    def fetch_vpn(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "fetchVpn"))

    @fetch_vpn.setter
    def fetch_vpn(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsIntegrationsVpcOutputReference, "fetch_vpn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchVpn", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsIntegrationsVpcOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="tagKey")
    def tag_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagKey"))

    @tag_key.setter
    def tag_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsIntegrationsVpcOutputReference, "tag_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagKey", value)

    @builtins.property
    @jsii.member(jsii_name="tagValue")
    def tag_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagValue"))

    @tag_value.setter
    def tag_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsIntegrationsVpcOutputReference, "tag_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsIntegrationsVpc]:
        return typing.cast(typing.Optional[CloudAwsIntegrationsVpc], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CloudAwsIntegrationsVpc]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsIntegrationsVpcOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsXRay",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "metrics_polling_interval": "metricsPollingInterval",
    },
)
class CloudAwsIntegrationsXRay:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAwsIntegrationsXRay.__init__)
            check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if aws_regions is not None:
            self._values["aws_regions"] = aws_regions
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each AWS region that includes the resources that you want to monitor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#aws_regions CloudAwsIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_integrations#metrics_polling_interval CloudAwsIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsIntegrationsXRay(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsIntegrationsXRayOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsIntegrations.CloudAwsIntegrationsXRayOutputReference",
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
            type_hints = typing.get_type_hints(CloudAwsIntegrationsXRayOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAwsRegions")
    def reset_aws_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegions", []))

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="awsRegionsInput")
    def aws_regions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "awsRegionsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="awsRegions")
    def aws_regions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "awsRegions"))

    @aws_regions.setter
    def aws_regions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsIntegrationsXRayOutputReference, "aws_regions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsIntegrationsXRayOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsIntegrationsXRay]:
        return typing.cast(typing.Optional[CloudAwsIntegrationsXRay], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CloudAwsIntegrationsXRay]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsIntegrationsXRayOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CloudAwsIntegrations",
    "CloudAwsIntegrationsBilling",
    "CloudAwsIntegrationsBillingOutputReference",
    "CloudAwsIntegrationsCloudtrail",
    "CloudAwsIntegrationsCloudtrailOutputReference",
    "CloudAwsIntegrationsConfig",
    "CloudAwsIntegrationsHealth",
    "CloudAwsIntegrationsHealthOutputReference",
    "CloudAwsIntegrationsTrustedAdvisor",
    "CloudAwsIntegrationsTrustedAdvisorOutputReference",
    "CloudAwsIntegrationsVpc",
    "CloudAwsIntegrationsVpcOutputReference",
    "CloudAwsIntegrationsXRay",
    "CloudAwsIntegrationsXRayOutputReference",
]

publication.publish()
