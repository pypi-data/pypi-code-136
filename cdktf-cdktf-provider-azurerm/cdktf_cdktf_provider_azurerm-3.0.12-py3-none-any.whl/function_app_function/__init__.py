'''
# `azurerm_function_app_function`

Refer to the Terraform Registory for docs: [`azurerm_function_app_function`](https://www.terraform.io/docs/providers/azurerm/r/function_app_function).
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


class FunctionAppFunction(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.functionAppFunction.FunctionAppFunction",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function azurerm_function_app_function}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        config_json: builtins.str,
        function_app_id: builtins.str,
        name: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        file: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FunctionAppFunctionFile", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        language: typing.Optional[builtins.str] = None,
        test_data: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["FunctionAppFunctionTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function azurerm_function_app_function} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param config_json: The config for this Function in JSON format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#config_json FunctionAppFunction#config_json}
        :param function_app_id: The ID of the Function App in which this function should reside. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#function_app_id FunctionAppFunction#function_app_id}
        :param name: The name of the function. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#name FunctionAppFunction#name}
        :param enabled: Should this function be enabled. Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#enabled FunctionAppFunction#enabled}
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#file FunctionAppFunction#file}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#id FunctionAppFunction#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param language: The language the Function is written in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#language FunctionAppFunction#language}
        :param test_data: The test data for the function. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#test_data FunctionAppFunction#test_data}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#timeouts FunctionAppFunction#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FunctionAppFunction.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = FunctionAppFunctionConfig(
            config_json=config_json,
            function_app_id=function_app_id,
            name=name,
            enabled=enabled,
            file=file,
            id=id,
            language=language,
            test_data=test_data,
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

    @jsii.member(jsii_name="putFile")
    def put_file(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FunctionAppFunctionFile", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FunctionAppFunction.put_file)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFile", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#create FunctionAppFunction#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#delete FunctionAppFunction#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#read FunctionAppFunction#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#update FunctionAppFunction#update}.
        '''
        value = FunctionAppFunctionTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @jsii.member(jsii_name="resetFile")
    def reset_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFile", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLanguage")
    def reset_language(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLanguage", []))

    @jsii.member(jsii_name="resetTestData")
    def reset_test_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTestData", []))

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
    @jsii.member(jsii_name="configUrl")
    def config_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configUrl"))

    @builtins.property
    @jsii.member(jsii_name="file")
    def file(self) -> "FunctionAppFunctionFileList":
        return typing.cast("FunctionAppFunctionFileList", jsii.get(self, "file"))

    @builtins.property
    @jsii.member(jsii_name="invocationUrl")
    def invocation_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "invocationUrl"))

    @builtins.property
    @jsii.member(jsii_name="scriptRootPathUrl")
    def script_root_path_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scriptRootPathUrl"))

    @builtins.property
    @jsii.member(jsii_name="scriptUrl")
    def script_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scriptUrl"))

    @builtins.property
    @jsii.member(jsii_name="secretsFileUrl")
    def secrets_file_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretsFileUrl"))

    @builtins.property
    @jsii.member(jsii_name="testDataUrl")
    def test_data_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "testDataUrl"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "FunctionAppFunctionTimeoutsOutputReference":
        return typing.cast("FunctionAppFunctionTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @builtins.property
    @jsii.member(jsii_name="configJsonInput")
    def config_json_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "configJsonInput"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="fileInput")
    def file_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FunctionAppFunctionFile"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FunctionAppFunctionFile"]]], jsii.get(self, "fileInput"))

    @builtins.property
    @jsii.member(jsii_name="functionAppIdInput")
    def function_app_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "functionAppIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="languageInput")
    def language_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "languageInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="testDataInput")
    def test_data_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "testDataInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["FunctionAppFunctionTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["FunctionAppFunctionTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="configJson")
    def config_json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "configJson"))

    @config_json.setter
    def config_json(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FunctionAppFunction, "config_json").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configJson", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FunctionAppFunction, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="functionAppId")
    def function_app_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "functionAppId"))

    @function_app_id.setter
    def function_app_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FunctionAppFunction, "function_app_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionAppId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FunctionAppFunction, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="language")
    def language(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "language"))

    @language.setter
    def language(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FunctionAppFunction, "language").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "language", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FunctionAppFunction, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="testData")
    def test_data(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "testData"))

    @test_data.setter
    def test_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FunctionAppFunction, "test_data").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "testData", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.functionAppFunction.FunctionAppFunctionConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "config_json": "configJson",
        "function_app_id": "functionAppId",
        "name": "name",
        "enabled": "enabled",
        "file": "file",
        "id": "id",
        "language": "language",
        "test_data": "testData",
        "timeouts": "timeouts",
    },
)
class FunctionAppFunctionConfig(cdktf.TerraformMetaArguments):
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
        config_json: builtins.str,
        function_app_id: builtins.str,
        name: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        file: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["FunctionAppFunctionFile", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        language: typing.Optional[builtins.str] = None,
        test_data: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["FunctionAppFunctionTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param config_json: The config for this Function in JSON format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#config_json FunctionAppFunction#config_json}
        :param function_app_id: The ID of the Function App in which this function should reside. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#function_app_id FunctionAppFunction#function_app_id}
        :param name: The name of the function. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#name FunctionAppFunction#name}
        :param enabled: Should this function be enabled. Defaults to ``true``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#enabled FunctionAppFunction#enabled}
        :param file: file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#file FunctionAppFunction#file}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#id FunctionAppFunction#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param language: The language the Function is written in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#language FunctionAppFunction#language}
        :param test_data: The test data for the function. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#test_data FunctionAppFunction#test_data}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#timeouts FunctionAppFunction#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = FunctionAppFunctionTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(FunctionAppFunctionConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument config_json", value=config_json, expected_type=type_hints["config_json"])
            check_type(argname="argument function_app_id", value=function_app_id, expected_type=type_hints["function_app_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument file", value=file, expected_type=type_hints["file"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument language", value=language, expected_type=type_hints["language"])
            check_type(argname="argument test_data", value=test_data, expected_type=type_hints["test_data"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "config_json": config_json,
            "function_app_id": function_app_id,
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
        if enabled is not None:
            self._values["enabled"] = enabled
        if file is not None:
            self._values["file"] = file
        if id is not None:
            self._values["id"] = id
        if language is not None:
            self._values["language"] = language
        if test_data is not None:
            self._values["test_data"] = test_data
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
    def config_json(self) -> builtins.str:
        '''The config for this Function in JSON format.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#config_json FunctionAppFunction#config_json}
        '''
        result = self._values.get("config_json")
        assert result is not None, "Required property 'config_json' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def function_app_id(self) -> builtins.str:
        '''The ID of the Function App in which this function should reside.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#function_app_id FunctionAppFunction#function_app_id}
        '''
        result = self._values.get("function_app_id")
        assert result is not None, "Required property 'function_app_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the function.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#name FunctionAppFunction#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Should this function be enabled. Defaults to ``true``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#enabled FunctionAppFunction#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def file(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FunctionAppFunctionFile"]]]:
        '''file block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#file FunctionAppFunction#file}
        '''
        result = self._values.get("file")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["FunctionAppFunctionFile"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#id FunctionAppFunction#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def language(self) -> typing.Optional[builtins.str]:
        '''The language the Function is written in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#language FunctionAppFunction#language}
        '''
        result = self._values.get("language")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def test_data(self) -> typing.Optional[builtins.str]:
        '''The test data for the function.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#test_data FunctionAppFunction#test_data}
        '''
        result = self._values.get("test_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["FunctionAppFunctionTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#timeouts FunctionAppFunction#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["FunctionAppFunctionTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FunctionAppFunctionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.functionAppFunction.FunctionAppFunctionFile",
    jsii_struct_bases=[],
    name_mapping={"content": "content", "name": "name"},
)
class FunctionAppFunctionFile:
    def __init__(self, *, content: builtins.str, name: builtins.str) -> None:
        '''
        :param content: The content of the file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#content FunctionAppFunction#content}
        :param name: The filename of the file to be uploaded. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#name FunctionAppFunction#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FunctionAppFunctionFile.__init__)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
            "name": name,
        }

    @builtins.property
    def content(self) -> builtins.str:
        '''The content of the file.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#content FunctionAppFunction#content}
        '''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The filename of the file to be uploaded.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#name FunctionAppFunction#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FunctionAppFunctionFile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FunctionAppFunctionFileList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.functionAppFunction.FunctionAppFunctionFileList",
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
            type_hints = typing.get_type_hints(FunctionAppFunctionFileList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "FunctionAppFunctionFileOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FunctionAppFunctionFileList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("FunctionAppFunctionFileOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FunctionAppFunctionFileList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(FunctionAppFunctionFileList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(FunctionAppFunctionFileList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FunctionAppFunctionFile]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FunctionAppFunctionFile]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[FunctionAppFunctionFile]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FunctionAppFunctionFileList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class FunctionAppFunctionFileOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.functionAppFunction.FunctionAppFunctionFileOutputReference",
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
            type_hints = typing.get_type_hints(FunctionAppFunctionFileOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FunctionAppFunctionFileOutputReference, "content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FunctionAppFunctionFileOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[FunctionAppFunctionFile, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FunctionAppFunctionFile, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FunctionAppFunctionFile, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FunctionAppFunctionFileOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.functionAppFunction.FunctionAppFunctionTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class FunctionAppFunctionTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#create FunctionAppFunction#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#delete FunctionAppFunction#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#read FunctionAppFunction#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#update FunctionAppFunction#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(FunctionAppFunctionTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if read is not None:
            self._values["read"] = read
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#create FunctionAppFunction#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#delete FunctionAppFunction#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#read FunctionAppFunction#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/function_app_function#update FunctionAppFunction#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "FunctionAppFunctionTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class FunctionAppFunctionTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.functionAppFunction.FunctionAppFunctionTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(FunctionAppFunctionTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetRead")
    def reset_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRead", []))

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
    @jsii.member(jsii_name="readInput")
    def read_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readInput"))

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
            type_hints = typing.get_type_hints(getattr(FunctionAppFunctionTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FunctionAppFunctionTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FunctionAppFunctionTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FunctionAppFunctionTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[FunctionAppFunctionTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[FunctionAppFunctionTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[FunctionAppFunctionTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(FunctionAppFunctionTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "FunctionAppFunction",
    "FunctionAppFunctionConfig",
    "FunctionAppFunctionFile",
    "FunctionAppFunctionFileList",
    "FunctionAppFunctionFileOutputReference",
    "FunctionAppFunctionTimeouts",
    "FunctionAppFunctionTimeoutsOutputReference",
]

publication.publish()
