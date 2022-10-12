'''
# `google_data_catalog_policy_tag`

Refer to the Terraform Registory for docs: [`google_data_catalog_policy_tag`](https://www.terraform.io/docs/providers/google-beta/r/google_data_catalog_policy_tag).
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


class GoogleDataCatalogPolicyTag(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataCatalogPolicyTag.GoogleDataCatalogPolicyTag",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_catalog_policy_tag google_data_catalog_policy_tag}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        display_name: builtins.str,
        taxonomy: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        parent_policy_tag: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleDataCatalogPolicyTagTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_catalog_policy_tag google_data_catalog_policy_tag} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param display_name: User defined name of this policy tag. It must: be unique within the parent taxonomy; contain only unicode letters, numbers, underscores, dashes and spaces; not start or end with spaces; and be at most 200 bytes long when encoded in UTF-8. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_catalog_policy_tag#display_name GoogleDataCatalogPolicyTag#display_name}
        :param taxonomy: Taxonomy the policy tag is associated with. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_catalog_policy_tag#taxonomy GoogleDataCatalogPolicyTag#taxonomy}
        :param description: Description of this policy tag. It must: contain only unicode characters, tabs, newlines, carriage returns and page breaks; and be at most 2000 bytes long when encoded in UTF-8. If not set, defaults to an empty description. If not set, defaults to an empty description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_catalog_policy_tag#description GoogleDataCatalogPolicyTag#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_catalog_policy_tag#id GoogleDataCatalogPolicyTag#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param parent_policy_tag: Resource name of this policy tag's parent policy tag. If empty, it means this policy tag is a top level policy tag. If not set, defaults to an empty string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_catalog_policy_tag#parent_policy_tag GoogleDataCatalogPolicyTag#parent_policy_tag}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_catalog_policy_tag#timeouts GoogleDataCatalogPolicyTag#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataCatalogPolicyTag.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleDataCatalogPolicyTagConfig(
            display_name=display_name,
            taxonomy=taxonomy,
            description=description,
            id=id,
            parent_policy_tag=parent_policy_tag,
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

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_catalog_policy_tag#create GoogleDataCatalogPolicyTag#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_catalog_policy_tag#delete GoogleDataCatalogPolicyTag#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_catalog_policy_tag#update GoogleDataCatalogPolicyTag#update}.
        '''
        value = GoogleDataCatalogPolicyTagTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetParentPolicyTag")
    def reset_parent_policy_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParentPolicyTag", []))

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
    @jsii.member(jsii_name="childPolicyTags")
    def child_policy_tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "childPolicyTags"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleDataCatalogPolicyTagTimeoutsOutputReference":
        return typing.cast("GoogleDataCatalogPolicyTagTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="parentPolicyTagInput")
    def parent_policy_tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parentPolicyTagInput"))

    @builtins.property
    @jsii.member(jsii_name="taxonomyInput")
    def taxonomy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "taxonomyInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleDataCatalogPolicyTagTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleDataCatalogPolicyTagTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataCatalogPolicyTag, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataCatalogPolicyTag, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataCatalogPolicyTag, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="parentPolicyTag")
    def parent_policy_tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parentPolicyTag"))

    @parent_policy_tag.setter
    def parent_policy_tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataCatalogPolicyTag, "parent_policy_tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parentPolicyTag", value)

    @builtins.property
    @jsii.member(jsii_name="taxonomy")
    def taxonomy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "taxonomy"))

    @taxonomy.setter
    def taxonomy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataCatalogPolicyTag, "taxonomy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taxonomy", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataCatalogPolicyTag.GoogleDataCatalogPolicyTagConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "display_name": "displayName",
        "taxonomy": "taxonomy",
        "description": "description",
        "id": "id",
        "parent_policy_tag": "parentPolicyTag",
        "timeouts": "timeouts",
    },
)
class GoogleDataCatalogPolicyTagConfig(cdktf.TerraformMetaArguments):
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
        display_name: builtins.str,
        taxonomy: builtins.str,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        parent_policy_tag: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleDataCatalogPolicyTagTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param display_name: User defined name of this policy tag. It must: be unique within the parent taxonomy; contain only unicode letters, numbers, underscores, dashes and spaces; not start or end with spaces; and be at most 200 bytes long when encoded in UTF-8. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_catalog_policy_tag#display_name GoogleDataCatalogPolicyTag#display_name}
        :param taxonomy: Taxonomy the policy tag is associated with. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_catalog_policy_tag#taxonomy GoogleDataCatalogPolicyTag#taxonomy}
        :param description: Description of this policy tag. It must: contain only unicode characters, tabs, newlines, carriage returns and page breaks; and be at most 2000 bytes long when encoded in UTF-8. If not set, defaults to an empty description. If not set, defaults to an empty description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_catalog_policy_tag#description GoogleDataCatalogPolicyTag#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_catalog_policy_tag#id GoogleDataCatalogPolicyTag#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param parent_policy_tag: Resource name of this policy tag's parent policy tag. If empty, it means this policy tag is a top level policy tag. If not set, defaults to an empty string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_catalog_policy_tag#parent_policy_tag GoogleDataCatalogPolicyTag#parent_policy_tag}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_catalog_policy_tag#timeouts GoogleDataCatalogPolicyTag#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = GoogleDataCatalogPolicyTagTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataCatalogPolicyTagConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument taxonomy", value=taxonomy, expected_type=type_hints["taxonomy"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument parent_policy_tag", value=parent_policy_tag, expected_type=type_hints["parent_policy_tag"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "display_name": display_name,
            "taxonomy": taxonomy,
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
        if id is not None:
            self._values["id"] = id
        if parent_policy_tag is not None:
            self._values["parent_policy_tag"] = parent_policy_tag
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
    def display_name(self) -> builtins.str:
        '''User defined name of this policy tag.

        It must: be unique within the parent
        taxonomy; contain only unicode letters, numbers, underscores, dashes and spaces;
        not start or end with spaces; and be at most 200 bytes long when encoded in UTF-8.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_catalog_policy_tag#display_name GoogleDataCatalogPolicyTag#display_name}
        '''
        result = self._values.get("display_name")
        assert result is not None, "Required property 'display_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def taxonomy(self) -> builtins.str:
        '''Taxonomy the policy tag is associated with.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_catalog_policy_tag#taxonomy GoogleDataCatalogPolicyTag#taxonomy}
        '''
        result = self._values.get("taxonomy")
        assert result is not None, "Required property 'taxonomy' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Description of this policy tag.

        It must: contain only unicode characters, tabs,
        newlines, carriage returns and page breaks; and be at most 2000 bytes long when
        encoded in UTF-8. If not set, defaults to an empty description.
        If not set, defaults to an empty description.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_catalog_policy_tag#description GoogleDataCatalogPolicyTag#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_catalog_policy_tag#id GoogleDataCatalogPolicyTag#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parent_policy_tag(self) -> typing.Optional[builtins.str]:
        '''Resource name of this policy tag's parent policy tag.

        If empty, it means this policy tag is a top level policy tag.
        If not set, defaults to an empty string.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_catalog_policy_tag#parent_policy_tag GoogleDataCatalogPolicyTag#parent_policy_tag}
        '''
        result = self._values.get("parent_policy_tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleDataCatalogPolicyTagTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_catalog_policy_tag#timeouts GoogleDataCatalogPolicyTag#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleDataCatalogPolicyTagTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataCatalogPolicyTagConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataCatalogPolicyTag.GoogleDataCatalogPolicyTagTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleDataCatalogPolicyTagTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_catalog_policy_tag#create GoogleDataCatalogPolicyTag#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_catalog_policy_tag#delete GoogleDataCatalogPolicyTag#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_catalog_policy_tag#update GoogleDataCatalogPolicyTag#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataCatalogPolicyTagTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_catalog_policy_tag#create GoogleDataCatalogPolicyTag#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_catalog_policy_tag#delete GoogleDataCatalogPolicyTag#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_data_catalog_policy_tag#update GoogleDataCatalogPolicyTag#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataCatalogPolicyTagTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataCatalogPolicyTagTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataCatalogPolicyTag.GoogleDataCatalogPolicyTagTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataCatalogPolicyTagTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleDataCatalogPolicyTagTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataCatalogPolicyTagTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataCatalogPolicyTagTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDataCatalogPolicyTagTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDataCatalogPolicyTagTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDataCatalogPolicyTagTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataCatalogPolicyTagTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleDataCatalogPolicyTag",
    "GoogleDataCatalogPolicyTagConfig",
    "GoogleDataCatalogPolicyTagTimeouts",
    "GoogleDataCatalogPolicyTagTimeoutsOutputReference",
]

publication.publish()
