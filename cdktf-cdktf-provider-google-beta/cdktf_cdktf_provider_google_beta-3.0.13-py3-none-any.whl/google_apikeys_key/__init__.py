'''
# `google_apikeys_key`

Refer to the Terraform Registory for docs: [`google_apikeys_key`](https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key).
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


class GoogleApikeysKey(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleApikeysKey.GoogleApikeysKey",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key google_apikeys_key}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        display_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        restrictions: typing.Optional[typing.Union["GoogleApikeysKeyRestrictions", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleApikeysKeyTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key google_apikeys_key} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The resource name of the key. The name must be unique within the project, must conform with RFC-1034, is restricted to lower-cased letters, and has a maximum length of 63 characters. In another word, the name must match the regular expression: ``[a-z]([a-z0-9-]{0,61}[a-z0-9])?``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#name GoogleApikeysKey#name}
        :param display_name: Human-readable display name of this API key. Modifiable by user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#display_name GoogleApikeysKey#display_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#id GoogleApikeysKey#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: The project for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#project GoogleApikeysKey#project}
        :param restrictions: restrictions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#restrictions GoogleApikeysKey#restrictions}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#timeouts GoogleApikeysKey#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApikeysKey.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleApikeysKeyConfig(
            name=name,
            display_name=display_name,
            id=id,
            project=project,
            restrictions=restrictions,
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

    @jsii.member(jsii_name="putRestrictions")
    def put_restrictions(
        self,
        *,
        android_key_restrictions: typing.Optional[typing.Union["GoogleApikeysKeyRestrictionsAndroidKeyRestrictions", typing.Dict[str, typing.Any]]] = None,
        api_targets: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleApikeysKeyRestrictionsApiTargets", typing.Dict[str, typing.Any]]]]] = None,
        browser_key_restrictions: typing.Optional[typing.Union["GoogleApikeysKeyRestrictionsBrowserKeyRestrictions", typing.Dict[str, typing.Any]]] = None,
        ios_key_restrictions: typing.Optional[typing.Union["GoogleApikeysKeyRestrictionsIosKeyRestrictions", typing.Dict[str, typing.Any]]] = None,
        server_key_restrictions: typing.Optional[typing.Union["GoogleApikeysKeyRestrictionsServerKeyRestrictions", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param android_key_restrictions: android_key_restrictions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#android_key_restrictions GoogleApikeysKey#android_key_restrictions}
        :param api_targets: api_targets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#api_targets GoogleApikeysKey#api_targets}
        :param browser_key_restrictions: browser_key_restrictions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#browser_key_restrictions GoogleApikeysKey#browser_key_restrictions}
        :param ios_key_restrictions: ios_key_restrictions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#ios_key_restrictions GoogleApikeysKey#ios_key_restrictions}
        :param server_key_restrictions: server_key_restrictions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#server_key_restrictions GoogleApikeysKey#server_key_restrictions}
        '''
        value = GoogleApikeysKeyRestrictions(
            android_key_restrictions=android_key_restrictions,
            api_targets=api_targets,
            browser_key_restrictions=browser_key_restrictions,
            ios_key_restrictions=ios_key_restrictions,
            server_key_restrictions=server_key_restrictions,
        )

        return typing.cast(None, jsii.invoke(self, "putRestrictions", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#create GoogleApikeysKey#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#delete GoogleApikeysKey#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#update GoogleApikeysKey#update}.
        '''
        value = GoogleApikeysKeyTimeouts(create=create, delete=delete, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetRestrictions")
    def reset_restrictions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRestrictions", []))

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
    @jsii.member(jsii_name="keyString")
    def key_string(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyString"))

    @builtins.property
    @jsii.member(jsii_name="restrictions")
    def restrictions(self) -> "GoogleApikeysKeyRestrictionsOutputReference":
        return typing.cast("GoogleApikeysKeyRestrictionsOutputReference", jsii.get(self, "restrictions"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleApikeysKeyTimeoutsOutputReference":
        return typing.cast("GoogleApikeysKeyTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="restrictionsInput")
    def restrictions_input(self) -> typing.Optional["GoogleApikeysKeyRestrictions"]:
        return typing.cast(typing.Optional["GoogleApikeysKeyRestrictions"], jsii.get(self, "restrictionsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleApikeysKeyTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleApikeysKeyTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApikeysKey, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApikeysKey, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApikeysKey, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApikeysKey, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleApikeysKey.GoogleApikeysKeyConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "display_name": "displayName",
        "id": "id",
        "project": "project",
        "restrictions": "restrictions",
        "timeouts": "timeouts",
    },
)
class GoogleApikeysKeyConfig(cdktf.TerraformMetaArguments):
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
        name: builtins.str,
        display_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        restrictions: typing.Optional[typing.Union["GoogleApikeysKeyRestrictions", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleApikeysKeyTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The resource name of the key. The name must be unique within the project, must conform with RFC-1034, is restricted to lower-cased letters, and has a maximum length of 63 characters. In another word, the name must match the regular expression: ``[a-z]([a-z0-9-]{0,61}[a-z0-9])?``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#name GoogleApikeysKey#name}
        :param display_name: Human-readable display name of this API key. Modifiable by user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#display_name GoogleApikeysKey#display_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#id GoogleApikeysKey#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: The project for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#project GoogleApikeysKey#project}
        :param restrictions: restrictions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#restrictions GoogleApikeysKey#restrictions}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#timeouts GoogleApikeysKey#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(restrictions, dict):
            restrictions = GoogleApikeysKeyRestrictions(**restrictions)
        if isinstance(timeouts, dict):
            timeouts = GoogleApikeysKeyTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApikeysKeyConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument restrictions", value=restrictions, expected_type=type_hints["restrictions"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
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
        if display_name is not None:
            self._values["display_name"] = display_name
        if id is not None:
            self._values["id"] = id
        if project is not None:
            self._values["project"] = project
        if restrictions is not None:
            self._values["restrictions"] = restrictions
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
    def name(self) -> builtins.str:
        '''The resource name of the key.

        The name must be unique within the project, must conform with RFC-1034, is restricted to lower-cased letters, and has a maximum length of 63 characters. In another word, the name must match the regular expression: ``[a-z]([a-z0-9-]{0,61}[a-z0-9])?``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#name GoogleApikeysKey#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''Human-readable display name of this API key. Modifiable by user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#display_name GoogleApikeysKey#display_name}
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#id GoogleApikeysKey#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''The project for the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#project GoogleApikeysKey#project}
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def restrictions(self) -> typing.Optional["GoogleApikeysKeyRestrictions"]:
        '''restrictions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#restrictions GoogleApikeysKey#restrictions}
        '''
        result = self._values.get("restrictions")
        return typing.cast(typing.Optional["GoogleApikeysKeyRestrictions"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleApikeysKeyTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#timeouts GoogleApikeysKey#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleApikeysKeyTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleApikeysKeyConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleApikeysKey.GoogleApikeysKeyRestrictions",
    jsii_struct_bases=[],
    name_mapping={
        "android_key_restrictions": "androidKeyRestrictions",
        "api_targets": "apiTargets",
        "browser_key_restrictions": "browserKeyRestrictions",
        "ios_key_restrictions": "iosKeyRestrictions",
        "server_key_restrictions": "serverKeyRestrictions",
    },
)
class GoogleApikeysKeyRestrictions:
    def __init__(
        self,
        *,
        android_key_restrictions: typing.Optional[typing.Union["GoogleApikeysKeyRestrictionsAndroidKeyRestrictions", typing.Dict[str, typing.Any]]] = None,
        api_targets: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleApikeysKeyRestrictionsApiTargets", typing.Dict[str, typing.Any]]]]] = None,
        browser_key_restrictions: typing.Optional[typing.Union["GoogleApikeysKeyRestrictionsBrowserKeyRestrictions", typing.Dict[str, typing.Any]]] = None,
        ios_key_restrictions: typing.Optional[typing.Union["GoogleApikeysKeyRestrictionsIosKeyRestrictions", typing.Dict[str, typing.Any]]] = None,
        server_key_restrictions: typing.Optional[typing.Union["GoogleApikeysKeyRestrictionsServerKeyRestrictions", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param android_key_restrictions: android_key_restrictions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#android_key_restrictions GoogleApikeysKey#android_key_restrictions}
        :param api_targets: api_targets block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#api_targets GoogleApikeysKey#api_targets}
        :param browser_key_restrictions: browser_key_restrictions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#browser_key_restrictions GoogleApikeysKey#browser_key_restrictions}
        :param ios_key_restrictions: ios_key_restrictions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#ios_key_restrictions GoogleApikeysKey#ios_key_restrictions}
        :param server_key_restrictions: server_key_restrictions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#server_key_restrictions GoogleApikeysKey#server_key_restrictions}
        '''
        if isinstance(android_key_restrictions, dict):
            android_key_restrictions = GoogleApikeysKeyRestrictionsAndroidKeyRestrictions(**android_key_restrictions)
        if isinstance(browser_key_restrictions, dict):
            browser_key_restrictions = GoogleApikeysKeyRestrictionsBrowserKeyRestrictions(**browser_key_restrictions)
        if isinstance(ios_key_restrictions, dict):
            ios_key_restrictions = GoogleApikeysKeyRestrictionsIosKeyRestrictions(**ios_key_restrictions)
        if isinstance(server_key_restrictions, dict):
            server_key_restrictions = GoogleApikeysKeyRestrictionsServerKeyRestrictions(**server_key_restrictions)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApikeysKeyRestrictions.__init__)
            check_type(argname="argument android_key_restrictions", value=android_key_restrictions, expected_type=type_hints["android_key_restrictions"])
            check_type(argname="argument api_targets", value=api_targets, expected_type=type_hints["api_targets"])
            check_type(argname="argument browser_key_restrictions", value=browser_key_restrictions, expected_type=type_hints["browser_key_restrictions"])
            check_type(argname="argument ios_key_restrictions", value=ios_key_restrictions, expected_type=type_hints["ios_key_restrictions"])
            check_type(argname="argument server_key_restrictions", value=server_key_restrictions, expected_type=type_hints["server_key_restrictions"])
        self._values: typing.Dict[str, typing.Any] = {}
        if android_key_restrictions is not None:
            self._values["android_key_restrictions"] = android_key_restrictions
        if api_targets is not None:
            self._values["api_targets"] = api_targets
        if browser_key_restrictions is not None:
            self._values["browser_key_restrictions"] = browser_key_restrictions
        if ios_key_restrictions is not None:
            self._values["ios_key_restrictions"] = ios_key_restrictions
        if server_key_restrictions is not None:
            self._values["server_key_restrictions"] = server_key_restrictions

    @builtins.property
    def android_key_restrictions(
        self,
    ) -> typing.Optional["GoogleApikeysKeyRestrictionsAndroidKeyRestrictions"]:
        '''android_key_restrictions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#android_key_restrictions GoogleApikeysKey#android_key_restrictions}
        '''
        result = self._values.get("android_key_restrictions")
        return typing.cast(typing.Optional["GoogleApikeysKeyRestrictionsAndroidKeyRestrictions"], result)

    @builtins.property
    def api_targets(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleApikeysKeyRestrictionsApiTargets"]]]:
        '''api_targets block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#api_targets GoogleApikeysKey#api_targets}
        '''
        result = self._values.get("api_targets")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleApikeysKeyRestrictionsApiTargets"]]], result)

    @builtins.property
    def browser_key_restrictions(
        self,
    ) -> typing.Optional["GoogleApikeysKeyRestrictionsBrowserKeyRestrictions"]:
        '''browser_key_restrictions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#browser_key_restrictions GoogleApikeysKey#browser_key_restrictions}
        '''
        result = self._values.get("browser_key_restrictions")
        return typing.cast(typing.Optional["GoogleApikeysKeyRestrictionsBrowserKeyRestrictions"], result)

    @builtins.property
    def ios_key_restrictions(
        self,
    ) -> typing.Optional["GoogleApikeysKeyRestrictionsIosKeyRestrictions"]:
        '''ios_key_restrictions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#ios_key_restrictions GoogleApikeysKey#ios_key_restrictions}
        '''
        result = self._values.get("ios_key_restrictions")
        return typing.cast(typing.Optional["GoogleApikeysKeyRestrictionsIosKeyRestrictions"], result)

    @builtins.property
    def server_key_restrictions(
        self,
    ) -> typing.Optional["GoogleApikeysKeyRestrictionsServerKeyRestrictions"]:
        '''server_key_restrictions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#server_key_restrictions GoogleApikeysKey#server_key_restrictions}
        '''
        result = self._values.get("server_key_restrictions")
        return typing.cast(typing.Optional["GoogleApikeysKeyRestrictionsServerKeyRestrictions"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleApikeysKeyRestrictions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleApikeysKey.GoogleApikeysKeyRestrictionsAndroidKeyRestrictions",
    jsii_struct_bases=[],
    name_mapping={"allowed_applications": "allowedApplications"},
)
class GoogleApikeysKeyRestrictionsAndroidKeyRestrictions:
    def __init__(
        self,
        *,
        allowed_applications: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplications", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param allowed_applications: allowed_applications block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#allowed_applications GoogleApikeysKey#allowed_applications}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApikeysKeyRestrictionsAndroidKeyRestrictions.__init__)
            check_type(argname="argument allowed_applications", value=allowed_applications, expected_type=type_hints["allowed_applications"])
        self._values: typing.Dict[str, typing.Any] = {
            "allowed_applications": allowed_applications,
        }

    @builtins.property
    def allowed_applications(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplications"]]:
        '''allowed_applications block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#allowed_applications GoogleApikeysKey#allowed_applications}
        '''
        result = self._values.get("allowed_applications")
        assert result is not None, "Required property 'allowed_applications' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplications"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleApikeysKeyRestrictionsAndroidKeyRestrictions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleApikeysKey.GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplications",
    jsii_struct_bases=[],
    name_mapping={
        "package_name": "packageName",
        "sha1_fingerprint": "sha1Fingerprint",
    },
)
class GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplications:
    def __init__(
        self,
        *,
        package_name: builtins.str,
        sha1_fingerprint: builtins.str,
    ) -> None:
        '''
        :param package_name: The package name of the application. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#package_name GoogleApikeysKey#package_name}
        :param sha1_fingerprint: The SHA1 fingerprint of the application. For example, both sha1 formats are acceptable : DA:39:A3:EE:5E:6B:4B:0D:32:55:BF:EF:95:60:18:90:AF:D8:07:09 or DA39A3EE5E6B4B0D3255BFEF95601890AFD80709. Output format is the latter. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#sha1_fingerprint GoogleApikeysKey#sha1_fingerprint}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplications.__init__)
            check_type(argname="argument package_name", value=package_name, expected_type=type_hints["package_name"])
            check_type(argname="argument sha1_fingerprint", value=sha1_fingerprint, expected_type=type_hints["sha1_fingerprint"])
        self._values: typing.Dict[str, typing.Any] = {
            "package_name": package_name,
            "sha1_fingerprint": sha1_fingerprint,
        }

    @builtins.property
    def package_name(self) -> builtins.str:
        '''The package name of the application.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#package_name GoogleApikeysKey#package_name}
        '''
        result = self._values.get("package_name")
        assert result is not None, "Required property 'package_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sha1_fingerprint(self) -> builtins.str:
        '''The SHA1 fingerprint of the application.

        For example, both sha1 formats are acceptable : DA:39:A3:EE:5E:6B:4B:0D:32:55:BF:EF:95:60:18:90:AF:D8:07:09 or DA39A3EE5E6B4B0D3255BFEF95601890AFD80709. Output format is the latter.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#sha1_fingerprint GoogleApikeysKey#sha1_fingerprint}
        '''
        result = self._values.get("sha1_fingerprint")
        assert result is not None, "Required property 'sha1_fingerprint' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplications(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplicationsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleApikeysKey.GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplicationsList",
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
            type_hints = typing.get_type_hints(GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplicationsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplicationsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplicationsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplicationsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplicationsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplicationsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplicationsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplications]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplications]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplications]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplicationsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplicationsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleApikeysKey.GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplicationsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplicationsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="packageNameInput")
    def package_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "packageNameInput"))

    @builtins.property
    @jsii.member(jsii_name="sha1FingerprintInput")
    def sha1_fingerprint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sha1FingerprintInput"))

    @builtins.property
    @jsii.member(jsii_name="packageName")
    def package_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "packageName"))

    @package_name.setter
    def package_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplicationsOutputReference, "package_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "packageName", value)

    @builtins.property
    @jsii.member(jsii_name="sha1Fingerprint")
    def sha1_fingerprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sha1Fingerprint"))

    @sha1_fingerprint.setter
    def sha1_fingerprint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplicationsOutputReference, "sha1_fingerprint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sha1Fingerprint", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplications, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplications, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplications, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplicationsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleApikeysKey.GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAllowedApplications")
    def put_allowed_applications(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplications, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsOutputReference.put_allowed_applications)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAllowedApplications", [value]))

    @builtins.property
    @jsii.member(jsii_name="allowedApplications")
    def allowed_applications(
        self,
    ) -> GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplicationsList:
        return typing.cast(GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplicationsList, jsii.get(self, "allowedApplications"))

    @builtins.property
    @jsii.member(jsii_name="allowedApplicationsInput")
    def allowed_applications_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplications]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplications]]], jsii.get(self, "allowedApplicationsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleApikeysKeyRestrictionsAndroidKeyRestrictions]:
        return typing.cast(typing.Optional[GoogleApikeysKeyRestrictionsAndroidKeyRestrictions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleApikeysKeyRestrictionsAndroidKeyRestrictions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleApikeysKey.GoogleApikeysKeyRestrictionsApiTargets",
    jsii_struct_bases=[],
    name_mapping={"service": "service", "methods": "methods"},
)
class GoogleApikeysKeyRestrictionsApiTargets:
    def __init__(
        self,
        *,
        service: builtins.str,
        methods: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param service: The service for this restriction. It should be the canonical service name, for example: ``translate.googleapis.com``. You can use ``gcloud services list`` to get a list of services that are enabled in the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#service GoogleApikeysKey#service}
        :param methods: Optional. List of one or more methods that can be called. If empty, all methods for the service are allowed. A wildcard (*) can be used as the last symbol. Valid examples: ``google.cloud.translate.v2.TranslateService.GetSupportedLanguage`` ``TranslateText`` ``Get*`` ``translate.googleapis.com.Get*`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#methods GoogleApikeysKey#methods}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApikeysKeyRestrictionsApiTargets.__init__)
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument methods", value=methods, expected_type=type_hints["methods"])
        self._values: typing.Dict[str, typing.Any] = {
            "service": service,
        }
        if methods is not None:
            self._values["methods"] = methods

    @builtins.property
    def service(self) -> builtins.str:
        '''The service for this restriction.

        It should be the canonical service name, for example: ``translate.googleapis.com``. You can use ``gcloud services list`` to get a list of services that are enabled in the project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#service GoogleApikeysKey#service}
        '''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def methods(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        List of one or more methods that can be called. If empty, all methods for the service are allowed. A wildcard (*) can be used as the last symbol. Valid examples: ``google.cloud.translate.v2.TranslateService.GetSupportedLanguage`` ``TranslateText`` ``Get*`` ``translate.googleapis.com.Get*``

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#methods GoogleApikeysKey#methods}
        '''
        result = self._values.get("methods")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleApikeysKeyRestrictionsApiTargets(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleApikeysKeyRestrictionsApiTargetsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleApikeysKey.GoogleApikeysKeyRestrictionsApiTargetsList",
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
            type_hints = typing.get_type_hints(GoogleApikeysKeyRestrictionsApiTargetsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleApikeysKeyRestrictionsApiTargetsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApikeysKeyRestrictionsApiTargetsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleApikeysKeyRestrictionsApiTargetsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApikeysKeyRestrictionsApiTargetsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleApikeysKeyRestrictionsApiTargetsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleApikeysKeyRestrictionsApiTargetsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleApikeysKeyRestrictionsApiTargets]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleApikeysKeyRestrictionsApiTargets]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleApikeysKeyRestrictionsApiTargets]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApikeysKeyRestrictionsApiTargetsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleApikeysKeyRestrictionsApiTargetsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleApikeysKey.GoogleApikeysKeyRestrictionsApiTargetsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleApikeysKeyRestrictionsApiTargetsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMethods")
    def reset_methods(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMethods", []))

    @builtins.property
    @jsii.member(jsii_name="methodsInput")
    def methods_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "methodsInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="methods")
    def methods(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "methods"))

    @methods.setter
    def methods(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApikeysKeyRestrictionsApiTargetsOutputReference, "methods").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "methods", value)

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "service"))

    @service.setter
    def service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApikeysKeyRestrictionsApiTargetsOutputReference, "service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleApikeysKeyRestrictionsApiTargets, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleApikeysKeyRestrictionsApiTargets, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleApikeysKeyRestrictionsApiTargets, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApikeysKeyRestrictionsApiTargetsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleApikeysKey.GoogleApikeysKeyRestrictionsBrowserKeyRestrictions",
    jsii_struct_bases=[],
    name_mapping={"allowed_referrers": "allowedReferrers"},
)
class GoogleApikeysKeyRestrictionsBrowserKeyRestrictions:
    def __init__(self, *, allowed_referrers: typing.Sequence[builtins.str]) -> None:
        '''
        :param allowed_referrers: A list of regular expressions for the referrer URLs that are allowed to make API calls with this key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#allowed_referrers GoogleApikeysKey#allowed_referrers}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApikeysKeyRestrictionsBrowserKeyRestrictions.__init__)
            check_type(argname="argument allowed_referrers", value=allowed_referrers, expected_type=type_hints["allowed_referrers"])
        self._values: typing.Dict[str, typing.Any] = {
            "allowed_referrers": allowed_referrers,
        }

    @builtins.property
    def allowed_referrers(self) -> typing.List[builtins.str]:
        '''A list of regular expressions for the referrer URLs that are allowed to make API calls with this key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#allowed_referrers GoogleApikeysKey#allowed_referrers}
        '''
        result = self._values.get("allowed_referrers")
        assert result is not None, "Required property 'allowed_referrers' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleApikeysKeyRestrictionsBrowserKeyRestrictions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleApikeysKeyRestrictionsBrowserKeyRestrictionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleApikeysKey.GoogleApikeysKeyRestrictionsBrowserKeyRestrictionsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleApikeysKeyRestrictionsBrowserKeyRestrictionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="allowedReferrersInput")
    def allowed_referrers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedReferrersInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedReferrers")
    def allowed_referrers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedReferrers"))

    @allowed_referrers.setter
    def allowed_referrers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApikeysKeyRestrictionsBrowserKeyRestrictionsOutputReference, "allowed_referrers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedReferrers", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleApikeysKeyRestrictionsBrowserKeyRestrictions]:
        return typing.cast(typing.Optional[GoogleApikeysKeyRestrictionsBrowserKeyRestrictions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleApikeysKeyRestrictionsBrowserKeyRestrictions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApikeysKeyRestrictionsBrowserKeyRestrictionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleApikeysKey.GoogleApikeysKeyRestrictionsIosKeyRestrictions",
    jsii_struct_bases=[],
    name_mapping={"allowed_bundle_ids": "allowedBundleIds"},
)
class GoogleApikeysKeyRestrictionsIosKeyRestrictions:
    def __init__(self, *, allowed_bundle_ids: typing.Sequence[builtins.str]) -> None:
        '''
        :param allowed_bundle_ids: A list of bundle IDs that are allowed when making API calls with this key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#allowed_bundle_ids GoogleApikeysKey#allowed_bundle_ids}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApikeysKeyRestrictionsIosKeyRestrictions.__init__)
            check_type(argname="argument allowed_bundle_ids", value=allowed_bundle_ids, expected_type=type_hints["allowed_bundle_ids"])
        self._values: typing.Dict[str, typing.Any] = {
            "allowed_bundle_ids": allowed_bundle_ids,
        }

    @builtins.property
    def allowed_bundle_ids(self) -> typing.List[builtins.str]:
        '''A list of bundle IDs that are allowed when making API calls with this key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#allowed_bundle_ids GoogleApikeysKey#allowed_bundle_ids}
        '''
        result = self._values.get("allowed_bundle_ids")
        assert result is not None, "Required property 'allowed_bundle_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleApikeysKeyRestrictionsIosKeyRestrictions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleApikeysKeyRestrictionsIosKeyRestrictionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleApikeysKey.GoogleApikeysKeyRestrictionsIosKeyRestrictionsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleApikeysKeyRestrictionsIosKeyRestrictionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="allowedBundleIdsInput")
    def allowed_bundle_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedBundleIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedBundleIds")
    def allowed_bundle_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedBundleIds"))

    @allowed_bundle_ids.setter
    def allowed_bundle_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApikeysKeyRestrictionsIosKeyRestrictionsOutputReference, "allowed_bundle_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedBundleIds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleApikeysKeyRestrictionsIosKeyRestrictions]:
        return typing.cast(typing.Optional[GoogleApikeysKeyRestrictionsIosKeyRestrictions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleApikeysKeyRestrictionsIosKeyRestrictions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApikeysKeyRestrictionsIosKeyRestrictionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleApikeysKeyRestrictionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleApikeysKey.GoogleApikeysKeyRestrictionsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleApikeysKeyRestrictionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAndroidKeyRestrictions")
    def put_android_key_restrictions(
        self,
        *,
        allowed_applications: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplications, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param allowed_applications: allowed_applications block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#allowed_applications GoogleApikeysKey#allowed_applications}
        '''
        value = GoogleApikeysKeyRestrictionsAndroidKeyRestrictions(
            allowed_applications=allowed_applications
        )

        return typing.cast(None, jsii.invoke(self, "putAndroidKeyRestrictions", [value]))

    @jsii.member(jsii_name="putApiTargets")
    def put_api_targets(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleApikeysKeyRestrictionsApiTargets, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApikeysKeyRestrictionsOutputReference.put_api_targets)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putApiTargets", [value]))

    @jsii.member(jsii_name="putBrowserKeyRestrictions")
    def put_browser_key_restrictions(
        self,
        *,
        allowed_referrers: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param allowed_referrers: A list of regular expressions for the referrer URLs that are allowed to make API calls with this key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#allowed_referrers GoogleApikeysKey#allowed_referrers}
        '''
        value = GoogleApikeysKeyRestrictionsBrowserKeyRestrictions(
            allowed_referrers=allowed_referrers
        )

        return typing.cast(None, jsii.invoke(self, "putBrowserKeyRestrictions", [value]))

    @jsii.member(jsii_name="putIosKeyRestrictions")
    def put_ios_key_restrictions(
        self,
        *,
        allowed_bundle_ids: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param allowed_bundle_ids: A list of bundle IDs that are allowed when making API calls with this key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#allowed_bundle_ids GoogleApikeysKey#allowed_bundle_ids}
        '''
        value = GoogleApikeysKeyRestrictionsIosKeyRestrictions(
            allowed_bundle_ids=allowed_bundle_ids
        )

        return typing.cast(None, jsii.invoke(self, "putIosKeyRestrictions", [value]))

    @jsii.member(jsii_name="putServerKeyRestrictions")
    def put_server_key_restrictions(
        self,
        *,
        allowed_ips: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param allowed_ips: A list of the caller IP addresses that are allowed to make API calls with this key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#allowed_ips GoogleApikeysKey#allowed_ips}
        '''
        value = GoogleApikeysKeyRestrictionsServerKeyRestrictions(
            allowed_ips=allowed_ips
        )

        return typing.cast(None, jsii.invoke(self, "putServerKeyRestrictions", [value]))

    @jsii.member(jsii_name="resetAndroidKeyRestrictions")
    def reset_android_key_restrictions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAndroidKeyRestrictions", []))

    @jsii.member(jsii_name="resetApiTargets")
    def reset_api_targets(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiTargets", []))

    @jsii.member(jsii_name="resetBrowserKeyRestrictions")
    def reset_browser_key_restrictions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBrowserKeyRestrictions", []))

    @jsii.member(jsii_name="resetIosKeyRestrictions")
    def reset_ios_key_restrictions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIosKeyRestrictions", []))

    @jsii.member(jsii_name="resetServerKeyRestrictions")
    def reset_server_key_restrictions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServerKeyRestrictions", []))

    @builtins.property
    @jsii.member(jsii_name="androidKeyRestrictions")
    def android_key_restrictions(
        self,
    ) -> GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsOutputReference:
        return typing.cast(GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsOutputReference, jsii.get(self, "androidKeyRestrictions"))

    @builtins.property
    @jsii.member(jsii_name="apiTargets")
    def api_targets(self) -> GoogleApikeysKeyRestrictionsApiTargetsList:
        return typing.cast(GoogleApikeysKeyRestrictionsApiTargetsList, jsii.get(self, "apiTargets"))

    @builtins.property
    @jsii.member(jsii_name="browserKeyRestrictions")
    def browser_key_restrictions(
        self,
    ) -> GoogleApikeysKeyRestrictionsBrowserKeyRestrictionsOutputReference:
        return typing.cast(GoogleApikeysKeyRestrictionsBrowserKeyRestrictionsOutputReference, jsii.get(self, "browserKeyRestrictions"))

    @builtins.property
    @jsii.member(jsii_name="iosKeyRestrictions")
    def ios_key_restrictions(
        self,
    ) -> GoogleApikeysKeyRestrictionsIosKeyRestrictionsOutputReference:
        return typing.cast(GoogleApikeysKeyRestrictionsIosKeyRestrictionsOutputReference, jsii.get(self, "iosKeyRestrictions"))

    @builtins.property
    @jsii.member(jsii_name="serverKeyRestrictions")
    def server_key_restrictions(
        self,
    ) -> "GoogleApikeysKeyRestrictionsServerKeyRestrictionsOutputReference":
        return typing.cast("GoogleApikeysKeyRestrictionsServerKeyRestrictionsOutputReference", jsii.get(self, "serverKeyRestrictions"))

    @builtins.property
    @jsii.member(jsii_name="androidKeyRestrictionsInput")
    def android_key_restrictions_input(
        self,
    ) -> typing.Optional[GoogleApikeysKeyRestrictionsAndroidKeyRestrictions]:
        return typing.cast(typing.Optional[GoogleApikeysKeyRestrictionsAndroidKeyRestrictions], jsii.get(self, "androidKeyRestrictionsInput"))

    @builtins.property
    @jsii.member(jsii_name="apiTargetsInput")
    def api_targets_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleApikeysKeyRestrictionsApiTargets]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleApikeysKeyRestrictionsApiTargets]]], jsii.get(self, "apiTargetsInput"))

    @builtins.property
    @jsii.member(jsii_name="browserKeyRestrictionsInput")
    def browser_key_restrictions_input(
        self,
    ) -> typing.Optional[GoogleApikeysKeyRestrictionsBrowserKeyRestrictions]:
        return typing.cast(typing.Optional[GoogleApikeysKeyRestrictionsBrowserKeyRestrictions], jsii.get(self, "browserKeyRestrictionsInput"))

    @builtins.property
    @jsii.member(jsii_name="iosKeyRestrictionsInput")
    def ios_key_restrictions_input(
        self,
    ) -> typing.Optional[GoogleApikeysKeyRestrictionsIosKeyRestrictions]:
        return typing.cast(typing.Optional[GoogleApikeysKeyRestrictionsIosKeyRestrictions], jsii.get(self, "iosKeyRestrictionsInput"))

    @builtins.property
    @jsii.member(jsii_name="serverKeyRestrictionsInput")
    def server_key_restrictions_input(
        self,
    ) -> typing.Optional["GoogleApikeysKeyRestrictionsServerKeyRestrictions"]:
        return typing.cast(typing.Optional["GoogleApikeysKeyRestrictionsServerKeyRestrictions"], jsii.get(self, "serverKeyRestrictionsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleApikeysKeyRestrictions]:
        return typing.cast(typing.Optional[GoogleApikeysKeyRestrictions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleApikeysKeyRestrictions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApikeysKeyRestrictionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleApikeysKey.GoogleApikeysKeyRestrictionsServerKeyRestrictions",
    jsii_struct_bases=[],
    name_mapping={"allowed_ips": "allowedIps"},
)
class GoogleApikeysKeyRestrictionsServerKeyRestrictions:
    def __init__(self, *, allowed_ips: typing.Sequence[builtins.str]) -> None:
        '''
        :param allowed_ips: A list of the caller IP addresses that are allowed to make API calls with this key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#allowed_ips GoogleApikeysKey#allowed_ips}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApikeysKeyRestrictionsServerKeyRestrictions.__init__)
            check_type(argname="argument allowed_ips", value=allowed_ips, expected_type=type_hints["allowed_ips"])
        self._values: typing.Dict[str, typing.Any] = {
            "allowed_ips": allowed_ips,
        }

    @builtins.property
    def allowed_ips(self) -> typing.List[builtins.str]:
        '''A list of the caller IP addresses that are allowed to make API calls with this key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#allowed_ips GoogleApikeysKey#allowed_ips}
        '''
        result = self._values.get("allowed_ips")
        assert result is not None, "Required property 'allowed_ips' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleApikeysKeyRestrictionsServerKeyRestrictions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleApikeysKeyRestrictionsServerKeyRestrictionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleApikeysKey.GoogleApikeysKeyRestrictionsServerKeyRestrictionsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleApikeysKeyRestrictionsServerKeyRestrictionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="allowedIpsInput")
    def allowed_ips_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedIpsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedIps")
    def allowed_ips(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedIps"))

    @allowed_ips.setter
    def allowed_ips(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApikeysKeyRestrictionsServerKeyRestrictionsOutputReference, "allowed_ips").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedIps", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleApikeysKeyRestrictionsServerKeyRestrictions]:
        return typing.cast(typing.Optional[GoogleApikeysKeyRestrictionsServerKeyRestrictions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleApikeysKeyRestrictionsServerKeyRestrictions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApikeysKeyRestrictionsServerKeyRestrictionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleApikeysKey.GoogleApikeysKeyTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleApikeysKeyTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#create GoogleApikeysKey#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#delete GoogleApikeysKey#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#update GoogleApikeysKey#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleApikeysKeyTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#create GoogleApikeysKey#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#delete GoogleApikeysKey#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_apikeys_key#update GoogleApikeysKey#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleApikeysKeyTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleApikeysKeyTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleApikeysKey.GoogleApikeysKeyTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleApikeysKeyTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleApikeysKeyTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApikeysKeyTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApikeysKeyTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleApikeysKeyTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleApikeysKeyTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleApikeysKeyTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleApikeysKeyTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleApikeysKey",
    "GoogleApikeysKeyConfig",
    "GoogleApikeysKeyRestrictions",
    "GoogleApikeysKeyRestrictionsAndroidKeyRestrictions",
    "GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplications",
    "GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplicationsList",
    "GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsAllowedApplicationsOutputReference",
    "GoogleApikeysKeyRestrictionsAndroidKeyRestrictionsOutputReference",
    "GoogleApikeysKeyRestrictionsApiTargets",
    "GoogleApikeysKeyRestrictionsApiTargetsList",
    "GoogleApikeysKeyRestrictionsApiTargetsOutputReference",
    "GoogleApikeysKeyRestrictionsBrowserKeyRestrictions",
    "GoogleApikeysKeyRestrictionsBrowserKeyRestrictionsOutputReference",
    "GoogleApikeysKeyRestrictionsIosKeyRestrictions",
    "GoogleApikeysKeyRestrictionsIosKeyRestrictionsOutputReference",
    "GoogleApikeysKeyRestrictionsOutputReference",
    "GoogleApikeysKeyRestrictionsServerKeyRestrictions",
    "GoogleApikeysKeyRestrictionsServerKeyRestrictionsOutputReference",
    "GoogleApikeysKeyTimeouts",
    "GoogleApikeysKeyTimeoutsOutputReference",
]

publication.publish()
