import json
import time
from typing import Any
from unittest.mock import Mock, patch

import pytest

from anyscale.util import (
    _check_python_version,
    _ray_version_major_minor,
    _update_external_ids_for_policy,
    extract_versions_from_image_name,
    poll,
    prepare_cloudformation_template,
    sleep_till,
    str_data_size,
    updating_printer,
)


def test_updating_printer() -> None:
    out = ""

    def mock_print(
        string: str, *args: Any, end: str = "\n", flush: bool = False, **kwargs: Any
    ) -> None:
        nonlocal out
        out += string
        out += end

    with patch("anyscale.util.print", new=mock_print), patch(
        "shutil.get_terminal_size"
    ) as get_terminal_size_mock:
        get_terminal_size_mock.return_value = (10, 24)
        with updating_printer() as print_status:
            print_status("Step 1")
            print_status("Step 2")
            print_status("Step 3")

    assert out == (
        "\r          \r"
        "Step 1"
        "\r          \r"
        "Step 2"
        "\r          \r"
        "Step 3"
        "\r          \r"
    )


def test_updating_printer_multiline() -> None:
    out = ""

    def mock_print(
        string: str, *args: Any, end: str = "\n", flush: bool = False, **kwargs: Any
    ) -> None:
        nonlocal out
        out += string
        out += end

    with patch("anyscale.util.print", new=mock_print), patch(
        "shutil.get_terminal_size"
    ) as get_terminal_size_mock:
        get_terminal_size_mock.return_value = (10, 24)
        with updating_printer() as print_status:
            print_status("Step 1\nExtra stuff")
            print_status("ExtraLongLine12345")
            print_status("ExtraLongLine12345\nExtra stuff")
            print_status("Step 3")

    assert out == (
        "\r          \r"
        "Step 1..."
        "\r          \r"
        "ExtraLo..."
        "\r          \r"
        "ExtraLo..."
        "\r          \r"
        "Step 3"
        "\r          \r"
    )


STATEMENT_TEMPLATE = {
    "Action": "sts:AssumeRole",
    "Effect": "Allow",
    "Principal": {"AWS": "arn:aws:iam::ACCT_ID:root"},
}


@pytest.mark.parametrize(
    "statement_policy,expected_conditions",
    [
        pytest.param(
            [STATEMENT_TEMPLATE],
            [{"StringEquals": {"sts:ExternalId": ["new_id"]}}],
            id="OneStatement,NoPrior",
        ),
        pytest.param(
            [STATEMENT_TEMPLATE, STATEMENT_TEMPLATE],
            [{"StringEquals": {"sts:ExternalId": ["new_id"]}}] * 2,
            id="TwoStatements,NoPrior",
        ),
        pytest.param(
            [
                {
                    "Condition": {"StringEquals": {"sts:ExternalId": "old_id"}},
                    **STATEMENT_TEMPLATE,  # type: ignore
                }
            ],
            [{"StringEquals": {"sts:ExternalId": ["old_id", "new_id"]}}],
            id="OneStatement,OnePriorExternal",
        ),
        pytest.param(
            [
                {
                    "Condition": {"StringEquals": {"sts:ExternalId": "old_id"}},
                    **STATEMENT_TEMPLATE,  # type: ignore
                },
                STATEMENT_TEMPLATE,
            ],
            [
                {"StringEquals": {"sts:ExternalId": ["old_id", "new_id"]}},
                {"StringEquals": {"sts:ExternalId": ["new_id"]}},
            ],
            id="TwoStatements,OnePriorExternal",
        ),
        pytest.param(
            [
                {
                    "Condition": {"StringNotEquals": {"sts:ExternalId": "old_id"}},
                    **STATEMENT_TEMPLATE,  # type: ignore
                },
                STATEMENT_TEMPLATE,
            ],
            [
                {
                    "StringEquals": {"sts:ExternalId": ["new_id"]},
                    "StringNotEquals": {"sts:ExternalId": "old_id"},
                },
            ],
            id="OneStatemnt,OtherCondition",
        ),
    ],
)
def test_update_external_ids_for_policy(statement_policy, expected_conditions):
    policy_document = {
        "Statement": statement_policy,
        "Version": "2012-10-17",
    }
    new_policy = _update_external_ids_for_policy(policy_document, "new_id")

    for new, expected in zip(new_policy["Statement"], expected_conditions):
        assert new["Condition"] == expected


@pytest.mark.parametrize(
    "image_name, expected, exception_substr",
    [
        ("anyscale/ray-ml:1.11.1-py38-gpu", ("py38", "1.11.1"), None),
        ("anyscale/ray:1.12-py37-cpu", ("py37", "1.12"), None),
        ("anyscale/ray:1.12-py37", ("py37", "1.12"), None),
        ("anyscale/ray:1.12py37", None, "got 1.12py37"),
    ],
)
def test_extract_versions_from_image_name(image_name, expected, exception_substr):
    if exception_substr is not None:
        with pytest.raises(ValueError) as exc_info:
            extract_versions_from_image_name(image_name)
        assert exception_substr in str(exc_info.value)
    else:
        python_version, ray_version = extract_versions_from_image_name(image_name)
        assert (python_version, ray_version) == expected


@pytest.mark.parametrize(
    "ray_version, expected, exception_substr",
    [
        ("1.12", (1, 12), None),
        ("0.0", (0, 0), None),
        ("0:0", (0, 0), "unexpected"),
        ("112", (0, 0), "unexpected"),
        ("", (0, 0), "unexpected"),
        ("1.x", (0, 0), "unexpected"),
        ("0x10.12", (0, 0), "unexpected"),
    ],
)
def test_ray_version_major_minor(ray_version, expected, exception_substr):
    if exception_substr is not None:
        with pytest.raises(Exception) as exc_info:
            _ray_version_major_minor(ray_version)
        assert exception_substr in str(exc_info.value)
    else:
        got = _ray_version_major_minor(ray_version)
        assert got == expected


@pytest.mark.parametrize(
    "python_version, exception_substr",
    [
        ("py36", None),
        ("py37", None),
        ("py38", None),
        ("py39", None),
        ("py10", "got py10"),
        ("py3.6", "got py3.6"),
        ("py3", "got py3."),
        ("py35", "got py35"),
    ],
)
def test_python_version_major_minor(python_version, exception_substr):
    if exception_substr is not None:
        with pytest.raises(Exception) as exc_info:
            _check_python_version(python_version)
        assert exception_substr in str(exc_info.value)
    else:
        _check_python_version(python_version)


def test_poll():
    """Test the poll function.
    """

    end_time = time.time() + 0.5
    sleep_till(end_time)
    assert time.time() == pytest.approx(end_time)

    # This should poll forever
    count = 0
    start_time = time.time()
    for i in poll(0.01):
        count += 1
        assert count == i
        if count > 100:
            break
    assert count == 101
    assert time.time() == pytest.approx(start_time + 1.01)

    # Assert we stop iterating at max iter
    expected_i = 1
    for i in poll(0.01, max_iter=5):
        assert i == expected_i
        expected_i += 1
        assert i <= 5


def test_str_data_size():
    assert str_data_size("abcd") == 4

    # Serialized form: '{"hi": "ih"}'
    assert str_data_size(json.dumps({"hi": "ih"})) == 12


def test_prepare_cloudformation_template():

    mock_region = "us-east-1"
    mock_cfn_stack_name = "mock_cfn_stack_name"
    mock_cloud_id = "mock_cloud_id"

    mock_azs = [
        "us-east-1a",
        "us-east-1b",
        "us-east-1c",
        "us-east-1d",
        "us-east-1e",
        "us-east-1f",
    ]

    with patch("anyscale.util.get_availability_zones", new=Mock(return_value=mock_azs)):
        cfn_template = prepare_cloudformation_template(
            mock_region, mock_cfn_stack_name, mock_cloud_id
        )

    assert (
        cfn_template
        == """Description: This tempalte creates the resources necessary for anyscale clouds to function.

Parameters:
  EnvironmentName:
    Description: Anyscale deploy environment. Used in resource names and tags.
    Type: String

  CloudID:
    Description: ID of the anyscale cloud.
    Type: String

  VpcCIDR:
    Description: CIDR for the anyscale cloud VPC.
    Type: String
    Default: 10.0.0.0/16

  AnyscaleAWSAccountID:
    Description: Anyscale control plane AWS account.
    Type: String
    Default: 525325868955

  AnyscaleCrossAccountIAMRoleName:
    Description: Name of the cross account IAM role.
    Type: String

  AnyscaleCrossAccountIAMPolicySteadyState:
    Description: Stead state IAM policy document
    Type: String

  AnyscaleCrossAccountIAMPolicyInitialRun:
    Description: Initial run IAM policy document
    Type: String

  AnyscaleSecurityGroupName:
    Description: Name of the anyscale security group
    Type: String
    Default: "anyscale-security-group"

  ClusterNodeIAMRoleArn:
    Description: ARN of the data plane cluster IAM role
    Type: String

Resources:
  VPC:
    Type: AWS::EC2::VPC
    Properties:
      CidrBlock: !Ref VpcCIDR
      EnableDnsSupport: true
      EnableDnsHostnames: true
      Tags:
        - Key: Name
          Value: !Ref AWS::StackName
        - Key: anyscale-cloud-id
          Value: !Ref CloudID
        - Key: anyscale-deploy-environment
          Value: !Ref EnvironmentName

  InternetGateway:
    Type: AWS::EC2::InternetGateway
    Properties:
      Tags:
        - Key: Name
          Value: !Ref AWS::StackName
        - Key: anyscale-cloud-id
          Value: !Ref CloudID
        - Key: anyscale-deploy-environment
          Value: !Ref EnvironmentName

  InternetGatewayAttachment:
    Type: AWS::EC2::VPCGatewayAttachment
    Properties:
      InternetGatewayId: !Ref InternetGateway
      VpcId: !Ref VPC


  Subnet0:
    Type: AWS::EC2::Subnet
    Properties:
        VpcId: !Ref VPC
        AvailabilityZone: us-east-1a
        CidrBlock: 10.0.0.0/19
        MapPublicIpOnLaunch: true
        Tags:
        - Key: Name
          Value: mock_cfn_stack_name-subnet-us-east-1a
        - Key: anyscale-cloud-id
          Value: mock_cloud_id

  Subnet1:
    Type: AWS::EC2::Subnet
    Properties:
        VpcId: !Ref VPC
        AvailabilityZone: us-east-1b
        CidrBlock: 10.0.32.0/19
        MapPublicIpOnLaunch: true
        Tags:
        - Key: Name
          Value: mock_cfn_stack_name-subnet-us-east-1b
        - Key: anyscale-cloud-id
          Value: mock_cloud_id

  Subnet2:
    Type: AWS::EC2::Subnet
    Properties:
        VpcId: !Ref VPC
        AvailabilityZone: us-east-1c
        CidrBlock: 10.0.64.0/19
        MapPublicIpOnLaunch: true
        Tags:
        - Key: Name
          Value: mock_cfn_stack_name-subnet-us-east-1c
        - Key: anyscale-cloud-id
          Value: mock_cloud_id

  Subnet3:
    Type: AWS::EC2::Subnet
    Properties:
        VpcId: !Ref VPC
        AvailabilityZone: us-east-1d
        CidrBlock: 10.0.96.0/19
        MapPublicIpOnLaunch: true
        Tags:
        - Key: Name
          Value: mock_cfn_stack_name-subnet-us-east-1d
        - Key: anyscale-cloud-id
          Value: mock_cloud_id

  Subnet4:
    Type: AWS::EC2::Subnet
    Properties:
        VpcId: !Ref VPC
        AvailabilityZone: us-east-1e
        CidrBlock: 10.0.128.0/19
        MapPublicIpOnLaunch: true
        Tags:
        - Key: Name
          Value: mock_cfn_stack_name-subnet-us-east-1e
        - Key: anyscale-cloud-id
          Value: mock_cloud_id

  Subnet5:
    Type: AWS::EC2::Subnet
    Properties:
        VpcId: !Ref VPC
        AvailabilityZone: us-east-1f
        CidrBlock: 10.0.160.0/19
        MapPublicIpOnLaunch: true
        Tags:
        - Key: Name
          Value: mock_cfn_stack_name-subnet-us-east-1f
        - Key: anyscale-cloud-id
          Value: mock_cloud_id

  PublicRouteTable:
    Type: AWS::EC2::RouteTable
    Properties:
      VpcId: !Ref VPC
      Tags:
        - Key: Name
          Value: !Sub ${AWS::StackName} Public Routes
        - Key: anyscale-cloud-id
          Value: !Ref CloudID
        - Key: anyscale-deploy-environment
          Value: !Ref EnvironmentName

  DefaultPublicRoute:
    Type: AWS::EC2::Route
    DependsOn: InternetGatewayAttachment
    Properties:
      RouteTableId: !Ref PublicRouteTable
      DestinationCidrBlock: 0.0.0.0/0
      GatewayId: !Ref InternetGateway


  Subnet0RouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
        RouteTableId: !Ref PublicRouteTable
        SubnetId: !Ref Subnet0

  Subnet1RouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
        RouteTableId: !Ref PublicRouteTable
        SubnetId: !Ref Subnet1

  Subnet2RouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
        RouteTableId: !Ref PublicRouteTable
        SubnetId: !Ref Subnet2

  Subnet3RouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
        RouteTableId: !Ref PublicRouteTable
        SubnetId: !Ref Subnet3

  Subnet4RouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
        RouteTableId: !Ref PublicRouteTable
        SubnetId: !Ref Subnet4

  Subnet5RouteTableAssociation:
    Type: AWS::EC2::SubnetRouteTableAssociation
    Properties:
        RouteTableId: !Ref PublicRouteTable
        SubnetId: !Ref Subnet5

  AnyscaleSecurityGroup:
    Type: AWS::EC2::SecurityGroup
    Properties:
      GroupName: !Ref AnyscaleSecurityGroupName
      GroupDescription: "Anyscale security group"
      VpcId: !Ref VPC
      SecurityGroupIngress:
        # For https
        - IpProtocol: "tcp"
          FromPort: 443
          ToPort: 443
          CidrIp: "0.0.0.0/0"
        # For ssh
        - IpProtocol: "tcp"
          FromPort: 22
          ToPort: 22
          CidrIp: "0.0.0.0/0"
      Tags:
        - Key: anyscale-cloud-id
          Value: !Ref CloudID
        - Key: anyscale-deploy-environment
          Value: !Ref EnvironmentName

  # This allows ray cluster nodes to talk to each other since all nodes have the same security group attached.
  # This also allows ray cluster nodes to talk to EFS since they have the same security group attached.
  AnyscaleSecurityGroupIntraClusterIngressRule:
    Type: AWS::EC2::SecurityGroupIngress
    Properties:
      IpProtocol: "-1"
      GroupId: !Ref AnyscaleSecurityGroup
      SourceSecurityGroupId: !Ref AnyscaleSecurityGroup

  S3Bucket:
    Type: AWS::S3::Bucket
    Description: Anyscale managed s3 bucket.
    Properties:
      BucketName: !Sub anyscale-${EnvironmentName}-data-${AWS::StackName}
      CorsConfiguration:
        CorsRules:
          - AllowedHeaders:
              - '*'
            AllowedMethods:
              - GET
            AllowedOrigins:
              - https://console.anyscale.com
            Id: AnyscaleCORSRule
      PublicAccessBlockConfiguration:
        BlockPublicAcls: True
        BlockPublicPolicy: True
        IgnorePublicAcls: True
        RestrictPublicBuckets: True
      Tags:
        - Key: anyscale-cloud-id
          Value: !Ref CloudID
        - Key: anyscale-deploy-environment
          Value: !Ref EnvironmentName

  S3BucketPolicy:
    Type: AWS::S3::BucketPolicy
    Description: Bucket policy that allow ray autoscaler role to access the bucket.
    Properties:
      Bucket: !Ref S3Bucket
      PolicyDocument:
        Version: 2012-10-17
        Statement:
          - Action:
              - "s3:PutObject"
              - "s3:DeleteObject"
              - "s3:GetObject"
              - "s3:ListBucket"
            Effect: Allow
            Resource:
              - !Sub arn:aws:s3:::${S3Bucket}
              - !Sub arn:aws:s3:::${S3Bucket}/*
            Principal:
              AWS:
                - !Ref ClusterNodeIAMRoleArn
                - !GetAtt
                  - customerRole
                  - Arn
  EFS:
    Type: AWS::EFS::FileSystem
    Properties:
        BackupPolicy:
          Status: ENABLED
        Encrypted: true
        LifecyclePolicies:
          - TransitionToIA: AFTER_60_DAYS
        PerformanceMode: generalPurpose
        Encrypted: true
        ThroughputMode: bursting
        FileSystemTags:
          - Key: anyscale-cloud-id
            Value: !Ref CloudID
          - Key: anyscale-deploy-environment
            Value: !Ref EnvironmentName

  EFSMountTarget:
    Type: AWS::EFS::MountTarget
    Properties:
        FileSystemId: !Ref EFS
        SecurityGroups:
          - !Ref AnyscaleSecurityGroup
        SubnetId: !Ref Subnet1

  customerRole:
    Type: 'AWS::IAM::Role'
    Properties:
      RoleName: !Ref AnyscaleCrossAccountIAMRoleName
      AssumeRolePolicyDocument:
        Statement:
          - Action: 'sts:AssumeRole'
            Effect: Allow
            Principal:
              AWS: !Ref AnyscaleAWSAccountID
            Sid: 'AnyscaleControlPlaneAssumeRole'
            Condition:
              StringEquals:
                  sts:ExternalId: !Ref CloudID
        Version: 2012-10-17
      Path: /
      Tags:
        - Key: Name
          Value: !Ref AWS::StackName
        - Key: anyscale-cloud-id
          Value: !Ref CloudID
        - Key: anyscale-deploy-environment
          Value: !Ref EnvironmentName

  IAMPermissionEC2SteadyState:
    Type: AWS::IAM::Policy
    Properties:
      PolicyDocument: !Ref AnyscaleCrossAccountIAMPolicySteadyState
      PolicyName: Anyscale_IAM_Policy_Steady_State
      Roles:
        - !Ref customerRole

  IAMPermissionEC2InitialRun:
    Type: AWS::IAM::Policy
    Properties:
      PolicyDocument: !Ref AnyscaleCrossAccountIAMPolicyInitialRun
      PolicyName: Anyscale_IAM_Policy_Initial_Setup
      Roles:
        - !Ref customerRole

Outputs:
  VPC:
    Description: A reference to the created VPC
    Value: !Ref VPC

  PublicSubnets:
    Description: A list of the public subnets
    Value: !Join [",", [!Ref Subnet0,!Ref Subnet1,!Ref Subnet2,!Ref Subnet3,!Ref Subnet4,!Ref Subnet5]]

  AnyscaleSecurityGroup:
    Description: Anyscale Security group
    Value: !Ref AnyscaleSecurityGroup

  S3Bucket:
    Description: Anyscale managed S3 bucket
    Value: !Ref S3Bucket

  EFS:
    Description: Anyscale managed EFS
    Value: !Ref EFS

  AnyscaleIAMRole:
    Description: ARN of the cross-account IAM role
    Value: !GetAtt
      - customerRole
      - Arn
"""
    )
