'''
# `databricks_metastore_data_access`

Refer to the Terraform Registory for docs: [`databricks_metastore_data_access`](https://www.terraform.io/docs/providers/databricks/r/metastore_data_access).
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


class MetastoreDataAccess(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.metastoreDataAccess.MetastoreDataAccess",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access databricks_metastore_data_access}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        metastore_id: builtins.str,
        name: builtins.str,
        aws_iam_role: typing.Optional[typing.Union["MetastoreDataAccessAwsIamRole", typing.Dict[str, typing.Any]]] = None,
        azure_managed_identity: typing.Optional[typing.Union["MetastoreDataAccessAzureManagedIdentity", typing.Dict[str, typing.Any]]] = None,
        azure_service_principal: typing.Optional[typing.Union["MetastoreDataAccessAzureServicePrincipal", typing.Dict[str, typing.Any]]] = None,
        configuration_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        is_default: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access databricks_metastore_data_access} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param metastore_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#metastore_id MetastoreDataAccess#metastore_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#name MetastoreDataAccess#name}.
        :param aws_iam_role: aws_iam_role block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#aws_iam_role MetastoreDataAccess#aws_iam_role}
        :param azure_managed_identity: azure_managed_identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#azure_managed_identity MetastoreDataAccess#azure_managed_identity}
        :param azure_service_principal: azure_service_principal block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#azure_service_principal MetastoreDataAccess#azure_service_principal}
        :param configuration_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#configuration_type MetastoreDataAccess#configuration_type}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#id MetastoreDataAccess#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#is_default MetastoreDataAccess#is_default}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MetastoreDataAccess.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = MetastoreDataAccessConfig(
            metastore_id=metastore_id,
            name=name,
            aws_iam_role=aws_iam_role,
            azure_managed_identity=azure_managed_identity,
            azure_service_principal=azure_service_principal,
            configuration_type=configuration_type,
            id=id,
            is_default=is_default,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAwsIamRole")
    def put_aws_iam_role(self, *, role_arn: builtins.str) -> None:
        '''
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#role_arn MetastoreDataAccess#role_arn}.
        '''
        value = MetastoreDataAccessAwsIamRole(role_arn=role_arn)

        return typing.cast(None, jsii.invoke(self, "putAwsIamRole", [value]))

    @jsii.member(jsii_name="putAzureManagedIdentity")
    def put_azure_managed_identity(self, *, access_connector_id: builtins.str) -> None:
        '''
        :param access_connector_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#access_connector_id MetastoreDataAccess#access_connector_id}.
        '''
        value = MetastoreDataAccessAzureManagedIdentity(
            access_connector_id=access_connector_id
        )

        return typing.cast(None, jsii.invoke(self, "putAzureManagedIdentity", [value]))

    @jsii.member(jsii_name="putAzureServicePrincipal")
    def put_azure_service_principal(
        self,
        *,
        application_id: builtins.str,
        client_secret: builtins.str,
        directory_id: builtins.str,
    ) -> None:
        '''
        :param application_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#application_id MetastoreDataAccess#application_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#client_secret MetastoreDataAccess#client_secret}.
        :param directory_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#directory_id MetastoreDataAccess#directory_id}.
        '''
        value = MetastoreDataAccessAzureServicePrincipal(
            application_id=application_id,
            client_secret=client_secret,
            directory_id=directory_id,
        )

        return typing.cast(None, jsii.invoke(self, "putAzureServicePrincipal", [value]))

    @jsii.member(jsii_name="resetAwsIamRole")
    def reset_aws_iam_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsIamRole", []))

    @jsii.member(jsii_name="resetAzureManagedIdentity")
    def reset_azure_managed_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureManagedIdentity", []))

    @jsii.member(jsii_name="resetAzureServicePrincipal")
    def reset_azure_service_principal(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureServicePrincipal", []))

    @jsii.member(jsii_name="resetConfigurationType")
    def reset_configuration_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConfigurationType", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIsDefault")
    def reset_is_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsDefault", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="awsIamRole")
    def aws_iam_role(self) -> "MetastoreDataAccessAwsIamRoleOutputReference":
        return typing.cast("MetastoreDataAccessAwsIamRoleOutputReference", jsii.get(self, "awsIamRole"))

    @builtins.property
    @jsii.member(jsii_name="azureManagedIdentity")
    def azure_managed_identity(
        self,
    ) -> "MetastoreDataAccessAzureManagedIdentityOutputReference":
        return typing.cast("MetastoreDataAccessAzureManagedIdentityOutputReference", jsii.get(self, "azureManagedIdentity"))

    @builtins.property
    @jsii.member(jsii_name="azureServicePrincipal")
    def azure_service_principal(
        self,
    ) -> "MetastoreDataAccessAzureServicePrincipalOutputReference":
        return typing.cast("MetastoreDataAccessAzureServicePrincipalOutputReference", jsii.get(self, "azureServicePrincipal"))

    @builtins.property
    @jsii.member(jsii_name="awsIamRoleInput")
    def aws_iam_role_input(self) -> typing.Optional["MetastoreDataAccessAwsIamRole"]:
        return typing.cast(typing.Optional["MetastoreDataAccessAwsIamRole"], jsii.get(self, "awsIamRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="azureManagedIdentityInput")
    def azure_managed_identity_input(
        self,
    ) -> typing.Optional["MetastoreDataAccessAzureManagedIdentity"]:
        return typing.cast(typing.Optional["MetastoreDataAccessAzureManagedIdentity"], jsii.get(self, "azureManagedIdentityInput"))

    @builtins.property
    @jsii.member(jsii_name="azureServicePrincipalInput")
    def azure_service_principal_input(
        self,
    ) -> typing.Optional["MetastoreDataAccessAzureServicePrincipal"]:
        return typing.cast(typing.Optional["MetastoreDataAccessAzureServicePrincipal"], jsii.get(self, "azureServicePrincipalInput"))

    @builtins.property
    @jsii.member(jsii_name="configurationTypeInput")
    def configuration_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configurationTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="isDefaultInput")
    def is_default_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isDefaultInput"))

    @builtins.property
    @jsii.member(jsii_name="metastoreIdInput")
    def metastore_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metastoreIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="configurationType")
    def configuration_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configurationType"))

    @configuration_type.setter
    def configuration_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MetastoreDataAccess, "configuration_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationType", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MetastoreDataAccess, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="isDefault")
    def is_default(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isDefault"))

    @is_default.setter
    def is_default(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MetastoreDataAccess, "is_default").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isDefault", value)

    @builtins.property
    @jsii.member(jsii_name="metastoreId")
    def metastore_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metastoreId"))

    @metastore_id.setter
    def metastore_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MetastoreDataAccess, "metastore_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metastoreId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MetastoreDataAccess, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.metastoreDataAccess.MetastoreDataAccessAwsIamRole",
    jsii_struct_bases=[],
    name_mapping={"role_arn": "roleArn"},
)
class MetastoreDataAccessAwsIamRole:
    def __init__(self, *, role_arn: builtins.str) -> None:
        '''
        :param role_arn: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#role_arn MetastoreDataAccess#role_arn}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MetastoreDataAccessAwsIamRole.__init__)
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
        self._values: typing.Dict[str, typing.Any] = {
            "role_arn": role_arn,
        }

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#role_arn MetastoreDataAccess#role_arn}.'''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetastoreDataAccessAwsIamRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MetastoreDataAccessAwsIamRoleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.metastoreDataAccess.MetastoreDataAccessAwsIamRoleOutputReference",
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
            type_hints = typing.get_type_hints(MetastoreDataAccessAwsIamRoleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="roleArnInput")
    def role_arn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleArnInput"))

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MetastoreDataAccessAwsIamRoleOutputReference, "role_arn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[MetastoreDataAccessAwsIamRole]:
        return typing.cast(typing.Optional[MetastoreDataAccessAwsIamRole], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MetastoreDataAccessAwsIamRole],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MetastoreDataAccessAwsIamRoleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.metastoreDataAccess.MetastoreDataAccessAzureManagedIdentity",
    jsii_struct_bases=[],
    name_mapping={"access_connector_id": "accessConnectorId"},
)
class MetastoreDataAccessAzureManagedIdentity:
    def __init__(self, *, access_connector_id: builtins.str) -> None:
        '''
        :param access_connector_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#access_connector_id MetastoreDataAccess#access_connector_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MetastoreDataAccessAzureManagedIdentity.__init__)
            check_type(argname="argument access_connector_id", value=access_connector_id, expected_type=type_hints["access_connector_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "access_connector_id": access_connector_id,
        }

    @builtins.property
    def access_connector_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#access_connector_id MetastoreDataAccess#access_connector_id}.'''
        result = self._values.get("access_connector_id")
        assert result is not None, "Required property 'access_connector_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetastoreDataAccessAzureManagedIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MetastoreDataAccessAzureManagedIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.metastoreDataAccess.MetastoreDataAccessAzureManagedIdentityOutputReference",
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
            type_hints = typing.get_type_hints(MetastoreDataAccessAzureManagedIdentityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="accessConnectorIdInput")
    def access_connector_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessConnectorIdInput"))

    @builtins.property
    @jsii.member(jsii_name="accessConnectorId")
    def access_connector_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessConnectorId"))

    @access_connector_id.setter
    def access_connector_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MetastoreDataAccessAzureManagedIdentityOutputReference, "access_connector_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessConnectorId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MetastoreDataAccessAzureManagedIdentity]:
        return typing.cast(typing.Optional[MetastoreDataAccessAzureManagedIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MetastoreDataAccessAzureManagedIdentity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MetastoreDataAccessAzureManagedIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.metastoreDataAccess.MetastoreDataAccessAzureServicePrincipal",
    jsii_struct_bases=[],
    name_mapping={
        "application_id": "applicationId",
        "client_secret": "clientSecret",
        "directory_id": "directoryId",
    },
)
class MetastoreDataAccessAzureServicePrincipal:
    def __init__(
        self,
        *,
        application_id: builtins.str,
        client_secret: builtins.str,
        directory_id: builtins.str,
    ) -> None:
        '''
        :param application_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#application_id MetastoreDataAccess#application_id}.
        :param client_secret: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#client_secret MetastoreDataAccess#client_secret}.
        :param directory_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#directory_id MetastoreDataAccess#directory_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(MetastoreDataAccessAzureServicePrincipal.__init__)
            check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument directory_id", value=directory_id, expected_type=type_hints["directory_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "application_id": application_id,
            "client_secret": client_secret,
            "directory_id": directory_id,
        }

    @builtins.property
    def application_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#application_id MetastoreDataAccess#application_id}.'''
        result = self._values.get("application_id")
        assert result is not None, "Required property 'application_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#client_secret MetastoreDataAccess#client_secret}.'''
        result = self._values.get("client_secret")
        assert result is not None, "Required property 'client_secret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def directory_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#directory_id MetastoreDataAccess#directory_id}.'''
        result = self._values.get("directory_id")
        assert result is not None, "Required property 'directory_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetastoreDataAccessAzureServicePrincipal(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class MetastoreDataAccessAzureServicePrincipalOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-databricks.metastoreDataAccess.MetastoreDataAccessAzureServicePrincipalOutputReference",
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
            type_hints = typing.get_type_hints(MetastoreDataAccessAzureServicePrincipalOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="applicationIdInput")
    def application_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="directoryIdInput")
    def directory_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directoryIdInput"))

    @builtins.property
    @jsii.member(jsii_name="applicationId")
    def application_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationId"))

    @application_id.setter
    def application_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MetastoreDataAccessAzureServicePrincipalOutputReference, "application_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MetastoreDataAccessAzureServicePrincipalOutputReference, "client_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="directoryId")
    def directory_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "directoryId"))

    @directory_id.setter
    def directory_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MetastoreDataAccessAzureServicePrincipalOutputReference, "directory_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "directoryId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[MetastoreDataAccessAzureServicePrincipal]:
        return typing.cast(typing.Optional[MetastoreDataAccessAzureServicePrincipal], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[MetastoreDataAccessAzureServicePrincipal],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(MetastoreDataAccessAzureServicePrincipalOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-databricks.metastoreDataAccess.MetastoreDataAccessConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "metastore_id": "metastoreId",
        "name": "name",
        "aws_iam_role": "awsIamRole",
        "azure_managed_identity": "azureManagedIdentity",
        "azure_service_principal": "azureServicePrincipal",
        "configuration_type": "configurationType",
        "id": "id",
        "is_default": "isDefault",
    },
)
class MetastoreDataAccessConfig(cdktf.TerraformMetaArguments):
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
        metastore_id: builtins.str,
        name: builtins.str,
        aws_iam_role: typing.Optional[typing.Union[MetastoreDataAccessAwsIamRole, typing.Dict[str, typing.Any]]] = None,
        azure_managed_identity: typing.Optional[typing.Union[MetastoreDataAccessAzureManagedIdentity, typing.Dict[str, typing.Any]]] = None,
        azure_service_principal: typing.Optional[typing.Union[MetastoreDataAccessAzureServicePrincipal, typing.Dict[str, typing.Any]]] = None,
        configuration_type: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        is_default: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param metastore_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#metastore_id MetastoreDataAccess#metastore_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#name MetastoreDataAccess#name}.
        :param aws_iam_role: aws_iam_role block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#aws_iam_role MetastoreDataAccess#aws_iam_role}
        :param azure_managed_identity: azure_managed_identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#azure_managed_identity MetastoreDataAccess#azure_managed_identity}
        :param azure_service_principal: azure_service_principal block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#azure_service_principal MetastoreDataAccess#azure_service_principal}
        :param configuration_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#configuration_type MetastoreDataAccess#configuration_type}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#id MetastoreDataAccess#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param is_default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#is_default MetastoreDataAccess#is_default}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(aws_iam_role, dict):
            aws_iam_role = MetastoreDataAccessAwsIamRole(**aws_iam_role)
        if isinstance(azure_managed_identity, dict):
            azure_managed_identity = MetastoreDataAccessAzureManagedIdentity(**azure_managed_identity)
        if isinstance(azure_service_principal, dict):
            azure_service_principal = MetastoreDataAccessAzureServicePrincipal(**azure_service_principal)
        if __debug__:
            type_hints = typing.get_type_hints(MetastoreDataAccessConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument metastore_id", value=metastore_id, expected_type=type_hints["metastore_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument aws_iam_role", value=aws_iam_role, expected_type=type_hints["aws_iam_role"])
            check_type(argname="argument azure_managed_identity", value=azure_managed_identity, expected_type=type_hints["azure_managed_identity"])
            check_type(argname="argument azure_service_principal", value=azure_service_principal, expected_type=type_hints["azure_service_principal"])
            check_type(argname="argument configuration_type", value=configuration_type, expected_type=type_hints["configuration_type"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument is_default", value=is_default, expected_type=type_hints["is_default"])
        self._values: typing.Dict[str, typing.Any] = {
            "metastore_id": metastore_id,
            "name": name,
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
        if aws_iam_role is not None:
            self._values["aws_iam_role"] = aws_iam_role
        if azure_managed_identity is not None:
            self._values["azure_managed_identity"] = azure_managed_identity
        if azure_service_principal is not None:
            self._values["azure_service_principal"] = azure_service_principal
        if configuration_type is not None:
            self._values["configuration_type"] = configuration_type
        if id is not None:
            self._values["id"] = id
        if is_default is not None:
            self._values["is_default"] = is_default

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
    def metastore_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#metastore_id MetastoreDataAccess#metastore_id}.'''
        result = self._values.get("metastore_id")
        assert result is not None, "Required property 'metastore_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#name MetastoreDataAccess#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def aws_iam_role(self) -> typing.Optional[MetastoreDataAccessAwsIamRole]:
        '''aws_iam_role block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#aws_iam_role MetastoreDataAccess#aws_iam_role}
        '''
        result = self._values.get("aws_iam_role")
        return typing.cast(typing.Optional[MetastoreDataAccessAwsIamRole], result)

    @builtins.property
    def azure_managed_identity(
        self,
    ) -> typing.Optional[MetastoreDataAccessAzureManagedIdentity]:
        '''azure_managed_identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#azure_managed_identity MetastoreDataAccess#azure_managed_identity}
        '''
        result = self._values.get("azure_managed_identity")
        return typing.cast(typing.Optional[MetastoreDataAccessAzureManagedIdentity], result)

    @builtins.property
    def azure_service_principal(
        self,
    ) -> typing.Optional[MetastoreDataAccessAzureServicePrincipal]:
        '''azure_service_principal block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#azure_service_principal MetastoreDataAccess#azure_service_principal}
        '''
        result = self._values.get("azure_service_principal")
        return typing.cast(typing.Optional[MetastoreDataAccessAzureServicePrincipal], result)

    @builtins.property
    def configuration_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#configuration_type MetastoreDataAccess#configuration_type}.'''
        result = self._values.get("configuration_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#id MetastoreDataAccess#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def is_default(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/databricks/r/metastore_data_access#is_default MetastoreDataAccess#is_default}.'''
        result = self._values.get("is_default")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MetastoreDataAccessConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "MetastoreDataAccess",
    "MetastoreDataAccessAwsIamRole",
    "MetastoreDataAccessAwsIamRoleOutputReference",
    "MetastoreDataAccessAzureManagedIdentity",
    "MetastoreDataAccessAzureManagedIdentityOutputReference",
    "MetastoreDataAccessAzureServicePrincipal",
    "MetastoreDataAccessAzureServicePrincipalOutputReference",
    "MetastoreDataAccessConfig",
]

publication.publish()
