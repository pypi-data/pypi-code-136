'''
# `kubernetes_persistent_volume_v1`

Refer to the Terraform Registory for docs: [`kubernetes_persistent_volume_v1`](https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1).
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


class PersistentVolumeV1(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1 kubernetes_persistent_volume_v1}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        metadata: typing.Union["PersistentVolumeV1Metadata", typing.Dict[str, typing.Any]],
        spec: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["PersistentVolumeV1Spec", typing.Dict[str, typing.Any]]]],
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["PersistentVolumeV1Timeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1 kubernetes_persistent_volume_v1} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#metadata PersistentVolumeV1#metadata}
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#spec PersistentVolumeV1#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#id PersistentVolumeV1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#timeouts PersistentVolumeV1#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = PersistentVolumeV1Config(
            metadata=metadata,
            spec=spec,
            id=id,
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

    @jsii.member(jsii_name="putMetadata")
    def put_metadata(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the persistent volume that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#annotations PersistentVolumeV1#annotations}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the persistent volume. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#labels PersistentVolumeV1#labels}
        :param name: Name of the persistent volume, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#name PersistentVolumeV1#name}
        '''
        value = PersistentVolumeV1Metadata(
            annotations=annotations, labels=labels, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putMetadata", [value]))

    @jsii.member(jsii_name="putSpec")
    def put_spec(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["PersistentVolumeV1Spec", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1.put_spec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSpec", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, create: typing.Optional[builtins.str] = None) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#create PersistentVolumeV1#create}.
        '''
        value = PersistentVolumeV1Timeouts(create=create)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

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
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> "PersistentVolumeV1MetadataOutputReference":
        return typing.cast("PersistentVolumeV1MetadataOutputReference", jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="spec")
    def spec(self) -> "PersistentVolumeV1SpecList":
        return typing.cast("PersistentVolumeV1SpecList", jsii.get(self, "spec"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "PersistentVolumeV1TimeoutsOutputReference":
        return typing.cast("PersistentVolumeV1TimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(self) -> typing.Optional["PersistentVolumeV1Metadata"]:
        return typing.cast(typing.Optional["PersistentVolumeV1Metadata"], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="specInput")
    def spec_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PersistentVolumeV1Spec"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PersistentVolumeV1Spec"]]], jsii.get(self, "specInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["PersistentVolumeV1Timeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["PersistentVolumeV1Timeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1Config",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "metadata": "metadata",
        "spec": "spec",
        "id": "id",
        "timeouts": "timeouts",
    },
)
class PersistentVolumeV1Config(cdktf.TerraformMetaArguments):
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
        metadata: typing.Union["PersistentVolumeV1Metadata", typing.Dict[str, typing.Any]],
        spec: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["PersistentVolumeV1Spec", typing.Dict[str, typing.Any]]]],
        id: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["PersistentVolumeV1Timeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#metadata PersistentVolumeV1#metadata}
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#spec PersistentVolumeV1#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#id PersistentVolumeV1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#timeouts PersistentVolumeV1#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(metadata, dict):
            metadata = PersistentVolumeV1Metadata(**metadata)
        if isinstance(timeouts, dict):
            timeouts = PersistentVolumeV1Timeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1Config.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument spec", value=spec, expected_type=type_hints["spec"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "metadata": metadata,
            "spec": spec,
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
    def metadata(self) -> "PersistentVolumeV1Metadata":
        '''metadata block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#metadata PersistentVolumeV1#metadata}
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast("PersistentVolumeV1Metadata", result)

    @builtins.property
    def spec(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["PersistentVolumeV1Spec"]]:
        '''spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#spec PersistentVolumeV1#spec}
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["PersistentVolumeV1Spec"]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#id PersistentVolumeV1#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["PersistentVolumeV1Timeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#timeouts PersistentVolumeV1#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["PersistentVolumeV1Timeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1Metadata",
    jsii_struct_bases=[],
    name_mapping={"annotations": "annotations", "labels": "labels", "name": "name"},
)
class PersistentVolumeV1Metadata:
    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the persistent volume that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#annotations PersistentVolumeV1#annotations}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the persistent volume. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#labels PersistentVolumeV1#labels}
        :param name: Name of the persistent volume, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#name PersistentVolumeV1#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1Metadata.__init__)
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if annotations is not None:
            self._values["annotations"] = annotations
        if labels is not None:
            self._values["labels"] = labels
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''An unstructured key value map stored with the persistent volume that may be used to store arbitrary metadata.

        More info: http://kubernetes.io/docs/user-guide/annotations

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#annotations PersistentVolumeV1#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of string keys and values that can be used to organize and categorize (scope and select) the persistent volume.

        May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#labels PersistentVolumeV1#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the persistent volume, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#name PersistentVolumeV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1Metadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeV1MetadataOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1MetadataOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1MetadataOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAnnotations")
    def reset_annotations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnnotations", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @builtins.property
    @jsii.member(jsii_name="generation")
    def generation(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "generation"))

    @builtins.property
    @jsii.member(jsii_name="resourceVersion")
    def resource_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceVersion"))

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uid"))

    @builtins.property
    @jsii.member(jsii_name="annotationsInput")
    def annotations_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "annotationsInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="annotations")
    def annotations(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "annotations"))

    @annotations.setter
    def annotations(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1MetadataOutputReference, "annotations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1MetadataOutputReference, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1MetadataOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PersistentVolumeV1Metadata]:
        return typing.cast(typing.Optional[PersistentVolumeV1Metadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeV1Metadata],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1MetadataOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1Spec",
    jsii_struct_bases=[],
    name_mapping={
        "access_modes": "accessModes",
        "capacity": "capacity",
        "persistent_volume_source": "persistentVolumeSource",
        "claim_ref": "claimRef",
        "mount_options": "mountOptions",
        "node_affinity": "nodeAffinity",
        "persistent_volume_reclaim_policy": "persistentVolumeReclaimPolicy",
        "storage_class_name": "storageClassName",
        "volume_mode": "volumeMode",
    },
)
class PersistentVolumeV1Spec:
    def __init__(
        self,
        *,
        access_modes: typing.Sequence[builtins.str],
        capacity: typing.Mapping[builtins.str, builtins.str],
        persistent_volume_source: typing.Union["PersistentVolumeV1SpecPersistentVolumeSource", typing.Dict[str, typing.Any]],
        claim_ref: typing.Optional[typing.Union["PersistentVolumeV1SpecClaimRef", typing.Dict[str, typing.Any]]] = None,
        mount_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        node_affinity: typing.Optional[typing.Union["PersistentVolumeV1SpecNodeAffinity", typing.Dict[str, typing.Any]]] = None,
        persistent_volume_reclaim_policy: typing.Optional[builtins.str] = None,
        storage_class_name: typing.Optional[builtins.str] = None,
        volume_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_modes: Contains all ways the volume can be mounted. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#access-modes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#access_modes PersistentVolumeV1#access_modes}
        :param capacity: A description of the persistent volume's resources and capacity. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#capacity. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#capacity PersistentVolumeV1#capacity}
        :param persistent_volume_source: persistent_volume_source block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#persistent_volume_source PersistentVolumeV1#persistent_volume_source}
        :param claim_ref: claim_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#claim_ref PersistentVolumeV1#claim_ref}
        :param mount_options: A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#mount_options PersistentVolumeV1#mount_options}
        :param node_affinity: node_affinity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#node_affinity PersistentVolumeV1#node_affinity}
        :param persistent_volume_reclaim_policy: What happens to a persistent volume when released from its claim. Valid options are Retain (default) and Recycle. Recycling must be supported by the volume plugin underlying this persistent volume. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#recycling-policy Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#persistent_volume_reclaim_policy PersistentVolumeV1#persistent_volume_reclaim_policy}
        :param storage_class_name: A description of the persistent volume's class. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#class. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#storage_class_name PersistentVolumeV1#storage_class_name}
        :param volume_mode: Defines if a volume is intended to be used with a formatted filesystem. or to remain in raw block state. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#volume_mode PersistentVolumeV1#volume_mode}
        '''
        if isinstance(persistent_volume_source, dict):
            persistent_volume_source = PersistentVolumeV1SpecPersistentVolumeSource(**persistent_volume_source)
        if isinstance(claim_ref, dict):
            claim_ref = PersistentVolumeV1SpecClaimRef(**claim_ref)
        if isinstance(node_affinity, dict):
            node_affinity = PersistentVolumeV1SpecNodeAffinity(**node_affinity)
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1Spec.__init__)
            check_type(argname="argument access_modes", value=access_modes, expected_type=type_hints["access_modes"])
            check_type(argname="argument capacity", value=capacity, expected_type=type_hints["capacity"])
            check_type(argname="argument persistent_volume_source", value=persistent_volume_source, expected_type=type_hints["persistent_volume_source"])
            check_type(argname="argument claim_ref", value=claim_ref, expected_type=type_hints["claim_ref"])
            check_type(argname="argument mount_options", value=mount_options, expected_type=type_hints["mount_options"])
            check_type(argname="argument node_affinity", value=node_affinity, expected_type=type_hints["node_affinity"])
            check_type(argname="argument persistent_volume_reclaim_policy", value=persistent_volume_reclaim_policy, expected_type=type_hints["persistent_volume_reclaim_policy"])
            check_type(argname="argument storage_class_name", value=storage_class_name, expected_type=type_hints["storage_class_name"])
            check_type(argname="argument volume_mode", value=volume_mode, expected_type=type_hints["volume_mode"])
        self._values: typing.Dict[str, typing.Any] = {
            "access_modes": access_modes,
            "capacity": capacity,
            "persistent_volume_source": persistent_volume_source,
        }
        if claim_ref is not None:
            self._values["claim_ref"] = claim_ref
        if mount_options is not None:
            self._values["mount_options"] = mount_options
        if node_affinity is not None:
            self._values["node_affinity"] = node_affinity
        if persistent_volume_reclaim_policy is not None:
            self._values["persistent_volume_reclaim_policy"] = persistent_volume_reclaim_policy
        if storage_class_name is not None:
            self._values["storage_class_name"] = storage_class_name
        if volume_mode is not None:
            self._values["volume_mode"] = volume_mode

    @builtins.property
    def access_modes(self) -> typing.List[builtins.str]:
        '''Contains all ways the volume can be mounted. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#access-modes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#access_modes PersistentVolumeV1#access_modes}
        '''
        result = self._values.get("access_modes")
        assert result is not None, "Required property 'access_modes' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def capacity(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''A description of the persistent volume's resources and capacity. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#capacity.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#capacity PersistentVolumeV1#capacity}
        '''
        result = self._values.get("capacity")
        assert result is not None, "Required property 'capacity' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    @builtins.property
    def persistent_volume_source(
        self,
    ) -> "PersistentVolumeV1SpecPersistentVolumeSource":
        '''persistent_volume_source block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#persistent_volume_source PersistentVolumeV1#persistent_volume_source}
        '''
        result = self._values.get("persistent_volume_source")
        assert result is not None, "Required property 'persistent_volume_source' is missing"
        return typing.cast("PersistentVolumeV1SpecPersistentVolumeSource", result)

    @builtins.property
    def claim_ref(self) -> typing.Optional["PersistentVolumeV1SpecClaimRef"]:
        '''claim_ref block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#claim_ref PersistentVolumeV1#claim_ref}
        '''
        result = self._values.get("claim_ref")
        return typing.cast(typing.Optional["PersistentVolumeV1SpecClaimRef"], result)

    @builtins.property
    def mount_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#mount_options PersistentVolumeV1#mount_options}
        '''
        result = self._values.get("mount_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def node_affinity(self) -> typing.Optional["PersistentVolumeV1SpecNodeAffinity"]:
        '''node_affinity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#node_affinity PersistentVolumeV1#node_affinity}
        '''
        result = self._values.get("node_affinity")
        return typing.cast(typing.Optional["PersistentVolumeV1SpecNodeAffinity"], result)

    @builtins.property
    def persistent_volume_reclaim_policy(self) -> typing.Optional[builtins.str]:
        '''What happens to a persistent volume when released from its claim.

        Valid options are Retain (default) and Recycle. Recycling must be supported by the volume plugin underlying this persistent volume. More info: http://kubernetes.io/docs/user-guide/persistent-volumes#recycling-policy

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#persistent_volume_reclaim_policy PersistentVolumeV1#persistent_volume_reclaim_policy}
        '''
        result = self._values.get("persistent_volume_reclaim_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_class_name(self) -> typing.Optional[builtins.str]:
        '''A description of the persistent volume's class. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes/#class.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#storage_class_name PersistentVolumeV1#storage_class_name}
        '''
        result = self._values.get("storage_class_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def volume_mode(self) -> typing.Optional[builtins.str]:
        '''Defines if a volume is intended to be used with a formatted filesystem.

        or to remain in raw block state.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#volume_mode PersistentVolumeV1#volume_mode}
        '''
        result = self._values.get("volume_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1Spec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecClaimRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class PersistentVolumeV1SpecClaimRef:
    def __init__(
        self,
        *,
        name: builtins.str,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: The name of the PersistentVolumeClaim. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#name PersistentVolumeV1#name}
        :param namespace: The namespace of the PersistentVolumeClaim. Uses 'default' namespace if none is specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#namespace PersistentVolumeV1#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecClaimRef.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the PersistentVolumeClaim.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#name PersistentVolumeV1#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace of the PersistentVolumeClaim. Uses 'default' namespace if none is specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#namespace PersistentVolumeV1#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1SpecClaimRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeV1SpecClaimRefOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecClaimRefOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecClaimRefOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecClaimRefOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecClaimRefOutputReference, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PersistentVolumeV1SpecClaimRef]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecClaimRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeV1SpecClaimRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecClaimRefOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PersistentVolumeV1SpecList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecList",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "PersistentVolumeV1SpecOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PersistentVolumeV1SpecOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PersistentVolumeV1Spec]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PersistentVolumeV1Spec]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PersistentVolumeV1Spec]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecNodeAffinity",
    jsii_struct_bases=[],
    name_mapping={"required": "required"},
)
class PersistentVolumeV1SpecNodeAffinity:
    def __init__(
        self,
        *,
        required: typing.Optional[typing.Union["PersistentVolumeV1SpecNodeAffinityRequired", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param required: required block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#required PersistentVolumeV1#required}
        '''
        if isinstance(required, dict):
            required = PersistentVolumeV1SpecNodeAffinityRequired(**required)
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecNodeAffinity.__init__)
            check_type(argname="argument required", value=required, expected_type=type_hints["required"])
        self._values: typing.Dict[str, typing.Any] = {}
        if required is not None:
            self._values["required"] = required

    @builtins.property
    def required(self) -> typing.Optional["PersistentVolumeV1SpecNodeAffinityRequired"]:
        '''required block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#required PersistentVolumeV1#required}
        '''
        result = self._values.get("required")
        return typing.cast(typing.Optional["PersistentVolumeV1SpecNodeAffinityRequired"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1SpecNodeAffinity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeV1SpecNodeAffinityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecNodeAffinityOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecNodeAffinityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRequired")
    def put_required(
        self,
        *,
        node_selector_term: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param node_selector_term: node_selector_term block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#node_selector_term PersistentVolumeV1#node_selector_term}
        '''
        value = PersistentVolumeV1SpecNodeAffinityRequired(
            node_selector_term=node_selector_term
        )

        return typing.cast(None, jsii.invoke(self, "putRequired", [value]))

    @jsii.member(jsii_name="resetRequired")
    def reset_required(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequired", []))

    @builtins.property
    @jsii.member(jsii_name="required")
    def required(self) -> "PersistentVolumeV1SpecNodeAffinityRequiredOutputReference":
        return typing.cast("PersistentVolumeV1SpecNodeAffinityRequiredOutputReference", jsii.get(self, "required"))

    @builtins.property
    @jsii.member(jsii_name="requiredInput")
    def required_input(
        self,
    ) -> typing.Optional["PersistentVolumeV1SpecNodeAffinityRequired"]:
        return typing.cast(typing.Optional["PersistentVolumeV1SpecNodeAffinityRequired"], jsii.get(self, "requiredInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PersistentVolumeV1SpecNodeAffinity]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecNodeAffinity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeV1SpecNodeAffinity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecNodeAffinityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecNodeAffinityRequired",
    jsii_struct_bases=[],
    name_mapping={"node_selector_term": "nodeSelectorTerm"},
)
class PersistentVolumeV1SpecNodeAffinityRequired:
    def __init__(
        self,
        *,
        node_selector_term: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param node_selector_term: node_selector_term block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#node_selector_term PersistentVolumeV1#node_selector_term}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecNodeAffinityRequired.__init__)
            check_type(argname="argument node_selector_term", value=node_selector_term, expected_type=type_hints["node_selector_term"])
        self._values: typing.Dict[str, typing.Any] = {
            "node_selector_term": node_selector_term,
        }

    @builtins.property
    def node_selector_term(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm"]]:
        '''node_selector_term block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#node_selector_term PersistentVolumeV1#node_selector_term}
        '''
        result = self._values.get("node_selector_term")
        assert result is not None, "Required property 'node_selector_term' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1SpecNodeAffinityRequired(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_fields": "matchFields",
    },
)
class PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions", typing.Dict[str, typing.Any]]]]] = None,
        match_fields: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param match_expressions: match_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#match_expressions PersistentVolumeV1#match_expressions}
        :param match_fields: match_fields block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#match_fields PersistentVolumeV1#match_fields}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm.__init__)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_fields", value=match_fields, expected_type=type_hints["match_fields"])
        self._values: typing.Dict[str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_fields is not None:
            self._values["match_fields"] = match_fields

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions"]]]:
        '''match_expressions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#match_expressions PersistentVolumeV1#match_expressions}
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions"]]], result)

    @builtins.property
    def match_fields(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields"]]]:
        '''match_fields block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#match_fields PersistentVolumeV1#match_fields}
        '''
        result = self._values.get("match_fields")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermList",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: The label key that the selector applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#key PersistentVolumeV1#key}
        :param operator: A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists``, ``DoesNotExist``, ``Gt``, and ``Lt``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#operator PersistentVolumeV1#operator}
        :param values: An array of string values. If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#values PersistentVolumeV1#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "operator": operator,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> builtins.str:
        '''The label key that the selector applies to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#key PersistentVolumeV1#key}
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists``, ``DoesNotExist``, ``Gt``, and ``Lt``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#operator PersistentVolumeV1#operator}
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values.

        If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#values PersistentVolumeV1#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsList",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields:
    def __init__(
        self,
        *,
        key: builtins.str,
        operator: builtins.str,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: The label key that the selector applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#key PersistentVolumeV1#key}
        :param operator: A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists``, ``DoesNotExist``, ``Gt``, and ``Lt``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#operator PersistentVolumeV1#operator}
        :param values: An array of string values. If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#values PersistentVolumeV1#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {
            "key": key,
            "operator": operator,
        }
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> builtins.str:
        '''The label key that the selector applies to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#key PersistentVolumeV1#key}
        '''
        result = self._values.get("key")
        assert result is not None, "Required property 'key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operator(self) -> builtins.str:
        '''A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists``, ``DoesNotExist``, ``Gt``, and ``Lt``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#operator PersistentVolumeV1#operator}
        '''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values.

        If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#values PersistentVolumeV1#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFieldsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFieldsList",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFieldsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFieldsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFieldsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFieldsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFieldsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFieldsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFieldsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFieldsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFieldsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFieldsOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFieldsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetValues")
    def reset_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValues", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="valuesInput")
    def values_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "valuesInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFieldsOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFieldsOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFieldsOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFieldsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMatchExpressions")
    def put_match_expressions(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermOutputReference.put_match_expressions)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchExpressions", [value]))

    @jsii.member(jsii_name="putMatchFields")
    def put_match_fields(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermOutputReference.put_match_fields)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchFields", [value]))

    @jsii.member(jsii_name="resetMatchExpressions")
    def reset_match_expressions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchExpressions", []))

    @jsii.member(jsii_name="resetMatchFields")
    def reset_match_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchFields", []))

    @builtins.property
    @jsii.member(jsii_name="matchExpressions")
    def match_expressions(
        self,
    ) -> PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsList:
        return typing.cast(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsList, jsii.get(self, "matchExpressions"))

    @builtins.property
    @jsii.member(jsii_name="matchFields")
    def match_fields(
        self,
    ) -> PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFieldsList:
        return typing.cast(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFieldsList, jsii.get(self, "matchFields"))

    @builtins.property
    @jsii.member(jsii_name="matchExpressionsInput")
    def match_expressions_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions]]], jsii.get(self, "matchExpressionsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchFieldsInput")
    def match_fields_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields]]], jsii.get(self, "matchFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PersistentVolumeV1SpecNodeAffinityRequiredOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecNodeAffinityRequiredOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecNodeAffinityRequiredOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putNodeSelectorTerm")
    def put_node_selector_term(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecNodeAffinityRequiredOutputReference.put_node_selector_term)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNodeSelectorTerm", [value]))

    @builtins.property
    @jsii.member(jsii_name="nodeSelectorTerm")
    def node_selector_term(
        self,
    ) -> PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermList:
        return typing.cast(PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermList, jsii.get(self, "nodeSelectorTerm"))

    @builtins.property
    @jsii.member(jsii_name="nodeSelectorTermInput")
    def node_selector_term_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm]]], jsii.get(self, "nodeSelectorTermInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecNodeAffinityRequired]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecNodeAffinityRequired], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeV1SpecNodeAffinityRequired],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecNodeAffinityRequiredOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PersistentVolumeV1SpecOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putClaimRef")
    def put_claim_ref(
        self,
        *,
        name: builtins.str,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: The name of the PersistentVolumeClaim. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#name PersistentVolumeV1#name}
        :param namespace: The namespace of the PersistentVolumeClaim. Uses 'default' namespace if none is specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#namespace PersistentVolumeV1#namespace}
        '''
        value = PersistentVolumeV1SpecClaimRef(name=name, namespace=namespace)

        return typing.cast(None, jsii.invoke(self, "putClaimRef", [value]))

    @jsii.member(jsii_name="putNodeAffinity")
    def put_node_affinity(
        self,
        *,
        required: typing.Optional[typing.Union[PersistentVolumeV1SpecNodeAffinityRequired, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param required: required block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#required PersistentVolumeV1#required}
        '''
        value = PersistentVolumeV1SpecNodeAffinity(required=required)

        return typing.cast(None, jsii.invoke(self, "putNodeAffinity", [value]))

    @jsii.member(jsii_name="putPersistentVolumeSource")
    def put_persistent_volume_source(
        self,
        *,
        aws_elastic_block_store: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStore", typing.Dict[str, typing.Any]]] = None,
        azure_disk: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceAzureDisk", typing.Dict[str, typing.Any]]] = None,
        azure_file: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceAzureFile", typing.Dict[str, typing.Any]]] = None,
        ceph_fs: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceCephFs", typing.Dict[str, typing.Any]]] = None,
        cinder: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceCinder", typing.Dict[str, typing.Any]]] = None,
        csi: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceCsi", typing.Dict[str, typing.Any]]] = None,
        fc: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceFc", typing.Dict[str, typing.Any]]] = None,
        flex_volume: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceFlexVolume", typing.Dict[str, typing.Any]]] = None,
        flocker: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceFlocker", typing.Dict[str, typing.Any]]] = None,
        gce_persistent_disk: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDisk", typing.Dict[str, typing.Any]]] = None,
        glusterfs: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceGlusterfs", typing.Dict[str, typing.Any]]] = None,
        host_path: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceHostPath", typing.Dict[str, typing.Any]]] = None,
        iscsi: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceIscsi", typing.Dict[str, typing.Any]]] = None,
        local: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceLocal", typing.Dict[str, typing.Any]]] = None,
        nfs: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceNfs", typing.Dict[str, typing.Any]]] = None,
        photon_persistent_disk: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDisk", typing.Dict[str, typing.Any]]] = None,
        quobyte: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceQuobyte", typing.Dict[str, typing.Any]]] = None,
        rbd: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceRbd", typing.Dict[str, typing.Any]]] = None,
        vsphere_volume: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceVsphereVolume", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param aws_elastic_block_store: aws_elastic_block_store block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#aws_elastic_block_store PersistentVolumeV1#aws_elastic_block_store}
        :param azure_disk: azure_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#azure_disk PersistentVolumeV1#azure_disk}
        :param azure_file: azure_file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#azure_file PersistentVolumeV1#azure_file}
        :param ceph_fs: ceph_fs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#ceph_fs PersistentVolumeV1#ceph_fs}
        :param cinder: cinder block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#cinder PersistentVolumeV1#cinder}
        :param csi: csi block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#csi PersistentVolumeV1#csi}
        :param fc: fc block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fc PersistentVolumeV1#fc}
        :param flex_volume: flex_volume block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#flex_volume PersistentVolumeV1#flex_volume}
        :param flocker: flocker block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#flocker PersistentVolumeV1#flocker}
        :param gce_persistent_disk: gce_persistent_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#gce_persistent_disk PersistentVolumeV1#gce_persistent_disk}
        :param glusterfs: glusterfs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#glusterfs PersistentVolumeV1#glusterfs}
        :param host_path: host_path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#host_path PersistentVolumeV1#host_path}
        :param iscsi: iscsi block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#iscsi PersistentVolumeV1#iscsi}
        :param local: local block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#local PersistentVolumeV1#local}
        :param nfs: nfs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#nfs PersistentVolumeV1#nfs}
        :param photon_persistent_disk: photon_persistent_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#photon_persistent_disk PersistentVolumeV1#photon_persistent_disk}
        :param quobyte: quobyte block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#quobyte PersistentVolumeV1#quobyte}
        :param rbd: rbd block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#rbd PersistentVolumeV1#rbd}
        :param vsphere_volume: vsphere_volume block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#vsphere_volume PersistentVolumeV1#vsphere_volume}
        '''
        value = PersistentVolumeV1SpecPersistentVolumeSource(
            aws_elastic_block_store=aws_elastic_block_store,
            azure_disk=azure_disk,
            azure_file=azure_file,
            ceph_fs=ceph_fs,
            cinder=cinder,
            csi=csi,
            fc=fc,
            flex_volume=flex_volume,
            flocker=flocker,
            gce_persistent_disk=gce_persistent_disk,
            glusterfs=glusterfs,
            host_path=host_path,
            iscsi=iscsi,
            local=local,
            nfs=nfs,
            photon_persistent_disk=photon_persistent_disk,
            quobyte=quobyte,
            rbd=rbd,
            vsphere_volume=vsphere_volume,
        )

        return typing.cast(None, jsii.invoke(self, "putPersistentVolumeSource", [value]))

    @jsii.member(jsii_name="resetClaimRef")
    def reset_claim_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClaimRef", []))

    @jsii.member(jsii_name="resetMountOptions")
    def reset_mount_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMountOptions", []))

    @jsii.member(jsii_name="resetNodeAffinity")
    def reset_node_affinity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeAffinity", []))

    @jsii.member(jsii_name="resetPersistentVolumeReclaimPolicy")
    def reset_persistent_volume_reclaim_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPersistentVolumeReclaimPolicy", []))

    @jsii.member(jsii_name="resetStorageClassName")
    def reset_storage_class_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageClassName", []))

    @jsii.member(jsii_name="resetVolumeMode")
    def reset_volume_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeMode", []))

    @builtins.property
    @jsii.member(jsii_name="claimRef")
    def claim_ref(self) -> PersistentVolumeV1SpecClaimRefOutputReference:
        return typing.cast(PersistentVolumeV1SpecClaimRefOutputReference, jsii.get(self, "claimRef"))

    @builtins.property
    @jsii.member(jsii_name="nodeAffinity")
    def node_affinity(self) -> PersistentVolumeV1SpecNodeAffinityOutputReference:
        return typing.cast(PersistentVolumeV1SpecNodeAffinityOutputReference, jsii.get(self, "nodeAffinity"))

    @builtins.property
    @jsii.member(jsii_name="persistentVolumeSource")
    def persistent_volume_source(
        self,
    ) -> "PersistentVolumeV1SpecPersistentVolumeSourceOutputReference":
        return typing.cast("PersistentVolumeV1SpecPersistentVolumeSourceOutputReference", jsii.get(self, "persistentVolumeSource"))

    @builtins.property
    @jsii.member(jsii_name="accessModesInput")
    def access_modes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "accessModesInput"))

    @builtins.property
    @jsii.member(jsii_name="capacityInput")
    def capacity_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "capacityInput"))

    @builtins.property
    @jsii.member(jsii_name="claimRefInput")
    def claim_ref_input(self) -> typing.Optional[PersistentVolumeV1SpecClaimRef]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecClaimRef], jsii.get(self, "claimRefInput"))

    @builtins.property
    @jsii.member(jsii_name="mountOptionsInput")
    def mount_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "mountOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeAffinityInput")
    def node_affinity_input(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecNodeAffinity]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecNodeAffinity], jsii.get(self, "nodeAffinityInput"))

    @builtins.property
    @jsii.member(jsii_name="persistentVolumeReclaimPolicyInput")
    def persistent_volume_reclaim_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "persistentVolumeReclaimPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="persistentVolumeSourceInput")
    def persistent_volume_source_input(
        self,
    ) -> typing.Optional["PersistentVolumeV1SpecPersistentVolumeSource"]:
        return typing.cast(typing.Optional["PersistentVolumeV1SpecPersistentVolumeSource"], jsii.get(self, "persistentVolumeSourceInput"))

    @builtins.property
    @jsii.member(jsii_name="storageClassNameInput")
    def storage_class_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageClassNameInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeModeInput")
    def volume_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeModeInput"))

    @builtins.property
    @jsii.member(jsii_name="accessModes")
    def access_modes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "accessModes"))

    @access_modes.setter
    def access_modes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecOutputReference, "access_modes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessModes", value)

    @builtins.property
    @jsii.member(jsii_name="capacity")
    def capacity(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "capacity"))

    @capacity.setter
    def capacity(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecOutputReference, "capacity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "capacity", value)

    @builtins.property
    @jsii.member(jsii_name="mountOptions")
    def mount_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "mountOptions"))

    @mount_options.setter
    def mount_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecOutputReference, "mount_options").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountOptions", value)

    @builtins.property
    @jsii.member(jsii_name="persistentVolumeReclaimPolicy")
    def persistent_volume_reclaim_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "persistentVolumeReclaimPolicy"))

    @persistent_volume_reclaim_policy.setter
    def persistent_volume_reclaim_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecOutputReference, "persistent_volume_reclaim_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "persistentVolumeReclaimPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="storageClassName")
    def storage_class_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageClassName"))

    @storage_class_name.setter
    def storage_class_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecOutputReference, "storage_class_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageClassName", value)

    @builtins.property
    @jsii.member(jsii_name="volumeMode")
    def volume_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeMode"))

    @volume_mode.setter
    def volume_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecOutputReference, "volume_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeMode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PersistentVolumeV1Spec, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PersistentVolumeV1Spec, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PersistentVolumeV1Spec, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSource",
    jsii_struct_bases=[],
    name_mapping={
        "aws_elastic_block_store": "awsElasticBlockStore",
        "azure_disk": "azureDisk",
        "azure_file": "azureFile",
        "ceph_fs": "cephFs",
        "cinder": "cinder",
        "csi": "csi",
        "fc": "fc",
        "flex_volume": "flexVolume",
        "flocker": "flocker",
        "gce_persistent_disk": "gcePersistentDisk",
        "glusterfs": "glusterfs",
        "host_path": "hostPath",
        "iscsi": "iscsi",
        "local": "local",
        "nfs": "nfs",
        "photon_persistent_disk": "photonPersistentDisk",
        "quobyte": "quobyte",
        "rbd": "rbd",
        "vsphere_volume": "vsphereVolume",
    },
)
class PersistentVolumeV1SpecPersistentVolumeSource:
    def __init__(
        self,
        *,
        aws_elastic_block_store: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStore", typing.Dict[str, typing.Any]]] = None,
        azure_disk: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceAzureDisk", typing.Dict[str, typing.Any]]] = None,
        azure_file: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceAzureFile", typing.Dict[str, typing.Any]]] = None,
        ceph_fs: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceCephFs", typing.Dict[str, typing.Any]]] = None,
        cinder: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceCinder", typing.Dict[str, typing.Any]]] = None,
        csi: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceCsi", typing.Dict[str, typing.Any]]] = None,
        fc: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceFc", typing.Dict[str, typing.Any]]] = None,
        flex_volume: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceFlexVolume", typing.Dict[str, typing.Any]]] = None,
        flocker: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceFlocker", typing.Dict[str, typing.Any]]] = None,
        gce_persistent_disk: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDisk", typing.Dict[str, typing.Any]]] = None,
        glusterfs: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceGlusterfs", typing.Dict[str, typing.Any]]] = None,
        host_path: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceHostPath", typing.Dict[str, typing.Any]]] = None,
        iscsi: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceIscsi", typing.Dict[str, typing.Any]]] = None,
        local: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceLocal", typing.Dict[str, typing.Any]]] = None,
        nfs: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceNfs", typing.Dict[str, typing.Any]]] = None,
        photon_persistent_disk: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDisk", typing.Dict[str, typing.Any]]] = None,
        quobyte: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceQuobyte", typing.Dict[str, typing.Any]]] = None,
        rbd: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceRbd", typing.Dict[str, typing.Any]]] = None,
        vsphere_volume: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceVsphereVolume", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param aws_elastic_block_store: aws_elastic_block_store block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#aws_elastic_block_store PersistentVolumeV1#aws_elastic_block_store}
        :param azure_disk: azure_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#azure_disk PersistentVolumeV1#azure_disk}
        :param azure_file: azure_file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#azure_file PersistentVolumeV1#azure_file}
        :param ceph_fs: ceph_fs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#ceph_fs PersistentVolumeV1#ceph_fs}
        :param cinder: cinder block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#cinder PersistentVolumeV1#cinder}
        :param csi: csi block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#csi PersistentVolumeV1#csi}
        :param fc: fc block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fc PersistentVolumeV1#fc}
        :param flex_volume: flex_volume block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#flex_volume PersistentVolumeV1#flex_volume}
        :param flocker: flocker block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#flocker PersistentVolumeV1#flocker}
        :param gce_persistent_disk: gce_persistent_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#gce_persistent_disk PersistentVolumeV1#gce_persistent_disk}
        :param glusterfs: glusterfs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#glusterfs PersistentVolumeV1#glusterfs}
        :param host_path: host_path block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#host_path PersistentVolumeV1#host_path}
        :param iscsi: iscsi block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#iscsi PersistentVolumeV1#iscsi}
        :param local: local block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#local PersistentVolumeV1#local}
        :param nfs: nfs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#nfs PersistentVolumeV1#nfs}
        :param photon_persistent_disk: photon_persistent_disk block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#photon_persistent_disk PersistentVolumeV1#photon_persistent_disk}
        :param quobyte: quobyte block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#quobyte PersistentVolumeV1#quobyte}
        :param rbd: rbd block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#rbd PersistentVolumeV1#rbd}
        :param vsphere_volume: vsphere_volume block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#vsphere_volume PersistentVolumeV1#vsphere_volume}
        '''
        if isinstance(aws_elastic_block_store, dict):
            aws_elastic_block_store = PersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStore(**aws_elastic_block_store)
        if isinstance(azure_disk, dict):
            azure_disk = PersistentVolumeV1SpecPersistentVolumeSourceAzureDisk(**azure_disk)
        if isinstance(azure_file, dict):
            azure_file = PersistentVolumeV1SpecPersistentVolumeSourceAzureFile(**azure_file)
        if isinstance(ceph_fs, dict):
            ceph_fs = PersistentVolumeV1SpecPersistentVolumeSourceCephFs(**ceph_fs)
        if isinstance(cinder, dict):
            cinder = PersistentVolumeV1SpecPersistentVolumeSourceCinder(**cinder)
        if isinstance(csi, dict):
            csi = PersistentVolumeV1SpecPersistentVolumeSourceCsi(**csi)
        if isinstance(fc, dict):
            fc = PersistentVolumeV1SpecPersistentVolumeSourceFc(**fc)
        if isinstance(flex_volume, dict):
            flex_volume = PersistentVolumeV1SpecPersistentVolumeSourceFlexVolume(**flex_volume)
        if isinstance(flocker, dict):
            flocker = PersistentVolumeV1SpecPersistentVolumeSourceFlocker(**flocker)
        if isinstance(gce_persistent_disk, dict):
            gce_persistent_disk = PersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDisk(**gce_persistent_disk)
        if isinstance(glusterfs, dict):
            glusterfs = PersistentVolumeV1SpecPersistentVolumeSourceGlusterfs(**glusterfs)
        if isinstance(host_path, dict):
            host_path = PersistentVolumeV1SpecPersistentVolumeSourceHostPath(**host_path)
        if isinstance(iscsi, dict):
            iscsi = PersistentVolumeV1SpecPersistentVolumeSourceIscsi(**iscsi)
        if isinstance(local, dict):
            local = PersistentVolumeV1SpecPersistentVolumeSourceLocal(**local)
        if isinstance(nfs, dict):
            nfs = PersistentVolumeV1SpecPersistentVolumeSourceNfs(**nfs)
        if isinstance(photon_persistent_disk, dict):
            photon_persistent_disk = PersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDisk(**photon_persistent_disk)
        if isinstance(quobyte, dict):
            quobyte = PersistentVolumeV1SpecPersistentVolumeSourceQuobyte(**quobyte)
        if isinstance(rbd, dict):
            rbd = PersistentVolumeV1SpecPersistentVolumeSourceRbd(**rbd)
        if isinstance(vsphere_volume, dict):
            vsphere_volume = PersistentVolumeV1SpecPersistentVolumeSourceVsphereVolume(**vsphere_volume)
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSource.__init__)
            check_type(argname="argument aws_elastic_block_store", value=aws_elastic_block_store, expected_type=type_hints["aws_elastic_block_store"])
            check_type(argname="argument azure_disk", value=azure_disk, expected_type=type_hints["azure_disk"])
            check_type(argname="argument azure_file", value=azure_file, expected_type=type_hints["azure_file"])
            check_type(argname="argument ceph_fs", value=ceph_fs, expected_type=type_hints["ceph_fs"])
            check_type(argname="argument cinder", value=cinder, expected_type=type_hints["cinder"])
            check_type(argname="argument csi", value=csi, expected_type=type_hints["csi"])
            check_type(argname="argument fc", value=fc, expected_type=type_hints["fc"])
            check_type(argname="argument flex_volume", value=flex_volume, expected_type=type_hints["flex_volume"])
            check_type(argname="argument flocker", value=flocker, expected_type=type_hints["flocker"])
            check_type(argname="argument gce_persistent_disk", value=gce_persistent_disk, expected_type=type_hints["gce_persistent_disk"])
            check_type(argname="argument glusterfs", value=glusterfs, expected_type=type_hints["glusterfs"])
            check_type(argname="argument host_path", value=host_path, expected_type=type_hints["host_path"])
            check_type(argname="argument iscsi", value=iscsi, expected_type=type_hints["iscsi"])
            check_type(argname="argument local", value=local, expected_type=type_hints["local"])
            check_type(argname="argument nfs", value=nfs, expected_type=type_hints["nfs"])
            check_type(argname="argument photon_persistent_disk", value=photon_persistent_disk, expected_type=type_hints["photon_persistent_disk"])
            check_type(argname="argument quobyte", value=quobyte, expected_type=type_hints["quobyte"])
            check_type(argname="argument rbd", value=rbd, expected_type=type_hints["rbd"])
            check_type(argname="argument vsphere_volume", value=vsphere_volume, expected_type=type_hints["vsphere_volume"])
        self._values: typing.Dict[str, typing.Any] = {}
        if aws_elastic_block_store is not None:
            self._values["aws_elastic_block_store"] = aws_elastic_block_store
        if azure_disk is not None:
            self._values["azure_disk"] = azure_disk
        if azure_file is not None:
            self._values["azure_file"] = azure_file
        if ceph_fs is not None:
            self._values["ceph_fs"] = ceph_fs
        if cinder is not None:
            self._values["cinder"] = cinder
        if csi is not None:
            self._values["csi"] = csi
        if fc is not None:
            self._values["fc"] = fc
        if flex_volume is not None:
            self._values["flex_volume"] = flex_volume
        if flocker is not None:
            self._values["flocker"] = flocker
        if gce_persistent_disk is not None:
            self._values["gce_persistent_disk"] = gce_persistent_disk
        if glusterfs is not None:
            self._values["glusterfs"] = glusterfs
        if host_path is not None:
            self._values["host_path"] = host_path
        if iscsi is not None:
            self._values["iscsi"] = iscsi
        if local is not None:
            self._values["local"] = local
        if nfs is not None:
            self._values["nfs"] = nfs
        if photon_persistent_disk is not None:
            self._values["photon_persistent_disk"] = photon_persistent_disk
        if quobyte is not None:
            self._values["quobyte"] = quobyte
        if rbd is not None:
            self._values["rbd"] = rbd
        if vsphere_volume is not None:
            self._values["vsphere_volume"] = vsphere_volume

    @builtins.property
    def aws_elastic_block_store(
        self,
    ) -> typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStore"]:
        '''aws_elastic_block_store block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#aws_elastic_block_store PersistentVolumeV1#aws_elastic_block_store}
        '''
        result = self._values.get("aws_elastic_block_store")
        return typing.cast(typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStore"], result)

    @builtins.property
    def azure_disk(
        self,
    ) -> typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceAzureDisk"]:
        '''azure_disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#azure_disk PersistentVolumeV1#azure_disk}
        '''
        result = self._values.get("azure_disk")
        return typing.cast(typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceAzureDisk"], result)

    @builtins.property
    def azure_file(
        self,
    ) -> typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceAzureFile"]:
        '''azure_file block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#azure_file PersistentVolumeV1#azure_file}
        '''
        result = self._values.get("azure_file")
        return typing.cast(typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceAzureFile"], result)

    @builtins.property
    def ceph_fs(
        self,
    ) -> typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceCephFs"]:
        '''ceph_fs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#ceph_fs PersistentVolumeV1#ceph_fs}
        '''
        result = self._values.get("ceph_fs")
        return typing.cast(typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceCephFs"], result)

    @builtins.property
    def cinder(
        self,
    ) -> typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceCinder"]:
        '''cinder block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#cinder PersistentVolumeV1#cinder}
        '''
        result = self._values.get("cinder")
        return typing.cast(typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceCinder"], result)

    @builtins.property
    def csi(self) -> typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceCsi"]:
        '''csi block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#csi PersistentVolumeV1#csi}
        '''
        result = self._values.get("csi")
        return typing.cast(typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceCsi"], result)

    @builtins.property
    def fc(self) -> typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceFc"]:
        '''fc block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fc PersistentVolumeV1#fc}
        '''
        result = self._values.get("fc")
        return typing.cast(typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceFc"], result)

    @builtins.property
    def flex_volume(
        self,
    ) -> typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceFlexVolume"]:
        '''flex_volume block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#flex_volume PersistentVolumeV1#flex_volume}
        '''
        result = self._values.get("flex_volume")
        return typing.cast(typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceFlexVolume"], result)

    @builtins.property
    def flocker(
        self,
    ) -> typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceFlocker"]:
        '''flocker block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#flocker PersistentVolumeV1#flocker}
        '''
        result = self._values.get("flocker")
        return typing.cast(typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceFlocker"], result)

    @builtins.property
    def gce_persistent_disk(
        self,
    ) -> typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDisk"]:
        '''gce_persistent_disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#gce_persistent_disk PersistentVolumeV1#gce_persistent_disk}
        '''
        result = self._values.get("gce_persistent_disk")
        return typing.cast(typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDisk"], result)

    @builtins.property
    def glusterfs(
        self,
    ) -> typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceGlusterfs"]:
        '''glusterfs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#glusterfs PersistentVolumeV1#glusterfs}
        '''
        result = self._values.get("glusterfs")
        return typing.cast(typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceGlusterfs"], result)

    @builtins.property
    def host_path(
        self,
    ) -> typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceHostPath"]:
        '''host_path block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#host_path PersistentVolumeV1#host_path}
        '''
        result = self._values.get("host_path")
        return typing.cast(typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceHostPath"], result)

    @builtins.property
    def iscsi(
        self,
    ) -> typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceIscsi"]:
        '''iscsi block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#iscsi PersistentVolumeV1#iscsi}
        '''
        result = self._values.get("iscsi")
        return typing.cast(typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceIscsi"], result)

    @builtins.property
    def local(
        self,
    ) -> typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceLocal"]:
        '''local block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#local PersistentVolumeV1#local}
        '''
        result = self._values.get("local")
        return typing.cast(typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceLocal"], result)

    @builtins.property
    def nfs(self) -> typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceNfs"]:
        '''nfs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#nfs PersistentVolumeV1#nfs}
        '''
        result = self._values.get("nfs")
        return typing.cast(typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceNfs"], result)

    @builtins.property
    def photon_persistent_disk(
        self,
    ) -> typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDisk"]:
        '''photon_persistent_disk block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#photon_persistent_disk PersistentVolumeV1#photon_persistent_disk}
        '''
        result = self._values.get("photon_persistent_disk")
        return typing.cast(typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDisk"], result)

    @builtins.property
    def quobyte(
        self,
    ) -> typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceQuobyte"]:
        '''quobyte block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#quobyte PersistentVolumeV1#quobyte}
        '''
        result = self._values.get("quobyte")
        return typing.cast(typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceQuobyte"], result)

    @builtins.property
    def rbd(self) -> typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceRbd"]:
        '''rbd block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#rbd PersistentVolumeV1#rbd}
        '''
        result = self._values.get("rbd")
        return typing.cast(typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceRbd"], result)

    @builtins.property
    def vsphere_volume(
        self,
    ) -> typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceVsphereVolume"]:
        '''vsphere_volume block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#vsphere_volume PersistentVolumeV1#vsphere_volume}
        '''
        result = self._values.get("vsphere_volume")
        return typing.cast(typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceVsphereVolume"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1SpecPersistentVolumeSource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStore",
    jsii_struct_bases=[],
    name_mapping={
        "volume_id": "volumeId",
        "fs_type": "fsType",
        "partition": "partition",
        "read_only": "readOnly",
    },
)
class PersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStore:
    def __init__(
        self,
        *,
        volume_id: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        partition: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param volume_id: Unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#volume_id PersistentVolumeV1#volume_id}
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fs_type PersistentVolumeV1#fs_type}
        :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#partition PersistentVolumeV1#partition}
        :param read_only: Whether to set the read-only property in VolumeMounts to "true". If omitted, the default is "false". More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStore.__init__)
            check_type(argname="argument volume_id", value=volume_id, expected_type=type_hints["volume_id"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument partition", value=partition, expected_type=type_hints["partition"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[str, typing.Any] = {
            "volume_id": volume_id,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if partition is not None:
            self._values["partition"] = partition
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def volume_id(self) -> builtins.str:
        '''Unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#volume_id PersistentVolumeV1#volume_id}
        '''
        result = self._values.get("volume_id")
        assert result is not None, "Required property 'volume_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type of the volume that you want to mount.

        Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fs_type PersistentVolumeV1#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partition(self) -> typing.Optional[jsii.Number]:
        '''The partition in the volume that you want to mount.

        If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#partition PersistentVolumeV1#partition}
        '''
        result = self._values.get("partition")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to set the read-only property in VolumeMounts to "true". If omitted, the default is "false". More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStore(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStoreOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStoreOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStoreOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetPartition")
    def reset_partition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartition", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionInput")
    def partition_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "partitionInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeIdInput")
    def volume_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStoreOutputReference, "fs_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="partition")
    def partition(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "partition"))

    @partition.setter
    def partition(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStoreOutputReference, "partition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partition", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStoreOutputReference, "read_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="volumeId")
    def volume_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeId"))

    @volume_id.setter
    def volume_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStoreOutputReference, "volume_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStore]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStore], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStore],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStoreOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceAzureDisk",
    jsii_struct_bases=[],
    name_mapping={
        "caching_mode": "cachingMode",
        "data_disk_uri": "dataDiskUri",
        "disk_name": "diskName",
        "fs_type": "fsType",
        "kind": "kind",
        "read_only": "readOnly",
    },
)
class PersistentVolumeV1SpecPersistentVolumeSourceAzureDisk:
    def __init__(
        self,
        *,
        caching_mode: builtins.str,
        data_disk_uri: builtins.str,
        disk_name: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param caching_mode: Host Caching mode: None, Read Only, Read Write. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#caching_mode PersistentVolumeV1#caching_mode}
        :param data_disk_uri: The URI the data disk in the blob storage. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#data_disk_uri PersistentVolumeV1#data_disk_uri}
        :param disk_name: The Name of the data disk in the blob storage. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#disk_name PersistentVolumeV1#disk_name}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fs_type PersistentVolumeV1#fs_type}
        :param kind: The type for the data disk. Expected values: Shared, Dedicated, Managed. Defaults to Shared. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#kind PersistentVolumeV1#kind}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceAzureDisk.__init__)
            check_type(argname="argument caching_mode", value=caching_mode, expected_type=type_hints["caching_mode"])
            check_type(argname="argument data_disk_uri", value=data_disk_uri, expected_type=type_hints["data_disk_uri"])
            check_type(argname="argument disk_name", value=disk_name, expected_type=type_hints["disk_name"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[str, typing.Any] = {
            "caching_mode": caching_mode,
            "data_disk_uri": data_disk_uri,
            "disk_name": disk_name,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if kind is not None:
            self._values["kind"] = kind
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def caching_mode(self) -> builtins.str:
        '''Host Caching mode: None, Read Only, Read Write.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#caching_mode PersistentVolumeV1#caching_mode}
        '''
        result = self._values.get("caching_mode")
        assert result is not None, "Required property 'caching_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_disk_uri(self) -> builtins.str:
        '''The URI the data disk in the blob storage.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#data_disk_uri PersistentVolumeV1#data_disk_uri}
        '''
        result = self._values.get("data_disk_uri")
        assert result is not None, "Required property 'data_disk_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disk_name(self) -> builtins.str:
        '''The Name of the data disk in the blob storage.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#disk_name PersistentVolumeV1#disk_name}
        '''
        result = self._values.get("disk_name")
        assert result is not None, "Required property 'disk_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type to mount.

        Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fs_type PersistentVolumeV1#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional[builtins.str]:
        '''The type for the data disk. Expected values: Shared, Dedicated, Managed. Defaults to Shared.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#kind PersistentVolumeV1#kind}
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1SpecPersistentVolumeSourceAzureDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeV1SpecPersistentVolumeSourceAzureDiskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceAzureDiskOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceAzureDiskOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetKind")
    def reset_kind(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKind", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="cachingModeInput")
    def caching_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cachingModeInput"))

    @builtins.property
    @jsii.member(jsii_name="dataDiskUriInput")
    def data_disk_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataDiskUriInput"))

    @builtins.property
    @jsii.member(jsii_name="diskNameInput")
    def disk_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diskNameInput"))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="cachingMode")
    def caching_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "cachingMode"))

    @caching_mode.setter
    def caching_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceAzureDiskOutputReference, "caching_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cachingMode", value)

    @builtins.property
    @jsii.member(jsii_name="dataDiskUri")
    def data_disk_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataDiskUri"))

    @data_disk_uri.setter
    def data_disk_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceAzureDiskOutputReference, "data_disk_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataDiskUri", value)

    @builtins.property
    @jsii.member(jsii_name="diskName")
    def disk_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskName"))

    @disk_name.setter
    def disk_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceAzureDiskOutputReference, "disk_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskName", value)

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceAzureDiskOutputReference, "fs_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceAzureDiskOutputReference, "kind").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceAzureDiskOutputReference, "read_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceAzureDisk]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceAzureDisk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceAzureDisk],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceAzureDiskOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceAzureFile",
    jsii_struct_bases=[],
    name_mapping={
        "secret_name": "secretName",
        "share_name": "shareName",
        "read_only": "readOnly",
        "secret_namespace": "secretNamespace",
    },
)
class PersistentVolumeV1SpecPersistentVolumeSourceAzureFile:
    def __init__(
        self,
        *,
        secret_name: builtins.str,
        share_name: builtins.str,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        secret_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param secret_name: The name of secret that contains Azure Storage Account Name and Key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#secret_name PersistentVolumeV1#secret_name}
        :param share_name: Share Name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#share_name PersistentVolumeV1#share_name}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        :param secret_namespace: The namespace of the secret that contains Azure Storage Account Name and Key. For Kubernetes up to 1.18.x the default is the same as the Pod. For Kubernetes 1.19.x and later the default is "default" namespace. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#secret_namespace PersistentVolumeV1#secret_namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceAzureFile.__init__)
            check_type(argname="argument secret_name", value=secret_name, expected_type=type_hints["secret_name"])
            check_type(argname="argument share_name", value=share_name, expected_type=type_hints["share_name"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument secret_namespace", value=secret_namespace, expected_type=type_hints["secret_namespace"])
        self._values: typing.Dict[str, typing.Any] = {
            "secret_name": secret_name,
            "share_name": share_name,
        }
        if read_only is not None:
            self._values["read_only"] = read_only
        if secret_namespace is not None:
            self._values["secret_namespace"] = secret_namespace

    @builtins.property
    def secret_name(self) -> builtins.str:
        '''The name of secret that contains Azure Storage Account Name and Key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#secret_name PersistentVolumeV1#secret_name}
        '''
        result = self._values.get("secret_name")
        assert result is not None, "Required property 'secret_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def share_name(self) -> builtins.str:
        '''Share Name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#share_name PersistentVolumeV1#share_name}
        '''
        result = self._values.get("share_name")
        assert result is not None, "Required property 'share_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def secret_namespace(self) -> typing.Optional[builtins.str]:
        '''The namespace of the secret that contains Azure Storage Account Name and Key.

        For Kubernetes up to 1.18.x the default is the same as the Pod. For Kubernetes 1.19.x and later the default is "default" namespace.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#secret_namespace PersistentVolumeV1#secret_namespace}
        '''
        result = self._values.get("secret_namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1SpecPersistentVolumeSourceAzureFile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeV1SpecPersistentVolumeSourceAzureFileOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceAzureFileOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceAzureFileOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetSecretNamespace")
    def reset_secret_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="secretNameInput")
    def secret_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretNameInput"))

    @builtins.property
    @jsii.member(jsii_name="secretNamespaceInput")
    def secret_namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretNamespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="shareNameInput")
    def share_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "shareNameInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceAzureFileOutputReference, "read_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="secretName")
    def secret_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretName"))

    @secret_name.setter
    def secret_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceAzureFileOutputReference, "secret_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretName", value)

    @builtins.property
    @jsii.member(jsii_name="secretNamespace")
    def secret_namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretNamespace"))

    @secret_namespace.setter
    def secret_namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceAzureFileOutputReference, "secret_namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretNamespace", value)

    @builtins.property
    @jsii.member(jsii_name="shareName")
    def share_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "shareName"))

    @share_name.setter
    def share_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceAzureFileOutputReference, "share_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "shareName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceAzureFile]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceAzureFile], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceAzureFile],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceAzureFileOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceCephFs",
    jsii_struct_bases=[],
    name_mapping={
        "monitors": "monitors",
        "path": "path",
        "read_only": "readOnly",
        "secret_file": "secretFile",
        "secret_ref": "secretRef",
        "user": "user",
    },
)
class PersistentVolumeV1SpecPersistentVolumeSourceCephFs:
    def __init__(
        self,
        *,
        monitors: typing.Sequence[builtins.str],
        path: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        secret_file: typing.Optional[builtins.str] = None,
        secret_ref: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRef", typing.Dict[str, typing.Any]]] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param monitors: Monitors is a collection of Ceph monitors More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#monitors PersistentVolumeV1#monitors}
        :param path: Used as the mounted root, rather than the full Ceph tree, default is /. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#path PersistentVolumeV1#path}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to ``false`` (read/write). More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        :param secret_file: The path to key ring for User, default is /etc/ceph/user.secret More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#secret_file PersistentVolumeV1#secret_file}
        :param secret_ref: secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#secret_ref PersistentVolumeV1#secret_ref}
        :param user: User is the rados user name, default is admin. More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#user PersistentVolumeV1#user}
        '''
        if isinstance(secret_ref, dict):
            secret_ref = PersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRef(**secret_ref)
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceCephFs.__init__)
            check_type(argname="argument monitors", value=monitors, expected_type=type_hints["monitors"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument secret_file", value=secret_file, expected_type=type_hints["secret_file"])
            check_type(argname="argument secret_ref", value=secret_ref, expected_type=type_hints["secret_ref"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
        self._values: typing.Dict[str, typing.Any] = {
            "monitors": monitors,
        }
        if path is not None:
            self._values["path"] = path
        if read_only is not None:
            self._values["read_only"] = read_only
        if secret_file is not None:
            self._values["secret_file"] = secret_file
        if secret_ref is not None:
            self._values["secret_ref"] = secret_ref
        if user is not None:
            self._values["user"] = user

    @builtins.property
    def monitors(self) -> typing.List[builtins.str]:
        '''Monitors is a collection of Ceph monitors More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#monitors PersistentVolumeV1#monitors}
        '''
        result = self._values.get("monitors")
        assert result is not None, "Required property 'monitors' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Used as the mounted root, rather than the full Ceph tree, default is /.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#path PersistentVolumeV1#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to force the read-only setting in VolumeMounts. Defaults to ``false`` (read/write). More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def secret_file(self) -> typing.Optional[builtins.str]:
        '''The path to key ring for User, default is /etc/ceph/user.secret More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#secret_file PersistentVolumeV1#secret_file}
        '''
        result = self._values.get("secret_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secret_ref(
        self,
    ) -> typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRef"]:
        '''secret_ref block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#secret_ref PersistentVolumeV1#secret_ref}
        '''
        result = self._values.get("secret_ref")
        return typing.cast(typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRef"], result)

    @builtins.property
    def user(self) -> typing.Optional[builtins.str]:
        '''User is the rados user name, default is admin. More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#user PersistentVolumeV1#user}
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1SpecPersistentVolumeSourceCephFs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeV1SpecPersistentVolumeSourceCephFsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceCephFsOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceCephFsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSecretRef")
    def put_secret_ref(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#name PersistentVolumeV1#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#namespace PersistentVolumeV1#namespace}
        '''
        value = PersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRef(
            name=name, namespace=namespace
        )

        return typing.cast(None, jsii.invoke(self, "putSecretRef", [value]))

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetSecretFile")
    def reset_secret_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretFile", []))

    @jsii.member(jsii_name="resetSecretRef")
    def reset_secret_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretRef", []))

    @jsii.member(jsii_name="resetUser")
    def reset_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUser", []))

    @builtins.property
    @jsii.member(jsii_name="secretRef")
    def secret_ref(
        self,
    ) -> "PersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRefOutputReference":
        return typing.cast("PersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRefOutputReference", jsii.get(self, "secretRef"))

    @builtins.property
    @jsii.member(jsii_name="monitorsInput")
    def monitors_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "monitorsInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="secretFileInput")
    def secret_file_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretFileInput"))

    @builtins.property
    @jsii.member(jsii_name="secretRefInput")
    def secret_ref_input(
        self,
    ) -> typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRef"]:
        return typing.cast(typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRef"], jsii.get(self, "secretRefInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="monitors")
    def monitors(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "monitors"))

    @monitors.setter
    def monitors(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceCephFsOutputReference, "monitors").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "monitors", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceCephFsOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceCephFsOutputReference, "read_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="secretFile")
    def secret_file(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretFile"))

    @secret_file.setter
    def secret_file(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceCephFsOutputReference, "secret_file").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretFile", value)

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "user"))

    @user.setter
    def user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceCephFsOutputReference, "user").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "user", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCephFs]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCephFs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCephFs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceCephFsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class PersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRef:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#name PersistentVolumeV1#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#namespace PersistentVolumeV1#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRef.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#name PersistentVolumeV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#namespace PersistentVolumeV1#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRefOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRefOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRefOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRefOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRefOutputReference, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRef]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRefOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceCinder",
    jsii_struct_bases=[],
    name_mapping={
        "volume_id": "volumeId",
        "fs_type": "fsType",
        "read_only": "readOnly",
    },
)
class PersistentVolumeV1SpecPersistentVolumeSourceCinder:
    def __init__(
        self,
        *,
        volume_id: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param volume_id: Volume ID used to identify the volume in Cinder. More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#volume_id PersistentVolumeV1#volume_id}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fs_type PersistentVolumeV1#fs_type}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceCinder.__init__)
            check_type(argname="argument volume_id", value=volume_id, expected_type=type_hints["volume_id"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[str, typing.Any] = {
            "volume_id": volume_id,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def volume_id(self) -> builtins.str:
        '''Volume ID used to identify the volume in Cinder. More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#volume_id PersistentVolumeV1#volume_id}
        '''
        result = self._values.get("volume_id")
        assert result is not None, "Required property 'volume_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type to mount.

        Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fs_type PersistentVolumeV1#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1SpecPersistentVolumeSourceCinder(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeV1SpecPersistentVolumeSourceCinderOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceCinderOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceCinderOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeIdInput")
    def volume_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceCinderOutputReference, "fs_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceCinderOutputReference, "read_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="volumeId")
    def volume_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeId"))

    @volume_id.setter
    def volume_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceCinderOutputReference, "volume_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCinder]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCinder], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCinder],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceCinderOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceCsi",
    jsii_struct_bases=[],
    name_mapping={
        "driver": "driver",
        "volume_handle": "volumeHandle",
        "controller_expand_secret_ref": "controllerExpandSecretRef",
        "controller_publish_secret_ref": "controllerPublishSecretRef",
        "fs_type": "fsType",
        "node_publish_secret_ref": "nodePublishSecretRef",
        "node_stage_secret_ref": "nodeStageSecretRef",
        "read_only": "readOnly",
        "volume_attributes": "volumeAttributes",
    },
)
class PersistentVolumeV1SpecPersistentVolumeSourceCsi:
    def __init__(
        self,
        *,
        driver: builtins.str,
        volume_handle: builtins.str,
        controller_expand_secret_ref: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRef", typing.Dict[str, typing.Any]]] = None,
        controller_publish_secret_ref: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRef", typing.Dict[str, typing.Any]]] = None,
        fs_type: typing.Optional[builtins.str] = None,
        node_publish_secret_ref: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRef", typing.Dict[str, typing.Any]]] = None,
        node_stage_secret_ref: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRef", typing.Dict[str, typing.Any]]] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        volume_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param driver: the name of the volume driver to use. More info: https://kubernetes.io/docs/concepts/storage/volumes/#csi. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#driver PersistentVolumeV1#driver}
        :param volume_handle: A string value that uniquely identifies the volume. More info: https://kubernetes.io/docs/concepts/storage/volumes/#csi. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#volume_handle PersistentVolumeV1#volume_handle}
        :param controller_expand_secret_ref: controller_expand_secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#controller_expand_secret_ref PersistentVolumeV1#controller_expand_secret_ref}
        :param controller_publish_secret_ref: controller_publish_secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#controller_publish_secret_ref PersistentVolumeV1#controller_publish_secret_ref}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fs_type PersistentVolumeV1#fs_type}
        :param node_publish_secret_ref: node_publish_secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#node_publish_secret_ref PersistentVolumeV1#node_publish_secret_ref}
        :param node_stage_secret_ref: node_stage_secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#node_stage_secret_ref PersistentVolumeV1#node_stage_secret_ref}
        :param read_only: Whether to set the read-only property in VolumeMounts to "true". If omitted, the default is "false". More info: http://kubernetes.io/docs/user-guide/volumes#csi. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        :param volume_attributes: Attributes of the volume to publish. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#volume_attributes PersistentVolumeV1#volume_attributes}
        '''
        if isinstance(controller_expand_secret_ref, dict):
            controller_expand_secret_ref = PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRef(**controller_expand_secret_ref)
        if isinstance(controller_publish_secret_ref, dict):
            controller_publish_secret_ref = PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRef(**controller_publish_secret_ref)
        if isinstance(node_publish_secret_ref, dict):
            node_publish_secret_ref = PersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRef(**node_publish_secret_ref)
        if isinstance(node_stage_secret_ref, dict):
            node_stage_secret_ref = PersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRef(**node_stage_secret_ref)
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceCsi.__init__)
            check_type(argname="argument driver", value=driver, expected_type=type_hints["driver"])
            check_type(argname="argument volume_handle", value=volume_handle, expected_type=type_hints["volume_handle"])
            check_type(argname="argument controller_expand_secret_ref", value=controller_expand_secret_ref, expected_type=type_hints["controller_expand_secret_ref"])
            check_type(argname="argument controller_publish_secret_ref", value=controller_publish_secret_ref, expected_type=type_hints["controller_publish_secret_ref"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument node_publish_secret_ref", value=node_publish_secret_ref, expected_type=type_hints["node_publish_secret_ref"])
            check_type(argname="argument node_stage_secret_ref", value=node_stage_secret_ref, expected_type=type_hints["node_stage_secret_ref"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument volume_attributes", value=volume_attributes, expected_type=type_hints["volume_attributes"])
        self._values: typing.Dict[str, typing.Any] = {
            "driver": driver,
            "volume_handle": volume_handle,
        }
        if controller_expand_secret_ref is not None:
            self._values["controller_expand_secret_ref"] = controller_expand_secret_ref
        if controller_publish_secret_ref is not None:
            self._values["controller_publish_secret_ref"] = controller_publish_secret_ref
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if node_publish_secret_ref is not None:
            self._values["node_publish_secret_ref"] = node_publish_secret_ref
        if node_stage_secret_ref is not None:
            self._values["node_stage_secret_ref"] = node_stage_secret_ref
        if read_only is not None:
            self._values["read_only"] = read_only
        if volume_attributes is not None:
            self._values["volume_attributes"] = volume_attributes

    @builtins.property
    def driver(self) -> builtins.str:
        '''the name of the volume driver to use. More info: https://kubernetes.io/docs/concepts/storage/volumes/#csi.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#driver PersistentVolumeV1#driver}
        '''
        result = self._values.get("driver")
        assert result is not None, "Required property 'driver' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def volume_handle(self) -> builtins.str:
        '''A string value that uniquely identifies the volume. More info: https://kubernetes.io/docs/concepts/storage/volumes/#csi.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#volume_handle PersistentVolumeV1#volume_handle}
        '''
        result = self._values.get("volume_handle")
        assert result is not None, "Required property 'volume_handle' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def controller_expand_secret_ref(
        self,
    ) -> typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRef"]:
        '''controller_expand_secret_ref block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#controller_expand_secret_ref PersistentVolumeV1#controller_expand_secret_ref}
        '''
        result = self._values.get("controller_expand_secret_ref")
        return typing.cast(typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRef"], result)

    @builtins.property
    def controller_publish_secret_ref(
        self,
    ) -> typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRef"]:
        '''controller_publish_secret_ref block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#controller_publish_secret_ref PersistentVolumeV1#controller_publish_secret_ref}
        '''
        result = self._values.get("controller_publish_secret_ref")
        return typing.cast(typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRef"], result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type to mount.

        Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fs_type PersistentVolumeV1#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_publish_secret_ref(
        self,
    ) -> typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRef"]:
        '''node_publish_secret_ref block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#node_publish_secret_ref PersistentVolumeV1#node_publish_secret_ref}
        '''
        result = self._values.get("node_publish_secret_ref")
        return typing.cast(typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRef"], result)

    @builtins.property
    def node_stage_secret_ref(
        self,
    ) -> typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRef"]:
        '''node_stage_secret_ref block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#node_stage_secret_ref PersistentVolumeV1#node_stage_secret_ref}
        '''
        result = self._values.get("node_stage_secret_ref")
        return typing.cast(typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRef"], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to set the read-only property in VolumeMounts to "true". If omitted, the default is "false". More info: http://kubernetes.io/docs/user-guide/volumes#csi.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def volume_attributes(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Attributes of the volume to publish.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#volume_attributes PersistentVolumeV1#volume_attributes}
        '''
        result = self._values.get("volume_attributes")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1SpecPersistentVolumeSourceCsi(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRef:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#name PersistentVolumeV1#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#namespace PersistentVolumeV1#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRef.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#name PersistentVolumeV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#namespace PersistentVolumeV1#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRefOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRefOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRefOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRefOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRefOutputReference, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRef]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRefOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRef:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#name PersistentVolumeV1#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#namespace PersistentVolumeV1#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRef.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#name PersistentVolumeV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#namespace PersistentVolumeV1#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRefOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRefOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRefOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRefOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRefOutputReference, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRef]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRefOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class PersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRef:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#name PersistentVolumeV1#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#namespace PersistentVolumeV1#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRef.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#name PersistentVolumeV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#namespace PersistentVolumeV1#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRefOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRefOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRefOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRefOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRefOutputReference, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRef]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRefOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class PersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRef:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#name PersistentVolumeV1#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#namespace PersistentVolumeV1#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRef.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#name PersistentVolumeV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#namespace PersistentVolumeV1#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRefOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRefOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRefOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRefOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRefOutputReference, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRef]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRefOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PersistentVolumeV1SpecPersistentVolumeSourceCsiOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceCsiOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceCsiOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putControllerExpandSecretRef")
    def put_controller_expand_secret_ref(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#name PersistentVolumeV1#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#namespace PersistentVolumeV1#namespace}
        '''
        value = PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRef(
            name=name, namespace=namespace
        )

        return typing.cast(None, jsii.invoke(self, "putControllerExpandSecretRef", [value]))

    @jsii.member(jsii_name="putControllerPublishSecretRef")
    def put_controller_publish_secret_ref(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#name PersistentVolumeV1#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#namespace PersistentVolumeV1#namespace}
        '''
        value = PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRef(
            name=name, namespace=namespace
        )

        return typing.cast(None, jsii.invoke(self, "putControllerPublishSecretRef", [value]))

    @jsii.member(jsii_name="putNodePublishSecretRef")
    def put_node_publish_secret_ref(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#name PersistentVolumeV1#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#namespace PersistentVolumeV1#namespace}
        '''
        value = PersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRef(
            name=name, namespace=namespace
        )

        return typing.cast(None, jsii.invoke(self, "putNodePublishSecretRef", [value]))

    @jsii.member(jsii_name="putNodeStageSecretRef")
    def put_node_stage_secret_ref(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#name PersistentVolumeV1#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#namespace PersistentVolumeV1#namespace}
        '''
        value = PersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRef(
            name=name, namespace=namespace
        )

        return typing.cast(None, jsii.invoke(self, "putNodeStageSecretRef", [value]))

    @jsii.member(jsii_name="resetControllerExpandSecretRef")
    def reset_controller_expand_secret_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetControllerExpandSecretRef", []))

    @jsii.member(jsii_name="resetControllerPublishSecretRef")
    def reset_controller_publish_secret_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetControllerPublishSecretRef", []))

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetNodePublishSecretRef")
    def reset_node_publish_secret_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodePublishSecretRef", []))

    @jsii.member(jsii_name="resetNodeStageSecretRef")
    def reset_node_stage_secret_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeStageSecretRef", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetVolumeAttributes")
    def reset_volume_attributes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeAttributes", []))

    @builtins.property
    @jsii.member(jsii_name="controllerExpandSecretRef")
    def controller_expand_secret_ref(
        self,
    ) -> PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRefOutputReference:
        return typing.cast(PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRefOutputReference, jsii.get(self, "controllerExpandSecretRef"))

    @builtins.property
    @jsii.member(jsii_name="controllerPublishSecretRef")
    def controller_publish_secret_ref(
        self,
    ) -> PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRefOutputReference:
        return typing.cast(PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRefOutputReference, jsii.get(self, "controllerPublishSecretRef"))

    @builtins.property
    @jsii.member(jsii_name="nodePublishSecretRef")
    def node_publish_secret_ref(
        self,
    ) -> PersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRefOutputReference:
        return typing.cast(PersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRefOutputReference, jsii.get(self, "nodePublishSecretRef"))

    @builtins.property
    @jsii.member(jsii_name="nodeStageSecretRef")
    def node_stage_secret_ref(
        self,
    ) -> PersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRefOutputReference:
        return typing.cast(PersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRefOutputReference, jsii.get(self, "nodeStageSecretRef"))

    @builtins.property
    @jsii.member(jsii_name="controllerExpandSecretRefInput")
    def controller_expand_secret_ref_input(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRef]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRef], jsii.get(self, "controllerExpandSecretRefInput"))

    @builtins.property
    @jsii.member(jsii_name="controllerPublishSecretRefInput")
    def controller_publish_secret_ref_input(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRef]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRef], jsii.get(self, "controllerPublishSecretRefInput"))

    @builtins.property
    @jsii.member(jsii_name="driverInput")
    def driver_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "driverInput"))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="nodePublishSecretRefInput")
    def node_publish_secret_ref_input(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRef]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRef], jsii.get(self, "nodePublishSecretRefInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeStageSecretRefInput")
    def node_stage_secret_ref_input(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRef]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRef], jsii.get(self, "nodeStageSecretRefInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeAttributesInput")
    def volume_attributes_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "volumeAttributesInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeHandleInput")
    def volume_handle_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeHandleInput"))

    @builtins.property
    @jsii.member(jsii_name="driver")
    def driver(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "driver"))

    @driver.setter
    def driver(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceCsiOutputReference, "driver").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driver", value)

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceCsiOutputReference, "fs_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceCsiOutputReference, "read_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="volumeAttributes")
    def volume_attributes(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "volumeAttributes"))

    @volume_attributes.setter
    def volume_attributes(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceCsiOutputReference, "volume_attributes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="volumeHandle")
    def volume_handle(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumeHandle"))

    @volume_handle.setter
    def volume_handle(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceCsiOutputReference, "volume_handle").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeHandle", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCsi]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCsi], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCsi],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceCsiOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceFc",
    jsii_struct_bases=[],
    name_mapping={
        "lun": "lun",
        "target_ww_ns": "targetWwNs",
        "fs_type": "fsType",
        "read_only": "readOnly",
    },
)
class PersistentVolumeV1SpecPersistentVolumeSourceFc:
    def __init__(
        self,
        *,
        lun: jsii.Number,
        target_ww_ns: typing.Sequence[builtins.str],
        fs_type: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param lun: FC target lun number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#lun PersistentVolumeV1#lun}
        :param target_ww_ns: FC target worldwide names (WWNs). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#target_ww_ns PersistentVolumeV1#target_ww_ns}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fs_type PersistentVolumeV1#fs_type}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceFc.__init__)
            check_type(argname="argument lun", value=lun, expected_type=type_hints["lun"])
            check_type(argname="argument target_ww_ns", value=target_ww_ns, expected_type=type_hints["target_ww_ns"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[str, typing.Any] = {
            "lun": lun,
            "target_ww_ns": target_ww_ns,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def lun(self) -> jsii.Number:
        '''FC target lun number.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#lun PersistentVolumeV1#lun}
        '''
        result = self._values.get("lun")
        assert result is not None, "Required property 'lun' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def target_ww_ns(self) -> typing.List[builtins.str]:
        '''FC target worldwide names (WWNs).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#target_ww_ns PersistentVolumeV1#target_ww_ns}
        '''
        result = self._values.get("target_ww_ns")
        assert result is not None, "Required property 'target_ww_ns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type to mount.

        Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fs_type PersistentVolumeV1#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1SpecPersistentVolumeSourceFc(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeV1SpecPersistentVolumeSourceFcOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceFcOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceFcOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="lunInput")
    def lun_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lunInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="targetWwNsInput")
    def target_ww_ns_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "targetWwNsInput"))

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceFcOutputReference, "fs_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="lun")
    def lun(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lun"))

    @lun.setter
    def lun(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceFcOutputReference, "lun").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lun", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceFcOutputReference, "read_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="targetWwNs")
    def target_ww_ns(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "targetWwNs"))

    @target_ww_ns.setter
    def target_ww_ns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceFcOutputReference, "target_ww_ns").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetWwNs", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceFc]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceFc], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceFc],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceFcOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceFlexVolume",
    jsii_struct_bases=[],
    name_mapping={
        "driver": "driver",
        "fs_type": "fsType",
        "options": "options",
        "read_only": "readOnly",
        "secret_ref": "secretRef",
    },
)
class PersistentVolumeV1SpecPersistentVolumeSourceFlexVolume:
    def __init__(
        self,
        *,
        driver: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        secret_ref: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRef", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param driver: Driver is the name of the driver to use for this volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#driver PersistentVolumeV1#driver}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fs_type PersistentVolumeV1#fs_type}
        :param options: Extra command options if any. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#options PersistentVolumeV1#options}
        :param read_only: Whether to force the ReadOnly setting in VolumeMounts. Defaults to false (read/write). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        :param secret_ref: secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#secret_ref PersistentVolumeV1#secret_ref}
        '''
        if isinstance(secret_ref, dict):
            secret_ref = PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRef(**secret_ref)
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceFlexVolume.__init__)
            check_type(argname="argument driver", value=driver, expected_type=type_hints["driver"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument options", value=options, expected_type=type_hints["options"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument secret_ref", value=secret_ref, expected_type=type_hints["secret_ref"])
        self._values: typing.Dict[str, typing.Any] = {
            "driver": driver,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if options is not None:
            self._values["options"] = options
        if read_only is not None:
            self._values["read_only"] = read_only
        if secret_ref is not None:
            self._values["secret_ref"] = secret_ref

    @builtins.property
    def driver(self) -> builtins.str:
        '''Driver is the name of the driver to use for this volume.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#driver PersistentVolumeV1#driver}
        '''
        result = self._values.get("driver")
        assert result is not None, "Required property 'driver' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type to mount.

        Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fs_type PersistentVolumeV1#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def options(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Extra command options if any.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#options PersistentVolumeV1#options}
        '''
        result = self._values.get("options")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to force the ReadOnly setting in VolumeMounts. Defaults to false (read/write).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def secret_ref(
        self,
    ) -> typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRef"]:
        '''secret_ref block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#secret_ref PersistentVolumeV1#secret_ref}
        '''
        result = self._values.get("secret_ref")
        return typing.cast(typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRef"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1SpecPersistentVolumeSourceFlexVolume(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSecretRef")
    def put_secret_ref(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#name PersistentVolumeV1#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#namespace PersistentVolumeV1#namespace}
        '''
        value = PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRef(
            name=name, namespace=namespace
        )

        return typing.cast(None, jsii.invoke(self, "putSecretRef", [value]))

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetOptions")
    def reset_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOptions", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetSecretRef")
    def reset_secret_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretRef", []))

    @builtins.property
    @jsii.member(jsii_name="secretRef")
    def secret_ref(
        self,
    ) -> "PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRefOutputReference":
        return typing.cast("PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRefOutputReference", jsii.get(self, "secretRef"))

    @builtins.property
    @jsii.member(jsii_name="driverInput")
    def driver_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "driverInput"))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="optionsInput")
    def options_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "optionsInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="secretRefInput")
    def secret_ref_input(
        self,
    ) -> typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRef"]:
        return typing.cast(typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRef"], jsii.get(self, "secretRefInput"))

    @builtins.property
    @jsii.member(jsii_name="driver")
    def driver(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "driver"))

    @driver.setter
    def driver(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeOutputReference, "driver").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driver", value)

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeOutputReference, "fs_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="options")
    def options(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "options"))

    @options.setter
    def options(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeOutputReference, "options").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "options", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeOutputReference, "read_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceFlexVolume]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceFlexVolume], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceFlexVolume],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRef:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#name PersistentVolumeV1#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#namespace PersistentVolumeV1#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRef.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#name PersistentVolumeV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#namespace PersistentVolumeV1#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRefOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRefOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRefOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRefOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRefOutputReference, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRef]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRefOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceFlocker",
    jsii_struct_bases=[],
    name_mapping={"dataset_name": "datasetName", "dataset_uuid": "datasetUuid"},
)
class PersistentVolumeV1SpecPersistentVolumeSourceFlocker:
    def __init__(
        self,
        *,
        dataset_name: typing.Optional[builtins.str] = None,
        dataset_uuid: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dataset_name: Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#dataset_name PersistentVolumeV1#dataset_name}
        :param dataset_uuid: UUID of the dataset. This is unique identifier of a Flocker dataset. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#dataset_uuid PersistentVolumeV1#dataset_uuid}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceFlocker.__init__)
            check_type(argname="argument dataset_name", value=dataset_name, expected_type=type_hints["dataset_name"])
            check_type(argname="argument dataset_uuid", value=dataset_uuid, expected_type=type_hints["dataset_uuid"])
        self._values: typing.Dict[str, typing.Any] = {}
        if dataset_name is not None:
            self._values["dataset_name"] = dataset_name
        if dataset_uuid is not None:
            self._values["dataset_uuid"] = dataset_uuid

    @builtins.property
    def dataset_name(self) -> typing.Optional[builtins.str]:
        '''Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#dataset_name PersistentVolumeV1#dataset_name}
        '''
        result = self._values.get("dataset_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dataset_uuid(self) -> typing.Optional[builtins.str]:
        '''UUID of the dataset. This is unique identifier of a Flocker dataset.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#dataset_uuid PersistentVolumeV1#dataset_uuid}
        '''
        result = self._values.get("dataset_uuid")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1SpecPersistentVolumeSourceFlocker(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeV1SpecPersistentVolumeSourceFlockerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceFlockerOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceFlockerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDatasetName")
    def reset_dataset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatasetName", []))

    @jsii.member(jsii_name="resetDatasetUuid")
    def reset_dataset_uuid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatasetUuid", []))

    @builtins.property
    @jsii.member(jsii_name="datasetNameInput")
    def dataset_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetNameInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetUuidInput")
    def dataset_uuid_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetUuidInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetName")
    def dataset_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetName"))

    @dataset_name.setter
    def dataset_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceFlockerOutputReference, "dataset_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetName", value)

    @builtins.property
    @jsii.member(jsii_name="datasetUuid")
    def dataset_uuid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetUuid"))

    @dataset_uuid.setter
    def dataset_uuid(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceFlockerOutputReference, "dataset_uuid").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetUuid", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceFlocker]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceFlocker], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceFlocker],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceFlockerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDisk",
    jsii_struct_bases=[],
    name_mapping={
        "pd_name": "pdName",
        "fs_type": "fsType",
        "partition": "partition",
        "read_only": "readOnly",
    },
)
class PersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDisk:
    def __init__(
        self,
        *,
        pd_name: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        partition: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param pd_name: Unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#pd_name PersistentVolumeV1#pd_name}
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fs_type PersistentVolumeV1#fs_type}
        :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#partition PersistentVolumeV1#partition}
        :param read_only: Whether to force the ReadOnly setting in VolumeMounts. Defaults to false. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDisk.__init__)
            check_type(argname="argument pd_name", value=pd_name, expected_type=type_hints["pd_name"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument partition", value=partition, expected_type=type_hints["partition"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[str, typing.Any] = {
            "pd_name": pd_name,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if partition is not None:
            self._values["partition"] = partition
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def pd_name(self) -> builtins.str:
        '''Unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#pd_name PersistentVolumeV1#pd_name}
        '''
        result = self._values.get("pd_name")
        assert result is not None, "Required property 'pd_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type of the volume that you want to mount.

        Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fs_type PersistentVolumeV1#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partition(self) -> typing.Optional[jsii.Number]:
        '''The partition in the volume that you want to mount.

        If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#partition PersistentVolumeV1#partition}
        '''
        result = self._values.get("partition")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to force the ReadOnly setting in VolumeMounts. Defaults to false. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDiskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDiskOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDiskOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetPartition")
    def reset_partition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartition", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="partitionInput")
    def partition_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "partitionInput"))

    @builtins.property
    @jsii.member(jsii_name="pdNameInput")
    def pd_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pdNameInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDiskOutputReference, "fs_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="partition")
    def partition(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "partition"))

    @partition.setter
    def partition(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDiskOutputReference, "partition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partition", value)

    @builtins.property
    @jsii.member(jsii_name="pdName")
    def pd_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pdName"))

    @pd_name.setter
    def pd_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDiskOutputReference, "pd_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pdName", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDiskOutputReference, "read_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDisk]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDisk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDisk],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDiskOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceGlusterfs",
    jsii_struct_bases=[],
    name_mapping={
        "endpoints_name": "endpointsName",
        "path": "path",
        "read_only": "readOnly",
    },
)
class PersistentVolumeV1SpecPersistentVolumeSourceGlusterfs:
    def __init__(
        self,
        *,
        endpoints_name: builtins.str,
        path: builtins.str,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param endpoints_name: The endpoint name that details Glusterfs topology. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#endpoints_name PersistentVolumeV1#endpoints_name}
        :param path: The Glusterfs volume path. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#path PersistentVolumeV1#path}
        :param read_only: Whether to force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceGlusterfs.__init__)
            check_type(argname="argument endpoints_name", value=endpoints_name, expected_type=type_hints["endpoints_name"])
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[str, typing.Any] = {
            "endpoints_name": endpoints_name,
            "path": path,
        }
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def endpoints_name(self) -> builtins.str:
        '''The endpoint name that details Glusterfs topology. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#endpoints_name PersistentVolumeV1#endpoints_name}
        '''
        result = self._values.get("endpoints_name")
        assert result is not None, "Required property 'endpoints_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def path(self) -> builtins.str:
        '''The Glusterfs volume path. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#path PersistentVolumeV1#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1SpecPersistentVolumeSourceGlusterfs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeV1SpecPersistentVolumeSourceGlusterfsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceGlusterfsOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceGlusterfsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="endpointsNameInput")
    def endpoints_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointsNameInput"))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointsName")
    def endpoints_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpointsName"))

    @endpoints_name.setter
    def endpoints_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceGlusterfsOutputReference, "endpoints_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointsName", value)

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceGlusterfsOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceGlusterfsOutputReference, "read_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceGlusterfs]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceGlusterfs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceGlusterfs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceGlusterfsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceHostPath",
    jsii_struct_bases=[],
    name_mapping={"path": "path", "type": "type"},
)
class PersistentVolumeV1SpecPersistentVolumeSourceHostPath:
    def __init__(
        self,
        *,
        path: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param path: Path of the directory on the host. More info: http://kubernetes.io/docs/user-guide/volumes#hostpath. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#path PersistentVolumeV1#path}
        :param type: Type for HostPath volume. Allowed values are "" (default), DirectoryOrCreate, Directory, FileOrCreate, File, Socket, CharDevice and BlockDevice. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#type PersistentVolumeV1#type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceHostPath.__init__)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if path is not None:
            self._values["path"] = path
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Path of the directory on the host. More info: http://kubernetes.io/docs/user-guide/volumes#hostpath.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#path PersistentVolumeV1#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Type for HostPath volume. Allowed values are "" (default), DirectoryOrCreate, Directory, FileOrCreate, File, Socket, CharDevice and BlockDevice.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#type PersistentVolumeV1#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1SpecPersistentVolumeSourceHostPath(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeV1SpecPersistentVolumeSourceHostPathOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceHostPathOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceHostPathOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceHostPathOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceHostPathOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceHostPath]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceHostPath], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceHostPath],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceHostPathOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceIscsi",
    jsii_struct_bases=[],
    name_mapping={
        "iqn": "iqn",
        "target_portal": "targetPortal",
        "fs_type": "fsType",
        "iscsi_interface": "iscsiInterface",
        "lun": "lun",
        "read_only": "readOnly",
    },
)
class PersistentVolumeV1SpecPersistentVolumeSourceIscsi:
    def __init__(
        self,
        *,
        iqn: builtins.str,
        target_portal: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        iscsi_interface: typing.Optional[builtins.str] = None,
        lun: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param iqn: Target iSCSI Qualified Name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#iqn PersistentVolumeV1#iqn}
        :param target_portal: iSCSI target portal. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#target_portal PersistentVolumeV1#target_portal}
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#iscsi Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fs_type PersistentVolumeV1#fs_type}
        :param iscsi_interface: iSCSI interface name that uses an iSCSI transport. Defaults to 'default' (tcp). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#iscsi_interface PersistentVolumeV1#iscsi_interface}
        :param lun: iSCSI target lun number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#lun PersistentVolumeV1#lun}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceIscsi.__init__)
            check_type(argname="argument iqn", value=iqn, expected_type=type_hints["iqn"])
            check_type(argname="argument target_portal", value=target_portal, expected_type=type_hints["target_portal"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument iscsi_interface", value=iscsi_interface, expected_type=type_hints["iscsi_interface"])
            check_type(argname="argument lun", value=lun, expected_type=type_hints["lun"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[str, typing.Any] = {
            "iqn": iqn,
            "target_portal": target_portal,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if iscsi_interface is not None:
            self._values["iscsi_interface"] = iscsi_interface
        if lun is not None:
            self._values["lun"] = lun
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def iqn(self) -> builtins.str:
        '''Target iSCSI Qualified Name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#iqn PersistentVolumeV1#iqn}
        '''
        result = self._values.get("iqn")
        assert result is not None, "Required property 'iqn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_portal(self) -> builtins.str:
        '''iSCSI target portal.

        The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#target_portal PersistentVolumeV1#target_portal}
        '''
        result = self._values.get("target_portal")
        assert result is not None, "Required property 'target_portal' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type of the volume that you want to mount.

        Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#iscsi

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fs_type PersistentVolumeV1#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iscsi_interface(self) -> typing.Optional[builtins.str]:
        '''iSCSI interface name that uses an iSCSI transport. Defaults to 'default' (tcp).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#iscsi_interface PersistentVolumeV1#iscsi_interface}
        '''
        result = self._values.get("iscsi_interface")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lun(self) -> typing.Optional[jsii.Number]:
        '''iSCSI target lun number.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#lun PersistentVolumeV1#lun}
        '''
        result = self._values.get("lun")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to force the read-only setting in VolumeMounts. Defaults to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1SpecPersistentVolumeSourceIscsi(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeV1SpecPersistentVolumeSourceIscsiOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceIscsiOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceIscsiOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetIscsiInterface")
    def reset_iscsi_interface(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIscsiInterface", []))

    @jsii.member(jsii_name="resetLun")
    def reset_lun(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLun", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="iqnInput")
    def iqn_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iqnInput"))

    @builtins.property
    @jsii.member(jsii_name="iscsiInterfaceInput")
    def iscsi_interface_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iscsiInterfaceInput"))

    @builtins.property
    @jsii.member(jsii_name="lunInput")
    def lun_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lunInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="targetPortalInput")
    def target_portal_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetPortalInput"))

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceIscsiOutputReference, "fs_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="iqn")
    def iqn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iqn"))

    @iqn.setter
    def iqn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceIscsiOutputReference, "iqn").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iqn", value)

    @builtins.property
    @jsii.member(jsii_name="iscsiInterface")
    def iscsi_interface(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iscsiInterface"))

    @iscsi_interface.setter
    def iscsi_interface(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceIscsiOutputReference, "iscsi_interface").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iscsiInterface", value)

    @builtins.property
    @jsii.member(jsii_name="lun")
    def lun(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lun"))

    @lun.setter
    def lun(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceIscsiOutputReference, "lun").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lun", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceIscsiOutputReference, "read_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="targetPortal")
    def target_portal(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "targetPortal"))

    @target_portal.setter
    def target_portal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceIscsiOutputReference, "target_portal").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetPortal", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceIscsi]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceIscsi], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceIscsi],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceIscsiOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceLocal",
    jsii_struct_bases=[],
    name_mapping={"path": "path"},
)
class PersistentVolumeV1SpecPersistentVolumeSourceLocal:
    def __init__(self, *, path: typing.Optional[builtins.str] = None) -> None:
        '''
        :param path: Path of the directory on the host. More info: http://kubernetes.io/docs/user-guide/volumes#local. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#path PersistentVolumeV1#path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceLocal.__init__)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
        self._values: typing.Dict[str, typing.Any] = {}
        if path is not None:
            self._values["path"] = path

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Path of the directory on the host. More info: http://kubernetes.io/docs/user-guide/volumes#local.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#path PersistentVolumeV1#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1SpecPersistentVolumeSourceLocal(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeV1SpecPersistentVolumeSourceLocalOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceLocalOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceLocalOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceLocalOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceLocal]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceLocal], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceLocal],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceLocalOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceNfs",
    jsii_struct_bases=[],
    name_mapping={"path": "path", "server": "server", "read_only": "readOnly"},
)
class PersistentVolumeV1SpecPersistentVolumeSourceNfs:
    def __init__(
        self,
        *,
        path: builtins.str,
        server: builtins.str,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param path: Path that is exported by the NFS server. More info: http://kubernetes.io/docs/user-guide/volumes#nfs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#path PersistentVolumeV1#path}
        :param server: Server is the hostname or IP address of the NFS server. More info: http://kubernetes.io/docs/user-guide/volumes#nfs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#server PersistentVolumeV1#server}
        :param read_only: Whether to force the NFS export to be mounted with read-only permissions. Defaults to false. More info: http://kubernetes.io/docs/user-guide/volumes#nfs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceNfs.__init__)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument server", value=server, expected_type=type_hints["server"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[str, typing.Any] = {
            "path": path,
            "server": server,
        }
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def path(self) -> builtins.str:
        '''Path that is exported by the NFS server. More info: http://kubernetes.io/docs/user-guide/volumes#nfs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#path PersistentVolumeV1#path}
        '''
        result = self._values.get("path")
        assert result is not None, "Required property 'path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def server(self) -> builtins.str:
        '''Server is the hostname or IP address of the NFS server. More info: http://kubernetes.io/docs/user-guide/volumes#nfs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#server PersistentVolumeV1#server}
        '''
        result = self._values.get("server")
        assert result is not None, "Required property 'server' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to force the NFS export to be mounted with read-only permissions. Defaults to false. More info: http://kubernetes.io/docs/user-guide/volumes#nfs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1SpecPersistentVolumeSourceNfs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeV1SpecPersistentVolumeSourceNfsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceNfsOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceNfsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="serverInput")
    def server_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceNfsOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceNfsOutputReference, "read_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="server")
    def server(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "server"))

    @server.setter
    def server(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceNfsOutputReference, "server").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "server", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceNfs]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceNfs], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceNfs],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceNfsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PersistentVolumeV1SpecPersistentVolumeSourceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAwsElasticBlockStore")
    def put_aws_elastic_block_store(
        self,
        *,
        volume_id: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        partition: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param volume_id: Unique ID of the persistent disk resource in AWS (Amazon EBS volume). More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#volume_id PersistentVolumeV1#volume_id}
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fs_type PersistentVolumeV1#fs_type}
        :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#partition PersistentVolumeV1#partition}
        :param read_only: Whether to set the read-only property in VolumeMounts to "true". If omitted, the default is "false". More info: http://kubernetes.io/docs/user-guide/volumes#awselasticblockstore. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        '''
        value = PersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStore(
            volume_id=volume_id,
            fs_type=fs_type,
            partition=partition,
            read_only=read_only,
        )

        return typing.cast(None, jsii.invoke(self, "putAwsElasticBlockStore", [value]))

    @jsii.member(jsii_name="putAzureDisk")
    def put_azure_disk(
        self,
        *,
        caching_mode: builtins.str,
        data_disk_uri: builtins.str,
        disk_name: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param caching_mode: Host Caching mode: None, Read Only, Read Write. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#caching_mode PersistentVolumeV1#caching_mode}
        :param data_disk_uri: The URI the data disk in the blob storage. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#data_disk_uri PersistentVolumeV1#data_disk_uri}
        :param disk_name: The Name of the data disk in the blob storage. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#disk_name PersistentVolumeV1#disk_name}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fs_type PersistentVolumeV1#fs_type}
        :param kind: The type for the data disk. Expected values: Shared, Dedicated, Managed. Defaults to Shared. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#kind PersistentVolumeV1#kind}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        '''
        value = PersistentVolumeV1SpecPersistentVolumeSourceAzureDisk(
            caching_mode=caching_mode,
            data_disk_uri=data_disk_uri,
            disk_name=disk_name,
            fs_type=fs_type,
            kind=kind,
            read_only=read_only,
        )

        return typing.cast(None, jsii.invoke(self, "putAzureDisk", [value]))

    @jsii.member(jsii_name="putAzureFile")
    def put_azure_file(
        self,
        *,
        secret_name: builtins.str,
        share_name: builtins.str,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        secret_namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param secret_name: The name of secret that contains Azure Storage Account Name and Key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#secret_name PersistentVolumeV1#secret_name}
        :param share_name: Share Name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#share_name PersistentVolumeV1#share_name}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        :param secret_namespace: The namespace of the secret that contains Azure Storage Account Name and Key. For Kubernetes up to 1.18.x the default is the same as the Pod. For Kubernetes 1.19.x and later the default is "default" namespace. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#secret_namespace PersistentVolumeV1#secret_namespace}
        '''
        value = PersistentVolumeV1SpecPersistentVolumeSourceAzureFile(
            secret_name=secret_name,
            share_name=share_name,
            read_only=read_only,
            secret_namespace=secret_namespace,
        )

        return typing.cast(None, jsii.invoke(self, "putAzureFile", [value]))

    @jsii.member(jsii_name="putCephFs")
    def put_ceph_fs(
        self,
        *,
        monitors: typing.Sequence[builtins.str],
        path: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        secret_file: typing.Optional[builtins.str] = None,
        secret_ref: typing.Optional[typing.Union[PersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRef, typing.Dict[str, typing.Any]]] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param monitors: Monitors is a collection of Ceph monitors More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#monitors PersistentVolumeV1#monitors}
        :param path: Used as the mounted root, rather than the full Ceph tree, default is /. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#path PersistentVolumeV1#path}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to ``false`` (read/write). More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        :param secret_file: The path to key ring for User, default is /etc/ceph/user.secret More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#secret_file PersistentVolumeV1#secret_file}
        :param secret_ref: secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#secret_ref PersistentVolumeV1#secret_ref}
        :param user: User is the rados user name, default is admin. More info: http://releases.k8s.io/HEAD/examples/volumes/cephfs/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#user PersistentVolumeV1#user}
        '''
        value = PersistentVolumeV1SpecPersistentVolumeSourceCephFs(
            monitors=monitors,
            path=path,
            read_only=read_only,
            secret_file=secret_file,
            secret_ref=secret_ref,
            user=user,
        )

        return typing.cast(None, jsii.invoke(self, "putCephFs", [value]))

    @jsii.member(jsii_name="putCinder")
    def put_cinder(
        self,
        *,
        volume_id: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param volume_id: Volume ID used to identify the volume in Cinder. More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#volume_id PersistentVolumeV1#volume_id}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fs_type PersistentVolumeV1#fs_type}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). More info: http://releases.k8s.io/HEAD/examples/mysql-cinder-pd/README.md. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        '''
        value = PersistentVolumeV1SpecPersistentVolumeSourceCinder(
            volume_id=volume_id, fs_type=fs_type, read_only=read_only
        )

        return typing.cast(None, jsii.invoke(self, "putCinder", [value]))

    @jsii.member(jsii_name="putCsi")
    def put_csi(
        self,
        *,
        driver: builtins.str,
        volume_handle: builtins.str,
        controller_expand_secret_ref: typing.Optional[typing.Union[PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRef, typing.Dict[str, typing.Any]]] = None,
        controller_publish_secret_ref: typing.Optional[typing.Union[PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRef, typing.Dict[str, typing.Any]]] = None,
        fs_type: typing.Optional[builtins.str] = None,
        node_publish_secret_ref: typing.Optional[typing.Union[PersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRef, typing.Dict[str, typing.Any]]] = None,
        node_stage_secret_ref: typing.Optional[typing.Union[PersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRef, typing.Dict[str, typing.Any]]] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        volume_attributes: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param driver: the name of the volume driver to use. More info: https://kubernetes.io/docs/concepts/storage/volumes/#csi. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#driver PersistentVolumeV1#driver}
        :param volume_handle: A string value that uniquely identifies the volume. More info: https://kubernetes.io/docs/concepts/storage/volumes/#csi. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#volume_handle PersistentVolumeV1#volume_handle}
        :param controller_expand_secret_ref: controller_expand_secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#controller_expand_secret_ref PersistentVolumeV1#controller_expand_secret_ref}
        :param controller_publish_secret_ref: controller_publish_secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#controller_publish_secret_ref PersistentVolumeV1#controller_publish_secret_ref}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fs_type PersistentVolumeV1#fs_type}
        :param node_publish_secret_ref: node_publish_secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#node_publish_secret_ref PersistentVolumeV1#node_publish_secret_ref}
        :param node_stage_secret_ref: node_stage_secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#node_stage_secret_ref PersistentVolumeV1#node_stage_secret_ref}
        :param read_only: Whether to set the read-only property in VolumeMounts to "true". If omitted, the default is "false". More info: http://kubernetes.io/docs/user-guide/volumes#csi. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        :param volume_attributes: Attributes of the volume to publish. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#volume_attributes PersistentVolumeV1#volume_attributes}
        '''
        value = PersistentVolumeV1SpecPersistentVolumeSourceCsi(
            driver=driver,
            volume_handle=volume_handle,
            controller_expand_secret_ref=controller_expand_secret_ref,
            controller_publish_secret_ref=controller_publish_secret_ref,
            fs_type=fs_type,
            node_publish_secret_ref=node_publish_secret_ref,
            node_stage_secret_ref=node_stage_secret_ref,
            read_only=read_only,
            volume_attributes=volume_attributes,
        )

        return typing.cast(None, jsii.invoke(self, "putCsi", [value]))

    @jsii.member(jsii_name="putFc")
    def put_fc(
        self,
        *,
        lun: jsii.Number,
        target_ww_ns: typing.Sequence[builtins.str],
        fs_type: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param lun: FC target lun number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#lun PersistentVolumeV1#lun}
        :param target_ww_ns: FC target worldwide names (WWNs). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#target_ww_ns PersistentVolumeV1#target_ww_ns}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fs_type PersistentVolumeV1#fs_type}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false (read/write). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        '''
        value = PersistentVolumeV1SpecPersistentVolumeSourceFc(
            lun=lun, target_ww_ns=target_ww_ns, fs_type=fs_type, read_only=read_only
        )

        return typing.cast(None, jsii.invoke(self, "putFc", [value]))

    @jsii.member(jsii_name="putFlexVolume")
    def put_flex_volume(
        self,
        *,
        driver: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        options: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        secret_ref: typing.Optional[typing.Union[PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRef, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param driver: Driver is the name of the driver to use for this volume. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#driver PersistentVolumeV1#driver}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". The default filesystem depends on FlexVolume script. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fs_type PersistentVolumeV1#fs_type}
        :param options: Extra command options if any. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#options PersistentVolumeV1#options}
        :param read_only: Whether to force the ReadOnly setting in VolumeMounts. Defaults to false (read/write). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        :param secret_ref: secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#secret_ref PersistentVolumeV1#secret_ref}
        '''
        value = PersistentVolumeV1SpecPersistentVolumeSourceFlexVolume(
            driver=driver,
            fs_type=fs_type,
            options=options,
            read_only=read_only,
            secret_ref=secret_ref,
        )

        return typing.cast(None, jsii.invoke(self, "putFlexVolume", [value]))

    @jsii.member(jsii_name="putFlocker")
    def put_flocker(
        self,
        *,
        dataset_name: typing.Optional[builtins.str] = None,
        dataset_uuid: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dataset_name: Name of the dataset stored as metadata -> name on the dataset for Flocker should be considered as deprecated. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#dataset_name PersistentVolumeV1#dataset_name}
        :param dataset_uuid: UUID of the dataset. This is unique identifier of a Flocker dataset. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#dataset_uuid PersistentVolumeV1#dataset_uuid}
        '''
        value = PersistentVolumeV1SpecPersistentVolumeSourceFlocker(
            dataset_name=dataset_name, dataset_uuid=dataset_uuid
        )

        return typing.cast(None, jsii.invoke(self, "putFlocker", [value]))

    @jsii.member(jsii_name="putGcePersistentDisk")
    def put_gce_persistent_disk(
        self,
        *,
        pd_name: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        partition: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param pd_name: Unique name of the PD resource in GCE. Used to identify the disk in GCE. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#pd_name PersistentVolumeV1#pd_name}
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fs_type PersistentVolumeV1#fs_type}
        :param partition: The partition in the volume that you want to mount. If omitted, the default is to mount by volume name. Examples: For volume /dev/sda1, you specify the partition as "1". Similarly, the volume partition for /dev/sda is "0" (or you can leave the property empty). More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#partition PersistentVolumeV1#partition}
        :param read_only: Whether to force the ReadOnly setting in VolumeMounts. Defaults to false. More info: http://kubernetes.io/docs/user-guide/volumes#gcepersistentdisk. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        '''
        value = PersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDisk(
            pd_name=pd_name, fs_type=fs_type, partition=partition, read_only=read_only
        )

        return typing.cast(None, jsii.invoke(self, "putGcePersistentDisk", [value]))

    @jsii.member(jsii_name="putGlusterfs")
    def put_glusterfs(
        self,
        *,
        endpoints_name: builtins.str,
        path: builtins.str,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param endpoints_name: The endpoint name that details Glusterfs topology. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#endpoints_name PersistentVolumeV1#endpoints_name}
        :param path: The Glusterfs volume path. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#path PersistentVolumeV1#path}
        :param read_only: Whether to force the Glusterfs volume to be mounted with read-only permissions. Defaults to false. More info: http://releases.k8s.io/HEAD/examples/volumes/glusterfs/README.md#create-a-pod. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        '''
        value = PersistentVolumeV1SpecPersistentVolumeSourceGlusterfs(
            endpoints_name=endpoints_name, path=path, read_only=read_only
        )

        return typing.cast(None, jsii.invoke(self, "putGlusterfs", [value]))

    @jsii.member(jsii_name="putHostPath")
    def put_host_path(
        self,
        *,
        path: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param path: Path of the directory on the host. More info: http://kubernetes.io/docs/user-guide/volumes#hostpath. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#path PersistentVolumeV1#path}
        :param type: Type for HostPath volume. Allowed values are "" (default), DirectoryOrCreate, Directory, FileOrCreate, File, Socket, CharDevice and BlockDevice. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#type PersistentVolumeV1#type}
        '''
        value = PersistentVolumeV1SpecPersistentVolumeSourceHostPath(
            path=path, type=type
        )

        return typing.cast(None, jsii.invoke(self, "putHostPath", [value]))

    @jsii.member(jsii_name="putIscsi")
    def put_iscsi(
        self,
        *,
        iqn: builtins.str,
        target_portal: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        iscsi_interface: typing.Optional[builtins.str] = None,
        lun: typing.Optional[jsii.Number] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param iqn: Target iSCSI Qualified Name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#iqn PersistentVolumeV1#iqn}
        :param target_portal: iSCSI target portal. The portal is either an IP or ip_addr:port if the port is other than default (typically TCP ports 860 and 3260). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#target_portal PersistentVolumeV1#target_portal}
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#iscsi Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fs_type PersistentVolumeV1#fs_type}
        :param iscsi_interface: iSCSI interface name that uses an iSCSI transport. Defaults to 'default' (tcp). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#iscsi_interface PersistentVolumeV1#iscsi_interface}
        :param lun: iSCSI target lun number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#lun PersistentVolumeV1#lun}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        '''
        value = PersistentVolumeV1SpecPersistentVolumeSourceIscsi(
            iqn=iqn,
            target_portal=target_portal,
            fs_type=fs_type,
            iscsi_interface=iscsi_interface,
            lun=lun,
            read_only=read_only,
        )

        return typing.cast(None, jsii.invoke(self, "putIscsi", [value]))

    @jsii.member(jsii_name="putLocal")
    def put_local(self, *, path: typing.Optional[builtins.str] = None) -> None:
        '''
        :param path: Path of the directory on the host. More info: http://kubernetes.io/docs/user-guide/volumes#local. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#path PersistentVolumeV1#path}
        '''
        value = PersistentVolumeV1SpecPersistentVolumeSourceLocal(path=path)

        return typing.cast(None, jsii.invoke(self, "putLocal", [value]))

    @jsii.member(jsii_name="putNfs")
    def put_nfs(
        self,
        *,
        path: builtins.str,
        server: builtins.str,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param path: Path that is exported by the NFS server. More info: http://kubernetes.io/docs/user-guide/volumes#nfs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#path PersistentVolumeV1#path}
        :param server: Server is the hostname or IP address of the NFS server. More info: http://kubernetes.io/docs/user-guide/volumes#nfs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#server PersistentVolumeV1#server}
        :param read_only: Whether to force the NFS export to be mounted with read-only permissions. Defaults to false. More info: http://kubernetes.io/docs/user-guide/volumes#nfs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        '''
        value = PersistentVolumeV1SpecPersistentVolumeSourceNfs(
            path=path, server=server, read_only=read_only
        )

        return typing.cast(None, jsii.invoke(self, "putNfs", [value]))

    @jsii.member(jsii_name="putPhotonPersistentDisk")
    def put_photon_persistent_disk(
        self,
        *,
        pd_id: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param pd_id: ID that identifies Photon Controller persistent disk. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#pd_id PersistentVolumeV1#pd_id}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fs_type PersistentVolumeV1#fs_type}
        '''
        value = PersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDisk(
            pd_id=pd_id, fs_type=fs_type
        )

        return typing.cast(None, jsii.invoke(self, "putPhotonPersistentDisk", [value]))

    @jsii.member(jsii_name="putQuobyte")
    def put_quobyte(
        self,
        *,
        registry: builtins.str,
        volume: builtins.str,
        group: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param registry: Registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#registry PersistentVolumeV1#registry}
        :param volume: Volume is a string that references an already created Quobyte volume by name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#volume PersistentVolumeV1#volume}
        :param group: Group to map volume access to Default is no group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#group PersistentVolumeV1#group}
        :param read_only: Whether to force the Quobyte volume to be mounted with read-only permissions. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        :param user: User to map volume access to Defaults to serivceaccount user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#user PersistentVolumeV1#user}
        '''
        value = PersistentVolumeV1SpecPersistentVolumeSourceQuobyte(
            registry=registry,
            volume=volume,
            group=group,
            read_only=read_only,
            user=user,
        )

        return typing.cast(None, jsii.invoke(self, "putQuobyte", [value]))

    @jsii.member(jsii_name="putRbd")
    def put_rbd(
        self,
        *,
        ceph_monitors: typing.Sequence[builtins.str],
        rbd_image: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        keyring: typing.Optional[builtins.str] = None,
        rados_user: typing.Optional[builtins.str] = None,
        rbd_pool: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        secret_ref: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRef", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param ceph_monitors: A collection of Ceph monitors. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#ceph_monitors PersistentVolumeV1#ceph_monitors}
        :param rbd_image: The rados image name. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#rbd_image PersistentVolumeV1#rbd_image}
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#rbd Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fs_type PersistentVolumeV1#fs_type}
        :param keyring: Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#keyring PersistentVolumeV1#keyring}
        :param rados_user: The rados user name. Default is admin. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#rados_user PersistentVolumeV1#rados_user}
        :param rbd_pool: The rados pool name. Default is rbd. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#rbd_pool PersistentVolumeV1#rbd_pool}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        :param secret_ref: secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#secret_ref PersistentVolumeV1#secret_ref}
        '''
        value = PersistentVolumeV1SpecPersistentVolumeSourceRbd(
            ceph_monitors=ceph_monitors,
            rbd_image=rbd_image,
            fs_type=fs_type,
            keyring=keyring,
            rados_user=rados_user,
            rbd_pool=rbd_pool,
            read_only=read_only,
            secret_ref=secret_ref,
        )

        return typing.cast(None, jsii.invoke(self, "putRbd", [value]))

    @jsii.member(jsii_name="putVsphereVolume")
    def put_vsphere_volume(
        self,
        *,
        volume_path: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param volume_path: Path that identifies vSphere volume vmdk. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#volume_path PersistentVolumeV1#volume_path}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fs_type PersistentVolumeV1#fs_type}
        '''
        value = PersistentVolumeV1SpecPersistentVolumeSourceVsphereVolume(
            volume_path=volume_path, fs_type=fs_type
        )

        return typing.cast(None, jsii.invoke(self, "putVsphereVolume", [value]))

    @jsii.member(jsii_name="resetAwsElasticBlockStore")
    def reset_aws_elastic_block_store(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAwsElasticBlockStore", []))

    @jsii.member(jsii_name="resetAzureDisk")
    def reset_azure_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureDisk", []))

    @jsii.member(jsii_name="resetAzureFile")
    def reset_azure_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureFile", []))

    @jsii.member(jsii_name="resetCephFs")
    def reset_ceph_fs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCephFs", []))

    @jsii.member(jsii_name="resetCinder")
    def reset_cinder(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCinder", []))

    @jsii.member(jsii_name="resetCsi")
    def reset_csi(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCsi", []))

    @jsii.member(jsii_name="resetFc")
    def reset_fc(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFc", []))

    @jsii.member(jsii_name="resetFlexVolume")
    def reset_flex_volume(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFlexVolume", []))

    @jsii.member(jsii_name="resetFlocker")
    def reset_flocker(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFlocker", []))

    @jsii.member(jsii_name="resetGcePersistentDisk")
    def reset_gce_persistent_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGcePersistentDisk", []))

    @jsii.member(jsii_name="resetGlusterfs")
    def reset_glusterfs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGlusterfs", []))

    @jsii.member(jsii_name="resetHostPath")
    def reset_host_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostPath", []))

    @jsii.member(jsii_name="resetIscsi")
    def reset_iscsi(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIscsi", []))

    @jsii.member(jsii_name="resetLocal")
    def reset_local(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocal", []))

    @jsii.member(jsii_name="resetNfs")
    def reset_nfs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNfs", []))

    @jsii.member(jsii_name="resetPhotonPersistentDisk")
    def reset_photon_persistent_disk(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPhotonPersistentDisk", []))

    @jsii.member(jsii_name="resetQuobyte")
    def reset_quobyte(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQuobyte", []))

    @jsii.member(jsii_name="resetRbd")
    def reset_rbd(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRbd", []))

    @jsii.member(jsii_name="resetVsphereVolume")
    def reset_vsphere_volume(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVsphereVolume", []))

    @builtins.property
    @jsii.member(jsii_name="awsElasticBlockStore")
    def aws_elastic_block_store(
        self,
    ) -> PersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStoreOutputReference:
        return typing.cast(PersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStoreOutputReference, jsii.get(self, "awsElasticBlockStore"))

    @builtins.property
    @jsii.member(jsii_name="azureDisk")
    def azure_disk(
        self,
    ) -> PersistentVolumeV1SpecPersistentVolumeSourceAzureDiskOutputReference:
        return typing.cast(PersistentVolumeV1SpecPersistentVolumeSourceAzureDiskOutputReference, jsii.get(self, "azureDisk"))

    @builtins.property
    @jsii.member(jsii_name="azureFile")
    def azure_file(
        self,
    ) -> PersistentVolumeV1SpecPersistentVolumeSourceAzureFileOutputReference:
        return typing.cast(PersistentVolumeV1SpecPersistentVolumeSourceAzureFileOutputReference, jsii.get(self, "azureFile"))

    @builtins.property
    @jsii.member(jsii_name="cephFs")
    def ceph_fs(
        self,
    ) -> PersistentVolumeV1SpecPersistentVolumeSourceCephFsOutputReference:
        return typing.cast(PersistentVolumeV1SpecPersistentVolumeSourceCephFsOutputReference, jsii.get(self, "cephFs"))

    @builtins.property
    @jsii.member(jsii_name="cinder")
    def cinder(
        self,
    ) -> PersistentVolumeV1SpecPersistentVolumeSourceCinderOutputReference:
        return typing.cast(PersistentVolumeV1SpecPersistentVolumeSourceCinderOutputReference, jsii.get(self, "cinder"))

    @builtins.property
    @jsii.member(jsii_name="csi")
    def csi(self) -> PersistentVolumeV1SpecPersistentVolumeSourceCsiOutputReference:
        return typing.cast(PersistentVolumeV1SpecPersistentVolumeSourceCsiOutputReference, jsii.get(self, "csi"))

    @builtins.property
    @jsii.member(jsii_name="fc")
    def fc(self) -> PersistentVolumeV1SpecPersistentVolumeSourceFcOutputReference:
        return typing.cast(PersistentVolumeV1SpecPersistentVolumeSourceFcOutputReference, jsii.get(self, "fc"))

    @builtins.property
    @jsii.member(jsii_name="flexVolume")
    def flex_volume(
        self,
    ) -> PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeOutputReference:
        return typing.cast(PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeOutputReference, jsii.get(self, "flexVolume"))

    @builtins.property
    @jsii.member(jsii_name="flocker")
    def flocker(
        self,
    ) -> PersistentVolumeV1SpecPersistentVolumeSourceFlockerOutputReference:
        return typing.cast(PersistentVolumeV1SpecPersistentVolumeSourceFlockerOutputReference, jsii.get(self, "flocker"))

    @builtins.property
    @jsii.member(jsii_name="gcePersistentDisk")
    def gce_persistent_disk(
        self,
    ) -> PersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDiskOutputReference:
        return typing.cast(PersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDiskOutputReference, jsii.get(self, "gcePersistentDisk"))

    @builtins.property
    @jsii.member(jsii_name="glusterfs")
    def glusterfs(
        self,
    ) -> PersistentVolumeV1SpecPersistentVolumeSourceGlusterfsOutputReference:
        return typing.cast(PersistentVolumeV1SpecPersistentVolumeSourceGlusterfsOutputReference, jsii.get(self, "glusterfs"))

    @builtins.property
    @jsii.member(jsii_name="hostPath")
    def host_path(
        self,
    ) -> PersistentVolumeV1SpecPersistentVolumeSourceHostPathOutputReference:
        return typing.cast(PersistentVolumeV1SpecPersistentVolumeSourceHostPathOutputReference, jsii.get(self, "hostPath"))

    @builtins.property
    @jsii.member(jsii_name="iscsi")
    def iscsi(self) -> PersistentVolumeV1SpecPersistentVolumeSourceIscsiOutputReference:
        return typing.cast(PersistentVolumeV1SpecPersistentVolumeSourceIscsiOutputReference, jsii.get(self, "iscsi"))

    @builtins.property
    @jsii.member(jsii_name="local")
    def local(self) -> PersistentVolumeV1SpecPersistentVolumeSourceLocalOutputReference:
        return typing.cast(PersistentVolumeV1SpecPersistentVolumeSourceLocalOutputReference, jsii.get(self, "local"))

    @builtins.property
    @jsii.member(jsii_name="nfs")
    def nfs(self) -> PersistentVolumeV1SpecPersistentVolumeSourceNfsOutputReference:
        return typing.cast(PersistentVolumeV1SpecPersistentVolumeSourceNfsOutputReference, jsii.get(self, "nfs"))

    @builtins.property
    @jsii.member(jsii_name="photonPersistentDisk")
    def photon_persistent_disk(
        self,
    ) -> "PersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDiskOutputReference":
        return typing.cast("PersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDiskOutputReference", jsii.get(self, "photonPersistentDisk"))

    @builtins.property
    @jsii.member(jsii_name="quobyte")
    def quobyte(
        self,
    ) -> "PersistentVolumeV1SpecPersistentVolumeSourceQuobyteOutputReference":
        return typing.cast("PersistentVolumeV1SpecPersistentVolumeSourceQuobyteOutputReference", jsii.get(self, "quobyte"))

    @builtins.property
    @jsii.member(jsii_name="rbd")
    def rbd(self) -> "PersistentVolumeV1SpecPersistentVolumeSourceRbdOutputReference":
        return typing.cast("PersistentVolumeV1SpecPersistentVolumeSourceRbdOutputReference", jsii.get(self, "rbd"))

    @builtins.property
    @jsii.member(jsii_name="vsphereVolume")
    def vsphere_volume(
        self,
    ) -> "PersistentVolumeV1SpecPersistentVolumeSourceVsphereVolumeOutputReference":
        return typing.cast("PersistentVolumeV1SpecPersistentVolumeSourceVsphereVolumeOutputReference", jsii.get(self, "vsphereVolume"))

    @builtins.property
    @jsii.member(jsii_name="awsElasticBlockStoreInput")
    def aws_elastic_block_store_input(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStore]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStore], jsii.get(self, "awsElasticBlockStoreInput"))

    @builtins.property
    @jsii.member(jsii_name="azureDiskInput")
    def azure_disk_input(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceAzureDisk]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceAzureDisk], jsii.get(self, "azureDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="azureFileInput")
    def azure_file_input(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceAzureFile]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceAzureFile], jsii.get(self, "azureFileInput"))

    @builtins.property
    @jsii.member(jsii_name="cephFsInput")
    def ceph_fs_input(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCephFs]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCephFs], jsii.get(self, "cephFsInput"))

    @builtins.property
    @jsii.member(jsii_name="cinderInput")
    def cinder_input(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCinder]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCinder], jsii.get(self, "cinderInput"))

    @builtins.property
    @jsii.member(jsii_name="csiInput")
    def csi_input(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCsi]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceCsi], jsii.get(self, "csiInput"))

    @builtins.property
    @jsii.member(jsii_name="fcInput")
    def fc_input(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceFc]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceFc], jsii.get(self, "fcInput"))

    @builtins.property
    @jsii.member(jsii_name="flexVolumeInput")
    def flex_volume_input(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceFlexVolume]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceFlexVolume], jsii.get(self, "flexVolumeInput"))

    @builtins.property
    @jsii.member(jsii_name="flockerInput")
    def flocker_input(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceFlocker]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceFlocker], jsii.get(self, "flockerInput"))

    @builtins.property
    @jsii.member(jsii_name="gcePersistentDiskInput")
    def gce_persistent_disk_input(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDisk]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDisk], jsii.get(self, "gcePersistentDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="glusterfsInput")
    def glusterfs_input(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceGlusterfs]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceGlusterfs], jsii.get(self, "glusterfsInput"))

    @builtins.property
    @jsii.member(jsii_name="hostPathInput")
    def host_path_input(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceHostPath]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceHostPath], jsii.get(self, "hostPathInput"))

    @builtins.property
    @jsii.member(jsii_name="iscsiInput")
    def iscsi_input(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceIscsi]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceIscsi], jsii.get(self, "iscsiInput"))

    @builtins.property
    @jsii.member(jsii_name="localInput")
    def local_input(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceLocal]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceLocal], jsii.get(self, "localInput"))

    @builtins.property
    @jsii.member(jsii_name="nfsInput")
    def nfs_input(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceNfs]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceNfs], jsii.get(self, "nfsInput"))

    @builtins.property
    @jsii.member(jsii_name="photonPersistentDiskInput")
    def photon_persistent_disk_input(
        self,
    ) -> typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDisk"]:
        return typing.cast(typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDisk"], jsii.get(self, "photonPersistentDiskInput"))

    @builtins.property
    @jsii.member(jsii_name="quobyteInput")
    def quobyte_input(
        self,
    ) -> typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceQuobyte"]:
        return typing.cast(typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceQuobyte"], jsii.get(self, "quobyteInput"))

    @builtins.property
    @jsii.member(jsii_name="rbdInput")
    def rbd_input(
        self,
    ) -> typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceRbd"]:
        return typing.cast(typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceRbd"], jsii.get(self, "rbdInput"))

    @builtins.property
    @jsii.member(jsii_name="vsphereVolumeInput")
    def vsphere_volume_input(
        self,
    ) -> typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceVsphereVolume"]:
        return typing.cast(typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceVsphereVolume"], jsii.get(self, "vsphereVolumeInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSource]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeV1SpecPersistentVolumeSource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDisk",
    jsii_struct_bases=[],
    name_mapping={"pd_id": "pdId", "fs_type": "fsType"},
)
class PersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDisk:
    def __init__(
        self,
        *,
        pd_id: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param pd_id: ID that identifies Photon Controller persistent disk. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#pd_id PersistentVolumeV1#pd_id}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fs_type PersistentVolumeV1#fs_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDisk.__init__)
            check_type(argname="argument pd_id", value=pd_id, expected_type=type_hints["pd_id"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "pd_id": pd_id,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type

    @builtins.property
    def pd_id(self) -> builtins.str:
        '''ID that identifies Photon Controller persistent disk.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#pd_id PersistentVolumeV1#pd_id}
        '''
        result = self._values.get("pd_id")
        assert result is not None, "Required property 'pd_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type to mount.

        Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fs_type PersistentVolumeV1#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDisk(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDiskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDiskOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDiskOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="pdIdInput")
    def pd_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pdIdInput"))

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDiskOutputReference, "fs_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="pdId")
    def pd_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pdId"))

    @pd_id.setter
    def pd_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDiskOutputReference, "pd_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pdId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDisk]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDisk], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDisk],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDiskOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceQuobyte",
    jsii_struct_bases=[],
    name_mapping={
        "registry": "registry",
        "volume": "volume",
        "group": "group",
        "read_only": "readOnly",
        "user": "user",
    },
)
class PersistentVolumeV1SpecPersistentVolumeSourceQuobyte:
    def __init__(
        self,
        *,
        registry: builtins.str,
        volume: builtins.str,
        group: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        user: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param registry: Registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#registry PersistentVolumeV1#registry}
        :param volume: Volume is a string that references an already created Quobyte volume by name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#volume PersistentVolumeV1#volume}
        :param group: Group to map volume access to Default is no group. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#group PersistentVolumeV1#group}
        :param read_only: Whether to force the Quobyte volume to be mounted with read-only permissions. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        :param user: User to map volume access to Defaults to serivceaccount user. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#user PersistentVolumeV1#user}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceQuobyte.__init__)
            check_type(argname="argument registry", value=registry, expected_type=type_hints["registry"])
            check_type(argname="argument volume", value=volume, expected_type=type_hints["volume"])
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
        self._values: typing.Dict[str, typing.Any] = {
            "registry": registry,
            "volume": volume,
        }
        if group is not None:
            self._values["group"] = group
        if read_only is not None:
            self._values["read_only"] = read_only
        if user is not None:
            self._values["user"] = user

    @builtins.property
    def registry(self) -> builtins.str:
        '''Registry represents a single or multiple Quobyte Registry services specified as a string as host:port pair (multiple entries are separated with commas) which acts as the central registry for volumes.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#registry PersistentVolumeV1#registry}
        '''
        result = self._values.get("registry")
        assert result is not None, "Required property 'registry' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def volume(self) -> builtins.str:
        '''Volume is a string that references an already created Quobyte volume by name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#volume PersistentVolumeV1#volume}
        '''
        result = self._values.get("volume")
        assert result is not None, "Required property 'volume' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def group(self) -> typing.Optional[builtins.str]:
        '''Group to map volume access to Default is no group.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#group PersistentVolumeV1#group}
        '''
        result = self._values.get("group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to force the Quobyte volume to be mounted with read-only permissions. Defaults to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def user(self) -> typing.Optional[builtins.str]:
        '''User to map volume access to Defaults to serivceaccount user.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#user PersistentVolumeV1#user}
        '''
        result = self._values.get("user")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1SpecPersistentVolumeSourceQuobyte(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeV1SpecPersistentVolumeSourceQuobyteOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceQuobyteOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceQuobyteOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetGroup")
    def reset_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGroup", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetUser")
    def reset_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUser", []))

    @builtins.property
    @jsii.member(jsii_name="groupInput")
    def group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "groupInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="registryInput")
    def registry_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "registryInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeInput")
    def volume_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumeInput"))

    @builtins.property
    @jsii.member(jsii_name="group")
    def group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "group"))

    @group.setter
    def group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceQuobyteOutputReference, "group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "group", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceQuobyteOutputReference, "read_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="registry")
    def registry(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registry"))

    @registry.setter
    def registry(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceQuobyteOutputReference, "registry").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registry", value)

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "user"))

    @user.setter
    def user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceQuobyteOutputReference, "user").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "user", value)

    @builtins.property
    @jsii.member(jsii_name="volume")
    def volume(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volume"))

    @volume.setter
    def volume(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceQuobyteOutputReference, "volume").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volume", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceQuobyte]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceQuobyte], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceQuobyte],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceQuobyteOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceRbd",
    jsii_struct_bases=[],
    name_mapping={
        "ceph_monitors": "cephMonitors",
        "rbd_image": "rbdImage",
        "fs_type": "fsType",
        "keyring": "keyring",
        "rados_user": "radosUser",
        "rbd_pool": "rbdPool",
        "read_only": "readOnly",
        "secret_ref": "secretRef",
    },
)
class PersistentVolumeV1SpecPersistentVolumeSourceRbd:
    def __init__(
        self,
        *,
        ceph_monitors: typing.Sequence[builtins.str],
        rbd_image: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
        keyring: typing.Optional[builtins.str] = None,
        rados_user: typing.Optional[builtins.str] = None,
        rbd_pool: typing.Optional[builtins.str] = None,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        secret_ref: typing.Optional[typing.Union["PersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRef", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param ceph_monitors: A collection of Ceph monitors. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#ceph_monitors PersistentVolumeV1#ceph_monitors}
        :param rbd_image: The rados image name. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#rbd_image PersistentVolumeV1#rbd_image}
        :param fs_type: Filesystem type of the volume that you want to mount. Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#rbd Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fs_type PersistentVolumeV1#fs_type}
        :param keyring: Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#keyring PersistentVolumeV1#keyring}
        :param rados_user: The rados user name. Default is admin. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#rados_user PersistentVolumeV1#rados_user}
        :param rbd_pool: The rados pool name. Default is rbd. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#rbd_pool PersistentVolumeV1#rbd_pool}
        :param read_only: Whether to force the read-only setting in VolumeMounts. Defaults to false. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        :param secret_ref: secret_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#secret_ref PersistentVolumeV1#secret_ref}
        '''
        if isinstance(secret_ref, dict):
            secret_ref = PersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRef(**secret_ref)
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceRbd.__init__)
            check_type(argname="argument ceph_monitors", value=ceph_monitors, expected_type=type_hints["ceph_monitors"])
            check_type(argname="argument rbd_image", value=rbd_image, expected_type=type_hints["rbd_image"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
            check_type(argname="argument keyring", value=keyring, expected_type=type_hints["keyring"])
            check_type(argname="argument rados_user", value=rados_user, expected_type=type_hints["rados_user"])
            check_type(argname="argument rbd_pool", value=rbd_pool, expected_type=type_hints["rbd_pool"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
            check_type(argname="argument secret_ref", value=secret_ref, expected_type=type_hints["secret_ref"])
        self._values: typing.Dict[str, typing.Any] = {
            "ceph_monitors": ceph_monitors,
            "rbd_image": rbd_image,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type
        if keyring is not None:
            self._values["keyring"] = keyring
        if rados_user is not None:
            self._values["rados_user"] = rados_user
        if rbd_pool is not None:
            self._values["rbd_pool"] = rbd_pool
        if read_only is not None:
            self._values["read_only"] = read_only
        if secret_ref is not None:
            self._values["secret_ref"] = secret_ref

    @builtins.property
    def ceph_monitors(self) -> typing.List[builtins.str]:
        '''A collection of Ceph monitors. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#ceph_monitors PersistentVolumeV1#ceph_monitors}
        '''
        result = self._values.get("ceph_monitors")
        assert result is not None, "Required property 'ceph_monitors' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def rbd_image(self) -> builtins.str:
        '''The rados image name. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#rbd_image PersistentVolumeV1#rbd_image}
        '''
        result = self._values.get("rbd_image")
        assert result is not None, "Required property 'rbd_image' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type of the volume that you want to mount.

        Tip: Ensure that the filesystem type is supported by the host operating system. Examples: "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. More info: http://kubernetes.io/docs/user-guide/volumes#rbd

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fs_type PersistentVolumeV1#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def keyring(self) -> typing.Optional[builtins.str]:
        '''Keyring is the path to key ring for RBDUser. Default is /etc/ceph/keyring. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#keyring PersistentVolumeV1#keyring}
        '''
        result = self._values.get("keyring")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rados_user(self) -> typing.Optional[builtins.str]:
        '''The rados user name. Default is admin. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#rados_user PersistentVolumeV1#rados_user}
        '''
        result = self._values.get("rados_user")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rbd_pool(self) -> typing.Optional[builtins.str]:
        '''The rados pool name. Default is rbd. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#rbd_pool PersistentVolumeV1#rbd_pool}
        '''
        result = self._values.get("rbd_pool")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to force the read-only setting in VolumeMounts. Defaults to false. More info: http://releases.k8s.io/HEAD/examples/volumes/rbd/README.md#how-to-use-it.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#read_only PersistentVolumeV1#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def secret_ref(
        self,
    ) -> typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRef"]:
        '''secret_ref block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#secret_ref PersistentVolumeV1#secret_ref}
        '''
        result = self._values.get("secret_ref")
        return typing.cast(typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRef"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1SpecPersistentVolumeSourceRbd(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeV1SpecPersistentVolumeSourceRbdOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceRbdOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceRbdOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSecretRef")
    def put_secret_ref(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#name PersistentVolumeV1#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#namespace PersistentVolumeV1#namespace}
        '''
        value = PersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRef(
            name=name, namespace=namespace
        )

        return typing.cast(None, jsii.invoke(self, "putSecretRef", [value]))

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @jsii.member(jsii_name="resetKeyring")
    def reset_keyring(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyring", []))

    @jsii.member(jsii_name="resetRadosUser")
    def reset_rados_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRadosUser", []))

    @jsii.member(jsii_name="resetRbdPool")
    def reset_rbd_pool(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRbdPool", []))

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @jsii.member(jsii_name="resetSecretRef")
    def reset_secret_ref(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretRef", []))

    @builtins.property
    @jsii.member(jsii_name="secretRef")
    def secret_ref(
        self,
    ) -> "PersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRefOutputReference":
        return typing.cast("PersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRefOutputReference", jsii.get(self, "secretRef"))

    @builtins.property
    @jsii.member(jsii_name="cephMonitorsInput")
    def ceph_monitors_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cephMonitorsInput"))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="keyringInput")
    def keyring_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyringInput"))

    @builtins.property
    @jsii.member(jsii_name="radosUserInput")
    def rados_user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "radosUserInput"))

    @builtins.property
    @jsii.member(jsii_name="rbdImageInput")
    def rbd_image_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rbdImageInput"))

    @builtins.property
    @jsii.member(jsii_name="rbdPoolInput")
    def rbd_pool_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rbdPoolInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="secretRefInput")
    def secret_ref_input(
        self,
    ) -> typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRef"]:
        return typing.cast(typing.Optional["PersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRef"], jsii.get(self, "secretRefInput"))

    @builtins.property
    @jsii.member(jsii_name="cephMonitors")
    def ceph_monitors(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "cephMonitors"))

    @ceph_monitors.setter
    def ceph_monitors(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceRbdOutputReference, "ceph_monitors").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cephMonitors", value)

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceRbdOutputReference, "fs_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="keyring")
    def keyring(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyring"))

    @keyring.setter
    def keyring(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceRbdOutputReference, "keyring").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyring", value)

    @builtins.property
    @jsii.member(jsii_name="radosUser")
    def rados_user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "radosUser"))

    @rados_user.setter
    def rados_user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceRbdOutputReference, "rados_user").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "radosUser", value)

    @builtins.property
    @jsii.member(jsii_name="rbdImage")
    def rbd_image(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rbdImage"))

    @rbd_image.setter
    def rbd_image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceRbdOutputReference, "rbd_image").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rbdImage", value)

    @builtins.property
    @jsii.member(jsii_name="rbdPool")
    def rbd_pool(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rbdPool"))

    @rbd_pool.setter
    def rbd_pool(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceRbdOutputReference, "rbd_pool").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rbdPool", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceRbdOutputReference, "read_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceRbd]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceRbd], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceRbd],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceRbdOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRef",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace": "namespace"},
)
class PersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRef:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#name PersistentVolumeV1#name}
        :param namespace: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#namespace PersistentVolumeV1#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRef.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#name PersistentVolumeV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#namespace PersistentVolumeV1#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRefOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRefOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRefOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRefOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRefOutputReference, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRef]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRefOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceVsphereVolume",
    jsii_struct_bases=[],
    name_mapping={"volume_path": "volumePath", "fs_type": "fsType"},
)
class PersistentVolumeV1SpecPersistentVolumeSourceVsphereVolume:
    def __init__(
        self,
        *,
        volume_path: builtins.str,
        fs_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param volume_path: Path that identifies vSphere volume vmdk. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#volume_path PersistentVolumeV1#volume_path}
        :param fs_type: Filesystem type to mount. Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fs_type PersistentVolumeV1#fs_type}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceVsphereVolume.__init__)
            check_type(argname="argument volume_path", value=volume_path, expected_type=type_hints["volume_path"])
            check_type(argname="argument fs_type", value=fs_type, expected_type=type_hints["fs_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "volume_path": volume_path,
        }
        if fs_type is not None:
            self._values["fs_type"] = fs_type

    @builtins.property
    def volume_path(self) -> builtins.str:
        '''Path that identifies vSphere volume vmdk.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#volume_path PersistentVolumeV1#volume_path}
        '''
        result = self._values.get("volume_path")
        assert result is not None, "Required property 'volume_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def fs_type(self) -> typing.Optional[builtins.str]:
        '''Filesystem type to mount.

        Must be a filesystem type supported by the host operating system. Ex. "ext4", "xfs", "ntfs". Implicitly inferred to be "ext4" if unspecified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#fs_type PersistentVolumeV1#fs_type}
        '''
        result = self._values.get("fs_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1SpecPersistentVolumeSourceVsphereVolume(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeV1SpecPersistentVolumeSourceVsphereVolumeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1SpecPersistentVolumeSourceVsphereVolumeOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1SpecPersistentVolumeSourceVsphereVolumeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFsType")
    def reset_fs_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFsType", []))

    @builtins.property
    @jsii.member(jsii_name="fsTypeInput")
    def fs_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fsTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="volumePathInput")
    def volume_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "volumePathInput"))

    @builtins.property
    @jsii.member(jsii_name="fsType")
    def fs_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fsType"))

    @fs_type.setter
    def fs_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceVsphereVolumeOutputReference, "fs_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fsType", value)

    @builtins.property
    @jsii.member(jsii_name="volumePath")
    def volume_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "volumePath"))

    @volume_path.setter
    def volume_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceVsphereVolumeOutputReference, "volume_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumePath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceVsphereVolume]:
        return typing.cast(typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceVsphereVolume], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PersistentVolumeV1SpecPersistentVolumeSourceVsphereVolume],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1SpecPersistentVolumeSourceVsphereVolumeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1Timeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create"},
)
class PersistentVolumeV1Timeouts:
    def __init__(self, *, create: typing.Optional[builtins.str] = None) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#create PersistentVolumeV1#create}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PersistentVolumeV1Timeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/persistent_volume_v1#create PersistentVolumeV1#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PersistentVolumeV1Timeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PersistentVolumeV1TimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.persistentVolumeV1.PersistentVolumeV1TimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(PersistentVolumeV1TimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1TimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PersistentVolumeV1Timeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PersistentVolumeV1Timeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PersistentVolumeV1Timeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PersistentVolumeV1TimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "PersistentVolumeV1",
    "PersistentVolumeV1Config",
    "PersistentVolumeV1Metadata",
    "PersistentVolumeV1MetadataOutputReference",
    "PersistentVolumeV1Spec",
    "PersistentVolumeV1SpecClaimRef",
    "PersistentVolumeV1SpecClaimRefOutputReference",
    "PersistentVolumeV1SpecList",
    "PersistentVolumeV1SpecNodeAffinity",
    "PersistentVolumeV1SpecNodeAffinityOutputReference",
    "PersistentVolumeV1SpecNodeAffinityRequired",
    "PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTerm",
    "PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermList",
    "PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressions",
    "PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsList",
    "PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchExpressionsOutputReference",
    "PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFields",
    "PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFieldsList",
    "PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermMatchFieldsOutputReference",
    "PersistentVolumeV1SpecNodeAffinityRequiredNodeSelectorTermOutputReference",
    "PersistentVolumeV1SpecNodeAffinityRequiredOutputReference",
    "PersistentVolumeV1SpecOutputReference",
    "PersistentVolumeV1SpecPersistentVolumeSource",
    "PersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStore",
    "PersistentVolumeV1SpecPersistentVolumeSourceAwsElasticBlockStoreOutputReference",
    "PersistentVolumeV1SpecPersistentVolumeSourceAzureDisk",
    "PersistentVolumeV1SpecPersistentVolumeSourceAzureDiskOutputReference",
    "PersistentVolumeV1SpecPersistentVolumeSourceAzureFile",
    "PersistentVolumeV1SpecPersistentVolumeSourceAzureFileOutputReference",
    "PersistentVolumeV1SpecPersistentVolumeSourceCephFs",
    "PersistentVolumeV1SpecPersistentVolumeSourceCephFsOutputReference",
    "PersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRef",
    "PersistentVolumeV1SpecPersistentVolumeSourceCephFsSecretRefOutputReference",
    "PersistentVolumeV1SpecPersistentVolumeSourceCinder",
    "PersistentVolumeV1SpecPersistentVolumeSourceCinderOutputReference",
    "PersistentVolumeV1SpecPersistentVolumeSourceCsi",
    "PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRef",
    "PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerExpandSecretRefOutputReference",
    "PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRef",
    "PersistentVolumeV1SpecPersistentVolumeSourceCsiControllerPublishSecretRefOutputReference",
    "PersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRef",
    "PersistentVolumeV1SpecPersistentVolumeSourceCsiNodePublishSecretRefOutputReference",
    "PersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRef",
    "PersistentVolumeV1SpecPersistentVolumeSourceCsiNodeStageSecretRefOutputReference",
    "PersistentVolumeV1SpecPersistentVolumeSourceCsiOutputReference",
    "PersistentVolumeV1SpecPersistentVolumeSourceFc",
    "PersistentVolumeV1SpecPersistentVolumeSourceFcOutputReference",
    "PersistentVolumeV1SpecPersistentVolumeSourceFlexVolume",
    "PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeOutputReference",
    "PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRef",
    "PersistentVolumeV1SpecPersistentVolumeSourceFlexVolumeSecretRefOutputReference",
    "PersistentVolumeV1SpecPersistentVolumeSourceFlocker",
    "PersistentVolumeV1SpecPersistentVolumeSourceFlockerOutputReference",
    "PersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDisk",
    "PersistentVolumeV1SpecPersistentVolumeSourceGcePersistentDiskOutputReference",
    "PersistentVolumeV1SpecPersistentVolumeSourceGlusterfs",
    "PersistentVolumeV1SpecPersistentVolumeSourceGlusterfsOutputReference",
    "PersistentVolumeV1SpecPersistentVolumeSourceHostPath",
    "PersistentVolumeV1SpecPersistentVolumeSourceHostPathOutputReference",
    "PersistentVolumeV1SpecPersistentVolumeSourceIscsi",
    "PersistentVolumeV1SpecPersistentVolumeSourceIscsiOutputReference",
    "PersistentVolumeV1SpecPersistentVolumeSourceLocal",
    "PersistentVolumeV1SpecPersistentVolumeSourceLocalOutputReference",
    "PersistentVolumeV1SpecPersistentVolumeSourceNfs",
    "PersistentVolumeV1SpecPersistentVolumeSourceNfsOutputReference",
    "PersistentVolumeV1SpecPersistentVolumeSourceOutputReference",
    "PersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDisk",
    "PersistentVolumeV1SpecPersistentVolumeSourcePhotonPersistentDiskOutputReference",
    "PersistentVolumeV1SpecPersistentVolumeSourceQuobyte",
    "PersistentVolumeV1SpecPersistentVolumeSourceQuobyteOutputReference",
    "PersistentVolumeV1SpecPersistentVolumeSourceRbd",
    "PersistentVolumeV1SpecPersistentVolumeSourceRbdOutputReference",
    "PersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRef",
    "PersistentVolumeV1SpecPersistentVolumeSourceRbdSecretRefOutputReference",
    "PersistentVolumeV1SpecPersistentVolumeSourceVsphereVolume",
    "PersistentVolumeV1SpecPersistentVolumeSourceVsphereVolumeOutputReference",
    "PersistentVolumeV1Timeouts",
    "PersistentVolumeV1TimeoutsOutputReference",
]

publication.publish()
