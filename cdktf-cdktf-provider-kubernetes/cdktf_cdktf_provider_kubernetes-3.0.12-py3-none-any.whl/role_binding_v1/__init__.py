'''
# `kubernetes_role_binding_v1`

Refer to the Terraform Registory for docs: [`kubernetes_role_binding_v1`](https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1).
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


class RoleBindingV1(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.roleBindingV1.RoleBindingV1",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1 kubernetes_role_binding_v1}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        metadata: typing.Union["RoleBindingV1Metadata", typing.Dict[str, typing.Any]],
        role_ref: typing.Union["RoleBindingV1RoleRef", typing.Dict[str, typing.Any]],
        subject: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["RoleBindingV1Subject", typing.Dict[str, typing.Any]]]],
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1 kubernetes_role_binding_v1} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#metadata RoleBindingV1#metadata}
        :param role_ref: role_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#role_ref RoleBindingV1#role_ref}
        :param subject: subject block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#subject RoleBindingV1#subject}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#id RoleBindingV1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RoleBindingV1.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = RoleBindingV1Config(
            metadata=metadata,
            role_ref=role_ref,
            subject=subject,
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
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the roleBinding that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#annotations RoleBindingV1#annotations}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the roleBinding. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#labels RoleBindingV1#labels}
        :param name: Name of the roleBinding, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#name RoleBindingV1#name}
        :param namespace: Namespace defines the space within which name of the roleBinding must be unique. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#namespace RoleBindingV1#namespace}
        '''
        value = RoleBindingV1Metadata(
            annotations=annotations, labels=labels, name=name, namespace=namespace
        )

        return typing.cast(None, jsii.invoke(self, "putMetadata", [value]))

    @jsii.member(jsii_name="putRoleRef")
    def put_role_ref(
        self,
        *,
        api_group: builtins.str,
        kind: builtins.str,
        name: builtins.str,
    ) -> None:
        '''
        :param api_group: The API group of the user. The only value possible at the moment is ``rbac.authorization.k8s.io``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#api_group RoleBindingV1#api_group}
        :param kind: The kind of resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#kind RoleBindingV1#kind}
        :param name: The name of the User to bind to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#name RoleBindingV1#name}
        '''
        value = RoleBindingV1RoleRef(api_group=api_group, kind=kind, name=name)

        return typing.cast(None, jsii.invoke(self, "putRoleRef", [value]))

    @jsii.member(jsii_name="putSubject")
    def put_subject(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["RoleBindingV1Subject", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RoleBindingV1.put_subject)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSubject", [value]))

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
    def metadata(self) -> "RoleBindingV1MetadataOutputReference":
        return typing.cast("RoleBindingV1MetadataOutputReference", jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="roleRef")
    def role_ref(self) -> "RoleBindingV1RoleRefOutputReference":
        return typing.cast("RoleBindingV1RoleRefOutputReference", jsii.get(self, "roleRef"))

    @builtins.property
    @jsii.member(jsii_name="subject")
    def subject(self) -> "RoleBindingV1SubjectList":
        return typing.cast("RoleBindingV1SubjectList", jsii.get(self, "subject"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(self) -> typing.Optional["RoleBindingV1Metadata"]:
        return typing.cast(typing.Optional["RoleBindingV1Metadata"], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="roleRefInput")
    def role_ref_input(self) -> typing.Optional["RoleBindingV1RoleRef"]:
        return typing.cast(typing.Optional["RoleBindingV1RoleRef"], jsii.get(self, "roleRefInput"))

    @builtins.property
    @jsii.member(jsii_name="subjectInput")
    def subject_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RoleBindingV1Subject"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["RoleBindingV1Subject"]]], jsii.get(self, "subjectInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RoleBindingV1, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.roleBindingV1.RoleBindingV1Config",
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
        "role_ref": "roleRef",
        "subject": "subject",
        "id": "id",
    },
)
class RoleBindingV1Config(cdktf.TerraformMetaArguments):
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
        metadata: typing.Union["RoleBindingV1Metadata", typing.Dict[str, typing.Any]],
        role_ref: typing.Union["RoleBindingV1RoleRef", typing.Dict[str, typing.Any]],
        subject: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["RoleBindingV1Subject", typing.Dict[str, typing.Any]]]],
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
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#metadata RoleBindingV1#metadata}
        :param role_ref: role_ref block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#role_ref RoleBindingV1#role_ref}
        :param subject: subject block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#subject RoleBindingV1#subject}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#id RoleBindingV1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(metadata, dict):
            metadata = RoleBindingV1Metadata(**metadata)
        if isinstance(role_ref, dict):
            role_ref = RoleBindingV1RoleRef(**role_ref)
        if __debug__:
            type_hints = typing.get_type_hints(RoleBindingV1Config.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument role_ref", value=role_ref, expected_type=type_hints["role_ref"])
            check_type(argname="argument subject", value=subject, expected_type=type_hints["subject"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "metadata": metadata,
            "role_ref": role_ref,
            "subject": subject,
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
    def metadata(self) -> "RoleBindingV1Metadata":
        '''metadata block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#metadata RoleBindingV1#metadata}
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast("RoleBindingV1Metadata", result)

    @builtins.property
    def role_ref(self) -> "RoleBindingV1RoleRef":
        '''role_ref block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#role_ref RoleBindingV1#role_ref}
        '''
        result = self._values.get("role_ref")
        assert result is not None, "Required property 'role_ref' is missing"
        return typing.cast("RoleBindingV1RoleRef", result)

    @builtins.property
    def subject(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["RoleBindingV1Subject"]]:
        '''subject block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#subject RoleBindingV1#subject}
        '''
        result = self._values.get("subject")
        assert result is not None, "Required property 'subject' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["RoleBindingV1Subject"]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#id RoleBindingV1#id}.

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
        return "RoleBindingV1Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.roleBindingV1.RoleBindingV1Metadata",
    jsii_struct_bases=[],
    name_mapping={
        "annotations": "annotations",
        "labels": "labels",
        "name": "name",
        "namespace": "namespace",
    },
)
class RoleBindingV1Metadata:
    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the roleBinding that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#annotations RoleBindingV1#annotations}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the roleBinding. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#labels RoleBindingV1#labels}
        :param name: Name of the roleBinding, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#name RoleBindingV1#name}
        :param namespace: Namespace defines the space within which name of the roleBinding must be unique. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#namespace RoleBindingV1#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RoleBindingV1Metadata.__init__)
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[str, typing.Any] = {}
        if annotations is not None:
            self._values["annotations"] = annotations
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
        '''An unstructured key value map stored with the roleBinding that may be used to store arbitrary metadata.

        More info: http://kubernetes.io/docs/user-guide/annotations

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#annotations RoleBindingV1#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of string keys and values that can be used to organize and categorize (scope and select) the roleBinding.

        May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#labels RoleBindingV1#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the roleBinding, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#name RoleBindingV1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Namespace defines the space within which name of the roleBinding must be unique.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#namespace RoleBindingV1#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RoleBindingV1Metadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RoleBindingV1MetadataOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.roleBindingV1.RoleBindingV1MetadataOutputReference",
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
            type_hints = typing.get_type_hints(RoleBindingV1MetadataOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(RoleBindingV1MetadataOutputReference, "annotations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RoleBindingV1MetadataOutputReference, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RoleBindingV1MetadataOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RoleBindingV1MetadataOutputReference, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RoleBindingV1Metadata]:
        return typing.cast(typing.Optional[RoleBindingV1Metadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[RoleBindingV1Metadata]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RoleBindingV1MetadataOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.roleBindingV1.RoleBindingV1RoleRef",
    jsii_struct_bases=[],
    name_mapping={"api_group": "apiGroup", "kind": "kind", "name": "name"},
)
class RoleBindingV1RoleRef:
    def __init__(
        self,
        *,
        api_group: builtins.str,
        kind: builtins.str,
        name: builtins.str,
    ) -> None:
        '''
        :param api_group: The API group of the user. The only value possible at the moment is ``rbac.authorization.k8s.io``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#api_group RoleBindingV1#api_group}
        :param kind: The kind of resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#kind RoleBindingV1#kind}
        :param name: The name of the User to bind to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#name RoleBindingV1#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RoleBindingV1RoleRef.__init__)
            check_type(argname="argument api_group", value=api_group, expected_type=type_hints["api_group"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "api_group": api_group,
            "kind": kind,
            "name": name,
        }

    @builtins.property
    def api_group(self) -> builtins.str:
        '''The API group of the user. The only value possible at the moment is ``rbac.authorization.k8s.io``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#api_group RoleBindingV1#api_group}
        '''
        result = self._values.get("api_group")
        assert result is not None, "Required property 'api_group' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kind(self) -> builtins.str:
        '''The kind of resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#kind RoleBindingV1#kind}
        '''
        result = self._values.get("kind")
        assert result is not None, "Required property 'kind' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the User to bind to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#name RoleBindingV1#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RoleBindingV1RoleRef(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RoleBindingV1RoleRefOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.roleBindingV1.RoleBindingV1RoleRefOutputReference",
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
            type_hints = typing.get_type_hints(RoleBindingV1RoleRefOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="apiGroupInput")
    def api_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="apiGroup")
    def api_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiGroup"))

    @api_group.setter
    def api_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RoleBindingV1RoleRefOutputReference, "api_group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiGroup", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RoleBindingV1RoleRefOutputReference, "kind").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RoleBindingV1RoleRefOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RoleBindingV1RoleRef]:
        return typing.cast(typing.Optional[RoleBindingV1RoleRef], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[RoleBindingV1RoleRef]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RoleBindingV1RoleRefOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.roleBindingV1.RoleBindingV1Subject",
    jsii_struct_bases=[],
    name_mapping={
        "kind": "kind",
        "name": "name",
        "api_group": "apiGroup",
        "namespace": "namespace",
    },
)
class RoleBindingV1Subject:
    def __init__(
        self,
        *,
        kind: builtins.str,
        name: builtins.str,
        api_group: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param kind: The kind of resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#kind RoleBindingV1#kind}
        :param name: The name of the resource to bind to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#name RoleBindingV1#name}
        :param api_group: The API group of the subject resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#api_group RoleBindingV1#api_group}
        :param namespace: The Namespace of the subject resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#namespace RoleBindingV1#namespace}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RoleBindingV1Subject.__init__)
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument api_group", value=api_group, expected_type=type_hints["api_group"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[str, typing.Any] = {
            "kind": kind,
            "name": name,
        }
        if api_group is not None:
            self._values["api_group"] = api_group
        if namespace is not None:
            self._values["namespace"] = namespace

    @builtins.property
    def kind(self) -> builtins.str:
        '''The kind of resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#kind RoleBindingV1#kind}
        '''
        result = self._values.get("kind")
        assert result is not None, "Required property 'kind' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the resource to bind to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#name RoleBindingV1#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_group(self) -> typing.Optional[builtins.str]:
        '''The API group of the subject resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#api_group RoleBindingV1#api_group}
        '''
        result = self._values.get("api_group")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''The Namespace of the subject resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/role_binding_v1#namespace RoleBindingV1#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RoleBindingV1Subject(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RoleBindingV1SubjectList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.roleBindingV1.RoleBindingV1SubjectList",
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
            type_hints = typing.get_type_hints(RoleBindingV1SubjectList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "RoleBindingV1SubjectOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RoleBindingV1SubjectList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("RoleBindingV1SubjectOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RoleBindingV1SubjectList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(RoleBindingV1SubjectList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(RoleBindingV1SubjectList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RoleBindingV1Subject]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RoleBindingV1Subject]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[RoleBindingV1Subject]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RoleBindingV1SubjectList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class RoleBindingV1SubjectOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.roleBindingV1.RoleBindingV1SubjectOutputReference",
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
            type_hints = typing.get_type_hints(RoleBindingV1SubjectOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetApiGroup")
    def reset_api_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetApiGroup", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @builtins.property
    @jsii.member(jsii_name="apiGroupInput")
    def api_group_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="apiGroup")
    def api_group(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiGroup"))

    @api_group.setter
    def api_group(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RoleBindingV1SubjectOutputReference, "api_group").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiGroup", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RoleBindingV1SubjectOutputReference, "kind").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RoleBindingV1SubjectOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RoleBindingV1SubjectOutputReference, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[RoleBindingV1Subject, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[RoleBindingV1Subject, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[RoleBindingV1Subject, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RoleBindingV1SubjectOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "RoleBindingV1",
    "RoleBindingV1Config",
    "RoleBindingV1Metadata",
    "RoleBindingV1MetadataOutputReference",
    "RoleBindingV1RoleRef",
    "RoleBindingV1RoleRefOutputReference",
    "RoleBindingV1Subject",
    "RoleBindingV1SubjectList",
    "RoleBindingV1SubjectOutputReference",
]

publication.publish()
