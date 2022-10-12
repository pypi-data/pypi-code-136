'''
# `google_vertex_ai_featurestore_entitytype`

Refer to the Terraform Registory for docs: [`google_vertex_ai_featurestore_entitytype`](https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype).
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


class GoogleVertexAiFeaturestoreEntitytype(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleVertexAiFeaturestoreEntitytype.GoogleVertexAiFeaturestoreEntitytype",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype google_vertex_ai_featurestore_entitytype}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        featurestore: builtins.str,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        monitoring_config: typing.Optional[typing.Union["GoogleVertexAiFeaturestoreEntitytypeMonitoringConfig", typing.Dict[str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleVertexAiFeaturestoreEntitytypeTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype google_vertex_ai_featurestore_entitytype} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param featurestore: The name of the Featurestore to use, in the format projects/{project}/locations/{location}/featurestores/{featurestore}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#featurestore GoogleVertexAiFeaturestoreEntitytype#featurestore}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#id GoogleVertexAiFeaturestoreEntitytype#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: A set of key/value label pairs to assign to this EntityType. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#labels GoogleVertexAiFeaturestoreEntitytype#labels}
        :param monitoring_config: monitoring_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#monitoring_config GoogleVertexAiFeaturestoreEntitytype#monitoring_config}
        :param name: The name of the EntityType. This value may be up to 60 characters, and valid characters are [a-z0-9_]. The first character cannot be a number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#name GoogleVertexAiFeaturestoreEntitytype#name}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#timeouts GoogleVertexAiFeaturestoreEntitytype#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleVertexAiFeaturestoreEntitytype.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleVertexAiFeaturestoreEntitytypeConfig(
            featurestore=featurestore,
            id=id,
            labels=labels,
            monitoring_config=monitoring_config,
            name=name,
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

    @jsii.member(jsii_name="putMonitoringConfig")
    def put_monitoring_config(
        self,
        *,
        snapshot_analysis: typing.Optional[typing.Union["GoogleVertexAiFeaturestoreEntitytypeMonitoringConfigSnapshotAnalysis", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param snapshot_analysis: snapshot_analysis block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#snapshot_analysis GoogleVertexAiFeaturestoreEntitytype#snapshot_analysis}
        '''
        value = GoogleVertexAiFeaturestoreEntitytypeMonitoringConfig(
            snapshot_analysis=snapshot_analysis
        )

        return typing.cast(None, jsii.invoke(self, "putMonitoringConfig", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#create GoogleVertexAiFeaturestoreEntitytype#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#delete GoogleVertexAiFeaturestoreEntitytype#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#update GoogleVertexAiFeaturestoreEntitytype#update}.
        '''
        value = GoogleVertexAiFeaturestoreEntitytypeTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetMonitoringConfig")
    def reset_monitoring_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonitoringConfig", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

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
    @jsii.member(jsii_name="etag")
    def etag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "etag"))

    @builtins.property
    @jsii.member(jsii_name="monitoringConfig")
    def monitoring_config(
        self,
    ) -> "GoogleVertexAiFeaturestoreEntitytypeMonitoringConfigOutputReference":
        return typing.cast("GoogleVertexAiFeaturestoreEntitytypeMonitoringConfigOutputReference", jsii.get(self, "monitoringConfig"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleVertexAiFeaturestoreEntitytypeTimeoutsOutputReference":
        return typing.cast("GoogleVertexAiFeaturestoreEntitytypeTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="updateTime")
    def update_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updateTime"))

    @builtins.property
    @jsii.member(jsii_name="featurestoreInput")
    def featurestore_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "featurestoreInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="monitoringConfigInput")
    def monitoring_config_input(
        self,
    ) -> typing.Optional["GoogleVertexAiFeaturestoreEntitytypeMonitoringConfig"]:
        return typing.cast(typing.Optional["GoogleVertexAiFeaturestoreEntitytypeMonitoringConfig"], jsii.get(self, "monitoringConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleVertexAiFeaturestoreEntitytypeTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleVertexAiFeaturestoreEntitytypeTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="featurestore")
    def featurestore(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "featurestore"))

    @featurestore.setter
    def featurestore(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleVertexAiFeaturestoreEntitytype, "featurestore").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "featurestore", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleVertexAiFeaturestoreEntitytype, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleVertexAiFeaturestoreEntitytype, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleVertexAiFeaturestoreEntitytype, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleVertexAiFeaturestoreEntitytype.GoogleVertexAiFeaturestoreEntitytypeConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "featurestore": "featurestore",
        "id": "id",
        "labels": "labels",
        "monitoring_config": "monitoringConfig",
        "name": "name",
        "timeouts": "timeouts",
    },
)
class GoogleVertexAiFeaturestoreEntitytypeConfig(cdktf.TerraformMetaArguments):
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
        featurestore: builtins.str,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        monitoring_config: typing.Optional[typing.Union["GoogleVertexAiFeaturestoreEntitytypeMonitoringConfig", typing.Dict[str, typing.Any]]] = None,
        name: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleVertexAiFeaturestoreEntitytypeTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param featurestore: The name of the Featurestore to use, in the format projects/{project}/locations/{location}/featurestores/{featurestore}. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#featurestore GoogleVertexAiFeaturestoreEntitytype#featurestore}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#id GoogleVertexAiFeaturestoreEntitytype#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: A set of key/value label pairs to assign to this EntityType. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#labels GoogleVertexAiFeaturestoreEntitytype#labels}
        :param monitoring_config: monitoring_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#monitoring_config GoogleVertexAiFeaturestoreEntitytype#monitoring_config}
        :param name: The name of the EntityType. This value may be up to 60 characters, and valid characters are [a-z0-9_]. The first character cannot be a number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#name GoogleVertexAiFeaturestoreEntitytype#name}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#timeouts GoogleVertexAiFeaturestoreEntitytype#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(monitoring_config, dict):
            monitoring_config = GoogleVertexAiFeaturestoreEntitytypeMonitoringConfig(**monitoring_config)
        if isinstance(timeouts, dict):
            timeouts = GoogleVertexAiFeaturestoreEntitytypeTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleVertexAiFeaturestoreEntitytypeConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument featurestore", value=featurestore, expected_type=type_hints["featurestore"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument monitoring_config", value=monitoring_config, expected_type=type_hints["monitoring_config"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "featurestore": featurestore,
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
        if labels is not None:
            self._values["labels"] = labels
        if monitoring_config is not None:
            self._values["monitoring_config"] = monitoring_config
        if name is not None:
            self._values["name"] = name
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
    def featurestore(self) -> builtins.str:
        '''The name of the Featurestore to use, in the format projects/{project}/locations/{location}/featurestores/{featurestore}.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#featurestore GoogleVertexAiFeaturestoreEntitytype#featurestore}
        '''
        result = self._values.get("featurestore")
        assert result is not None, "Required property 'featurestore' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#id GoogleVertexAiFeaturestoreEntitytype#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A set of key/value label pairs to assign to this EntityType.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#labels GoogleVertexAiFeaturestoreEntitytype#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def monitoring_config(
        self,
    ) -> typing.Optional["GoogleVertexAiFeaturestoreEntitytypeMonitoringConfig"]:
        '''monitoring_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#monitoring_config GoogleVertexAiFeaturestoreEntitytype#monitoring_config}
        '''
        result = self._values.get("monitoring_config")
        return typing.cast(typing.Optional["GoogleVertexAiFeaturestoreEntitytypeMonitoringConfig"], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the EntityType.

        This value may be up to 60 characters, and valid characters are [a-z0-9_]. The first character cannot be a number.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#name GoogleVertexAiFeaturestoreEntitytype#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(
        self,
    ) -> typing.Optional["GoogleVertexAiFeaturestoreEntitytypeTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#timeouts GoogleVertexAiFeaturestoreEntitytype#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleVertexAiFeaturestoreEntitytypeTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleVertexAiFeaturestoreEntitytypeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleVertexAiFeaturestoreEntitytype.GoogleVertexAiFeaturestoreEntitytypeMonitoringConfig",
    jsii_struct_bases=[],
    name_mapping={"snapshot_analysis": "snapshotAnalysis"},
)
class GoogleVertexAiFeaturestoreEntitytypeMonitoringConfig:
    def __init__(
        self,
        *,
        snapshot_analysis: typing.Optional[typing.Union["GoogleVertexAiFeaturestoreEntitytypeMonitoringConfigSnapshotAnalysis", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param snapshot_analysis: snapshot_analysis block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#snapshot_analysis GoogleVertexAiFeaturestoreEntitytype#snapshot_analysis}
        '''
        if isinstance(snapshot_analysis, dict):
            snapshot_analysis = GoogleVertexAiFeaturestoreEntitytypeMonitoringConfigSnapshotAnalysis(**snapshot_analysis)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleVertexAiFeaturestoreEntitytypeMonitoringConfig.__init__)
            check_type(argname="argument snapshot_analysis", value=snapshot_analysis, expected_type=type_hints["snapshot_analysis"])
        self._values: typing.Dict[str, typing.Any] = {}
        if snapshot_analysis is not None:
            self._values["snapshot_analysis"] = snapshot_analysis

    @builtins.property
    def snapshot_analysis(
        self,
    ) -> typing.Optional["GoogleVertexAiFeaturestoreEntitytypeMonitoringConfigSnapshotAnalysis"]:
        '''snapshot_analysis block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#snapshot_analysis GoogleVertexAiFeaturestoreEntitytype#snapshot_analysis}
        '''
        result = self._values.get("snapshot_analysis")
        return typing.cast(typing.Optional["GoogleVertexAiFeaturestoreEntitytypeMonitoringConfigSnapshotAnalysis"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleVertexAiFeaturestoreEntitytypeMonitoringConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleVertexAiFeaturestoreEntitytypeMonitoringConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleVertexAiFeaturestoreEntitytype.GoogleVertexAiFeaturestoreEntitytypeMonitoringConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleVertexAiFeaturestoreEntitytypeMonitoringConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSnapshotAnalysis")
    def put_snapshot_analysis(
        self,
        *,
        disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        monitoring_interval: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param disabled: The monitoring schedule for snapshot analysis. For EntityType-level config: unset / disabled = true indicates disabled by default for Features under it; otherwise by default enable snapshot analysis monitoring with monitoringInterval for Features under it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#disabled GoogleVertexAiFeaturestoreEntitytype#disabled}
        :param monitoring_interval: Configuration of the snapshot analysis based monitoring pipeline running interval. The value is rolled up to full day. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#monitoring_interval GoogleVertexAiFeaturestoreEntitytype#monitoring_interval}
        '''
        value = GoogleVertexAiFeaturestoreEntitytypeMonitoringConfigSnapshotAnalysis(
            disabled=disabled, monitoring_interval=monitoring_interval
        )

        return typing.cast(None, jsii.invoke(self, "putSnapshotAnalysis", [value]))

    @jsii.member(jsii_name="resetSnapshotAnalysis")
    def reset_snapshot_analysis(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSnapshotAnalysis", []))

    @builtins.property
    @jsii.member(jsii_name="snapshotAnalysis")
    def snapshot_analysis(
        self,
    ) -> "GoogleVertexAiFeaturestoreEntitytypeMonitoringConfigSnapshotAnalysisOutputReference":
        return typing.cast("GoogleVertexAiFeaturestoreEntitytypeMonitoringConfigSnapshotAnalysisOutputReference", jsii.get(self, "snapshotAnalysis"))

    @builtins.property
    @jsii.member(jsii_name="snapshotAnalysisInput")
    def snapshot_analysis_input(
        self,
    ) -> typing.Optional["GoogleVertexAiFeaturestoreEntitytypeMonitoringConfigSnapshotAnalysis"]:
        return typing.cast(typing.Optional["GoogleVertexAiFeaturestoreEntitytypeMonitoringConfigSnapshotAnalysis"], jsii.get(self, "snapshotAnalysisInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleVertexAiFeaturestoreEntitytypeMonitoringConfig]:
        return typing.cast(typing.Optional[GoogleVertexAiFeaturestoreEntitytypeMonitoringConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleVertexAiFeaturestoreEntitytypeMonitoringConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleVertexAiFeaturestoreEntitytypeMonitoringConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleVertexAiFeaturestoreEntitytype.GoogleVertexAiFeaturestoreEntitytypeMonitoringConfigSnapshotAnalysis",
    jsii_struct_bases=[],
    name_mapping={"disabled": "disabled", "monitoring_interval": "monitoringInterval"},
)
class GoogleVertexAiFeaturestoreEntitytypeMonitoringConfigSnapshotAnalysis:
    def __init__(
        self,
        *,
        disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        monitoring_interval: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param disabled: The monitoring schedule for snapshot analysis. For EntityType-level config: unset / disabled = true indicates disabled by default for Features under it; otherwise by default enable snapshot analysis monitoring with monitoringInterval for Features under it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#disabled GoogleVertexAiFeaturestoreEntitytype#disabled}
        :param monitoring_interval: Configuration of the snapshot analysis based monitoring pipeline running interval. The value is rolled up to full day. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#monitoring_interval GoogleVertexAiFeaturestoreEntitytype#monitoring_interval}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleVertexAiFeaturestoreEntitytypeMonitoringConfigSnapshotAnalysis.__init__)
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
            check_type(argname="argument monitoring_interval", value=monitoring_interval, expected_type=type_hints["monitoring_interval"])
        self._values: typing.Dict[str, typing.Any] = {}
        if disabled is not None:
            self._values["disabled"] = disabled
        if monitoring_interval is not None:
            self._values["monitoring_interval"] = monitoring_interval

    @builtins.property
    def disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''The monitoring schedule for snapshot analysis.

        For EntityType-level config: unset / disabled = true indicates disabled by default for Features under it; otherwise by default enable snapshot analysis monitoring with monitoringInterval for Features under it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#disabled GoogleVertexAiFeaturestoreEntitytype#disabled}
        '''
        result = self._values.get("disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def monitoring_interval(self) -> typing.Optional[builtins.str]:
        '''Configuration of the snapshot analysis based monitoring pipeline running interval. The value is rolled up to full day.

        A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#monitoring_interval GoogleVertexAiFeaturestoreEntitytype#monitoring_interval}
        '''
        result = self._values.get("monitoring_interval")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleVertexAiFeaturestoreEntitytypeMonitoringConfigSnapshotAnalysis(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleVertexAiFeaturestoreEntitytypeMonitoringConfigSnapshotAnalysisOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleVertexAiFeaturestoreEntitytype.GoogleVertexAiFeaturestoreEntitytypeMonitoringConfigSnapshotAnalysisOutputReference",
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
            type_hints = typing.get_type_hints(GoogleVertexAiFeaturestoreEntitytypeMonitoringConfigSnapshotAnalysisOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDisabled")
    def reset_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisabled", []))

    @jsii.member(jsii_name="resetMonitoringInterval")
    def reset_monitoring_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMonitoringInterval", []))

    @builtins.property
    @jsii.member(jsii_name="disabledInput")
    def disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disabledInput"))

    @builtins.property
    @jsii.member(jsii_name="monitoringIntervalInput")
    def monitoring_interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "monitoringIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="disabled")
    def disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disabled"))

    @disabled.setter
    def disabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleVertexAiFeaturestoreEntitytypeMonitoringConfigSnapshotAnalysisOutputReference, "disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="monitoringInterval")
    def monitoring_interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "monitoringInterval"))

    @monitoring_interval.setter
    def monitoring_interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleVertexAiFeaturestoreEntitytypeMonitoringConfigSnapshotAnalysisOutputReference, "monitoring_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitoringInterval", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleVertexAiFeaturestoreEntitytypeMonitoringConfigSnapshotAnalysis]:
        return typing.cast(typing.Optional[GoogleVertexAiFeaturestoreEntitytypeMonitoringConfigSnapshotAnalysis], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleVertexAiFeaturestoreEntitytypeMonitoringConfigSnapshotAnalysis],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleVertexAiFeaturestoreEntitytypeMonitoringConfigSnapshotAnalysisOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleVertexAiFeaturestoreEntitytype.GoogleVertexAiFeaturestoreEntitytypeTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleVertexAiFeaturestoreEntitytypeTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#create GoogleVertexAiFeaturestoreEntitytype#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#delete GoogleVertexAiFeaturestoreEntitytype#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#update GoogleVertexAiFeaturestoreEntitytype#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleVertexAiFeaturestoreEntitytypeTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#create GoogleVertexAiFeaturestoreEntitytype#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#delete GoogleVertexAiFeaturestoreEntitytype#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_vertex_ai_featurestore_entitytype#update GoogleVertexAiFeaturestoreEntitytype#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleVertexAiFeaturestoreEntitytypeTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleVertexAiFeaturestoreEntitytypeTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleVertexAiFeaturestoreEntitytype.GoogleVertexAiFeaturestoreEntitytypeTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleVertexAiFeaturestoreEntitytypeTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleVertexAiFeaturestoreEntitytypeTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleVertexAiFeaturestoreEntitytypeTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleVertexAiFeaturestoreEntitytypeTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleVertexAiFeaturestoreEntitytypeTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleVertexAiFeaturestoreEntitytypeTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleVertexAiFeaturestoreEntitytypeTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleVertexAiFeaturestoreEntitytypeTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleVertexAiFeaturestoreEntitytype",
    "GoogleVertexAiFeaturestoreEntitytypeConfig",
    "GoogleVertexAiFeaturestoreEntitytypeMonitoringConfig",
    "GoogleVertexAiFeaturestoreEntitytypeMonitoringConfigOutputReference",
    "GoogleVertexAiFeaturestoreEntitytypeMonitoringConfigSnapshotAnalysis",
    "GoogleVertexAiFeaturestoreEntitytypeMonitoringConfigSnapshotAnalysisOutputReference",
    "GoogleVertexAiFeaturestoreEntitytypeTimeouts",
    "GoogleVertexAiFeaturestoreEntitytypeTimeoutsOutputReference",
]

publication.publish()
