'''
# `google_cloud_identity_group`

Refer to the Terraform Registory for docs: [`google_cloud_identity_group`](https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group).
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


class GoogleCloudIdentityGroup(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudIdentityGroup.GoogleCloudIdentityGroup",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group google_cloud_identity_group}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        group_key: typing.Union["GoogleCloudIdentityGroupGroupKey", typing.Dict[str, typing.Any]],
        labels: typing.Mapping[builtins.str, builtins.str],
        parent: builtins.str,
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        initial_group_config: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleCloudIdentityGroupTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group google_cloud_identity_group} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param group_key: group_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#group_key GoogleCloudIdentityGroup#group_key}
        :param labels: The labels that apply to the Group. Must not contain more than one entry. Must contain the entry 'cloudidentity.googleapis.com/groups.discussion_forum': '' if the Group is a Google Group or 'system/groups/external': '' if the Group is an external-identity-mapped group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#labels GoogleCloudIdentityGroup#labels}
        :param parent: The resource name of the entity under which this Group resides in the Cloud Identity resource hierarchy. Must be of the form identitysources/{identity_source_id} for external-identity-mapped groups or customers/{customer_id} for Google Groups. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#parent GoogleCloudIdentityGroup#parent}
        :param description: An extended description to help users determine the purpose of a Group. Must not be longer than 4,096 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#description GoogleCloudIdentityGroup#description}
        :param display_name: The display name of the Group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#display_name GoogleCloudIdentityGroup#display_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#id GoogleCloudIdentityGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param initial_group_config: The initial configuration options for creating a Group. See the `API reference <https://cloud.google.com/identity/docs/reference/rest/v1beta1/groups/create#initialgroupconfig>`_ for possible values. Default value: "EMPTY" Possible values: ["INITIAL_GROUP_CONFIG_UNSPECIFIED", "WITH_INITIAL_OWNER", "EMPTY"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#initial_group_config GoogleCloudIdentityGroup#initial_group_config}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#timeouts GoogleCloudIdentityGroup#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudIdentityGroup.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleCloudIdentityGroupConfig(
            group_key=group_key,
            labels=labels,
            parent=parent,
            description=description,
            display_name=display_name,
            id=id,
            initial_group_config=initial_group_config,
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

    @jsii.member(jsii_name="putGroupKey")
    def put_group_key(
        self,
        *,
        id: builtins.str,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: The ID of the entity. For Google-managed entities, the id must be the email address of an existing group or user. For external-identity-mapped entities, the id must be a string conforming to the Identity Source's requirements. Must be unique within a namespace. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#id GoogleCloudIdentityGroup#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param namespace: The namespace in which the entity exists. If not specified, the EntityKey represents a Google-managed entity such as a Google user or a Google Group. If specified, the EntityKey represents an external-identity-mapped group. The namespace must correspond to an identity source created in Admin Console and must be in the form of 'identitysources/{identity_source_id}'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#namespace GoogleCloudIdentityGroup#namespace}
        '''
        value = GoogleCloudIdentityGroupGroupKey(id=id, namespace=namespace)

        return typing.cast(None, jsii.invoke(self, "putGroupKey", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#create GoogleCloudIdentityGroup#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#delete GoogleCloudIdentityGroup#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#update GoogleCloudIdentityGroup#update}.
        '''
        value = GoogleCloudIdentityGroupTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInitialGroupConfig")
    def reset_initial_group_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitialGroupConfig", []))

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
    @jsii.member(jsii_name="groupKey")
    def group_key(self) -> "GoogleCloudIdentityGroupGroupKeyOutputReference":
        return typing.cast("GoogleCloudIdentityGroupGroupKeyOutputReference", jsii.get(self, "groupKey"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleCloudIdentityGroupTimeoutsOutputReference":
        return typing.cast("GoogleCloudIdentityGroupTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="updateTime")
    def update_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updateTime"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="groupKeyInput")
    def group_key_input(self) -> typing.Optional["GoogleCloudIdentityGroupGroupKey"]:
        return typing.cast(typing.Optional["GoogleCloudIdentityGroupGroupKey"], jsii.get(self, "groupKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="initialGroupConfigInput")
    def initial_group_config_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "initialGroupConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="parentInput")
    def parent_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parentInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleCloudIdentityGroupTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleCloudIdentityGroupTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudIdentityGroup, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudIdentityGroup, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudIdentityGroup, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="initialGroupConfig")
    def initial_group_config(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "initialGroupConfig"))

    @initial_group_config.setter
    def initial_group_config(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudIdentityGroup, "initial_group_config").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialGroupConfig", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudIdentityGroup, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="parent")
    def parent(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parent"))

    @parent.setter
    def parent(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudIdentityGroup, "parent").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parent", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleCloudIdentityGroup.GoogleCloudIdentityGroupConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "group_key": "groupKey",
        "labels": "labels",
        "parent": "parent",
        "description": "description",
        "display_name": "displayName",
        "id": "id",
        "initial_group_config": "initialGroupConfig",
        "timeouts": "timeouts",
    },
)
class GoogleCloudIdentityGroupConfig(cdktf.TerraformMetaArguments):
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
        group_key: typing.Union["GoogleCloudIdentityGroupGroupKey", typing.Dict[str, typing.Any]],
        labels: typing.Mapping[builtins.str, builtins.str],
        parent: builtins.str,
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        initial_group_config: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleCloudIdentityGroupTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param group_key: group_key block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#group_key GoogleCloudIdentityGroup#group_key}
        :param labels: The labels that apply to the Group. Must not contain more than one entry. Must contain the entry 'cloudidentity.googleapis.com/groups.discussion_forum': '' if the Group is a Google Group or 'system/groups/external': '' if the Group is an external-identity-mapped group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#labels GoogleCloudIdentityGroup#labels}
        :param parent: The resource name of the entity under which this Group resides in the Cloud Identity resource hierarchy. Must be of the form identitysources/{identity_source_id} for external-identity-mapped groups or customers/{customer_id} for Google Groups. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#parent GoogleCloudIdentityGroup#parent}
        :param description: An extended description to help users determine the purpose of a Group. Must not be longer than 4,096 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#description GoogleCloudIdentityGroup#description}
        :param display_name: The display name of the Group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#display_name GoogleCloudIdentityGroup#display_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#id GoogleCloudIdentityGroup#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param initial_group_config: The initial configuration options for creating a Group. See the `API reference <https://cloud.google.com/identity/docs/reference/rest/v1beta1/groups/create#initialgroupconfig>`_ for possible values. Default value: "EMPTY" Possible values: ["INITIAL_GROUP_CONFIG_UNSPECIFIED", "WITH_INITIAL_OWNER", "EMPTY"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#initial_group_config GoogleCloudIdentityGroup#initial_group_config}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#timeouts GoogleCloudIdentityGroup#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(group_key, dict):
            group_key = GoogleCloudIdentityGroupGroupKey(**group_key)
        if isinstance(timeouts, dict):
            timeouts = GoogleCloudIdentityGroupTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudIdentityGroupConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument group_key", value=group_key, expected_type=type_hints["group_key"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument parent", value=parent, expected_type=type_hints["parent"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument initial_group_config", value=initial_group_config, expected_type=type_hints["initial_group_config"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "group_key": group_key,
            "labels": labels,
            "parent": parent,
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
        if description is not None:
            self._values["description"] = description
        if display_name is not None:
            self._values["display_name"] = display_name
        if id is not None:
            self._values["id"] = id
        if initial_group_config is not None:
            self._values["initial_group_config"] = initial_group_config
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
    def group_key(self) -> "GoogleCloudIdentityGroupGroupKey":
        '''group_key block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#group_key GoogleCloudIdentityGroup#group_key}
        '''
        result = self._values.get("group_key")
        assert result is not None, "Required property 'group_key' is missing"
        return typing.cast("GoogleCloudIdentityGroupGroupKey", result)

    @builtins.property
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''The labels that apply to the Group.

        Must not contain more than one entry. Must contain the entry
        'cloudidentity.googleapis.com/groups.discussion_forum': '' if the Group is a Google Group or
        'system/groups/external': '' if the Group is an external-identity-mapped group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#labels GoogleCloudIdentityGroup#labels}
        '''
        result = self._values.get("labels")
        assert result is not None, "Required property 'labels' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    @builtins.property
    def parent(self) -> builtins.str:
        '''The resource name of the entity under which this Group resides in the Cloud Identity resource hierarchy.

        Must be of the form identitysources/{identity_source_id} for external-identity-mapped
        groups or customers/{customer_id} for Google Groups.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#parent GoogleCloudIdentityGroup#parent}
        '''
        result = self._values.get("parent")
        assert result is not None, "Required property 'parent' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An extended description to help users determine the purpose of a Group. Must not be longer than 4,096 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#description GoogleCloudIdentityGroup#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The display name of the Group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#display_name GoogleCloudIdentityGroup#display_name}
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#id GoogleCloudIdentityGroup#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initial_group_config(self) -> typing.Optional[builtins.str]:
        '''The initial configuration options for creating a Group.

        See the
        `API reference <https://cloud.google.com/identity/docs/reference/rest/v1beta1/groups/create#initialgroupconfig>`_
        for possible values. Default value: "EMPTY" Possible values: ["INITIAL_GROUP_CONFIG_UNSPECIFIED", "WITH_INITIAL_OWNER", "EMPTY"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#initial_group_config GoogleCloudIdentityGroup#initial_group_config}
        '''
        result = self._values.get("initial_group_config")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleCloudIdentityGroupTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#timeouts GoogleCloudIdentityGroup#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleCloudIdentityGroupTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleCloudIdentityGroupConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleCloudIdentityGroup.GoogleCloudIdentityGroupGroupKey",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "namespace": "namespace"},
)
class GoogleCloudIdentityGroupGroupKey:
    def __init__(
        self,
        *,
        id: builtins.str,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: The ID of the entity. For Google-managed entities, the id must be the email address of an existing group or user. For external-identity-mapped entities, the id must be a string conforming to the Identity Source's requirements. Must be unique within a namespace. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#id GoogleCloudIdentityGroup#id} Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param namespace: The namespace in which the entity exists. If not specified, the EntityKey represents a Google-managed entity such as a Google user or a Google Group. If specified, the EntityKey represents an external-identity-mapped group. The namespace must correspond to an identity source created in Admin Console and must be in the form of 'identitysources/{identity_source_id}'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#namespace GoogleCloudIdentityGroup#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudIdentityGroupGroupKey.__init__)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
        }
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def id(self) -> builtins.str:
        '''The ID of the entity.

        For Google-managed entities, the id must be the email address of an existing
        group or user.

        For external-identity-mapped entities, the id must be a string conforming
        to the Identity Source's requirements.

        Must be unique within a namespace.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#id GoogleCloudIdentityGroup#id}

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace in which the entity exists.

        If not specified, the EntityKey represents a Google-managed entity
        such as a Google user or a Google Group.

        If specified, the EntityKey represents an external-identity-mapped group.
        The namespace must correspond to an identity source created in Admin Console
        and must be in the form of 'identitysources/{identity_source_id}'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#namespace GoogleCloudIdentityGroup#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleCloudIdentityGroupGroupKey(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleCloudIdentityGroupGroupKeyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudIdentityGroup.GoogleCloudIdentityGroupGroupKeyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleCloudIdentityGroupGroupKeyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudIdentityGroupGroupKeyOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudIdentityGroupGroupKeyOutputReference, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleCloudIdentityGroupGroupKey]:
        return typing.cast(typing.Optional[GoogleCloudIdentityGroupGroupKey], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleCloudIdentityGroupGroupKey],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudIdentityGroupGroupKeyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleCloudIdentityGroup.GoogleCloudIdentityGroupTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleCloudIdentityGroupTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#create GoogleCloudIdentityGroup#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#delete GoogleCloudIdentityGroup#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#update GoogleCloudIdentityGroup#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleCloudIdentityGroupTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#create GoogleCloudIdentityGroup#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#delete GoogleCloudIdentityGroup#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_cloud_identity_group#update GoogleCloudIdentityGroup#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleCloudIdentityGroupTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleCloudIdentityGroupTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleCloudIdentityGroup.GoogleCloudIdentityGroupTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleCloudIdentityGroupTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleCloudIdentityGroupTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudIdentityGroupTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudIdentityGroupTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleCloudIdentityGroupTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleCloudIdentityGroupTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleCloudIdentityGroupTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleCloudIdentityGroupTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleCloudIdentityGroup",
    "GoogleCloudIdentityGroupConfig",
    "GoogleCloudIdentityGroupGroupKey",
    "GoogleCloudIdentityGroupGroupKeyOutputReference",
    "GoogleCloudIdentityGroupTimeouts",
    "GoogleCloudIdentityGroupTimeoutsOutputReference",
]

publication.publish()
