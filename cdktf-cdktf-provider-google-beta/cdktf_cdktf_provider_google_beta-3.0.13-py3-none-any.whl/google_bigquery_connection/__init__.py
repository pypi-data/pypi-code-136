'''
# `google_bigquery_connection`

Refer to the Terraform Registory for docs: [`google_bigquery_connection`](https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection).
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


class GoogleBigqueryConnection(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryConnection.GoogleBigqueryConnection",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection google_bigquery_connection}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        aws: typing.Optional[typing.Union["GoogleBigqueryConnectionAws", typing.Dict[str, typing.Any]]] = None,
        azure: typing.Optional[typing.Union["GoogleBigqueryConnectionAzure", typing.Dict[str, typing.Any]]] = None,
        cloud_resource: typing.Optional[typing.Union["GoogleBigqueryConnectionCloudResource", typing.Dict[str, typing.Any]]] = None,
        cloud_spanner: typing.Optional[typing.Union["GoogleBigqueryConnectionCloudSpanner", typing.Dict[str, typing.Any]]] = None,
        cloud_sql: typing.Optional[typing.Union["GoogleBigqueryConnectionCloudSql", typing.Dict[str, typing.Any]]] = None,
        connection_id: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        friendly_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleBigqueryConnectionTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection google_bigquery_connection} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param aws: aws block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#aws GoogleBigqueryConnection#aws}
        :param azure: azure block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#azure GoogleBigqueryConnection#azure}
        :param cloud_resource: cloud_resource block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#cloud_resource GoogleBigqueryConnection#cloud_resource}
        :param cloud_spanner: cloud_spanner block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#cloud_spanner GoogleBigqueryConnection#cloud_spanner}
        :param cloud_sql: cloud_sql block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#cloud_sql GoogleBigqueryConnection#cloud_sql}
        :param connection_id: Optional connection id that should be assigned to the created connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#connection_id GoogleBigqueryConnection#connection_id}
        :param description: A descriptive description for the connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#description GoogleBigqueryConnection#description}
        :param friendly_name: A descriptive name for the connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#friendly_name GoogleBigqueryConnection#friendly_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#id GoogleBigqueryConnection#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param location: The geographic location where the connection should reside. Cloud SQL instance must be in the same location as the connection with following exceptions: Cloud SQL us-central1 maps to BigQuery US, Cloud SQL europe-west1 maps to BigQuery EU. Examples: US, EU, asia-northeast1, us-central1, europe-west1. Spanner Connections same as spanner region AWS allowed regions are aws-us-east-1 Azure allowed regions are azure-eastus2 Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#location GoogleBigqueryConnection#location}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#project GoogleBigqueryConnection#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#timeouts GoogleBigqueryConnection#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryConnection.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleBigqueryConnectionConfig(
            aws=aws,
            azure=azure,
            cloud_resource=cloud_resource,
            cloud_spanner=cloud_spanner,
            cloud_sql=cloud_sql,
            connection_id=connection_id,
            description=description,
            friendly_name=friendly_name,
            id=id,
            location=location,
            project=project,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAws")
    def put_aws(
        self,
        *,
        access_role: typing.Union["GoogleBigqueryConnectionAwsAccessRole", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param access_role: access_role block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#access_role GoogleBigqueryConnection#access_role}
        '''
        value = GoogleBigqueryConnectionAws(access_role=access_role)

        return typing.cast(None, jsii.invoke(self, "putAws", [value]))

    @jsii.member(jsii_name="putAzure")
    def put_azure(self, *, customer_tenant_id: builtins.str) -> None:
        '''
        :param customer_tenant_id: The id of customer's directory that host the data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#customer_tenant_id GoogleBigqueryConnection#customer_tenant_id}
        '''
        value = GoogleBigqueryConnectionAzure(customer_tenant_id=customer_tenant_id)

        return typing.cast(None, jsii.invoke(self, "putAzure", [value]))

    @jsii.member(jsii_name="putCloudResource")
    def put_cloud_resource(self) -> None:
        value = GoogleBigqueryConnectionCloudResource()

        return typing.cast(None, jsii.invoke(self, "putCloudResource", [value]))

    @jsii.member(jsii_name="putCloudSpanner")
    def put_cloud_spanner(
        self,
        *,
        database: builtins.str,
        use_parallelism: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param database: Cloud Spanner database in the form 'project/instance/database'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#database GoogleBigqueryConnection#database}
        :param use_parallelism: If parallelism should be used when reading from Cloud Spanner. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#use_parallelism GoogleBigqueryConnection#use_parallelism}
        '''
        value = GoogleBigqueryConnectionCloudSpanner(
            database=database, use_parallelism=use_parallelism
        )

        return typing.cast(None, jsii.invoke(self, "putCloudSpanner", [value]))

    @jsii.member(jsii_name="putCloudSql")
    def put_cloud_sql(
        self,
        *,
        credential: typing.Union["GoogleBigqueryConnectionCloudSqlCredential", typing.Dict[str, typing.Any]],
        database: builtins.str,
        instance_id: builtins.str,
        type: builtins.str,
    ) -> None:
        '''
        :param credential: credential block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#credential GoogleBigqueryConnection#credential}
        :param database: Database name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#database GoogleBigqueryConnection#database}
        :param instance_id: Cloud SQL instance ID in the form project:location:instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#instance_id GoogleBigqueryConnection#instance_id}
        :param type: Type of the Cloud SQL database. Possible values: ["DATABASE_TYPE_UNSPECIFIED", "POSTGRES", "MYSQL"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#type GoogleBigqueryConnection#type}
        '''
        value = GoogleBigqueryConnectionCloudSql(
            credential=credential,
            database=database,
            instance_id=instance_id,
            type=type,
        )

        return typing.cast(None, jsii.invoke(self, "putCloudSql", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#create GoogleBigqueryConnection#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#delete GoogleBigqueryConnection#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#update GoogleBigqueryConnection#update}.
        '''
        value = GoogleBigqueryConnectionTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAws")
    def reset_aws(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAws", []))

    @jsii.member(jsii_name="resetAzure")
    def reset_azure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzure", []))

    @jsii.member(jsii_name="resetCloudResource")
    def reset_cloud_resource(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudResource", []))

    @jsii.member(jsii_name="resetCloudSpanner")
    def reset_cloud_spanner(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudSpanner", []))

    @jsii.member(jsii_name="resetCloudSql")
    def reset_cloud_sql(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudSql", []))

    @jsii.member(jsii_name="resetConnectionId")
    def reset_connection_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionId", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetFriendlyName")
    def reset_friendly_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFriendlyName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="aws")
    def aws(self) -> "GoogleBigqueryConnectionAwsOutputReference":
        return typing.cast("GoogleBigqueryConnectionAwsOutputReference", jsii.get(self, "aws"))

    @builtins.property
    @jsii.member(jsii_name="azure")
    def azure(self) -> "GoogleBigqueryConnectionAzureOutputReference":
        return typing.cast("GoogleBigqueryConnectionAzureOutputReference", jsii.get(self, "azure"))

    @builtins.property
    @jsii.member(jsii_name="cloudResource")
    def cloud_resource(self) -> "GoogleBigqueryConnectionCloudResourceOutputReference":
        return typing.cast("GoogleBigqueryConnectionCloudResourceOutputReference", jsii.get(self, "cloudResource"))

    @builtins.property
    @jsii.member(jsii_name="cloudSpanner")
    def cloud_spanner(self) -> "GoogleBigqueryConnectionCloudSpannerOutputReference":
        return typing.cast("GoogleBigqueryConnectionCloudSpannerOutputReference", jsii.get(self, "cloudSpanner"))

    @builtins.property
    @jsii.member(jsii_name="cloudSql")
    def cloud_sql(self) -> "GoogleBigqueryConnectionCloudSqlOutputReference":
        return typing.cast("GoogleBigqueryConnectionCloudSqlOutputReference", jsii.get(self, "cloudSql"))

    @builtins.property
    @jsii.member(jsii_name="hasCredential")
    def has_credential(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "hasCredential"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleBigqueryConnectionTimeoutsOutputReference":
        return typing.cast("GoogleBigqueryConnectionTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="awsInput")
    def aws_input(self) -> typing.Optional["GoogleBigqueryConnectionAws"]:
        return typing.cast(typing.Optional["GoogleBigqueryConnectionAws"], jsii.get(self, "awsInput"))

    @builtins.property
    @jsii.member(jsii_name="azureInput")
    def azure_input(self) -> typing.Optional["GoogleBigqueryConnectionAzure"]:
        return typing.cast(typing.Optional["GoogleBigqueryConnectionAzure"], jsii.get(self, "azureInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudResourceInput")
    def cloud_resource_input(
        self,
    ) -> typing.Optional["GoogleBigqueryConnectionCloudResource"]:
        return typing.cast(typing.Optional["GoogleBigqueryConnectionCloudResource"], jsii.get(self, "cloudResourceInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudSpannerInput")
    def cloud_spanner_input(
        self,
    ) -> typing.Optional["GoogleBigqueryConnectionCloudSpanner"]:
        return typing.cast(typing.Optional["GoogleBigqueryConnectionCloudSpanner"], jsii.get(self, "cloudSpannerInput"))

    @builtins.property
    @jsii.member(jsii_name="cloudSqlInput")
    def cloud_sql_input(self) -> typing.Optional["GoogleBigqueryConnectionCloudSql"]:
        return typing.cast(typing.Optional["GoogleBigqueryConnectionCloudSql"], jsii.get(self, "cloudSqlInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionIdInput")
    def connection_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="friendlyNameInput")
    def friendly_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "friendlyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleBigqueryConnectionTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleBigqueryConnectionTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionId")
    def connection_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionId"))

    @connection_id.setter
    def connection_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryConnection, "connection_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryConnection, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="friendlyName")
    def friendly_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "friendlyName"))

    @friendly_name.setter
    def friendly_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryConnection, "friendly_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "friendlyName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryConnection, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryConnection, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryConnection, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryConnection.GoogleBigqueryConnectionAws",
    jsii_struct_bases=[],
    name_mapping={"access_role": "accessRole"},
)
class GoogleBigqueryConnectionAws:
    def __init__(
        self,
        *,
        access_role: typing.Union["GoogleBigqueryConnectionAwsAccessRole", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param access_role: access_role block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#access_role GoogleBigqueryConnection#access_role}
        '''
        if isinstance(access_role, dict):
            access_role = GoogleBigqueryConnectionAwsAccessRole(**access_role)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryConnectionAws.__init__)
            check_type(argname="argument access_role", value=access_role, expected_type=type_hints["access_role"])
        self._values: typing.Dict[str, typing.Any] = {
            "access_role": access_role,
        }

    @builtins.property
    def access_role(self) -> "GoogleBigqueryConnectionAwsAccessRole":
        '''access_role block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#access_role GoogleBigqueryConnection#access_role}
        '''
        result = self._values.get("access_role")
        assert result is not None, "Required property 'access_role' is missing"
        return typing.cast("GoogleBigqueryConnectionAwsAccessRole", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryConnectionAws(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryConnection.GoogleBigqueryConnectionAwsAccessRole",
    jsii_struct_bases=[],
    name_mapping={"iam_role_id": "iamRoleId"},
)
class GoogleBigqueryConnectionAwsAccessRole:
    def __init__(self, *, iam_role_id: builtins.str) -> None:
        '''
        :param iam_role_id: The user’s AWS IAM Role that trusts the Google-owned AWS IAM user Connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#iam_role_id GoogleBigqueryConnection#iam_role_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryConnectionAwsAccessRole.__init__)
            check_type(argname="argument iam_role_id", value=iam_role_id, expected_type=type_hints["iam_role_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "iam_role_id": iam_role_id,
        }

    @builtins.property
    def iam_role_id(self) -> builtins.str:
        '''The user’s AWS IAM Role that trusts the Google-owned AWS IAM user Connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#iam_role_id GoogleBigqueryConnection#iam_role_id}
        '''
        result = self._values.get("iam_role_id")
        assert result is not None, "Required property 'iam_role_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryConnectionAwsAccessRole(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryConnectionAwsAccessRoleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryConnection.GoogleBigqueryConnectionAwsAccessRoleOutputReference",
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
            type_hints = typing.get_type_hints(GoogleBigqueryConnectionAwsAccessRoleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="identity")
    def identity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="iamRoleIdInput")
    def iam_role_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamRoleIdInput"))

    @builtins.property
    @jsii.member(jsii_name="iamRoleId")
    def iam_role_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iamRoleId"))

    @iam_role_id.setter
    def iam_role_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryConnectionAwsAccessRoleOutputReference, "iam_role_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamRoleId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryConnectionAwsAccessRole]:
        return typing.cast(typing.Optional[GoogleBigqueryConnectionAwsAccessRole], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryConnectionAwsAccessRole],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryConnectionAwsAccessRoleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleBigqueryConnectionAwsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryConnection.GoogleBigqueryConnectionAwsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleBigqueryConnectionAwsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAccessRole")
    def put_access_role(self, *, iam_role_id: builtins.str) -> None:
        '''
        :param iam_role_id: The user’s AWS IAM Role that trusts the Google-owned AWS IAM user Connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#iam_role_id GoogleBigqueryConnection#iam_role_id}
        '''
        value = GoogleBigqueryConnectionAwsAccessRole(iam_role_id=iam_role_id)

        return typing.cast(None, jsii.invoke(self, "putAccessRole", [value]))

    @builtins.property
    @jsii.member(jsii_name="accessRole")
    def access_role(self) -> GoogleBigqueryConnectionAwsAccessRoleOutputReference:
        return typing.cast(GoogleBigqueryConnectionAwsAccessRoleOutputReference, jsii.get(self, "accessRole"))

    @builtins.property
    @jsii.member(jsii_name="accessRoleInput")
    def access_role_input(
        self,
    ) -> typing.Optional[GoogleBigqueryConnectionAwsAccessRole]:
        return typing.cast(typing.Optional[GoogleBigqueryConnectionAwsAccessRole], jsii.get(self, "accessRoleInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryConnectionAws]:
        return typing.cast(typing.Optional[GoogleBigqueryConnectionAws], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryConnectionAws],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryConnectionAwsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryConnection.GoogleBigqueryConnectionAzure",
    jsii_struct_bases=[],
    name_mapping={"customer_tenant_id": "customerTenantId"},
)
class GoogleBigqueryConnectionAzure:
    def __init__(self, *, customer_tenant_id: builtins.str) -> None:
        '''
        :param customer_tenant_id: The id of customer's directory that host the data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#customer_tenant_id GoogleBigqueryConnection#customer_tenant_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryConnectionAzure.__init__)
            check_type(argname="argument customer_tenant_id", value=customer_tenant_id, expected_type=type_hints["customer_tenant_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "customer_tenant_id": customer_tenant_id,
        }

    @builtins.property
    def customer_tenant_id(self) -> builtins.str:
        '''The id of customer's directory that host the data.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#customer_tenant_id GoogleBigqueryConnection#customer_tenant_id}
        '''
        result = self._values.get("customer_tenant_id")
        assert result is not None, "Required property 'customer_tenant_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryConnectionAzure(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryConnectionAzureOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryConnection.GoogleBigqueryConnectionAzureOutputReference",
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
            type_hints = typing.get_type_hints(GoogleBigqueryConnectionAzureOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="application")
    def application(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "application"))

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @builtins.property
    @jsii.member(jsii_name="objectId")
    def object_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "objectId"))

    @builtins.property
    @jsii.member(jsii_name="redirectUri")
    def redirect_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "redirectUri"))

    @builtins.property
    @jsii.member(jsii_name="customerTenantIdInput")
    def customer_tenant_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customerTenantIdInput"))

    @builtins.property
    @jsii.member(jsii_name="customerTenantId")
    def customer_tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customerTenantId"))

    @customer_tenant_id.setter
    def customer_tenant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryConnectionAzureOutputReference, "customer_tenant_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customerTenantId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryConnectionAzure]:
        return typing.cast(typing.Optional[GoogleBigqueryConnectionAzure], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryConnectionAzure],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryConnectionAzureOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryConnection.GoogleBigqueryConnectionCloudResource",
    jsii_struct_bases=[],
    name_mapping={},
)
class GoogleBigqueryConnectionCloudResource:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryConnectionCloudResource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryConnectionCloudResourceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryConnection.GoogleBigqueryConnectionCloudResourceOutputReference",
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
            type_hints = typing.get_type_hints(GoogleBigqueryConnectionCloudResourceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="serviceAccountId")
    def service_account_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "serviceAccountId"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryConnectionCloudResource]:
        return typing.cast(typing.Optional[GoogleBigqueryConnectionCloudResource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryConnectionCloudResource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryConnectionCloudResourceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryConnection.GoogleBigqueryConnectionCloudSpanner",
    jsii_struct_bases=[],
    name_mapping={"database": "database", "use_parallelism": "useParallelism"},
)
class GoogleBigqueryConnectionCloudSpanner:
    def __init__(
        self,
        *,
        database: builtins.str,
        use_parallelism: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param database: Cloud Spanner database in the form 'project/instance/database'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#database GoogleBigqueryConnection#database}
        :param use_parallelism: If parallelism should be used when reading from Cloud Spanner. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#use_parallelism GoogleBigqueryConnection#use_parallelism}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryConnectionCloudSpanner.__init__)
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument use_parallelism", value=use_parallelism, expected_type=type_hints["use_parallelism"])
        self._values: typing.Dict[str, typing.Any] = {
            "database": database,
        }
        if use_parallelism is not None:
            self._values["use_parallelism"] = use_parallelism

    @builtins.property
    def database(self) -> builtins.str:
        '''Cloud Spanner database in the form 'project/instance/database'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#database GoogleBigqueryConnection#database}
        '''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def use_parallelism(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If parallelism should be used when reading from Cloud Spanner.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#use_parallelism GoogleBigqueryConnection#use_parallelism}
        '''
        result = self._values.get("use_parallelism")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryConnectionCloudSpanner(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryConnectionCloudSpannerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryConnection.GoogleBigqueryConnectionCloudSpannerOutputReference",
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
            type_hints = typing.get_type_hints(GoogleBigqueryConnectionCloudSpannerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetUseParallelism")
    def reset_use_parallelism(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseParallelism", []))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="useParallelismInput")
    def use_parallelism_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useParallelismInput"))

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryConnectionCloudSpannerOutputReference, "database").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="useParallelism")
    def use_parallelism(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "useParallelism"))

    @use_parallelism.setter
    def use_parallelism(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryConnectionCloudSpannerOutputReference, "use_parallelism").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useParallelism", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryConnectionCloudSpanner]:
        return typing.cast(typing.Optional[GoogleBigqueryConnectionCloudSpanner], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryConnectionCloudSpanner],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryConnectionCloudSpannerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryConnection.GoogleBigqueryConnectionCloudSql",
    jsii_struct_bases=[],
    name_mapping={
        "credential": "credential",
        "database": "database",
        "instance_id": "instanceId",
        "type": "type",
    },
)
class GoogleBigqueryConnectionCloudSql:
    def __init__(
        self,
        *,
        credential: typing.Union["GoogleBigqueryConnectionCloudSqlCredential", typing.Dict[str, typing.Any]],
        database: builtins.str,
        instance_id: builtins.str,
        type: builtins.str,
    ) -> None:
        '''
        :param credential: credential block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#credential GoogleBigqueryConnection#credential}
        :param database: Database name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#database GoogleBigqueryConnection#database}
        :param instance_id: Cloud SQL instance ID in the form project:location:instance. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#instance_id GoogleBigqueryConnection#instance_id}
        :param type: Type of the Cloud SQL database. Possible values: ["DATABASE_TYPE_UNSPECIFIED", "POSTGRES", "MYSQL"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#type GoogleBigqueryConnection#type}
        '''
        if isinstance(credential, dict):
            credential = GoogleBigqueryConnectionCloudSqlCredential(**credential)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryConnectionCloudSql.__init__)
            check_type(argname="argument credential", value=credential, expected_type=type_hints["credential"])
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument instance_id", value=instance_id, expected_type=type_hints["instance_id"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "credential": credential,
            "database": database,
            "instance_id": instance_id,
            "type": type,
        }

    @builtins.property
    def credential(self) -> "GoogleBigqueryConnectionCloudSqlCredential":
        '''credential block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#credential GoogleBigqueryConnection#credential}
        '''
        result = self._values.get("credential")
        assert result is not None, "Required property 'credential' is missing"
        return typing.cast("GoogleBigqueryConnectionCloudSqlCredential", result)

    @builtins.property
    def database(self) -> builtins.str:
        '''Database name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#database GoogleBigqueryConnection#database}
        '''
        result = self._values.get("database")
        assert result is not None, "Required property 'database' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_id(self) -> builtins.str:
        '''Cloud SQL instance ID in the form project:location:instance.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#instance_id GoogleBigqueryConnection#instance_id}
        '''
        result = self._values.get("instance_id")
        assert result is not None, "Required property 'instance_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Type of the Cloud SQL database. Possible values: ["DATABASE_TYPE_UNSPECIFIED", "POSTGRES", "MYSQL"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#type GoogleBigqueryConnection#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryConnectionCloudSql(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryConnection.GoogleBigqueryConnectionCloudSqlCredential",
    jsii_struct_bases=[],
    name_mapping={"password": "password", "username": "username"},
)
class GoogleBigqueryConnectionCloudSqlCredential:
    def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Password for database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#password GoogleBigqueryConnection#password}
        :param username: Username for database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#username GoogleBigqueryConnection#username}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryConnectionCloudSqlCredential.__init__)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {
            "password": password,
            "username": username,
        }

    @builtins.property
    def password(self) -> builtins.str:
        '''Password for database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#password GoogleBigqueryConnection#password}
        '''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def username(self) -> builtins.str:
        '''Username for database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#username GoogleBigqueryConnection#username}
        '''
        result = self._values.get("username")
        assert result is not None, "Required property 'username' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryConnectionCloudSqlCredential(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryConnectionCloudSqlCredentialOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryConnection.GoogleBigqueryConnectionCloudSqlCredentialOutputReference",
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
            type_hints = typing.get_type_hints(GoogleBigqueryConnectionCloudSqlCredentialOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryConnectionCloudSqlCredentialOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryConnectionCloudSqlCredentialOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleBigqueryConnectionCloudSqlCredential]:
        return typing.cast(typing.Optional[GoogleBigqueryConnectionCloudSqlCredential], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryConnectionCloudSqlCredential],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryConnectionCloudSqlCredentialOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleBigqueryConnectionCloudSqlOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryConnection.GoogleBigqueryConnectionCloudSqlOutputReference",
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
            type_hints = typing.get_type_hints(GoogleBigqueryConnectionCloudSqlOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCredential")
    def put_credential(self, *, password: builtins.str, username: builtins.str) -> None:
        '''
        :param password: Password for database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#password GoogleBigqueryConnection#password}
        :param username: Username for database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#username GoogleBigqueryConnection#username}
        '''
        value = GoogleBigqueryConnectionCloudSqlCredential(
            password=password, username=username
        )

        return typing.cast(None, jsii.invoke(self, "putCredential", [value]))

    @builtins.property
    @jsii.member(jsii_name="credential")
    def credential(self) -> GoogleBigqueryConnectionCloudSqlCredentialOutputReference:
        return typing.cast(GoogleBigqueryConnectionCloudSqlCredentialOutputReference, jsii.get(self, "credential"))

    @builtins.property
    @jsii.member(jsii_name="credentialInput")
    def credential_input(
        self,
    ) -> typing.Optional[GoogleBigqueryConnectionCloudSqlCredential]:
        return typing.cast(typing.Optional[GoogleBigqueryConnectionCloudSqlCredential], jsii.get(self, "credentialInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceIdInput")
    def instance_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "database"))

    @database.setter
    def database(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryConnectionCloudSqlOutputReference, "database").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "database", value)

    @builtins.property
    @jsii.member(jsii_name="instanceId")
    def instance_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceId"))

    @instance_id.setter
    def instance_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryConnectionCloudSqlOutputReference, "instance_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceId", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryConnectionCloudSqlOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryConnectionCloudSql]:
        return typing.cast(typing.Optional[GoogleBigqueryConnectionCloudSql], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryConnectionCloudSql],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryConnectionCloudSqlOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryConnection.GoogleBigqueryConnectionConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "aws": "aws",
        "azure": "azure",
        "cloud_resource": "cloudResource",
        "cloud_spanner": "cloudSpanner",
        "cloud_sql": "cloudSql",
        "connection_id": "connectionId",
        "description": "description",
        "friendly_name": "friendlyName",
        "id": "id",
        "location": "location",
        "project": "project",
        "timeouts": "timeouts",
    },
)
class GoogleBigqueryConnectionConfig(cdktf.TerraformMetaArguments):
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
        aws: typing.Optional[typing.Union[GoogleBigqueryConnectionAws, typing.Dict[str, typing.Any]]] = None,
        azure: typing.Optional[typing.Union[GoogleBigqueryConnectionAzure, typing.Dict[str, typing.Any]]] = None,
        cloud_resource: typing.Optional[typing.Union[GoogleBigqueryConnectionCloudResource, typing.Dict[str, typing.Any]]] = None,
        cloud_spanner: typing.Optional[typing.Union[GoogleBigqueryConnectionCloudSpanner, typing.Dict[str, typing.Any]]] = None,
        cloud_sql: typing.Optional[typing.Union[GoogleBigqueryConnectionCloudSql, typing.Dict[str, typing.Any]]] = None,
        connection_id: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        friendly_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        location: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleBigqueryConnectionTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param aws: aws block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#aws GoogleBigqueryConnection#aws}
        :param azure: azure block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#azure GoogleBigqueryConnection#azure}
        :param cloud_resource: cloud_resource block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#cloud_resource GoogleBigqueryConnection#cloud_resource}
        :param cloud_spanner: cloud_spanner block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#cloud_spanner GoogleBigqueryConnection#cloud_spanner}
        :param cloud_sql: cloud_sql block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#cloud_sql GoogleBigqueryConnection#cloud_sql}
        :param connection_id: Optional connection id that should be assigned to the created connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#connection_id GoogleBigqueryConnection#connection_id}
        :param description: A descriptive description for the connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#description GoogleBigqueryConnection#description}
        :param friendly_name: A descriptive name for the connection. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#friendly_name GoogleBigqueryConnection#friendly_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#id GoogleBigqueryConnection#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param location: The geographic location where the connection should reside. Cloud SQL instance must be in the same location as the connection with following exceptions: Cloud SQL us-central1 maps to BigQuery US, Cloud SQL europe-west1 maps to BigQuery EU. Examples: US, EU, asia-northeast1, us-central1, europe-west1. Spanner Connections same as spanner region AWS allowed regions are aws-us-east-1 Azure allowed regions are azure-eastus2 Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#location GoogleBigqueryConnection#location}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#project GoogleBigqueryConnection#project}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#timeouts GoogleBigqueryConnection#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(aws, dict):
            aws = GoogleBigqueryConnectionAws(**aws)
        if isinstance(azure, dict):
            azure = GoogleBigqueryConnectionAzure(**azure)
        if isinstance(cloud_resource, dict):
            cloud_resource = GoogleBigqueryConnectionCloudResource(**cloud_resource)
        if isinstance(cloud_spanner, dict):
            cloud_spanner = GoogleBigqueryConnectionCloudSpanner(**cloud_spanner)
        if isinstance(cloud_sql, dict):
            cloud_sql = GoogleBigqueryConnectionCloudSql(**cloud_sql)
        if isinstance(timeouts, dict):
            timeouts = GoogleBigqueryConnectionTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryConnectionConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument aws", value=aws, expected_type=type_hints["aws"])
            check_type(argname="argument azure", value=azure, expected_type=type_hints["azure"])
            check_type(argname="argument cloud_resource", value=cloud_resource, expected_type=type_hints["cloud_resource"])
            check_type(argname="argument cloud_spanner", value=cloud_spanner, expected_type=type_hints["cloud_spanner"])
            check_type(argname="argument cloud_sql", value=cloud_sql, expected_type=type_hints["cloud_sql"])
            check_type(argname="argument connection_id", value=connection_id, expected_type=type_hints["connection_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument friendly_name", value=friendly_name, expected_type=type_hints["friendly_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {}
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
        if aws is not None:
            self._values["aws"] = aws
        if azure is not None:
            self._values["azure"] = azure
        if cloud_resource is not None:
            self._values["cloud_resource"] = cloud_resource
        if cloud_spanner is not None:
            self._values["cloud_spanner"] = cloud_spanner
        if cloud_sql is not None:
            self._values["cloud_sql"] = cloud_sql
        if connection_id is not None:
            self._values["connection_id"] = connection_id
        if description is not None:
            self._values["description"] = description
        if friendly_name is not None:
            self._values["friendly_name"] = friendly_name
        if id is not None:
            self._values["id"] = id
        if location is not None:
            self._values["location"] = location
        if project is not None:
            self._values["project"] = project
        if timeouts is not None:
            self._values["timeouts"] = timeouts

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
    def aws(self) -> typing.Optional[GoogleBigqueryConnectionAws]:
        '''aws block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#aws GoogleBigqueryConnection#aws}
        '''
        result = self._values.get("aws")
        return typing.cast(typing.Optional[GoogleBigqueryConnectionAws], result)

    @builtins.property
    def azure(self) -> typing.Optional[GoogleBigqueryConnectionAzure]:
        '''azure block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#azure GoogleBigqueryConnection#azure}
        '''
        result = self._values.get("azure")
        return typing.cast(typing.Optional[GoogleBigqueryConnectionAzure], result)

    @builtins.property
    def cloud_resource(self) -> typing.Optional[GoogleBigqueryConnectionCloudResource]:
        '''cloud_resource block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#cloud_resource GoogleBigqueryConnection#cloud_resource}
        '''
        result = self._values.get("cloud_resource")
        return typing.cast(typing.Optional[GoogleBigqueryConnectionCloudResource], result)

    @builtins.property
    def cloud_spanner(self) -> typing.Optional[GoogleBigqueryConnectionCloudSpanner]:
        '''cloud_spanner block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#cloud_spanner GoogleBigqueryConnection#cloud_spanner}
        '''
        result = self._values.get("cloud_spanner")
        return typing.cast(typing.Optional[GoogleBigqueryConnectionCloudSpanner], result)

    @builtins.property
    def cloud_sql(self) -> typing.Optional[GoogleBigqueryConnectionCloudSql]:
        '''cloud_sql block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#cloud_sql GoogleBigqueryConnection#cloud_sql}
        '''
        result = self._values.get("cloud_sql")
        return typing.cast(typing.Optional[GoogleBigqueryConnectionCloudSql], result)

    @builtins.property
    def connection_id(self) -> typing.Optional[builtins.str]:
        '''Optional connection id that should be assigned to the created connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#connection_id GoogleBigqueryConnection#connection_id}
        '''
        result = self._values.get("connection_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A descriptive description for the connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#description GoogleBigqueryConnection#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def friendly_name(self) -> typing.Optional[builtins.str]:
        '''A descriptive name for the connection.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#friendly_name GoogleBigqueryConnection#friendly_name}
        '''
        result = self._values.get("friendly_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#id GoogleBigqueryConnection#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''The geographic location where the connection should reside.

        Cloud SQL instance must be in the same location as the connection
        with following exceptions: Cloud SQL us-central1 maps to BigQuery US, Cloud SQL europe-west1 maps to BigQuery EU.
        Examples: US, EU, asia-northeast1, us-central1, europe-west1.
        Spanner Connections same as spanner region
        AWS allowed regions are aws-us-east-1
        Azure allowed regions are azure-eastus2

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#location GoogleBigqueryConnection#location}
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#project GoogleBigqueryConnection#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleBigqueryConnectionTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#timeouts GoogleBigqueryConnection#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleBigqueryConnectionTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryConnectionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryConnection.GoogleBigqueryConnectionTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleBigqueryConnectionTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#create GoogleBigqueryConnection#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#delete GoogleBigqueryConnection#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#update GoogleBigqueryConnection#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryConnectionTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#create GoogleBigqueryConnection#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#delete GoogleBigqueryConnection#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_connection#update GoogleBigqueryConnection#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryConnectionTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryConnectionTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryConnection.GoogleBigqueryConnectionTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleBigqueryConnectionTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="updateInput")
    def update_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "updateInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryConnectionTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryConnectionTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryConnectionTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleBigqueryConnectionTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleBigqueryConnectionTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleBigqueryConnectionTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryConnectionTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleBigqueryConnection",
    "GoogleBigqueryConnectionAws",
    "GoogleBigqueryConnectionAwsAccessRole",
    "GoogleBigqueryConnectionAwsAccessRoleOutputReference",
    "GoogleBigqueryConnectionAwsOutputReference",
    "GoogleBigqueryConnectionAzure",
    "GoogleBigqueryConnectionAzureOutputReference",
    "GoogleBigqueryConnectionCloudResource",
    "GoogleBigqueryConnectionCloudResourceOutputReference",
    "GoogleBigqueryConnectionCloudSpanner",
    "GoogleBigqueryConnectionCloudSpannerOutputReference",
    "GoogleBigqueryConnectionCloudSql",
    "GoogleBigqueryConnectionCloudSqlCredential",
    "GoogleBigqueryConnectionCloudSqlCredentialOutputReference",
    "GoogleBigqueryConnectionCloudSqlOutputReference",
    "GoogleBigqueryConnectionConfig",
    "GoogleBigqueryConnectionTimeouts",
    "GoogleBigqueryConnectionTimeoutsOutputReference",
]

publication.publish()
