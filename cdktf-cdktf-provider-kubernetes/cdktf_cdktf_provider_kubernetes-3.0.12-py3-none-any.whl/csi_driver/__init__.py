'''
# `kubernetes_csi_driver`

Refer to the Terraform Registory for docs: [`kubernetes_csi_driver`](https://www.terraform.io/docs/providers/kubernetes/r/csi_driver).
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


class CsiDriver(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.csiDriver.CsiDriver",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/kubernetes/r/csi_driver kubernetes_csi_driver}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        metadata: typing.Union["CsiDriverMetadata", typing.Dict[str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        spec: typing.Optional[typing.Union["CsiDriverSpec", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/kubernetes/r/csi_driver kubernetes_csi_driver} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/csi_driver#metadata CsiDriver#metadata}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/csi_driver#id CsiDriver#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/csi_driver#spec CsiDriver#spec}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CsiDriver.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CsiDriverConfig(
            metadata=metadata,
            id=id,
            spec=spec,
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
        generate_name: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the csi driver that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/csi_driver#annotations CsiDriver#annotations}
        :param generate_name: Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided. This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/csi_driver#generate_name CsiDriver#generate_name}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the csi driver. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/csi_driver#labels CsiDriver#labels}
        :param name: Name of the csi driver, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/csi_driver#name CsiDriver#name}
        '''
        value = CsiDriverMetadata(
            annotations=annotations,
            generate_name=generate_name,
            labels=labels,
            name=name,
        )

        return typing.cast(None, jsii.invoke(self, "putMetadata", [value]))

    @jsii.member(jsii_name="putSpec")
    def put_spec(
        self,
        *,
        attach_required: typing.Union[builtins.bool, cdktf.IResolvable],
        pod_info_on_mount: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        volume_lifecycle_modes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param attach_required: Indicates if the CSI volume driver requires an attach operation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/csi_driver#attach_required CsiDriver#attach_required}
        :param pod_info_on_mount: Indicates that the CSI volume driver requires additional pod information (like podName, podUID, etc.) during mount operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/csi_driver#pod_info_on_mount CsiDriver#pod_info_on_mount}
        :param volume_lifecycle_modes: Defines what kind of volumes this CSI volume driver supports. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/csi_driver#volume_lifecycle_modes CsiDriver#volume_lifecycle_modes}
        '''
        value = CsiDriverSpec(
            attach_required=attach_required,
            pod_info_on_mount=pod_info_on_mount,
            volume_lifecycle_modes=volume_lifecycle_modes,
        )

        return typing.cast(None, jsii.invoke(self, "putSpec", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSpec")
    def reset_spec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpec", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> "CsiDriverMetadataOutputReference":
        return typing.cast("CsiDriverMetadataOutputReference", jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="spec")
    def spec(self) -> "CsiDriverSpecOutputReference":
        return typing.cast("CsiDriverSpecOutputReference", jsii.get(self, "spec"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(self) -> typing.Optional["CsiDriverMetadata"]:
        return typing.cast(typing.Optional["CsiDriverMetadata"], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="specInput")
    def spec_input(self) -> typing.Optional["CsiDriverSpec"]:
        return typing.cast(typing.Optional["CsiDriverSpec"], jsii.get(self, "specInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CsiDriver, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.csiDriver.CsiDriverConfig",
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
        "id": "id",
        "spec": "spec",
    },
)
class CsiDriverConfig(cdktf.TerraformMetaArguments):
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
        metadata: typing.Union["CsiDriverMetadata", typing.Dict[str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        spec: typing.Optional[typing.Union["CsiDriverSpec", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/csi_driver#metadata CsiDriver#metadata}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/csi_driver#id CsiDriver#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/csi_driver#spec CsiDriver#spec}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(metadata, dict):
            metadata = CsiDriverMetadata(**metadata)
        if isinstance(spec, dict):
            spec = CsiDriverSpec(**spec)
        if __debug__:
            type_hints = typing.get_type_hints(CsiDriverConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument spec", value=spec, expected_type=type_hints["spec"])
        self._values: typing.Dict[str, typing.Any] = {
            "metadata": metadata,
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
        if spec is not None:
            self._values["spec"] = spec

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
    def metadata(self) -> "CsiDriverMetadata":
        '''metadata block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/csi_driver#metadata CsiDriver#metadata}
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast("CsiDriverMetadata", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/csi_driver#id CsiDriver#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spec(self) -> typing.Optional["CsiDriverSpec"]:
        '''spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/csi_driver#spec CsiDriver#spec}
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional["CsiDriverSpec"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CsiDriverConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.csiDriver.CsiDriverMetadata",
    jsii_struct_bases=[],
    name_mapping={
        "annotations": "annotations",
        "generate_name": "generateName",
        "labels": "labels",
        "name": "name",
    },
)
class CsiDriverMetadata:
    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        generate_name: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the csi driver that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/csi_driver#annotations CsiDriver#annotations}
        :param generate_name: Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided. This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/csi_driver#generate_name CsiDriver#generate_name}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the csi driver. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/csi_driver#labels CsiDriver#labels}
        :param name: Name of the csi driver, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/csi_driver#name CsiDriver#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CsiDriverMetadata.__init__)
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument generate_name", value=generate_name, expected_type=type_hints["generate_name"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if annotations is not None:
            self._values["annotations"] = annotations
        if generate_name is not None:
            self._values["generate_name"] = generate_name
        if labels is not None:
            self._values["labels"] = labels
        if name is not None:
            self._values["name"] = name

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''An unstructured key value map stored with the csi driver that may be used to store arbitrary metadata.

        More info: http://kubernetes.io/docs/user-guide/annotations

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/csi_driver#annotations CsiDriver#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def generate_name(self) -> typing.Optional[builtins.str]:
        '''Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided.

        This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/csi_driver#generate_name CsiDriver#generate_name}
        '''
        result = self._values.get("generate_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of string keys and values that can be used to organize and categorize (scope and select) the csi driver.

        May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/csi_driver#labels CsiDriver#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the csi driver, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/csi_driver#name CsiDriver#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CsiDriverMetadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CsiDriverMetadataOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.csiDriver.CsiDriverMetadataOutputReference",
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
            type_hints = typing.get_type_hints(CsiDriverMetadataOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAnnotations")
    def reset_annotations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnnotations", []))

    @jsii.member(jsii_name="resetGenerateName")
    def reset_generate_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGenerateName", []))

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
    @jsii.member(jsii_name="generateNameInput")
    def generate_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "generateNameInput"))

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
            type_hints = typing.get_type_hints(getattr(CsiDriverMetadataOutputReference, "annotations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="generateName")
    def generate_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "generateName"))

    @generate_name.setter
    def generate_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CsiDriverMetadataOutputReference, "generate_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "generateName", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CsiDriverMetadataOutputReference, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CsiDriverMetadataOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CsiDriverMetadata]:
        return typing.cast(typing.Optional[CsiDriverMetadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CsiDriverMetadata]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CsiDriverMetadataOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.csiDriver.CsiDriverSpec",
    jsii_struct_bases=[],
    name_mapping={
        "attach_required": "attachRequired",
        "pod_info_on_mount": "podInfoOnMount",
        "volume_lifecycle_modes": "volumeLifecycleModes",
    },
)
class CsiDriverSpec:
    def __init__(
        self,
        *,
        attach_required: typing.Union[builtins.bool, cdktf.IResolvable],
        pod_info_on_mount: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        volume_lifecycle_modes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param attach_required: Indicates if the CSI volume driver requires an attach operation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/csi_driver#attach_required CsiDriver#attach_required}
        :param pod_info_on_mount: Indicates that the CSI volume driver requires additional pod information (like podName, podUID, etc.) during mount operations. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/csi_driver#pod_info_on_mount CsiDriver#pod_info_on_mount}
        :param volume_lifecycle_modes: Defines what kind of volumes this CSI volume driver supports. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/csi_driver#volume_lifecycle_modes CsiDriver#volume_lifecycle_modes}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CsiDriverSpec.__init__)
            check_type(argname="argument attach_required", value=attach_required, expected_type=type_hints["attach_required"])
            check_type(argname="argument pod_info_on_mount", value=pod_info_on_mount, expected_type=type_hints["pod_info_on_mount"])
            check_type(argname="argument volume_lifecycle_modes", value=volume_lifecycle_modes, expected_type=type_hints["volume_lifecycle_modes"])
        self._values: typing.Dict[str, typing.Any] = {
            "attach_required": attach_required,
        }
        if pod_info_on_mount is not None:
            self._values["pod_info_on_mount"] = pod_info_on_mount
        if volume_lifecycle_modes is not None:
            self._values["volume_lifecycle_modes"] = volume_lifecycle_modes

    @builtins.property
    def attach_required(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Indicates if the CSI volume driver requires an attach operation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/csi_driver#attach_required CsiDriver#attach_required}
        '''
        result = self._values.get("attach_required")
        assert result is not None, "Required property 'attach_required' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def pod_info_on_mount(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates that the CSI volume driver requires additional pod information (like podName, podUID, etc.) during mount operations.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/csi_driver#pod_info_on_mount CsiDriver#pod_info_on_mount}
        '''
        result = self._values.get("pod_info_on_mount")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def volume_lifecycle_modes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Defines what kind of volumes this CSI volume driver supports.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/csi_driver#volume_lifecycle_modes CsiDriver#volume_lifecycle_modes}
        '''
        result = self._values.get("volume_lifecycle_modes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CsiDriverSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CsiDriverSpecOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.csiDriver.CsiDriverSpecOutputReference",
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
            type_hints = typing.get_type_hints(CsiDriverSpecOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetPodInfoOnMount")
    def reset_pod_info_on_mount(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPodInfoOnMount", []))

    @jsii.member(jsii_name="resetVolumeLifecycleModes")
    def reset_volume_lifecycle_modes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumeLifecycleModes", []))

    @builtins.property
    @jsii.member(jsii_name="attachRequiredInput")
    def attach_required_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "attachRequiredInput"))

    @builtins.property
    @jsii.member(jsii_name="podInfoOnMountInput")
    def pod_info_on_mount_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "podInfoOnMountInput"))

    @builtins.property
    @jsii.member(jsii_name="volumeLifecycleModesInput")
    def volume_lifecycle_modes_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "volumeLifecycleModesInput"))

    @builtins.property
    @jsii.member(jsii_name="attachRequired")
    def attach_required(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "attachRequired"))

    @attach_required.setter
    def attach_required(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CsiDriverSpecOutputReference, "attach_required").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "attachRequired", value)

    @builtins.property
    @jsii.member(jsii_name="podInfoOnMount")
    def pod_info_on_mount(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "podInfoOnMount"))

    @pod_info_on_mount.setter
    def pod_info_on_mount(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CsiDriverSpecOutputReference, "pod_info_on_mount").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "podInfoOnMount", value)

    @builtins.property
    @jsii.member(jsii_name="volumeLifecycleModes")
    def volume_lifecycle_modes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "volumeLifecycleModes"))

    @volume_lifecycle_modes.setter
    def volume_lifecycle_modes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CsiDriverSpecOutputReference, "volume_lifecycle_modes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumeLifecycleModes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CsiDriverSpec]:
        return typing.cast(typing.Optional[CsiDriverSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CsiDriverSpec]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CsiDriverSpecOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CsiDriver",
    "CsiDriverConfig",
    "CsiDriverMetadata",
    "CsiDriverMetadataOutputReference",
    "CsiDriverSpec",
    "CsiDriverSpecOutputReference",
]

publication.publish()
