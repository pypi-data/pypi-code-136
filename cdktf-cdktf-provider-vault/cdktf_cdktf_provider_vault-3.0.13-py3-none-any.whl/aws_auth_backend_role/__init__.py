'''
# `vault_aws_auth_backend_role`

Refer to the Terraform Registory for docs: [`vault_aws_auth_backend_role`](https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role).
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


class AwsAuthBackendRole(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.awsAuthBackendRole.AwsAuthBackendRole",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role vault_aws_auth_backend_role}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        role: builtins.str,
        allow_instance_migration: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        auth_type: typing.Optional[builtins.str] = None,
        backend: typing.Optional[builtins.str] = None,
        bound_account_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        bound_ami_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        bound_ec2_instance_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        bound_iam_instance_profile_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        bound_iam_principal_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        bound_iam_role_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        bound_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        bound_subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        bound_vpc_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        disallow_reauthentication: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        inferred_aws_region: typing.Optional[builtins.str] = None,
        inferred_entity_type: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        resolve_aws_unique_ids: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        role_tag: typing.Optional[builtins.str] = None,
        token_bound_cidrs: typing.Optional[typing.Sequence[builtins.str]] = None,
        token_explicit_max_ttl: typing.Optional[jsii.Number] = None,
        token_max_ttl: typing.Optional[jsii.Number] = None,
        token_no_default_policy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        token_num_uses: typing.Optional[jsii.Number] = None,
        token_period: typing.Optional[jsii.Number] = None,
        token_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        token_ttl: typing.Optional[jsii.Number] = None,
        token_type: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role vault_aws_auth_backend_role} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param role: Name of the role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#role AwsAuthBackendRole#role}
        :param allow_instance_migration: When true, allows migration of the underlying instance where the client resides. Use with caution. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#allow_instance_migration AwsAuthBackendRole#allow_instance_migration}
        :param auth_type: The auth type permitted for this role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#auth_type AwsAuthBackendRole#auth_type}
        :param backend: Unique name of the auth backend to configure. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#backend AwsAuthBackendRole#backend}
        :param bound_account_ids: Only EC2 instances with this account ID in their identity document will be permitted to log in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#bound_account_ids AwsAuthBackendRole#bound_account_ids}
        :param bound_ami_ids: Only EC2 instances using this AMI ID will be permitted to log in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#bound_ami_ids AwsAuthBackendRole#bound_ami_ids}
        :param bound_ec2_instance_ids: Only EC2 instances that match this instance ID will be permitted to log in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#bound_ec2_instance_ids AwsAuthBackendRole#bound_ec2_instance_ids}
        :param bound_iam_instance_profile_arns: Only EC2 instances associated with an IAM instance profile ARN that matches this value will be permitted to log in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#bound_iam_instance_profile_arns AwsAuthBackendRole#bound_iam_instance_profile_arns}
        :param bound_iam_principal_arns: The IAM principal that must be authenticated using the iam auth method. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#bound_iam_principal_arns AwsAuthBackendRole#bound_iam_principal_arns}
        :param bound_iam_role_arns: Only EC2 instances that match this IAM role ARN will be permitted to log in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#bound_iam_role_arns AwsAuthBackendRole#bound_iam_role_arns}
        :param bound_regions: Only EC2 instances in this region will be permitted to log in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#bound_regions AwsAuthBackendRole#bound_regions}
        :param bound_subnet_ids: Only EC2 instances associated with this subnet ID will be permitted to log in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#bound_subnet_ids AwsAuthBackendRole#bound_subnet_ids}
        :param bound_vpc_ids: Only EC2 instances associated with this VPC ID will be permitted to log in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#bound_vpc_ids AwsAuthBackendRole#bound_vpc_ids}
        :param disallow_reauthentication: When true, only allows a single token to be granted per instance ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#disallow_reauthentication AwsAuthBackendRole#disallow_reauthentication}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#id AwsAuthBackendRole#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param inferred_aws_region: The region to search for the inferred entities in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#inferred_aws_region AwsAuthBackendRole#inferred_aws_region}
        :param inferred_entity_type: The type of inferencing Vault should do. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#inferred_entity_type AwsAuthBackendRole#inferred_entity_type}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#namespace AwsAuthBackendRole#namespace}
        :param resolve_aws_unique_ids: Whether or not Vault should resolve the bound_iam_principal_arn to an AWS Unique ID. When true, deleting a principal and recreating it with the same name won't automatically grant the new principal the same roles in Vault that the old principal had. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#resolve_aws_unique_ids AwsAuthBackendRole#resolve_aws_unique_ids}
        :param role_tag: The key of the tag on EC2 instance to use for role tags. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#role_tag AwsAuthBackendRole#role_tag}
        :param token_bound_cidrs: Specifies the blocks of IP addresses which are allowed to use the generated token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#token_bound_cidrs AwsAuthBackendRole#token_bound_cidrs}
        :param token_explicit_max_ttl: Generated Token's Explicit Maximum TTL in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#token_explicit_max_ttl AwsAuthBackendRole#token_explicit_max_ttl}
        :param token_max_ttl: The maximum lifetime of the generated token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#token_max_ttl AwsAuthBackendRole#token_max_ttl}
        :param token_no_default_policy: If true, the 'default' policy will not automatically be added to generated tokens. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#token_no_default_policy AwsAuthBackendRole#token_no_default_policy}
        :param token_num_uses: The maximum number of times a token may be used, a value of zero means unlimited. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#token_num_uses AwsAuthBackendRole#token_num_uses}
        :param token_period: Generated Token's Period. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#token_period AwsAuthBackendRole#token_period}
        :param token_policies: Generated Token's Policies. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#token_policies AwsAuthBackendRole#token_policies}
        :param token_ttl: The initial ttl of the token to generate in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#token_ttl AwsAuthBackendRole#token_ttl}
        :param token_type: The type of token to generate, service or batch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#token_type AwsAuthBackendRole#token_type}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AwsAuthBackendRole.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AwsAuthBackendRoleConfig(
            role=role,
            allow_instance_migration=allow_instance_migration,
            auth_type=auth_type,
            backend=backend,
            bound_account_ids=bound_account_ids,
            bound_ami_ids=bound_ami_ids,
            bound_ec2_instance_ids=bound_ec2_instance_ids,
            bound_iam_instance_profile_arns=bound_iam_instance_profile_arns,
            bound_iam_principal_arns=bound_iam_principal_arns,
            bound_iam_role_arns=bound_iam_role_arns,
            bound_regions=bound_regions,
            bound_subnet_ids=bound_subnet_ids,
            bound_vpc_ids=bound_vpc_ids,
            disallow_reauthentication=disallow_reauthentication,
            id=id,
            inferred_aws_region=inferred_aws_region,
            inferred_entity_type=inferred_entity_type,
            namespace=namespace,
            resolve_aws_unique_ids=resolve_aws_unique_ids,
            role_tag=role_tag,
            token_bound_cidrs=token_bound_cidrs,
            token_explicit_max_ttl=token_explicit_max_ttl,
            token_max_ttl=token_max_ttl,
            token_no_default_policy=token_no_default_policy,
            token_num_uses=token_num_uses,
            token_period=token_period,
            token_policies=token_policies,
            token_ttl=token_ttl,
            token_type=token_type,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetAllowInstanceMigration")
    def reset_allow_instance_migration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowInstanceMigration", []))

    @jsii.member(jsii_name="resetAuthType")
    def reset_auth_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthType", []))

    @jsii.member(jsii_name="resetBackend")
    def reset_backend(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackend", []))

    @jsii.member(jsii_name="resetBoundAccountIds")
    def reset_bound_account_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBoundAccountIds", []))

    @jsii.member(jsii_name="resetBoundAmiIds")
    def reset_bound_ami_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBoundAmiIds", []))

    @jsii.member(jsii_name="resetBoundEc2InstanceIds")
    def reset_bound_ec2_instance_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBoundEc2InstanceIds", []))

    @jsii.member(jsii_name="resetBoundIamInstanceProfileArns")
    def reset_bound_iam_instance_profile_arns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBoundIamInstanceProfileArns", []))

    @jsii.member(jsii_name="resetBoundIamPrincipalArns")
    def reset_bound_iam_principal_arns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBoundIamPrincipalArns", []))

    @jsii.member(jsii_name="resetBoundIamRoleArns")
    def reset_bound_iam_role_arns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBoundIamRoleArns", []))

    @jsii.member(jsii_name="resetBoundRegions")
    def reset_bound_regions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBoundRegions", []))

    @jsii.member(jsii_name="resetBoundSubnetIds")
    def reset_bound_subnet_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBoundSubnetIds", []))

    @jsii.member(jsii_name="resetBoundVpcIds")
    def reset_bound_vpc_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBoundVpcIds", []))

    @jsii.member(jsii_name="resetDisallowReauthentication")
    def reset_disallow_reauthentication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisallowReauthentication", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInferredAwsRegion")
    def reset_inferred_aws_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInferredAwsRegion", []))

    @jsii.member(jsii_name="resetInferredEntityType")
    def reset_inferred_entity_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInferredEntityType", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetResolveAwsUniqueIds")
    def reset_resolve_aws_unique_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResolveAwsUniqueIds", []))

    @jsii.member(jsii_name="resetRoleTag")
    def reset_role_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoleTag", []))

    @jsii.member(jsii_name="resetTokenBoundCidrs")
    def reset_token_bound_cidrs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenBoundCidrs", []))

    @jsii.member(jsii_name="resetTokenExplicitMaxTtl")
    def reset_token_explicit_max_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenExplicitMaxTtl", []))

    @jsii.member(jsii_name="resetTokenMaxTtl")
    def reset_token_max_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenMaxTtl", []))

    @jsii.member(jsii_name="resetTokenNoDefaultPolicy")
    def reset_token_no_default_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenNoDefaultPolicy", []))

    @jsii.member(jsii_name="resetTokenNumUses")
    def reset_token_num_uses(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenNumUses", []))

    @jsii.member(jsii_name="resetTokenPeriod")
    def reset_token_period(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenPeriod", []))

    @jsii.member(jsii_name="resetTokenPolicies")
    def reset_token_policies(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenPolicies", []))

    @jsii.member(jsii_name="resetTokenTtl")
    def reset_token_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenTtl", []))

    @jsii.member(jsii_name="resetTokenType")
    def reset_token_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenType", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="roleId")
    def role_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleId"))

    @builtins.property
    @jsii.member(jsii_name="allowInstanceMigrationInput")
    def allow_instance_migration_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowInstanceMigrationInput"))

    @builtins.property
    @jsii.member(jsii_name="authTypeInput")
    def auth_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="backendInput")
    def backend_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendInput"))

    @builtins.property
    @jsii.member(jsii_name="boundAccountIdsInput")
    def bound_account_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "boundAccountIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="boundAmiIdsInput")
    def bound_ami_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "boundAmiIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="boundEc2InstanceIdsInput")
    def bound_ec2_instance_ids_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "boundEc2InstanceIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="boundIamInstanceProfileArnsInput")
    def bound_iam_instance_profile_arns_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "boundIamInstanceProfileArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="boundIamPrincipalArnsInput")
    def bound_iam_principal_arns_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "boundIamPrincipalArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="boundIamRoleArnsInput")
    def bound_iam_role_arns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "boundIamRoleArnsInput"))

    @builtins.property
    @jsii.member(jsii_name="boundRegionsInput")
    def bound_regions_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "boundRegionsInput"))

    @builtins.property
    @jsii.member(jsii_name="boundSubnetIdsInput")
    def bound_subnet_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "boundSubnetIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="boundVpcIdsInput")
    def bound_vpc_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "boundVpcIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="disallowReauthenticationInput")
    def disallow_reauthentication_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disallowReauthenticationInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="inferredAwsRegionInput")
    def inferred_aws_region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inferredAwsRegionInput"))

    @builtins.property
    @jsii.member(jsii_name="inferredEntityTypeInput")
    def inferred_entity_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inferredEntityTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="resolveAwsUniqueIdsInput")
    def resolve_aws_unique_ids_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "resolveAwsUniqueIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="roleInput")
    def role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleInput"))

    @builtins.property
    @jsii.member(jsii_name="roleTagInput")
    def role_tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleTagInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenBoundCidrsInput")
    def token_bound_cidrs_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tokenBoundCidrsInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenExplicitMaxTtlInput")
    def token_explicit_max_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tokenExplicitMaxTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenMaxTtlInput")
    def token_max_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tokenMaxTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenNoDefaultPolicyInput")
    def token_no_default_policy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "tokenNoDefaultPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenNumUsesInput")
    def token_num_uses_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tokenNumUsesInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenPeriodInput")
    def token_period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tokenPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenPoliciesInput")
    def token_policies_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tokenPoliciesInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenTtlInput")
    def token_ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "tokenTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenTypeInput")
    def token_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="allowInstanceMigration")
    def allow_instance_migration(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowInstanceMigration"))

    @allow_instance_migration.setter
    def allow_instance_migration(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendRole, "allow_instance_migration").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowInstanceMigration", value)

    @builtins.property
    @jsii.member(jsii_name="authType")
    def auth_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authType"))

    @auth_type.setter
    def auth_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendRole, "auth_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authType", value)

    @builtins.property
    @jsii.member(jsii_name="backend")
    def backend(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backend"))

    @backend.setter
    def backend(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendRole, "backend").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backend", value)

    @builtins.property
    @jsii.member(jsii_name="boundAccountIds")
    def bound_account_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "boundAccountIds"))

    @bound_account_ids.setter
    def bound_account_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendRole, "bound_account_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "boundAccountIds", value)

    @builtins.property
    @jsii.member(jsii_name="boundAmiIds")
    def bound_ami_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "boundAmiIds"))

    @bound_ami_ids.setter
    def bound_ami_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendRole, "bound_ami_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "boundAmiIds", value)

    @builtins.property
    @jsii.member(jsii_name="boundEc2InstanceIds")
    def bound_ec2_instance_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "boundEc2InstanceIds"))

    @bound_ec2_instance_ids.setter
    def bound_ec2_instance_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendRole, "bound_ec2_instance_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "boundEc2InstanceIds", value)

    @builtins.property
    @jsii.member(jsii_name="boundIamInstanceProfileArns")
    def bound_iam_instance_profile_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "boundIamInstanceProfileArns"))

    @bound_iam_instance_profile_arns.setter
    def bound_iam_instance_profile_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendRole, "bound_iam_instance_profile_arns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "boundIamInstanceProfileArns", value)

    @builtins.property
    @jsii.member(jsii_name="boundIamPrincipalArns")
    def bound_iam_principal_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "boundIamPrincipalArns"))

    @bound_iam_principal_arns.setter
    def bound_iam_principal_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendRole, "bound_iam_principal_arns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "boundIamPrincipalArns", value)

    @builtins.property
    @jsii.member(jsii_name="boundIamRoleArns")
    def bound_iam_role_arns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "boundIamRoleArns"))

    @bound_iam_role_arns.setter
    def bound_iam_role_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendRole, "bound_iam_role_arns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "boundIamRoleArns", value)

    @builtins.property
    @jsii.member(jsii_name="boundRegions")
    def bound_regions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "boundRegions"))

    @bound_regions.setter
    def bound_regions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendRole, "bound_regions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "boundRegions", value)

    @builtins.property
    @jsii.member(jsii_name="boundSubnetIds")
    def bound_subnet_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "boundSubnetIds"))

    @bound_subnet_ids.setter
    def bound_subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendRole, "bound_subnet_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "boundSubnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="boundVpcIds")
    def bound_vpc_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "boundVpcIds"))

    @bound_vpc_ids.setter
    def bound_vpc_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendRole, "bound_vpc_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "boundVpcIds", value)

    @builtins.property
    @jsii.member(jsii_name="disallowReauthentication")
    def disallow_reauthentication(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disallowReauthentication"))

    @disallow_reauthentication.setter
    def disallow_reauthentication(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendRole, "disallow_reauthentication").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disallowReauthentication", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendRole, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="inferredAwsRegion")
    def inferred_aws_region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "inferredAwsRegion"))

    @inferred_aws_region.setter
    def inferred_aws_region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendRole, "inferred_aws_region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inferredAwsRegion", value)

    @builtins.property
    @jsii.member(jsii_name="inferredEntityType")
    def inferred_entity_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "inferredEntityType"))

    @inferred_entity_type.setter
    def inferred_entity_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendRole, "inferred_entity_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inferredEntityType", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendRole, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="resolveAwsUniqueIds")
    def resolve_aws_unique_ids(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "resolveAwsUniqueIds"))

    @resolve_aws_unique_ids.setter
    def resolve_aws_unique_ids(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendRole, "resolve_aws_unique_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resolveAwsUniqueIds", value)

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendRole, "role").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value)

    @builtins.property
    @jsii.member(jsii_name="roleTag")
    def role_tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleTag"))

    @role_tag.setter
    def role_tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendRole, "role_tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleTag", value)

    @builtins.property
    @jsii.member(jsii_name="tokenBoundCidrs")
    def token_bound_cidrs(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tokenBoundCidrs"))

    @token_bound_cidrs.setter
    def token_bound_cidrs(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendRole, "token_bound_cidrs").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenBoundCidrs", value)

    @builtins.property
    @jsii.member(jsii_name="tokenExplicitMaxTtl")
    def token_explicit_max_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tokenExplicitMaxTtl"))

    @token_explicit_max_ttl.setter
    def token_explicit_max_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendRole, "token_explicit_max_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenExplicitMaxTtl", value)

    @builtins.property
    @jsii.member(jsii_name="tokenMaxTtl")
    def token_max_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tokenMaxTtl"))

    @token_max_ttl.setter
    def token_max_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendRole, "token_max_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenMaxTtl", value)

    @builtins.property
    @jsii.member(jsii_name="tokenNoDefaultPolicy")
    def token_no_default_policy(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "tokenNoDefaultPolicy"))

    @token_no_default_policy.setter
    def token_no_default_policy(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendRole, "token_no_default_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenNoDefaultPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="tokenNumUses")
    def token_num_uses(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tokenNumUses"))

    @token_num_uses.setter
    def token_num_uses(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendRole, "token_num_uses").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenNumUses", value)

    @builtins.property
    @jsii.member(jsii_name="tokenPeriod")
    def token_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tokenPeriod"))

    @token_period.setter
    def token_period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendRole, "token_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="tokenPolicies")
    def token_policies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tokenPolicies"))

    @token_policies.setter
    def token_policies(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendRole, "token_policies").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenPolicies", value)

    @builtins.property
    @jsii.member(jsii_name="tokenTtl")
    def token_ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "tokenTtl"))

    @token_ttl.setter
    def token_ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendRole, "token_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenTtl", value)

    @builtins.property
    @jsii.member(jsii_name="tokenType")
    def token_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenType"))

    @token_type.setter
    def token_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendRole, "token_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenType", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.awsAuthBackendRole.AwsAuthBackendRoleConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "role": "role",
        "allow_instance_migration": "allowInstanceMigration",
        "auth_type": "authType",
        "backend": "backend",
        "bound_account_ids": "boundAccountIds",
        "bound_ami_ids": "boundAmiIds",
        "bound_ec2_instance_ids": "boundEc2InstanceIds",
        "bound_iam_instance_profile_arns": "boundIamInstanceProfileArns",
        "bound_iam_principal_arns": "boundIamPrincipalArns",
        "bound_iam_role_arns": "boundIamRoleArns",
        "bound_regions": "boundRegions",
        "bound_subnet_ids": "boundSubnetIds",
        "bound_vpc_ids": "boundVpcIds",
        "disallow_reauthentication": "disallowReauthentication",
        "id": "id",
        "inferred_aws_region": "inferredAwsRegion",
        "inferred_entity_type": "inferredEntityType",
        "namespace": "namespace",
        "resolve_aws_unique_ids": "resolveAwsUniqueIds",
        "role_tag": "roleTag",
        "token_bound_cidrs": "tokenBoundCidrs",
        "token_explicit_max_ttl": "tokenExplicitMaxTtl",
        "token_max_ttl": "tokenMaxTtl",
        "token_no_default_policy": "tokenNoDefaultPolicy",
        "token_num_uses": "tokenNumUses",
        "token_period": "tokenPeriod",
        "token_policies": "tokenPolicies",
        "token_ttl": "tokenTtl",
        "token_type": "tokenType",
    },
)
class AwsAuthBackendRoleConfig(cdktf.TerraformMetaArguments):
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
        role: builtins.str,
        allow_instance_migration: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        auth_type: typing.Optional[builtins.str] = None,
        backend: typing.Optional[builtins.str] = None,
        bound_account_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        bound_ami_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        bound_ec2_instance_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        bound_iam_instance_profile_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        bound_iam_principal_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        bound_iam_role_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        bound_regions: typing.Optional[typing.Sequence[builtins.str]] = None,
        bound_subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        bound_vpc_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        disallow_reauthentication: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        inferred_aws_region: typing.Optional[builtins.str] = None,
        inferred_entity_type: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        resolve_aws_unique_ids: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        role_tag: typing.Optional[builtins.str] = None,
        token_bound_cidrs: typing.Optional[typing.Sequence[builtins.str]] = None,
        token_explicit_max_ttl: typing.Optional[jsii.Number] = None,
        token_max_ttl: typing.Optional[jsii.Number] = None,
        token_no_default_policy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        token_num_uses: typing.Optional[jsii.Number] = None,
        token_period: typing.Optional[jsii.Number] = None,
        token_policies: typing.Optional[typing.Sequence[builtins.str]] = None,
        token_ttl: typing.Optional[jsii.Number] = None,
        token_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param role: Name of the role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#role AwsAuthBackendRole#role}
        :param allow_instance_migration: When true, allows migration of the underlying instance where the client resides. Use with caution. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#allow_instance_migration AwsAuthBackendRole#allow_instance_migration}
        :param auth_type: The auth type permitted for this role. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#auth_type AwsAuthBackendRole#auth_type}
        :param backend: Unique name of the auth backend to configure. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#backend AwsAuthBackendRole#backend}
        :param bound_account_ids: Only EC2 instances with this account ID in their identity document will be permitted to log in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#bound_account_ids AwsAuthBackendRole#bound_account_ids}
        :param bound_ami_ids: Only EC2 instances using this AMI ID will be permitted to log in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#bound_ami_ids AwsAuthBackendRole#bound_ami_ids}
        :param bound_ec2_instance_ids: Only EC2 instances that match this instance ID will be permitted to log in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#bound_ec2_instance_ids AwsAuthBackendRole#bound_ec2_instance_ids}
        :param bound_iam_instance_profile_arns: Only EC2 instances associated with an IAM instance profile ARN that matches this value will be permitted to log in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#bound_iam_instance_profile_arns AwsAuthBackendRole#bound_iam_instance_profile_arns}
        :param bound_iam_principal_arns: The IAM principal that must be authenticated using the iam auth method. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#bound_iam_principal_arns AwsAuthBackendRole#bound_iam_principal_arns}
        :param bound_iam_role_arns: Only EC2 instances that match this IAM role ARN will be permitted to log in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#bound_iam_role_arns AwsAuthBackendRole#bound_iam_role_arns}
        :param bound_regions: Only EC2 instances in this region will be permitted to log in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#bound_regions AwsAuthBackendRole#bound_regions}
        :param bound_subnet_ids: Only EC2 instances associated with this subnet ID will be permitted to log in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#bound_subnet_ids AwsAuthBackendRole#bound_subnet_ids}
        :param bound_vpc_ids: Only EC2 instances associated with this VPC ID will be permitted to log in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#bound_vpc_ids AwsAuthBackendRole#bound_vpc_ids}
        :param disallow_reauthentication: When true, only allows a single token to be granted per instance ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#disallow_reauthentication AwsAuthBackendRole#disallow_reauthentication}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#id AwsAuthBackendRole#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param inferred_aws_region: The region to search for the inferred entities in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#inferred_aws_region AwsAuthBackendRole#inferred_aws_region}
        :param inferred_entity_type: The type of inferencing Vault should do. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#inferred_entity_type AwsAuthBackendRole#inferred_entity_type}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#namespace AwsAuthBackendRole#namespace}
        :param resolve_aws_unique_ids: Whether or not Vault should resolve the bound_iam_principal_arn to an AWS Unique ID. When true, deleting a principal and recreating it with the same name won't automatically grant the new principal the same roles in Vault that the old principal had. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#resolve_aws_unique_ids AwsAuthBackendRole#resolve_aws_unique_ids}
        :param role_tag: The key of the tag on EC2 instance to use for role tags. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#role_tag AwsAuthBackendRole#role_tag}
        :param token_bound_cidrs: Specifies the blocks of IP addresses which are allowed to use the generated token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#token_bound_cidrs AwsAuthBackendRole#token_bound_cidrs}
        :param token_explicit_max_ttl: Generated Token's Explicit Maximum TTL in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#token_explicit_max_ttl AwsAuthBackendRole#token_explicit_max_ttl}
        :param token_max_ttl: The maximum lifetime of the generated token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#token_max_ttl AwsAuthBackendRole#token_max_ttl}
        :param token_no_default_policy: If true, the 'default' policy will not automatically be added to generated tokens. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#token_no_default_policy AwsAuthBackendRole#token_no_default_policy}
        :param token_num_uses: The maximum number of times a token may be used, a value of zero means unlimited. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#token_num_uses AwsAuthBackendRole#token_num_uses}
        :param token_period: Generated Token's Period. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#token_period AwsAuthBackendRole#token_period}
        :param token_policies: Generated Token's Policies. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#token_policies AwsAuthBackendRole#token_policies}
        :param token_ttl: The initial ttl of the token to generate in seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#token_ttl AwsAuthBackendRole#token_ttl}
        :param token_type: The type of token to generate, service or batch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#token_type AwsAuthBackendRole#token_type}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(AwsAuthBackendRoleConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument allow_instance_migration", value=allow_instance_migration, expected_type=type_hints["allow_instance_migration"])
            check_type(argname="argument auth_type", value=auth_type, expected_type=type_hints["auth_type"])
            check_type(argname="argument backend", value=backend, expected_type=type_hints["backend"])
            check_type(argname="argument bound_account_ids", value=bound_account_ids, expected_type=type_hints["bound_account_ids"])
            check_type(argname="argument bound_ami_ids", value=bound_ami_ids, expected_type=type_hints["bound_ami_ids"])
            check_type(argname="argument bound_ec2_instance_ids", value=bound_ec2_instance_ids, expected_type=type_hints["bound_ec2_instance_ids"])
            check_type(argname="argument bound_iam_instance_profile_arns", value=bound_iam_instance_profile_arns, expected_type=type_hints["bound_iam_instance_profile_arns"])
            check_type(argname="argument bound_iam_principal_arns", value=bound_iam_principal_arns, expected_type=type_hints["bound_iam_principal_arns"])
            check_type(argname="argument bound_iam_role_arns", value=bound_iam_role_arns, expected_type=type_hints["bound_iam_role_arns"])
            check_type(argname="argument bound_regions", value=bound_regions, expected_type=type_hints["bound_regions"])
            check_type(argname="argument bound_subnet_ids", value=bound_subnet_ids, expected_type=type_hints["bound_subnet_ids"])
            check_type(argname="argument bound_vpc_ids", value=bound_vpc_ids, expected_type=type_hints["bound_vpc_ids"])
            check_type(argname="argument disallow_reauthentication", value=disallow_reauthentication, expected_type=type_hints["disallow_reauthentication"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument inferred_aws_region", value=inferred_aws_region, expected_type=type_hints["inferred_aws_region"])
            check_type(argname="argument inferred_entity_type", value=inferred_entity_type, expected_type=type_hints["inferred_entity_type"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument resolve_aws_unique_ids", value=resolve_aws_unique_ids, expected_type=type_hints["resolve_aws_unique_ids"])
            check_type(argname="argument role_tag", value=role_tag, expected_type=type_hints["role_tag"])
            check_type(argname="argument token_bound_cidrs", value=token_bound_cidrs, expected_type=type_hints["token_bound_cidrs"])
            check_type(argname="argument token_explicit_max_ttl", value=token_explicit_max_ttl, expected_type=type_hints["token_explicit_max_ttl"])
            check_type(argname="argument token_max_ttl", value=token_max_ttl, expected_type=type_hints["token_max_ttl"])
            check_type(argname="argument token_no_default_policy", value=token_no_default_policy, expected_type=type_hints["token_no_default_policy"])
            check_type(argname="argument token_num_uses", value=token_num_uses, expected_type=type_hints["token_num_uses"])
            check_type(argname="argument token_period", value=token_period, expected_type=type_hints["token_period"])
            check_type(argname="argument token_policies", value=token_policies, expected_type=type_hints["token_policies"])
            check_type(argname="argument token_ttl", value=token_ttl, expected_type=type_hints["token_ttl"])
            check_type(argname="argument token_type", value=token_type, expected_type=type_hints["token_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "role": role,
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
        if allow_instance_migration is not None:
            self._values["allow_instance_migration"] = allow_instance_migration
        if auth_type is not None:
            self._values["auth_type"] = auth_type
        if backend is not None:
            self._values["backend"] = backend
        if bound_account_ids is not None:
            self._values["bound_account_ids"] = bound_account_ids
        if bound_ami_ids is not None:
            self._values["bound_ami_ids"] = bound_ami_ids
        if bound_ec2_instance_ids is not None:
            self._values["bound_ec2_instance_ids"] = bound_ec2_instance_ids
        if bound_iam_instance_profile_arns is not None:
            self._values["bound_iam_instance_profile_arns"] = bound_iam_instance_profile_arns
        if bound_iam_principal_arns is not None:
            self._values["bound_iam_principal_arns"] = bound_iam_principal_arns
        if bound_iam_role_arns is not None:
            self._values["bound_iam_role_arns"] = bound_iam_role_arns
        if bound_regions is not None:
            self._values["bound_regions"] = bound_regions
        if bound_subnet_ids is not None:
            self._values["bound_subnet_ids"] = bound_subnet_ids
        if bound_vpc_ids is not None:
            self._values["bound_vpc_ids"] = bound_vpc_ids
        if disallow_reauthentication is not None:
            self._values["disallow_reauthentication"] = disallow_reauthentication
        if id is not None:
            self._values["id"] = id
        if inferred_aws_region is not None:
            self._values["inferred_aws_region"] = inferred_aws_region
        if inferred_entity_type is not None:
            self._values["inferred_entity_type"] = inferred_entity_type
        if namespace is not None:
            self._values["namespace"] = namespace
        if resolve_aws_unique_ids is not None:
            self._values["resolve_aws_unique_ids"] = resolve_aws_unique_ids
        if role_tag is not None:
            self._values["role_tag"] = role_tag
        if token_bound_cidrs is not None:
            self._values["token_bound_cidrs"] = token_bound_cidrs
        if token_explicit_max_ttl is not None:
            self._values["token_explicit_max_ttl"] = token_explicit_max_ttl
        if token_max_ttl is not None:
            self._values["token_max_ttl"] = token_max_ttl
        if token_no_default_policy is not None:
            self._values["token_no_default_policy"] = token_no_default_policy
        if token_num_uses is not None:
            self._values["token_num_uses"] = token_num_uses
        if token_period is not None:
            self._values["token_period"] = token_period
        if token_policies is not None:
            self._values["token_policies"] = token_policies
        if token_ttl is not None:
            self._values["token_ttl"] = token_ttl
        if token_type is not None:
            self._values["token_type"] = token_type

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
    def role(self) -> builtins.str:
        '''Name of the role.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#role AwsAuthBackendRole#role}
        '''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_instance_migration(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''When true, allows migration of the underlying instance where the client resides. Use with caution.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#allow_instance_migration AwsAuthBackendRole#allow_instance_migration}
        '''
        result = self._values.get("allow_instance_migration")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def auth_type(self) -> typing.Optional[builtins.str]:
        '''The auth type permitted for this role.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#auth_type AwsAuthBackendRole#auth_type}
        '''
        result = self._values.get("auth_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def backend(self) -> typing.Optional[builtins.str]:
        '''Unique name of the auth backend to configure.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#backend AwsAuthBackendRole#backend}
        '''
        result = self._values.get("backend")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def bound_account_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Only EC2 instances with this account ID in their identity document will be permitted to log in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#bound_account_ids AwsAuthBackendRole#bound_account_ids}
        '''
        result = self._values.get("bound_account_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def bound_ami_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Only EC2 instances using this AMI ID will be permitted to log in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#bound_ami_ids AwsAuthBackendRole#bound_ami_ids}
        '''
        result = self._values.get("bound_ami_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def bound_ec2_instance_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Only EC2 instances that match this instance ID will be permitted to log in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#bound_ec2_instance_ids AwsAuthBackendRole#bound_ec2_instance_ids}
        '''
        result = self._values.get("bound_ec2_instance_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def bound_iam_instance_profile_arns(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        '''Only EC2 instances associated with an IAM instance profile ARN that matches this value will be permitted to log in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#bound_iam_instance_profile_arns AwsAuthBackendRole#bound_iam_instance_profile_arns}
        '''
        result = self._values.get("bound_iam_instance_profile_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def bound_iam_principal_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The IAM principal that must be authenticated using the iam auth method.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#bound_iam_principal_arns AwsAuthBackendRole#bound_iam_principal_arns}
        '''
        result = self._values.get("bound_iam_principal_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def bound_iam_role_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Only EC2 instances that match this IAM role ARN will be permitted to log in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#bound_iam_role_arns AwsAuthBackendRole#bound_iam_role_arns}
        '''
        result = self._values.get("bound_iam_role_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def bound_regions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Only EC2 instances in this region will be permitted to log in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#bound_regions AwsAuthBackendRole#bound_regions}
        '''
        result = self._values.get("bound_regions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def bound_subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Only EC2 instances associated with this subnet ID will be permitted to log in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#bound_subnet_ids AwsAuthBackendRole#bound_subnet_ids}
        '''
        result = self._values.get("bound_subnet_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def bound_vpc_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Only EC2 instances associated with this VPC ID will be permitted to log in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#bound_vpc_ids AwsAuthBackendRole#bound_vpc_ids}
        '''
        result = self._values.get("bound_vpc_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def disallow_reauthentication(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''When true, only allows a single token to be granted per instance ID.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#disallow_reauthentication AwsAuthBackendRole#disallow_reauthentication}
        '''
        result = self._values.get("disallow_reauthentication")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#id AwsAuthBackendRole#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def inferred_aws_region(self) -> typing.Optional[builtins.str]:
        '''The region to search for the inferred entities in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#inferred_aws_region AwsAuthBackendRole#inferred_aws_region}
        '''
        result = self._values.get("inferred_aws_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def inferred_entity_type(self) -> typing.Optional[builtins.str]:
        '''The type of inferencing Vault should do.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#inferred_entity_type AwsAuthBackendRole#inferred_entity_type}
        '''
        result = self._values.get("inferred_entity_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Target namespace. (requires Enterprise).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#namespace AwsAuthBackendRole#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resolve_aws_unique_ids(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether or not Vault should resolve the bound_iam_principal_arn to an AWS Unique ID.

        When true, deleting a principal and recreating it with the same name won't automatically grant the new principal the same roles in Vault that the old principal had.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#resolve_aws_unique_ids AwsAuthBackendRole#resolve_aws_unique_ids}
        '''
        result = self._values.get("resolve_aws_unique_ids")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def role_tag(self) -> typing.Optional[builtins.str]:
        '''The key of the tag on EC2 instance to use for role tags.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#role_tag AwsAuthBackendRole#role_tag}
        '''
        result = self._values.get("role_tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_bound_cidrs(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the blocks of IP addresses which are allowed to use the generated token.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#token_bound_cidrs AwsAuthBackendRole#token_bound_cidrs}
        '''
        result = self._values.get("token_bound_cidrs")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def token_explicit_max_ttl(self) -> typing.Optional[jsii.Number]:
        '''Generated Token's Explicit Maximum TTL in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#token_explicit_max_ttl AwsAuthBackendRole#token_explicit_max_ttl}
        '''
        result = self._values.get("token_explicit_max_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def token_max_ttl(self) -> typing.Optional[jsii.Number]:
        '''The maximum lifetime of the generated token.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#token_max_ttl AwsAuthBackendRole#token_max_ttl}
        '''
        result = self._values.get("token_max_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def token_no_default_policy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, the 'default' policy will not automatically be added to generated tokens.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#token_no_default_policy AwsAuthBackendRole#token_no_default_policy}
        '''
        result = self._values.get("token_no_default_policy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def token_num_uses(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of times a token may be used, a value of zero means unlimited.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#token_num_uses AwsAuthBackendRole#token_num_uses}
        '''
        result = self._values.get("token_num_uses")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def token_period(self) -> typing.Optional[jsii.Number]:
        '''Generated Token's Period.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#token_period AwsAuthBackendRole#token_period}
        '''
        result = self._values.get("token_period")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def token_policies(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Generated Token's Policies.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#token_policies AwsAuthBackendRole#token_policies}
        '''
        result = self._values.get("token_policies")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def token_ttl(self) -> typing.Optional[jsii.Number]:
        '''The initial ttl of the token to generate in seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#token_ttl AwsAuthBackendRole#token_ttl}
        '''
        result = self._values.get("token_ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def token_type(self) -> typing.Optional[builtins.str]:
        '''The type of token to generate, service or batch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_role#token_type AwsAuthBackendRole#token_type}
        '''
        result = self._values.get("token_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsAuthBackendRoleConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AwsAuthBackendRole",
    "AwsAuthBackendRoleConfig",
]

publication.publish()
