'''
# `kubernetes_pod_security_policy_v1beta1`

Refer to the Terraform Registory for docs: [`kubernetes_pod_security_policy_v1beta1`](https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1).
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


class PodSecurityPolicyV1Beta1(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1 kubernetes_pod_security_policy_v1beta1}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        metadata: typing.Union["PodSecurityPolicyV1Beta1Metadata", typing.Dict[str, typing.Any]],
        spec: typing.Union["PodSecurityPolicyV1Beta1Spec", typing.Dict[str, typing.Any]],
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1 kubernetes_pod_security_policy_v1beta1} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#metadata PodSecurityPolicyV1Beta1#metadata}
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#spec PodSecurityPolicyV1Beta1#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#id PodSecurityPolicyV1Beta1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = PodSecurityPolicyV1Beta1Config(
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
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the podsecuritypolicy that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#annotations PodSecurityPolicyV1Beta1#annotations}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the podsecuritypolicy. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#labels PodSecurityPolicyV1Beta1#labels}
        :param name: Name of the podsecuritypolicy, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#name PodSecurityPolicyV1Beta1#name}
        '''
        value = PodSecurityPolicyV1Beta1Metadata(
            annotations=annotations, labels=labels, name=name
        )

        return typing.cast(None, jsii.invoke(self, "putMetadata", [value]))

    @jsii.member(jsii_name="putSpec")
    def put_spec(
        self,
        *,
        fs_group: typing.Union["PodSecurityPolicyV1Beta1SpecFsGroup", typing.Dict[str, typing.Any]],
        run_as_user: typing.Union["PodSecurityPolicyV1Beta1SpecRunAsUser", typing.Dict[str, typing.Any]],
        supplemental_groups: typing.Union["PodSecurityPolicyV1Beta1SpecSupplementalGroups", typing.Dict[str, typing.Any]],
        allowed_capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_flex_volumes: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes", typing.Dict[str, typing.Any]]]]] = None,
        allowed_host_paths: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecAllowedHostPaths", typing.Dict[str, typing.Any]]]]] = None,
        allowed_proc_mount_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_unsafe_sysctls: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_privilege_escalation: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        default_add_capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        default_allow_privilege_escalation: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        forbidden_sysctls: typing.Optional[typing.Sequence[builtins.str]] = None,
        host_ipc: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        host_network: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        host_pid: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        host_ports: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecHostPorts", typing.Dict[str, typing.Any]]]]] = None,
        privileged: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        read_only_root_filesystem: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        required_drop_capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        run_as_group: typing.Optional[typing.Union["PodSecurityPolicyV1Beta1SpecRunAsGroup", typing.Dict[str, typing.Any]]] = None,
        se_linux: typing.Optional[typing.Union["PodSecurityPolicyV1Beta1SpecSeLinux", typing.Dict[str, typing.Any]]] = None,
        volumes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param fs_group: fs_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#fs_group PodSecurityPolicyV1Beta1#fs_group}
        :param run_as_user: run_as_user block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#run_as_user PodSecurityPolicyV1Beta1#run_as_user}
        :param supplemental_groups: supplemental_groups block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#supplemental_groups PodSecurityPolicyV1Beta1#supplemental_groups}
        :param allowed_capabilities: allowedCapabilities is a list of capabilities that can be requested to add to the container. Capabilities in this field may be added at the pod author's discretion. You must not list a capability in both allowedCapabilities and requiredDropCapabilities. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_capabilities PodSecurityPolicyV1Beta1#allowed_capabilities}
        :param allowed_flex_volumes: allowed_flex_volumes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_flex_volumes PodSecurityPolicyV1Beta1#allowed_flex_volumes}
        :param allowed_host_paths: allowed_host_paths block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_host_paths PodSecurityPolicyV1Beta1#allowed_host_paths}
        :param allowed_proc_mount_types: AllowedProcMountTypes is an allowlist of allowed ProcMountTypes. Empty or nil indicates that only the DefaultProcMountType may be used. This requires the ProcMountType feature flag to be enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_proc_mount_types PodSecurityPolicyV1Beta1#allowed_proc_mount_types}
        :param allowed_unsafe_sysctls: allowedUnsafeSysctls is a list of explicitly allowed unsafe sysctls, defaults to none. Each entry is either a plain sysctl name or ends in "*" in which case it is considered as a prefix of allowed sysctls. Single * means all unsafe sysctls are allowed. Kubelet has to allowlist all allowed unsafe sysctls explicitly to avoid rejection. Examples: e.g. "foo/*" allows "foo/bar", "foo/baz", etc. e.g. "foo.*" allows "foo.bar", "foo.baz", etc. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_unsafe_sysctls PodSecurityPolicyV1Beta1#allowed_unsafe_sysctls}
        :param allow_privilege_escalation: allowPrivilegeEscalation determines if a pod can request to allow privilege escalation. If unspecified, defaults to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allow_privilege_escalation PodSecurityPolicyV1Beta1#allow_privilege_escalation}
        :param default_add_capabilities: defaultAddCapabilities is the default set of capabilities that will be added to the container unless the pod spec specifically drops the capability. You may not list a capability in both defaultAddCapabilities and requiredDropCapabilities. Capabilities added here are implicitly allowed, and need not be included in the allowedCapabilities list. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#default_add_capabilities PodSecurityPolicyV1Beta1#default_add_capabilities}
        :param default_allow_privilege_escalation: defaultAllowPrivilegeEscalation controls the default setting for whether a process can gain more privileges than its parent process. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#default_allow_privilege_escalation PodSecurityPolicyV1Beta1#default_allow_privilege_escalation}
        :param forbidden_sysctls: forbiddenSysctls is a list of explicitly forbidden sysctls, defaults to none. Each entry is either a plain sysctl name or ends in "*" in which case it is considered as a prefix of forbidden sysctls. Single * means all sysctls are forbidden. Examples: e.g. "foo/*" forbids "foo/bar", "foo/baz", etc. e.g. "foo.*" forbids "foo.bar", "foo.baz", etc. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#forbidden_sysctls PodSecurityPolicyV1Beta1#forbidden_sysctls}
        :param host_ipc: hostIPC determines if the policy allows the use of HostIPC in the pod spec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_ipc PodSecurityPolicyV1Beta1#host_ipc}
        :param host_network: hostNetwork determines if the policy allows the use of HostNetwork in the pod spec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_network PodSecurityPolicyV1Beta1#host_network}
        :param host_pid: hostPID determines if the policy allows the use of HostPID in the pod spec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_pid PodSecurityPolicyV1Beta1#host_pid}
        :param host_ports: host_ports block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_ports PodSecurityPolicyV1Beta1#host_ports}
        :param privileged: privileged determines if a pod can request to be run as privileged. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#privileged PodSecurityPolicyV1Beta1#privileged}
        :param read_only_root_filesystem: readOnlyRootFilesystem when set to true will force containers to run with a read only root file system. If the container specifically requests to run with a non-read only root file system the PSP should deny the pod. If set to false the container may run with a read only root file system if it wishes but it will not be forced to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#read_only_root_filesystem PodSecurityPolicyV1Beta1#read_only_root_filesystem}
        :param required_drop_capabilities: requiredDropCapabilities are the capabilities that will be dropped from the container. These are required to be dropped and cannot be added. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#required_drop_capabilities PodSecurityPolicyV1Beta1#required_drop_capabilities}
        :param run_as_group: run_as_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#run_as_group PodSecurityPolicyV1Beta1#run_as_group}
        :param se_linux: se_linux block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#se_linux PodSecurityPolicyV1Beta1#se_linux}
        :param volumes: volumes is an allowlist of volume plugins. Empty indicates that no volumes may be used. To allow all volumes you may use '*'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#volumes PodSecurityPolicyV1Beta1#volumes}
        '''
        value = PodSecurityPolicyV1Beta1Spec(
            fs_group=fs_group,
            run_as_user=run_as_user,
            supplemental_groups=supplemental_groups,
            allowed_capabilities=allowed_capabilities,
            allowed_flex_volumes=allowed_flex_volumes,
            allowed_host_paths=allowed_host_paths,
            allowed_proc_mount_types=allowed_proc_mount_types,
            allowed_unsafe_sysctls=allowed_unsafe_sysctls,
            allow_privilege_escalation=allow_privilege_escalation,
            default_add_capabilities=default_add_capabilities,
            default_allow_privilege_escalation=default_allow_privilege_escalation,
            forbidden_sysctls=forbidden_sysctls,
            host_ipc=host_ipc,
            host_network=host_network,
            host_pid=host_pid,
            host_ports=host_ports,
            privileged=privileged,
            read_only_root_filesystem=read_only_root_filesystem,
            required_drop_capabilities=required_drop_capabilities,
            run_as_group=run_as_group,
            se_linux=se_linux,
            volumes=volumes,
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
    def metadata(self) -> "PodSecurityPolicyV1Beta1MetadataOutputReference":
        return typing.cast("PodSecurityPolicyV1Beta1MetadataOutputReference", jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="spec")
    def spec(self) -> "PodSecurityPolicyV1Beta1SpecOutputReference":
        return typing.cast("PodSecurityPolicyV1Beta1SpecOutputReference", jsii.get(self, "spec"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(self) -> typing.Optional["PodSecurityPolicyV1Beta1Metadata"]:
        return typing.cast(typing.Optional["PodSecurityPolicyV1Beta1Metadata"], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="specInput")
    def spec_input(self) -> typing.Optional["PodSecurityPolicyV1Beta1Spec"]:
        return typing.cast(typing.Optional["PodSecurityPolicyV1Beta1Spec"], jsii.get(self, "specInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1Config",
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
class PodSecurityPolicyV1Beta1Config(cdktf.TerraformMetaArguments):
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
        metadata: typing.Union["PodSecurityPolicyV1Beta1Metadata", typing.Dict[str, typing.Any]],
        spec: typing.Union["PodSecurityPolicyV1Beta1Spec", typing.Dict[str, typing.Any]],
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
        :param metadata: metadata block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#metadata PodSecurityPolicyV1Beta1#metadata}
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#spec PodSecurityPolicyV1Beta1#spec}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#id PodSecurityPolicyV1Beta1#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(metadata, dict):
            metadata = PodSecurityPolicyV1Beta1Metadata(**metadata)
        if isinstance(spec, dict):
            spec = PodSecurityPolicyV1Beta1Spec(**spec)
        if __debug__:
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1Config.__init__)
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
    def metadata(self) -> "PodSecurityPolicyV1Beta1Metadata":
        '''metadata block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#metadata PodSecurityPolicyV1Beta1#metadata}
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast("PodSecurityPolicyV1Beta1Metadata", result)

    @builtins.property
    def spec(self) -> "PodSecurityPolicyV1Beta1Spec":
        '''spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#spec PodSecurityPolicyV1Beta1#spec}
        '''
        result = self._values.get("spec")
        assert result is not None, "Required property 'spec' is missing"
        return typing.cast("PodSecurityPolicyV1Beta1Spec", result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#id PodSecurityPolicyV1Beta1#id}.

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
        return "PodSecurityPolicyV1Beta1Config(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1Metadata",
    jsii_struct_bases=[],
    name_mapping={"annotations": "annotations", "labels": "labels", "name": "name"},
)
class PodSecurityPolicyV1Beta1Metadata:
    def __init__(
        self,
        *,
        annotations: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param annotations: An unstructured key value map stored with the podsecuritypolicy that may be used to store arbitrary metadata. More info: http://kubernetes.io/docs/user-guide/annotations Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#annotations PodSecurityPolicyV1Beta1#annotations}
        :param labels: Map of string keys and values that can be used to organize and categorize (scope and select) the podsecuritypolicy. May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#labels PodSecurityPolicyV1Beta1#labels}
        :param name: Name of the podsecuritypolicy, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#name PodSecurityPolicyV1Beta1#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1Metadata.__init__)
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
        '''An unstructured key value map stored with the podsecuritypolicy that may be used to store arbitrary metadata.

        More info: http://kubernetes.io/docs/user-guide/annotations

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#annotations PodSecurityPolicyV1Beta1#annotations}
        '''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Map of string keys and values that can be used to organize and categorize (scope and select) the podsecuritypolicy.

        May match selectors of replication controllers and services. More info: http://kubernetes.io/docs/user-guide/labels

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#labels PodSecurityPolicyV1Beta1#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name of the podsecuritypolicy, must be unique. Cannot be updated. More info: http://kubernetes.io/docs/user-guide/identifiers#names.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#name PodSecurityPolicyV1Beta1#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1Metadata(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1MetadataOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1MetadataOutputReference",
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
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1MetadataOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1MetadataOutputReference, "annotations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1MetadataOutputReference, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1MetadataOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PodSecurityPolicyV1Beta1Metadata]:
        return typing.cast(typing.Optional[PodSecurityPolicyV1Beta1Metadata], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PodSecurityPolicyV1Beta1Metadata],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1MetadataOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1Spec",
    jsii_struct_bases=[],
    name_mapping={
        "fs_group": "fsGroup",
        "run_as_user": "runAsUser",
        "supplemental_groups": "supplementalGroups",
        "allowed_capabilities": "allowedCapabilities",
        "allowed_flex_volumes": "allowedFlexVolumes",
        "allowed_host_paths": "allowedHostPaths",
        "allowed_proc_mount_types": "allowedProcMountTypes",
        "allowed_unsafe_sysctls": "allowedUnsafeSysctls",
        "allow_privilege_escalation": "allowPrivilegeEscalation",
        "default_add_capabilities": "defaultAddCapabilities",
        "default_allow_privilege_escalation": "defaultAllowPrivilegeEscalation",
        "forbidden_sysctls": "forbiddenSysctls",
        "host_ipc": "hostIpc",
        "host_network": "hostNetwork",
        "host_pid": "hostPid",
        "host_ports": "hostPorts",
        "privileged": "privileged",
        "read_only_root_filesystem": "readOnlyRootFilesystem",
        "required_drop_capabilities": "requiredDropCapabilities",
        "run_as_group": "runAsGroup",
        "se_linux": "seLinux",
        "volumes": "volumes",
    },
)
class PodSecurityPolicyV1Beta1Spec:
    def __init__(
        self,
        *,
        fs_group: typing.Union["PodSecurityPolicyV1Beta1SpecFsGroup", typing.Dict[str, typing.Any]],
        run_as_user: typing.Union["PodSecurityPolicyV1Beta1SpecRunAsUser", typing.Dict[str, typing.Any]],
        supplemental_groups: typing.Union["PodSecurityPolicyV1Beta1SpecSupplementalGroups", typing.Dict[str, typing.Any]],
        allowed_capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_flex_volumes: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes", typing.Dict[str, typing.Any]]]]] = None,
        allowed_host_paths: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecAllowedHostPaths", typing.Dict[str, typing.Any]]]]] = None,
        allowed_proc_mount_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        allowed_unsafe_sysctls: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_privilege_escalation: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        default_add_capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        default_allow_privilege_escalation: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        forbidden_sysctls: typing.Optional[typing.Sequence[builtins.str]] = None,
        host_ipc: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        host_network: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        host_pid: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        host_ports: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecHostPorts", typing.Dict[str, typing.Any]]]]] = None,
        privileged: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        read_only_root_filesystem: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        required_drop_capabilities: typing.Optional[typing.Sequence[builtins.str]] = None,
        run_as_group: typing.Optional[typing.Union["PodSecurityPolicyV1Beta1SpecRunAsGroup", typing.Dict[str, typing.Any]]] = None,
        se_linux: typing.Optional[typing.Union["PodSecurityPolicyV1Beta1SpecSeLinux", typing.Dict[str, typing.Any]]] = None,
        volumes: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param fs_group: fs_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#fs_group PodSecurityPolicyV1Beta1#fs_group}
        :param run_as_user: run_as_user block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#run_as_user PodSecurityPolicyV1Beta1#run_as_user}
        :param supplemental_groups: supplemental_groups block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#supplemental_groups PodSecurityPolicyV1Beta1#supplemental_groups}
        :param allowed_capabilities: allowedCapabilities is a list of capabilities that can be requested to add to the container. Capabilities in this field may be added at the pod author's discretion. You must not list a capability in both allowedCapabilities and requiredDropCapabilities. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_capabilities PodSecurityPolicyV1Beta1#allowed_capabilities}
        :param allowed_flex_volumes: allowed_flex_volumes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_flex_volumes PodSecurityPolicyV1Beta1#allowed_flex_volumes}
        :param allowed_host_paths: allowed_host_paths block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_host_paths PodSecurityPolicyV1Beta1#allowed_host_paths}
        :param allowed_proc_mount_types: AllowedProcMountTypes is an allowlist of allowed ProcMountTypes. Empty or nil indicates that only the DefaultProcMountType may be used. This requires the ProcMountType feature flag to be enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_proc_mount_types PodSecurityPolicyV1Beta1#allowed_proc_mount_types}
        :param allowed_unsafe_sysctls: allowedUnsafeSysctls is a list of explicitly allowed unsafe sysctls, defaults to none. Each entry is either a plain sysctl name or ends in "*" in which case it is considered as a prefix of allowed sysctls. Single * means all unsafe sysctls are allowed. Kubelet has to allowlist all allowed unsafe sysctls explicitly to avoid rejection. Examples: e.g. "foo/*" allows "foo/bar", "foo/baz", etc. e.g. "foo.*" allows "foo.bar", "foo.baz", etc. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_unsafe_sysctls PodSecurityPolicyV1Beta1#allowed_unsafe_sysctls}
        :param allow_privilege_escalation: allowPrivilegeEscalation determines if a pod can request to allow privilege escalation. If unspecified, defaults to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allow_privilege_escalation PodSecurityPolicyV1Beta1#allow_privilege_escalation}
        :param default_add_capabilities: defaultAddCapabilities is the default set of capabilities that will be added to the container unless the pod spec specifically drops the capability. You may not list a capability in both defaultAddCapabilities and requiredDropCapabilities. Capabilities added here are implicitly allowed, and need not be included in the allowedCapabilities list. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#default_add_capabilities PodSecurityPolicyV1Beta1#default_add_capabilities}
        :param default_allow_privilege_escalation: defaultAllowPrivilegeEscalation controls the default setting for whether a process can gain more privileges than its parent process. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#default_allow_privilege_escalation PodSecurityPolicyV1Beta1#default_allow_privilege_escalation}
        :param forbidden_sysctls: forbiddenSysctls is a list of explicitly forbidden sysctls, defaults to none. Each entry is either a plain sysctl name or ends in "*" in which case it is considered as a prefix of forbidden sysctls. Single * means all sysctls are forbidden. Examples: e.g. "foo/*" forbids "foo/bar", "foo/baz", etc. e.g. "foo.*" forbids "foo.bar", "foo.baz", etc. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#forbidden_sysctls PodSecurityPolicyV1Beta1#forbidden_sysctls}
        :param host_ipc: hostIPC determines if the policy allows the use of HostIPC in the pod spec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_ipc PodSecurityPolicyV1Beta1#host_ipc}
        :param host_network: hostNetwork determines if the policy allows the use of HostNetwork in the pod spec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_network PodSecurityPolicyV1Beta1#host_network}
        :param host_pid: hostPID determines if the policy allows the use of HostPID in the pod spec. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_pid PodSecurityPolicyV1Beta1#host_pid}
        :param host_ports: host_ports block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_ports PodSecurityPolicyV1Beta1#host_ports}
        :param privileged: privileged determines if a pod can request to be run as privileged. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#privileged PodSecurityPolicyV1Beta1#privileged}
        :param read_only_root_filesystem: readOnlyRootFilesystem when set to true will force containers to run with a read only root file system. If the container specifically requests to run with a non-read only root file system the PSP should deny the pod. If set to false the container may run with a read only root file system if it wishes but it will not be forced to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#read_only_root_filesystem PodSecurityPolicyV1Beta1#read_only_root_filesystem}
        :param required_drop_capabilities: requiredDropCapabilities are the capabilities that will be dropped from the container. These are required to be dropped and cannot be added. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#required_drop_capabilities PodSecurityPolicyV1Beta1#required_drop_capabilities}
        :param run_as_group: run_as_group block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#run_as_group PodSecurityPolicyV1Beta1#run_as_group}
        :param se_linux: se_linux block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#se_linux PodSecurityPolicyV1Beta1#se_linux}
        :param volumes: volumes is an allowlist of volume plugins. Empty indicates that no volumes may be used. To allow all volumes you may use '*'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#volumes PodSecurityPolicyV1Beta1#volumes}
        '''
        if isinstance(fs_group, dict):
            fs_group = PodSecurityPolicyV1Beta1SpecFsGroup(**fs_group)
        if isinstance(run_as_user, dict):
            run_as_user = PodSecurityPolicyV1Beta1SpecRunAsUser(**run_as_user)
        if isinstance(supplemental_groups, dict):
            supplemental_groups = PodSecurityPolicyV1Beta1SpecSupplementalGroups(**supplemental_groups)
        if isinstance(run_as_group, dict):
            run_as_group = PodSecurityPolicyV1Beta1SpecRunAsGroup(**run_as_group)
        if isinstance(se_linux, dict):
            se_linux = PodSecurityPolicyV1Beta1SpecSeLinux(**se_linux)
        if __debug__:
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1Spec.__init__)
            check_type(argname="argument fs_group", value=fs_group, expected_type=type_hints["fs_group"])
            check_type(argname="argument run_as_user", value=run_as_user, expected_type=type_hints["run_as_user"])
            check_type(argname="argument supplemental_groups", value=supplemental_groups, expected_type=type_hints["supplemental_groups"])
            check_type(argname="argument allowed_capabilities", value=allowed_capabilities, expected_type=type_hints["allowed_capabilities"])
            check_type(argname="argument allowed_flex_volumes", value=allowed_flex_volumes, expected_type=type_hints["allowed_flex_volumes"])
            check_type(argname="argument allowed_host_paths", value=allowed_host_paths, expected_type=type_hints["allowed_host_paths"])
            check_type(argname="argument allowed_proc_mount_types", value=allowed_proc_mount_types, expected_type=type_hints["allowed_proc_mount_types"])
            check_type(argname="argument allowed_unsafe_sysctls", value=allowed_unsafe_sysctls, expected_type=type_hints["allowed_unsafe_sysctls"])
            check_type(argname="argument allow_privilege_escalation", value=allow_privilege_escalation, expected_type=type_hints["allow_privilege_escalation"])
            check_type(argname="argument default_add_capabilities", value=default_add_capabilities, expected_type=type_hints["default_add_capabilities"])
            check_type(argname="argument default_allow_privilege_escalation", value=default_allow_privilege_escalation, expected_type=type_hints["default_allow_privilege_escalation"])
            check_type(argname="argument forbidden_sysctls", value=forbidden_sysctls, expected_type=type_hints["forbidden_sysctls"])
            check_type(argname="argument host_ipc", value=host_ipc, expected_type=type_hints["host_ipc"])
            check_type(argname="argument host_network", value=host_network, expected_type=type_hints["host_network"])
            check_type(argname="argument host_pid", value=host_pid, expected_type=type_hints["host_pid"])
            check_type(argname="argument host_ports", value=host_ports, expected_type=type_hints["host_ports"])
            check_type(argname="argument privileged", value=privileged, expected_type=type_hints["privileged"])
            check_type(argname="argument read_only_root_filesystem", value=read_only_root_filesystem, expected_type=type_hints["read_only_root_filesystem"])
            check_type(argname="argument required_drop_capabilities", value=required_drop_capabilities, expected_type=type_hints["required_drop_capabilities"])
            check_type(argname="argument run_as_group", value=run_as_group, expected_type=type_hints["run_as_group"])
            check_type(argname="argument se_linux", value=se_linux, expected_type=type_hints["se_linux"])
            check_type(argname="argument volumes", value=volumes, expected_type=type_hints["volumes"])
        self._values: typing.Dict[str, typing.Any] = {
            "fs_group": fs_group,
            "run_as_user": run_as_user,
            "supplemental_groups": supplemental_groups,
        }
        if allowed_capabilities is not None:
            self._values["allowed_capabilities"] = allowed_capabilities
        if allowed_flex_volumes is not None:
            self._values["allowed_flex_volumes"] = allowed_flex_volumes
        if allowed_host_paths is not None:
            self._values["allowed_host_paths"] = allowed_host_paths
        if allowed_proc_mount_types is not None:
            self._values["allowed_proc_mount_types"] = allowed_proc_mount_types
        if allowed_unsafe_sysctls is not None:
            self._values["allowed_unsafe_sysctls"] = allowed_unsafe_sysctls
        if allow_privilege_escalation is not None:
            self._values["allow_privilege_escalation"] = allow_privilege_escalation
        if default_add_capabilities is not None:
            self._values["default_add_capabilities"] = default_add_capabilities
        if default_allow_privilege_escalation is not None:
            self._values["default_allow_privilege_escalation"] = default_allow_privilege_escalation
        if forbidden_sysctls is not None:
            self._values["forbidden_sysctls"] = forbidden_sysctls
        if host_ipc is not None:
            self._values["host_ipc"] = host_ipc
        if host_network is not None:
            self._values["host_network"] = host_network
        if host_pid is not None:
            self._values["host_pid"] = host_pid
        if host_ports is not None:
            self._values["host_ports"] = host_ports
        if privileged is not None:
            self._values["privileged"] = privileged
        if read_only_root_filesystem is not None:
            self._values["read_only_root_filesystem"] = read_only_root_filesystem
        if required_drop_capabilities is not None:
            self._values["required_drop_capabilities"] = required_drop_capabilities
        if run_as_group is not None:
            self._values["run_as_group"] = run_as_group
        if se_linux is not None:
            self._values["se_linux"] = se_linux
        if volumes is not None:
            self._values["volumes"] = volumes

    @builtins.property
    def fs_group(self) -> "PodSecurityPolicyV1Beta1SpecFsGroup":
        '''fs_group block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#fs_group PodSecurityPolicyV1Beta1#fs_group}
        '''
        result = self._values.get("fs_group")
        assert result is not None, "Required property 'fs_group' is missing"
        return typing.cast("PodSecurityPolicyV1Beta1SpecFsGroup", result)

    @builtins.property
    def run_as_user(self) -> "PodSecurityPolicyV1Beta1SpecRunAsUser":
        '''run_as_user block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#run_as_user PodSecurityPolicyV1Beta1#run_as_user}
        '''
        result = self._values.get("run_as_user")
        assert result is not None, "Required property 'run_as_user' is missing"
        return typing.cast("PodSecurityPolicyV1Beta1SpecRunAsUser", result)

    @builtins.property
    def supplemental_groups(self) -> "PodSecurityPolicyV1Beta1SpecSupplementalGroups":
        '''supplemental_groups block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#supplemental_groups PodSecurityPolicyV1Beta1#supplemental_groups}
        '''
        result = self._values.get("supplemental_groups")
        assert result is not None, "Required property 'supplemental_groups' is missing"
        return typing.cast("PodSecurityPolicyV1Beta1SpecSupplementalGroups", result)

    @builtins.property
    def allowed_capabilities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''allowedCapabilities is a list of capabilities that can be requested to add to the container.

        Capabilities in this field may be added at the pod author's discretion. You must not list a capability in both allowedCapabilities and requiredDropCapabilities.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_capabilities PodSecurityPolicyV1Beta1#allowed_capabilities}
        '''
        result = self._values.get("allowed_capabilities")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allowed_flex_volumes(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes"]]]:
        '''allowed_flex_volumes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_flex_volumes PodSecurityPolicyV1Beta1#allowed_flex_volumes}
        '''
        result = self._values.get("allowed_flex_volumes")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes"]]], result)

    @builtins.property
    def allowed_host_paths(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecAllowedHostPaths"]]]:
        '''allowed_host_paths block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_host_paths PodSecurityPolicyV1Beta1#allowed_host_paths}
        '''
        result = self._values.get("allowed_host_paths")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecAllowedHostPaths"]]], result)

    @builtins.property
    def allowed_proc_mount_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''AllowedProcMountTypes is an allowlist of allowed ProcMountTypes.

        Empty or nil indicates that only the DefaultProcMountType may be used. This requires the ProcMountType feature flag to be enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_proc_mount_types PodSecurityPolicyV1Beta1#allowed_proc_mount_types}
        '''
        result = self._values.get("allowed_proc_mount_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allowed_unsafe_sysctls(self) -> typing.Optional[typing.List[builtins.str]]:
        '''allowedUnsafeSysctls is a list of explicitly allowed unsafe sysctls, defaults to none.

        Each entry is either a plain sysctl name or ends in "*" in which case it is considered as a prefix of allowed sysctls. Single * means all unsafe sysctls are allowed. Kubelet has to allowlist all allowed unsafe sysctls explicitly to avoid rejection.

        Examples: e.g. "foo/*" allows "foo/bar", "foo/baz", etc. e.g. "foo.*" allows "foo.bar", "foo.baz", etc.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allowed_unsafe_sysctls PodSecurityPolicyV1Beta1#allowed_unsafe_sysctls}
        '''
        result = self._values.get("allowed_unsafe_sysctls")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allow_privilege_escalation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''allowPrivilegeEscalation determines if a pod can request to allow privilege escalation. If unspecified, defaults to true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#allow_privilege_escalation PodSecurityPolicyV1Beta1#allow_privilege_escalation}
        '''
        result = self._values.get("allow_privilege_escalation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def default_add_capabilities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''defaultAddCapabilities is the default set of capabilities that will be added to the container unless the pod spec specifically drops the capability.

        You may not list a capability in both defaultAddCapabilities and requiredDropCapabilities. Capabilities added here are implicitly allowed, and need not be included in the allowedCapabilities list.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#default_add_capabilities PodSecurityPolicyV1Beta1#default_add_capabilities}
        '''
        result = self._values.get("default_add_capabilities")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def default_allow_privilege_escalation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''defaultAllowPrivilegeEscalation controls the default setting for whether a process can gain more privileges than its parent process.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#default_allow_privilege_escalation PodSecurityPolicyV1Beta1#default_allow_privilege_escalation}
        '''
        result = self._values.get("default_allow_privilege_escalation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def forbidden_sysctls(self) -> typing.Optional[typing.List[builtins.str]]:
        '''forbiddenSysctls is a list of explicitly forbidden sysctls, defaults to none.

        Each entry is either a plain sysctl name or ends in "*" in which case it is considered as a prefix of forbidden sysctls. Single * means all sysctls are forbidden.

        Examples: e.g. "foo/*" forbids "foo/bar", "foo/baz", etc. e.g. "foo.*" forbids "foo.bar", "foo.baz", etc.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#forbidden_sysctls PodSecurityPolicyV1Beta1#forbidden_sysctls}
        '''
        result = self._values.get("forbidden_sysctls")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def host_ipc(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''hostIPC determines if the policy allows the use of HostIPC in the pod spec.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_ipc PodSecurityPolicyV1Beta1#host_ipc}
        '''
        result = self._values.get("host_ipc")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def host_network(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''hostNetwork determines if the policy allows the use of HostNetwork in the pod spec.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_network PodSecurityPolicyV1Beta1#host_network}
        '''
        result = self._values.get("host_network")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def host_pid(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''hostPID determines if the policy allows the use of HostPID in the pod spec.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_pid PodSecurityPolicyV1Beta1#host_pid}
        '''
        result = self._values.get("host_pid")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def host_ports(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecHostPorts"]]]:
        '''host_ports block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#host_ports PodSecurityPolicyV1Beta1#host_ports}
        '''
        result = self._values.get("host_ports")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecHostPorts"]]], result)

    @builtins.property
    def privileged(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''privileged determines if a pod can request to be run as privileged.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#privileged PodSecurityPolicyV1Beta1#privileged}
        '''
        result = self._values.get("privileged")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def read_only_root_filesystem(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''readOnlyRootFilesystem when set to true will force containers to run with a read only root file system.

        If the container specifically requests to run with a non-read only root file system the PSP should deny the pod. If set to false the container may run with a read only root file system if it wishes but it will not be forced to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#read_only_root_filesystem PodSecurityPolicyV1Beta1#read_only_root_filesystem}
        '''
        result = self._values.get("read_only_root_filesystem")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def required_drop_capabilities(self) -> typing.Optional[typing.List[builtins.str]]:
        '''requiredDropCapabilities are the capabilities that will be dropped from the container.

        These are required to be dropped and cannot be added.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#required_drop_capabilities PodSecurityPolicyV1Beta1#required_drop_capabilities}
        '''
        result = self._values.get("required_drop_capabilities")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def run_as_group(self) -> typing.Optional["PodSecurityPolicyV1Beta1SpecRunAsGroup"]:
        '''run_as_group block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#run_as_group PodSecurityPolicyV1Beta1#run_as_group}
        '''
        result = self._values.get("run_as_group")
        return typing.cast(typing.Optional["PodSecurityPolicyV1Beta1SpecRunAsGroup"], result)

    @builtins.property
    def se_linux(self) -> typing.Optional["PodSecurityPolicyV1Beta1SpecSeLinux"]:
        '''se_linux block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#se_linux PodSecurityPolicyV1Beta1#se_linux}
        '''
        result = self._values.get("se_linux")
        return typing.cast(typing.Optional["PodSecurityPolicyV1Beta1SpecSeLinux"], result)

    @builtins.property
    def volumes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''volumes is an allowlist of volume plugins.

        Empty indicates that no volumes may be used. To allow all volumes you may use '*'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#volumes PodSecurityPolicyV1Beta1#volumes}
        '''
        result = self._values.get("volumes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1Spec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes",
    jsii_struct_bases=[],
    name_mapping={"driver": "driver"},
)
class PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes:
    def __init__(self, *, driver: builtins.str) -> None:
        '''
        :param driver: driver is the name of the Flexvolume driver. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#driver PodSecurityPolicyV1Beta1#driver}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes.__init__)
            check_type(argname="argument driver", value=driver, expected_type=type_hints["driver"])
        self._values: typing.Dict[str, typing.Any] = {
            "driver": driver,
        }

    @builtins.property
    def driver(self) -> builtins.str:
        '''driver is the name of the Flexvolume driver.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#driver PodSecurityPolicyV1Beta1#driver}
        '''
        result = self._values.get("driver")
        assert result is not None, "Required property 'driver' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesList",
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
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesOutputReference",
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
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="driverInput")
    def driver_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "driverInput"))

    @builtins.property
    @jsii.member(jsii_name="driver")
    def driver(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "driver"))

    @driver.setter
    def driver(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesOutputReference, "driver").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driver", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecAllowedHostPaths",
    jsii_struct_bases=[],
    name_mapping={"path_prefix": "pathPrefix", "read_only": "readOnly"},
)
class PodSecurityPolicyV1Beta1SpecAllowedHostPaths:
    def __init__(
        self,
        *,
        path_prefix: builtins.str,
        read_only: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param path_prefix: pathPrefix is the path prefix that the host volume must match. It does not support ``*``. Trailing slashes are trimmed when validating the path prefix with a host path. Examples: ``/foo`` would allow ``/foo``, ``/foo/`` and ``/foo/bar`` ``/foo`` would not allow ``/food`` or ``/etc/foo`` Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#path_prefix PodSecurityPolicyV1Beta1#path_prefix}
        :param read_only: when set to true, will allow host volumes matching the pathPrefix only if all volume mounts are readOnly. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#read_only PodSecurityPolicyV1Beta1#read_only}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecAllowedHostPaths.__init__)
            check_type(argname="argument path_prefix", value=path_prefix, expected_type=type_hints["path_prefix"])
            check_type(argname="argument read_only", value=read_only, expected_type=type_hints["read_only"])
        self._values: typing.Dict[str, typing.Any] = {
            "path_prefix": path_prefix,
        }
        if read_only is not None:
            self._values["read_only"] = read_only

    @builtins.property
    def path_prefix(self) -> builtins.str:
        '''pathPrefix is the path prefix that the host volume must match.

        It does not support ``*``. Trailing slashes are trimmed when validating the path prefix with a host path.

        Examples: ``/foo`` would allow ``/foo``, ``/foo/`` and ``/foo/bar`` ``/foo`` would not allow ``/food`` or ``/etc/foo``

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#path_prefix PodSecurityPolicyV1Beta1#path_prefix}
        '''
        result = self._values.get("path_prefix")
        assert result is not None, "Required property 'path_prefix' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def read_only(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''when set to true, will allow host volumes matching the pathPrefix only if all volume mounts are readOnly.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#read_only PodSecurityPolicyV1Beta1#read_only}
        '''
        result = self._values.get("read_only")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecAllowedHostPaths(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecAllowedHostPathsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecAllowedHostPathsList",
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
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecAllowedHostPathsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PodSecurityPolicyV1Beta1SpecAllowedHostPathsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecAllowedHostPathsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PodSecurityPolicyV1Beta1SpecAllowedHostPathsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecAllowedHostPathsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecAllowedHostPathsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecAllowedHostPathsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecAllowedHostPaths]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecAllowedHostPaths]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecAllowedHostPaths]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecAllowedHostPathsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PodSecurityPolicyV1Beta1SpecAllowedHostPathsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecAllowedHostPathsOutputReference",
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
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecAllowedHostPathsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetReadOnly")
    def reset_read_only(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnly", []))

    @builtins.property
    @jsii.member(jsii_name="pathPrefixInput")
    def path_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyInput")
    def read_only_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "readOnlyInput"))

    @builtins.property
    @jsii.member(jsii_name="pathPrefix")
    def path_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pathPrefix"))

    @path_prefix.setter
    def path_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecAllowedHostPathsOutputReference, "path_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pathPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="readOnly")
    def read_only(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "readOnly"))

    @read_only.setter
    def read_only(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecAllowedHostPathsOutputReference, "read_only").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnly", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedHostPaths, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedHostPaths, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedHostPaths, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecAllowedHostPathsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecFsGroup",
    jsii_struct_bases=[],
    name_mapping={"rule": "rule", "range": "range"},
)
class PodSecurityPolicyV1Beta1SpecFsGroup:
    def __init__(
        self,
        *,
        rule: builtins.str,
        range: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecFsGroupRange", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param rule: rule is the strategy that will dictate what FSGroup is used in the SecurityContext. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecFsGroup.__init__)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument range", value=range, expected_type=type_hints["range"])
        self._values: typing.Dict[str, typing.Any] = {
            "rule": rule,
        }
        if range is not None:
            self._values["range"] = range

    @builtins.property
    def rule(self) -> builtins.str:
        '''rule is the strategy that will dictate what FSGroup is used in the SecurityContext.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def range(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecFsGroupRange"]]]:
        '''range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        result = self._values.get("range")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecFsGroupRange"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecFsGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecFsGroupOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecFsGroupOutputReference",
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
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecFsGroupOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRange")
    def put_range(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecFsGroupRange", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecFsGroupOutputReference.put_range)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRange", [value]))

    @jsii.member(jsii_name="resetRange")
    def reset_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRange", []))

    @builtins.property
    @jsii.member(jsii_name="range")
    def range(self) -> "PodSecurityPolicyV1Beta1SpecFsGroupRangeList":
        return typing.cast("PodSecurityPolicyV1Beta1SpecFsGroupRangeList", jsii.get(self, "range"))

    @builtins.property
    @jsii.member(jsii_name="rangeInput")
    def range_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecFsGroupRange"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecFsGroupRange"]]], jsii.get(self, "rangeInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rule"))

    @rule.setter
    def rule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecFsGroupOutputReference, "rule").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PodSecurityPolicyV1Beta1SpecFsGroup]:
        return typing.cast(typing.Optional[PodSecurityPolicyV1Beta1SpecFsGroup], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PodSecurityPolicyV1Beta1SpecFsGroup],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecFsGroupOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecFsGroupRange",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class PodSecurityPolicyV1Beta1SpecFsGroupRange:
    def __init__(self, *, max: jsii.Number, min: jsii.Number) -> None:
        '''
        :param max: max is the end of the range, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#max PodSecurityPolicyV1Beta1#max}
        :param min: min is the start of the range, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#min PodSecurityPolicyV1Beta1#min}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecFsGroupRange.__init__)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[str, typing.Any] = {
            "max": max,
            "min": min,
        }

    @builtins.property
    def max(self) -> jsii.Number:
        '''max is the end of the range, inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#max PodSecurityPolicyV1Beta1#max}
        '''
        result = self._values.get("max")
        assert result is not None, "Required property 'max' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min(self) -> jsii.Number:
        '''min is the start of the range, inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#min PodSecurityPolicyV1Beta1#min}
        '''
        result = self._values.get("min")
        assert result is not None, "Required property 'min' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecFsGroupRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecFsGroupRangeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecFsGroupRangeList",
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
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecFsGroupRangeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PodSecurityPolicyV1Beta1SpecFsGroupRangeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecFsGroupRangeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PodSecurityPolicyV1Beta1SpecFsGroupRangeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecFsGroupRangeList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecFsGroupRangeList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecFsGroupRangeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecFsGroupRange]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecFsGroupRange]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecFsGroupRange]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecFsGroupRangeList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PodSecurityPolicyV1Beta1SpecFsGroupRangeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecFsGroupRangeOutputReference",
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
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecFsGroupRangeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecFsGroupRangeOutputReference, "max").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecFsGroupRangeOutputReference, "min").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecFsGroupRange, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecFsGroupRange, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecFsGroupRange, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecFsGroupRangeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecHostPorts",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class PodSecurityPolicyV1Beta1SpecHostPorts:
    def __init__(self, *, max: jsii.Number, min: jsii.Number) -> None:
        '''
        :param max: max is the end of the range, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#max PodSecurityPolicyV1Beta1#max}
        :param min: min is the start of the range, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#min PodSecurityPolicyV1Beta1#min}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecHostPorts.__init__)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[str, typing.Any] = {
            "max": max,
            "min": min,
        }

    @builtins.property
    def max(self) -> jsii.Number:
        '''max is the end of the range, inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#max PodSecurityPolicyV1Beta1#max}
        '''
        result = self._values.get("max")
        assert result is not None, "Required property 'max' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min(self) -> jsii.Number:
        '''min is the start of the range, inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#min PodSecurityPolicyV1Beta1#min}
        '''
        result = self._values.get("min")
        assert result is not None, "Required property 'min' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecHostPorts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecHostPortsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecHostPortsList",
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
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecHostPortsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PodSecurityPolicyV1Beta1SpecHostPortsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecHostPortsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PodSecurityPolicyV1Beta1SpecHostPortsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecHostPortsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecHostPortsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecHostPortsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecHostPorts]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecHostPorts]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecHostPorts]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecHostPortsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PodSecurityPolicyV1Beta1SpecHostPortsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecHostPortsOutputReference",
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
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecHostPortsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecHostPortsOutputReference, "max").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecHostPortsOutputReference, "min").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecHostPorts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecHostPorts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecHostPorts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecHostPortsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PodSecurityPolicyV1Beta1SpecOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecOutputReference",
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
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAllowedFlexVolumes")
    def put_allowed_flex_volumes(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecOutputReference.put_allowed_flex_volumes)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAllowedFlexVolumes", [value]))

    @jsii.member(jsii_name="putAllowedHostPaths")
    def put_allowed_host_paths(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecAllowedHostPaths, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecOutputReference.put_allowed_host_paths)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAllowedHostPaths", [value]))

    @jsii.member(jsii_name="putFsGroup")
    def put_fs_group(
        self,
        *,
        rule: builtins.str,
        range: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecFsGroupRange, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param rule: rule is the strategy that will dictate what FSGroup is used in the SecurityContext. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        value = PodSecurityPolicyV1Beta1SpecFsGroup(rule=rule, range=range)

        return typing.cast(None, jsii.invoke(self, "putFsGroup", [value]))

    @jsii.member(jsii_name="putHostPorts")
    def put_host_ports(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[PodSecurityPolicyV1Beta1SpecHostPorts, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecOutputReference.put_host_ports)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putHostPorts", [value]))

    @jsii.member(jsii_name="putRunAsGroup")
    def put_run_as_group(
        self,
        *,
        rule: builtins.str,
        range: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecRunAsGroupRange", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param rule: rule is the strategy that will dictate the allowable RunAsGroup values that may be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        value = PodSecurityPolicyV1Beta1SpecRunAsGroup(rule=rule, range=range)

        return typing.cast(None, jsii.invoke(self, "putRunAsGroup", [value]))

    @jsii.member(jsii_name="putRunAsUser")
    def put_run_as_user(
        self,
        *,
        rule: builtins.str,
        range: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecRunAsUserRange", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param rule: rule is the strategy that will dictate the allowable RunAsUser values that may be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        value = PodSecurityPolicyV1Beta1SpecRunAsUser(rule=rule, range=range)

        return typing.cast(None, jsii.invoke(self, "putRunAsUser", [value]))

    @jsii.member(jsii_name="putSeLinux")
    def put_se_linux(
        self,
        *,
        rule: builtins.str,
        se_linux_options: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param rule: rule is the strategy that will dictate the allowable labels that may be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        :param se_linux_options: se_linux_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#se_linux_options PodSecurityPolicyV1Beta1#se_linux_options}
        '''
        value = PodSecurityPolicyV1Beta1SpecSeLinux(
            rule=rule, se_linux_options=se_linux_options
        )

        return typing.cast(None, jsii.invoke(self, "putSeLinux", [value]))

    @jsii.member(jsii_name="putSupplementalGroups")
    def put_supplemental_groups(
        self,
        *,
        rule: builtins.str,
        range: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param rule: rule is the strategy that will dictate what supplemental groups is used in the SecurityContext. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        value = PodSecurityPolicyV1Beta1SpecSupplementalGroups(rule=rule, range=range)

        return typing.cast(None, jsii.invoke(self, "putSupplementalGroups", [value]))

    @jsii.member(jsii_name="resetAllowedCapabilities")
    def reset_allowed_capabilities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedCapabilities", []))

    @jsii.member(jsii_name="resetAllowedFlexVolumes")
    def reset_allowed_flex_volumes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedFlexVolumes", []))

    @jsii.member(jsii_name="resetAllowedHostPaths")
    def reset_allowed_host_paths(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedHostPaths", []))

    @jsii.member(jsii_name="resetAllowedProcMountTypes")
    def reset_allowed_proc_mount_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedProcMountTypes", []))

    @jsii.member(jsii_name="resetAllowedUnsafeSysctls")
    def reset_allowed_unsafe_sysctls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowedUnsafeSysctls", []))

    @jsii.member(jsii_name="resetAllowPrivilegeEscalation")
    def reset_allow_privilege_escalation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowPrivilegeEscalation", []))

    @jsii.member(jsii_name="resetDefaultAddCapabilities")
    def reset_default_add_capabilities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultAddCapabilities", []))

    @jsii.member(jsii_name="resetDefaultAllowPrivilegeEscalation")
    def reset_default_allow_privilege_escalation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultAllowPrivilegeEscalation", []))

    @jsii.member(jsii_name="resetForbiddenSysctls")
    def reset_forbidden_sysctls(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForbiddenSysctls", []))

    @jsii.member(jsii_name="resetHostIpc")
    def reset_host_ipc(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostIpc", []))

    @jsii.member(jsii_name="resetHostNetwork")
    def reset_host_network(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostNetwork", []))

    @jsii.member(jsii_name="resetHostPid")
    def reset_host_pid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostPid", []))

    @jsii.member(jsii_name="resetHostPorts")
    def reset_host_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHostPorts", []))

    @jsii.member(jsii_name="resetPrivileged")
    def reset_privileged(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivileged", []))

    @jsii.member(jsii_name="resetReadOnlyRootFilesystem")
    def reset_read_only_root_filesystem(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReadOnlyRootFilesystem", []))

    @jsii.member(jsii_name="resetRequiredDropCapabilities")
    def reset_required_drop_capabilities(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequiredDropCapabilities", []))

    @jsii.member(jsii_name="resetRunAsGroup")
    def reset_run_as_group(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRunAsGroup", []))

    @jsii.member(jsii_name="resetSeLinux")
    def reset_se_linux(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSeLinux", []))

    @jsii.member(jsii_name="resetVolumes")
    def reset_volumes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVolumes", []))

    @builtins.property
    @jsii.member(jsii_name="allowedFlexVolumes")
    def allowed_flex_volumes(
        self,
    ) -> PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesList:
        return typing.cast(PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesList, jsii.get(self, "allowedFlexVolumes"))

    @builtins.property
    @jsii.member(jsii_name="allowedHostPaths")
    def allowed_host_paths(self) -> PodSecurityPolicyV1Beta1SpecAllowedHostPathsList:
        return typing.cast(PodSecurityPolicyV1Beta1SpecAllowedHostPathsList, jsii.get(self, "allowedHostPaths"))

    @builtins.property
    @jsii.member(jsii_name="fsGroup")
    def fs_group(self) -> PodSecurityPolicyV1Beta1SpecFsGroupOutputReference:
        return typing.cast(PodSecurityPolicyV1Beta1SpecFsGroupOutputReference, jsii.get(self, "fsGroup"))

    @builtins.property
    @jsii.member(jsii_name="hostPorts")
    def host_ports(self) -> PodSecurityPolicyV1Beta1SpecHostPortsList:
        return typing.cast(PodSecurityPolicyV1Beta1SpecHostPortsList, jsii.get(self, "hostPorts"))

    @builtins.property
    @jsii.member(jsii_name="runAsGroup")
    def run_as_group(self) -> "PodSecurityPolicyV1Beta1SpecRunAsGroupOutputReference":
        return typing.cast("PodSecurityPolicyV1Beta1SpecRunAsGroupOutputReference", jsii.get(self, "runAsGroup"))

    @builtins.property
    @jsii.member(jsii_name="runAsUser")
    def run_as_user(self) -> "PodSecurityPolicyV1Beta1SpecRunAsUserOutputReference":
        return typing.cast("PodSecurityPolicyV1Beta1SpecRunAsUserOutputReference", jsii.get(self, "runAsUser"))

    @builtins.property
    @jsii.member(jsii_name="seLinux")
    def se_linux(self) -> "PodSecurityPolicyV1Beta1SpecSeLinuxOutputReference":
        return typing.cast("PodSecurityPolicyV1Beta1SpecSeLinuxOutputReference", jsii.get(self, "seLinux"))

    @builtins.property
    @jsii.member(jsii_name="supplementalGroups")
    def supplemental_groups(
        self,
    ) -> "PodSecurityPolicyV1Beta1SpecSupplementalGroupsOutputReference":
        return typing.cast("PodSecurityPolicyV1Beta1SpecSupplementalGroupsOutputReference", jsii.get(self, "supplementalGroups"))

    @builtins.property
    @jsii.member(jsii_name="allowedCapabilitiesInput")
    def allowed_capabilities_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedCapabilitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedFlexVolumesInput")
    def allowed_flex_volumes_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes]]], jsii.get(self, "allowedFlexVolumesInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedHostPathsInput")
    def allowed_host_paths_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecAllowedHostPaths]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecAllowedHostPaths]]], jsii.get(self, "allowedHostPathsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedProcMountTypesInput")
    def allowed_proc_mount_types_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedProcMountTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedUnsafeSysctlsInput")
    def allowed_unsafe_sysctls_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowedUnsafeSysctlsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowPrivilegeEscalationInput")
    def allow_privilege_escalation_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowPrivilegeEscalationInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultAddCapabilitiesInput")
    def default_add_capabilities_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "defaultAddCapabilitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultAllowPrivilegeEscalationInput")
    def default_allow_privilege_escalation_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "defaultAllowPrivilegeEscalationInput"))

    @builtins.property
    @jsii.member(jsii_name="forbiddenSysctlsInput")
    def forbidden_sysctls_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "forbiddenSysctlsInput"))

    @builtins.property
    @jsii.member(jsii_name="fsGroupInput")
    def fs_group_input(self) -> typing.Optional[PodSecurityPolicyV1Beta1SpecFsGroup]:
        return typing.cast(typing.Optional[PodSecurityPolicyV1Beta1SpecFsGroup], jsii.get(self, "fsGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="hostIpcInput")
    def host_ipc_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "hostIpcInput"))

    @builtins.property
    @jsii.member(jsii_name="hostNetworkInput")
    def host_network_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "hostNetworkInput"))

    @builtins.property
    @jsii.member(jsii_name="hostPidInput")
    def host_pid_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "hostPidInput"))

    @builtins.property
    @jsii.member(jsii_name="hostPortsInput")
    def host_ports_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecHostPorts]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecHostPorts]]], jsii.get(self, "hostPortsInput"))

    @builtins.property
    @jsii.member(jsii_name="privilegedInput")
    def privileged_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "privilegedInput"))

    @builtins.property
    @jsii.member(jsii_name="readOnlyRootFilesystemInput")
    def read_only_root_filesystem_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "readOnlyRootFilesystemInput"))

    @builtins.property
    @jsii.member(jsii_name="requiredDropCapabilitiesInput")
    def required_drop_capabilities_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "requiredDropCapabilitiesInput"))

    @builtins.property
    @jsii.member(jsii_name="runAsGroupInput")
    def run_as_group_input(
        self,
    ) -> typing.Optional["PodSecurityPolicyV1Beta1SpecRunAsGroup"]:
        return typing.cast(typing.Optional["PodSecurityPolicyV1Beta1SpecRunAsGroup"], jsii.get(self, "runAsGroupInput"))

    @builtins.property
    @jsii.member(jsii_name="runAsUserInput")
    def run_as_user_input(
        self,
    ) -> typing.Optional["PodSecurityPolicyV1Beta1SpecRunAsUser"]:
        return typing.cast(typing.Optional["PodSecurityPolicyV1Beta1SpecRunAsUser"], jsii.get(self, "runAsUserInput"))

    @builtins.property
    @jsii.member(jsii_name="seLinuxInput")
    def se_linux_input(self) -> typing.Optional["PodSecurityPolicyV1Beta1SpecSeLinux"]:
        return typing.cast(typing.Optional["PodSecurityPolicyV1Beta1SpecSeLinux"], jsii.get(self, "seLinuxInput"))

    @builtins.property
    @jsii.member(jsii_name="supplementalGroupsInput")
    def supplemental_groups_input(
        self,
    ) -> typing.Optional["PodSecurityPolicyV1Beta1SpecSupplementalGroups"]:
        return typing.cast(typing.Optional["PodSecurityPolicyV1Beta1SpecSupplementalGroups"], jsii.get(self, "supplementalGroupsInput"))

    @builtins.property
    @jsii.member(jsii_name="volumesInput")
    def volumes_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "volumesInput"))

    @builtins.property
    @jsii.member(jsii_name="allowedCapabilities")
    def allowed_capabilities(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedCapabilities"))

    @allowed_capabilities.setter
    def allowed_capabilities(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecOutputReference, "allowed_capabilities").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedCapabilities", value)

    @builtins.property
    @jsii.member(jsii_name="allowedProcMountTypes")
    def allowed_proc_mount_types(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedProcMountTypes"))

    @allowed_proc_mount_types.setter
    def allowed_proc_mount_types(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecOutputReference, "allowed_proc_mount_types").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedProcMountTypes", value)

    @builtins.property
    @jsii.member(jsii_name="allowedUnsafeSysctls")
    def allowed_unsafe_sysctls(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowedUnsafeSysctls"))

    @allowed_unsafe_sysctls.setter
    def allowed_unsafe_sysctls(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecOutputReference, "allowed_unsafe_sysctls").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowedUnsafeSysctls", value)

    @builtins.property
    @jsii.member(jsii_name="allowPrivilegeEscalation")
    def allow_privilege_escalation(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowPrivilegeEscalation"))

    @allow_privilege_escalation.setter
    def allow_privilege_escalation(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecOutputReference, "allow_privilege_escalation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowPrivilegeEscalation", value)

    @builtins.property
    @jsii.member(jsii_name="defaultAddCapabilities")
    def default_add_capabilities(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "defaultAddCapabilities"))

    @default_add_capabilities.setter
    def default_add_capabilities(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecOutputReference, "default_add_capabilities").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultAddCapabilities", value)

    @builtins.property
    @jsii.member(jsii_name="defaultAllowPrivilegeEscalation")
    def default_allow_privilege_escalation(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "defaultAllowPrivilegeEscalation"))

    @default_allow_privilege_escalation.setter
    def default_allow_privilege_escalation(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecOutputReference, "default_allow_privilege_escalation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultAllowPrivilegeEscalation", value)

    @builtins.property
    @jsii.member(jsii_name="forbiddenSysctls")
    def forbidden_sysctls(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "forbiddenSysctls"))

    @forbidden_sysctls.setter
    def forbidden_sysctls(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecOutputReference, "forbidden_sysctls").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forbiddenSysctls", value)

    @builtins.property
    @jsii.member(jsii_name="hostIpc")
    def host_ipc(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "hostIpc"))

    @host_ipc.setter
    def host_ipc(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecOutputReference, "host_ipc").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostIpc", value)

    @builtins.property
    @jsii.member(jsii_name="hostNetwork")
    def host_network(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "hostNetwork"))

    @host_network.setter
    def host_network(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecOutputReference, "host_network").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostNetwork", value)

    @builtins.property
    @jsii.member(jsii_name="hostPid")
    def host_pid(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "hostPid"))

    @host_pid.setter
    def host_pid(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecOutputReference, "host_pid").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostPid", value)

    @builtins.property
    @jsii.member(jsii_name="privileged")
    def privileged(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "privileged"))

    @privileged.setter
    def privileged(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecOutputReference, "privileged").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privileged", value)

    @builtins.property
    @jsii.member(jsii_name="readOnlyRootFilesystem")
    def read_only_root_filesystem(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "readOnlyRootFilesystem"))

    @read_only_root_filesystem.setter
    def read_only_root_filesystem(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecOutputReference, "read_only_root_filesystem").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "readOnlyRootFilesystem", value)

    @builtins.property
    @jsii.member(jsii_name="requiredDropCapabilities")
    def required_drop_capabilities(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "requiredDropCapabilities"))

    @required_drop_capabilities.setter
    def required_drop_capabilities(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecOutputReference, "required_drop_capabilities").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requiredDropCapabilities", value)

    @builtins.property
    @jsii.member(jsii_name="volumes")
    def volumes(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "volumes"))

    @volumes.setter
    def volumes(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecOutputReference, "volumes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "volumes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PodSecurityPolicyV1Beta1Spec]:
        return typing.cast(typing.Optional[PodSecurityPolicyV1Beta1Spec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PodSecurityPolicyV1Beta1Spec],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecRunAsGroup",
    jsii_struct_bases=[],
    name_mapping={"rule": "rule", "range": "range"},
)
class PodSecurityPolicyV1Beta1SpecRunAsGroup:
    def __init__(
        self,
        *,
        rule: builtins.str,
        range: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecRunAsGroupRange", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param rule: rule is the strategy that will dictate the allowable RunAsGroup values that may be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecRunAsGroup.__init__)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument range", value=range, expected_type=type_hints["range"])
        self._values: typing.Dict[str, typing.Any] = {
            "rule": rule,
        }
        if range is not None:
            self._values["range"] = range

    @builtins.property
    def rule(self) -> builtins.str:
        '''rule is the strategy that will dictate the allowable RunAsGroup values that may be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def range(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecRunAsGroupRange"]]]:
        '''range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        result = self._values.get("range")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecRunAsGroupRange"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecRunAsGroup(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecRunAsGroupOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecRunAsGroupOutputReference",
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
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecRunAsGroupOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRange")
    def put_range(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecRunAsGroupRange", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecRunAsGroupOutputReference.put_range)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRange", [value]))

    @jsii.member(jsii_name="resetRange")
    def reset_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRange", []))

    @builtins.property
    @jsii.member(jsii_name="range")
    def range(self) -> "PodSecurityPolicyV1Beta1SpecRunAsGroupRangeList":
        return typing.cast("PodSecurityPolicyV1Beta1SpecRunAsGroupRangeList", jsii.get(self, "range"))

    @builtins.property
    @jsii.member(jsii_name="rangeInput")
    def range_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecRunAsGroupRange"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecRunAsGroupRange"]]], jsii.get(self, "rangeInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rule"))

    @rule.setter
    def rule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecRunAsGroupOutputReference, "rule").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PodSecurityPolicyV1Beta1SpecRunAsGroup]:
        return typing.cast(typing.Optional[PodSecurityPolicyV1Beta1SpecRunAsGroup], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PodSecurityPolicyV1Beta1SpecRunAsGroup],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecRunAsGroupOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecRunAsGroupRange",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class PodSecurityPolicyV1Beta1SpecRunAsGroupRange:
    def __init__(self, *, max: jsii.Number, min: jsii.Number) -> None:
        '''
        :param max: max is the end of the range, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#max PodSecurityPolicyV1Beta1#max}
        :param min: min is the start of the range, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#min PodSecurityPolicyV1Beta1#min}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecRunAsGroupRange.__init__)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[str, typing.Any] = {
            "max": max,
            "min": min,
        }

    @builtins.property
    def max(self) -> jsii.Number:
        '''max is the end of the range, inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#max PodSecurityPolicyV1Beta1#max}
        '''
        result = self._values.get("max")
        assert result is not None, "Required property 'max' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min(self) -> jsii.Number:
        '''min is the start of the range, inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#min PodSecurityPolicyV1Beta1#min}
        '''
        result = self._values.get("min")
        assert result is not None, "Required property 'min' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecRunAsGroupRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecRunAsGroupRangeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecRunAsGroupRangeList",
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
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecRunAsGroupRangeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PodSecurityPolicyV1Beta1SpecRunAsGroupRangeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecRunAsGroupRangeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PodSecurityPolicyV1Beta1SpecRunAsGroupRangeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecRunAsGroupRangeList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecRunAsGroupRangeList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecRunAsGroupRangeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecRunAsGroupRange]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecRunAsGroupRange]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecRunAsGroupRange]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecRunAsGroupRangeList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PodSecurityPolicyV1Beta1SpecRunAsGroupRangeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecRunAsGroupRangeOutputReference",
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
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecRunAsGroupRangeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecRunAsGroupRangeOutputReference, "max").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecRunAsGroupRangeOutputReference, "min").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecRunAsGroupRange, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecRunAsGroupRange, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecRunAsGroupRange, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecRunAsGroupRangeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecRunAsUser",
    jsii_struct_bases=[],
    name_mapping={"rule": "rule", "range": "range"},
)
class PodSecurityPolicyV1Beta1SpecRunAsUser:
    def __init__(
        self,
        *,
        rule: builtins.str,
        range: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecRunAsUserRange", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param rule: rule is the strategy that will dictate the allowable RunAsUser values that may be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecRunAsUser.__init__)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument range", value=range, expected_type=type_hints["range"])
        self._values: typing.Dict[str, typing.Any] = {
            "rule": rule,
        }
        if range is not None:
            self._values["range"] = range

    @builtins.property
    def rule(self) -> builtins.str:
        '''rule is the strategy that will dictate the allowable RunAsUser values that may be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def range(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecRunAsUserRange"]]]:
        '''range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        result = self._values.get("range")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecRunAsUserRange"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecRunAsUser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecRunAsUserOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecRunAsUserOutputReference",
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
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecRunAsUserOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRange")
    def put_range(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecRunAsUserRange", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecRunAsUserOutputReference.put_range)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRange", [value]))

    @jsii.member(jsii_name="resetRange")
    def reset_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRange", []))

    @builtins.property
    @jsii.member(jsii_name="range")
    def range(self) -> "PodSecurityPolicyV1Beta1SpecRunAsUserRangeList":
        return typing.cast("PodSecurityPolicyV1Beta1SpecRunAsUserRangeList", jsii.get(self, "range"))

    @builtins.property
    @jsii.member(jsii_name="rangeInput")
    def range_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecRunAsUserRange"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecRunAsUserRange"]]], jsii.get(self, "rangeInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rule"))

    @rule.setter
    def rule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecRunAsUserOutputReference, "rule").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PodSecurityPolicyV1Beta1SpecRunAsUser]:
        return typing.cast(typing.Optional[PodSecurityPolicyV1Beta1SpecRunAsUser], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PodSecurityPolicyV1Beta1SpecRunAsUser],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecRunAsUserOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecRunAsUserRange",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class PodSecurityPolicyV1Beta1SpecRunAsUserRange:
    def __init__(self, *, max: jsii.Number, min: jsii.Number) -> None:
        '''
        :param max: max is the end of the range, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#max PodSecurityPolicyV1Beta1#max}
        :param min: min is the start of the range, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#min PodSecurityPolicyV1Beta1#min}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecRunAsUserRange.__init__)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[str, typing.Any] = {
            "max": max,
            "min": min,
        }

    @builtins.property
    def max(self) -> jsii.Number:
        '''max is the end of the range, inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#max PodSecurityPolicyV1Beta1#max}
        '''
        result = self._values.get("max")
        assert result is not None, "Required property 'max' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min(self) -> jsii.Number:
        '''min is the start of the range, inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#min PodSecurityPolicyV1Beta1#min}
        '''
        result = self._values.get("min")
        assert result is not None, "Required property 'min' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecRunAsUserRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecRunAsUserRangeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecRunAsUserRangeList",
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
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecRunAsUserRangeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PodSecurityPolicyV1Beta1SpecRunAsUserRangeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecRunAsUserRangeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PodSecurityPolicyV1Beta1SpecRunAsUserRangeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecRunAsUserRangeList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecRunAsUserRangeList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecRunAsUserRangeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecRunAsUserRange]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecRunAsUserRange]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecRunAsUserRange]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecRunAsUserRangeList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PodSecurityPolicyV1Beta1SpecRunAsUserRangeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecRunAsUserRangeOutputReference",
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
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecRunAsUserRangeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecRunAsUserRangeOutputReference, "max").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecRunAsUserRangeOutputReference, "min").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecRunAsUserRange, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecRunAsUserRange, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecRunAsUserRange, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecRunAsUserRangeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecSeLinux",
    jsii_struct_bases=[],
    name_mapping={"rule": "rule", "se_linux_options": "seLinuxOptions"},
)
class PodSecurityPolicyV1Beta1SpecSeLinux:
    def __init__(
        self,
        *,
        rule: builtins.str,
        se_linux_options: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param rule: rule is the strategy that will dictate the allowable labels that may be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        :param se_linux_options: se_linux_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#se_linux_options PodSecurityPolicyV1Beta1#se_linux_options}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecSeLinux.__init__)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument se_linux_options", value=se_linux_options, expected_type=type_hints["se_linux_options"])
        self._values: typing.Dict[str, typing.Any] = {
            "rule": rule,
        }
        if se_linux_options is not None:
            self._values["se_linux_options"] = se_linux_options

    @builtins.property
    def rule(self) -> builtins.str:
        '''rule is the strategy that will dictate the allowable labels that may be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def se_linux_options(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions"]]]:
        '''se_linux_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#se_linux_options PodSecurityPolicyV1Beta1#se_linux_options}
        '''
        result = self._values.get("se_linux_options")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecSeLinux(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecSeLinuxOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecSeLinuxOutputReference",
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
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecSeLinuxOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSeLinuxOptions")
    def put_se_linux_options(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecSeLinuxOutputReference.put_se_linux_options)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSeLinuxOptions", [value]))

    @jsii.member(jsii_name="resetSeLinuxOptions")
    def reset_se_linux_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSeLinuxOptions", []))

    @builtins.property
    @jsii.member(jsii_name="seLinuxOptions")
    def se_linux_options(
        self,
    ) -> "PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsList":
        return typing.cast("PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsList", jsii.get(self, "seLinuxOptions"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="seLinuxOptionsInput")
    def se_linux_options_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions"]]], jsii.get(self, "seLinuxOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rule"))

    @rule.setter
    def rule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecSeLinuxOutputReference, "rule").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PodSecurityPolicyV1Beta1SpecSeLinux]:
        return typing.cast(typing.Optional[PodSecurityPolicyV1Beta1SpecSeLinux], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PodSecurityPolicyV1Beta1SpecSeLinux],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecSeLinuxOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions",
    jsii_struct_bases=[],
    name_mapping={"level": "level", "role": "role", "type": "type", "user": "user"},
)
class PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions:
    def __init__(
        self,
        *,
        level: builtins.str,
        role: builtins.str,
        type: builtins.str,
        user: builtins.str,
    ) -> None:
        '''
        :param level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#level PodSecurityPolicyV1Beta1#level}.
        :param role: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#role PodSecurityPolicyV1Beta1#role}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#type PodSecurityPolicyV1Beta1#type}.
        :param user: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#user PodSecurityPolicyV1Beta1#user}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions.__init__)
            check_type(argname="argument level", value=level, expected_type=type_hints["level"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument user", value=user, expected_type=type_hints["user"])
        self._values: typing.Dict[str, typing.Any] = {
            "level": level,
            "role": role,
            "type": type,
            "user": user,
        }

    @builtins.property
    def level(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#level PodSecurityPolicyV1Beta1#level}.'''
        result = self._values.get("level")
        assert result is not None, "Required property 'level' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#role PodSecurityPolicyV1Beta1#role}.'''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#type PodSecurityPolicyV1Beta1#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#user PodSecurityPolicyV1Beta1#user}.'''
        result = self._values.get("user")
        assert result is not None, "Required property 'user' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsList",
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
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsOutputReference",
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
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="levelInput")
    def level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "levelInput"))

    @builtins.property
    @jsii.member(jsii_name="roleInput")
    def role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="userInput")
    def user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userInput"))

    @builtins.property
    @jsii.member(jsii_name="level")
    def level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "level"))

    @level.setter
    def level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsOutputReference, "level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "level", value)

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsOutputReference, "role").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="user")
    def user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "user"))

    @user.setter
    def user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsOutputReference, "user").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "user", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecSupplementalGroups",
    jsii_struct_bases=[],
    name_mapping={"rule": "rule", "range": "range"},
)
class PodSecurityPolicyV1Beta1SpecSupplementalGroups:
    def __init__(
        self,
        *,
        rule: builtins.str,
        range: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param rule: rule is the strategy that will dictate what supplemental groups is used in the SecurityContext. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecSupplementalGroups.__init__)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument range", value=range, expected_type=type_hints["range"])
        self._values: typing.Dict[str, typing.Any] = {
            "rule": rule,
        }
        if range is not None:
            self._values["range"] = range

    @builtins.property
    def rule(self) -> builtins.str:
        '''rule is the strategy that will dictate what supplemental groups is used in the SecurityContext.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#rule PodSecurityPolicyV1Beta1#rule}
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def range(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange"]]]:
        '''range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#range PodSecurityPolicyV1Beta1#range}
        '''
        result = self._values.get("range")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecSupplementalGroups(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecSupplementalGroupsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecSupplementalGroupsOutputReference",
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
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecSupplementalGroupsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRange")
    def put_range(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecSupplementalGroupsOutputReference.put_range)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRange", [value]))

    @jsii.member(jsii_name="resetRange")
    def reset_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRange", []))

    @builtins.property
    @jsii.member(jsii_name="range")
    def range(self) -> "PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeList":
        return typing.cast("PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeList", jsii.get(self, "range"))

    @builtins.property
    @jsii.member(jsii_name="rangeInput")
    def range_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange"]]], jsii.get(self, "rangeInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rule"))

    @rule.setter
    def rule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecSupplementalGroupsOutputReference, "rule").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[PodSecurityPolicyV1Beta1SpecSupplementalGroups]:
        return typing.cast(typing.Optional[PodSecurityPolicyV1Beta1SpecSupplementalGroups], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[PodSecurityPolicyV1Beta1SpecSupplementalGroups],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecSupplementalGroupsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange",
    jsii_struct_bases=[],
    name_mapping={"max": "max", "min": "min"},
)
class PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange:
    def __init__(self, *, max: jsii.Number, min: jsii.Number) -> None:
        '''
        :param max: max is the end of the range, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#max PodSecurityPolicyV1Beta1#max}
        :param min: min is the start of the range, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#min PodSecurityPolicyV1Beta1#min}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange.__init__)
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
        self._values: typing.Dict[str, typing.Any] = {
            "max": max,
            "min": min,
        }

    @builtins.property
    def max(self) -> jsii.Number:
        '''max is the end of the range, inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#max PodSecurityPolicyV1Beta1#max}
        '''
        result = self._values.get("max")
        assert result is not None, "Required property 'max' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def min(self) -> jsii.Number:
        '''min is the start of the range, inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/kubernetes/r/pod_security_policy_v1beta1#min PodSecurityPolicyV1Beta1#min}
        '''
        result = self._values.get("min")
        assert result is not None, "Required property 'min' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeList",
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
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-kubernetes.podSecurityPolicyV1Beta1.PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeOutputReference",
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
            type_hints = typing.get_type_hints(PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="maxInput")
    def max_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxInput"))

    @builtins.property
    @jsii.member(jsii_name="minInput")
    def min_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minInput"))

    @builtins.property
    @jsii.member(jsii_name="max")
    def max(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "max"))

    @max.setter
    def max(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeOutputReference, "max").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "max", value)

    @builtins.property
    @jsii.member(jsii_name="min")
    def min(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "min"))

    @min.setter
    def min(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeOutputReference, "min").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "min", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "PodSecurityPolicyV1Beta1",
    "PodSecurityPolicyV1Beta1Config",
    "PodSecurityPolicyV1Beta1Metadata",
    "PodSecurityPolicyV1Beta1MetadataOutputReference",
    "PodSecurityPolicyV1Beta1Spec",
    "PodSecurityPolicyV1Beta1SpecAllowedFlexVolumes",
    "PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesList",
    "PodSecurityPolicyV1Beta1SpecAllowedFlexVolumesOutputReference",
    "PodSecurityPolicyV1Beta1SpecAllowedHostPaths",
    "PodSecurityPolicyV1Beta1SpecAllowedHostPathsList",
    "PodSecurityPolicyV1Beta1SpecAllowedHostPathsOutputReference",
    "PodSecurityPolicyV1Beta1SpecFsGroup",
    "PodSecurityPolicyV1Beta1SpecFsGroupOutputReference",
    "PodSecurityPolicyV1Beta1SpecFsGroupRange",
    "PodSecurityPolicyV1Beta1SpecFsGroupRangeList",
    "PodSecurityPolicyV1Beta1SpecFsGroupRangeOutputReference",
    "PodSecurityPolicyV1Beta1SpecHostPorts",
    "PodSecurityPolicyV1Beta1SpecHostPortsList",
    "PodSecurityPolicyV1Beta1SpecHostPortsOutputReference",
    "PodSecurityPolicyV1Beta1SpecOutputReference",
    "PodSecurityPolicyV1Beta1SpecRunAsGroup",
    "PodSecurityPolicyV1Beta1SpecRunAsGroupOutputReference",
    "PodSecurityPolicyV1Beta1SpecRunAsGroupRange",
    "PodSecurityPolicyV1Beta1SpecRunAsGroupRangeList",
    "PodSecurityPolicyV1Beta1SpecRunAsGroupRangeOutputReference",
    "PodSecurityPolicyV1Beta1SpecRunAsUser",
    "PodSecurityPolicyV1Beta1SpecRunAsUserOutputReference",
    "PodSecurityPolicyV1Beta1SpecRunAsUserRange",
    "PodSecurityPolicyV1Beta1SpecRunAsUserRangeList",
    "PodSecurityPolicyV1Beta1SpecRunAsUserRangeOutputReference",
    "PodSecurityPolicyV1Beta1SpecSeLinux",
    "PodSecurityPolicyV1Beta1SpecSeLinuxOutputReference",
    "PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptions",
    "PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsList",
    "PodSecurityPolicyV1Beta1SpecSeLinuxSeLinuxOptionsOutputReference",
    "PodSecurityPolicyV1Beta1SpecSupplementalGroups",
    "PodSecurityPolicyV1Beta1SpecSupplementalGroupsOutputReference",
    "PodSecurityPolicyV1Beta1SpecSupplementalGroupsRange",
    "PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeList",
    "PodSecurityPolicyV1Beta1SpecSupplementalGroupsRangeOutputReference",
]

publication.publish()
