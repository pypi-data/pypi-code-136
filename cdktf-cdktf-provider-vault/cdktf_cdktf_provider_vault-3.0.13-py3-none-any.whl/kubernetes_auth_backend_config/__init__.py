'''
# `vault_kubernetes_auth_backend_config`

Refer to the Terraform Registory for docs: [`vault_kubernetes_auth_backend_config`](https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_config).
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


class KubernetesAuthBackendConfig(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.kubernetesAuthBackendConfig.KubernetesAuthBackendConfig",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_config vault_kubernetes_auth_backend_config}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        kubernetes_host: builtins.str,
        backend: typing.Optional[builtins.str] = None,
        disable_iss_validation: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        disable_local_ca_jwt: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        issuer: typing.Optional[builtins.str] = None,
        kubernetes_ca_cert: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        pem_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        token_reviewer_jwt: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_config vault_kubernetes_auth_backend_config} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param kubernetes_host: Host must be a host string, a host:port pair, or a URL to the base of the Kubernetes API server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_config#kubernetes_host KubernetesAuthBackendConfig#kubernetes_host}
        :param backend: Unique name of the kubernetes backend to configure. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_config#backend KubernetesAuthBackendConfig#backend}
        :param disable_iss_validation: Optional disable JWT issuer validation. Allows to skip ISS validation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_config#disable_iss_validation KubernetesAuthBackendConfig#disable_iss_validation}
        :param disable_local_ca_jwt: Optional disable defaulting to the local CA cert and service account JWT when running in a Kubernetes pod. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_config#disable_local_ca_jwt KubernetesAuthBackendConfig#disable_local_ca_jwt}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_config#id KubernetesAuthBackendConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param issuer: Optional JWT issuer. If no issuer is specified, kubernetes.io/serviceaccount will be used as the default issuer. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_config#issuer KubernetesAuthBackendConfig#issuer}
        :param kubernetes_ca_cert: PEM encoded CA cert for use by the TLS client used to talk with the Kubernetes API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_config#kubernetes_ca_cert KubernetesAuthBackendConfig#kubernetes_ca_cert}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_config#namespace KubernetesAuthBackendConfig#namespace}
        :param pem_keys: Optional list of PEM-formatted public keys or certificates used to verify the signatures of Kubernetes service account JWTs. If a certificate is given, its public key will be extracted. Not every installation of Kubernetes exposes these keys. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_config#pem_keys KubernetesAuthBackendConfig#pem_keys}
        :param token_reviewer_jwt: A service account JWT used to access the TokenReview API to validate other JWTs during login. If not set the JWT used for login will be used to access the API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_config#token_reviewer_jwt KubernetesAuthBackendConfig#token_reviewer_jwt}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesAuthBackendConfig.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = KubernetesAuthBackendConfigConfig(
            kubernetes_host=kubernetes_host,
            backend=backend,
            disable_iss_validation=disable_iss_validation,
            disable_local_ca_jwt=disable_local_ca_jwt,
            id=id,
            issuer=issuer,
            kubernetes_ca_cert=kubernetes_ca_cert,
            namespace=namespace,
            pem_keys=pem_keys,
            token_reviewer_jwt=token_reviewer_jwt,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="resetBackend")
    def reset_backend(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackend", []))

    @jsii.member(jsii_name="resetDisableIssValidation")
    def reset_disable_iss_validation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableIssValidation", []))

    @jsii.member(jsii_name="resetDisableLocalCaJwt")
    def reset_disable_local_ca_jwt(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisableLocalCaJwt", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIssuer")
    def reset_issuer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIssuer", []))

    @jsii.member(jsii_name="resetKubernetesCaCert")
    def reset_kubernetes_ca_cert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKubernetesCaCert", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetPemKeys")
    def reset_pem_keys(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPemKeys", []))

    @jsii.member(jsii_name="resetTokenReviewerJwt")
    def reset_token_reviewer_jwt(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenReviewerJwt", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="backendInput")
    def backend_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendInput"))

    @builtins.property
    @jsii.member(jsii_name="disableIssValidationInput")
    def disable_iss_validation_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableIssValidationInput"))

    @builtins.property
    @jsii.member(jsii_name="disableLocalCaJwtInput")
    def disable_local_ca_jwt_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disableLocalCaJwtInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="issuerInput")
    def issuer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "issuerInput"))

    @builtins.property
    @jsii.member(jsii_name="kubernetesCaCertInput")
    def kubernetes_ca_cert_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kubernetesCaCertInput"))

    @builtins.property
    @jsii.member(jsii_name="kubernetesHostInput")
    def kubernetes_host_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kubernetesHostInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="pemKeysInput")
    def pem_keys_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "pemKeysInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenReviewerJwtInput")
    def token_reviewer_jwt_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenReviewerJwtInput"))

    @builtins.property
    @jsii.member(jsii_name="backend")
    def backend(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backend"))

    @backend.setter
    def backend(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesAuthBackendConfig, "backend").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backend", value)

    @builtins.property
    @jsii.member(jsii_name="disableIssValidation")
    def disable_iss_validation(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disableIssValidation"))

    @disable_iss_validation.setter
    def disable_iss_validation(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesAuthBackendConfig, "disable_iss_validation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableIssValidation", value)

    @builtins.property
    @jsii.member(jsii_name="disableLocalCaJwt")
    def disable_local_ca_jwt(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disableLocalCaJwt"))

    @disable_local_ca_jwt.setter
    def disable_local_ca_jwt(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesAuthBackendConfig, "disable_local_ca_jwt").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableLocalCaJwt", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesAuthBackendConfig, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="issuer")
    def issuer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issuer"))

    @issuer.setter
    def issuer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesAuthBackendConfig, "issuer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "issuer", value)

    @builtins.property
    @jsii.member(jsii_name="kubernetesCaCert")
    def kubernetes_ca_cert(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kubernetesCaCert"))

    @kubernetes_ca_cert.setter
    def kubernetes_ca_cert(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesAuthBackendConfig, "kubernetes_ca_cert").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kubernetesCaCert", value)

    @builtins.property
    @jsii.member(jsii_name="kubernetesHost")
    def kubernetes_host(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kubernetesHost"))

    @kubernetes_host.setter
    def kubernetes_host(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesAuthBackendConfig, "kubernetes_host").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kubernetesHost", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesAuthBackendConfig, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="pemKeys")
    def pem_keys(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "pemKeys"))

    @pem_keys.setter
    def pem_keys(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesAuthBackendConfig, "pem_keys").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pemKeys", value)

    @builtins.property
    @jsii.member(jsii_name="tokenReviewerJwt")
    def token_reviewer_jwt(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenReviewerJwt"))

    @token_reviewer_jwt.setter
    def token_reviewer_jwt(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(KubernetesAuthBackendConfig, "token_reviewer_jwt").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenReviewerJwt", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.kubernetesAuthBackendConfig.KubernetesAuthBackendConfigConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "kubernetes_host": "kubernetesHost",
        "backend": "backend",
        "disable_iss_validation": "disableIssValidation",
        "disable_local_ca_jwt": "disableLocalCaJwt",
        "id": "id",
        "issuer": "issuer",
        "kubernetes_ca_cert": "kubernetesCaCert",
        "namespace": "namespace",
        "pem_keys": "pemKeys",
        "token_reviewer_jwt": "tokenReviewerJwt",
    },
)
class KubernetesAuthBackendConfigConfig(cdktf.TerraformMetaArguments):
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
        kubernetes_host: builtins.str,
        backend: typing.Optional[builtins.str] = None,
        disable_iss_validation: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        disable_local_ca_jwt: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        issuer: typing.Optional[builtins.str] = None,
        kubernetes_ca_cert: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        pem_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        token_reviewer_jwt: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param kubernetes_host: Host must be a host string, a host:port pair, or a URL to the base of the Kubernetes API server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_config#kubernetes_host KubernetesAuthBackendConfig#kubernetes_host}
        :param backend: Unique name of the kubernetes backend to configure. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_config#backend KubernetesAuthBackendConfig#backend}
        :param disable_iss_validation: Optional disable JWT issuer validation. Allows to skip ISS validation. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_config#disable_iss_validation KubernetesAuthBackendConfig#disable_iss_validation}
        :param disable_local_ca_jwt: Optional disable defaulting to the local CA cert and service account JWT when running in a Kubernetes pod. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_config#disable_local_ca_jwt KubernetesAuthBackendConfig#disable_local_ca_jwt}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_config#id KubernetesAuthBackendConfig#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param issuer: Optional JWT issuer. If no issuer is specified, kubernetes.io/serviceaccount will be used as the default issuer. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_config#issuer KubernetesAuthBackendConfig#issuer}
        :param kubernetes_ca_cert: PEM encoded CA cert for use by the TLS client used to talk with the Kubernetes API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_config#kubernetes_ca_cert KubernetesAuthBackendConfig#kubernetes_ca_cert}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_config#namespace KubernetesAuthBackendConfig#namespace}
        :param pem_keys: Optional list of PEM-formatted public keys or certificates used to verify the signatures of Kubernetes service account JWTs. If a certificate is given, its public key will be extracted. Not every installation of Kubernetes exposes these keys. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_config#pem_keys KubernetesAuthBackendConfig#pem_keys}
        :param token_reviewer_jwt: A service account JWT used to access the TokenReview API to validate other JWTs during login. If not set the JWT used for login will be used to access the API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_config#token_reviewer_jwt KubernetesAuthBackendConfig#token_reviewer_jwt}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(KubernetesAuthBackendConfigConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument kubernetes_host", value=kubernetes_host, expected_type=type_hints["kubernetes_host"])
            check_type(argname="argument backend", value=backend, expected_type=type_hints["backend"])
            check_type(argname="argument disable_iss_validation", value=disable_iss_validation, expected_type=type_hints["disable_iss_validation"])
            check_type(argname="argument disable_local_ca_jwt", value=disable_local_ca_jwt, expected_type=type_hints["disable_local_ca_jwt"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument issuer", value=issuer, expected_type=type_hints["issuer"])
            check_type(argname="argument kubernetes_ca_cert", value=kubernetes_ca_cert, expected_type=type_hints["kubernetes_ca_cert"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument pem_keys", value=pem_keys, expected_type=type_hints["pem_keys"])
            check_type(argname="argument token_reviewer_jwt", value=token_reviewer_jwt, expected_type=type_hints["token_reviewer_jwt"])
        self._values: typing.Dict[str, typing.Any] = {
            "kubernetes_host": kubernetes_host,
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
        if backend is not None:
            self._values["backend"] = backend
        if disable_iss_validation is not None:
            self._values["disable_iss_validation"] = disable_iss_validation
        if disable_local_ca_jwt is not None:
            self._values["disable_local_ca_jwt"] = disable_local_ca_jwt
        if id is not None:
            self._values["id"] = id
        if issuer is not None:
            self._values["issuer"] = issuer
        if kubernetes_ca_cert is not None:
            self._values["kubernetes_ca_cert"] = kubernetes_ca_cert
        if namespace is not None:
            self._values["namespace"] = namespace
        if pem_keys is not None:
            self._values["pem_keys"] = pem_keys
        if token_reviewer_jwt is not None:
            self._values["token_reviewer_jwt"] = token_reviewer_jwt

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
    def kubernetes_host(self) -> builtins.str:
        '''Host must be a host string, a host:port pair, or a URL to the base of the Kubernetes API server.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_config#kubernetes_host KubernetesAuthBackendConfig#kubernetes_host}
        '''
        result = self._values.get("kubernetes_host")
        assert result is not None, "Required property 'kubernetes_host' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def backend(self) -> typing.Optional[builtins.str]:
        '''Unique name of the kubernetes backend to configure.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_config#backend KubernetesAuthBackendConfig#backend}
        '''
        result = self._values.get("backend")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_iss_validation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Optional disable JWT issuer validation. Allows to skip ISS validation.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_config#disable_iss_validation KubernetesAuthBackendConfig#disable_iss_validation}
        '''
        result = self._values.get("disable_iss_validation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def disable_local_ca_jwt(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Optional disable defaulting to the local CA cert and service account JWT when running in a Kubernetes pod.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_config#disable_local_ca_jwt KubernetesAuthBackendConfig#disable_local_ca_jwt}
        '''
        result = self._values.get("disable_local_ca_jwt")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_config#id KubernetesAuthBackendConfig#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def issuer(self) -> typing.Optional[builtins.str]:
        '''Optional JWT issuer. If no issuer is specified, kubernetes.io/serviceaccount will be used as the default issuer.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_config#issuer KubernetesAuthBackendConfig#issuer}
        '''
        result = self._values.get("issuer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kubernetes_ca_cert(self) -> typing.Optional[builtins.str]:
        '''PEM encoded CA cert for use by the TLS client used to talk with the Kubernetes API.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_config#kubernetes_ca_cert KubernetesAuthBackendConfig#kubernetes_ca_cert}
        '''
        result = self._values.get("kubernetes_ca_cert")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Target namespace. (requires Enterprise).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_config#namespace KubernetesAuthBackendConfig#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pem_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional list of PEM-formatted public keys or certificates used to verify the signatures of Kubernetes service account JWTs.

        If a certificate is given, its public key will be extracted. Not every installation of Kubernetes exposes these keys.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_config#pem_keys KubernetesAuthBackendConfig#pem_keys}
        '''
        result = self._values.get("pem_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def token_reviewer_jwt(self) -> typing.Optional[builtins.str]:
        '''A service account JWT used to access the TokenReview API to validate other JWTs during login.

        If not set the JWT used for login will be used to access the API.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/kubernetes_auth_backend_config#token_reviewer_jwt KubernetesAuthBackendConfig#token_reviewer_jwt}
        '''
        result = self._values.get("token_reviewer_jwt")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KubernetesAuthBackendConfigConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "KubernetesAuthBackendConfig",
    "KubernetesAuthBackendConfigConfig",
]

publication.publish()
