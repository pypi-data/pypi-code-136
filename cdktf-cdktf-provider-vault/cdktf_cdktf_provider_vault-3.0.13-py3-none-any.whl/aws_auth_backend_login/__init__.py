'''
# `vault_aws_auth_backend_login`

Refer to the Terraform Registory for docs: [`vault_aws_auth_backend_login`](https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login).
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


class AwsAuthBackendLogin(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.awsAuthBackendLogin.AwsAuthBackendLogin",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login vault_aws_auth_backend_login}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        backend: typing.Optional[builtins.str] = None,
        iam_http_request_method: typing.Optional[builtins.str] = None,
        iam_request_body: typing.Optional[builtins.str] = None,
        iam_request_headers: typing.Optional[builtins.str] = None,
        iam_request_url: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        nonce: typing.Optional[builtins.str] = None,
        pkcs7: typing.Optional[builtins.str] = None,
        role: typing.Optional[builtins.str] = None,
        signature: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login vault_aws_auth_backend_login} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param backend: AWS Auth Backend to read the token from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#backend AwsAuthBackendLogin#backend}
        :param iam_http_request_method: The HTTP method used in the signed request. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#iam_http_request_method AwsAuthBackendLogin#iam_http_request_method}
        :param iam_request_body: The Base64-encoded body of the signed request. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#iam_request_body AwsAuthBackendLogin#iam_request_body}
        :param iam_request_headers: The Base64-encoded, JSON serialized representation of the sts:GetCallerIdentity HTTP request headers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#iam_request_headers AwsAuthBackendLogin#iam_request_headers}
        :param iam_request_url: The Base64-encoded HTTP URL used in the signed request. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#iam_request_url AwsAuthBackendLogin#iam_request_url}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#id AwsAuthBackendLogin#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: Base64-encoded EC2 instance identity document to authenticate with. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#identity AwsAuthBackendLogin#identity}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#namespace AwsAuthBackendLogin#namespace}
        :param nonce: The nonce to be used for subsequent login requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#nonce AwsAuthBackendLogin#nonce}
        :param pkcs7: PKCS7 signature of the identity document to authenticate with, with all newline characters removed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#pkcs7 AwsAuthBackendLogin#pkcs7}
        :param role: AWS Auth Role to read the token from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#role AwsAuthBackendLogin#role}
        :param signature: Base64-encoded SHA256 RSA signature of the instance identtiy document to authenticate with. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#signature AwsAuthBackendLogin#signature}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AwsAuthBackendLogin.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AwsAuthBackendLoginConfig(
            backend=backend,
            iam_http_request_method=iam_http_request_method,
            iam_request_body=iam_request_body,
            iam_request_headers=iam_request_headers,
            iam_request_url=iam_request_url,
            id=id,
            identity=identity,
            namespace=namespace,
            nonce=nonce,
            pkcs7=pkcs7,
            role=role,
            signature=signature,
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

    @jsii.member(jsii_name="resetIamHttpRequestMethod")
    def reset_iam_http_request_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIamHttpRequestMethod", []))

    @jsii.member(jsii_name="resetIamRequestBody")
    def reset_iam_request_body(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIamRequestBody", []))

    @jsii.member(jsii_name="resetIamRequestHeaders")
    def reset_iam_request_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIamRequestHeaders", []))

    @jsii.member(jsii_name="resetIamRequestUrl")
    def reset_iam_request_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIamRequestUrl", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentity")
    def reset_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentity", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetNonce")
    def reset_nonce(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNonce", []))

    @jsii.member(jsii_name="resetPkcs7")
    def reset_pkcs7(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPkcs7", []))

    @jsii.member(jsii_name="resetRole")
    def reset_role(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRole", []))

    @jsii.member(jsii_name="resetSignature")
    def reset_signature(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSignature", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="accessor")
    def accessor(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessor"))

    @builtins.property
    @jsii.member(jsii_name="authType")
    def auth_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authType"))

    @builtins.property
    @jsii.member(jsii_name="clientToken")
    def client_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientToken"))

    @builtins.property
    @jsii.member(jsii_name="leaseDuration")
    def lease_duration(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "leaseDuration"))

    @builtins.property
    @jsii.member(jsii_name="leaseStartTime")
    def lease_start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "leaseStartTime"))

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="policies")
    def policies(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "policies"))

    @builtins.property
    @jsii.member(jsii_name="renewable")
    def renewable(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "renewable"))

    @builtins.property
    @jsii.member(jsii_name="backendInput")
    def backend_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backendInput"))

    @builtins.property
    @jsii.member(jsii_name="iamHttpRequestMethodInput")
    def iam_http_request_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamHttpRequestMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="iamRequestBodyInput")
    def iam_request_body_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamRequestBodyInput"))

    @builtins.property
    @jsii.member(jsii_name="iamRequestHeadersInput")
    def iam_request_headers_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamRequestHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="iamRequestUrlInput")
    def iam_request_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "iamRequestUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="nonceInput")
    def nonce_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nonceInput"))

    @builtins.property
    @jsii.member(jsii_name="pkcs7Input")
    def pkcs7_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pkcs7Input"))

    @builtins.property
    @jsii.member(jsii_name="roleInput")
    def role_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleInput"))

    @builtins.property
    @jsii.member(jsii_name="signatureInput")
    def signature_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "signatureInput"))

    @builtins.property
    @jsii.member(jsii_name="backend")
    def backend(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backend"))

    @backend.setter
    def backend(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendLogin, "backend").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backend", value)

    @builtins.property
    @jsii.member(jsii_name="iamHttpRequestMethod")
    def iam_http_request_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iamHttpRequestMethod"))

    @iam_http_request_method.setter
    def iam_http_request_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendLogin, "iam_http_request_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamHttpRequestMethod", value)

    @builtins.property
    @jsii.member(jsii_name="iamRequestBody")
    def iam_request_body(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iamRequestBody"))

    @iam_request_body.setter
    def iam_request_body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendLogin, "iam_request_body").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamRequestBody", value)

    @builtins.property
    @jsii.member(jsii_name="iamRequestHeaders")
    def iam_request_headers(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iamRequestHeaders"))

    @iam_request_headers.setter
    def iam_request_headers(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendLogin, "iam_request_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamRequestHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="iamRequestUrl")
    def iam_request_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "iamRequestUrl"))

    @iam_request_url.setter
    def iam_request_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendLogin, "iam_request_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "iamRequestUrl", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendLogin, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="identity")
    def identity(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identity"))

    @identity.setter
    def identity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendLogin, "identity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identity", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendLogin, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)

    @builtins.property
    @jsii.member(jsii_name="nonce")
    def nonce(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nonce"))

    @nonce.setter
    def nonce(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendLogin, "nonce").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nonce", value)

    @builtins.property
    @jsii.member(jsii_name="pkcs7")
    def pkcs7(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pkcs7"))

    @pkcs7.setter
    def pkcs7(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendLogin, "pkcs7").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pkcs7", value)

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendLogin, "role").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value)

    @builtins.property
    @jsii.member(jsii_name="signature")
    def signature(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signature"))

    @signature.setter
    def signature(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AwsAuthBackendLogin, "signature").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signature", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.awsAuthBackendLogin.AwsAuthBackendLoginConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "backend": "backend",
        "iam_http_request_method": "iamHttpRequestMethod",
        "iam_request_body": "iamRequestBody",
        "iam_request_headers": "iamRequestHeaders",
        "iam_request_url": "iamRequestUrl",
        "id": "id",
        "identity": "identity",
        "namespace": "namespace",
        "nonce": "nonce",
        "pkcs7": "pkcs7",
        "role": "role",
        "signature": "signature",
    },
)
class AwsAuthBackendLoginConfig(cdktf.TerraformMetaArguments):
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
        backend: typing.Optional[builtins.str] = None,
        iam_http_request_method: typing.Optional[builtins.str] = None,
        iam_request_body: typing.Optional[builtins.str] = None,
        iam_request_headers: typing.Optional[builtins.str] = None,
        iam_request_url: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        nonce: typing.Optional[builtins.str] = None,
        pkcs7: typing.Optional[builtins.str] = None,
        role: typing.Optional[builtins.str] = None,
        signature: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param backend: AWS Auth Backend to read the token from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#backend AwsAuthBackendLogin#backend}
        :param iam_http_request_method: The HTTP method used in the signed request. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#iam_http_request_method AwsAuthBackendLogin#iam_http_request_method}
        :param iam_request_body: The Base64-encoded body of the signed request. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#iam_request_body AwsAuthBackendLogin#iam_request_body}
        :param iam_request_headers: The Base64-encoded, JSON serialized representation of the sts:GetCallerIdentity HTTP request headers. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#iam_request_headers AwsAuthBackendLogin#iam_request_headers}
        :param iam_request_url: The Base64-encoded HTTP URL used in the signed request. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#iam_request_url AwsAuthBackendLogin#iam_request_url}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#id AwsAuthBackendLogin#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: Base64-encoded EC2 instance identity document to authenticate with. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#identity AwsAuthBackendLogin#identity}
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#namespace AwsAuthBackendLogin#namespace}
        :param nonce: The nonce to be used for subsequent login requests. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#nonce AwsAuthBackendLogin#nonce}
        :param pkcs7: PKCS7 signature of the identity document to authenticate with, with all newline characters removed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#pkcs7 AwsAuthBackendLogin#pkcs7}
        :param role: AWS Auth Role to read the token from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#role AwsAuthBackendLogin#role}
        :param signature: Base64-encoded SHA256 RSA signature of the instance identtiy document to authenticate with. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#signature AwsAuthBackendLogin#signature}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(AwsAuthBackendLoginConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument backend", value=backend, expected_type=type_hints["backend"])
            check_type(argname="argument iam_http_request_method", value=iam_http_request_method, expected_type=type_hints["iam_http_request_method"])
            check_type(argname="argument iam_request_body", value=iam_request_body, expected_type=type_hints["iam_request_body"])
            check_type(argname="argument iam_request_headers", value=iam_request_headers, expected_type=type_hints["iam_request_headers"])
            check_type(argname="argument iam_request_url", value=iam_request_url, expected_type=type_hints["iam_request_url"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument nonce", value=nonce, expected_type=type_hints["nonce"])
            check_type(argname="argument pkcs7", value=pkcs7, expected_type=type_hints["pkcs7"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument signature", value=signature, expected_type=type_hints["signature"])
        self._values: typing.Dict[str, typing.Any] = {}
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
        if iam_http_request_method is not None:
            self._values["iam_http_request_method"] = iam_http_request_method
        if iam_request_body is not None:
            self._values["iam_request_body"] = iam_request_body
        if iam_request_headers is not None:
            self._values["iam_request_headers"] = iam_request_headers
        if iam_request_url is not None:
            self._values["iam_request_url"] = iam_request_url
        if id is not None:
            self._values["id"] = id
        if identity is not None:
            self._values["identity"] = identity
        if namespace is not None:
            self._values["namespace"] = namespace
        if nonce is not None:
            self._values["nonce"] = nonce
        if pkcs7 is not None:
            self._values["pkcs7"] = pkcs7
        if role is not None:
            self._values["role"] = role
        if signature is not None:
            self._values["signature"] = signature

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
    def backend(self) -> typing.Optional[builtins.str]:
        '''AWS Auth Backend to read the token from.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#backend AwsAuthBackendLogin#backend}
        '''
        result = self._values.get("backend")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam_http_request_method(self) -> typing.Optional[builtins.str]:
        '''The HTTP method used in the signed request.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#iam_http_request_method AwsAuthBackendLogin#iam_http_request_method}
        '''
        result = self._values.get("iam_http_request_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam_request_body(self) -> typing.Optional[builtins.str]:
        '''The Base64-encoded body of the signed request.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#iam_request_body AwsAuthBackendLogin#iam_request_body}
        '''
        result = self._values.get("iam_request_body")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam_request_headers(self) -> typing.Optional[builtins.str]:
        '''The Base64-encoded, JSON serialized representation of the sts:GetCallerIdentity HTTP request headers.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#iam_request_headers AwsAuthBackendLogin#iam_request_headers}
        '''
        result = self._values.get("iam_request_headers")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def iam_request_url(self) -> typing.Optional[builtins.str]:
        '''The Base64-encoded HTTP URL used in the signed request.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#iam_request_url AwsAuthBackendLogin#iam_request_url}
        '''
        result = self._values.get("iam_request_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#id AwsAuthBackendLogin#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity(self) -> typing.Optional[builtins.str]:
        '''Base64-encoded EC2 instance identity document to authenticate with.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#identity AwsAuthBackendLogin#identity}
        '''
        result = self._values.get("identity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Target namespace. (requires Enterprise).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#namespace AwsAuthBackendLogin#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def nonce(self) -> typing.Optional[builtins.str]:
        '''The nonce to be used for subsequent login requests.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#nonce AwsAuthBackendLogin#nonce}
        '''
        result = self._values.get("nonce")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pkcs7(self) -> typing.Optional[builtins.str]:
        '''PKCS7 signature of the identity document to authenticate with, with all newline characters removed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#pkcs7 AwsAuthBackendLogin#pkcs7}
        '''
        result = self._values.get("pkcs7")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def role(self) -> typing.Optional[builtins.str]:
        '''AWS Auth Role to read the token from.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#role AwsAuthBackendLogin#role}
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def signature(self) -> typing.Optional[builtins.str]:
        '''Base64-encoded SHA256 RSA signature of the instance identtiy document to authenticate with.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/aws_auth_backend_login#signature AwsAuthBackendLogin#signature}
        '''
        result = self._values.get("signature")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AwsAuthBackendLoginConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "AwsAuthBackendLogin",
    "AwsAuthBackendLoginConfig",
]

publication.publish()
