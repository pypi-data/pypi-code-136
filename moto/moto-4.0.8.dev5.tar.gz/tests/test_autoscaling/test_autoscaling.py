import boto3
import sure  # noqa # pylint: disable=unused-import
import pytest

from botocore.exceptions import ClientError
from moto import mock_autoscaling, mock_ec2
from moto.core import DEFAULT_ACCOUNT_ID as ACCOUNT_ID
from tests import EXAMPLE_AMI_ID
from .utils import setup_networking, setup_instance_with_networking


@mock_autoscaling
@mock_ec2
def test_propogate_tags():
    mocked_networking = setup_networking()
    conn = boto3.client("autoscaling", region_name="us-east-1")
    conn.create_launch_configuration(
        LaunchConfigurationName="TestLC",
        ImageId=EXAMPLE_AMI_ID,
        InstanceType="t2.medium",
    )

    conn.create_auto_scaling_group(
        AutoScalingGroupName="TestGroup1",
        MinSize=1,
        MaxSize=2,
        LaunchConfigurationName="TestLC",
        Tags=[
            {
                "ResourceId": "TestGroup1",
                "ResourceType": "auto-scaling-group",
                "PropagateAtLaunch": True,
                "Key": "TestTagKey1",
                "Value": "TestTagValue1",
            }
        ],
        VPCZoneIdentifier=mocked_networking["subnet1"],
    )

    ec2 = boto3.client("ec2", region_name="us-east-1")
    instances = ec2.describe_instances()

    tags = instances["Reservations"][0]["Instances"][0]["Tags"]
    tags.should.contain({"Value": "TestTagValue1", "Key": "TestTagKey1"})
    tags.should.contain({"Value": "TestGroup1", "Key": "aws:autoscaling:groupName"})


@mock_autoscaling
def test_create_autoscaling_group_from_instance():
    autoscaling_group_name = "test_asg"
    image_id = EXAMPLE_AMI_ID
    instance_type = "t2.micro"

    mocked_instance_with_networking = setup_instance_with_networking(
        image_id, instance_type
    )
    client = boto3.client("autoscaling", region_name="us-east-1")
    response = client.create_auto_scaling_group(
        AutoScalingGroupName=autoscaling_group_name,
        InstanceId=mocked_instance_with_networking["instance"],
        MinSize=1,
        MaxSize=3,
        DesiredCapacity=2,
        VPCZoneIdentifier=mocked_instance_with_networking["subnet1"],
        NewInstancesProtectedFromScaleIn=False,
    )
    response["ResponseMetadata"]["HTTPStatusCode"].should.equal(200)

    describe_launch_configurations_response = client.describe_launch_configurations()
    describe_launch_configurations_response[
        "LaunchConfigurations"
    ].should.have.length_of(1)
    launch_configuration_from_instance = describe_launch_configurations_response[
        "LaunchConfigurations"
    ][0]
    launch_configuration_from_instance["LaunchConfigurationName"].should.equal(
        "test_asg"
    )
    launch_configuration_from_instance["ImageId"].should.equal(image_id)
    launch_configuration_from_instance["InstanceType"].should.equal(instance_type)


@mock_autoscaling
def test_create_autoscaling_group_from_invalid_instance_id():
    invalid_instance_id = "invalid_instance"

    mocked_networking = setup_networking()
    client = boto3.client("autoscaling", region_name="us-east-1")
    with pytest.raises(ClientError) as ex:
        client.create_auto_scaling_group(
            AutoScalingGroupName="test_asg",
            InstanceId=invalid_instance_id,
            MinSize=9,
            MaxSize=15,
            DesiredCapacity=12,
            VPCZoneIdentifier=mocked_networking["subnet1"],
            NewInstancesProtectedFromScaleIn=False,
        )
    ex.value.response["ResponseMetadata"]["HTTPStatusCode"].should.equal(400)
    ex.value.response["Error"]["Code"].should.equal("ValidationError")
    ex.value.response["Error"]["Message"].should.equal(
        "Instance [{0}] is invalid.".format(invalid_instance_id)
    )


@mock_autoscaling
@mock_ec2
def test_create_autoscaling_group_from_template():
    mocked_networking = setup_networking()

    ec2_client = boto3.client("ec2", region_name="us-east-1")
    template = ec2_client.create_launch_template(
        LaunchTemplateName="test_launch_template",
        LaunchTemplateData={"ImageId": EXAMPLE_AMI_ID, "InstanceType": "t2.micro"},
    )["LaunchTemplate"]
    client = boto3.client("autoscaling", region_name="us-east-1")
    response = client.create_auto_scaling_group(
        AutoScalingGroupName="test_asg",
        LaunchTemplate={
            "LaunchTemplateId": template["LaunchTemplateId"],
            "Version": str(template["LatestVersionNumber"]),
        },
        MinSize=1,
        MaxSize=3,
        DesiredCapacity=2,
        VPCZoneIdentifier=mocked_networking["subnet1"],
        NewInstancesProtectedFromScaleIn=False,
    )
    response["ResponseMetadata"]["HTTPStatusCode"].should.equal(200)


@mock_ec2
@mock_autoscaling
def test_create_auto_scaling_from_template_version__latest():
    ec2_client = boto3.client("ec2", region_name="us-west-1")
    launch_template_name = "tester"
    ec2_client.create_launch_template(
        LaunchTemplateName=launch_template_name,
        LaunchTemplateData={"ImageId": EXAMPLE_AMI_ID, "InstanceType": "t2.medium"},
    )
    asg_client = boto3.client("autoscaling", region_name="us-west-1")
    asg_client.create_auto_scaling_group(
        AutoScalingGroupName="name",
        DesiredCapacity=1,
        MinSize=1,
        MaxSize=1,
        LaunchTemplate={
            "LaunchTemplateName": launch_template_name,
            "Version": "$Latest",
        },
        AvailabilityZones=["us-west-1a"],
    )

    response = asg_client.describe_auto_scaling_groups(AutoScalingGroupNames=["name"])[
        "AutoScalingGroups"
    ][0]
    response.should.have.key("LaunchTemplate")
    response["LaunchTemplate"].should.have.key("LaunchTemplateName").equals(
        launch_template_name
    )
    response["LaunchTemplate"].should.have.key("Version").equals("$Latest")


@mock_ec2
@mock_autoscaling
def test_create_auto_scaling_from_template_version__default():
    ec2_client = boto3.client("ec2", region_name="us-west-1")
    launch_template_name = "tester"
    ec2_client.create_launch_template(
        LaunchTemplateName=launch_template_name,
        LaunchTemplateData={"ImageId": EXAMPLE_AMI_ID, "InstanceType": "t2.medium"},
    )
    ec2_client.create_launch_template_version(
        LaunchTemplateName=launch_template_name,
        LaunchTemplateData={"ImageId": EXAMPLE_AMI_ID, "InstanceType": "t3.medium"},
        VersionDescription="v2",
    )
    asg_client = boto3.client("autoscaling", region_name="us-west-1")
    asg_client.create_auto_scaling_group(
        AutoScalingGroupName="name",
        DesiredCapacity=1,
        MinSize=1,
        MaxSize=1,
        LaunchTemplate={
            "LaunchTemplateName": launch_template_name,
            "Version": "$Default",
        },
        AvailabilityZones=["us-west-1a"],
    )

    response = asg_client.describe_auto_scaling_groups(AutoScalingGroupNames=["name"])[
        "AutoScalingGroups"
    ][0]
    response.should.have.key("LaunchTemplate")
    response["LaunchTemplate"].should.have.key("LaunchTemplateName").equals(
        launch_template_name
    )
    response["LaunchTemplate"].should.have.key("Version").equals("$Default")


@mock_ec2
@mock_autoscaling
def test_create_auto_scaling_from_template_version__no_version():
    ec2_client = boto3.client("ec2", region_name="us-west-1")
    launch_template_name = "tester"
    ec2_client.create_launch_template(
        LaunchTemplateName=launch_template_name,
        LaunchTemplateData={"ImageId": EXAMPLE_AMI_ID, "InstanceType": "t2.medium"},
    )
    asg_client = boto3.client("autoscaling", region_name="us-west-1")
    asg_client.create_auto_scaling_group(
        AutoScalingGroupName="name",
        DesiredCapacity=1,
        MinSize=1,
        MaxSize=1,
        LaunchTemplate={"LaunchTemplateName": launch_template_name},
        AvailabilityZones=["us-west-1a"],
    )

    response = asg_client.describe_auto_scaling_groups(AutoScalingGroupNames=["name"])[
        "AutoScalingGroups"
    ][0]
    response.should.have.key("LaunchTemplate")
    # We never specified the version - this is what it defaults to
    response["LaunchTemplate"].should.have.key("Version").equals("$Default")


@mock_autoscaling
@mock_ec2
def test_create_autoscaling_group_no_template_ref():
    mocked_networking = setup_networking()

    ec2_client = boto3.client("ec2", region_name="us-east-1")
    template = ec2_client.create_launch_template(
        LaunchTemplateName="test_launch_template",
        LaunchTemplateData={"ImageId": EXAMPLE_AMI_ID, "InstanceType": "t2.micro"},
    )["LaunchTemplate"]
    client = boto3.client("autoscaling", region_name="us-east-1")

    with pytest.raises(ClientError) as ex:
        client.create_auto_scaling_group(
            AutoScalingGroupName="test_asg",
            LaunchTemplate={"Version": str(template["LatestVersionNumber"])},
            MinSize=0,
            MaxSize=20,
            DesiredCapacity=5,
            VPCZoneIdentifier=mocked_networking["subnet1"],
            NewInstancesProtectedFromScaleIn=False,
        )
    ex.value.response["ResponseMetadata"]["HTTPStatusCode"].should.equal(400)
    ex.value.response["Error"]["Code"].should.equal("ValidationError")
    ex.value.response["Error"]["Message"].should.equal(
        "Valid requests must contain either launchTemplateId or LaunchTemplateName"
    )


@mock_autoscaling
@mock_ec2
def test_create_autoscaling_group_multiple_template_ref():
    mocked_networking = setup_networking()

    ec2_client = boto3.client("ec2", region_name="us-east-1")
    template = ec2_client.create_launch_template(
        LaunchTemplateName="test_launch_template",
        LaunchTemplateData={"ImageId": EXAMPLE_AMI_ID, "InstanceType": "t2.micro"},
    )["LaunchTemplate"]
    client = boto3.client("autoscaling", region_name="us-east-1")

    with pytest.raises(ClientError) as ex:
        client.create_auto_scaling_group(
            AutoScalingGroupName="test_asg",
            LaunchTemplate={
                "LaunchTemplateId": template["LaunchTemplateId"],
                "LaunchTemplateName": template["LaunchTemplateName"],
                "Version": str(template["LatestVersionNumber"]),
            },
            MinSize=0,
            MaxSize=20,
            DesiredCapacity=5,
            VPCZoneIdentifier=mocked_networking["subnet1"],
            NewInstancesProtectedFromScaleIn=False,
        )
    ex.value.response["ResponseMetadata"]["HTTPStatusCode"].should.equal(400)
    ex.value.response["Error"]["Code"].should.equal("ValidationError")
    ex.value.response["Error"]["Message"].should.equal(
        "Valid requests must contain either launchTemplateId or LaunchTemplateName"
    )


@mock_autoscaling
def test_create_autoscaling_group_no_launch_configuration():
    mocked_networking = setup_networking()
    client = boto3.client("autoscaling", region_name="us-east-1")
    with pytest.raises(ClientError) as ex:
        client.create_auto_scaling_group(
            AutoScalingGroupName="test_asg",
            MinSize=0,
            MaxSize=20,
            DesiredCapacity=5,
            VPCZoneIdentifier=mocked_networking["subnet1"],
            NewInstancesProtectedFromScaleIn=False,
        )
    ex.value.response["ResponseMetadata"]["HTTPStatusCode"].should.equal(400)
    ex.value.response["Error"]["Code"].should.equal("ValidationError")
    ex.value.response["Error"]["Message"].should.equal(
        "Valid requests must contain either LaunchTemplate, LaunchConfigurationName, "
        "InstanceId or MixedInstancesPolicy parameter."
    )


@mock_autoscaling
@mock_ec2
def test_create_autoscaling_group_multiple_launch_configurations():
    mocked_networking = setup_networking()

    ec2_client = boto3.client("ec2", region_name="us-east-1")
    template = ec2_client.create_launch_template(
        LaunchTemplateName="test_launch_template",
        LaunchTemplateData={"ImageId": EXAMPLE_AMI_ID, "InstanceType": "t2.micro"},
    )["LaunchTemplate"]
    client = boto3.client("autoscaling", region_name="us-east-1")
    client.create_launch_configuration(
        LaunchConfigurationName="test_launch_configuration",
        ImageId=EXAMPLE_AMI_ID,
        InstanceType="t2.medium",
    )

    with pytest.raises(ClientError) as ex:
        client.create_auto_scaling_group(
            AutoScalingGroupName="test_asg",
            LaunchConfigurationName="test_launch_configuration",
            LaunchTemplate={
                "LaunchTemplateId": template["LaunchTemplateId"],
                "Version": str(template["LatestVersionNumber"]),
            },
            MinSize=0,
            MaxSize=20,
            DesiredCapacity=5,
            VPCZoneIdentifier=mocked_networking["subnet1"],
            NewInstancesProtectedFromScaleIn=False,
        )
    ex.value.response["ResponseMetadata"]["HTTPStatusCode"].should.equal(400)
    ex.value.response["Error"]["Code"].should.equal("ValidationError")
    ex.value.response["Error"]["Message"].should.equal(
        "Valid requests must contain either LaunchTemplate, LaunchConfigurationName, "
        "InstanceId or MixedInstancesPolicy parameter."
    )


@mock_autoscaling
@mock_ec2
def test_describe_autoscaling_groups_launch_template():
    mocked_networking = setup_networking()
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    template = ec2_client.create_launch_template(
        LaunchTemplateName="test_launch_template",
        LaunchTemplateData={"ImageId": EXAMPLE_AMI_ID, "InstanceType": "t2.micro"},
    )["LaunchTemplate"]
    client = boto3.client("autoscaling", region_name="us-east-1")
    client.create_auto_scaling_group(
        AutoScalingGroupName="test_asg",
        LaunchTemplate={"LaunchTemplateName": "test_launch_template", "Version": "1"},
        MinSize=0,
        MaxSize=20,
        DesiredCapacity=5,
        VPCZoneIdentifier=mocked_networking["subnet1"],
        NewInstancesProtectedFromScaleIn=True,
    )
    expected_launch_template = {
        "LaunchTemplateId": template["LaunchTemplateId"],
        "LaunchTemplateName": "test_launch_template",
        "Version": "1",
    }

    response = client.describe_auto_scaling_groups(AutoScalingGroupNames=["test_asg"])
    response["ResponseMetadata"]["HTTPStatusCode"].should.equal(200)
    group = response["AutoScalingGroups"][0]
    group["AutoScalingGroupName"].should.equal("test_asg")
    group["LaunchTemplate"].should.equal(expected_launch_template)
    group.should_not.have.key("LaunchConfigurationName")
    group["AvailabilityZones"].should.equal(["us-east-1a"])
    group["VPCZoneIdentifier"].should.equal(mocked_networking["subnet1"])
    group["NewInstancesProtectedFromScaleIn"].should.equal(True)
    for instance in group["Instances"]:
        instance["LaunchTemplate"].should.equal(expected_launch_template)
        instance.should_not.have.key("LaunchConfigurationName")
        instance["AvailabilityZone"].should.equal("us-east-1a")
        instance["ProtectedFromScaleIn"].should.equal(True)
        instance["InstanceType"].should.equal("t2.micro")


@mock_autoscaling
def test_describe_autoscaling_instances_launch_config():
    mocked_networking = setup_networking()
    client = boto3.client("autoscaling", region_name="us-east-1")
    client.create_launch_configuration(
        LaunchConfigurationName="test_launch_configuration",
        InstanceType="t2.micro",
        ImageId=EXAMPLE_AMI_ID,
    )
    client.create_auto_scaling_group(
        AutoScalingGroupName="test_asg",
        LaunchConfigurationName="test_launch_configuration",
        MinSize=0,
        MaxSize=20,
        DesiredCapacity=5,
        VPCZoneIdentifier=mocked_networking["subnet1"],
        NewInstancesProtectedFromScaleIn=True,
    )

    response = client.describe_auto_scaling_instances()
    len(response["AutoScalingInstances"]).should.equal(5)
    for instance in response["AutoScalingInstances"]:
        instance["LaunchConfigurationName"].should.equal("test_launch_configuration")
        instance.should_not.have.key("LaunchTemplate")
        instance["AutoScalingGroupName"].should.equal("test_asg")
        instance["AvailabilityZone"].should.equal("us-east-1a")
        instance["ProtectedFromScaleIn"].should.equal(True)
        instance["InstanceType"].should.equal("t2.micro")


@mock_autoscaling
@mock_ec2
def test_describe_autoscaling_instances_launch_template():
    mocked_networking = setup_networking()
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    template = ec2_client.create_launch_template(
        LaunchTemplateName="test_launch_template",
        LaunchTemplateData={"ImageId": EXAMPLE_AMI_ID, "InstanceType": "t2.micro"},
    )["LaunchTemplate"]
    client = boto3.client("autoscaling", region_name="us-east-1")
    client.create_auto_scaling_group(
        AutoScalingGroupName="test_asg",
        LaunchTemplate={"LaunchTemplateName": "test_launch_template", "Version": "1"},
        MinSize=0,
        MaxSize=20,
        DesiredCapacity=5,
        VPCZoneIdentifier=mocked_networking["subnet1"],
        NewInstancesProtectedFromScaleIn=True,
    )
    expected_launch_template = {
        "LaunchTemplateId": template["LaunchTemplateId"],
        "LaunchTemplateName": "test_launch_template",
        "Version": "1",
    }

    response = client.describe_auto_scaling_instances()
    len(response["AutoScalingInstances"]).should.equal(5)
    for instance in response["AutoScalingInstances"]:
        instance["LaunchTemplate"].should.equal(expected_launch_template)
        instance.should_not.have.key("LaunchConfigurationName")
        instance["AutoScalingGroupName"].should.equal("test_asg")
        instance["AvailabilityZone"].should.equal("us-east-1a")
        instance["ProtectedFromScaleIn"].should.equal(True)
        instance["InstanceType"].should.equal("t2.micro")


@mock_autoscaling
def test_describe_autoscaling_instances_instanceid_filter():
    mocked_networking = setup_networking()
    client = boto3.client("autoscaling", region_name="us-east-1")
    _ = client.create_launch_configuration(
        LaunchConfigurationName="test_launch_configuration",
        ImageId=EXAMPLE_AMI_ID,
        InstanceType="t2.medium",
    )
    _ = client.create_auto_scaling_group(
        AutoScalingGroupName="test_asg",
        LaunchConfigurationName="test_launch_configuration",
        MinSize=0,
        MaxSize=20,
        DesiredCapacity=5,
        VPCZoneIdentifier=mocked_networking["subnet1"],
        NewInstancesProtectedFromScaleIn=True,
    )

    response = client.describe_auto_scaling_groups(AutoScalingGroupNames=["test_asg"])
    instance_ids = [
        instance["InstanceId"]
        for instance in response["AutoScalingGroups"][0]["Instances"]
    ]

    response = client.describe_auto_scaling_instances(
        InstanceIds=instance_ids[0:2]
    )  # Filter by first 2 of 5
    len(response["AutoScalingInstances"]).should.equal(2)
    for instance in response["AutoScalingInstances"]:
        instance["AutoScalingGroupName"].should.equal("test_asg")
        instance["AvailabilityZone"].should.equal("us-east-1a")
        instance["ProtectedFromScaleIn"].should.equal(True)


@mock_autoscaling
def test_update_autoscaling_group_launch_config():
    mocked_networking = setup_networking()
    client = boto3.client("autoscaling", region_name="us-east-1")
    client.create_launch_configuration(
        LaunchConfigurationName="test_launch_configuration",
        ImageId=EXAMPLE_AMI_ID,
        InstanceType="t2.medium",
    )
    client.create_launch_configuration(
        LaunchConfigurationName="test_launch_configuration_new",
        ImageId=EXAMPLE_AMI_ID,
        InstanceType="t2.medium",
    )
    client.create_auto_scaling_group(
        AutoScalingGroupName="test_asg",
        LaunchConfigurationName="test_launch_configuration",
        MinSize=0,
        MaxSize=20,
        DesiredCapacity=5,
        VPCZoneIdentifier=mocked_networking["subnet1"],
        NewInstancesProtectedFromScaleIn=True,
    )

    client.update_auto_scaling_group(
        AutoScalingGroupName="test_asg",
        LaunchConfigurationName="test_launch_configuration_new",
        MinSize=1,
        VPCZoneIdentifier="{subnet1},{subnet2}".format(
            subnet1=mocked_networking["subnet1"], subnet2=mocked_networking["subnet2"]
        ),
        NewInstancesProtectedFromScaleIn=False,
    )

    response = client.describe_auto_scaling_groups(AutoScalingGroupNames=["test_asg"])
    group = response["AutoScalingGroups"][0]
    group["LaunchConfigurationName"].should.equal("test_launch_configuration_new")
    group["MinSize"].should.equal(1)
    set(group["AvailabilityZones"]).should.equal({"us-east-1a", "us-east-1b"})
    group["NewInstancesProtectedFromScaleIn"].should.equal(False)


@mock_autoscaling
@mock_ec2
def test_update_autoscaling_group_launch_template():
    mocked_networking = setup_networking()
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    ec2_client.create_launch_template(
        LaunchTemplateName="test_launch_template",
        LaunchTemplateData={"ImageId": EXAMPLE_AMI_ID, "InstanceType": "t2.micro"},
    )
    template = ec2_client.create_launch_template(
        LaunchTemplateName="test_launch_template_new",
        LaunchTemplateData={
            "ImageId": "ami-1ea5b10a3d8867db4",
            "InstanceType": "t2.micro",
        },
    )["LaunchTemplate"]
    client = boto3.client("autoscaling", region_name="us-east-1")
    client.create_auto_scaling_group(
        AutoScalingGroupName="test_asg",
        LaunchTemplate={"LaunchTemplateName": "test_launch_template", "Version": "1"},
        MinSize=0,
        MaxSize=20,
        DesiredCapacity=5,
        VPCZoneIdentifier=mocked_networking["subnet1"],
        NewInstancesProtectedFromScaleIn=True,
    )

    client.update_auto_scaling_group(
        AutoScalingGroupName="test_asg",
        LaunchTemplate={
            "LaunchTemplateName": "test_launch_template_new",
            "Version": "1",
        },
        MinSize=1,
        VPCZoneIdentifier="{subnet1},{subnet2}".format(
            subnet1=mocked_networking["subnet1"], subnet2=mocked_networking["subnet2"]
        ),
        NewInstancesProtectedFromScaleIn=False,
    )

    expected_launch_template = {
        "LaunchTemplateId": template["LaunchTemplateId"],
        "LaunchTemplateName": "test_launch_template_new",
        "Version": "1",
    }

    response = client.describe_auto_scaling_groups(AutoScalingGroupNames=["test_asg"])
    group = response["AutoScalingGroups"][0]
    group["LaunchTemplate"].should.equal(expected_launch_template)
    group["MinSize"].should.equal(1)
    set(group["AvailabilityZones"]).should.equal({"us-east-1a", "us-east-1b"})
    group["NewInstancesProtectedFromScaleIn"].should.equal(False)


@mock_autoscaling
def test_update_autoscaling_group_min_size_desired_capacity_change():
    mocked_networking = setup_networking()
    client = boto3.client("autoscaling", region_name="us-east-1")

    client.create_launch_configuration(
        LaunchConfigurationName="test_launch_configuration",
        ImageId=EXAMPLE_AMI_ID,
        InstanceType="t2.medium",
    )
    client.create_auto_scaling_group(
        AutoScalingGroupName="test_asg",
        LaunchConfigurationName="test_launch_configuration",
        MinSize=2,
        MaxSize=20,
        DesiredCapacity=3,
        VPCZoneIdentifier=mocked_networking["subnet1"],
    )
    client.update_auto_scaling_group(AutoScalingGroupName="test_asg", MinSize=5)
    response = client.describe_auto_scaling_groups(AutoScalingGroupNames=["test_asg"])
    group = response["AutoScalingGroups"][0]
    group["DesiredCapacity"].should.equal(5)
    group["MinSize"].should.equal(5)
    group["Instances"].should.have.length_of(5)


@mock_autoscaling
def test_update_autoscaling_group_max_size_desired_capacity_change():
    mocked_networking = setup_networking()
    client = boto3.client("autoscaling", region_name="us-east-1")

    client.create_launch_configuration(
        LaunchConfigurationName="test_launch_configuration",
        ImageId=EXAMPLE_AMI_ID,
        InstanceType="t2.medium",
    )
    client.create_auto_scaling_group(
        AutoScalingGroupName="test_asg",
        LaunchConfigurationName="test_launch_configuration",
        MinSize=2,
        MaxSize=20,
        DesiredCapacity=10,
        VPCZoneIdentifier=mocked_networking["subnet1"],
    )
    client.update_auto_scaling_group(AutoScalingGroupName="test_asg", MaxSize=5)
    response = client.describe_auto_scaling_groups(AutoScalingGroupNames=["test_asg"])
    group = response["AutoScalingGroups"][0]
    group["DesiredCapacity"].should.equal(5)
    group["MaxSize"].should.equal(5)
    group["Instances"].should.have.length_of(5)


@mock_autoscaling
def test_autoscaling_describe_policies():
    mocked_networking = setup_networking()
    client = boto3.client("autoscaling", region_name="us-east-1")
    _ = client.create_launch_configuration(
        LaunchConfigurationName="test_launch_configuration",
        ImageId=EXAMPLE_AMI_ID,
        InstanceType="t2.medium",
    )
    _ = client.create_auto_scaling_group(
        AutoScalingGroupName="test_asg",
        LaunchConfigurationName="test_launch_configuration",
        MinSize=0,
        MaxSize=20,
        DesiredCapacity=5,
        Tags=[
            {
                "ResourceId": "test_asg",
                "Key": "test_key",
                "Value": "test_value",
                "PropagateAtLaunch": True,
            }
        ],
        VPCZoneIdentifier=mocked_networking["subnet1"],
    )

    client.put_scaling_policy(
        AutoScalingGroupName="test_asg",
        PolicyName="test_policy_down",
        PolicyType="SimpleScaling",
        MetricAggregationType="Minimum",
        AdjustmentType="PercentChangeInCapacity",
        ScalingAdjustment=-10,
        Cooldown=60,
        MinAdjustmentMagnitude=1,
    )
    client.put_scaling_policy(
        AutoScalingGroupName="test_asg",
        PolicyName="test_policy_up",
        PolicyType="SimpleScaling",
        AdjustmentType="PercentChangeInCapacity",
        ScalingAdjustment=10,
        Cooldown=60,
        MinAdjustmentMagnitude=1,
    )

    response = client.describe_policies()
    response["ScalingPolicies"].should.have.length_of(2)

    response = client.describe_policies(AutoScalingGroupName="test_asg")
    response["ScalingPolicies"].should.have.length_of(2)

    response = client.describe_policies(PolicyTypes=["StepScaling"])
    response["ScalingPolicies"].should.have.length_of(0)

    response = client.describe_policies(
        AutoScalingGroupName="test_asg",
        PolicyNames=["test_policy_down"],
        PolicyTypes=["SimpleScaling"],
    )
    response["ScalingPolicies"].should.have.length_of(1)
    policy = response["ScalingPolicies"][0]
    policy["PolicyType"].should.equal("SimpleScaling")
    policy["MetricAggregationType"].should.equal("Minimum")
    policy["AdjustmentType"].should.equal("PercentChangeInCapacity")
    policy["ScalingAdjustment"].should.equal(-10)
    policy["Cooldown"].should.equal(60)
    policy["PolicyARN"].should.equal(
        f"arn:aws:autoscaling:us-east-1:{ACCOUNT_ID}:scalingPolicy:c322761b-3172-4d56-9a21-0ed9d6161d67:autoScalingGroupName/test_asg:policyName/test_policy_down"
    )
    policy["PolicyName"].should.equal("test_policy_down")
    policy.shouldnt.have.key("TargetTrackingConfiguration")


@mock_autoscaling
@mock_ec2
def test_create_autoscaling_policy_with_policytype__targettrackingscaling():
    mocked_networking = setup_networking(region_name="us-west-1")
    client = boto3.client("autoscaling", region_name="us-west-1")
    configuration_name = "test"
    asg_name = "asg_test"

    client.create_launch_configuration(
        LaunchConfigurationName=configuration_name,
        ImageId=EXAMPLE_AMI_ID,
        InstanceType="m1.small",
    )
    client.create_auto_scaling_group(
        LaunchConfigurationName=configuration_name,
        AutoScalingGroupName=asg_name,
        MinSize=1,
        MaxSize=2,
        VPCZoneIdentifier=mocked_networking["subnet1"],
    )

    client.put_scaling_policy(
        AutoScalingGroupName=asg_name,
        PolicyName=configuration_name,
        PolicyType="TargetTrackingScaling",
        EstimatedInstanceWarmup=100,
        TargetTrackingConfiguration={
            "PredefinedMetricSpecification": {
                "PredefinedMetricType": "ASGAverageNetworkIn",
            },
            "TargetValue": 1000000.0,
        },
    )

    resp = client.describe_policies(AutoScalingGroupName=asg_name)
    policy = resp["ScalingPolicies"][0]
    policy.should.have.key("PolicyName").equals(configuration_name)
    policy.should.have.key("PolicyARN").equals(
        f"arn:aws:autoscaling:us-west-1:{ACCOUNT_ID}:scalingPolicy:c322761b-3172-4d56-9a21-0ed9d6161d67:autoScalingGroupName/{asg_name}:policyName/{configuration_name}"
    )
    policy.should.have.key("PolicyType").equals("TargetTrackingScaling")
    policy.should.have.key("TargetTrackingConfiguration").should.equal(
        {
            "PredefinedMetricSpecification": {
                "PredefinedMetricType": "ASGAverageNetworkIn",
            },
            "TargetValue": 1000000.0,
        }
    )
    policy.shouldnt.have.key("ScalingAdjustment")
    policy.shouldnt.have.key("Cooldown")


@mock_autoscaling
@mock_ec2
def test_create_autoscaling_policy_with_policytype__stepscaling():
    mocked_networking = setup_networking(region_name="eu-west-1")
    client = boto3.client("autoscaling", region_name="eu-west-1")
    launch_config_name = "lg_name"
    asg_name = "asg_test"

    client.create_launch_configuration(
        LaunchConfigurationName=launch_config_name,
        ImageId=EXAMPLE_AMI_ID,
        InstanceType="m1.small",
    )
    client.create_auto_scaling_group(
        LaunchConfigurationName=launch_config_name,
        AutoScalingGroupName=asg_name,
        MinSize=1,
        MaxSize=2,
        VPCZoneIdentifier=mocked_networking["subnet1"],
    )

    client.put_scaling_policy(
        AutoScalingGroupName=asg_name,
        PolicyName=launch_config_name,
        PolicyType="StepScaling",
        StepAdjustments=[
            {
                "MetricIntervalLowerBound": 2,
                "MetricIntervalUpperBound": 8,
                "ScalingAdjustment": 1,
            }
        ],
    )

    resp = client.describe_policies(AutoScalingGroupName=asg_name)
    policy = resp["ScalingPolicies"][0]
    policy.should.have.key("PolicyName").equals(launch_config_name)
    policy.should.have.key("PolicyARN").equals(
        f"arn:aws:autoscaling:eu-west-1:{ACCOUNT_ID}:scalingPolicy:c322761b-3172-4d56-9a21-0ed9d6161d67:autoScalingGroupName/{asg_name}:policyName/{launch_config_name}"
    )
    policy.should.have.key("PolicyType").equals("StepScaling")
    policy.should.have.key("StepAdjustments").equal(
        [
            {
                "MetricIntervalLowerBound": 2,
                "MetricIntervalUpperBound": 8,
                "ScalingAdjustment": 1,
            }
        ]
    )
    policy.shouldnt.have.key("TargetTrackingConfiguration")
    policy.shouldnt.have.key("ScalingAdjustment")
    policy.shouldnt.have.key("Cooldown")


@mock_autoscaling
@mock_ec2
def test_create_autoscaling_policy_with_predictive_scaling_config():
    mocked_networking = setup_networking(region_name="eu-west-1")
    client = boto3.client("autoscaling", region_name="eu-west-1")
    launch_config_name = "lg_name"
    asg_name = "asg_test"

    client.create_launch_configuration(
        LaunchConfigurationName=launch_config_name,
        ImageId=EXAMPLE_AMI_ID,
        InstanceType="m1.small",
    )
    client.create_auto_scaling_group(
        LaunchConfigurationName=launch_config_name,
        AutoScalingGroupName=asg_name,
        MinSize=1,
        MaxSize=2,
        VPCZoneIdentifier=mocked_networking["subnet1"],
    )

    client.put_scaling_policy(
        AutoScalingGroupName=asg_name,
        PolicyName=launch_config_name,
        PolicyType="PredictiveScaling",
        PredictiveScalingConfiguration={
            "MetricSpecifications": [{"TargetValue": 5}],
            "SchedulingBufferTime": 7,
        },
    )

    resp = client.describe_policies(AutoScalingGroupName=asg_name)
    policy = resp["ScalingPolicies"][0]
    policy.should.have.key("PredictiveScalingConfiguration").equals(
        {"MetricSpecifications": [{"TargetValue": 5.0}], "SchedulingBufferTime": 7}
    )


@mock_autoscaling
@mock_ec2
def test_create_auto_scaling_group_with_mixed_instances_policy():
    mocked_networking = setup_networking(region_name="eu-west-1")
    client = boto3.client("autoscaling", region_name="eu-west-1")
    ec2_client = boto3.client("ec2", region_name="eu-west-1")
    asg_name = "asg_test"

    lt = ec2_client.create_launch_template(
        LaunchTemplateName="launchie",
        LaunchTemplateData={"ImageId": EXAMPLE_AMI_ID},
    )["LaunchTemplate"]
    client.create_auto_scaling_group(
        MixedInstancesPolicy={
            "LaunchTemplate": {
                "LaunchTemplateSpecification": {
                    "LaunchTemplateName": "launchie",
                    "Version": "$DEFAULT",
                }
            }
        },
        AutoScalingGroupName=asg_name,
        MinSize=2,
        MaxSize=2,
        VPCZoneIdentifier=mocked_networking["subnet1"],
    )

    # Assert we can describe MixedInstancesPolicy
    response = client.describe_auto_scaling_groups(AutoScalingGroupNames=[asg_name])
    group = response["AutoScalingGroups"][0]
    group.should.have.key("MixedInstancesPolicy").equals(
        {
            "LaunchTemplate": {
                "LaunchTemplateSpecification": {
                    "LaunchTemplateId": lt["LaunchTemplateId"],
                    "LaunchTemplateName": "launchie",
                    "Version": "$DEFAULT",
                }
            }
        }
    )

    # Assert the LaunchTemplate is known for the resulting instances
    response = client.describe_auto_scaling_instances()
    len(response["AutoScalingInstances"]).should.equal(2)
    for instance in response["AutoScalingInstances"]:
        instance["LaunchTemplate"].should.equal(
            {
                "LaunchTemplateId": lt["LaunchTemplateId"],
                "LaunchTemplateName": "launchie",
                "Version": "$DEFAULT",
            }
        )


@mock_autoscaling
@mock_ec2
def test_create_auto_scaling_group_with_mixed_instances_policy_overrides():
    mocked_networking = setup_networking(region_name="eu-west-1")
    client = boto3.client("autoscaling", region_name="eu-west-1")
    ec2_client = boto3.client("ec2", region_name="eu-west-1")
    asg_name = "asg_test"

    lt = ec2_client.create_launch_template(
        LaunchTemplateName="launchie",
        LaunchTemplateData={"ImageId": EXAMPLE_AMI_ID},
    )["LaunchTemplate"]
    client.create_auto_scaling_group(
        MixedInstancesPolicy={
            "LaunchTemplate": {
                "LaunchTemplateSpecification": {
                    "LaunchTemplateName": "launchie",
                    "Version": "$DEFAULT",
                },
                "Overrides": [
                    {
                        "InstanceType": "t2.medium",
                        "WeightedCapacity": "50",
                    }
                ],
            }
        },
        AutoScalingGroupName=asg_name,
        MinSize=2,
        MaxSize=2,
        VPCZoneIdentifier=mocked_networking["subnet1"],
    )

    # Assert we can describe MixedInstancesPolicy
    response = client.describe_auto_scaling_groups(AutoScalingGroupNames=[asg_name])
    group = response["AutoScalingGroups"][0]
    group.should.have.key("MixedInstancesPolicy").equals(
        {
            "LaunchTemplate": {
                "LaunchTemplateSpecification": {
                    "LaunchTemplateId": lt["LaunchTemplateId"],
                    "LaunchTemplateName": "launchie",
                    "Version": "$DEFAULT",
                },
                "Overrides": [
                    {
                        "InstanceType": "t2.medium",
                        "WeightedCapacity": "50",
                    }
                ],
            }
        }
    )


@mock_autoscaling
def test_set_instance_protection():
    mocked_networking = setup_networking()
    client = boto3.client("autoscaling", region_name="us-east-1")
    _ = client.create_launch_configuration(
        LaunchConfigurationName="test_launch_configuration",
        ImageId=EXAMPLE_AMI_ID,
        InstanceType="t2.medium",
    )
    _ = client.create_auto_scaling_group(
        AutoScalingGroupName="test_asg",
        LaunchConfigurationName="test_launch_configuration",
        MinSize=0,
        MaxSize=20,
        DesiredCapacity=5,
        VPCZoneIdentifier=mocked_networking["subnet1"],
        NewInstancesProtectedFromScaleIn=False,
    )

    response = client.describe_auto_scaling_groups(AutoScalingGroupNames=["test_asg"])
    instance_ids = [
        instance["InstanceId"]
        for instance in response["AutoScalingGroups"][0]["Instances"]
    ]
    protected = instance_ids[:3]

    _ = client.set_instance_protection(
        AutoScalingGroupName="test_asg",
        InstanceIds=protected,
        ProtectedFromScaleIn=True,
    )

    response = client.describe_auto_scaling_groups(AutoScalingGroupNames=["test_asg"])
    for instance in response["AutoScalingGroups"][0]["Instances"]:
        instance["ProtectedFromScaleIn"].should.equal(
            instance["InstanceId"] in protected
        )


@mock_autoscaling
def test_set_desired_capacity_up():
    mocked_networking = setup_networking()
    client = boto3.client("autoscaling", region_name="us-east-1")
    _ = client.create_launch_configuration(
        LaunchConfigurationName="test_launch_configuration",
        ImageId=EXAMPLE_AMI_ID,
        InstanceType="t2.medium",
    )
    _ = client.create_auto_scaling_group(
        AutoScalingGroupName="test_asg",
        LaunchConfigurationName="test_launch_configuration",
        MinSize=0,
        MaxSize=20,
        DesiredCapacity=5,
        VPCZoneIdentifier=mocked_networking["subnet1"],
        NewInstancesProtectedFromScaleIn=True,
    )

    _ = client.set_desired_capacity(AutoScalingGroupName="test_asg", DesiredCapacity=10)

    response = client.describe_auto_scaling_groups(AutoScalingGroupNames=["test_asg"])
    instances = response["AutoScalingGroups"][0]["Instances"]
    instances.should.have.length_of(10)
    for instance in instances:
        instance["ProtectedFromScaleIn"].should.equal(True)


@mock_autoscaling
def test_set_desired_capacity_down():
    mocked_networking = setup_networking()
    client = boto3.client("autoscaling", region_name="us-east-1")
    _ = client.create_launch_configuration(
        LaunchConfigurationName="test_launch_configuration",
        ImageId=EXAMPLE_AMI_ID,
        InstanceType="t2.medium",
    )
    _ = client.create_auto_scaling_group(
        AutoScalingGroupName="test_asg",
        LaunchConfigurationName="test_launch_configuration",
        MinSize=0,
        MaxSize=20,
        DesiredCapacity=5,
        VPCZoneIdentifier=mocked_networking["subnet1"],
        NewInstancesProtectedFromScaleIn=True,
    )

    response = client.describe_auto_scaling_groups(AutoScalingGroupNames=["test_asg"])
    instance_ids = [
        instance["InstanceId"]
        for instance in response["AutoScalingGroups"][0]["Instances"]
    ]
    unprotected, protected = instance_ids[:2], instance_ids[2:]

    _ = client.set_instance_protection(
        AutoScalingGroupName="test_asg",
        InstanceIds=unprotected,
        ProtectedFromScaleIn=False,
    )

    _ = client.set_desired_capacity(AutoScalingGroupName="test_asg", DesiredCapacity=1)

    response = client.describe_auto_scaling_groups(AutoScalingGroupNames=["test_asg"])
    group = response["AutoScalingGroups"][0]
    group["DesiredCapacity"].should.equal(1)
    instance_ids = {instance["InstanceId"] for instance in group["Instances"]}
    set(protected).should.equal(instance_ids)
    set(unprotected).should_not.be.within(instance_ids)  # only unprotected killed


@mock_autoscaling
@mock_ec2
def test_terminate_instance_via_ec2_in_autoscaling_group():
    mocked_networking = setup_networking()
    client = boto3.client("autoscaling", region_name="us-east-1")
    _ = client.create_launch_configuration(
        LaunchConfigurationName="test_launch_configuration",
        ImageId=EXAMPLE_AMI_ID,
        InstanceType="t2.medium",
    )
    _ = client.create_auto_scaling_group(
        AutoScalingGroupName="test_asg",
        LaunchConfigurationName="test_launch_configuration",
        MinSize=1,
        MaxSize=20,
        VPCZoneIdentifier=mocked_networking["subnet1"],
        NewInstancesProtectedFromScaleIn=False,
    )

    response = client.describe_auto_scaling_groups(AutoScalingGroupNames=["test_asg"])
    original_instance_id = next(
        instance["InstanceId"]
        for instance in response["AutoScalingGroups"][0]["Instances"]
    )
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    ec2_client.terminate_instances(InstanceIds=[original_instance_id])

    response = client.describe_auto_scaling_groups(AutoScalingGroupNames=["test_asg"])
    replaced_instance_id = next(
        instance["InstanceId"]
        for instance in response["AutoScalingGroups"][0]["Instances"]
    )
    replaced_instance_id.should_not.equal(original_instance_id)


@mock_ec2
@mock_autoscaling
def test_attach_instances():
    asg_client = boto3.client("autoscaling", region_name="us-east-1")
    ec2_client = boto3.client("ec2", region_name="us-east-1")

    kwargs = {
        "KeyName": "foobar",
        "ImageId": EXAMPLE_AMI_ID,
        "MinCount": 1,
        "MaxCount": 1,
        "InstanceType": "c4.2xlarge",
        "TagSpecifications": [
            {"ResourceType": "instance", "Tags": [{"Key": "key", "Value": "val"}]},
        ],
    }
    fake_instance = ec2_client.run_instances(**kwargs)["Instances"][0]
    asg_client.create_launch_configuration(
        LaunchConfigurationName="test_launch_configuration",
        ImageId="ami-pytest",
        InstanceType="t3.micro",
        KeyName="foobar",
    )
    asg_client.create_auto_scaling_group(
        AutoScalingGroupName="test_asg",
        LaunchConfigurationName="test_launch_configuration",
        MinSize=0,
        MaxSize=1,
        AvailabilityZones=[fake_instance["Placement"]["AvailabilityZone"]],
    )
    asg_client.attach_instances(
        InstanceIds=[fake_instance["InstanceId"]], AutoScalingGroupName="test_asg"
    )
    response = asg_client.describe_auto_scaling_instances()
    len(response["AutoScalingInstances"]).should.equal(1)
    for instance in response["AutoScalingInstances"]:
        instance["LaunchConfigurationName"].should.equal("test_launch_configuration")
        instance["AutoScalingGroupName"].should.equal("test_asg")
        instance["InstanceType"].should.equal("c4.2xlarge")


@mock_autoscaling
def test_autoscaling_lifecyclehook():
    mocked_networking = setup_networking()
    client = boto3.client("autoscaling", region_name="us-east-1")
    client.create_launch_configuration(
        LaunchConfigurationName="test_launch_configuration",
        ImageId="ami-pytest",
        InstanceType="t3.micro",
        KeyName="foobar",
    )
    client.create_auto_scaling_group(
        AutoScalingGroupName="test_asg",
        LaunchConfigurationName="test_launch_configuration",
        MinSize=0,
        MaxSize=1,
        VPCZoneIdentifier=mocked_networking["subnet1"],
    )
    client.put_lifecycle_hook(
        LifecycleHookName="test-lifecyclehook",
        AutoScalingGroupName="test_asg",
        LifecycleTransition="autoscaling:EC2_INSTANCE_TERMINATING",
    )

    response = client.describe_lifecycle_hooks(
        AutoScalingGroupName="test_asg", LifecycleHookNames=["test-lifecyclehook"]
    )
    len(response["LifecycleHooks"]).should.equal(1)
    for hook in response["LifecycleHooks"]:
        hook["LifecycleHookName"].should.equal("test-lifecyclehook")
        hook["AutoScalingGroupName"].should.equal("test_asg")
        hook["LifecycleTransition"].should.equal("autoscaling:EC2_INSTANCE_TERMINATING")

    client.delete_lifecycle_hook(
        LifecycleHookName="test-lifecyclehook", AutoScalingGroupName="test_asg"
    )

    response = client.describe_lifecycle_hooks(
        AutoScalingGroupName="test_asg", LifecycleHookNames=["test-lifecyclehook"]
    )

    len(response["LifecycleHooks"]).should.equal(0)


@pytest.mark.parametrize("original,new", [(2, 1), (2, 3), (1, 5), (1, 1)])
@mock_autoscaling
def test_set_desired_capacity_without_protection(original, new):
    mocked_networking = setup_networking()
    client = boto3.client("autoscaling", region_name="us-east-1")
    client.create_launch_configuration(
        LaunchConfigurationName="test_launch_configuration",
        ImageId=EXAMPLE_AMI_ID,
        InstanceType="t2.medium",
    )

    client.create_auto_scaling_group(
        AutoScalingGroupName="tester_group",
        LaunchConfigurationName="test_launch_configuration",
        AvailabilityZones=["us-east-1a"],
        MinSize=original,
        MaxSize=original,
        DesiredCapacity=original,
        VPCZoneIdentifier=mocked_networking["subnet1"],
    )

    group = client.describe_auto_scaling_groups()["AutoScalingGroups"][0]
    group["DesiredCapacity"].should.equal(original)
    instances = client.describe_auto_scaling_instances()["AutoScalingInstances"]
    instances.should.have.length_of(original)

    client.update_auto_scaling_group(
        AutoScalingGroupName="tester_group", DesiredCapacity=new
    )

    group = client.describe_auto_scaling_groups()["AutoScalingGroups"][0]
    group["DesiredCapacity"].should.equal(new)
    instances = client.describe_auto_scaling_instances()["AutoScalingInstances"]
    instances.should.have.length_of(new)


@mock_autoscaling
@mock_ec2
def test_create_template_with_block_device():
    ec2_client = boto3.client("ec2", region_name="ap-southeast-2")
    ec2_client.create_launch_template(
        LaunchTemplateName="launchie",
        LaunchTemplateData={
            "ImageId": EXAMPLE_AMI_ID,
            "BlockDeviceMappings": [
                {
                    "DeviceName": "/dev/sda1",
                    "Ebs": {
                        "VolumeSize": 20,
                        "DeleteOnTermination": True,
                        "VolumeType": "gp3",
                        "Encrypted": True,
                    },
                }
            ],
        },
    )

    ec2_client.run_instances(
        MaxCount=1, MinCount=1, LaunchTemplate={"LaunchTemplateName": "launchie"}
    )
    ec2_client = boto3.client("ec2", region_name="ap-southeast-2")
    volumes = ec2_client.describe_volumes()["Volumes"]
    # The standard root volume
    volumes[0]["VolumeType"].should.equal("gp2")
    volumes[0]["Size"].should.equal(8)
    # Our Ebs-volume
    volumes[1]["VolumeType"].should.equal("gp3")
    volumes[1]["Size"].should.equal(20)
