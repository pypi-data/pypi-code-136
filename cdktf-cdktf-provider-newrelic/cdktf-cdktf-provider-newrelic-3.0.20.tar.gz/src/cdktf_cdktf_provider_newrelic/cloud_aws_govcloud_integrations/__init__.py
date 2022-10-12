'''
# `newrelic_cloud_aws_govcloud_integrations`

Refer to the Terraform Registory for docs: [`newrelic_cloud_aws_govcloud_integrations`](https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations).
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


class CloudAwsGovcloudIntegrations(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrations",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations newrelic_cloud_aws_govcloud_integrations}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        linked_account_id: jsii.Number,
        account_id: typing.Optional[jsii.Number] = None,
        alb: typing.Optional[typing.Union["CloudAwsGovcloudIntegrationsAlb", typing.Dict[str, typing.Any]]] = None,
        api_gateway: typing.Optional[typing.Union["CloudAwsGovcloudIntegrationsApiGateway", typing.Dict[str, typing.Any]]] = None,
        auto_scaling: typing.Optional[typing.Union["CloudAwsGovcloudIntegrationsAutoScaling", typing.Dict[str, typing.Any]]] = None,
        aws_direct_connect: typing.Optional[typing.Union["CloudAwsGovcloudIntegrationsAwsDirectConnect", typing.Dict[str, typing.Any]]] = None,
        aws_states: typing.Optional[typing.Union["CloudAwsGovcloudIntegrationsAwsStates", typing.Dict[str, typing.Any]]] = None,
        cloudtrail: typing.Optional[typing.Union["CloudAwsGovcloudIntegrationsCloudtrail", typing.Dict[str, typing.Any]]] = None,
        dynamo_db: typing.Optional[typing.Union["CloudAwsGovcloudIntegrationsDynamoDb", typing.Dict[str, typing.Any]]] = None,
        ebs: typing.Optional[typing.Union["CloudAwsGovcloudIntegrationsEbs", typing.Dict[str, typing.Any]]] = None,
        ec2: typing.Optional[typing.Union["CloudAwsGovcloudIntegrationsEc2", typing.Dict[str, typing.Any]]] = None,
        elastic_search: typing.Optional[typing.Union["CloudAwsGovcloudIntegrationsElasticSearch", typing.Dict[str, typing.Any]]] = None,
        elb: typing.Optional[typing.Union["CloudAwsGovcloudIntegrationsElb", typing.Dict[str, typing.Any]]] = None,
        emr: typing.Optional[typing.Union["CloudAwsGovcloudIntegrationsEmr", typing.Dict[str, typing.Any]]] = None,
        iam: typing.Optional[typing.Union["CloudAwsGovcloudIntegrationsIam", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        lambda_: typing.Optional[typing.Union["CloudAwsGovcloudIntegrationsLambda", typing.Dict[str, typing.Any]]] = None,
        rds: typing.Optional[typing.Union["CloudAwsGovcloudIntegrationsRds", typing.Dict[str, typing.Any]]] = None,
        red_shift: typing.Optional[typing.Union["CloudAwsGovcloudIntegrationsRedShift", typing.Dict[str, typing.Any]]] = None,
        route53: typing.Optional[typing.Union["CloudAwsGovcloudIntegrationsRoute53", typing.Dict[str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union["CloudAwsGovcloudIntegrationsS3", typing.Dict[str, typing.Any]]] = None,
        sns: typing.Optional[typing.Union["CloudAwsGovcloudIntegrationsSns", typing.Dict[str, typing.Any]]] = None,
        sqs: typing.Optional[typing.Union["CloudAwsGovcloudIntegrationsSqs", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations newrelic_cloud_aws_govcloud_integrations} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param linked_account_id: The ID of the linked AwsGovCloud account in New Relic. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#linked_account_id CloudAwsGovcloudIntegrations#linked_account_id}
        :param account_id: The ID of the account in New Relic. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#account_id CloudAwsGovcloudIntegrations#account_id}
        :param alb: alb block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#alb CloudAwsGovcloudIntegrations#alb}
        :param api_gateway: api_gateway block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#api_gateway CloudAwsGovcloudIntegrations#api_gateway}
        :param auto_scaling: auto_scaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#auto_scaling CloudAwsGovcloudIntegrations#auto_scaling}
        :param aws_direct_connect: aws_direct_connect block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_direct_connect CloudAwsGovcloudIntegrations#aws_direct_connect}
        :param aws_states: aws_states block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_states CloudAwsGovcloudIntegrations#aws_states}
        :param cloudtrail: cloudtrail block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#cloudtrail CloudAwsGovcloudIntegrations#cloudtrail}
        :param dynamo_db: dynamo_db block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#dynamo_db CloudAwsGovcloudIntegrations#dynamo_db}
        :param ebs: ebs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#ebs CloudAwsGovcloudIntegrations#ebs}
        :param ec2: ec2 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#ec2 CloudAwsGovcloudIntegrations#ec2}
        :param elastic_search: elastic_search block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#elastic_search CloudAwsGovcloudIntegrations#elastic_search}
        :param elb: elb block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#elb CloudAwsGovcloudIntegrations#elb}
        :param emr: emr block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#emr CloudAwsGovcloudIntegrations#emr}
        :param iam: iam block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#iam CloudAwsGovcloudIntegrations#iam}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#id CloudAwsGovcloudIntegrations#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param lambda_: lambda block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#lambda CloudAwsGovcloudIntegrations#lambda}
        :param rds: rds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#rds CloudAwsGovcloudIntegrations#rds}
        :param red_shift: red_shift block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#red_shift CloudAwsGovcloudIntegrations#red_shift}
        :param route53: route53 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#route53 CloudAwsGovcloudIntegrations#route53}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#s3 CloudAwsGovcloudIntegrations#s3}
        :param sns: sns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#sns CloudAwsGovcloudIntegrations#sns}
        :param sqs: sqs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#sqs CloudAwsGovcloudIntegrations#sqs}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrations.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CloudAwsGovcloudIntegrationsConfig(
            linked_account_id=linked_account_id,
            account_id=account_id,
            alb=alb,
            api_gateway=api_gateway,
            auto_scaling=auto_scaling,
            aws_direct_connect=aws_direct_connect,
            aws_states=aws_states,
            cloudtrail=cloudtrail,
            dynamo_db=dynamo_db,
            ebs=ebs,
            ec2=ec2,
            elastic_search=elastic_search,
            elb=elb,
            emr=emr,
            iam=iam,
            id=id,
            lambda_=lambda_,
            rds=rds,
            red_shift=red_shift,
            route53=route53,
            s3=s3,
            sns=sns,
            sqs=sqs,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAlb")
    def put_alb(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        fetch_extended_inventory: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        fetch_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        load_balancer_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        :param fetch_extended_inventory: Determine if extra inventory data be collected or not. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_extended_inventory CloudAwsGovcloudIntegrations#fetch_extended_inventory}
        :param fetch_tags: Specify if tags should be collected. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_tags CloudAwsGovcloudIntegrations#fetch_tags}
        :param load_balancer_prefixes: Specify each name or prefix for the LBs that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#load_balancer_prefixes CloudAwsGovcloudIntegrations#load_balancer_prefixes}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        value = CloudAwsGovcloudIntegrationsAlb(
            aws_regions=aws_regions,
            fetch_extended_inventory=fetch_extended_inventory,
            fetch_tags=fetch_tags,
            load_balancer_prefixes=load_balancer_prefixes,
            metrics_polling_interval=metrics_polling_interval,
            tag_key=tag_key,
            tag_value=tag_value,
        )

        return typing.cast(None, jsii.invoke(self, "putAlb", [value]))

    @jsii.member(jsii_name="putApiGateway")
    def put_api_gateway(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        stage_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        :param stage_prefixes: Determine if extra inventory data be collected or not. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#stage_prefixes CloudAwsGovcloudIntegrations#stage_prefixes}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        value = CloudAwsGovcloudIntegrationsApiGateway(
            aws_regions=aws_regions,
            metrics_polling_interval=metrics_polling_interval,
            stage_prefixes=stage_prefixes,
            tag_key=tag_key,
            tag_value=tag_value,
        )

        return typing.cast(None, jsii.invoke(self, "putApiGateway", [value]))

    @jsii.member(jsii_name="putAutoScaling")
    def put_auto_scaling(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        '''
        value = CloudAwsGovcloudIntegrationsAutoScaling(
            aws_regions=aws_regions, metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putAutoScaling", [value]))

    @jsii.member(jsii_name="putAwsDirectConnect")
    def put_aws_direct_connect(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        '''
        value = CloudAwsGovcloudIntegrationsAwsDirectConnect(
            aws_regions=aws_regions, metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putAwsDirectConnect", [value]))

    @jsii.member(jsii_name="putAwsStates")
    def put_aws_states(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        '''
        value = CloudAwsGovcloudIntegrationsAwsStates(
            aws_regions=aws_regions, metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putAwsStates", [value]))

    @jsii.member(jsii_name="putCloudtrail")
    def put_cloudtrail(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        '''
        value = CloudAwsGovcloudIntegrationsCloudtrail(
            aws_regions=aws_regions, metrics_polling_interval=metrics_polling_interval
        )

        return typing.cast(None, jsii.invoke(self, "putCloudtrail", [value]))

    @jsii.member(jsii_name="putDynamoDb")
    def put_dynamo_db(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        fetch_extended_inventory: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        fetch_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        :param fetch_extended_inventory: Determine if extra inventory data be collected or not. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_extended_inventory CloudAwsGovcloudIntegrations#fetch_extended_inventory}
        :param fetch_tags: Specify if tags should be collected. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_tags CloudAwsGovcloudIntegrations#fetch_tags}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        value = CloudAwsGovcloudIntegrationsDynamoDb(
            aws_regions=aws_regions,
            fetch_extended_inventory=fetch_extended_inventory,
            fetch_tags=fetch_tags,
            metrics_polling_interval=metrics_polling_interval,
            tag_key=tag_key,
            tag_value=tag_value,
        )

        return typing.cast(None, jsii.invoke(self, "putDynamoDb", [value]))

    @jsii.member(jsii_name="putEbs")
    def put_ebs(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        fetch_extended_inventory: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        :param fetch_extended_inventory: Determine if extra inventory data be collected or not. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_extended_inventory CloudAwsGovcloudIntegrations#fetch_extended_inventory}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        value = CloudAwsGovcloudIntegrationsEbs(
            aws_regions=aws_regions,
            fetch_extended_inventory=fetch_extended_inventory,
            metrics_polling_interval=metrics_polling_interval,
            tag_key=tag_key,
            tag_value=tag_value,
        )

        return typing.cast(None, jsii.invoke(self, "putEbs", [value]))

    @jsii.member(jsii_name="putEc2")
    def put_ec2(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        fetch_ip_addresses: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        :param fetch_ip_addresses: Specify if IP addresses of ec2 instance should be collected. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_ip_addresses CloudAwsGovcloudIntegrations#fetch_ip_addresses}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        value = CloudAwsGovcloudIntegrationsEc2(
            aws_regions=aws_regions,
            fetch_ip_addresses=fetch_ip_addresses,
            metrics_polling_interval=metrics_polling_interval,
            tag_key=tag_key,
            tag_value=tag_value,
        )

        return typing.cast(None, jsii.invoke(self, "putEc2", [value]))

    @jsii.member(jsii_name="putElasticSearch")
    def put_elastic_search(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        fetch_nodes: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        :param fetch_nodes: Specify if IP addresses of ec2 instance should be collected. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_nodes CloudAwsGovcloudIntegrations#fetch_nodes}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        value = CloudAwsGovcloudIntegrationsElasticSearch(
            aws_regions=aws_regions,
            fetch_nodes=fetch_nodes,
            metrics_polling_interval=metrics_polling_interval,
            tag_key=tag_key,
            tag_value=tag_value,
        )

        return typing.cast(None, jsii.invoke(self, "putElasticSearch", [value]))

    @jsii.member(jsii_name="putElb")
    def put_elb(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        fetch_extended_inventory: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        fetch_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        :param fetch_extended_inventory: Determine if extra inventory data be collected or not. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_extended_inventory CloudAwsGovcloudIntegrations#fetch_extended_inventory}
        :param fetch_tags: Specify if tags should be collected. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_tags CloudAwsGovcloudIntegrations#fetch_tags}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        '''
        value = CloudAwsGovcloudIntegrationsElb(
            aws_regions=aws_regions,
            fetch_extended_inventory=fetch_extended_inventory,
            fetch_tags=fetch_tags,
            metrics_polling_interval=metrics_polling_interval,
        )

        return typing.cast(None, jsii.invoke(self, "putElb", [value]))

    @jsii.member(jsii_name="putEmr")
    def put_emr(
        self,
        *,
        aws_regions: typing.Optional[builtins.str] = None,
        fetch_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        :param fetch_tags: Specify if tags should be collected. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_tags CloudAwsGovcloudIntegrations#fetch_tags}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        value = CloudAwsGovcloudIntegrationsEmr(
            aws_regions=aws_regions,
            fetch_tags=fetch_tags,
            metrics_polling_interval=metrics_polling_interval,
            tag_key=tag_key,
            tag_value=tag_value,
        )

        return typing.cast(None, jsii.invoke(self, "putEmr", [value]))

    @jsii.member(jsii_name="putIam")
    def put_iam(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        value = CloudAwsGovcloudIntegrationsIam(
            metrics_polling_interval=metrics_polling_interval,
            tag_key=tag_key,
            tag_value=tag_value,
        )

        return typing.cast(None, jsii.invoke(self, "putIam", [value]))

    @jsii.member(jsii_name="putLambda")
    def put_lambda(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        fetch_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        :param fetch_tags: Specify if tags should be collected. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_tags CloudAwsGovcloudIntegrations#fetch_tags}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        value = CloudAwsGovcloudIntegrationsLambda(
            aws_regions=aws_regions,
            fetch_tags=fetch_tags,
            metrics_polling_interval=metrics_polling_interval,
            tag_key=tag_key,
            tag_value=tag_value,
        )

        return typing.cast(None, jsii.invoke(self, "putLambda", [value]))

    @jsii.member(jsii_name="putRds")
    def put_rds(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        fetch_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        :param fetch_tags: Specify if tags should be collected. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_tags CloudAwsGovcloudIntegrations#fetch_tags}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        value = CloudAwsGovcloudIntegrationsRds(
            aws_regions=aws_regions,
            fetch_tags=fetch_tags,
            metrics_polling_interval=metrics_polling_interval,
            tag_key=tag_key,
            tag_value=tag_value,
        )

        return typing.cast(None, jsii.invoke(self, "putRds", [value]))

    @jsii.member(jsii_name="putRedShift")
    def put_red_shift(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        value = CloudAwsGovcloudIntegrationsRedShift(
            aws_regions=aws_regions,
            metrics_polling_interval=metrics_polling_interval,
            tag_key=tag_key,
            tag_value=tag_value,
        )

        return typing.cast(None, jsii.invoke(self, "putRedShift", [value]))

    @jsii.member(jsii_name="putRoute53")
    def put_route53(
        self,
        *,
        fetch_extended_inventory: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param fetch_extended_inventory: Determine if extra inventory data be collected or not. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_extended_inventory CloudAwsGovcloudIntegrations#fetch_extended_inventory}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        '''
        value = CloudAwsGovcloudIntegrationsRoute53(
            fetch_extended_inventory=fetch_extended_inventory,
            metrics_polling_interval=metrics_polling_interval,
        )

        return typing.cast(None, jsii.invoke(self, "putRoute53", [value]))

    @jsii.member(jsii_name="putS3")
    def put_s3(
        self,
        *,
        fetch_extended_inventory: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        fetch_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param fetch_extended_inventory: Determine if extra inventory data be collected or not. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_extended_inventory CloudAwsGovcloudIntegrations#fetch_extended_inventory}
        :param fetch_tags: Specify if tags should be collected. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_tags CloudAwsGovcloudIntegrations#fetch_tags}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        value = CloudAwsGovcloudIntegrationsS3(
            fetch_extended_inventory=fetch_extended_inventory,
            fetch_tags=fetch_tags,
            metrics_polling_interval=metrics_polling_interval,
            tag_key=tag_key,
            tag_value=tag_value,
        )

        return typing.cast(None, jsii.invoke(self, "putS3", [value]))

    @jsii.member(jsii_name="putSns")
    def put_sns(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        fetch_extended_inventory: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        :param fetch_extended_inventory: Determine if extra inventory data be collected or not. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_extended_inventory CloudAwsGovcloudIntegrations#fetch_extended_inventory}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        '''
        value = CloudAwsGovcloudIntegrationsSns(
            aws_regions=aws_regions,
            fetch_extended_inventory=fetch_extended_inventory,
            metrics_polling_interval=metrics_polling_interval,
        )

        return typing.cast(None, jsii.invoke(self, "putSns", [value]))

    @jsii.member(jsii_name="putSqs")
    def put_sqs(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        fetch_extended_inventory: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        fetch_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        queue_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        :param fetch_extended_inventory: Determine if extra inventory data be collected or not. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_extended_inventory CloudAwsGovcloudIntegrations#fetch_extended_inventory}
        :param fetch_tags: Specify if tags should be collected. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_tags CloudAwsGovcloudIntegrations#fetch_tags}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        :param queue_prefixes: Specify each name or prefix for the Queues that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#queue_prefixes CloudAwsGovcloudIntegrations#queue_prefixes}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        value = CloudAwsGovcloudIntegrationsSqs(
            aws_regions=aws_regions,
            fetch_extended_inventory=fetch_extended_inventory,
            fetch_tags=fetch_tags,
            metrics_polling_interval=metrics_polling_interval,
            queue_prefixes=queue_prefixes,
            tag_key=tag_key,
            tag_value=tag_value,
        )

        return typing.cast(None, jsii.invoke(self, "putSqs", [value]))

    @jsii.member(jsii_name="resetAccountId")
    def reset_account_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountId", []))

    @jsii.member(jsii_name="resetAlb")
    def reset_alb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlb", []))

    @jsii.member(jsii_name="resetApiGateway")
    def reset_api_gateway(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiGateway", []))

    @jsii.member(jsii_name="resetAutoScaling")
    def reset_auto_scaling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoScaling", []))

    @jsii.member(jsii_name="resetAwsDirectConnect")
    def reset_aws_direct_connect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsDirectConnect", []))

    @jsii.member(jsii_name="resetAwsStates")
    def reset_aws_states(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsStates", []))

    @jsii.member(jsii_name="resetCloudtrail")
    def reset_cloudtrail(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudtrail", []))

    @jsii.member(jsii_name="resetDynamoDb")
    def reset_dynamo_db(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDynamoDb", []))

    @jsii.member(jsii_name="resetEbs")
    def reset_ebs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEbs", []))

    @jsii.member(jsii_name="resetEc2")
    def reset_ec2(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEc2", []))

    @jsii.member(jsii_name="resetElasticSearch")
    def reset_elastic_search(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetElasticSearch", []))

    @jsii.member(jsii_name="resetElb")
    def reset_elb(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetElb", []))

    @jsii.member(jsii_name="resetEmr")
    def reset_emr(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmr", []))

    @jsii.member(jsii_name="resetIam")
    def reset_iam(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIam", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLambda")
    def reset_lambda(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLambda", []))

    @jsii.member(jsii_name="resetRds")
    def reset_rds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRds", []))

    @jsii.member(jsii_name="resetRedShift")
    def reset_red_shift(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRedShift", []))

    @jsii.member(jsii_name="resetRoute53")
    def reset_route53(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoute53", []))

    @jsii.member(jsii_name="resetS3")
    def reset_s3(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetS3", []))

    @jsii.member(jsii_name="resetSns")
    def reset_sns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSns", []))

    @jsii.member(jsii_name="resetSqs")
    def reset_sqs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSqs", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="alb")
    def alb(self) -> "CloudAwsGovcloudIntegrationsAlbOutputReference":
        return typing.cast("CloudAwsGovcloudIntegrationsAlbOutputReference", jsii.get(self, "alb"))

    @builtins.property
    @jsii.member(jsii_name="apiGateway")
    def api_gateway(self) -> "CloudAwsGovcloudIntegrationsApiGatewayOutputReference":
        return typing.cast("CloudAwsGovcloudIntegrationsApiGatewayOutputReference", jsii.get(self, "apiGateway"))

    @builtins.property
    @jsii.member(jsii_name="autoScaling")
    def auto_scaling(self) -> "CloudAwsGovcloudIntegrationsAutoScalingOutputReference":
        return typing.cast("CloudAwsGovcloudIntegrationsAutoScalingOutputReference", jsii.get(self, "autoScaling"))

    @builtins.property
    @jsii.member(jsii_name="awsDirectConnect")
    def aws_direct_connect(
        self,
    ) -> "CloudAwsGovcloudIntegrationsAwsDirectConnectOutputReference":
        return typing.cast("CloudAwsGovcloudIntegrationsAwsDirectConnectOutputReference", jsii.get(self, "awsDirectConnect"))

    @builtins.property
    @jsii.member(jsii_name="awsStates")
    def aws_states(self) -> "CloudAwsGovcloudIntegrationsAwsStatesOutputReference":
        return typing.cast("CloudAwsGovcloudIntegrationsAwsStatesOutputReference", jsii.get(self, "awsStates"))

    @builtins.property
    @jsii.member(jsii_name="cloudtrail")
    def cloudtrail(self) -> "CloudAwsGovcloudIntegrationsCloudtrailOutputReference":
        return typing.cast("CloudAwsGovcloudIntegrationsCloudtrailOutputReference", jsii.get(self, "cloudtrail"))

    @builtins.property
    @jsii.member(jsii_name="dynamoDb")
    def dynamo_db(self) -> "CloudAwsGovcloudIntegrationsDynamoDbOutputReference":
        return typing.cast("CloudAwsGovcloudIntegrationsDynamoDbOutputReference", jsii.get(self, "dynamoDb"))

    @builtins.property
    @jsii.member(jsii_name="ebs")
    def ebs(self) -> "CloudAwsGovcloudIntegrationsEbsOutputReference":
        return typing.cast("CloudAwsGovcloudIntegrationsEbsOutputReference", jsii.get(self, "ebs"))

    @builtins.property
    @jsii.member(jsii_name="ec2")
    def ec2(self) -> "CloudAwsGovcloudIntegrationsEc2OutputReference":
        return typing.cast("CloudAwsGovcloudIntegrationsEc2OutputReference", jsii.get(self, "ec2"))

    @builtins.property
    @jsii.member(jsii_name="elasticSearch")
    def elastic_search(
        self,
    ) -> "CloudAwsGovcloudIntegrationsElasticSearchOutputReference":
        return typing.cast("CloudAwsGovcloudIntegrationsElasticSearchOutputReference", jsii.get(self, "elasticSearch"))

    @builtins.property
    @jsii.member(jsii_name="elb")
    def elb(self) -> "CloudAwsGovcloudIntegrationsElbOutputReference":
        return typing.cast("CloudAwsGovcloudIntegrationsElbOutputReference", jsii.get(self, "elb"))

    @builtins.property
    @jsii.member(jsii_name="emr")
    def emr(self) -> "CloudAwsGovcloudIntegrationsEmrOutputReference":
        return typing.cast("CloudAwsGovcloudIntegrationsEmrOutputReference", jsii.get(self, "emr"))

    @builtins.property
    @jsii.member(jsii_name="iam")
    def iam(self) -> "CloudAwsGovcloudIntegrationsIamOutputReference":
        return typing.cast("CloudAwsGovcloudIntegrationsIamOutputReference", jsii.get(self, "iam"))

    @builtins.property
    @jsii.member(jsii_name="lambda")
    def lambda_(self) -> "CloudAwsGovcloudIntegrationsLambdaOutputReference":
        return typing.cast("CloudAwsGovcloudIntegrationsLambdaOutputReference", jsii.get(self, "lambda"))

    @builtins.property
    @jsii.member(jsii_name="rds")
    def rds(self) -> "CloudAwsGovcloudIntegrationsRdsOutputReference":
        return typing.cast("CloudAwsGovcloudIntegrationsRdsOutputReference", jsii.get(self, "rds"))

    @builtins.property
    @jsii.member(jsii_name="redShift")
    def red_shift(self) -> "CloudAwsGovcloudIntegrationsRedShiftOutputReference":
        return typing.cast("CloudAwsGovcloudIntegrationsRedShiftOutputReference", jsii.get(self, "redShift"))

    @builtins.property
    @jsii.member(jsii_name="route53")
    def route53(self) -> "CloudAwsGovcloudIntegrationsRoute53OutputReference":
        return typing.cast("CloudAwsGovcloudIntegrationsRoute53OutputReference", jsii.get(self, "route53"))

    @builtins.property
    @jsii.member(jsii_name="s3")
    def s3(self) -> "CloudAwsGovcloudIntegrationsS3OutputReference":
        return typing.cast("CloudAwsGovcloudIntegrationsS3OutputReference", jsii.get(self, "s3"))

    @builtins.property
    @jsii.member(jsii_name="sns")
    def sns(self) -> "CloudAwsGovcloudIntegrationsSnsOutputReference":
        return typing.cast("CloudAwsGovcloudIntegrationsSnsOutputReference", jsii.get(self, "sns"))

    @builtins.property
    @jsii.member(jsii_name="sqs")
    def sqs(self) -> "CloudAwsGovcloudIntegrationsSqsOutputReference":
        return typing.cast("CloudAwsGovcloudIntegrationsSqsOutputReference", jsii.get(self, "sqs"))

    @builtins.property
    @jsii.member(jsii_name="accountIdInput")
    def account_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "accountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="albInput")
    def alb_input(self) -> typing.Optional["CloudAwsGovcloudIntegrationsAlb"]:
        return typing.cast(typing.Optional["CloudAwsGovcloudIntegrationsAlb"], jsii.get(self, "albInput"))

    @builtins.property
    @jsii.member(jsii_name="apiGatewayInput")
    def api_gateway_input(
        self,
    ) -> typing.Optional["CloudAwsGovcloudIntegrationsApiGateway"]:
        return typing.cast(typing.Optional["CloudAwsGovcloudIntegrationsApiGateway"], jsii.get(self, "apiGatewayInput"))

    @builtins.property
    @jsii.member(jsii_name="autoScalingInput")
    def auto_scaling_input(
        self,
    ) -> typing.Optional["CloudAwsGovcloudIntegrationsAutoScaling"]:
        return typing.cast(typing.Optional["CloudAwsGovcloudIntegrationsAutoScaling"], jsii.get(self, "autoScalingInput"))

    @builtins.property
    @jsii.member(jsii_name="awsDirectConnectInput")
    def aws_direct_connect_input(
        self,
    ) -> typing.Optional["CloudAwsGovcloudIntegrationsAwsDirectConnect"]:
        return typing.cast(typing.Optional["CloudAwsGovcloudIntegrationsAwsDirectConnect"], jsii.get(self, "awsDirectConnectInput"))

    @builtins.property
    @jsii.member(jsii_name="awsStatesInput")
    def aws_states_input(
        self,
    ) -> typing.Optional["CloudAwsGovcloudIntegrationsAwsStates"]:
        return typing.cast(typing.Optional["CloudAwsGovcloudIntegrationsAwsStates"], jsii.get(self, "awsStatesInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudtrailInput")
    def cloudtrail_input(
        self,
    ) -> typing.Optional["CloudAwsGovcloudIntegrationsCloudtrail"]:
        return typing.cast(typing.Optional["CloudAwsGovcloudIntegrationsCloudtrail"], jsii.get(self, "cloudtrailInput"))

    @builtins.property
    @jsii.member(jsii_name="dynamoDbInput")
    def dynamo_db_input(
        self,
    ) -> typing.Optional["CloudAwsGovcloudIntegrationsDynamoDb"]:
        return typing.cast(typing.Optional["CloudAwsGovcloudIntegrationsDynamoDb"], jsii.get(self, "dynamoDbInput"))

    @builtins.property
    @jsii.member(jsii_name="ebsInput")
    def ebs_input(self) -> typing.Optional["CloudAwsGovcloudIntegrationsEbs"]:
        return typing.cast(typing.Optional["CloudAwsGovcloudIntegrationsEbs"], jsii.get(self, "ebsInput"))

    @builtins.property
    @jsii.member(jsii_name="ec2Input")
    def ec2_input(self) -> typing.Optional["CloudAwsGovcloudIntegrationsEc2"]:
        return typing.cast(typing.Optional["CloudAwsGovcloudIntegrationsEc2"], jsii.get(self, "ec2Input"))

    @builtins.property
    @jsii.member(jsii_name="elasticSearchInput")
    def elastic_search_input(
        self,
    ) -> typing.Optional["CloudAwsGovcloudIntegrationsElasticSearch"]:
        return typing.cast(typing.Optional["CloudAwsGovcloudIntegrationsElasticSearch"], jsii.get(self, "elasticSearchInput"))

    @builtins.property
    @jsii.member(jsii_name="elbInput")
    def elb_input(self) -> typing.Optional["CloudAwsGovcloudIntegrationsElb"]:
        return typing.cast(typing.Optional["CloudAwsGovcloudIntegrationsElb"], jsii.get(self, "elbInput"))

    @builtins.property
    @jsii.member(jsii_name="emrInput")
    def emr_input(self) -> typing.Optional["CloudAwsGovcloudIntegrationsEmr"]:
        return typing.cast(typing.Optional["CloudAwsGovcloudIntegrationsEmr"], jsii.get(self, "emrInput"))

    @builtins.property
    @jsii.member(jsii_name="iamInput")
    def iam_input(self) -> typing.Optional["CloudAwsGovcloudIntegrationsIam"]:
        return typing.cast(typing.Optional["CloudAwsGovcloudIntegrationsIam"], jsii.get(self, "iamInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="lambdaInput")
    def lambda_input(self) -> typing.Optional["CloudAwsGovcloudIntegrationsLambda"]:
        return typing.cast(typing.Optional["CloudAwsGovcloudIntegrationsLambda"], jsii.get(self, "lambdaInput"))

    @builtins.property
    @jsii.member(jsii_name="linkedAccountIdInput")
    def linked_account_id_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "linkedAccountIdInput"))

    @builtins.property
    @jsii.member(jsii_name="rdsInput")
    def rds_input(self) -> typing.Optional["CloudAwsGovcloudIntegrationsRds"]:
        return typing.cast(typing.Optional["CloudAwsGovcloudIntegrationsRds"], jsii.get(self, "rdsInput"))

    @builtins.property
    @jsii.member(jsii_name="redShiftInput")
    def red_shift_input(
        self,
    ) -> typing.Optional["CloudAwsGovcloudIntegrationsRedShift"]:
        return typing.cast(typing.Optional["CloudAwsGovcloudIntegrationsRedShift"], jsii.get(self, "redShiftInput"))

    @builtins.property
    @jsii.member(jsii_name="route53Input")
    def route53_input(self) -> typing.Optional["CloudAwsGovcloudIntegrationsRoute53"]:
        return typing.cast(typing.Optional["CloudAwsGovcloudIntegrationsRoute53"], jsii.get(self, "route53Input"))

    @builtins.property
    @jsii.member(jsii_name="s3Input")
    def s3_input(self) -> typing.Optional["CloudAwsGovcloudIntegrationsS3"]:
        return typing.cast(typing.Optional["CloudAwsGovcloudIntegrationsS3"], jsii.get(self, "s3Input"))

    @builtins.property
    @jsii.member(jsii_name="snsInput")
    def sns_input(self) -> typing.Optional["CloudAwsGovcloudIntegrationsSns"]:
        return typing.cast(typing.Optional["CloudAwsGovcloudIntegrationsSns"], jsii.get(self, "snsInput"))

    @builtins.property
    @jsii.member(jsii_name="sqsInput")
    def sqs_input(self) -> typing.Optional["CloudAwsGovcloudIntegrationsSqs"]:
        return typing.cast(typing.Optional["CloudAwsGovcloudIntegrationsSqs"], jsii.get(self, "sqsInput"))

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrations, "account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrations, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="linkedAccountId")
    def linked_account_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "linkedAccountId"))

    @linked_account_id.setter
    def linked_account_id(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrations, "linked_account_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "linkedAccountId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsAlb",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "fetch_extended_inventory": "fetchExtendedInventory",
        "fetch_tags": "fetchTags",
        "load_balancer_prefixes": "loadBalancerPrefixes",
        "metrics_polling_interval": "metricsPollingInterval",
        "tag_key": "tagKey",
        "tag_value": "tagValue",
    },
)
class CloudAwsGovcloudIntegrationsAlb:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        fetch_extended_inventory: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        fetch_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        load_balancer_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        :param fetch_extended_inventory: Determine if extra inventory data be collected or not. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_extended_inventory CloudAwsGovcloudIntegrations#fetch_extended_inventory}
        :param fetch_tags: Specify if tags should be collected. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_tags CloudAwsGovcloudIntegrations#fetch_tags}
        :param load_balancer_prefixes: Specify each name or prefix for the LBs that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#load_balancer_prefixes CloudAwsGovcloudIntegrations#load_balancer_prefixes}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsAlb.__init__)
            check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            check_type(argname="argument fetch_extended_inventory", value=fetch_extended_inventory, expected_type=type_hints["fetch_extended_inventory"])
            check_type(argname="argument fetch_tags", value=fetch_tags, expected_type=type_hints["fetch_tags"])
            check_type(argname="argument load_balancer_prefixes", value=load_balancer_prefixes, expected_type=type_hints["load_balancer_prefixes"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
            check_type(argname="argument tag_value", value=tag_value, expected_type=type_hints["tag_value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if aws_regions is not None:
            self._values["aws_regions"] = aws_regions
        if fetch_extended_inventory is not None:
            self._values["fetch_extended_inventory"] = fetch_extended_inventory
        if fetch_tags is not None:
            self._values["fetch_tags"] = fetch_tags
        if load_balancer_prefixes is not None:
            self._values["load_balancer_prefixes"] = load_balancer_prefixes
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if tag_key is not None:
            self._values["tag_key"] = tag_key
        if tag_value is not None:
            self._values["tag_value"] = tag_value

    @builtins.property
    def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each AWS region that includes the resources that you want to monitor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def fetch_extended_inventory(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Determine if extra inventory data be collected or not.

        May affect total data collection time and contribute to the Cloud provider API rate limit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_extended_inventory CloudAwsGovcloudIntegrations#fetch_extended_inventory}
        '''
        result = self._values.get("fetch_extended_inventory")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def fetch_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specify if tags should be collected.

        May affect total data collection time and contribute to the Cloud provider API rate limit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_tags CloudAwsGovcloudIntegrations#fetch_tags}
        '''
        result = self._values.get("fetch_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def load_balancer_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each name or prefix for the LBs that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#load_balancer_prefixes CloudAwsGovcloudIntegrations#load_balancer_prefixes}
        '''
        result = self._values.get("load_balancer_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tag_key(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        '''
        result = self._values.get("tag_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_value(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        result = self._values.get("tag_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsGovcloudIntegrationsAlb(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsGovcloudIntegrationsAlbOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsAlbOutputReference",
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
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsAlbOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAwsRegions")
    def reset_aws_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegions", []))

    @jsii.member(jsii_name="resetFetchExtendedInventory")
    def reset_fetch_extended_inventory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchExtendedInventory", []))

    @jsii.member(jsii_name="resetFetchTags")
    def reset_fetch_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchTags", []))

    @jsii.member(jsii_name="resetLoadBalancerPrefixes")
    def reset_load_balancer_prefixes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoadBalancerPrefixes", []))

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
    @jsii.member(jsii_name="fetchExtendedInventoryInput")
    def fetch_extended_inventory_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fetchExtendedInventoryInput"))

    @builtins.property
    @jsii.member(jsii_name="fetchTagsInput")
    def fetch_tags_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fetchTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="loadBalancerPrefixesInput")
    def load_balancer_prefixes_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "loadBalancerPrefixesInput"))

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
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsAlbOutputReference, "aws_regions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="fetchExtendedInventory")
    def fetch_extended_inventory(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "fetchExtendedInventory"))

    @fetch_extended_inventory.setter
    def fetch_extended_inventory(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsAlbOutputReference, "fetch_extended_inventory").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchExtendedInventory", value)

    @builtins.property
    @jsii.member(jsii_name="fetchTags")
    def fetch_tags(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "fetchTags"))

    @fetch_tags.setter
    def fetch_tags(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsAlbOutputReference, "fetch_tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchTags", value)

    @builtins.property
    @jsii.member(jsii_name="loadBalancerPrefixes")
    def load_balancer_prefixes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "loadBalancerPrefixes"))

    @load_balancer_prefixes.setter
    def load_balancer_prefixes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsAlbOutputReference, "load_balancer_prefixes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancerPrefixes", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsAlbOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="tagKey")
    def tag_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagKey"))

    @tag_key.setter
    def tag_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsAlbOutputReference, "tag_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagKey", value)

    @builtins.property
    @jsii.member(jsii_name="tagValue")
    def tag_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagValue"))

    @tag_value.setter
    def tag_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsAlbOutputReference, "tag_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsGovcloudIntegrationsAlb]:
        return typing.cast(typing.Optional[CloudAwsGovcloudIntegrationsAlb], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsGovcloudIntegrationsAlb],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsAlbOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsApiGateway",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "metrics_polling_interval": "metricsPollingInterval",
        "stage_prefixes": "stagePrefixes",
        "tag_key": "tagKey",
        "tag_value": "tagValue",
    },
)
class CloudAwsGovcloudIntegrationsApiGateway:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        stage_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        :param stage_prefixes: Determine if extra inventory data be collected or not. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#stage_prefixes CloudAwsGovcloudIntegrations#stage_prefixes}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsApiGateway.__init__)
            check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument stage_prefixes", value=stage_prefixes, expected_type=type_hints["stage_prefixes"])
            check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
            check_type(argname="argument tag_value", value=tag_value, expected_type=type_hints["tag_value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if aws_regions is not None:
            self._values["aws_regions"] = aws_regions
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if stage_prefixes is not None:
            self._values["stage_prefixes"] = stage_prefixes
        if tag_key is not None:
            self._values["tag_key"] = tag_key
        if tag_value is not None:
            self._values["tag_value"] = tag_value

    @builtins.property
    def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each AWS region that includes the resources that you want to monitor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def stage_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Determine if extra inventory data be collected or not.

        May affect total data collection time and contribute to the Cloud provider API rate limit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#stage_prefixes CloudAwsGovcloudIntegrations#stage_prefixes}
        '''
        result = self._values.get("stage_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tag_key(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        '''
        result = self._values.get("tag_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_value(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        result = self._values.get("tag_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsGovcloudIntegrationsApiGateway(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsGovcloudIntegrationsApiGatewayOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsApiGatewayOutputReference",
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
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsApiGatewayOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAwsRegions")
    def reset_aws_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegions", []))

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetStagePrefixes")
    def reset_stage_prefixes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStagePrefixes", []))

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
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="stagePrefixesInput")
    def stage_prefixes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "stagePrefixesInput"))

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
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsApiGatewayOutputReference, "aws_regions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsApiGatewayOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="stagePrefixes")
    def stage_prefixes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "stagePrefixes"))

    @stage_prefixes.setter
    def stage_prefixes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsApiGatewayOutputReference, "stage_prefixes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stagePrefixes", value)

    @builtins.property
    @jsii.member(jsii_name="tagKey")
    def tag_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagKey"))

    @tag_key.setter
    def tag_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsApiGatewayOutputReference, "tag_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagKey", value)

    @builtins.property
    @jsii.member(jsii_name="tagValue")
    def tag_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagValue"))

    @tag_value.setter
    def tag_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsApiGatewayOutputReference, "tag_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsGovcloudIntegrationsApiGateway]:
        return typing.cast(typing.Optional[CloudAwsGovcloudIntegrationsApiGateway], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsGovcloudIntegrationsApiGateway],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsApiGatewayOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsAutoScaling",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "metrics_polling_interval": "metricsPollingInterval",
    },
)
class CloudAwsGovcloudIntegrationsAutoScaling:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsAutoScaling.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsGovcloudIntegrationsAutoScaling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsGovcloudIntegrationsAutoScalingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsAutoScalingOutputReference",
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
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsAutoScalingOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsAutoScalingOutputReference, "aws_regions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsAutoScalingOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudAwsGovcloudIntegrationsAutoScaling]:
        return typing.cast(typing.Optional[CloudAwsGovcloudIntegrationsAutoScaling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsGovcloudIntegrationsAutoScaling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsAutoScalingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsAwsDirectConnect",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "metrics_polling_interval": "metricsPollingInterval",
    },
)
class CloudAwsGovcloudIntegrationsAwsDirectConnect:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsAwsDirectConnect.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsGovcloudIntegrationsAwsDirectConnect(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsGovcloudIntegrationsAwsDirectConnectOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsAwsDirectConnectOutputReference",
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
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsAwsDirectConnectOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsAwsDirectConnectOutputReference, "aws_regions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsAwsDirectConnectOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudAwsGovcloudIntegrationsAwsDirectConnect]:
        return typing.cast(typing.Optional[CloudAwsGovcloudIntegrationsAwsDirectConnect], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsGovcloudIntegrationsAwsDirectConnect],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsAwsDirectConnectOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsAwsStates",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "metrics_polling_interval": "metricsPollingInterval",
    },
)
class CloudAwsGovcloudIntegrationsAwsStates:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsAwsStates.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsGovcloudIntegrationsAwsStates(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsGovcloudIntegrationsAwsStatesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsAwsStatesOutputReference",
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
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsAwsStatesOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsAwsStatesOutputReference, "aws_regions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsAwsStatesOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsGovcloudIntegrationsAwsStates]:
        return typing.cast(typing.Optional[CloudAwsGovcloudIntegrationsAwsStates], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsGovcloudIntegrationsAwsStates],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsAwsStatesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsCloudtrail",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "metrics_polling_interval": "metricsPollingInterval",
    },
)
class CloudAwsGovcloudIntegrationsCloudtrail:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsCloudtrail.__init__)
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

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsGovcloudIntegrationsCloudtrail(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsGovcloudIntegrationsCloudtrailOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsCloudtrailOutputReference",
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
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsCloudtrailOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsCloudtrailOutputReference, "aws_regions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsCloudtrailOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsGovcloudIntegrationsCloudtrail]:
        return typing.cast(typing.Optional[CloudAwsGovcloudIntegrationsCloudtrail], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsGovcloudIntegrationsCloudtrail],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsCloudtrailOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsConfig",
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
        "alb": "alb",
        "api_gateway": "apiGateway",
        "auto_scaling": "autoScaling",
        "aws_direct_connect": "awsDirectConnect",
        "aws_states": "awsStates",
        "cloudtrail": "cloudtrail",
        "dynamo_db": "dynamoDb",
        "ebs": "ebs",
        "ec2": "ec2",
        "elastic_search": "elasticSearch",
        "elb": "elb",
        "emr": "emr",
        "iam": "iam",
        "id": "id",
        "lambda_": "lambda",
        "rds": "rds",
        "red_shift": "redShift",
        "route53": "route53",
        "s3": "s3",
        "sns": "sns",
        "sqs": "sqs",
    },
)
class CloudAwsGovcloudIntegrationsConfig(cdktf.TerraformMetaArguments):
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
        alb: typing.Optional[typing.Union[CloudAwsGovcloudIntegrationsAlb, typing.Dict[str, typing.Any]]] = None,
        api_gateway: typing.Optional[typing.Union[CloudAwsGovcloudIntegrationsApiGateway, typing.Dict[str, typing.Any]]] = None,
        auto_scaling: typing.Optional[typing.Union[CloudAwsGovcloudIntegrationsAutoScaling, typing.Dict[str, typing.Any]]] = None,
        aws_direct_connect: typing.Optional[typing.Union[CloudAwsGovcloudIntegrationsAwsDirectConnect, typing.Dict[str, typing.Any]]] = None,
        aws_states: typing.Optional[typing.Union[CloudAwsGovcloudIntegrationsAwsStates, typing.Dict[str, typing.Any]]] = None,
        cloudtrail: typing.Optional[typing.Union[CloudAwsGovcloudIntegrationsCloudtrail, typing.Dict[str, typing.Any]]] = None,
        dynamo_db: typing.Optional[typing.Union["CloudAwsGovcloudIntegrationsDynamoDb", typing.Dict[str, typing.Any]]] = None,
        ebs: typing.Optional[typing.Union["CloudAwsGovcloudIntegrationsEbs", typing.Dict[str, typing.Any]]] = None,
        ec2: typing.Optional[typing.Union["CloudAwsGovcloudIntegrationsEc2", typing.Dict[str, typing.Any]]] = None,
        elastic_search: typing.Optional[typing.Union["CloudAwsGovcloudIntegrationsElasticSearch", typing.Dict[str, typing.Any]]] = None,
        elb: typing.Optional[typing.Union["CloudAwsGovcloudIntegrationsElb", typing.Dict[str, typing.Any]]] = None,
        emr: typing.Optional[typing.Union["CloudAwsGovcloudIntegrationsEmr", typing.Dict[str, typing.Any]]] = None,
        iam: typing.Optional[typing.Union["CloudAwsGovcloudIntegrationsIam", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        lambda_: typing.Optional[typing.Union["CloudAwsGovcloudIntegrationsLambda", typing.Dict[str, typing.Any]]] = None,
        rds: typing.Optional[typing.Union["CloudAwsGovcloudIntegrationsRds", typing.Dict[str, typing.Any]]] = None,
        red_shift: typing.Optional[typing.Union["CloudAwsGovcloudIntegrationsRedShift", typing.Dict[str, typing.Any]]] = None,
        route53: typing.Optional[typing.Union["CloudAwsGovcloudIntegrationsRoute53", typing.Dict[str, typing.Any]]] = None,
        s3: typing.Optional[typing.Union["CloudAwsGovcloudIntegrationsS3", typing.Dict[str, typing.Any]]] = None,
        sns: typing.Optional[typing.Union["CloudAwsGovcloudIntegrationsSns", typing.Dict[str, typing.Any]]] = None,
        sqs: typing.Optional[typing.Union["CloudAwsGovcloudIntegrationsSqs", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param linked_account_id: The ID of the linked AwsGovCloud account in New Relic. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#linked_account_id CloudAwsGovcloudIntegrations#linked_account_id}
        :param account_id: The ID of the account in New Relic. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#account_id CloudAwsGovcloudIntegrations#account_id}
        :param alb: alb block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#alb CloudAwsGovcloudIntegrations#alb}
        :param api_gateway: api_gateway block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#api_gateway CloudAwsGovcloudIntegrations#api_gateway}
        :param auto_scaling: auto_scaling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#auto_scaling CloudAwsGovcloudIntegrations#auto_scaling}
        :param aws_direct_connect: aws_direct_connect block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_direct_connect CloudAwsGovcloudIntegrations#aws_direct_connect}
        :param aws_states: aws_states block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_states CloudAwsGovcloudIntegrations#aws_states}
        :param cloudtrail: cloudtrail block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#cloudtrail CloudAwsGovcloudIntegrations#cloudtrail}
        :param dynamo_db: dynamo_db block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#dynamo_db CloudAwsGovcloudIntegrations#dynamo_db}
        :param ebs: ebs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#ebs CloudAwsGovcloudIntegrations#ebs}
        :param ec2: ec2 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#ec2 CloudAwsGovcloudIntegrations#ec2}
        :param elastic_search: elastic_search block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#elastic_search CloudAwsGovcloudIntegrations#elastic_search}
        :param elb: elb block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#elb CloudAwsGovcloudIntegrations#elb}
        :param emr: emr block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#emr CloudAwsGovcloudIntegrations#emr}
        :param iam: iam block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#iam CloudAwsGovcloudIntegrations#iam}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#id CloudAwsGovcloudIntegrations#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param lambda_: lambda block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#lambda CloudAwsGovcloudIntegrations#lambda}
        :param rds: rds block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#rds CloudAwsGovcloudIntegrations#rds}
        :param red_shift: red_shift block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#red_shift CloudAwsGovcloudIntegrations#red_shift}
        :param route53: route53 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#route53 CloudAwsGovcloudIntegrations#route53}
        :param s3: s3 block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#s3 CloudAwsGovcloudIntegrations#s3}
        :param sns: sns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#sns CloudAwsGovcloudIntegrations#sns}
        :param sqs: sqs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#sqs CloudAwsGovcloudIntegrations#sqs}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(alb, dict):
            alb = CloudAwsGovcloudIntegrationsAlb(**alb)
        if isinstance(api_gateway, dict):
            api_gateway = CloudAwsGovcloudIntegrationsApiGateway(**api_gateway)
        if isinstance(auto_scaling, dict):
            auto_scaling = CloudAwsGovcloudIntegrationsAutoScaling(**auto_scaling)
        if isinstance(aws_direct_connect, dict):
            aws_direct_connect = CloudAwsGovcloudIntegrationsAwsDirectConnect(**aws_direct_connect)
        if isinstance(aws_states, dict):
            aws_states = CloudAwsGovcloudIntegrationsAwsStates(**aws_states)
        if isinstance(cloudtrail, dict):
            cloudtrail = CloudAwsGovcloudIntegrationsCloudtrail(**cloudtrail)
        if isinstance(dynamo_db, dict):
            dynamo_db = CloudAwsGovcloudIntegrationsDynamoDb(**dynamo_db)
        if isinstance(ebs, dict):
            ebs = CloudAwsGovcloudIntegrationsEbs(**ebs)
        if isinstance(ec2, dict):
            ec2 = CloudAwsGovcloudIntegrationsEc2(**ec2)
        if isinstance(elastic_search, dict):
            elastic_search = CloudAwsGovcloudIntegrationsElasticSearch(**elastic_search)
        if isinstance(elb, dict):
            elb = CloudAwsGovcloudIntegrationsElb(**elb)
        if isinstance(emr, dict):
            emr = CloudAwsGovcloudIntegrationsEmr(**emr)
        if isinstance(iam, dict):
            iam = CloudAwsGovcloudIntegrationsIam(**iam)
        if isinstance(lambda_, dict):
            lambda_ = CloudAwsGovcloudIntegrationsLambda(**lambda_)
        if isinstance(rds, dict):
            rds = CloudAwsGovcloudIntegrationsRds(**rds)
        if isinstance(red_shift, dict):
            red_shift = CloudAwsGovcloudIntegrationsRedShift(**red_shift)
        if isinstance(route53, dict):
            route53 = CloudAwsGovcloudIntegrationsRoute53(**route53)
        if isinstance(s3, dict):
            s3 = CloudAwsGovcloudIntegrationsS3(**s3)
        if isinstance(sns, dict):
            sns = CloudAwsGovcloudIntegrationsSns(**sns)
        if isinstance(sqs, dict):
            sqs = CloudAwsGovcloudIntegrationsSqs(**sqs)
        if __debug__:
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument linked_account_id", value=linked_account_id, expected_type=type_hints["linked_account_id"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument alb", value=alb, expected_type=type_hints["alb"])
            check_type(argname="argument api_gateway", value=api_gateway, expected_type=type_hints["api_gateway"])
            check_type(argname="argument auto_scaling", value=auto_scaling, expected_type=type_hints["auto_scaling"])
            check_type(argname="argument aws_direct_connect", value=aws_direct_connect, expected_type=type_hints["aws_direct_connect"])
            check_type(argname="argument aws_states", value=aws_states, expected_type=type_hints["aws_states"])
            check_type(argname="argument cloudtrail", value=cloudtrail, expected_type=type_hints["cloudtrail"])
            check_type(argname="argument dynamo_db", value=dynamo_db, expected_type=type_hints["dynamo_db"])
            check_type(argname="argument ebs", value=ebs, expected_type=type_hints["ebs"])
            check_type(argname="argument ec2", value=ec2, expected_type=type_hints["ec2"])
            check_type(argname="argument elastic_search", value=elastic_search, expected_type=type_hints["elastic_search"])
            check_type(argname="argument elb", value=elb, expected_type=type_hints["elb"])
            check_type(argname="argument emr", value=emr, expected_type=type_hints["emr"])
            check_type(argname="argument iam", value=iam, expected_type=type_hints["iam"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument lambda_", value=lambda_, expected_type=type_hints["lambda_"])
            check_type(argname="argument rds", value=rds, expected_type=type_hints["rds"])
            check_type(argname="argument red_shift", value=red_shift, expected_type=type_hints["red_shift"])
            check_type(argname="argument route53", value=route53, expected_type=type_hints["route53"])
            check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
            check_type(argname="argument sns", value=sns, expected_type=type_hints["sns"])
            check_type(argname="argument sqs", value=sqs, expected_type=type_hints["sqs"])
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
        if alb is not None:
            self._values["alb"] = alb
        if api_gateway is not None:
            self._values["api_gateway"] = api_gateway
        if auto_scaling is not None:
            self._values["auto_scaling"] = auto_scaling
        if aws_direct_connect is not None:
            self._values["aws_direct_connect"] = aws_direct_connect
        if aws_states is not None:
            self._values["aws_states"] = aws_states
        if cloudtrail is not None:
            self._values["cloudtrail"] = cloudtrail
        if dynamo_db is not None:
            self._values["dynamo_db"] = dynamo_db
        if ebs is not None:
            self._values["ebs"] = ebs
        if ec2 is not None:
            self._values["ec2"] = ec2
        if elastic_search is not None:
            self._values["elastic_search"] = elastic_search
        if elb is not None:
            self._values["elb"] = elb
        if emr is not None:
            self._values["emr"] = emr
        if iam is not None:
            self._values["iam"] = iam
        if id is not None:
            self._values["id"] = id
        if lambda_ is not None:
            self._values["lambda_"] = lambda_
        if rds is not None:
            self._values["rds"] = rds
        if red_shift is not None:
            self._values["red_shift"] = red_shift
        if route53 is not None:
            self._values["route53"] = route53
        if s3 is not None:
            self._values["s3"] = s3
        if sns is not None:
            self._values["sns"] = sns
        if sqs is not None:
            self._values["sqs"] = sqs

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
        '''The ID of the linked AwsGovCloud account in New Relic.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#linked_account_id CloudAwsGovcloudIntegrations#linked_account_id}
        '''
        result = self._values.get("linked_account_id")
        assert result is not None, "Required property 'linked_account_id' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def account_id(self) -> typing.Optional[jsii.Number]:
        '''The ID of the account in New Relic.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#account_id CloudAwsGovcloudIntegrations#account_id}
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def alb(self) -> typing.Optional[CloudAwsGovcloudIntegrationsAlb]:
        '''alb block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#alb CloudAwsGovcloudIntegrations#alb}
        '''
        result = self._values.get("alb")
        return typing.cast(typing.Optional[CloudAwsGovcloudIntegrationsAlb], result)

    @builtins.property
    def api_gateway(self) -> typing.Optional[CloudAwsGovcloudIntegrationsApiGateway]:
        '''api_gateway block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#api_gateway CloudAwsGovcloudIntegrations#api_gateway}
        '''
        result = self._values.get("api_gateway")
        return typing.cast(typing.Optional[CloudAwsGovcloudIntegrationsApiGateway], result)

    @builtins.property
    def auto_scaling(self) -> typing.Optional[CloudAwsGovcloudIntegrationsAutoScaling]:
        '''auto_scaling block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#auto_scaling CloudAwsGovcloudIntegrations#auto_scaling}
        '''
        result = self._values.get("auto_scaling")
        return typing.cast(typing.Optional[CloudAwsGovcloudIntegrationsAutoScaling], result)

    @builtins.property
    def aws_direct_connect(
        self,
    ) -> typing.Optional[CloudAwsGovcloudIntegrationsAwsDirectConnect]:
        '''aws_direct_connect block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_direct_connect CloudAwsGovcloudIntegrations#aws_direct_connect}
        '''
        result = self._values.get("aws_direct_connect")
        return typing.cast(typing.Optional[CloudAwsGovcloudIntegrationsAwsDirectConnect], result)

    @builtins.property
    def aws_states(self) -> typing.Optional[CloudAwsGovcloudIntegrationsAwsStates]:
        '''aws_states block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_states CloudAwsGovcloudIntegrations#aws_states}
        '''
        result = self._values.get("aws_states")
        return typing.cast(typing.Optional[CloudAwsGovcloudIntegrationsAwsStates], result)

    @builtins.property
    def cloudtrail(self) -> typing.Optional[CloudAwsGovcloudIntegrationsCloudtrail]:
        '''cloudtrail block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#cloudtrail CloudAwsGovcloudIntegrations#cloudtrail}
        '''
        result = self._values.get("cloudtrail")
        return typing.cast(typing.Optional[CloudAwsGovcloudIntegrationsCloudtrail], result)

    @builtins.property
    def dynamo_db(self) -> typing.Optional["CloudAwsGovcloudIntegrationsDynamoDb"]:
        '''dynamo_db block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#dynamo_db CloudAwsGovcloudIntegrations#dynamo_db}
        '''
        result = self._values.get("dynamo_db")
        return typing.cast(typing.Optional["CloudAwsGovcloudIntegrationsDynamoDb"], result)

    @builtins.property
    def ebs(self) -> typing.Optional["CloudAwsGovcloudIntegrationsEbs"]:
        '''ebs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#ebs CloudAwsGovcloudIntegrations#ebs}
        '''
        result = self._values.get("ebs")
        return typing.cast(typing.Optional["CloudAwsGovcloudIntegrationsEbs"], result)

    @builtins.property
    def ec2(self) -> typing.Optional["CloudAwsGovcloudIntegrationsEc2"]:
        '''ec2 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#ec2 CloudAwsGovcloudIntegrations#ec2}
        '''
        result = self._values.get("ec2")
        return typing.cast(typing.Optional["CloudAwsGovcloudIntegrationsEc2"], result)

    @builtins.property
    def elastic_search(
        self,
    ) -> typing.Optional["CloudAwsGovcloudIntegrationsElasticSearch"]:
        '''elastic_search block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#elastic_search CloudAwsGovcloudIntegrations#elastic_search}
        '''
        result = self._values.get("elastic_search")
        return typing.cast(typing.Optional["CloudAwsGovcloudIntegrationsElasticSearch"], result)

    @builtins.property
    def elb(self) -> typing.Optional["CloudAwsGovcloudIntegrationsElb"]:
        '''elb block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#elb CloudAwsGovcloudIntegrations#elb}
        '''
        result = self._values.get("elb")
        return typing.cast(typing.Optional["CloudAwsGovcloudIntegrationsElb"], result)

    @builtins.property
    def emr(self) -> typing.Optional["CloudAwsGovcloudIntegrationsEmr"]:
        '''emr block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#emr CloudAwsGovcloudIntegrations#emr}
        '''
        result = self._values.get("emr")
        return typing.cast(typing.Optional["CloudAwsGovcloudIntegrationsEmr"], result)

    @builtins.property
    def iam(self) -> typing.Optional["CloudAwsGovcloudIntegrationsIam"]:
        '''iam block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#iam CloudAwsGovcloudIntegrations#iam}
        '''
        result = self._values.get("iam")
        return typing.cast(typing.Optional["CloudAwsGovcloudIntegrationsIam"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#id CloudAwsGovcloudIntegrations#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lambda_(self) -> typing.Optional["CloudAwsGovcloudIntegrationsLambda"]:
        '''lambda block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#lambda CloudAwsGovcloudIntegrations#lambda}
        '''
        result = self._values.get("lambda_")
        return typing.cast(typing.Optional["CloudAwsGovcloudIntegrationsLambda"], result)

    @builtins.property
    def rds(self) -> typing.Optional["CloudAwsGovcloudIntegrationsRds"]:
        '''rds block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#rds CloudAwsGovcloudIntegrations#rds}
        '''
        result = self._values.get("rds")
        return typing.cast(typing.Optional["CloudAwsGovcloudIntegrationsRds"], result)

    @builtins.property
    def red_shift(self) -> typing.Optional["CloudAwsGovcloudIntegrationsRedShift"]:
        '''red_shift block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#red_shift CloudAwsGovcloudIntegrations#red_shift}
        '''
        result = self._values.get("red_shift")
        return typing.cast(typing.Optional["CloudAwsGovcloudIntegrationsRedShift"], result)

    @builtins.property
    def route53(self) -> typing.Optional["CloudAwsGovcloudIntegrationsRoute53"]:
        '''route53 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#route53 CloudAwsGovcloudIntegrations#route53}
        '''
        result = self._values.get("route53")
        return typing.cast(typing.Optional["CloudAwsGovcloudIntegrationsRoute53"], result)

    @builtins.property
    def s3(self) -> typing.Optional["CloudAwsGovcloudIntegrationsS3"]:
        '''s3 block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#s3 CloudAwsGovcloudIntegrations#s3}
        '''
        result = self._values.get("s3")
        return typing.cast(typing.Optional["CloudAwsGovcloudIntegrationsS3"], result)

    @builtins.property
    def sns(self) -> typing.Optional["CloudAwsGovcloudIntegrationsSns"]:
        '''sns block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#sns CloudAwsGovcloudIntegrations#sns}
        '''
        result = self._values.get("sns")
        return typing.cast(typing.Optional["CloudAwsGovcloudIntegrationsSns"], result)

    @builtins.property
    def sqs(self) -> typing.Optional["CloudAwsGovcloudIntegrationsSqs"]:
        '''sqs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#sqs CloudAwsGovcloudIntegrations#sqs}
        '''
        result = self._values.get("sqs")
        return typing.cast(typing.Optional["CloudAwsGovcloudIntegrationsSqs"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsGovcloudIntegrationsConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsDynamoDb",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "fetch_extended_inventory": "fetchExtendedInventory",
        "fetch_tags": "fetchTags",
        "metrics_polling_interval": "metricsPollingInterval",
        "tag_key": "tagKey",
        "tag_value": "tagValue",
    },
)
class CloudAwsGovcloudIntegrationsDynamoDb:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        fetch_extended_inventory: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        fetch_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        :param fetch_extended_inventory: Determine if extra inventory data be collected or not. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_extended_inventory CloudAwsGovcloudIntegrations#fetch_extended_inventory}
        :param fetch_tags: Specify if tags should be collected. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_tags CloudAwsGovcloudIntegrations#fetch_tags}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsDynamoDb.__init__)
            check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            check_type(argname="argument fetch_extended_inventory", value=fetch_extended_inventory, expected_type=type_hints["fetch_extended_inventory"])
            check_type(argname="argument fetch_tags", value=fetch_tags, expected_type=type_hints["fetch_tags"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
            check_type(argname="argument tag_value", value=tag_value, expected_type=type_hints["tag_value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if aws_regions is not None:
            self._values["aws_regions"] = aws_regions
        if fetch_extended_inventory is not None:
            self._values["fetch_extended_inventory"] = fetch_extended_inventory
        if fetch_tags is not None:
            self._values["fetch_tags"] = fetch_tags
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if tag_key is not None:
            self._values["tag_key"] = tag_key
        if tag_value is not None:
            self._values["tag_value"] = tag_value

    @builtins.property
    def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each AWS region that includes the resources that you want to monitor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def fetch_extended_inventory(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Determine if extra inventory data be collected or not.

        May affect total data collection time and contribute to the Cloud provider API rate limit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_extended_inventory CloudAwsGovcloudIntegrations#fetch_extended_inventory}
        '''
        result = self._values.get("fetch_extended_inventory")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def fetch_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specify if tags should be collected.

        May affect total data collection time and contribute to the Cloud provider API rate limit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_tags CloudAwsGovcloudIntegrations#fetch_tags}
        '''
        result = self._values.get("fetch_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tag_key(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        '''
        result = self._values.get("tag_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_value(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        result = self._values.get("tag_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsGovcloudIntegrationsDynamoDb(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsGovcloudIntegrationsDynamoDbOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsDynamoDbOutputReference",
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
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsDynamoDbOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAwsRegions")
    def reset_aws_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegions", []))

    @jsii.member(jsii_name="resetFetchExtendedInventory")
    def reset_fetch_extended_inventory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchExtendedInventory", []))

    @jsii.member(jsii_name="resetFetchTags")
    def reset_fetch_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchTags", []))

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
    @jsii.member(jsii_name="fetchExtendedInventoryInput")
    def fetch_extended_inventory_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fetchExtendedInventoryInput"))

    @builtins.property
    @jsii.member(jsii_name="fetchTagsInput")
    def fetch_tags_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fetchTagsInput"))

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
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsDynamoDbOutputReference, "aws_regions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="fetchExtendedInventory")
    def fetch_extended_inventory(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "fetchExtendedInventory"))

    @fetch_extended_inventory.setter
    def fetch_extended_inventory(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsDynamoDbOutputReference, "fetch_extended_inventory").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchExtendedInventory", value)

    @builtins.property
    @jsii.member(jsii_name="fetchTags")
    def fetch_tags(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "fetchTags"))

    @fetch_tags.setter
    def fetch_tags(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsDynamoDbOutputReference, "fetch_tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchTags", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsDynamoDbOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="tagKey")
    def tag_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagKey"))

    @tag_key.setter
    def tag_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsDynamoDbOutputReference, "tag_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagKey", value)

    @builtins.property
    @jsii.member(jsii_name="tagValue")
    def tag_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagValue"))

    @tag_value.setter
    def tag_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsDynamoDbOutputReference, "tag_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsGovcloudIntegrationsDynamoDb]:
        return typing.cast(typing.Optional[CloudAwsGovcloudIntegrationsDynamoDb], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsGovcloudIntegrationsDynamoDb],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsDynamoDbOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsEbs",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "fetch_extended_inventory": "fetchExtendedInventory",
        "metrics_polling_interval": "metricsPollingInterval",
        "tag_key": "tagKey",
        "tag_value": "tagValue",
    },
)
class CloudAwsGovcloudIntegrationsEbs:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        fetch_extended_inventory: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        :param fetch_extended_inventory: Determine if extra inventory data be collected or not. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_extended_inventory CloudAwsGovcloudIntegrations#fetch_extended_inventory}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsEbs.__init__)
            check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            check_type(argname="argument fetch_extended_inventory", value=fetch_extended_inventory, expected_type=type_hints["fetch_extended_inventory"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
            check_type(argname="argument tag_value", value=tag_value, expected_type=type_hints["tag_value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if aws_regions is not None:
            self._values["aws_regions"] = aws_regions
        if fetch_extended_inventory is not None:
            self._values["fetch_extended_inventory"] = fetch_extended_inventory
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if tag_key is not None:
            self._values["tag_key"] = tag_key
        if tag_value is not None:
            self._values["tag_value"] = tag_value

    @builtins.property
    def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each AWS region that includes the resources that you want to monitor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def fetch_extended_inventory(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Determine if extra inventory data be collected or not.

        May affect total data collection time and contribute to the Cloud provider API rate limit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_extended_inventory CloudAwsGovcloudIntegrations#fetch_extended_inventory}
        '''
        result = self._values.get("fetch_extended_inventory")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tag_key(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        '''
        result = self._values.get("tag_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_value(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        result = self._values.get("tag_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsGovcloudIntegrationsEbs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsGovcloudIntegrationsEbsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsEbsOutputReference",
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
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsEbsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAwsRegions")
    def reset_aws_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegions", []))

    @jsii.member(jsii_name="resetFetchExtendedInventory")
    def reset_fetch_extended_inventory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchExtendedInventory", []))

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
    @jsii.member(jsii_name="fetchExtendedInventoryInput")
    def fetch_extended_inventory_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fetchExtendedInventoryInput"))

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
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsEbsOutputReference, "aws_regions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="fetchExtendedInventory")
    def fetch_extended_inventory(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "fetchExtendedInventory"))

    @fetch_extended_inventory.setter
    def fetch_extended_inventory(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsEbsOutputReference, "fetch_extended_inventory").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchExtendedInventory", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsEbsOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="tagKey")
    def tag_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagKey"))

    @tag_key.setter
    def tag_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsEbsOutputReference, "tag_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagKey", value)

    @builtins.property
    @jsii.member(jsii_name="tagValue")
    def tag_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagValue"))

    @tag_value.setter
    def tag_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsEbsOutputReference, "tag_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsGovcloudIntegrationsEbs]:
        return typing.cast(typing.Optional[CloudAwsGovcloudIntegrationsEbs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsGovcloudIntegrationsEbs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsEbsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsEc2",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "fetch_ip_addresses": "fetchIpAddresses",
        "metrics_polling_interval": "metricsPollingInterval",
        "tag_key": "tagKey",
        "tag_value": "tagValue",
    },
)
class CloudAwsGovcloudIntegrationsEc2:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        fetch_ip_addresses: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        :param fetch_ip_addresses: Specify if IP addresses of ec2 instance should be collected. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_ip_addresses CloudAwsGovcloudIntegrations#fetch_ip_addresses}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsEc2.__init__)
            check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            check_type(argname="argument fetch_ip_addresses", value=fetch_ip_addresses, expected_type=type_hints["fetch_ip_addresses"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
            check_type(argname="argument tag_value", value=tag_value, expected_type=type_hints["tag_value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if aws_regions is not None:
            self._values["aws_regions"] = aws_regions
        if fetch_ip_addresses is not None:
            self._values["fetch_ip_addresses"] = fetch_ip_addresses
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if tag_key is not None:
            self._values["tag_key"] = tag_key
        if tag_value is not None:
            self._values["tag_value"] = tag_value

    @builtins.property
    def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each AWS region that includes the resources that you want to monitor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def fetch_ip_addresses(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specify if IP addresses of ec2 instance should be collected.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_ip_addresses CloudAwsGovcloudIntegrations#fetch_ip_addresses}
        '''
        result = self._values.get("fetch_ip_addresses")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tag_key(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        '''
        result = self._values.get("tag_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_value(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        result = self._values.get("tag_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsGovcloudIntegrationsEc2(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsGovcloudIntegrationsEc2OutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsEc2OutputReference",
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
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsEc2OutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAwsRegions")
    def reset_aws_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegions", []))

    @jsii.member(jsii_name="resetFetchIpAddresses")
    def reset_fetch_ip_addresses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchIpAddresses", []))

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
    @jsii.member(jsii_name="fetchIpAddressesInput")
    def fetch_ip_addresses_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fetchIpAddressesInput"))

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
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsEc2OutputReference, "aws_regions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="fetchIpAddresses")
    def fetch_ip_addresses(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "fetchIpAddresses"))

    @fetch_ip_addresses.setter
    def fetch_ip_addresses(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsEc2OutputReference, "fetch_ip_addresses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchIpAddresses", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsEc2OutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="tagKey")
    def tag_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagKey"))

    @tag_key.setter
    def tag_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsEc2OutputReference, "tag_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagKey", value)

    @builtins.property
    @jsii.member(jsii_name="tagValue")
    def tag_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagValue"))

    @tag_value.setter
    def tag_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsEc2OutputReference, "tag_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsGovcloudIntegrationsEc2]:
        return typing.cast(typing.Optional[CloudAwsGovcloudIntegrationsEc2], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsGovcloudIntegrationsEc2],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsEc2OutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsElasticSearch",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "fetch_nodes": "fetchNodes",
        "metrics_polling_interval": "metricsPollingInterval",
        "tag_key": "tagKey",
        "tag_value": "tagValue",
    },
)
class CloudAwsGovcloudIntegrationsElasticSearch:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        fetch_nodes: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        :param fetch_nodes: Specify if IP addresses of ec2 instance should be collected. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_nodes CloudAwsGovcloudIntegrations#fetch_nodes}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsElasticSearch.__init__)
            check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            check_type(argname="argument fetch_nodes", value=fetch_nodes, expected_type=type_hints["fetch_nodes"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
            check_type(argname="argument tag_value", value=tag_value, expected_type=type_hints["tag_value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if aws_regions is not None:
            self._values["aws_regions"] = aws_regions
        if fetch_nodes is not None:
            self._values["fetch_nodes"] = fetch_nodes
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if tag_key is not None:
            self._values["tag_key"] = tag_key
        if tag_value is not None:
            self._values["tag_value"] = tag_value

    @builtins.property
    def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each AWS region that includes the resources that you want to monitor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def fetch_nodes(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specify if IP addresses of ec2 instance should be collected.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_nodes CloudAwsGovcloudIntegrations#fetch_nodes}
        '''
        result = self._values.get("fetch_nodes")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tag_key(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        '''
        result = self._values.get("tag_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_value(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        result = self._values.get("tag_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsGovcloudIntegrationsElasticSearch(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsGovcloudIntegrationsElasticSearchOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsElasticSearchOutputReference",
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
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsElasticSearchOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAwsRegions")
    def reset_aws_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegions", []))

    @jsii.member(jsii_name="resetFetchNodes")
    def reset_fetch_nodes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchNodes", []))

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
    @jsii.member(jsii_name="fetchNodesInput")
    def fetch_nodes_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fetchNodesInput"))

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
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsElasticSearchOutputReference, "aws_regions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="fetchNodes")
    def fetch_nodes(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "fetchNodes"))

    @fetch_nodes.setter
    def fetch_nodes(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsElasticSearchOutputReference, "fetch_nodes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchNodes", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsElasticSearchOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="tagKey")
    def tag_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagKey"))

    @tag_key.setter
    def tag_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsElasticSearchOutputReference, "tag_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagKey", value)

    @builtins.property
    @jsii.member(jsii_name="tagValue")
    def tag_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagValue"))

    @tag_value.setter
    def tag_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsElasticSearchOutputReference, "tag_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[CloudAwsGovcloudIntegrationsElasticSearch]:
        return typing.cast(typing.Optional[CloudAwsGovcloudIntegrationsElasticSearch], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsGovcloudIntegrationsElasticSearch],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsElasticSearchOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsElb",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "fetch_extended_inventory": "fetchExtendedInventory",
        "fetch_tags": "fetchTags",
        "metrics_polling_interval": "metricsPollingInterval",
    },
)
class CloudAwsGovcloudIntegrationsElb:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        fetch_extended_inventory: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        fetch_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        :param fetch_extended_inventory: Determine if extra inventory data be collected or not. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_extended_inventory CloudAwsGovcloudIntegrations#fetch_extended_inventory}
        :param fetch_tags: Specify if tags should be collected. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_tags CloudAwsGovcloudIntegrations#fetch_tags}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsElb.__init__)
            check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            check_type(argname="argument fetch_extended_inventory", value=fetch_extended_inventory, expected_type=type_hints["fetch_extended_inventory"])
            check_type(argname="argument fetch_tags", value=fetch_tags, expected_type=type_hints["fetch_tags"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if aws_regions is not None:
            self._values["aws_regions"] = aws_regions
        if fetch_extended_inventory is not None:
            self._values["fetch_extended_inventory"] = fetch_extended_inventory
        if fetch_tags is not None:
            self._values["fetch_tags"] = fetch_tags
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each AWS region that includes the resources that you want to monitor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def fetch_extended_inventory(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Determine if extra inventory data be collected or not.

        May affect total data collection time and contribute to the Cloud provider API rate limit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_extended_inventory CloudAwsGovcloudIntegrations#fetch_extended_inventory}
        '''
        result = self._values.get("fetch_extended_inventory")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def fetch_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specify if tags should be collected.

        May affect total data collection time and contribute to the Cloud provider API rate limit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_tags CloudAwsGovcloudIntegrations#fetch_tags}
        '''
        result = self._values.get("fetch_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsGovcloudIntegrationsElb(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsGovcloudIntegrationsElbOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsElbOutputReference",
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
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsElbOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAwsRegions")
    def reset_aws_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegions", []))

    @jsii.member(jsii_name="resetFetchExtendedInventory")
    def reset_fetch_extended_inventory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchExtendedInventory", []))

    @jsii.member(jsii_name="resetFetchTags")
    def reset_fetch_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchTags", []))

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="awsRegionsInput")
    def aws_regions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "awsRegionsInput"))

    @builtins.property
    @jsii.member(jsii_name="fetchExtendedInventoryInput")
    def fetch_extended_inventory_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fetchExtendedInventoryInput"))

    @builtins.property
    @jsii.member(jsii_name="fetchTagsInput")
    def fetch_tags_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fetchTagsInput"))

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
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsElbOutputReference, "aws_regions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="fetchExtendedInventory")
    def fetch_extended_inventory(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "fetchExtendedInventory"))

    @fetch_extended_inventory.setter
    def fetch_extended_inventory(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsElbOutputReference, "fetch_extended_inventory").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchExtendedInventory", value)

    @builtins.property
    @jsii.member(jsii_name="fetchTags")
    def fetch_tags(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "fetchTags"))

    @fetch_tags.setter
    def fetch_tags(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsElbOutputReference, "fetch_tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchTags", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsElbOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsGovcloudIntegrationsElb]:
        return typing.cast(typing.Optional[CloudAwsGovcloudIntegrationsElb], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsGovcloudIntegrationsElb],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsElbOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsEmr",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "fetch_tags": "fetchTags",
        "metrics_polling_interval": "metricsPollingInterval",
        "tag_key": "tagKey",
        "tag_value": "tagValue",
    },
)
class CloudAwsGovcloudIntegrationsEmr:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[builtins.str] = None,
        fetch_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        :param fetch_tags: Specify if tags should be collected. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_tags CloudAwsGovcloudIntegrations#fetch_tags}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsEmr.__init__)
            check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            check_type(argname="argument fetch_tags", value=fetch_tags, expected_type=type_hints["fetch_tags"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
            check_type(argname="argument tag_value", value=tag_value, expected_type=type_hints["tag_value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if aws_regions is not None:
            self._values["aws_regions"] = aws_regions
        if fetch_tags is not None:
            self._values["fetch_tags"] = fetch_tags
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if tag_key is not None:
            self._values["tag_key"] = tag_key
        if tag_value is not None:
            self._values["tag_value"] = tag_value

    @builtins.property
    def aws_regions(self) -> typing.Optional[builtins.str]:
        '''Specify each AWS region that includes the resources that you want to monitor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fetch_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specify if tags should be collected.

        May affect total data collection time and contribute to the Cloud provider API rate limit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_tags CloudAwsGovcloudIntegrations#fetch_tags}
        '''
        result = self._values.get("fetch_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tag_key(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        '''
        result = self._values.get("tag_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_value(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        result = self._values.get("tag_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsGovcloudIntegrationsEmr(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsGovcloudIntegrationsEmrOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsEmrOutputReference",
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
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsEmrOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAwsRegions")
    def reset_aws_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegions", []))

    @jsii.member(jsii_name="resetFetchTags")
    def reset_fetch_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchTags", []))

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
    def aws_regions_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "awsRegionsInput"))

    @builtins.property
    @jsii.member(jsii_name="fetchTagsInput")
    def fetch_tags_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fetchTagsInput"))

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
    def aws_regions(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "awsRegions"))

    @aws_regions.setter
    def aws_regions(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsEmrOutputReference, "aws_regions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="fetchTags")
    def fetch_tags(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "fetchTags"))

    @fetch_tags.setter
    def fetch_tags(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsEmrOutputReference, "fetch_tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchTags", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsEmrOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="tagKey")
    def tag_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagKey"))

    @tag_key.setter
    def tag_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsEmrOutputReference, "tag_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagKey", value)

    @builtins.property
    @jsii.member(jsii_name="tagValue")
    def tag_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagValue"))

    @tag_value.setter
    def tag_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsEmrOutputReference, "tag_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsGovcloudIntegrationsEmr]:
        return typing.cast(typing.Optional[CloudAwsGovcloudIntegrationsEmr], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsGovcloudIntegrationsEmr],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsEmrOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsIam",
    jsii_struct_bases=[],
    name_mapping={
        "metrics_polling_interval": "metricsPollingInterval",
        "tag_key": "tagKey",
        "tag_value": "tagValue",
    },
)
class CloudAwsGovcloudIntegrationsIam:
    def __init__(
        self,
        *,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsIam.__init__)
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
            check_type(argname="argument tag_value", value=tag_value, expected_type=type_hints["tag_value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if tag_key is not None:
            self._values["tag_key"] = tag_key
        if tag_value is not None:
            self._values["tag_value"] = tag_value

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tag_key(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        '''
        result = self._values.get("tag_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_value(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        result = self._values.get("tag_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsGovcloudIntegrationsIam(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsGovcloudIntegrationsIamOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsIamOutputReference",
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
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsIamOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsIamOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="tagKey")
    def tag_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagKey"))

    @tag_key.setter
    def tag_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsIamOutputReference, "tag_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagKey", value)

    @builtins.property
    @jsii.member(jsii_name="tagValue")
    def tag_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagValue"))

    @tag_value.setter
    def tag_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsIamOutputReference, "tag_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsGovcloudIntegrationsIam]:
        return typing.cast(typing.Optional[CloudAwsGovcloudIntegrationsIam], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsGovcloudIntegrationsIam],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsIamOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsLambda",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "fetch_tags": "fetchTags",
        "metrics_polling_interval": "metricsPollingInterval",
        "tag_key": "tagKey",
        "tag_value": "tagValue",
    },
)
class CloudAwsGovcloudIntegrationsLambda:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        fetch_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        :param fetch_tags: Specify if tags should be collected. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_tags CloudAwsGovcloudIntegrations#fetch_tags}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsLambda.__init__)
            check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            check_type(argname="argument fetch_tags", value=fetch_tags, expected_type=type_hints["fetch_tags"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
            check_type(argname="argument tag_value", value=tag_value, expected_type=type_hints["tag_value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if aws_regions is not None:
            self._values["aws_regions"] = aws_regions
        if fetch_tags is not None:
            self._values["fetch_tags"] = fetch_tags
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if tag_key is not None:
            self._values["tag_key"] = tag_key
        if tag_value is not None:
            self._values["tag_value"] = tag_value

    @builtins.property
    def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each AWS region that includes the resources that you want to monitor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def fetch_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specify if tags should be collected.

        May affect total data collection time and contribute to the Cloud provider API rate limit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_tags CloudAwsGovcloudIntegrations#fetch_tags}
        '''
        result = self._values.get("fetch_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tag_key(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        '''
        result = self._values.get("tag_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_value(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        result = self._values.get("tag_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsGovcloudIntegrationsLambda(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsGovcloudIntegrationsLambdaOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsLambdaOutputReference",
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
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsLambdaOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAwsRegions")
    def reset_aws_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegions", []))

    @jsii.member(jsii_name="resetFetchTags")
    def reset_fetch_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchTags", []))

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
    @jsii.member(jsii_name="fetchTagsInput")
    def fetch_tags_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fetchTagsInput"))

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
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsLambdaOutputReference, "aws_regions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="fetchTags")
    def fetch_tags(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "fetchTags"))

    @fetch_tags.setter
    def fetch_tags(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsLambdaOutputReference, "fetch_tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchTags", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsLambdaOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="tagKey")
    def tag_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagKey"))

    @tag_key.setter
    def tag_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsLambdaOutputReference, "tag_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagKey", value)

    @builtins.property
    @jsii.member(jsii_name="tagValue")
    def tag_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagValue"))

    @tag_value.setter
    def tag_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsLambdaOutputReference, "tag_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsGovcloudIntegrationsLambda]:
        return typing.cast(typing.Optional[CloudAwsGovcloudIntegrationsLambda], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsGovcloudIntegrationsLambda],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsLambdaOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsRds",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "fetch_tags": "fetchTags",
        "metrics_polling_interval": "metricsPollingInterval",
        "tag_key": "tagKey",
        "tag_value": "tagValue",
    },
)
class CloudAwsGovcloudIntegrationsRds:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        fetch_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        :param fetch_tags: Specify if tags should be collected. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_tags CloudAwsGovcloudIntegrations#fetch_tags}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsRds.__init__)
            check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            check_type(argname="argument fetch_tags", value=fetch_tags, expected_type=type_hints["fetch_tags"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
            check_type(argname="argument tag_value", value=tag_value, expected_type=type_hints["tag_value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if aws_regions is not None:
            self._values["aws_regions"] = aws_regions
        if fetch_tags is not None:
            self._values["fetch_tags"] = fetch_tags
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if tag_key is not None:
            self._values["tag_key"] = tag_key
        if tag_value is not None:
            self._values["tag_value"] = tag_value

    @builtins.property
    def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each AWS region that includes the resources that you want to monitor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def fetch_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specify if tags should be collected.

        May affect total data collection time and contribute to the Cloud provider API rate limit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_tags CloudAwsGovcloudIntegrations#fetch_tags}
        '''
        result = self._values.get("fetch_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tag_key(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        '''
        result = self._values.get("tag_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_value(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        result = self._values.get("tag_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsGovcloudIntegrationsRds(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsGovcloudIntegrationsRdsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsRdsOutputReference",
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
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsRdsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAwsRegions")
    def reset_aws_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegions", []))

    @jsii.member(jsii_name="resetFetchTags")
    def reset_fetch_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchTags", []))

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
    @jsii.member(jsii_name="fetchTagsInput")
    def fetch_tags_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fetchTagsInput"))

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
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsRdsOutputReference, "aws_regions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="fetchTags")
    def fetch_tags(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "fetchTags"))

    @fetch_tags.setter
    def fetch_tags(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsRdsOutputReference, "fetch_tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchTags", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsRdsOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="tagKey")
    def tag_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagKey"))

    @tag_key.setter
    def tag_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsRdsOutputReference, "tag_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagKey", value)

    @builtins.property
    @jsii.member(jsii_name="tagValue")
    def tag_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagValue"))

    @tag_value.setter
    def tag_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsRdsOutputReference, "tag_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsGovcloudIntegrationsRds]:
        return typing.cast(typing.Optional[CloudAwsGovcloudIntegrationsRds], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsGovcloudIntegrationsRds],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsRdsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsRedShift",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "metrics_polling_interval": "metricsPollingInterval",
        "tag_key": "tagKey",
        "tag_value": "tagValue",
    },
)
class CloudAwsGovcloudIntegrationsRedShift:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsRedShift.__init__)
            check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
            check_type(argname="argument tag_value", value=tag_value, expected_type=type_hints["tag_value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if aws_regions is not None:
            self._values["aws_regions"] = aws_regions
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if tag_key is not None:
            self._values["tag_key"] = tag_key
        if tag_value is not None:
            self._values["tag_value"] = tag_value

    @builtins.property
    def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each AWS region that includes the resources that you want to monitor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tag_key(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        '''
        result = self._values.get("tag_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_value(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        result = self._values.get("tag_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsGovcloudIntegrationsRedShift(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsGovcloudIntegrationsRedShiftOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsRedShiftOutputReference",
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
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsRedShiftOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAwsRegions")
    def reset_aws_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegions", []))

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
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsRedShiftOutputReference, "aws_regions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsRedShiftOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="tagKey")
    def tag_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagKey"))

    @tag_key.setter
    def tag_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsRedShiftOutputReference, "tag_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagKey", value)

    @builtins.property
    @jsii.member(jsii_name="tagValue")
    def tag_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagValue"))

    @tag_value.setter
    def tag_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsRedShiftOutputReference, "tag_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsGovcloudIntegrationsRedShift]:
        return typing.cast(typing.Optional[CloudAwsGovcloudIntegrationsRedShift], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsGovcloudIntegrationsRedShift],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsRedShiftOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsRoute53",
    jsii_struct_bases=[],
    name_mapping={
        "fetch_extended_inventory": "fetchExtendedInventory",
        "metrics_polling_interval": "metricsPollingInterval",
    },
)
class CloudAwsGovcloudIntegrationsRoute53:
    def __init__(
        self,
        *,
        fetch_extended_inventory: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param fetch_extended_inventory: Determine if extra inventory data be collected or not. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_extended_inventory CloudAwsGovcloudIntegrations#fetch_extended_inventory}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsRoute53.__init__)
            check_type(argname="argument fetch_extended_inventory", value=fetch_extended_inventory, expected_type=type_hints["fetch_extended_inventory"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if fetch_extended_inventory is not None:
            self._values["fetch_extended_inventory"] = fetch_extended_inventory
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def fetch_extended_inventory(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Determine if extra inventory data be collected or not.

        May affect total data collection time and contribute to the Cloud provider API rate limit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_extended_inventory CloudAwsGovcloudIntegrations#fetch_extended_inventory}
        '''
        result = self._values.get("fetch_extended_inventory")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsGovcloudIntegrationsRoute53(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsGovcloudIntegrationsRoute53OutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsRoute53OutputReference",
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
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsRoute53OutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFetchExtendedInventory")
    def reset_fetch_extended_inventory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchExtendedInventory", []))

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="fetchExtendedInventoryInput")
    def fetch_extended_inventory_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fetchExtendedInventoryInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="fetchExtendedInventory")
    def fetch_extended_inventory(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "fetchExtendedInventory"))

    @fetch_extended_inventory.setter
    def fetch_extended_inventory(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsRoute53OutputReference, "fetch_extended_inventory").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchExtendedInventory", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsRoute53OutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsGovcloudIntegrationsRoute53]:
        return typing.cast(typing.Optional[CloudAwsGovcloudIntegrationsRoute53], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsGovcloudIntegrationsRoute53],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsRoute53OutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsS3",
    jsii_struct_bases=[],
    name_mapping={
        "fetch_extended_inventory": "fetchExtendedInventory",
        "fetch_tags": "fetchTags",
        "metrics_polling_interval": "metricsPollingInterval",
        "tag_key": "tagKey",
        "tag_value": "tagValue",
    },
)
class CloudAwsGovcloudIntegrationsS3:
    def __init__(
        self,
        *,
        fetch_extended_inventory: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        fetch_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param fetch_extended_inventory: Determine if extra inventory data be collected or not. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_extended_inventory CloudAwsGovcloudIntegrations#fetch_extended_inventory}
        :param fetch_tags: Specify if tags should be collected. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_tags CloudAwsGovcloudIntegrations#fetch_tags}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsS3.__init__)
            check_type(argname="argument fetch_extended_inventory", value=fetch_extended_inventory, expected_type=type_hints["fetch_extended_inventory"])
            check_type(argname="argument fetch_tags", value=fetch_tags, expected_type=type_hints["fetch_tags"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
            check_type(argname="argument tag_value", value=tag_value, expected_type=type_hints["tag_value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if fetch_extended_inventory is not None:
            self._values["fetch_extended_inventory"] = fetch_extended_inventory
        if fetch_tags is not None:
            self._values["fetch_tags"] = fetch_tags
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if tag_key is not None:
            self._values["tag_key"] = tag_key
        if tag_value is not None:
            self._values["tag_value"] = tag_value

    @builtins.property
    def fetch_extended_inventory(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Determine if extra inventory data be collected or not.

        May affect total data collection time and contribute to the Cloud provider API rate limit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_extended_inventory CloudAwsGovcloudIntegrations#fetch_extended_inventory}
        '''
        result = self._values.get("fetch_extended_inventory")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def fetch_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specify if tags should be collected.

        May affect total data collection time and contribute to the Cloud provider API rate limit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_tags CloudAwsGovcloudIntegrations#fetch_tags}
        '''
        result = self._values.get("fetch_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tag_key(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        '''
        result = self._values.get("tag_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_value(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        result = self._values.get("tag_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsGovcloudIntegrationsS3(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsGovcloudIntegrationsS3OutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsS3OutputReference",
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
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsS3OutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFetchExtendedInventory")
    def reset_fetch_extended_inventory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchExtendedInventory", []))

    @jsii.member(jsii_name="resetFetchTags")
    def reset_fetch_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchTags", []))

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
    @jsii.member(jsii_name="fetchExtendedInventoryInput")
    def fetch_extended_inventory_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fetchExtendedInventoryInput"))

    @builtins.property
    @jsii.member(jsii_name="fetchTagsInput")
    def fetch_tags_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fetchTagsInput"))

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
    @jsii.member(jsii_name="fetchExtendedInventory")
    def fetch_extended_inventory(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "fetchExtendedInventory"))

    @fetch_extended_inventory.setter
    def fetch_extended_inventory(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsS3OutputReference, "fetch_extended_inventory").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchExtendedInventory", value)

    @builtins.property
    @jsii.member(jsii_name="fetchTags")
    def fetch_tags(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "fetchTags"))

    @fetch_tags.setter
    def fetch_tags(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsS3OutputReference, "fetch_tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchTags", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsS3OutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="tagKey")
    def tag_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagKey"))

    @tag_key.setter
    def tag_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsS3OutputReference, "tag_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagKey", value)

    @builtins.property
    @jsii.member(jsii_name="tagValue")
    def tag_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagValue"))

    @tag_value.setter
    def tag_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsS3OutputReference, "tag_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsGovcloudIntegrationsS3]:
        return typing.cast(typing.Optional[CloudAwsGovcloudIntegrationsS3], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsGovcloudIntegrationsS3],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsS3OutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsSns",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "fetch_extended_inventory": "fetchExtendedInventory",
        "metrics_polling_interval": "metricsPollingInterval",
    },
)
class CloudAwsGovcloudIntegrationsSns:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        fetch_extended_inventory: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        :param fetch_extended_inventory: Determine if extra inventory data be collected or not. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_extended_inventory CloudAwsGovcloudIntegrations#fetch_extended_inventory}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsSns.__init__)
            check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            check_type(argname="argument fetch_extended_inventory", value=fetch_extended_inventory, expected_type=type_hints["fetch_extended_inventory"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if aws_regions is not None:
            self._values["aws_regions"] = aws_regions
        if fetch_extended_inventory is not None:
            self._values["fetch_extended_inventory"] = fetch_extended_inventory
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval

    @builtins.property
    def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each AWS region that includes the resources that you want to monitor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def fetch_extended_inventory(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Determine if extra inventory data be collected or not.

        May affect total data collection time and contribute to the Cloud provider API rate limit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_extended_inventory CloudAwsGovcloudIntegrations#fetch_extended_inventory}
        '''
        result = self._values.get("fetch_extended_inventory")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsGovcloudIntegrationsSns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsGovcloudIntegrationsSnsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsSnsOutputReference",
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
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsSnsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAwsRegions")
    def reset_aws_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegions", []))

    @jsii.member(jsii_name="resetFetchExtendedInventory")
    def reset_fetch_extended_inventory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchExtendedInventory", []))

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @builtins.property
    @jsii.member(jsii_name="awsRegionsInput")
    def aws_regions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "awsRegionsInput"))

    @builtins.property
    @jsii.member(jsii_name="fetchExtendedInventoryInput")
    def fetch_extended_inventory_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fetchExtendedInventoryInput"))

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
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsSnsOutputReference, "aws_regions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="fetchExtendedInventory")
    def fetch_extended_inventory(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "fetchExtendedInventory"))

    @fetch_extended_inventory.setter
    def fetch_extended_inventory(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsSnsOutputReference, "fetch_extended_inventory").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchExtendedInventory", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsSnsOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsGovcloudIntegrationsSns]:
        return typing.cast(typing.Optional[CloudAwsGovcloudIntegrationsSns], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsGovcloudIntegrationsSns],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsSnsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsSqs",
    jsii_struct_bases=[],
    name_mapping={
        "aws_regions": "awsRegions",
        "fetch_extended_inventory": "fetchExtendedInventory",
        "fetch_tags": "fetchTags",
        "metrics_polling_interval": "metricsPollingInterval",
        "queue_prefixes": "queuePrefixes",
        "tag_key": "tagKey",
        "tag_value": "tagValue",
    },
)
class CloudAwsGovcloudIntegrationsSqs:
    def __init__(
        self,
        *,
        aws_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        fetch_extended_inventory: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        fetch_tags: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        metrics_polling_interval: typing.Optional[jsii.Number] = None,
        queue_prefixes: typing.Optional[typing.Sequence[builtins.str]] = None,
        tag_key: typing.Optional[builtins.str] = None,
        tag_value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param aws_regions: Specify each AWS region that includes the resources that you want to monitor. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        :param fetch_extended_inventory: Determine if extra inventory data be collected or not. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_extended_inventory CloudAwsGovcloudIntegrations#fetch_extended_inventory}
        :param fetch_tags: Specify if tags should be collected. May affect total data collection time and contribute to the Cloud provider API rate limit. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_tags CloudAwsGovcloudIntegrations#fetch_tags}
        :param metrics_polling_interval: The data polling interval in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        :param queue_prefixes: Specify each name or prefix for the Queues that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#queue_prefixes CloudAwsGovcloudIntegrations#queue_prefixes}
        :param tag_key: Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        :param tag_value: Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsSqs.__init__)
            check_type(argname="argument aws_regions", value=aws_regions, expected_type=type_hints["aws_regions"])
            check_type(argname="argument fetch_extended_inventory", value=fetch_extended_inventory, expected_type=type_hints["fetch_extended_inventory"])
            check_type(argname="argument fetch_tags", value=fetch_tags, expected_type=type_hints["fetch_tags"])
            check_type(argname="argument metrics_polling_interval", value=metrics_polling_interval, expected_type=type_hints["metrics_polling_interval"])
            check_type(argname="argument queue_prefixes", value=queue_prefixes, expected_type=type_hints["queue_prefixes"])
            check_type(argname="argument tag_key", value=tag_key, expected_type=type_hints["tag_key"])
            check_type(argname="argument tag_value", value=tag_value, expected_type=type_hints["tag_value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if aws_regions is not None:
            self._values["aws_regions"] = aws_regions
        if fetch_extended_inventory is not None:
            self._values["fetch_extended_inventory"] = fetch_extended_inventory
        if fetch_tags is not None:
            self._values["fetch_tags"] = fetch_tags
        if metrics_polling_interval is not None:
            self._values["metrics_polling_interval"] = metrics_polling_interval
        if queue_prefixes is not None:
            self._values["queue_prefixes"] = queue_prefixes
        if tag_key is not None:
            self._values["tag_key"] = tag_key
        if tag_value is not None:
            self._values["tag_value"] = tag_value

    @builtins.property
    def aws_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each AWS region that includes the resources that you want to monitor.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#aws_regions CloudAwsGovcloudIntegrations#aws_regions}
        '''
        result = self._values.get("aws_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def fetch_extended_inventory(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Determine if extra inventory data be collected or not.

        May affect total data collection time and contribute to the Cloud provider API rate limit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_extended_inventory CloudAwsGovcloudIntegrations#fetch_extended_inventory}
        '''
        result = self._values.get("fetch_extended_inventory")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def fetch_tags(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specify if tags should be collected.

        May affect total data collection time and contribute to the Cloud provider API rate limit.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#fetch_tags CloudAwsGovcloudIntegrations#fetch_tags}
        '''
        result = self._values.get("fetch_tags")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def metrics_polling_interval(self) -> typing.Optional[jsii.Number]:
        '''The data polling interval in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#metrics_polling_interval CloudAwsGovcloudIntegrations#metrics_polling_interval}
        '''
        result = self._values.get("metrics_polling_interval")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def queue_prefixes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specify each name or prefix for the Queues that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#queue_prefixes CloudAwsGovcloudIntegrations#queue_prefixes}
        '''
        result = self._values.get("queue_prefixes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tag_key(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag key associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_key CloudAwsGovcloudIntegrations#tag_key}
        '''
        result = self._values.get("tag_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag_value(self) -> typing.Optional[builtins.str]:
        '''Specify a Tag value associated with the resources that you want to monitor. Filter values are case-sensitive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/newrelic/r/cloud_aws_govcloud_integrations#tag_value CloudAwsGovcloudIntegrations#tag_value}
        '''
        result = self._values.get("tag_value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudAwsGovcloudIntegrationsSqs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CloudAwsGovcloudIntegrationsSqsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-newrelic.cloudAwsGovcloudIntegrations.CloudAwsGovcloudIntegrationsSqsOutputReference",
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
            type_hints = typing.get_type_hints(CloudAwsGovcloudIntegrationsSqsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAwsRegions")
    def reset_aws_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsRegions", []))

    @jsii.member(jsii_name="resetFetchExtendedInventory")
    def reset_fetch_extended_inventory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchExtendedInventory", []))

    @jsii.member(jsii_name="resetFetchTags")
    def reset_fetch_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFetchTags", []))

    @jsii.member(jsii_name="resetMetricsPollingInterval")
    def reset_metrics_polling_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetricsPollingInterval", []))

    @jsii.member(jsii_name="resetQueuePrefixes")
    def reset_queue_prefixes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueuePrefixes", []))

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
    @jsii.member(jsii_name="fetchExtendedInventoryInput")
    def fetch_extended_inventory_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fetchExtendedInventoryInput"))

    @builtins.property
    @jsii.member(jsii_name="fetchTagsInput")
    def fetch_tags_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "fetchTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="metricsPollingIntervalInput")
    def metrics_polling_interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "metricsPollingIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="queuePrefixesInput")
    def queue_prefixes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "queuePrefixesInput"))

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
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsSqsOutputReference, "aws_regions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "awsRegions", value)

    @builtins.property
    @jsii.member(jsii_name="fetchExtendedInventory")
    def fetch_extended_inventory(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "fetchExtendedInventory"))

    @fetch_extended_inventory.setter
    def fetch_extended_inventory(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsSqsOutputReference, "fetch_extended_inventory").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchExtendedInventory", value)

    @builtins.property
    @jsii.member(jsii_name="fetchTags")
    def fetch_tags(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "fetchTags"))

    @fetch_tags.setter
    def fetch_tags(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsSqsOutputReference, "fetch_tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fetchTags", value)

    @builtins.property
    @jsii.member(jsii_name="metricsPollingInterval")
    def metrics_polling_interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "metricsPollingInterval"))

    @metrics_polling_interval.setter
    def metrics_polling_interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsSqsOutputReference, "metrics_polling_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricsPollingInterval", value)

    @builtins.property
    @jsii.member(jsii_name="queuePrefixes")
    def queue_prefixes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "queuePrefixes"))

    @queue_prefixes.setter
    def queue_prefixes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsSqsOutputReference, "queue_prefixes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queuePrefixes", value)

    @builtins.property
    @jsii.member(jsii_name="tagKey")
    def tag_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagKey"))

    @tag_key.setter
    def tag_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsSqsOutputReference, "tag_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagKey", value)

    @builtins.property
    @jsii.member(jsii_name="tagValue")
    def tag_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tagValue"))

    @tag_value.setter
    def tag_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsSqsOutputReference, "tag_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagValue", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CloudAwsGovcloudIntegrationsSqs]:
        return typing.cast(typing.Optional[CloudAwsGovcloudIntegrationsSqs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[CloudAwsGovcloudIntegrationsSqs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CloudAwsGovcloudIntegrationsSqsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CloudAwsGovcloudIntegrations",
    "CloudAwsGovcloudIntegrationsAlb",
    "CloudAwsGovcloudIntegrationsAlbOutputReference",
    "CloudAwsGovcloudIntegrationsApiGateway",
    "CloudAwsGovcloudIntegrationsApiGatewayOutputReference",
    "CloudAwsGovcloudIntegrationsAutoScaling",
    "CloudAwsGovcloudIntegrationsAutoScalingOutputReference",
    "CloudAwsGovcloudIntegrationsAwsDirectConnect",
    "CloudAwsGovcloudIntegrationsAwsDirectConnectOutputReference",
    "CloudAwsGovcloudIntegrationsAwsStates",
    "CloudAwsGovcloudIntegrationsAwsStatesOutputReference",
    "CloudAwsGovcloudIntegrationsCloudtrail",
    "CloudAwsGovcloudIntegrationsCloudtrailOutputReference",
    "CloudAwsGovcloudIntegrationsConfig",
    "CloudAwsGovcloudIntegrationsDynamoDb",
    "CloudAwsGovcloudIntegrationsDynamoDbOutputReference",
    "CloudAwsGovcloudIntegrationsEbs",
    "CloudAwsGovcloudIntegrationsEbsOutputReference",
    "CloudAwsGovcloudIntegrationsEc2",
    "CloudAwsGovcloudIntegrationsEc2OutputReference",
    "CloudAwsGovcloudIntegrationsElasticSearch",
    "CloudAwsGovcloudIntegrationsElasticSearchOutputReference",
    "CloudAwsGovcloudIntegrationsElb",
    "CloudAwsGovcloudIntegrationsElbOutputReference",
    "CloudAwsGovcloudIntegrationsEmr",
    "CloudAwsGovcloudIntegrationsEmrOutputReference",
    "CloudAwsGovcloudIntegrationsIam",
    "CloudAwsGovcloudIntegrationsIamOutputReference",
    "CloudAwsGovcloudIntegrationsLambda",
    "CloudAwsGovcloudIntegrationsLambdaOutputReference",
    "CloudAwsGovcloudIntegrationsRds",
    "CloudAwsGovcloudIntegrationsRdsOutputReference",
    "CloudAwsGovcloudIntegrationsRedShift",
    "CloudAwsGovcloudIntegrationsRedShiftOutputReference",
    "CloudAwsGovcloudIntegrationsRoute53",
    "CloudAwsGovcloudIntegrationsRoute53OutputReference",
    "CloudAwsGovcloudIntegrationsS3",
    "CloudAwsGovcloudIntegrationsS3OutputReference",
    "CloudAwsGovcloudIntegrationsSns",
    "CloudAwsGovcloudIntegrationsSnsOutputReference",
    "CloudAwsGovcloudIntegrationsSqs",
    "CloudAwsGovcloudIntegrationsSqsOutputReference",
]

publication.publish()
