'''
# `kubernetes_horizontal_pod_autoscaler_v2beta2`

Refer to the Terraform Registory for docs: [`kubernetes_horizontal_pod_autoscaler_v2beta2`](https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2).
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


class HorizontalPodAutoscalerV2Beta2(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2 kubernetes_horizontal_pod_autoscaler_v2beta2}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        metadata: typing.Union["HorizontalPodAutoscalerV2Beta2Metadata", typing.Dict[str, typing.Any]],
        spec: typing.Union["HorizontalPodAutoscalerV2Beta2Spec", typing.Dict[str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2 kubernetes_horizontal_pod_autoscaler_v2beta2} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#metadata HorizontalPodAutoscalerV2Beta2#metadata}
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#spec HorizontalPodAutoscalerV2Beta2#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#id HorizontalPodAutoscalerV2Beta2#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = HorizontalPodAutoscalerV2Beta2Config(
            metadata=metadata,
            spec=spec,
            id=id,
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
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the horizontal pod autoscaler that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#annotations HorizontalPodAutoscalerV2Beta2#annotations}
        :param generate_name: Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided. This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#generate_name HorizontalPodAutoscalerV2Beta2#generate_name}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the horizontal pod autoscaler. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#labels HorizontalPodAutoscalerV2Beta2#labels}
        :param name: Name of the horizontal pod autoscaler, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#name HorizontalPodAutoscalerV2Beta2#name}
        :param namespace: Namespace defines the space within which name of the horizontal pod autoscaler must be unique. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#namespace HorizontalPodAutoscalerV2Beta2#namespace}
        '''
        value = HorizontalPodAutoscalerV2Beta2Metadata(
            annotations=annotations,
            generate_name=generate_name,
            labels=labels,
            name=name,
            namespace=namespace,
        )

        return typing.cast(None, jsii.invoke(self, "putMetadata", [value]))

    @jsii.member(jsii_name="putSpec")
    def put_spec(
        self,
        *,
        max_replicas: jsii.Number,
        scale_target_ref: typing.Union["HorizontalPodAutoscalerV2Beta2SpecScaleTargetRef", typing.Dict[str, typing.Any]],
        behavior: typing.Optional[typing.Union["HorizontalPodAutoscalerV2Beta2SpecBehavior", typing.Dict[str, typing.Any]]] = None,
        metric: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerV2Beta2SpecMetric", typing.Dict[str, typing.Any]]]]] = None,
        min_replicas: typing.Optional[jsii.Number] = None,
        target_cpu_utilization_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_replicas: Upper limit for the number of pods that can be set by the autoscaler. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#max_replicas HorizontalPodAutoscalerV2Beta2#max_replicas}
        :param scale_target_ref: scale_target_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#scale_target_ref HorizontalPodAutoscalerV2Beta2#scale_target_ref}
        :param behavior: behavior block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#behavior HorizontalPodAutoscalerV2Beta2#behavior}
        :param metric: metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#metric HorizontalPodAutoscalerV2Beta2#metric}
        :param min_replicas: Lower limit for the number of pods that can be set by the autoscaler, defaults to ``1``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#min_replicas HorizontalPodAutoscalerV2Beta2#min_replicas}
        :param target_cpu_utilization_percentage: Target average CPU utilization (represented as a percentage of requested CPU) over all the pods. If not specified the default autoscaling policy will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#target_cpu_utilization_percentage HorizontalPodAutoscalerV2Beta2#target_cpu_utilization_percentage}
        '''
        value = HorizontalPodAutoscalerV2Beta2Spec(
            max_replicas=max_replicas,
            scale_target_ref=scale_target_ref,
            behavior=behavior,
            metric=metric,
            min_replicas=min_replicas,
            target_cpu_utilization_percentage=target_cpu_utilization_percentage,
        )

        return typing.cast(None, jsii.invoke(self, "putSpec", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> "HorizontalPodAutoscalerV2Beta2MetadataOutputReference":
        return typing.cast("HorizontalPodAutoscalerV2Beta2MetadataOutputReference", jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="spec")
    def spec(self) -> "HorizontalPodAutoscalerV2Beta2SpecOutputReference":
        return typing.cast("HorizontalPodAutoscalerV2Beta2SpecOutputReference", jsii.get(self, "spec"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(
        self,
    ) -> typing.Optional["HorizontalPodAutoscalerV2Beta2Metadata"]:
        return typing.cast(typing.Optional["HorizontalPodAutoscalerV2Beta2Metadata"], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="specInput")
    def spec_input(self) -> typing.Optional["HorizontalPodAutoscalerV2Beta2Spec"]:
        return typing.cast(typing.Optional["HorizontalPodAutoscalerV2Beta2Spec"], jsii.get(self, "specInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2Config",
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
    },
)
class HorizontalPodAutoscalerV2Beta2Config(cdktf.TerraformMetaArguments):
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
        metadata: typing.Union["HorizontalPodAutoscalerV2Beta2Metadata", typing.Dict[str, typing.Any]],
        spec: typing.Union["HorizontalPodAutoscalerV2Beta2Spec", typing.Dict[str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#metadata HorizontalPodAutoscalerV2Beta2#metadata}
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#spec HorizontalPodAutoscalerV2Beta2#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#id HorizontalPodAutoscalerV2Beta2#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(metadata, dict):
            metadata = HorizontalPodAutoscalerV2Beta2Metadata(**metadata)
        if isinstance(spec, dict):
            spec = HorizontalPodAutoscalerV2Beta2Spec(**spec)
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2Config.__init__)
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
    def metadata(self) -> "HorizontalPodAutoscalerV2Beta2Metadata":
        '''metadata block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#metadata HorizontalPodAutoscalerV2Beta2#metadata}
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast("HorizontalPodAutoscalerV2Beta2Metadata", result)

    @builtins.property
    def spec(self) -> "HorizontalPodAutoscalerV2Beta2Spec":
        '''spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#spec HorizontalPodAutoscalerV2Beta2#spec}
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast("HorizontalPodAutoscalerV2Beta2Spec", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#id HorizontalPodAutoscalerV2Beta2#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerV2Beta2Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2Metadata",
    jsii_struct_bases=[],
    name_mapping={
        "annotations": "annotations",
        "generate_name": "generateName",
        "labels": "labels",
        "name": "name",
        "namespace": "namespace",
    },
)
class HorizontalPodAutoscalerV2Beta2Metadata:
    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        generate_name: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the horizontal pod autoscaler that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#annotations HorizontalPodAutoscalerV2Beta2#annotations}
        :param generate_name: Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided. This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#generate_name HorizontalPodAutoscalerV2Beta2#generate_name}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the horizontal pod autoscaler. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#labels HorizontalPodAutoscalerV2Beta2#labels}
        :param name: Name of the horizontal pod autoscaler, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#name HorizontalPodAutoscalerV2Beta2#name}
        :param namespace: Namespace defines the space within which name of the horizontal pod autoscaler must be unique. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#namespace HorizontalPodAutoscalerV2Beta2#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2Metadata.__init__)
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument generate_name", value=generate_name, expected_type=type_hints["generate_name"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[str, typing.Any] = {}
        if annotations is not None:
            self._values["annotations"] = annotations
        if generate_name is not None:
            self._values["generate_name"] = generate_name
        if labels is not None:
            self._values["labels"] = labels
        if name is not None:
            self._values["name"] = name
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def annotations(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''An unstructured key value map stored with the horizontal pod autoscaler that may be used to store arbitrary metadata.

        More info: http://kubernetes.io/docs/user-guide/annotations

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#annotations HorizontalPodAutoscalerV2Beta2#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def generate_name(self) -> typing.Optional[builtins.str]:
        '''Prefix, used by the server, to generate a unique name ONLY IF the ``name`` field has not been provided.

        This value will also be combined with a unique suffix. Read more: https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#idempotency

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#generate_name HorizontalPodAutoscalerV2Beta2#generate_name}
        '''
        result = self._values.get("generate_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of string keys and values that can be used to organize and categorize (scope and select) the horizontal pod autoscaler.

        May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#labels HorizontalPodAutoscalerV2Beta2#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the horizontal pod autoscaler, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#name HorizontalPodAutoscalerV2Beta2#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace defines the space within which name of the horizontal pod autoscaler must be unique.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#namespace HorizontalPodAutoscalerV2Beta2#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerV2Beta2Metadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerV2Beta2MetadataOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2MetadataOutputReference",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2MetadataOutputReference.__init__)
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

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

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
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="annotations")
    def annotations(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "annotations"))

    @annotations.setter
    def annotations(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2MetadataOutputReference, "annotations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="generateName")
    def generate_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "generateName"))

    @generate_name.setter
    def generate_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2MetadataOutputReference, "generate_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "generateName", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2MetadataOutputReference, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2MetadataOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2MetadataOutputReference, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[HorizontalPodAutoscalerV2Beta2Metadata]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerV2Beta2Metadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerV2Beta2Metadata],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2MetadataOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2Spec",
    jsii_struct_bases=[],
    name_mapping={
        "max_replicas": "maxReplicas",
        "scale_target_ref": "scaleTargetRef",
        "behavior": "behavior",
        "metric": "metric",
        "min_replicas": "minReplicas",
        "target_cpu_utilization_percentage": "targetCpuUtilizationPercentage",
    },
)
class HorizontalPodAutoscalerV2Beta2Spec:
    def __init__(
        self,
        *,
        max_replicas: jsii.Number,
        scale_target_ref: typing.Union["HorizontalPodAutoscalerV2Beta2SpecScaleTargetRef", typing.Dict[str, typing.Any]],
        behavior: typing.Optional[typing.Union["HorizontalPodAutoscalerV2Beta2SpecBehavior", typing.Dict[str, typing.Any]]] = None,
        metric: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerV2Beta2SpecMetric", typing.Dict[str, typing.Any]]]]] = None,
        min_replicas: typing.Optional[jsii.Number] = None,
        target_cpu_utilization_percentage: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param max_replicas: Upper limit for the number of pods that can be set by the autoscaler. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#max_replicas HorizontalPodAutoscalerV2Beta2#max_replicas}
        :param scale_target_ref: scale_target_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#scale_target_ref HorizontalPodAutoscalerV2Beta2#scale_target_ref}
        :param behavior: behavior block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#behavior HorizontalPodAutoscalerV2Beta2#behavior}
        :param metric: metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#metric HorizontalPodAutoscalerV2Beta2#metric}
        :param min_replicas: Lower limit for the number of pods that can be set by the autoscaler, defaults to ``1``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#min_replicas HorizontalPodAutoscalerV2Beta2#min_replicas}
        :param target_cpu_utilization_percentage: Target average CPU utilization (represented as a percentage of requested CPU) over all the pods. If not specified the default autoscaling policy will be used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#target_cpu_utilization_percentage HorizontalPodAutoscalerV2Beta2#target_cpu_utilization_percentage}
        '''
        if isinstance(scale_target_ref, dict):
            scale_target_ref = HorizontalPodAutoscalerV2Beta2SpecScaleTargetRef(**scale_target_ref)
        if isinstance(behavior, dict):
            behavior = HorizontalPodAutoscalerV2Beta2SpecBehavior(**behavior)
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2Spec.__init__)
            check_type(argname="argument max_replicas", value=max_replicas, expected_type=type_hints["max_replicas"])
            check_type(argname="argument scale_target_ref", value=scale_target_ref, expected_type=type_hints["scale_target_ref"])
            check_type(argname="argument behavior", value=behavior, expected_type=type_hints["behavior"])
            check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
            check_type(argname="argument min_replicas", value=min_replicas, expected_type=type_hints["min_replicas"])
            check_type(argname="argument target_cpu_utilization_percentage", value=target_cpu_utilization_percentage, expected_type=type_hints["target_cpu_utilization_percentage"])
        self._values: typing.Dict[str, typing.Any] = {
            "max_replicas": max_replicas,
            "scale_target_ref": scale_target_ref,
        }
        if behavior is not None:
            self._values["behavior"] = behavior
        if metric is not None:
            self._values["metric"] = metric
        if min_replicas is not None:
            self._values["min_replicas"] = min_replicas
        if target_cpu_utilization_percentage is not None:
            self._values["target_cpu_utilization_percentage"] = target_cpu_utilization_percentage

    @builtins.property
    def max_replicas(self) -> jsii.Number:
        '''Upper limit for the number of pods that can be set by the autoscaler.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#max_replicas HorizontalPodAutoscalerV2Beta2#max_replicas}
        '''
        result = self._values.get("max_replicas")
        assert result is not None, "Required property 'max_replicas' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def scale_target_ref(self) -> "HorizontalPodAutoscalerV2Beta2SpecScaleTargetRef":
        '''scale_target_ref block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#scale_target_ref HorizontalPodAutoscalerV2Beta2#scale_target_ref}
        '''
        result = self._values.get("scale_target_ref")
        assert result is not None, "Required property 'scale_target_ref' is missing"
        return typing.cast("HorizontalPodAutoscalerV2Beta2SpecScaleTargetRef", result)

    @builtins.property
    def behavior(self) -> typing.Optional["HorizontalPodAutoscalerV2Beta2SpecBehavior"]:
        '''behavior block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#behavior HorizontalPodAutoscalerV2Beta2#behavior}
        '''
        result = self._values.get("behavior")
        return typing.cast(typing.Optional["HorizontalPodAutoscalerV2Beta2SpecBehavior"], result)

    @builtins.property
    def metric(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecMetric"]]]:
        '''metric block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#metric HorizontalPodAutoscalerV2Beta2#metric}
        '''
        result = self._values.get("metric")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecMetric"]]], result)

    @builtins.property
    def min_replicas(self) -> typing.Optional[jsii.Number]:
        '''Lower limit for the number of pods that can be set by the autoscaler, defaults to ``1``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#min_replicas HorizontalPodAutoscalerV2Beta2#min_replicas}
        '''
        result = self._values.get("min_replicas")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target_cpu_utilization_percentage(self) -> typing.Optional[jsii.Number]:
        '''Target average CPU utilization (represented as a percentage of requested CPU) over all the pods.

        If not specified the default autoscaling policy will be used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#target_cpu_utilization_percentage HorizontalPodAutoscalerV2Beta2#target_cpu_utilization_percentage}
        '''
        result = self._values.get("target_cpu_utilization_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerV2Beta2Spec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecBehavior",
    jsii_struct_bases=[],
    name_mapping={"scale_down": "scaleDown", "scale_up": "scaleUp"},
)
class HorizontalPodAutoscalerV2Beta2SpecBehavior:
    def __init__(
        self,
        *,
        scale_down: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDown", typing.Dict[str, typing.Any]]]]] = None,
        scale_up: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUp", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param scale_down: scale_down block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#scale_down HorizontalPodAutoscalerV2Beta2#scale_down}
        :param scale_up: scale_up block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#scale_up HorizontalPodAutoscalerV2Beta2#scale_up}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecBehavior.__init__)
            check_type(argname="argument scale_down", value=scale_down, expected_type=type_hints["scale_down"])
            check_type(argname="argument scale_up", value=scale_up, expected_type=type_hints["scale_up"])
        self._values: typing.Dict[str, typing.Any] = {}
        if scale_down is not None:
            self._values["scale_down"] = scale_down
        if scale_up is not None:
            self._values["scale_up"] = scale_up

    @builtins.property
    def scale_down(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDown"]]]:
        '''scale_down block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#scale_down HorizontalPodAutoscalerV2Beta2#scale_down}
        '''
        result = self._values.get("scale_down")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDown"]]], result)

    @builtins.property
    def scale_up(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUp"]]]:
        '''scale_up block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#scale_up HorizontalPodAutoscalerV2Beta2#scale_up}
        '''
        result = self._values.get("scale_up")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUp"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerV2Beta2SpecBehavior(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerV2Beta2SpecBehaviorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecBehaviorOutputReference",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecBehaviorOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putScaleDown")
    def put_scale_down(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDown", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecBehaviorOutputReference.put_scale_down)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putScaleDown", [value]))

    @jsii.member(jsii_name="putScaleUp")
    def put_scale_up(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUp", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecBehaviorOutputReference.put_scale_up)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putScaleUp", [value]))

    @jsii.member(jsii_name="resetScaleDown")
    def reset_scale_down(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleDown", []))

    @jsii.member(jsii_name="resetScaleUp")
    def reset_scale_up(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScaleUp", []))

    @builtins.property
    @jsii.member(jsii_name="scaleDown")
    def scale_down(self) -> "HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownList":
        return typing.cast("HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownList", jsii.get(self, "scaleDown"))

    @builtins.property
    @jsii.member(jsii_name="scaleUp")
    def scale_up(self) -> "HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpList":
        return typing.cast("HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpList", jsii.get(self, "scaleUp"))

    @builtins.property
    @jsii.member(jsii_name="scaleDownInput")
    def scale_down_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDown"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDown"]]], jsii.get(self, "scaleDownInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleUpInput")
    def scale_up_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUp"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUp"]]], jsii.get(self, "scaleUpInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerV2Beta2SpecBehavior]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerV2Beta2SpecBehavior], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerV2Beta2SpecBehavior],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecBehaviorOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDown",
    jsii_struct_bases=[],
    name_mapping={
        "policy": "policy",
        "select_policy": "selectPolicy",
        "stabilization_window_seconds": "stabilizationWindowSeconds",
    },
)
class HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDown:
    def __init__(
        self,
        *,
        policy: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicy", typing.Dict[str, typing.Any]]]],
        select_policy: typing.Optional[builtins.str] = None,
        stabilization_window_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param policy: policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#policy HorizontalPodAutoscalerV2Beta2#policy}
        :param select_policy: Used to specify which policy should be used. If not set, the default value Max is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#select_policy HorizontalPodAutoscalerV2Beta2#select_policy}
        :param stabilization_window_seconds: Number of seconds for which past recommendations should be considered while scaling up or scaling down. This value must be greater than or equal to zero and less than or equal to 3600 (one hour). If not set, use the default values: - For scale up: 0 (i.e. no stabilization is done). - For scale down: 300 (i.e. the stabilization window is 300 seconds long). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#stabilization_window_seconds HorizontalPodAutoscalerV2Beta2#stabilization_window_seconds}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDown.__init__)
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument select_policy", value=select_policy, expected_type=type_hints["select_policy"])
            check_type(argname="argument stabilization_window_seconds", value=stabilization_window_seconds, expected_type=type_hints["stabilization_window_seconds"])
        self._values: typing.Dict[str, typing.Any] = {
            "policy": policy,
        }
        if select_policy is not None:
            self._values["select_policy"] = select_policy
        if stabilization_window_seconds is not None:
            self._values["stabilization_window_seconds"] = stabilization_window_seconds

    @builtins.property
    def policy(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicy"]]:
        '''policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#policy HorizontalPodAutoscalerV2Beta2#policy}
        '''
        result = self._values.get("policy")
        assert result is not None, "Required property 'policy' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicy"]], result)

    @builtins.property
    def select_policy(self) -> typing.Optional[builtins.str]:
        '''Used to specify which policy should be used. If not set, the default value Max is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#select_policy HorizontalPodAutoscalerV2Beta2#select_policy}
        '''
        result = self._values.get("select_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stabilization_window_seconds(self) -> typing.Optional[jsii.Number]:
        '''Number of seconds for which past recommendations should be considered while scaling up or scaling down.

        This value must be greater than or equal to zero and less than or equal to 3600 (one hour). If not set, use the default values: - For scale up: 0 (i.e. no stabilization is done). - For scale down: 300 (i.e. the stabilization window is 300 seconds long).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#stabilization_window_seconds HorizontalPodAutoscalerV2Beta2#stabilization_window_seconds}
        '''
        result = self._values.get("stabilization_window_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDown(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownList",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDown]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDown]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDown]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownOutputReference",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putPolicy")
    def put_policy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicy", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownOutputReference.put_policy)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPolicy", [value]))

    @jsii.member(jsii_name="resetSelectPolicy")
    def reset_select_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSelectPolicy", []))

    @jsii.member(jsii_name="resetStabilizationWindowSeconds")
    def reset_stabilization_window_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStabilizationWindowSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> "HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicyList":
        return typing.cast("HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicyList", jsii.get(self, "policy"))

    @builtins.property
    @jsii.member(jsii_name="policyInput")
    def policy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicy"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicy"]]], jsii.get(self, "policyInput"))

    @builtins.property
    @jsii.member(jsii_name="selectPolicyInput")
    def select_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "selectPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="stabilizationWindowSecondsInput")
    def stabilization_window_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "stabilizationWindowSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="selectPolicy")
    def select_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selectPolicy"))

    @select_policy.setter
    def select_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownOutputReference, "select_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selectPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="stabilizationWindowSeconds")
    def stabilization_window_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "stabilizationWindowSeconds"))

    @stabilization_window_seconds.setter
    def stabilization_window_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownOutputReference, "stabilization_window_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stabilizationWindowSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDown, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDown, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDown, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicy",
    jsii_struct_bases=[],
    name_mapping={"period_seconds": "periodSeconds", "type": "type", "value": "value"},
)
class HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicy:
    def __init__(
        self,
        *,
        period_seconds: jsii.Number,
        type: builtins.str,
        value: jsii.Number,
    ) -> None:
        '''
        :param period_seconds: Period specifies the window of time for which the policy should hold true. PeriodSeconds must be greater than zero and less than or equal to 1800 (30 min). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#period_seconds HorizontalPodAutoscalerV2Beta2#period_seconds}
        :param type: Type is used to specify the scaling policy: Percent or Pods. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#type HorizontalPodAutoscalerV2Beta2#type}
        :param value: Value contains the amount of change which is permitted by the policy. It must be greater than zero. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#value HorizontalPodAutoscalerV2Beta2#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicy.__init__)
            check_type(argname="argument period_seconds", value=period_seconds, expected_type=type_hints["period_seconds"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "period_seconds": period_seconds,
            "type": type,
            "value": value,
        }

    @builtins.property
    def period_seconds(self) -> jsii.Number:
        '''Period specifies the window of time for which the policy should hold true.

        PeriodSeconds must be greater than zero and less than or equal to 1800 (30 min).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#period_seconds HorizontalPodAutoscalerV2Beta2#period_seconds}
        '''
        result = self._values.get("period_seconds")
        assert result is not None, "Required property 'period_seconds' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Type is used to specify the scaling policy: Percent or Pods.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#type HorizontalPodAutoscalerV2Beta2#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Value contains the amount of change which is permitted by the policy. It must be greater than zero.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#value HorizontalPodAutoscalerV2Beta2#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicyList",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicyOutputReference",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="periodSecondsInput")
    def period_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "periodSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="periodSeconds")
    def period_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "periodSeconds"))

    @period_seconds.setter
    def period_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicyOutputReference, "period_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "periodSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicyOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicyOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUp",
    jsii_struct_bases=[],
    name_mapping={
        "policy": "policy",
        "select_policy": "selectPolicy",
        "stabilization_window_seconds": "stabilizationWindowSeconds",
    },
)
class HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUp:
    def __init__(
        self,
        *,
        policy: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicy", typing.Dict[str, typing.Any]]]],
        select_policy: typing.Optional[builtins.str] = None,
        stabilization_window_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param policy: policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#policy HorizontalPodAutoscalerV2Beta2#policy}
        :param select_policy: Used to specify which policy should be used. If not set, the default value Max is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#select_policy HorizontalPodAutoscalerV2Beta2#select_policy}
        :param stabilization_window_seconds: Number of seconds for which past recommendations should be considered while scaling up or scaling down. This value must be greater than or equal to zero and less than or equal to 3600 (one hour). If not set, use the default values: - For scale up: 0 (i.e. no stabilization is done). - For scale down: 300 (i.e. the stabilization window is 300 seconds long). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#stabilization_window_seconds HorizontalPodAutoscalerV2Beta2#stabilization_window_seconds}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUp.__init__)
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument select_policy", value=select_policy, expected_type=type_hints["select_policy"])
            check_type(argname="argument stabilization_window_seconds", value=stabilization_window_seconds, expected_type=type_hints["stabilization_window_seconds"])
        self._values: typing.Dict[str, typing.Any] = {
            "policy": policy,
        }
        if select_policy is not None:
            self._values["select_policy"] = select_policy
        if stabilization_window_seconds is not None:
            self._values["stabilization_window_seconds"] = stabilization_window_seconds

    @builtins.property
    def policy(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicy"]]:
        '''policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#policy HorizontalPodAutoscalerV2Beta2#policy}
        '''
        result = self._values.get("policy")
        assert result is not None, "Required property 'policy' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicy"]], result)

    @builtins.property
    def select_policy(self) -> typing.Optional[builtins.str]:
        '''Used to specify which policy should be used. If not set, the default value Max is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#select_policy HorizontalPodAutoscalerV2Beta2#select_policy}
        '''
        result = self._values.get("select_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stabilization_window_seconds(self) -> typing.Optional[jsii.Number]:
        '''Number of seconds for which past recommendations should be considered while scaling up or scaling down.

        This value must be greater than or equal to zero and less than or equal to 3600 (one hour). If not set, use the default values: - For scale up: 0 (i.e. no stabilization is done). - For scale down: 300 (i.e. the stabilization window is 300 seconds long).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#stabilization_window_seconds HorizontalPodAutoscalerV2Beta2#stabilization_window_seconds}
        '''
        result = self._values.get("stabilization_window_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUp(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpList",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUp]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUp]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUp]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpOutputReference",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putPolicy")
    def put_policy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicy", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpOutputReference.put_policy)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPolicy", [value]))

    @jsii.member(jsii_name="resetSelectPolicy")
    def reset_select_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSelectPolicy", []))

    @jsii.member(jsii_name="resetStabilizationWindowSeconds")
    def reset_stabilization_window_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStabilizationWindowSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> "HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicyList":
        return typing.cast("HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicyList", jsii.get(self, "policy"))

    @builtins.property
    @jsii.member(jsii_name="policyInput")
    def policy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicy"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicy"]]], jsii.get(self, "policyInput"))

    @builtins.property
    @jsii.member(jsii_name="selectPolicyInput")
    def select_policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "selectPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="stabilizationWindowSecondsInput")
    def stabilization_window_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "stabilizationWindowSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="selectPolicy")
    def select_policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selectPolicy"))

    @select_policy.setter
    def select_policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpOutputReference, "select_policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selectPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="stabilizationWindowSeconds")
    def stabilization_window_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "stabilizationWindowSeconds"))

    @stabilization_window_seconds.setter
    def stabilization_window_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpOutputReference, "stabilization_window_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stabilizationWindowSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUp, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUp, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUp, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicy",
    jsii_struct_bases=[],
    name_mapping={"period_seconds": "periodSeconds", "type": "type", "value": "value"},
)
class HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicy:
    def __init__(
        self,
        *,
        period_seconds: jsii.Number,
        type: builtins.str,
        value: jsii.Number,
    ) -> None:
        '''
        :param period_seconds: Period specifies the window of time for which the policy should hold true. PeriodSeconds must be greater than zero and less than or equal to 1800 (30 min). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#period_seconds HorizontalPodAutoscalerV2Beta2#period_seconds}
        :param type: Type is used to specify the scaling policy: Percent or Pods. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#type HorizontalPodAutoscalerV2Beta2#type}
        :param value: Value contains the amount of change which is permitted by the policy. It must be greater than zero. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#value HorizontalPodAutoscalerV2Beta2#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicy.__init__)
            check_type(argname="argument period_seconds", value=period_seconds, expected_type=type_hints["period_seconds"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "period_seconds": period_seconds,
            "type": type,
            "value": value,
        }

    @builtins.property
    def period_seconds(self) -> jsii.Number:
        '''Period specifies the window of time for which the policy should hold true.

        PeriodSeconds must be greater than zero and less than or equal to 1800 (30 min).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#period_seconds HorizontalPodAutoscalerV2Beta2#period_seconds}
        '''
        result = self._values.get("period_seconds")
        assert result is not None, "Required property 'period_seconds' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Type is used to specify the scaling policy: Percent or Pods.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#type HorizontalPodAutoscalerV2Beta2#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Value contains the amount of change which is permitted by the policy. It must be greater than zero.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#value HorizontalPodAutoscalerV2Beta2#value}
        '''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicyList",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicyOutputReference",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="periodSecondsInput")
    def period_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "periodSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="periodSeconds")
    def period_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "periodSeconds"))

    @period_seconds.setter
    def period_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicyOutputReference, "period_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "periodSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicyOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicyOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetric",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "container_resource": "containerResource",
        "external": "external",
        "object": "object",
        "pods": "pods",
        "resource": "resource",
    },
)
class HorizontalPodAutoscalerV2Beta2SpecMetric:
    def __init__(
        self,
        *,
        type: builtins.str,
        container_resource: typing.Optional[typing.Union["HorizontalPodAutoscalerV2Beta2SpecMetricContainerResource", typing.Dict[str, typing.Any]]] = None,
        external: typing.Optional[typing.Union["HorizontalPodAutoscalerV2Beta2SpecMetricExternal", typing.Dict[str, typing.Any]]] = None,
        object: typing.Optional[typing.Union["HorizontalPodAutoscalerV2Beta2SpecMetricObject", typing.Dict[str, typing.Any]]] = None,
        pods: typing.Optional[typing.Union["HorizontalPodAutoscalerV2Beta2SpecMetricPods", typing.Dict[str, typing.Any]]] = None,
        resource: typing.Optional[typing.Union["HorizontalPodAutoscalerV2Beta2SpecMetricResource", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param type: type is the type of metric source. It should be one of "ContainerResource", "External", "Object", "Pods" or "Resource", each mapping to a matching field in the object. Note: "ContainerResource" type is available on when the feature-gate HPAContainerMetrics is enabled Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#type HorizontalPodAutoscalerV2Beta2#type}
        :param container_resource: container_resource block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#container_resource HorizontalPodAutoscalerV2Beta2#container_resource}
        :param external: external block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#external HorizontalPodAutoscalerV2Beta2#external}
        :param object: object block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#object HorizontalPodAutoscalerV2Beta2#object}
        :param pods: pods block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#pods HorizontalPodAutoscalerV2Beta2#pods}
        :param resource: resource block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#resource HorizontalPodAutoscalerV2Beta2#resource}
        '''
        if isinstance(container_resource, dict):
            container_resource = HorizontalPodAutoscalerV2Beta2SpecMetricContainerResource(**container_resource)
        if isinstance(external, dict):
            external = HorizontalPodAutoscalerV2Beta2SpecMetricExternal(**external)
        if isinstance(object, dict):
            object = HorizontalPodAutoscalerV2Beta2SpecMetricObject(**object)
        if isinstance(pods, dict):
            pods = HorizontalPodAutoscalerV2Beta2SpecMetricPods(**pods)
        if isinstance(resource, dict):
            resource = HorizontalPodAutoscalerV2Beta2SpecMetricResource(**resource)
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetric.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument container_resource", value=container_resource, expected_type=type_hints["container_resource"])
            check_type(argname="argument external", value=external, expected_type=type_hints["external"])
            check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            check_type(argname="argument pods", value=pods, expected_type=type_hints["pods"])
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if container_resource is not None:
            self._values["container_resource"] = container_resource
        if external is not None:
            self._values["external"] = external
        if object is not None:
            self._values["object"] = object
        if pods is not None:
            self._values["pods"] = pods
        if resource is not None:
            self._values["resource"] = resource

    @builtins.property
    def type(self) -> builtins.str:
        '''type is the type of metric source.

        It should be one of "ContainerResource", "External", "Object", "Pods" or "Resource", each mapping to a matching field in the object. Note: "ContainerResource" type is available on when the feature-gate HPAContainerMetrics is enabled

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#type HorizontalPodAutoscalerV2Beta2#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_resource(
        self,
    ) -> typing.Optional["HorizontalPodAutoscalerV2Beta2SpecMetricContainerResource"]:
        '''container_resource block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#container_resource HorizontalPodAutoscalerV2Beta2#container_resource}
        '''
        result = self._values.get("container_resource")
        return typing.cast(typing.Optional["HorizontalPodAutoscalerV2Beta2SpecMetricContainerResource"], result)

    @builtins.property
    def external(
        self,
    ) -> typing.Optional["HorizontalPodAutoscalerV2Beta2SpecMetricExternal"]:
        '''external block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#external HorizontalPodAutoscalerV2Beta2#external}
        '''
        result = self._values.get("external")
        return typing.cast(typing.Optional["HorizontalPodAutoscalerV2Beta2SpecMetricExternal"], result)

    @builtins.property
    def object(
        self,
    ) -> typing.Optional["HorizontalPodAutoscalerV2Beta2SpecMetricObject"]:
        '''object block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#object HorizontalPodAutoscalerV2Beta2#object}
        '''
        result = self._values.get("object")
        return typing.cast(typing.Optional["HorizontalPodAutoscalerV2Beta2SpecMetricObject"], result)

    @builtins.property
    def pods(self) -> typing.Optional["HorizontalPodAutoscalerV2Beta2SpecMetricPods"]:
        '''pods block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#pods HorizontalPodAutoscalerV2Beta2#pods}
        '''
        result = self._values.get("pods")
        return typing.cast(typing.Optional["HorizontalPodAutoscalerV2Beta2SpecMetricPods"], result)

    @builtins.property
    def resource(
        self,
    ) -> typing.Optional["HorizontalPodAutoscalerV2Beta2SpecMetricResource"]:
        '''resource block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#resource HorizontalPodAutoscalerV2Beta2#resource}
        '''
        result = self._values.get("resource")
        return typing.cast(typing.Optional["HorizontalPodAutoscalerV2Beta2SpecMetricResource"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerV2Beta2SpecMetric(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricContainerResource",
    jsii_struct_bases=[],
    name_mapping={"container": "container", "name": "name", "target": "target"},
)
class HorizontalPodAutoscalerV2Beta2SpecMetricContainerResource:
    def __init__(
        self,
        *,
        container: builtins.str,
        name: builtins.str,
        target: typing.Optional[typing.Union["HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceTarget", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param container: name of the container in the pods of the scaling target. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#container HorizontalPodAutoscalerV2Beta2#container}
        :param name: name of the resource in question. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#name HorizontalPodAutoscalerV2Beta2#name}
        :param target: target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#target HorizontalPodAutoscalerV2Beta2#target}
        '''
        if isinstance(target, dict):
            target = HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceTarget(**target)
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricContainerResource.__init__)
            check_type(argname="argument container", value=container, expected_type=type_hints["container"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[str, typing.Any] = {
            "container": container,
            "name": name,
        }
        if target is not None:
            self._values["target"] = target

    @builtins.property
    def container(self) -> builtins.str:
        '''name of the container in the pods of the scaling target.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#container HorizontalPodAutoscalerV2Beta2#container}
        '''
        result = self._values.get("container")
        assert result is not None, "Required property 'container' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''name of the resource in question.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#name HorizontalPodAutoscalerV2Beta2#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target(
        self,
    ) -> typing.Optional["HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceTarget"]:
        '''target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#target HorizontalPodAutoscalerV2Beta2#target}
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional["HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceTarget"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerV2Beta2SpecMetricContainerResource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceOutputReference",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTarget")
    def put_target(
        self,
        *,
        type: builtins.str,
        average_utilization: typing.Optional[jsii.Number] = None,
        average_value: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: type represents whether the metric type is Utilization, Value, or AverageValue. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#type HorizontalPodAutoscalerV2Beta2#type}
        :param average_utilization: averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#average_utilization HorizontalPodAutoscalerV2Beta2#average_utilization}
        :param average_value: averageValue is the target value of the average of the metric across all relevant pods (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#average_value HorizontalPodAutoscalerV2Beta2#average_value}
        :param value: value is the target value of the metric (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#value HorizontalPodAutoscalerV2Beta2#value}
        '''
        value_ = HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceTarget(
            type=type,
            average_utilization=average_utilization,
            average_value=average_value,
            value=value,
        )

        return typing.cast(None, jsii.invoke(self, "putTarget", [value_]))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(
        self,
    ) -> "HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceTargetOutputReference":
        return typing.cast("HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceTargetOutputReference", jsii.get(self, "target"))

    @builtins.property
    @jsii.member(jsii_name="containerInput")
    def container_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(
        self,
    ) -> typing.Optional["HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceTarget"]:
        return typing.cast(typing.Optional["HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceTarget"], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="container")
    def container(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "container"))

    @container.setter
    def container(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceOutputReference, "container").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "container", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricContainerResource]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricContainerResource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricContainerResource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceTarget",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "average_utilization": "averageUtilization",
        "average_value": "averageValue",
        "value": "value",
    },
)
class HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceTarget:
    def __init__(
        self,
        *,
        type: builtins.str,
        average_utilization: typing.Optional[jsii.Number] = None,
        average_value: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: type represents whether the metric type is Utilization, Value, or AverageValue. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#type HorizontalPodAutoscalerV2Beta2#type}
        :param average_utilization: averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#average_utilization HorizontalPodAutoscalerV2Beta2#average_utilization}
        :param average_value: averageValue is the target value of the average of the metric across all relevant pods (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#average_value HorizontalPodAutoscalerV2Beta2#average_value}
        :param value: value is the target value of the metric (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#value HorizontalPodAutoscalerV2Beta2#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceTarget.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument average_utilization", value=average_utilization, expected_type=type_hints["average_utilization"])
            check_type(argname="argument average_value", value=average_value, expected_type=type_hints["average_value"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if average_utilization is not None:
            self._values["average_utilization"] = average_utilization
        if average_value is not None:
            self._values["average_value"] = average_value
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def type(self) -> builtins.str:
        '''type represents whether the metric type is Utilization, Value, or AverageValue.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#type HorizontalPodAutoscalerV2Beta2#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def average_utilization(self) -> typing.Optional[jsii.Number]:
        '''averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.

        Currently only valid for Resource metric source type

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#average_utilization HorizontalPodAutoscalerV2Beta2#average_utilization}
        '''
        result = self._values.get("average_utilization")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def average_value(self) -> typing.Optional[builtins.str]:
        '''averageValue is the target value of the average of the metric across all relevant pods (as a quantity).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#average_value HorizontalPodAutoscalerV2Beta2#average_value}
        '''
        result = self._values.get("average_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''value is the target value of the metric (as a quantity).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#value HorizontalPodAutoscalerV2Beta2#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceTargetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceTargetOutputReference",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceTargetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAverageUtilization")
    def reset_average_utilization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAverageUtilization", []))

    @jsii.member(jsii_name="resetAverageValue")
    def reset_average_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAverageValue", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="averageUtilizationInput")
    def average_utilization_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "averageUtilizationInput"))

    @builtins.property
    @jsii.member(jsii_name="averageValueInput")
    def average_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "averageValueInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="averageUtilization")
    def average_utilization(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "averageUtilization"))

    @average_utilization.setter
    def average_utilization(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceTargetOutputReference, "average_utilization").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "averageUtilization", value)

    @builtins.property
    @jsii.member(jsii_name="averageValue")
    def average_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "averageValue"))

    @average_value.setter
    def average_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceTargetOutputReference, "average_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "averageValue", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceTargetOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceTargetOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceTarget]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceTarget],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceTargetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricExternal",
    jsii_struct_bases=[],
    name_mapping={"metric": "metric", "target": "target"},
)
class HorizontalPodAutoscalerV2Beta2SpecMetricExternal:
    def __init__(
        self,
        *,
        metric: typing.Union["HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetric", typing.Dict[str, typing.Any]],
        target: typing.Optional[typing.Union["HorizontalPodAutoscalerV2Beta2SpecMetricExternalTarget", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param metric: metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#metric HorizontalPodAutoscalerV2Beta2#metric}
        :param target: target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#target HorizontalPodAutoscalerV2Beta2#target}
        '''
        if isinstance(metric, dict):
            metric = HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetric(**metric)
        if isinstance(target, dict):
            target = HorizontalPodAutoscalerV2Beta2SpecMetricExternalTarget(**target)
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricExternal.__init__)
            check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[str, typing.Any] = {
            "metric": metric,
        }
        if target is not None:
            self._values["target"] = target

    @builtins.property
    def metric(self) -> "HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetric":
        '''metric block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#metric HorizontalPodAutoscalerV2Beta2#metric}
        '''
        result = self._values.get("metric")
        assert result is not None, "Required property 'metric' is missing"
        return typing.cast("HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetric", result)

    @builtins.property
    def target(
        self,
    ) -> typing.Optional["HorizontalPodAutoscalerV2Beta2SpecMetricExternalTarget"]:
        '''target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#target HorizontalPodAutoscalerV2Beta2#target}
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional["HorizontalPodAutoscalerV2Beta2SpecMetricExternalTarget"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerV2Beta2SpecMetricExternal(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetric",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "selector": "selector"},
)
class HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetric:
    def __init__(
        self,
        *,
        name: builtins.str,
        selector: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelector", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name: name is the name of the given metric. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#name HorizontalPodAutoscalerV2Beta2#name}
        :param selector: selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#selector HorizontalPodAutoscalerV2Beta2#selector}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetric.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if selector is not None:
            self._values["selector"] = selector

    @builtins.property
    def name(self) -> builtins.str:
        '''name is the name of the given metric.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#name HorizontalPodAutoscalerV2Beta2#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def selector(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelector"]]]:
        '''selector block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#selector HorizontalPodAutoscalerV2Beta2#selector}
        '''
        result = self._values.get("selector")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelector"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetric(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricOutputReference",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSelector")
    def put_selector(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelector", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricOutputReference.put_selector)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSelector", [value]))

    @jsii.member(jsii_name="resetSelector")
    def reset_selector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSelector", []))

    @builtins.property
    @jsii.member(jsii_name="selector")
    def selector(
        self,
    ) -> "HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorList":
        return typing.cast("HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorList", jsii.get(self, "selector"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="selectorInput")
    def selector_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelector"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelector"]]], jsii.get(self, "selectorInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetric]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetric], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetric],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressions", typing.Dict[str, typing.Any]]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param match_expressions: match_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#match_expressions HorizontalPodAutoscalerV2Beta2#match_expressions}
        :param match_labels: A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#match_labels HorizontalPodAutoscalerV2Beta2#match_labels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelector.__init__)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_labels", value=match_labels, expected_type=type_hints["match_labels"])
        self._values: typing.Dict[str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressions"]]]:
        '''match_expressions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#match_expressions HorizontalPodAutoscalerV2Beta2#match_expressions}
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressions"]]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of {key,value} pairs.

        A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#match_labels HorizontalPodAutoscalerV2Beta2#match_labels}
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorList",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelector]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelector]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelector]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        operator: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: The label key that the selector applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#key HorizontalPodAutoscalerV2Beta2#key}
        :param operator: A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists`` and ``DoesNotExist``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#operator HorizontalPodAutoscalerV2Beta2#operator}
        :param values: An array of string values. If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#values HorizontalPodAutoscalerV2Beta2#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressions.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if operator is not None:
            self._values["operator"] = operator
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The label key that the selector applies to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#key HorizontalPodAutoscalerV2Beta2#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists`` and ``DoesNotExist``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#operator HorizontalPodAutoscalerV2Beta2#operator}
        '''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values.

        If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#values HorizontalPodAutoscalerV2Beta2#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressionsList",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressionsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressionsOutputReference",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

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
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressionsOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressionsOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressionsOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressions, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressions, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressions, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorOutputReference",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMatchExpressions")
    def put_match_expressions(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressions, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorOutputReference.put_match_expressions)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchExpressions", [value]))

    @jsii.member(jsii_name="resetMatchExpressions")
    def reset_match_expressions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchExpressions", []))

    @jsii.member(jsii_name="resetMatchLabels")
    def reset_match_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchLabels", []))

    @builtins.property
    @jsii.member(jsii_name="matchExpressions")
    def match_expressions(
        self,
    ) -> HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressionsList:
        return typing.cast(HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressionsList, jsii.get(self, "matchExpressions"))

    @builtins.property
    @jsii.member(jsii_name="matchExpressionsInput")
    def match_expressions_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressions]]], jsii.get(self, "matchExpressionsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchLabelsInput")
    def match_labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "matchLabelsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchLabels")
    def match_labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "matchLabels"))

    @match_labels.setter
    def match_labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorOutputReference, "match_labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchLabels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelector, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelector, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelector, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HorizontalPodAutoscalerV2Beta2SpecMetricExternalOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricExternalOutputReference",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricExternalOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMetric")
    def put_metric(
        self,
        *,
        name: builtins.str,
        selector: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelector, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name: name is the name of the given metric. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#name HorizontalPodAutoscalerV2Beta2#name}
        :param selector: selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#selector HorizontalPodAutoscalerV2Beta2#selector}
        '''
        value = HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetric(
            name=name, selector=selector
        )

        return typing.cast(None, jsii.invoke(self, "putMetric", [value]))

    @jsii.member(jsii_name="putTarget")
    def put_target(
        self,
        *,
        type: builtins.str,
        average_utilization: typing.Optional[jsii.Number] = None,
        average_value: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: type represents whether the metric type is Utilization, Value, or AverageValue. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#type HorizontalPodAutoscalerV2Beta2#type}
        :param average_utilization: averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#average_utilization HorizontalPodAutoscalerV2Beta2#average_utilization}
        :param average_value: averageValue is the target value of the average of the metric across all relevant pods (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#average_value HorizontalPodAutoscalerV2Beta2#average_value}
        :param value: value is the target value of the metric (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#value HorizontalPodAutoscalerV2Beta2#value}
        '''
        value_ = HorizontalPodAutoscalerV2Beta2SpecMetricExternalTarget(
            type=type,
            average_utilization=average_utilization,
            average_value=average_value,
            value=value,
        )

        return typing.cast(None, jsii.invoke(self, "putTarget", [value_]))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @builtins.property
    @jsii.member(jsii_name="metric")
    def metric(
        self,
    ) -> HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricOutputReference:
        return typing.cast(HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricOutputReference, jsii.get(self, "metric"))

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(
        self,
    ) -> "HorizontalPodAutoscalerV2Beta2SpecMetricExternalTargetOutputReference":
        return typing.cast("HorizontalPodAutoscalerV2Beta2SpecMetricExternalTargetOutputReference", jsii.get(self, "target"))

    @builtins.property
    @jsii.member(jsii_name="metricInput")
    def metric_input(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetric]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetric], jsii.get(self, "metricInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(
        self,
    ) -> typing.Optional["HorizontalPodAutoscalerV2Beta2SpecMetricExternalTarget"]:
        return typing.cast(typing.Optional["HorizontalPodAutoscalerV2Beta2SpecMetricExternalTarget"], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricExternal]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricExternal], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricExternal],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricExternalOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricExternalTarget",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "average_utilization": "averageUtilization",
        "average_value": "averageValue",
        "value": "value",
    },
)
class HorizontalPodAutoscalerV2Beta2SpecMetricExternalTarget:
    def __init__(
        self,
        *,
        type: builtins.str,
        average_utilization: typing.Optional[jsii.Number] = None,
        average_value: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: type represents whether the metric type is Utilization, Value, or AverageValue. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#type HorizontalPodAutoscalerV2Beta2#type}
        :param average_utilization: averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#average_utilization HorizontalPodAutoscalerV2Beta2#average_utilization}
        :param average_value: averageValue is the target value of the average of the metric across all relevant pods (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#average_value HorizontalPodAutoscalerV2Beta2#average_value}
        :param value: value is the target value of the metric (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#value HorizontalPodAutoscalerV2Beta2#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricExternalTarget.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument average_utilization", value=average_utilization, expected_type=type_hints["average_utilization"])
            check_type(argname="argument average_value", value=average_value, expected_type=type_hints["average_value"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if average_utilization is not None:
            self._values["average_utilization"] = average_utilization
        if average_value is not None:
            self._values["average_value"] = average_value
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def type(self) -> builtins.str:
        '''type represents whether the metric type is Utilization, Value, or AverageValue.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#type HorizontalPodAutoscalerV2Beta2#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def average_utilization(self) -> typing.Optional[jsii.Number]:
        '''averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.

        Currently only valid for Resource metric source type

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#average_utilization HorizontalPodAutoscalerV2Beta2#average_utilization}
        '''
        result = self._values.get("average_utilization")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def average_value(self) -> typing.Optional[builtins.str]:
        '''averageValue is the target value of the average of the metric across all relevant pods (as a quantity).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#average_value HorizontalPodAutoscalerV2Beta2#average_value}
        '''
        result = self._values.get("average_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''value is the target value of the metric (as a quantity).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#value HorizontalPodAutoscalerV2Beta2#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerV2Beta2SpecMetricExternalTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerV2Beta2SpecMetricExternalTargetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricExternalTargetOutputReference",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricExternalTargetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAverageUtilization")
    def reset_average_utilization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAverageUtilization", []))

    @jsii.member(jsii_name="resetAverageValue")
    def reset_average_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAverageValue", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="averageUtilizationInput")
    def average_utilization_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "averageUtilizationInput"))

    @builtins.property
    @jsii.member(jsii_name="averageValueInput")
    def average_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "averageValueInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="averageUtilization")
    def average_utilization(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "averageUtilization"))

    @average_utilization.setter
    def average_utilization(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricExternalTargetOutputReference, "average_utilization").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "averageUtilization", value)

    @builtins.property
    @jsii.member(jsii_name="averageValue")
    def average_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "averageValue"))

    @average_value.setter
    def average_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricExternalTargetOutputReference, "average_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "averageValue", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricExternalTargetOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricExternalTargetOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricExternalTarget]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricExternalTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricExternalTarget],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricExternalTargetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HorizontalPodAutoscalerV2Beta2SpecMetricList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricList",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HorizontalPodAutoscalerV2Beta2SpecMetricOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HorizontalPodAutoscalerV2Beta2SpecMetricOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecMetric]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecMetric]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecMetric]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricObject",
    jsii_struct_bases=[],
    name_mapping={
        "described_object": "describedObject",
        "metric": "metric",
        "target": "target",
    },
)
class HorizontalPodAutoscalerV2Beta2SpecMetricObject:
    def __init__(
        self,
        *,
        described_object: typing.Union["HorizontalPodAutoscalerV2Beta2SpecMetricObjectDescribedObject", typing.Dict[str, typing.Any]],
        metric: typing.Union["HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetric", typing.Dict[str, typing.Any]],
        target: typing.Optional[typing.Union["HorizontalPodAutoscalerV2Beta2SpecMetricObjectTarget", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param described_object: described_object block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#described_object HorizontalPodAutoscalerV2Beta2#described_object}
        :param metric: metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#metric HorizontalPodAutoscalerV2Beta2#metric}
        :param target: target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#target HorizontalPodAutoscalerV2Beta2#target}
        '''
        if isinstance(described_object, dict):
            described_object = HorizontalPodAutoscalerV2Beta2SpecMetricObjectDescribedObject(**described_object)
        if isinstance(metric, dict):
            metric = HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetric(**metric)
        if isinstance(target, dict):
            target = HorizontalPodAutoscalerV2Beta2SpecMetricObjectTarget(**target)
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricObject.__init__)
            check_type(argname="argument described_object", value=described_object, expected_type=type_hints["described_object"])
            check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[str, typing.Any] = {
            "described_object": described_object,
            "metric": metric,
        }
        if target is not None:
            self._values["target"] = target

    @builtins.property
    def described_object(
        self,
    ) -> "HorizontalPodAutoscalerV2Beta2SpecMetricObjectDescribedObject":
        '''described_object block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#described_object HorizontalPodAutoscalerV2Beta2#described_object}
        '''
        result = self._values.get("described_object")
        assert result is not None, "Required property 'described_object' is missing"
        return typing.cast("HorizontalPodAutoscalerV2Beta2SpecMetricObjectDescribedObject", result)

    @builtins.property
    def metric(self) -> "HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetric":
        '''metric block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#metric HorizontalPodAutoscalerV2Beta2#metric}
        '''
        result = self._values.get("metric")
        assert result is not None, "Required property 'metric' is missing"
        return typing.cast("HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetric", result)

    @builtins.property
    def target(
        self,
    ) -> typing.Optional["HorizontalPodAutoscalerV2Beta2SpecMetricObjectTarget"]:
        '''target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#target HorizontalPodAutoscalerV2Beta2#target}
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional["HorizontalPodAutoscalerV2Beta2SpecMetricObjectTarget"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerV2Beta2SpecMetricObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricObjectDescribedObject",
    jsii_struct_bases=[],
    name_mapping={"api_version": "apiVersion", "kind": "kind", "name": "name"},
)
class HorizontalPodAutoscalerV2Beta2SpecMetricObjectDescribedObject:
    def __init__(
        self,
        *,
        api_version: builtins.str,
        kind: builtins.str,
        name: builtins.str,
    ) -> None:
        '''
        :param api_version: API version of the referent. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#api_version HorizontalPodAutoscalerV2Beta2#api_version}
        :param kind: Kind of the referent; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#kind HorizontalPodAutoscalerV2Beta2#kind}
        :param name: Name of the referent; More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#name HorizontalPodAutoscalerV2Beta2#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricObjectDescribedObject.__init__)
            check_type(argname="argument api_version", value=api_version, expected_type=type_hints["api_version"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "api_version": api_version,
            "kind": kind,
            "name": name,
        }

    @builtins.property
    def api_version(self) -> builtins.str:
        '''API version of the referent.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#api_version HorizontalPodAutoscalerV2Beta2#api_version}
        '''
        result = self._values.get("api_version")
        assert result is not None, "Required property 'api_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kind(self) -> builtins.str:
        '''Kind of the referent; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#kind HorizontalPodAutoscalerV2Beta2#kind}
        '''
        result = self._values.get("kind")
        assert result is not None, "Required property 'kind' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the referent; More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#name HorizontalPodAutoscalerV2Beta2#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerV2Beta2SpecMetricObjectDescribedObject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerV2Beta2SpecMetricObjectDescribedObjectOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricObjectDescribedObjectOutputReference",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricObjectDescribedObjectOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="apiVersionInput")
    def api_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="apiVersion")
    def api_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiVersion"))

    @api_version.setter
    def api_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricObjectDescribedObjectOutputReference, "api_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiVersion", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricObjectDescribedObjectOutputReference, "kind").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricObjectDescribedObjectOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricObjectDescribedObject]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricObjectDescribedObject], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricObjectDescribedObject],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricObjectDescribedObjectOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetric",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "selector": "selector"},
)
class HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetric:
    def __init__(
        self,
        *,
        name: builtins.str,
        selector: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelector", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name: name is the name of the given metric. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#name HorizontalPodAutoscalerV2Beta2#name}
        :param selector: selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#selector HorizontalPodAutoscalerV2Beta2#selector}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetric.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if selector is not None:
            self._values["selector"] = selector

    @builtins.property
    def name(self) -> builtins.str:
        '''name is the name of the given metric.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#name HorizontalPodAutoscalerV2Beta2#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def selector(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelector"]]]:
        '''selector block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#selector HorizontalPodAutoscalerV2Beta2#selector}
        '''
        result = self._values.get("selector")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelector"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetric(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricOutputReference",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSelector")
    def put_selector(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelector", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricOutputReference.put_selector)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSelector", [value]))

    @jsii.member(jsii_name="resetSelector")
    def reset_selector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSelector", []))

    @builtins.property
    @jsii.member(jsii_name="selector")
    def selector(
        self,
    ) -> "HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorList":
        return typing.cast("HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorList", jsii.get(self, "selector"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="selectorInput")
    def selector_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelector"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelector"]]], jsii.get(self, "selectorInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetric]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetric], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetric],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressions", typing.Dict[str, typing.Any]]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param match_expressions: match_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#match_expressions HorizontalPodAutoscalerV2Beta2#match_expressions}
        :param match_labels: A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#match_labels HorizontalPodAutoscalerV2Beta2#match_labels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelector.__init__)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_labels", value=match_labels, expected_type=type_hints["match_labels"])
        self._values: typing.Dict[str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressions"]]]:
        '''match_expressions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#match_expressions HorizontalPodAutoscalerV2Beta2#match_expressions}
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressions"]]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of {key,value} pairs.

        A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#match_labels HorizontalPodAutoscalerV2Beta2#match_labels}
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorList",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelector]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelector]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelector]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        operator: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: The label key that the selector applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#key HorizontalPodAutoscalerV2Beta2#key}
        :param operator: A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists`` and ``DoesNotExist``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#operator HorizontalPodAutoscalerV2Beta2#operator}
        :param values: An array of string values. If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#values HorizontalPodAutoscalerV2Beta2#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressions.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if operator is not None:
            self._values["operator"] = operator
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The label key that the selector applies to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#key HorizontalPodAutoscalerV2Beta2#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists`` and ``DoesNotExist``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#operator HorizontalPodAutoscalerV2Beta2#operator}
        '''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values.

        If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#values HorizontalPodAutoscalerV2Beta2#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressionsList",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressionsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressionsOutputReference",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

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
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressionsOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressionsOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressionsOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressions, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressions, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressions, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorOutputReference",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMatchExpressions")
    def put_match_expressions(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressions, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorOutputReference.put_match_expressions)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchExpressions", [value]))

    @jsii.member(jsii_name="resetMatchExpressions")
    def reset_match_expressions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchExpressions", []))

    @jsii.member(jsii_name="resetMatchLabels")
    def reset_match_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchLabels", []))

    @builtins.property
    @jsii.member(jsii_name="matchExpressions")
    def match_expressions(
        self,
    ) -> HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressionsList:
        return typing.cast(HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressionsList, jsii.get(self, "matchExpressions"))

    @builtins.property
    @jsii.member(jsii_name="matchExpressionsInput")
    def match_expressions_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressions]]], jsii.get(self, "matchExpressionsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchLabelsInput")
    def match_labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "matchLabelsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchLabels")
    def match_labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "matchLabels"))

    @match_labels.setter
    def match_labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorOutputReference, "match_labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchLabels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelector, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelector, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelector, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HorizontalPodAutoscalerV2Beta2SpecMetricObjectOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricObjectOutputReference",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricObjectOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDescribedObject")
    def put_described_object(
        self,
        *,
        api_version: builtins.str,
        kind: builtins.str,
        name: builtins.str,
    ) -> None:
        '''
        :param api_version: API version of the referent. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#api_version HorizontalPodAutoscalerV2Beta2#api_version}
        :param kind: Kind of the referent; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#kind HorizontalPodAutoscalerV2Beta2#kind}
        :param name: Name of the referent; More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#name HorizontalPodAutoscalerV2Beta2#name}
        '''
        value = HorizontalPodAutoscalerV2Beta2SpecMetricObjectDescribedObject(
            api_version=api_version, kind=kind, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putDescribedObject", [value]))

    @jsii.member(jsii_name="putMetric")
    def put_metric(
        self,
        *,
        name: builtins.str,
        selector: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelector, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name: name is the name of the given metric. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#name HorizontalPodAutoscalerV2Beta2#name}
        :param selector: selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#selector HorizontalPodAutoscalerV2Beta2#selector}
        '''
        value = HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetric(
            name=name, selector=selector
        )

        return typing.cast(None, jsii.invoke(self, "putMetric", [value]))

    @jsii.member(jsii_name="putTarget")
    def put_target(
        self,
        *,
        type: builtins.str,
        average_utilization: typing.Optional[jsii.Number] = None,
        average_value: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: type represents whether the metric type is Utilization, Value, or AverageValue. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#type HorizontalPodAutoscalerV2Beta2#type}
        :param average_utilization: averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#average_utilization HorizontalPodAutoscalerV2Beta2#average_utilization}
        :param average_value: averageValue is the target value of the average of the metric across all relevant pods (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#average_value HorizontalPodAutoscalerV2Beta2#average_value}
        :param value: value is the target value of the metric (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#value HorizontalPodAutoscalerV2Beta2#value}
        '''
        value_ = HorizontalPodAutoscalerV2Beta2SpecMetricObjectTarget(
            type=type,
            average_utilization=average_utilization,
            average_value=average_value,
            value=value,
        )

        return typing.cast(None, jsii.invoke(self, "putTarget", [value_]))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @builtins.property
    @jsii.member(jsii_name="describedObject")
    def described_object(
        self,
    ) -> HorizontalPodAutoscalerV2Beta2SpecMetricObjectDescribedObjectOutputReference:
        return typing.cast(HorizontalPodAutoscalerV2Beta2SpecMetricObjectDescribedObjectOutputReference, jsii.get(self, "describedObject"))

    @builtins.property
    @jsii.member(jsii_name="metric")
    def metric(
        self,
    ) -> HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricOutputReference:
        return typing.cast(HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricOutputReference, jsii.get(self, "metric"))

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(
        self,
    ) -> "HorizontalPodAutoscalerV2Beta2SpecMetricObjectTargetOutputReference":
        return typing.cast("HorizontalPodAutoscalerV2Beta2SpecMetricObjectTargetOutputReference", jsii.get(self, "target"))

    @builtins.property
    @jsii.member(jsii_name="describedObjectInput")
    def described_object_input(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricObjectDescribedObject]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricObjectDescribedObject], jsii.get(self, "describedObjectInput"))

    @builtins.property
    @jsii.member(jsii_name="metricInput")
    def metric_input(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetric]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetric], jsii.get(self, "metricInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(
        self,
    ) -> typing.Optional["HorizontalPodAutoscalerV2Beta2SpecMetricObjectTarget"]:
        return typing.cast(typing.Optional["HorizontalPodAutoscalerV2Beta2SpecMetricObjectTarget"], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricObject]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricObject], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricObject],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricObjectOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricObjectTarget",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "average_utilization": "averageUtilization",
        "average_value": "averageValue",
        "value": "value",
    },
)
class HorizontalPodAutoscalerV2Beta2SpecMetricObjectTarget:
    def __init__(
        self,
        *,
        type: builtins.str,
        average_utilization: typing.Optional[jsii.Number] = None,
        average_value: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: type represents whether the metric type is Utilization, Value, or AverageValue. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#type HorizontalPodAutoscalerV2Beta2#type}
        :param average_utilization: averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#average_utilization HorizontalPodAutoscalerV2Beta2#average_utilization}
        :param average_value: averageValue is the target value of the average of the metric across all relevant pods (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#average_value HorizontalPodAutoscalerV2Beta2#average_value}
        :param value: value is the target value of the metric (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#value HorizontalPodAutoscalerV2Beta2#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricObjectTarget.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument average_utilization", value=average_utilization, expected_type=type_hints["average_utilization"])
            check_type(argname="argument average_value", value=average_value, expected_type=type_hints["average_value"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if average_utilization is not None:
            self._values["average_utilization"] = average_utilization
        if average_value is not None:
            self._values["average_value"] = average_value
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def type(self) -> builtins.str:
        '''type represents whether the metric type is Utilization, Value, or AverageValue.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#type HorizontalPodAutoscalerV2Beta2#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def average_utilization(self) -> typing.Optional[jsii.Number]:
        '''averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.

        Currently only valid for Resource metric source type

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#average_utilization HorizontalPodAutoscalerV2Beta2#average_utilization}
        '''
        result = self._values.get("average_utilization")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def average_value(self) -> typing.Optional[builtins.str]:
        '''averageValue is the target value of the average of the metric across all relevant pods (as a quantity).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#average_value HorizontalPodAutoscalerV2Beta2#average_value}
        '''
        result = self._values.get("average_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''value is the target value of the metric (as a quantity).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#value HorizontalPodAutoscalerV2Beta2#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerV2Beta2SpecMetricObjectTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerV2Beta2SpecMetricObjectTargetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricObjectTargetOutputReference",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricObjectTargetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAverageUtilization")
    def reset_average_utilization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAverageUtilization", []))

    @jsii.member(jsii_name="resetAverageValue")
    def reset_average_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAverageValue", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="averageUtilizationInput")
    def average_utilization_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "averageUtilizationInput"))

    @builtins.property
    @jsii.member(jsii_name="averageValueInput")
    def average_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "averageValueInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="averageUtilization")
    def average_utilization(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "averageUtilization"))

    @average_utilization.setter
    def average_utilization(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricObjectTargetOutputReference, "average_utilization").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "averageUtilization", value)

    @builtins.property
    @jsii.member(jsii_name="averageValue")
    def average_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "averageValue"))

    @average_value.setter
    def average_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricObjectTargetOutputReference, "average_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "averageValue", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricObjectTargetOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricObjectTargetOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricObjectTarget]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricObjectTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricObjectTarget],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricObjectTargetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HorizontalPodAutoscalerV2Beta2SpecMetricOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricOutputReference",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putContainerResource")
    def put_container_resource(
        self,
        *,
        container: builtins.str,
        name: builtins.str,
        target: typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceTarget, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param container: name of the container in the pods of the scaling target. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#container HorizontalPodAutoscalerV2Beta2#container}
        :param name: name of the resource in question. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#name HorizontalPodAutoscalerV2Beta2#name}
        :param target: target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#target HorizontalPodAutoscalerV2Beta2#target}
        '''
        value = HorizontalPodAutoscalerV2Beta2SpecMetricContainerResource(
            container=container, name=name, target=target
        )

        return typing.cast(None, jsii.invoke(self, "putContainerResource", [value]))

    @jsii.member(jsii_name="putExternal")
    def put_external(
        self,
        *,
        metric: typing.Union[HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetric, typing.Dict[str, typing.Any]],
        target: typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecMetricExternalTarget, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param metric: metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#metric HorizontalPodAutoscalerV2Beta2#metric}
        :param target: target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#target HorizontalPodAutoscalerV2Beta2#target}
        '''
        value = HorizontalPodAutoscalerV2Beta2SpecMetricExternal(
            metric=metric, target=target
        )

        return typing.cast(None, jsii.invoke(self, "putExternal", [value]))

    @jsii.member(jsii_name="putObject")
    def put_object(
        self,
        *,
        described_object: typing.Union[HorizontalPodAutoscalerV2Beta2SpecMetricObjectDescribedObject, typing.Dict[str, typing.Any]],
        metric: typing.Union[HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetric, typing.Dict[str, typing.Any]],
        target: typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecMetricObjectTarget, typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param described_object: described_object block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#described_object HorizontalPodAutoscalerV2Beta2#described_object}
        :param metric: metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#metric HorizontalPodAutoscalerV2Beta2#metric}
        :param target: target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#target HorizontalPodAutoscalerV2Beta2#target}
        '''
        value = HorizontalPodAutoscalerV2Beta2SpecMetricObject(
            described_object=described_object, metric=metric, target=target
        )

        return typing.cast(None, jsii.invoke(self, "putObject", [value]))

    @jsii.member(jsii_name="putPods")
    def put_pods(
        self,
        *,
        metric: typing.Union["HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetric", typing.Dict[str, typing.Any]],
        target: typing.Optional[typing.Union["HorizontalPodAutoscalerV2Beta2SpecMetricPodsTarget", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param metric: metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#metric HorizontalPodAutoscalerV2Beta2#metric}
        :param target: target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#target HorizontalPodAutoscalerV2Beta2#target}
        '''
        value = HorizontalPodAutoscalerV2Beta2SpecMetricPods(
            metric=metric, target=target
        )

        return typing.cast(None, jsii.invoke(self, "putPods", [value]))

    @jsii.member(jsii_name="putResource")
    def put_resource(
        self,
        *,
        name: builtins.str,
        target: typing.Optional[typing.Union["HorizontalPodAutoscalerV2Beta2SpecMetricResourceTarget", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: name is the name of the resource in question. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#name HorizontalPodAutoscalerV2Beta2#name}
        :param target: target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#target HorizontalPodAutoscalerV2Beta2#target}
        '''
        value = HorizontalPodAutoscalerV2Beta2SpecMetricResource(
            name=name, target=target
        )

        return typing.cast(None, jsii.invoke(self, "putResource", [value]))

    @jsii.member(jsii_name="resetContainerResource")
    def reset_container_resource(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerResource", []))

    @jsii.member(jsii_name="resetExternal")
    def reset_external(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternal", []))

    @jsii.member(jsii_name="resetObject")
    def reset_object(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetObject", []))

    @jsii.member(jsii_name="resetPods")
    def reset_pods(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPods", []))

    @jsii.member(jsii_name="resetResource")
    def reset_resource(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResource", []))

    @builtins.property
    @jsii.member(jsii_name="containerResource")
    def container_resource(
        self,
    ) -> HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceOutputReference:
        return typing.cast(HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceOutputReference, jsii.get(self, "containerResource"))

    @builtins.property
    @jsii.member(jsii_name="external")
    def external(
        self,
    ) -> HorizontalPodAutoscalerV2Beta2SpecMetricExternalOutputReference:
        return typing.cast(HorizontalPodAutoscalerV2Beta2SpecMetricExternalOutputReference, jsii.get(self, "external"))

    @builtins.property
    @jsii.member(jsii_name="object")
    def object(self) -> HorizontalPodAutoscalerV2Beta2SpecMetricObjectOutputReference:
        return typing.cast(HorizontalPodAutoscalerV2Beta2SpecMetricObjectOutputReference, jsii.get(self, "object"))

    @builtins.property
    @jsii.member(jsii_name="pods")
    def pods(self) -> "HorizontalPodAutoscalerV2Beta2SpecMetricPodsOutputReference":
        return typing.cast("HorizontalPodAutoscalerV2Beta2SpecMetricPodsOutputReference", jsii.get(self, "pods"))

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(
        self,
    ) -> "HorizontalPodAutoscalerV2Beta2SpecMetricResourceOutputReference":
        return typing.cast("HorizontalPodAutoscalerV2Beta2SpecMetricResourceOutputReference", jsii.get(self, "resource"))

    @builtins.property
    @jsii.member(jsii_name="containerResourceInput")
    def container_resource_input(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricContainerResource]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricContainerResource], jsii.get(self, "containerResourceInput"))

    @builtins.property
    @jsii.member(jsii_name="externalInput")
    def external_input(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricExternal]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricExternal], jsii.get(self, "externalInput"))

    @builtins.property
    @jsii.member(jsii_name="objectInput")
    def object_input(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricObject]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricObject], jsii.get(self, "objectInput"))

    @builtins.property
    @jsii.member(jsii_name="podsInput")
    def pods_input(
        self,
    ) -> typing.Optional["HorizontalPodAutoscalerV2Beta2SpecMetricPods"]:
        return typing.cast(typing.Optional["HorizontalPodAutoscalerV2Beta2SpecMetricPods"], jsii.get(self, "podsInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceInput")
    def resource_input(
        self,
    ) -> typing.Optional["HorizontalPodAutoscalerV2Beta2SpecMetricResource"]:
        return typing.cast(typing.Optional["HorizontalPodAutoscalerV2Beta2SpecMetricResource"], jsii.get(self, "resourceInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecMetric, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecMetric, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecMetric, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricPods",
    jsii_struct_bases=[],
    name_mapping={"metric": "metric", "target": "target"},
)
class HorizontalPodAutoscalerV2Beta2SpecMetricPods:
    def __init__(
        self,
        *,
        metric: typing.Union["HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetric", typing.Dict[str, typing.Any]],
        target: typing.Optional[typing.Union["HorizontalPodAutoscalerV2Beta2SpecMetricPodsTarget", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param metric: metric block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#metric HorizontalPodAutoscalerV2Beta2#metric}
        :param target: target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#target HorizontalPodAutoscalerV2Beta2#target}
        '''
        if isinstance(metric, dict):
            metric = HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetric(**metric)
        if isinstance(target, dict):
            target = HorizontalPodAutoscalerV2Beta2SpecMetricPodsTarget(**target)
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricPods.__init__)
            check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[str, typing.Any] = {
            "metric": metric,
        }
        if target is not None:
            self._values["target"] = target

    @builtins.property
    def metric(self) -> "HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetric":
        '''metric block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#metric HorizontalPodAutoscalerV2Beta2#metric}
        '''
        result = self._values.get("metric")
        assert result is not None, "Required property 'metric' is missing"
        return typing.cast("HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetric", result)

    @builtins.property
    def target(
        self,
    ) -> typing.Optional["HorizontalPodAutoscalerV2Beta2SpecMetricPodsTarget"]:
        '''target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#target HorizontalPodAutoscalerV2Beta2#target}
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional["HorizontalPodAutoscalerV2Beta2SpecMetricPodsTarget"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerV2Beta2SpecMetricPods(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetric",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "selector": "selector"},
)
class HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetric:
    def __init__(
        self,
        *,
        name: builtins.str,
        selector: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelector", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name: name is the name of the given metric. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#name HorizontalPodAutoscalerV2Beta2#name}
        :param selector: selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#selector HorizontalPodAutoscalerV2Beta2#selector}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetric.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if selector is not None:
            self._values["selector"] = selector

    @builtins.property
    def name(self) -> builtins.str:
        '''name is the name of the given metric.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#name HorizontalPodAutoscalerV2Beta2#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def selector(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelector"]]]:
        '''selector block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#selector HorizontalPodAutoscalerV2Beta2#selector}
        '''
        result = self._values.get("selector")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelector"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetric(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricOutputReference",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSelector")
    def put_selector(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelector", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricOutputReference.put_selector)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSelector", [value]))

    @jsii.member(jsii_name="resetSelector")
    def reset_selector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSelector", []))

    @builtins.property
    @jsii.member(jsii_name="selector")
    def selector(
        self,
    ) -> "HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorList":
        return typing.cast("HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorList", jsii.get(self, "selector"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="selectorInput")
    def selector_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelector"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelector"]]], jsii.get(self, "selectorInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetric]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetric], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetric],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelector",
    jsii_struct_bases=[],
    name_mapping={
        "match_expressions": "matchExpressions",
        "match_labels": "matchLabels",
    },
)
class HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelector:
    def __init__(
        self,
        *,
        match_expressions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressions", typing.Dict[str, typing.Any]]]]] = None,
        match_labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param match_expressions: match_expressions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#match_expressions HorizontalPodAutoscalerV2Beta2#match_expressions}
        :param match_labels: A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#match_labels HorizontalPodAutoscalerV2Beta2#match_labels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelector.__init__)
            check_type(argname="argument match_expressions", value=match_expressions, expected_type=type_hints["match_expressions"])
            check_type(argname="argument match_labels", value=match_labels, expected_type=type_hints["match_labels"])
        self._values: typing.Dict[str, typing.Any] = {}
        if match_expressions is not None:
            self._values["match_expressions"] = match_expressions
        if match_labels is not None:
            self._values["match_labels"] = match_labels

    @builtins.property
    def match_expressions(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressions"]]]:
        '''match_expressions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#match_expressions HorizontalPodAutoscalerV2Beta2#match_expressions}
        '''
        result = self._values.get("match_expressions")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressions"]]], result)

    @builtins.property
    def match_labels(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of {key,value} pairs.

        A single {key,value} in the matchLabels map is equivalent to an element of ``match_expressions``, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#match_labels HorizontalPodAutoscalerV2Beta2#match_labels}
        '''
        result = self._values.get("match_labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelector(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorList",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelector]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelector]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelector]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressions",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "operator": "operator", "values": "values"},
)
class HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressions:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        operator: typing.Optional[builtins.str] = None,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param key: The label key that the selector applies to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#key HorizontalPodAutoscalerV2Beta2#key}
        :param operator: A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists`` and ``DoesNotExist``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#operator HorizontalPodAutoscalerV2Beta2#operator}
        :param values: An array of string values. If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#values HorizontalPodAutoscalerV2Beta2#values}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressions.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if operator is not None:
            self._values["operator"] = operator
        if values is not None:
            self._values["values"] = values

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The label key that the selector applies to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#key HorizontalPodAutoscalerV2Beta2#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operator(self) -> typing.Optional[builtins.str]:
        '''A key's relationship to a set of values. Valid operators ard ``In``, ``NotIn``, ``Exists`` and ``DoesNotExist``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#operator HorizontalPodAutoscalerV2Beta2#operator}
        '''
        result = self._values.get("operator")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of string values.

        If the operator is ``In`` or ``NotIn``, the values array must be non-empty. If the operator is ``Exists`` or ``DoesNotExist``, the values array must be empty. This array is replaced during a strategic merge patch.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#values HorizontalPodAutoscalerV2Beta2#values}
        '''
        result = self._values.get("values")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressionsList",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressionsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressionsOutputReference",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetOperator")
    def reset_operator(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOperator", []))

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
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressionsOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressionsOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "values"))

    @values.setter
    def values(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressionsOutputReference, "values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "values", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressions, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressions, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressions, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorOutputReference",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putMatchExpressions")
    def put_match_expressions(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressions, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorOutputReference.put_match_expressions)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMatchExpressions", [value]))

    @jsii.member(jsii_name="resetMatchExpressions")
    def reset_match_expressions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchExpressions", []))

    @jsii.member(jsii_name="resetMatchLabels")
    def reset_match_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchLabels", []))

    @builtins.property
    @jsii.member(jsii_name="matchExpressions")
    def match_expressions(
        self,
    ) -> HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressionsList:
        return typing.cast(HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressionsList, jsii.get(self, "matchExpressions"))

    @builtins.property
    @jsii.member(jsii_name="matchExpressionsInput")
    def match_expressions_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressions]]], jsii.get(self, "matchExpressionsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchLabelsInput")
    def match_labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "matchLabelsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchLabels")
    def match_labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "matchLabels"))

    @match_labels.setter
    def match_labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorOutputReference, "match_labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchLabels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelector, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelector, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelector, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HorizontalPodAutoscalerV2Beta2SpecMetricPodsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricPodsOutputReference",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricPodsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putMetric")
    def put_metric(
        self,
        *,
        name: builtins.str,
        selector: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelector, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name: name is the name of the given metric. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#name HorizontalPodAutoscalerV2Beta2#name}
        :param selector: selector block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#selector HorizontalPodAutoscalerV2Beta2#selector}
        '''
        value = HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetric(
            name=name, selector=selector
        )

        return typing.cast(None, jsii.invoke(self, "putMetric", [value]))

    @jsii.member(jsii_name="putTarget")
    def put_target(
        self,
        *,
        type: builtins.str,
        average_utilization: typing.Optional[jsii.Number] = None,
        average_value: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: type represents whether the metric type is Utilization, Value, or AverageValue. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#type HorizontalPodAutoscalerV2Beta2#type}
        :param average_utilization: averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#average_utilization HorizontalPodAutoscalerV2Beta2#average_utilization}
        :param average_value: averageValue is the target value of the average of the metric across all relevant pods (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#average_value HorizontalPodAutoscalerV2Beta2#average_value}
        :param value: value is the target value of the metric (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#value HorizontalPodAutoscalerV2Beta2#value}
        '''
        value_ = HorizontalPodAutoscalerV2Beta2SpecMetricPodsTarget(
            type=type,
            average_utilization=average_utilization,
            average_value=average_value,
            value=value,
        )

        return typing.cast(None, jsii.invoke(self, "putTarget", [value_]))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @builtins.property
    @jsii.member(jsii_name="metric")
    def metric(
        self,
    ) -> HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricOutputReference:
        return typing.cast(HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricOutputReference, jsii.get(self, "metric"))

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(
        self,
    ) -> "HorizontalPodAutoscalerV2Beta2SpecMetricPodsTargetOutputReference":
        return typing.cast("HorizontalPodAutoscalerV2Beta2SpecMetricPodsTargetOutputReference", jsii.get(self, "target"))

    @builtins.property
    @jsii.member(jsii_name="metricInput")
    def metric_input(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetric]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetric], jsii.get(self, "metricInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(
        self,
    ) -> typing.Optional["HorizontalPodAutoscalerV2Beta2SpecMetricPodsTarget"]:
        return typing.cast(typing.Optional["HorizontalPodAutoscalerV2Beta2SpecMetricPodsTarget"], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricPods]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricPods], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricPods],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricPodsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricPodsTarget",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "average_utilization": "averageUtilization",
        "average_value": "averageValue",
        "value": "value",
    },
)
class HorizontalPodAutoscalerV2Beta2SpecMetricPodsTarget:
    def __init__(
        self,
        *,
        type: builtins.str,
        average_utilization: typing.Optional[jsii.Number] = None,
        average_value: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: type represents whether the metric type is Utilization, Value, or AverageValue. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#type HorizontalPodAutoscalerV2Beta2#type}
        :param average_utilization: averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#average_utilization HorizontalPodAutoscalerV2Beta2#average_utilization}
        :param average_value: averageValue is the target value of the average of the metric across all relevant pods (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#average_value HorizontalPodAutoscalerV2Beta2#average_value}
        :param value: value is the target value of the metric (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#value HorizontalPodAutoscalerV2Beta2#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricPodsTarget.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument average_utilization", value=average_utilization, expected_type=type_hints["average_utilization"])
            check_type(argname="argument average_value", value=average_value, expected_type=type_hints["average_value"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if average_utilization is not None:
            self._values["average_utilization"] = average_utilization
        if average_value is not None:
            self._values["average_value"] = average_value
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def type(self) -> builtins.str:
        '''type represents whether the metric type is Utilization, Value, or AverageValue.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#type HorizontalPodAutoscalerV2Beta2#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def average_utilization(self) -> typing.Optional[jsii.Number]:
        '''averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.

        Currently only valid for Resource metric source type

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#average_utilization HorizontalPodAutoscalerV2Beta2#average_utilization}
        '''
        result = self._values.get("average_utilization")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def average_value(self) -> typing.Optional[builtins.str]:
        '''averageValue is the target value of the average of the metric across all relevant pods (as a quantity).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#average_value HorizontalPodAutoscalerV2Beta2#average_value}
        '''
        result = self._values.get("average_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''value is the target value of the metric (as a quantity).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#value HorizontalPodAutoscalerV2Beta2#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerV2Beta2SpecMetricPodsTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerV2Beta2SpecMetricPodsTargetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricPodsTargetOutputReference",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricPodsTargetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAverageUtilization")
    def reset_average_utilization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAverageUtilization", []))

    @jsii.member(jsii_name="resetAverageValue")
    def reset_average_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAverageValue", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="averageUtilizationInput")
    def average_utilization_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "averageUtilizationInput"))

    @builtins.property
    @jsii.member(jsii_name="averageValueInput")
    def average_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "averageValueInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="averageUtilization")
    def average_utilization(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "averageUtilization"))

    @average_utilization.setter
    def average_utilization(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricPodsTargetOutputReference, "average_utilization").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "averageUtilization", value)

    @builtins.property
    @jsii.member(jsii_name="averageValue")
    def average_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "averageValue"))

    @average_value.setter
    def average_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricPodsTargetOutputReference, "average_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "averageValue", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricPodsTargetOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricPodsTargetOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricPodsTarget]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricPodsTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricPodsTarget],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricPodsTargetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricResource",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "target": "target"},
)
class HorizontalPodAutoscalerV2Beta2SpecMetricResource:
    def __init__(
        self,
        *,
        name: builtins.str,
        target: typing.Optional[typing.Union["HorizontalPodAutoscalerV2Beta2SpecMetricResourceTarget", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: name is the name of the resource in question. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#name HorizontalPodAutoscalerV2Beta2#name}
        :param target: target block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#target HorizontalPodAutoscalerV2Beta2#target}
        '''
        if isinstance(target, dict):
            target = HorizontalPodAutoscalerV2Beta2SpecMetricResourceTarget(**target)
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricResource.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if target is not None:
            self._values["target"] = target

    @builtins.property
    def name(self) -> builtins.str:
        '''name is the name of the resource in question.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#name HorizontalPodAutoscalerV2Beta2#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target(
        self,
    ) -> typing.Optional["HorizontalPodAutoscalerV2Beta2SpecMetricResourceTarget"]:
        '''target block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#target HorizontalPodAutoscalerV2Beta2#target}
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional["HorizontalPodAutoscalerV2Beta2SpecMetricResourceTarget"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerV2Beta2SpecMetricResource(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerV2Beta2SpecMetricResourceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricResourceOutputReference",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricResourceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTarget")
    def put_target(
        self,
        *,
        type: builtins.str,
        average_utilization: typing.Optional[jsii.Number] = None,
        average_value: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: type represents whether the metric type is Utilization, Value, or AverageValue. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#type HorizontalPodAutoscalerV2Beta2#type}
        :param average_utilization: averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#average_utilization HorizontalPodAutoscalerV2Beta2#average_utilization}
        :param average_value: averageValue is the target value of the average of the metric across all relevant pods (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#average_value HorizontalPodAutoscalerV2Beta2#average_value}
        :param value: value is the target value of the metric (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#value HorizontalPodAutoscalerV2Beta2#value}
        '''
        value_ = HorizontalPodAutoscalerV2Beta2SpecMetricResourceTarget(
            type=type,
            average_utilization=average_utilization,
            average_value=average_value,
            value=value,
        )

        return typing.cast(None, jsii.invoke(self, "putTarget", [value_]))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(
        self,
    ) -> "HorizontalPodAutoscalerV2Beta2SpecMetricResourceTargetOutputReference":
        return typing.cast("HorizontalPodAutoscalerV2Beta2SpecMetricResourceTargetOutputReference", jsii.get(self, "target"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(
        self,
    ) -> typing.Optional["HorizontalPodAutoscalerV2Beta2SpecMetricResourceTarget"]:
        return typing.cast(typing.Optional["HorizontalPodAutoscalerV2Beta2SpecMetricResourceTarget"], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricResourceOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricResource]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricResource], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricResource],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricResourceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricResourceTarget",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "average_utilization": "averageUtilization",
        "average_value": "averageValue",
        "value": "value",
    },
)
class HorizontalPodAutoscalerV2Beta2SpecMetricResourceTarget:
    def __init__(
        self,
        *,
        type: builtins.str,
        average_utilization: typing.Optional[jsii.Number] = None,
        average_value: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: type represents whether the metric type is Utilization, Value, or AverageValue. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#type HorizontalPodAutoscalerV2Beta2#type}
        :param average_utilization: averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#average_utilization HorizontalPodAutoscalerV2Beta2#average_utilization}
        :param average_value: averageValue is the target value of the average of the metric across all relevant pods (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#average_value HorizontalPodAutoscalerV2Beta2#average_value}
        :param value: value is the target value of the metric (as a quantity). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#value HorizontalPodAutoscalerV2Beta2#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricResourceTarget.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument average_utilization", value=average_utilization, expected_type=type_hints["average_utilization"])
            check_type(argname="argument average_value", value=average_value, expected_type=type_hints["average_value"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if average_utilization is not None:
            self._values["average_utilization"] = average_utilization
        if average_value is not None:
            self._values["average_value"] = average_value
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def type(self) -> builtins.str:
        '''type represents whether the metric type is Utilization, Value, or AverageValue.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#type HorizontalPodAutoscalerV2Beta2#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def average_utilization(self) -> typing.Optional[jsii.Number]:
        '''averageUtilization is the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods.

        Currently only valid for Resource metric source type

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#average_utilization HorizontalPodAutoscalerV2Beta2#average_utilization}
        '''
        result = self._values.get("average_utilization")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def average_value(self) -> typing.Optional[builtins.str]:
        '''averageValue is the target value of the average of the metric across all relevant pods (as a quantity).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#average_value HorizontalPodAutoscalerV2Beta2#average_value}
        '''
        result = self._values.get("average_value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''value is the target value of the metric (as a quantity).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#value HorizontalPodAutoscalerV2Beta2#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerV2Beta2SpecMetricResourceTarget(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerV2Beta2SpecMetricResourceTargetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecMetricResourceTargetOutputReference",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecMetricResourceTargetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAverageUtilization")
    def reset_average_utilization(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAverageUtilization", []))

    @jsii.member(jsii_name="resetAverageValue")
    def reset_average_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAverageValue", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="averageUtilizationInput")
    def average_utilization_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "averageUtilizationInput"))

    @builtins.property
    @jsii.member(jsii_name="averageValueInput")
    def average_value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "averageValueInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="averageUtilization")
    def average_utilization(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "averageUtilization"))

    @average_utilization.setter
    def average_utilization(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricResourceTargetOutputReference, "average_utilization").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "averageUtilization", value)

    @builtins.property
    @jsii.member(jsii_name="averageValue")
    def average_value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "averageValue"))

    @average_value.setter
    def average_value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricResourceTargetOutputReference, "average_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "averageValue", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricResourceTargetOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricResourceTargetOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricResourceTarget]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricResourceTarget], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerV2Beta2SpecMetricResourceTarget],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecMetricResourceTargetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class HorizontalPodAutoscalerV2Beta2SpecOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecOutputReference",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putBehavior")
    def put_behavior(
        self,
        *,
        scale_down: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDown, typing.Dict[str, typing.Any]]]]] = None,
        scale_up: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUp, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param scale_down: scale_down block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#scale_down HorizontalPodAutoscalerV2Beta2#scale_down}
        :param scale_up: scale_up block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#scale_up HorizontalPodAutoscalerV2Beta2#scale_up}
        '''
        value = HorizontalPodAutoscalerV2Beta2SpecBehavior(
            scale_down=scale_down, scale_up=scale_up
        )

        return typing.cast(None, jsii.invoke(self, "putBehavior", [value]))

    @jsii.member(jsii_name="putMetric")
    def put_metric(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[HorizontalPodAutoscalerV2Beta2SpecMetric, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecOutputReference.put_metric)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMetric", [value]))

    @jsii.member(jsii_name="putScaleTargetRef")
    def put_scale_target_ref(
        self,
        *,
        kind: builtins.str,
        name: builtins.str,
        api_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param kind: Kind of the referent. e.g. ``ReplicationController``. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#kind HorizontalPodAutoscalerV2Beta2#kind}
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#name HorizontalPodAutoscalerV2Beta2#name}
        :param api_version: API version of the referent. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#api_version HorizontalPodAutoscalerV2Beta2#api_version}
        '''
        value = HorizontalPodAutoscalerV2Beta2SpecScaleTargetRef(
            kind=kind, name=name, api_version=api_version
        )

        return typing.cast(None, jsii.invoke(self, "putScaleTargetRef", [value]))

    @jsii.member(jsii_name="resetBehavior")
    def reset_behavior(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBehavior", []))

    @jsii.member(jsii_name="resetMetric")
    def reset_metric(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetric", []))

    @jsii.member(jsii_name="resetMinReplicas")
    def reset_min_replicas(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinReplicas", []))

    @jsii.member(jsii_name="resetTargetCpuUtilizationPercentage")
    def reset_target_cpu_utilization_percentage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetCpuUtilizationPercentage", []))

    @builtins.property
    @jsii.member(jsii_name="behavior")
    def behavior(self) -> HorizontalPodAutoscalerV2Beta2SpecBehaviorOutputReference:
        return typing.cast(HorizontalPodAutoscalerV2Beta2SpecBehaviorOutputReference, jsii.get(self, "behavior"))

    @builtins.property
    @jsii.member(jsii_name="metric")
    def metric(self) -> HorizontalPodAutoscalerV2Beta2SpecMetricList:
        return typing.cast(HorizontalPodAutoscalerV2Beta2SpecMetricList, jsii.get(self, "metric"))

    @builtins.property
    @jsii.member(jsii_name="scaleTargetRef")
    def scale_target_ref(
        self,
    ) -> "HorizontalPodAutoscalerV2Beta2SpecScaleTargetRefOutputReference":
        return typing.cast("HorizontalPodAutoscalerV2Beta2SpecScaleTargetRefOutputReference", jsii.get(self, "scaleTargetRef"))

    @builtins.property
    @jsii.member(jsii_name="behaviorInput")
    def behavior_input(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerV2Beta2SpecBehavior]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerV2Beta2SpecBehavior], jsii.get(self, "behaviorInput"))

    @builtins.property
    @jsii.member(jsii_name="maxReplicasInput")
    def max_replicas_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxReplicasInput"))

    @builtins.property
    @jsii.member(jsii_name="metricInput")
    def metric_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecMetric]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[HorizontalPodAutoscalerV2Beta2SpecMetric]]], jsii.get(self, "metricInput"))

    @builtins.property
    @jsii.member(jsii_name="minReplicasInput")
    def min_replicas_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minReplicasInput"))

    @builtins.property
    @jsii.member(jsii_name="scaleTargetRefInput")
    def scale_target_ref_input(
        self,
    ) -> typing.Optional["HorizontalPodAutoscalerV2Beta2SpecScaleTargetRef"]:
        return typing.cast(typing.Optional["HorizontalPodAutoscalerV2Beta2SpecScaleTargetRef"], jsii.get(self, "scaleTargetRefInput"))

    @builtins.property
    @jsii.member(jsii_name="targetCpuUtilizationPercentageInput")
    def target_cpu_utilization_percentage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetCpuUtilizationPercentageInput"))

    @builtins.property
    @jsii.member(jsii_name="maxReplicas")
    def max_replicas(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxReplicas"))

    @max_replicas.setter
    def max_replicas(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecOutputReference, "max_replicas").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxReplicas", value)

    @builtins.property
    @jsii.member(jsii_name="minReplicas")
    def min_replicas(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minReplicas"))

    @min_replicas.setter
    def min_replicas(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecOutputReference, "min_replicas").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minReplicas", value)

    @builtins.property
    @jsii.member(jsii_name="targetCpuUtilizationPercentage")
    def target_cpu_utilization_percentage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetCpuUtilizationPercentage"))

    @target_cpu_utilization_percentage.setter
    def target_cpu_utilization_percentage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecOutputReference, "target_cpu_utilization_percentage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetCpuUtilizationPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[HorizontalPodAutoscalerV2Beta2Spec]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerV2Beta2Spec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerV2Beta2Spec],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecScaleTargetRef",
    jsii_struct_bases=[],
    name_mapping={"kind": "kind", "name": "name", "api_version": "apiVersion"},
)
class HorizontalPodAutoscalerV2Beta2SpecScaleTargetRef:
    def __init__(
        self,
        *,
        kind: builtins.str,
        name: builtins.str,
        api_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param kind: Kind of the referent. e.g. ``ReplicationController``. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#kind HorizontalPodAutoscalerV2Beta2#kind}
        :param name: Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#name HorizontalPodAutoscalerV2Beta2#name}
        :param api_version: API version of the referent. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#api_version HorizontalPodAutoscalerV2Beta2#api_version}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecScaleTargetRef.__init__)
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument api_version", value=api_version, expected_type=type_hints["api_version"])
        self._values: typing.Dict[str, typing.Any] = {
            "kind": kind,
            "name": name,
        }
        if api_version is not None:
            self._values["api_version"] = api_version

    @builtins.property
    def kind(self) -> builtins.str:
        '''Kind of the referent. e.g. ``ReplicationController``. More info: http://releases.k8s.io/HEAD/docs/devel/api-conventions.md#types-kinds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#kind HorizontalPodAutoscalerV2Beta2#kind}
        '''
        result = self._values.get("kind")
        assert result is not None, "Required property 'kind' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the referent. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#name HorizontalPodAutoscalerV2Beta2#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_version(self) -> typing.Optional[builtins.str]:
        '''API version of the referent.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/horizontal_pod_autoscaler_v2beta2#api_version HorizontalPodAutoscalerV2Beta2#api_version}
        '''
        result = self._values.get("api_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HorizontalPodAutoscalerV2Beta2SpecScaleTargetRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HorizontalPodAutoscalerV2Beta2SpecScaleTargetRefOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.horizontalPodAutoscalerV2Beta2.HorizontalPodAutoscalerV2Beta2SpecScaleTargetRefOutputReference",
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
            type_hints = typing.get_type_hints(HorizontalPodAutoscalerV2Beta2SpecScaleTargetRefOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetApiVersion")
    def reset_api_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiVersion", []))

    @builtins.property
    @jsii.member(jsii_name="apiVersionInput")
    def api_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="apiVersion")
    def api_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiVersion"))

    @api_version.setter
    def api_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecScaleTargetRefOutputReference, "api_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiVersion", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecScaleTargetRefOutputReference, "kind").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecScaleTargetRefOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[HorizontalPodAutoscalerV2Beta2SpecScaleTargetRef]:
        return typing.cast(typing.Optional[HorizontalPodAutoscalerV2Beta2SpecScaleTargetRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[HorizontalPodAutoscalerV2Beta2SpecScaleTargetRef],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(HorizontalPodAutoscalerV2Beta2SpecScaleTargetRefOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "HorizontalPodAutoscalerV2Beta2",
    "HorizontalPodAutoscalerV2Beta2Config",
    "HorizontalPodAutoscalerV2Beta2Metadata",
    "HorizontalPodAutoscalerV2Beta2MetadataOutputReference",
    "HorizontalPodAutoscalerV2Beta2Spec",
    "HorizontalPodAutoscalerV2Beta2SpecBehavior",
    "HorizontalPodAutoscalerV2Beta2SpecBehaviorOutputReference",
    "HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDown",
    "HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownList",
    "HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownOutputReference",
    "HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicy",
    "HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicyList",
    "HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleDownPolicyOutputReference",
    "HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUp",
    "HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpList",
    "HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpOutputReference",
    "HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicy",
    "HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicyList",
    "HorizontalPodAutoscalerV2Beta2SpecBehaviorScaleUpPolicyOutputReference",
    "HorizontalPodAutoscalerV2Beta2SpecMetric",
    "HorizontalPodAutoscalerV2Beta2SpecMetricContainerResource",
    "HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceOutputReference",
    "HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceTarget",
    "HorizontalPodAutoscalerV2Beta2SpecMetricContainerResourceTargetOutputReference",
    "HorizontalPodAutoscalerV2Beta2SpecMetricExternal",
    "HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetric",
    "HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricOutputReference",
    "HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelector",
    "HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorList",
    "HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressions",
    "HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressionsList",
    "HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorMatchExpressionsOutputReference",
    "HorizontalPodAutoscalerV2Beta2SpecMetricExternalMetricSelectorOutputReference",
    "HorizontalPodAutoscalerV2Beta2SpecMetricExternalOutputReference",
    "HorizontalPodAutoscalerV2Beta2SpecMetricExternalTarget",
    "HorizontalPodAutoscalerV2Beta2SpecMetricExternalTargetOutputReference",
    "HorizontalPodAutoscalerV2Beta2SpecMetricList",
    "HorizontalPodAutoscalerV2Beta2SpecMetricObject",
    "HorizontalPodAutoscalerV2Beta2SpecMetricObjectDescribedObject",
    "HorizontalPodAutoscalerV2Beta2SpecMetricObjectDescribedObjectOutputReference",
    "HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetric",
    "HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricOutputReference",
    "HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelector",
    "HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorList",
    "HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressions",
    "HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressionsList",
    "HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorMatchExpressionsOutputReference",
    "HorizontalPodAutoscalerV2Beta2SpecMetricObjectMetricSelectorOutputReference",
    "HorizontalPodAutoscalerV2Beta2SpecMetricObjectOutputReference",
    "HorizontalPodAutoscalerV2Beta2SpecMetricObjectTarget",
    "HorizontalPodAutoscalerV2Beta2SpecMetricObjectTargetOutputReference",
    "HorizontalPodAutoscalerV2Beta2SpecMetricOutputReference",
    "HorizontalPodAutoscalerV2Beta2SpecMetricPods",
    "HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetric",
    "HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricOutputReference",
    "HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelector",
    "HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorList",
    "HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressions",
    "HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressionsList",
    "HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorMatchExpressionsOutputReference",
    "HorizontalPodAutoscalerV2Beta2SpecMetricPodsMetricSelectorOutputReference",
    "HorizontalPodAutoscalerV2Beta2SpecMetricPodsOutputReference",
    "HorizontalPodAutoscalerV2Beta2SpecMetricPodsTarget",
    "HorizontalPodAutoscalerV2Beta2SpecMetricPodsTargetOutputReference",
    "HorizontalPodAutoscalerV2Beta2SpecMetricResource",
    "HorizontalPodAutoscalerV2Beta2SpecMetricResourceOutputReference",
    "HorizontalPodAutoscalerV2Beta2SpecMetricResourceTarget",
    "HorizontalPodAutoscalerV2Beta2SpecMetricResourceTargetOutputReference",
    "HorizontalPodAutoscalerV2Beta2SpecOutputReference",
    "HorizontalPodAutoscalerV2Beta2SpecScaleTargetRef",
    "HorizontalPodAutoscalerV2Beta2SpecScaleTargetRefOutputReference",
]

publication.publish()
