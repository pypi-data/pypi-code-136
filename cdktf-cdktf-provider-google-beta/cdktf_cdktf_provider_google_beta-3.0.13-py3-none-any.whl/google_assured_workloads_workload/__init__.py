'''
# `google_assured_workloads_workload`

Refer to the Terraform Registory for docs: [`google_assured_workloads_workload`](https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload).
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


class GoogleAssuredWorkloadsWorkload(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAssuredWorkloadsWorkload.GoogleAssuredWorkloadsWorkload",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload google_assured_workloads_workload}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        billing_account: builtins.str,
        compliance_regime: builtins.str,
        display_name: builtins.str,
        location: builtins.str,
        organization: builtins.str,
        id: typing.Optional[builtins.str] = None,
        kms_settings: typing.Optional[typing.Union["GoogleAssuredWorkloadsWorkloadKmsSettings", typing.Dict[str, typing.Any]]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        provisioned_resources_parent: typing.Optional[builtins.str] = None,
        resource_settings: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAssuredWorkloadsWorkloadResourceSettings", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleAssuredWorkloadsWorkloadTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload google_assured_workloads_workload} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param billing_account: Required. Input only. The billing account used for the resources which are direct children of workload. This billing account is initially associated with the resources created as part of Workload creation. After the initial creation of these resources, the customer can change the assigned billing account. The resource name has the form ``billingAccounts/{billing_account_id}``. For example, 'billingAccounts/012345-567890-ABCDEF`. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#billing_account GoogleAssuredWorkloadsWorkload#billing_account}
        :param compliance_regime: Required. Immutable. Compliance Regime associated with this workload. Possible values: COMPLIANCE_REGIME_UNSPECIFIED, IL4, CJIS, FEDRAMP_HIGH, FEDRAMP_MODERATE, US_REGIONAL_ACCESS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#compliance_regime GoogleAssuredWorkloadsWorkload#compliance_regime}
        :param display_name: Required. The user-assigned display name of the Workload. When present it must be between 4 to 30 characters. Allowed characters are: lowercase and uppercase letters, numbers, hyphen, and spaces. Example: My Workload Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#display_name GoogleAssuredWorkloadsWorkload#display_name}
        :param location: The location for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#location GoogleAssuredWorkloadsWorkload#location}
        :param organization: The organization for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#organization GoogleAssuredWorkloadsWorkload#organization}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#id GoogleAssuredWorkloadsWorkload#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_settings: kms_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#kms_settings GoogleAssuredWorkloadsWorkload#kms_settings}
        :param labels: Optional. Labels applied to the workload. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#labels GoogleAssuredWorkloadsWorkload#labels}
        :param provisioned_resources_parent: Input only. The parent resource for the resources managed by this Assured Workload. May be either an organization or a folder. Must be the same or a child of the Workload parent. If not specified all resources are created under the Workload parent. Formats: folders/{folder_id}, organizations/{organization_id} Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#provisioned_resources_parent GoogleAssuredWorkloadsWorkload#provisioned_resources_parent}
        :param resource_settings: resource_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#resource_settings GoogleAssuredWorkloadsWorkload#resource_settings}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#timeouts GoogleAssuredWorkloadsWorkload#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAssuredWorkloadsWorkload.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleAssuredWorkloadsWorkloadConfig(
            billing_account=billing_account,
            compliance_regime=compliance_regime,
            display_name=display_name,
            location=location,
            organization=organization,
            id=id,
            kms_settings=kms_settings,
            labels=labels,
            provisioned_resources_parent=provisioned_resources_parent,
            resource_settings=resource_settings,
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

    @jsii.member(jsii_name="putKmsSettings")
    def put_kms_settings(
        self,
        *,
        next_rotation_time: builtins.str,
        rotation_period: builtins.str,
    ) -> None:
        '''
        :param next_rotation_time: Required. Input only. Immutable. The time at which the Key Management Service will automatically create a new version of the crypto key and mark it as the primary. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#next_rotation_time GoogleAssuredWorkloadsWorkload#next_rotation_time}
        :param rotation_period: Required. Input only. Immutable. will be advanced by this period when the Key Management Service automatically rotates a key. Must be at least 24 hours and at most 876,000 hours. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#rotation_period GoogleAssuredWorkloadsWorkload#rotation_period}
        '''
        value = GoogleAssuredWorkloadsWorkloadKmsSettings(
            next_rotation_time=next_rotation_time, rotation_period=rotation_period
        )

        return typing.cast(None, jsii.invoke(self, "putKmsSettings", [value]))

    @jsii.member(jsii_name="putResourceSettings")
    def put_resource_settings(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAssuredWorkloadsWorkloadResourceSettings", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAssuredWorkloadsWorkload.put_resource_settings)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putResourceSettings", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#create GoogleAssuredWorkloadsWorkload#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#delete GoogleAssuredWorkloadsWorkload#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#update GoogleAssuredWorkloadsWorkload#update}.
        '''
        value = GoogleAssuredWorkloadsWorkloadTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKmsSettings")
    def reset_kms_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKmsSettings", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetProvisionedResourcesParent")
    def reset_provisioned_resources_parent(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProvisionedResourcesParent", []))

    @jsii.member(jsii_name="resetResourceSettings")
    def reset_resource_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceSettings", []))

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
    @jsii.member(jsii_name="createTime")
    def create_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createTime"))

    @builtins.property
    @jsii.member(jsii_name="kmsSettings")
    def kms_settings(
        self,
    ) -> "GoogleAssuredWorkloadsWorkloadKmsSettingsOutputReference":
        return typing.cast("GoogleAssuredWorkloadsWorkloadKmsSettingsOutputReference", jsii.get(self, "kmsSettings"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="resources")
    def resources(self) -> "GoogleAssuredWorkloadsWorkloadResourcesList":
        return typing.cast("GoogleAssuredWorkloadsWorkloadResourcesList", jsii.get(self, "resources"))

    @builtins.property
    @jsii.member(jsii_name="resourceSettings")
    def resource_settings(self) -> "GoogleAssuredWorkloadsWorkloadResourceSettingsList":
        return typing.cast("GoogleAssuredWorkloadsWorkloadResourceSettingsList", jsii.get(self, "resourceSettings"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleAssuredWorkloadsWorkloadTimeoutsOutputReference":
        return typing.cast("GoogleAssuredWorkloadsWorkloadTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="billingAccountInput")
    def billing_account_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "billingAccountInput"))

    @builtins.property
    @jsii.member(jsii_name="complianceRegimeInput")
    def compliance_regime_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "complianceRegimeInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsSettingsInput")
    def kms_settings_input(
        self,
    ) -> typing.Optional["GoogleAssuredWorkloadsWorkloadKmsSettings"]:
        return typing.cast(typing.Optional["GoogleAssuredWorkloadsWorkloadKmsSettings"], jsii.get(self, "kmsSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="organizationInput")
    def organization_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "organizationInput"))

    @builtins.property
    @jsii.member(jsii_name="provisionedResourcesParentInput")
    def provisioned_resources_parent_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "provisionedResourcesParentInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceSettingsInput")
    def resource_settings_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAssuredWorkloadsWorkloadResourceSettings"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAssuredWorkloadsWorkloadResourceSettings"]]], jsii.get(self, "resourceSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleAssuredWorkloadsWorkloadTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleAssuredWorkloadsWorkloadTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="billingAccount")
    def billing_account(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "billingAccount"))

    @billing_account.setter
    def billing_account(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAssuredWorkloadsWorkload, "billing_account").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "billingAccount", value)

    @builtins.property
    @jsii.member(jsii_name="complianceRegime")
    def compliance_regime(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "complianceRegime"))

    @compliance_regime.setter
    def compliance_regime(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAssuredWorkloadsWorkload, "compliance_regime").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "complianceRegime", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAssuredWorkloadsWorkload, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAssuredWorkloadsWorkload, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAssuredWorkloadsWorkload, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAssuredWorkloadsWorkload, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="organization")
    def organization(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "organization"))

    @organization.setter
    def organization(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAssuredWorkloadsWorkload, "organization").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "organization", value)

    @builtins.property
    @jsii.member(jsii_name="provisionedResourcesParent")
    def provisioned_resources_parent(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "provisionedResourcesParent"))

    @provisioned_resources_parent.setter
    def provisioned_resources_parent(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAssuredWorkloadsWorkload, "provisioned_resources_parent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisionedResourcesParent", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAssuredWorkloadsWorkload.GoogleAssuredWorkloadsWorkloadConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "billing_account": "billingAccount",
        "compliance_regime": "complianceRegime",
        "display_name": "displayName",
        "location": "location",
        "organization": "organization",
        "id": "id",
        "kms_settings": "kmsSettings",
        "labels": "labels",
        "provisioned_resources_parent": "provisionedResourcesParent",
        "resource_settings": "resourceSettings",
        "timeouts": "timeouts",
    },
)
class GoogleAssuredWorkloadsWorkloadConfig(cdktf.TerraformMetaArguments):
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
        billing_account: builtins.str,
        compliance_regime: builtins.str,
        display_name: builtins.str,
        location: builtins.str,
        organization: builtins.str,
        id: typing.Optional[builtins.str] = None,
        kms_settings: typing.Optional[typing.Union["GoogleAssuredWorkloadsWorkloadKmsSettings", typing.Dict[str, typing.Any]]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        provisioned_resources_parent: typing.Optional[builtins.str] = None,
        resource_settings: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleAssuredWorkloadsWorkloadResourceSettings", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleAssuredWorkloadsWorkloadTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param billing_account: Required. Input only. The billing account used for the resources which are direct children of workload. This billing account is initially associated with the resources created as part of Workload creation. After the initial creation of these resources, the customer can change the assigned billing account. The resource name has the form ``billingAccounts/{billing_account_id}``. For example, 'billingAccounts/012345-567890-ABCDEF`. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#billing_account GoogleAssuredWorkloadsWorkload#billing_account}
        :param compliance_regime: Required. Immutable. Compliance Regime associated with this workload. Possible values: COMPLIANCE_REGIME_UNSPECIFIED, IL4, CJIS, FEDRAMP_HIGH, FEDRAMP_MODERATE, US_REGIONAL_ACCESS. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#compliance_regime GoogleAssuredWorkloadsWorkload#compliance_regime}
        :param display_name: Required. The user-assigned display name of the Workload. When present it must be between 4 to 30 characters. Allowed characters are: lowercase and uppercase letters, numbers, hyphen, and spaces. Example: My Workload Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#display_name GoogleAssuredWorkloadsWorkload#display_name}
        :param location: The location for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#location GoogleAssuredWorkloadsWorkload#location}
        :param organization: The organization for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#organization GoogleAssuredWorkloadsWorkload#organization}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#id GoogleAssuredWorkloadsWorkload#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kms_settings: kms_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#kms_settings GoogleAssuredWorkloadsWorkload#kms_settings}
        :param labels: Optional. Labels applied to the workload. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#labels GoogleAssuredWorkloadsWorkload#labels}
        :param provisioned_resources_parent: Input only. The parent resource for the resources managed by this Assured Workload. May be either an organization or a folder. Must be the same or a child of the Workload parent. If not specified all resources are created under the Workload parent. Formats: folders/{folder_id}, organizations/{organization_id} Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#provisioned_resources_parent GoogleAssuredWorkloadsWorkload#provisioned_resources_parent}
        :param resource_settings: resource_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#resource_settings GoogleAssuredWorkloadsWorkload#resource_settings}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#timeouts GoogleAssuredWorkloadsWorkload#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(kms_settings, dict):
            kms_settings = GoogleAssuredWorkloadsWorkloadKmsSettings(**kms_settings)
        if isinstance(timeouts, dict):
            timeouts = GoogleAssuredWorkloadsWorkloadTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAssuredWorkloadsWorkloadConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument billing_account", value=billing_account, expected_type=type_hints["billing_account"])
            check_type(argname="argument compliance_regime", value=compliance_regime, expected_type=type_hints["compliance_regime"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument organization", value=organization, expected_type=type_hints["organization"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument kms_settings", value=kms_settings, expected_type=type_hints["kms_settings"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument provisioned_resources_parent", value=provisioned_resources_parent, expected_type=type_hints["provisioned_resources_parent"])
            check_type(argname="argument resource_settings", value=resource_settings, expected_type=type_hints["resource_settings"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "billing_account": billing_account,
            "compliance_regime": compliance_regime,
            "display_name": display_name,
            "location": location,
            "organization": organization,
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
        if id is not None:
            self._values["id"] = id
        if kms_settings is not None:
            self._values["kms_settings"] = kms_settings
        if labels is not None:
            self._values["labels"] = labels
        if provisioned_resources_parent is not None:
            self._values["provisioned_resources_parent"] = provisioned_resources_parent
        if resource_settings is not None:
            self._values["resource_settings"] = resource_settings
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
    def billing_account(self) -> builtins.str:
        '''Required.

        Input only. The billing account used for the resources which are direct children of workload. This billing account is initially associated with the resources created as part of Workload creation. After the initial creation of these resources, the customer can change the assigned billing account. The resource name has the form ``billingAccounts/{billing_account_id}``. For example, 'billingAccounts/012345-567890-ABCDEF`.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#billing_account GoogleAssuredWorkloadsWorkload#billing_account}
        '''
        result = self._values.get("billing_account")
        assert result is not None, "Required property 'billing_account' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def compliance_regime(self) -> builtins.str:
        '''Required. Immutable. Compliance Regime associated with this workload. Possible values: COMPLIANCE_REGIME_UNSPECIFIED, IL4, CJIS, FEDRAMP_HIGH, FEDRAMP_MODERATE, US_REGIONAL_ACCESS.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#compliance_regime GoogleAssuredWorkloadsWorkload#compliance_regime}
        '''
        result = self._values.get("compliance_regime")
        assert result is not None, "Required property 'compliance_regime' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def display_name(self) -> builtins.str:
        '''Required.

        The user-assigned display name of the Workload. When present it must be between 4 to 30 characters. Allowed characters are: lowercase and uppercase letters, numbers, hyphen, and spaces. Example: My Workload

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#display_name GoogleAssuredWorkloadsWorkload#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def location(self) -> builtins.str:
        '''The location for the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#location GoogleAssuredWorkloadsWorkload#location}
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def organization(self) -> builtins.str:
        '''The organization for the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#organization GoogleAssuredWorkloadsWorkload#organization}
        '''
        result = self._values.get("organization")
        assert result is not None, "Required property 'organization' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#id GoogleAssuredWorkloadsWorkload#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_settings(
        self,
    ) -> typing.Optional["GoogleAssuredWorkloadsWorkloadKmsSettings"]:
        '''kms_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#kms_settings GoogleAssuredWorkloadsWorkload#kms_settings}
        '''
        result = self._values.get("kms_settings")
        return typing.cast(typing.Optional["GoogleAssuredWorkloadsWorkloadKmsSettings"], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional. Labels applied to the workload.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#labels GoogleAssuredWorkloadsWorkload#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def provisioned_resources_parent(self) -> typing.Optional[builtins.str]:
        '''Input only.

        The parent resource for the resources managed by this Assured Workload. May be either an organization or a folder. Must be the same or a child of the Workload parent. If not specified all resources are created under the Workload parent. Formats: folders/{folder_id}, organizations/{organization_id}

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#provisioned_resources_parent GoogleAssuredWorkloadsWorkload#provisioned_resources_parent}
        '''
        result = self._values.get("provisioned_resources_parent")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_settings(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAssuredWorkloadsWorkloadResourceSettings"]]]:
        '''resource_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#resource_settings GoogleAssuredWorkloadsWorkload#resource_settings}
        '''
        result = self._values.get("resource_settings")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleAssuredWorkloadsWorkloadResourceSettings"]]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleAssuredWorkloadsWorkloadTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#timeouts GoogleAssuredWorkloadsWorkload#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleAssuredWorkloadsWorkloadTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAssuredWorkloadsWorkloadConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAssuredWorkloadsWorkload.GoogleAssuredWorkloadsWorkloadKmsSettings",
    jsii_struct_bases=[],
    name_mapping={
        "next_rotation_time": "nextRotationTime",
        "rotation_period": "rotationPeriod",
    },
)
class GoogleAssuredWorkloadsWorkloadKmsSettings:
    def __init__(
        self,
        *,
        next_rotation_time: builtins.str,
        rotation_period: builtins.str,
    ) -> None:
        '''
        :param next_rotation_time: Required. Input only. Immutable. The time at which the Key Management Service will automatically create a new version of the crypto key and mark it as the primary. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#next_rotation_time GoogleAssuredWorkloadsWorkload#next_rotation_time}
        :param rotation_period: Required. Input only. Immutable. will be advanced by this period when the Key Management Service automatically rotates a key. Must be at least 24 hours and at most 876,000 hours. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#rotation_period GoogleAssuredWorkloadsWorkload#rotation_period}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAssuredWorkloadsWorkloadKmsSettings.__init__)
            check_type(argname="argument next_rotation_time", value=next_rotation_time, expected_type=type_hints["next_rotation_time"])
            check_type(argname="argument rotation_period", value=rotation_period, expected_type=type_hints["rotation_period"])
        self._values: typing.Dict[str, typing.Any] = {
            "next_rotation_time": next_rotation_time,
            "rotation_period": rotation_period,
        }

    @builtins.property
    def next_rotation_time(self) -> builtins.str:
        '''Required.

        Input only. Immutable. The time at which the Key Management Service will automatically create a new version of the crypto key and mark it as the primary.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#next_rotation_time GoogleAssuredWorkloadsWorkload#next_rotation_time}
        '''
        result = self._values.get("next_rotation_time")
        assert result is not None, "Required property 'next_rotation_time' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rotation_period(self) -> builtins.str:
        '''Required.

        Input only. Immutable. will be advanced by this period when the Key Management Service automatically rotates a key. Must be at least 24 hours and at most 876,000 hours.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#rotation_period GoogleAssuredWorkloadsWorkload#rotation_period}
        '''
        result = self._values.get("rotation_period")
        assert result is not None, "Required property 'rotation_period' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAssuredWorkloadsWorkloadKmsSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAssuredWorkloadsWorkloadKmsSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAssuredWorkloadsWorkload.GoogleAssuredWorkloadsWorkloadKmsSettingsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAssuredWorkloadsWorkloadKmsSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="nextRotationTimeInput")
    def next_rotation_time_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nextRotationTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="rotationPeriodInput")
    def rotation_period_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rotationPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="nextRotationTime")
    def next_rotation_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nextRotationTime"))

    @next_rotation_time.setter
    def next_rotation_time(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAssuredWorkloadsWorkloadKmsSettingsOutputReference, "next_rotation_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nextRotationTime", value)

    @builtins.property
    @jsii.member(jsii_name="rotationPeriod")
    def rotation_period(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rotationPeriod"))

    @rotation_period.setter
    def rotation_period(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAssuredWorkloadsWorkloadKmsSettingsOutputReference, "rotation_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rotationPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAssuredWorkloadsWorkloadKmsSettings]:
        return typing.cast(typing.Optional[GoogleAssuredWorkloadsWorkloadKmsSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAssuredWorkloadsWorkloadKmsSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAssuredWorkloadsWorkloadKmsSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAssuredWorkloadsWorkload.GoogleAssuredWorkloadsWorkloadResourceSettings",
    jsii_struct_bases=[],
    name_mapping={"resource_id": "resourceId", "resource_type": "resourceType"},
)
class GoogleAssuredWorkloadsWorkloadResourceSettings:
    def __init__(
        self,
        *,
        resource_id: typing.Optional[builtins.str] = None,
        resource_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param resource_id: Resource identifier. For a project this represents project_number. If the project is already taken, the workload creation will fail. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#resource_id GoogleAssuredWorkloadsWorkload#resource_id}
        :param resource_type: Indicates the type of resource. This field should be specified to correspond the id to the right project type (CONSUMER_PROJECT or ENCRYPTION_KEYS_PROJECT) Possible values: RESOURCE_TYPE_UNSPECIFIED, CONSUMER_PROJECT, ENCRYPTION_KEYS_PROJECT, KEYRING, CONSUMER_FOLDER Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#resource_type GoogleAssuredWorkloadsWorkload#resource_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAssuredWorkloadsWorkloadResourceSettings.__init__)
            check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
            check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if resource_id is not None:
            self._values["resource_id"] = resource_id
        if resource_type is not None:
            self._values["resource_type"] = resource_type

    @builtins.property
    def resource_id(self) -> typing.Optional[builtins.str]:
        '''Resource identifier. For a project this represents project_number. If the project is already taken, the workload creation will fail.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#resource_id GoogleAssuredWorkloadsWorkload#resource_id}
        '''
        result = self._values.get("resource_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_type(self) -> typing.Optional[builtins.str]:
        '''Indicates the type of resource.

        This field should be specified to correspond the id to the right project type (CONSUMER_PROJECT or ENCRYPTION_KEYS_PROJECT) Possible values: RESOURCE_TYPE_UNSPECIFIED, CONSUMER_PROJECT, ENCRYPTION_KEYS_PROJECT, KEYRING, CONSUMER_FOLDER

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#resource_type GoogleAssuredWorkloadsWorkload#resource_type}
        '''
        result = self._values.get("resource_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAssuredWorkloadsWorkloadResourceSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAssuredWorkloadsWorkloadResourceSettingsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAssuredWorkloadsWorkload.GoogleAssuredWorkloadsWorkloadResourceSettingsList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAssuredWorkloadsWorkloadResourceSettingsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleAssuredWorkloadsWorkloadResourceSettingsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAssuredWorkloadsWorkloadResourceSettingsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleAssuredWorkloadsWorkloadResourceSettingsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAssuredWorkloadsWorkloadResourceSettingsList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAssuredWorkloadsWorkloadResourceSettingsList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAssuredWorkloadsWorkloadResourceSettingsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAssuredWorkloadsWorkloadResourceSettings]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAssuredWorkloadsWorkloadResourceSettings]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleAssuredWorkloadsWorkloadResourceSettings]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAssuredWorkloadsWorkloadResourceSettingsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleAssuredWorkloadsWorkloadResourceSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAssuredWorkloadsWorkload.GoogleAssuredWorkloadsWorkloadResourceSettingsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAssuredWorkloadsWorkloadResourceSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetResourceId")
    def reset_resource_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceId", []))

    @jsii.member(jsii_name="resetResourceType")
    def reset_resource_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceType", []))

    @builtins.property
    @jsii.member(jsii_name="resourceIdInput")
    def resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceTypeInput")
    def resource_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceId"))

    @resource_id.setter
    def resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAssuredWorkloadsWorkloadResourceSettingsOutputReference, "resource_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceId", value)

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @resource_type.setter
    def resource_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAssuredWorkloadsWorkloadResourceSettingsOutputReference, "resource_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleAssuredWorkloadsWorkloadResourceSettings, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleAssuredWorkloadsWorkloadResourceSettings, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleAssuredWorkloadsWorkloadResourceSettings, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAssuredWorkloadsWorkloadResourceSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAssuredWorkloadsWorkload.GoogleAssuredWorkloadsWorkloadResources",
    jsii_struct_bases=[],
    name_mapping={},
)
class GoogleAssuredWorkloadsWorkloadResources:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAssuredWorkloadsWorkloadResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAssuredWorkloadsWorkloadResourcesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAssuredWorkloadsWorkload.GoogleAssuredWorkloadsWorkloadResourcesList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAssuredWorkloadsWorkloadResourcesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleAssuredWorkloadsWorkloadResourcesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAssuredWorkloadsWorkloadResourcesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleAssuredWorkloadsWorkloadResourcesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAssuredWorkloadsWorkloadResourcesList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAssuredWorkloadsWorkloadResourcesList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAssuredWorkloadsWorkloadResourcesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GoogleAssuredWorkloadsWorkloadResourcesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAssuredWorkloadsWorkload.GoogleAssuredWorkloadsWorkloadResourcesOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAssuredWorkloadsWorkloadResourcesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="resourceId")
    def resource_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "resourceId"))

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceType"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAssuredWorkloadsWorkloadResources]:
        return typing.cast(typing.Optional[GoogleAssuredWorkloadsWorkloadResources], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAssuredWorkloadsWorkloadResources],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAssuredWorkloadsWorkloadResourcesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAssuredWorkloadsWorkload.GoogleAssuredWorkloadsWorkloadTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleAssuredWorkloadsWorkloadTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#create GoogleAssuredWorkloadsWorkload#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#delete GoogleAssuredWorkloadsWorkload#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#update GoogleAssuredWorkloadsWorkload#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAssuredWorkloadsWorkloadTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#create GoogleAssuredWorkloadsWorkload#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#delete GoogleAssuredWorkloadsWorkload#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_assured_workloads_workload#update GoogleAssuredWorkloadsWorkload#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAssuredWorkloadsWorkloadTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAssuredWorkloadsWorkloadTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAssuredWorkloadsWorkload.GoogleAssuredWorkloadsWorkloadTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAssuredWorkloadsWorkloadTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleAssuredWorkloadsWorkloadTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAssuredWorkloadsWorkloadTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAssuredWorkloadsWorkloadTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleAssuredWorkloadsWorkloadTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleAssuredWorkloadsWorkloadTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleAssuredWorkloadsWorkloadTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAssuredWorkloadsWorkloadTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleAssuredWorkloadsWorkload",
    "GoogleAssuredWorkloadsWorkloadConfig",
    "GoogleAssuredWorkloadsWorkloadKmsSettings",
    "GoogleAssuredWorkloadsWorkloadKmsSettingsOutputReference",
    "GoogleAssuredWorkloadsWorkloadResourceSettings",
    "GoogleAssuredWorkloadsWorkloadResourceSettingsList",
    "GoogleAssuredWorkloadsWorkloadResourceSettingsOutputReference",
    "GoogleAssuredWorkloadsWorkloadResources",
    "GoogleAssuredWorkloadsWorkloadResourcesList",
    "GoogleAssuredWorkloadsWorkloadResourcesOutputReference",
    "GoogleAssuredWorkloadsWorkloadTimeouts",
    "GoogleAssuredWorkloadsWorkloadTimeoutsOutputReference",
]

publication.publish()
