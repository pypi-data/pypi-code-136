from typing import List
from unittest.mock import Mock, patch

import pytest
from ray.autoscaler._private.aws.config import DEFAULT_RAY_IAM_ROLE

from anyscale.cloud_resource import (
    verify_aws_cloudformation_stack,
    verify_aws_efs,
    verify_aws_iam_roles,
    verify_aws_s3,
    verify_aws_security_groups,
    verify_aws_subnets,
    verify_aws_vpc,
)
from anyscale.conf import ANYSCALE_IAM_ROLE_NAME
from frontend.cli.anyscale.aws_iam_policies import (
    AMAZON_ECR_READONLY_ACCESS_POLICY_NAME,
    AMAZON_S3_FULL_ACCESS_POLICY_NAME,
    ANYSCALE_IAM_PERMISSIONS_EC2_INITIAL_RUN,
    ANYSCALE_IAM_PERMISSIONS_EC2_STEADY_STATE,
    ANYSCALE_IAM_POLICY_NAME_INITIAL_RUN,
    ANYSCALE_IAM_POLICY_NAME_STEADY_STATE,
    get_anyscale_aws_iam_assume_role_policy,
)
from frontend.cli.anyscale.client.openapi_client.models.create_cloud_resource import (
    CreateCloudResource,
)


def generate_cloud_resource_mock_aws() -> CreateCloudResource:
    return CreateCloudResource(
        aws_vpc_id="fake_aws_vpc_id",
        aws_subnet_ids=["fake_aws_subnet_id_0"],
        aws_iam_role_arns=["arn:aws:iam::123:role/mock_anyscale_role"],
        aws_security_groups=["fake_aws_security_group_0"],
        aws_s3_id="fake_aws_s3_id",
        aws_efs_id="fake_aws_efs_id",
        aws_cloudformation_stack_id="fake_aws_cloudformation_stack_id",
    )


def generate_cluod_aws_iam_roles() -> List[Mock]:
    anyscale_iam_role = Mock(role_name=ANYSCALE_IAM_ROLE_NAME)
    anyscale_iam_role.assume_role_policy_document = get_anyscale_aws_iam_assume_role_policy(
        anyscale_aws_account=""
    )
    steady_state_policy = Mock(
        policy_name=ANYSCALE_IAM_POLICY_NAME_STEADY_STATE,
        policy_document=ANYSCALE_IAM_PERMISSIONS_EC2_STEADY_STATE,
    )
    initial_run_policy = Mock(
        policy_name=ANYSCALE_IAM_POLICY_NAME_INITIAL_RUN,
        policy_document=ANYSCALE_IAM_PERMISSIONS_EC2_INITIAL_RUN,
    )
    anyscale_iam_role.policies.all = Mock(
        return_value=[steady_state_policy, initial_run_policy]
    )

    ray_iam_role = Mock(role_name=DEFAULT_RAY_IAM_ROLE)
    ecr_readonly_policy = Mock(policy_name=AMAZON_ECR_READONLY_ACCESS_POLICY_NAME)
    s3_full_access_policy = Mock(policy_name=AMAZON_S3_FULL_ACCESS_POLICY_NAME)
    ray_iam_role.attached_policies.all = Mock(
        return_value=[ecr_readonly_policy, s3_full_access_policy]
    )

    return [anyscale_iam_role, ray_iam_role]


def generate_aws_security_groups() -> List[Mock]:
    ip_permission_443 = {"FromPort": 443}
    ip_permission_22 = {"FromPort": 22}
    inbound_ip_permissions = [
        ip_permission_443,
        ip_permission_22,
        {
            "IpProtocol": "-1",
            "UserIdGroupPairs": [{"GroupId": "fake_aws_security_group_0"}],
        },
    ]
    anyscale_security_group = Mock(ip_permissions=inbound_ip_permissions)
    return anyscale_security_group


def generate_aws_subnets() -> List[Mock]:
    return [
        Mock(
            id="mock_id_0",
            cidr_block="0.0.0.0/18",
            vpc_id="fake_aws_vpc_id",
            availability_zone="us-west-2a",
        ),
        Mock(
            id="mock_id_1",
            cidr_block="0.0.0.0/19",
            vpc_id="fake_aws_vpc_id",
            availability_zone="us-west-2c",
        ),
        Mock(
            id="mock_id_2",
            cidr_block="1.2.3.4/20",
            vpc_id="fake_aws_vpc_id",
            availability_zone="us-west-2b",
        ),
    ]


@pytest.mark.parametrize(
    "vpc_exists,vpc_cidr_block,expected_result",
    [
        pytest.param(False, "0.0.0.0/0", False),
        pytest.param(True, "0.0.0.0/16", True),
        pytest.param(True, "1.23.45.67/20", False),
    ],
)
def test_verify_aws_vpc(vpc_exists: bool, vpc_cidr_block: str, expected_result: bool):
    cloud_resource_mock = generate_cloud_resource_mock_aws()
    vpc_mock = Mock(cidr_block=vpc_cidr_block) if vpc_exists else None
    ec2_mock = Mock(Vpc=Mock(return_value=vpc_mock))
    boto3_session_mock = Mock(resource=Mock(return_value=ec2_mock))

    result = verify_aws_vpc(
        cloud_resource=cloud_resource_mock,
        boto3_session=boto3_session_mock,
        logger=Mock(),
    )
    assert result == expected_result


def test_verify_aws_subnets():
    cloud_resource_mock = generate_cloud_resource_mock_aws()
    subnets_mock = generate_aws_subnets()
    availability_zones_mock = ["us-west-2a", "us-west-2b", "us-west-2c"]
    with patch.multiple(
        "anyscale.cloud_resource",
        _get_subnets_from_subnet_ids=Mock(return_value=subnets_mock),
        get_availability_zones=Mock(return_value=availability_zones_mock),
    ):
        result, cloud_resource = verify_aws_subnets(
            cloud_resource=cloud_resource_mock, region="fake_region", logger=Mock()
        )
        assert result
        # ensuring that the subnet ids is sorted according to availability zones' alphabetical order
        subnet_dict_by_id = {subnet.id: subnet for subnet in subnets_mock}
        subnet_availability_zones = [
            subnet_dict_by_id[subnet_id].availability_zone
            for subnet_id in cloud_resource.aws_subnet_ids
        ]
        assert subnet_availability_zones == sorted(subnet_availability_zones)


def test_verify_aws_iam_roles():
    cloud_resource_mock = generate_cloud_resource_mock_aws()
    iam_roles_mock = generate_cluod_aws_iam_roles()
    with patch.multiple(
        "anyscale.cloud_resource",
        _get_roles_from_role_names=Mock(return_value=iam_roles_mock),
        get_anyscale_aws_iam_assume_role_policy=Mock(
            return_value=iam_roles_mock[0].assume_role_policy_document
        ),
    ):
        result = verify_aws_iam_roles(
            cloud_resource=cloud_resource_mock,
            region="fake_region",
            anyscale_aws_account="fake_anyscale_aws_account",
            logger=Mock(),
        )
        assert result


def test_verify_aws_security_groups():
    cloud_resource_mock = generate_cloud_resource_mock_aws()
    security_group_mock = generate_aws_security_groups()
    ec2_mock = Mock(SecurityGroup=Mock(return_value=security_group_mock))
    boto3_session_mock = Mock(resource=Mock(return_value=ec2_mock))

    result = verify_aws_security_groups(
        cloud_resource=cloud_resource_mock,
        boto3_session=boto3_session_mock,
        logger=Mock(),
    )
    assert result


@pytest.mark.parametrize(
    "s3_exists,expected_result", [pytest.param(False, False), pytest.param(True, True)]
)
def test_verify_aws_s3(s3_exists: bool, expected_result: bool):
    cloud_resource_mock = generate_cloud_resource_mock_aws()
    s3_mock = Mock()
    s3_bucket_mock = Mock() if s3_exists else None
    s3_mock = Mock(Bucket=Mock(return_value=s3_bucket_mock))
    boto3_session_mock = Mock(resource=Mock(return_value=s3_mock))

    result = verify_aws_s3(
        cloud_resource=cloud_resource_mock,
        boto3_session=boto3_session_mock,
        logger=Mock(),
    )
    assert result == expected_result


@pytest.mark.parametrize(
    "efs_exists,expected_result",
    [pytest.param(False, False), pytest.param(True, True)],
)
def test_verify_aws_efs(efs_exists: bool, expected_result: bool):
    cloud_resource_mock = generate_cloud_resource_mock_aws()
    efs_response_mock = {"FileSystems": Mock() if efs_exists else None}
    efs_client_mock = Mock(describe_file_systems=Mock(return_value=efs_response_mock))
    boto3_session_mock = Mock(client=Mock(return_value=efs_client_mock))

    result = verify_aws_efs(
        cloud_resource=cloud_resource_mock,
        boto3_session=boto3_session_mock,
        logger=Mock(),
    )
    assert result == expected_result


@pytest.mark.parametrize(
    "cloudformation_stack_exists,expected_result",
    [pytest.param(False, False), pytest.param(True, True)],
)
def test_verify_aws_cloudformation_stack(
    cloudformation_stack_exists: bool, expected_result: bool
):
    cloud_resource_mock = generate_cloud_resource_mock_aws()
    cloudformation_stack_mock = Mock() if cloudformation_stack_exists else None
    cloudformation_mock = Mock(Stack=Mock(return_value=cloudformation_stack_mock))
    boto3_session_mock = Mock(resource=Mock(return_value=cloudformation_mock))

    result = verify_aws_cloudformation_stack(
        cloud_resource=cloud_resource_mock,
        boto3_session=boto3_session_mock,
        logger=Mock(),
    )
    assert result == expected_result
