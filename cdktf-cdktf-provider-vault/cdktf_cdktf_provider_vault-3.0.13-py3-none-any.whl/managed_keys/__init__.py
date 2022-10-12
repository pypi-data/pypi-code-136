'''
# `vault_managed_keys`

Refer to the Terraform Registory for docs: [`vault_managed_keys`](https://www.terraform.io/docs/providers/vault/r/managed_keys).
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


class ManagedKeys(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.managedKeys.ManagedKeys",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vault/r/managed_keys vault_managed_keys}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        aws: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ManagedKeysAws", typing.Dict[str, typing.Any]]]]] = None,
        azure: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ManagedKeysAzure", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        pkcs: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ManagedKeysPkcs", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vault/r/managed_keys vault_managed_keys} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param aws: aws block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#aws ManagedKeys#aws}
        :param azure: azure block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#azure ManagedKeys#azure}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#id ManagedKeys#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#namespace ManagedKeys#namespace}
        :param pkcs: pkcs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#pkcs ManagedKeys#pkcs}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedKeys.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ManagedKeysConfig(
            aws=aws,
            azure=azure,
            id=id,
            namespace=namespace,
            pkcs=pkcs,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAws")
    def put_aws(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ManagedKeysAws", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedKeys.put_aws)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAws", [value]))

    @jsii.member(jsii_name="putAzure")
    def put_azure(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ManagedKeysAzure", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedKeys.put_azure)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAzure", [value]))

    @jsii.member(jsii_name="putPkcs")
    def put_pkcs(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ManagedKeysPkcs", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedKeys.put_pkcs)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPkcs", [value]))

    @jsii.member(jsii_name="resetAws")
    def reset_aws(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAws", []))

    @jsii.member(jsii_name="resetAzure")
    def reset_azure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzure", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetNamespace")
    def reset_namespace(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNamespace", []))

    @jsii.member(jsii_name="resetPkcs")
    def reset_pkcs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPkcs", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="aws")
    def aws(self) -> "ManagedKeysAwsList":
        return typing.cast("ManagedKeysAwsList", jsii.get(self, "aws"))

    @builtins.property
    @jsii.member(jsii_name="azure")
    def azure(self) -> "ManagedKeysAzureList":
        return typing.cast("ManagedKeysAzureList", jsii.get(self, "azure"))

    @builtins.property
    @jsii.member(jsii_name="pkcs")
    def pkcs(self) -> "ManagedKeysPkcsList":
        return typing.cast("ManagedKeysPkcsList", jsii.get(self, "pkcs"))

    @builtins.property
    @jsii.member(jsii_name="awsInput")
    def aws_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ManagedKeysAws"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ManagedKeysAws"]]], jsii.get(self, "awsInput"))

    @builtins.property
    @jsii.member(jsii_name="azureInput")
    def azure_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ManagedKeysAzure"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ManagedKeysAzure"]]], jsii.get(self, "azureInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="pkcsInput")
    def pkcs_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ManagedKeysPkcs"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ManagedKeysPkcs"]]], jsii.get(self, "pkcsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeys, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespace"))

    @namespace.setter
    def namespace(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeys, "namespace").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespace", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.managedKeys.ManagedKeysAws",
    jsii_struct_bases=[],
    name_mapping={
        "access_key": "accessKey",
        "key_bits": "keyBits",
        "key_type": "keyType",
        "kms_key": "kmsKey",
        "name": "name",
        "secret_key": "secretKey",
        "allow_generate_key": "allowGenerateKey",
        "allow_replace_key": "allowReplaceKey",
        "allow_store_key": "allowStoreKey",
        "any_mount": "anyMount",
        "curve": "curve",
        "endpoint": "endpoint",
        "region": "region",
    },
)
class ManagedKeysAws:
    def __init__(
        self,
        *,
        access_key: builtins.str,
        key_bits: builtins.str,
        key_type: builtins.str,
        kms_key: builtins.str,
        name: builtins.str,
        secret_key: builtins.str,
        allow_generate_key: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_replace_key: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_store_key: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        any_mount: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        curve: typing.Optional[builtins.str] = None,
        endpoint: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param access_key: The AWS access key to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#access_key ManagedKeys#access_key}
        :param key_bits: The size in bits for an RSA key. This field is required when 'key_type' is 'RSA'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#key_bits ManagedKeys#key_bits}
        :param key_type: The type of key to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#key_type ManagedKeys#key_type}
        :param kms_key: An identifier for the key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#kms_key ManagedKeys#kms_key}
        :param name: A unique lowercase name that serves as identifying the key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#name ManagedKeys#name}
        :param secret_key: The AWS secret key to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#secret_key ManagedKeys#secret_key}
        :param allow_generate_key: If no existing key can be found in the referenced backend, instructs Vault to generate a key within the backend. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#allow_generate_key ManagedKeys#allow_generate_key}
        :param allow_replace_key: Controls the ability for Vault to replace through generation or importing a key into the configured backend even if a key is present, if set to false those operations are forbidden if a key exists. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#allow_replace_key ManagedKeys#allow_replace_key}
        :param allow_store_key: Controls the ability for Vault to import a key to the configured backend, if 'false', those operations will be forbidden. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#allow_store_key ManagedKeys#allow_store_key}
        :param any_mount: Allow usage from any mount point within the namespace if 'true'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#any_mount ManagedKeys#any_mount}
        :param curve: The curve to use for an ECDSA key. Used when key_type is 'ECDSA'. Required if 'allow_generate_key' is true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#curve ManagedKeys#curve}
        :param endpoint: Used to specify a custom AWS endpoint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#endpoint ManagedKeys#endpoint}
        :param region: The AWS region where the keys are stored (or will be stored). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#region ManagedKeys#region}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedKeysAws.__init__)
            check_type(argname="argument access_key", value=access_key, expected_type=type_hints["access_key"])
            check_type(argname="argument key_bits", value=key_bits, expected_type=type_hints["key_bits"])
            check_type(argname="argument key_type", value=key_type, expected_type=type_hints["key_type"])
            check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument secret_key", value=secret_key, expected_type=type_hints["secret_key"])
            check_type(argname="argument allow_generate_key", value=allow_generate_key, expected_type=type_hints["allow_generate_key"])
            check_type(argname="argument allow_replace_key", value=allow_replace_key, expected_type=type_hints["allow_replace_key"])
            check_type(argname="argument allow_store_key", value=allow_store_key, expected_type=type_hints["allow_store_key"])
            check_type(argname="argument any_mount", value=any_mount, expected_type=type_hints["any_mount"])
            check_type(argname="argument curve", value=curve, expected_type=type_hints["curve"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
        self._values: typing.Dict[str, typing.Any] = {
            "access_key": access_key,
            "key_bits": key_bits,
            "key_type": key_type,
            "kms_key": kms_key,
            "name": name,
            "secret_key": secret_key,
        }
        if allow_generate_key is not None:
            self._values["allow_generate_key"] = allow_generate_key
        if allow_replace_key is not None:
            self._values["allow_replace_key"] = allow_replace_key
        if allow_store_key is not None:
            self._values["allow_store_key"] = allow_store_key
        if any_mount is not None:
            self._values["any_mount"] = any_mount
        if curve is not None:
            self._values["curve"] = curve
        if endpoint is not None:
            self._values["endpoint"] = endpoint
        if region is not None:
            self._values["region"] = region

    @builtins.property
    def access_key(self) -> builtins.str:
        '''The AWS access key to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#access_key ManagedKeys#access_key}
        '''
        result = self._values.get("access_key")
        assert result is not None, "Required property 'access_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key_bits(self) -> builtins.str:
        '''The size in bits for an RSA key. This field is required when 'key_type' is 'RSA'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#key_bits ManagedKeys#key_bits}
        '''
        result = self._values.get("key_bits")
        assert result is not None, "Required property 'key_bits' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key_type(self) -> builtins.str:
        '''The type of key to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#key_type ManagedKeys#key_type}
        '''
        result = self._values.get("key_type")
        assert result is not None, "Required property 'key_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kms_key(self) -> builtins.str:
        '''An identifier for the key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#kms_key ManagedKeys#kms_key}
        '''
        result = self._values.get("kms_key")
        assert result is not None, "Required property 'kms_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A unique lowercase name that serves as identifying the key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#name ManagedKeys#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def secret_key(self) -> builtins.str:
        '''The AWS secret key to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#secret_key ManagedKeys#secret_key}
        '''
        result = self._values.get("secret_key")
        assert result is not None, "Required property 'secret_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_generate_key(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If no existing key can be found in the referenced backend, instructs Vault to generate a key within the backend.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#allow_generate_key ManagedKeys#allow_generate_key}
        '''
        result = self._values.get("allow_generate_key")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_replace_key(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Controls the ability for Vault to replace through generation or importing a key into the configured backend even if a key is present, if set to false those operations are forbidden if a key exists.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#allow_replace_key ManagedKeys#allow_replace_key}
        '''
        result = self._values.get("allow_replace_key")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_store_key(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Controls the ability for Vault to import a key to the configured backend, if 'false', those operations will be forbidden.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#allow_store_key ManagedKeys#allow_store_key}
        '''
        result = self._values.get("allow_store_key")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def any_mount(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Allow usage from any mount point within the namespace if 'true'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#any_mount ManagedKeys#any_mount}
        '''
        result = self._values.get("any_mount")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def curve(self) -> typing.Optional[builtins.str]:
        '''The curve to use for an ECDSA key. Used when key_type is 'ECDSA'. Required if 'allow_generate_key' is true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#curve ManagedKeys#curve}
        '''
        result = self._values.get("curve")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint(self) -> typing.Optional[builtins.str]:
        '''Used to specify a custom AWS endpoint.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#endpoint ManagedKeys#endpoint}
        '''
        result = self._values.get("endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The AWS region where the keys are stored (or will be stored).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#region ManagedKeys#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedKeysAws(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManagedKeysAwsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.managedKeys.ManagedKeysAwsList",
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
            type_hints = typing.get_type_hints(ManagedKeysAwsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ManagedKeysAwsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedKeysAwsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ManagedKeysAwsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysAwsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ManagedKeysAwsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ManagedKeysAwsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedKeysAws]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedKeysAws]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedKeysAws]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysAwsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ManagedKeysAwsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.managedKeys.ManagedKeysAwsOutputReference",
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
            type_hints = typing.get_type_hints(ManagedKeysAwsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAllowGenerateKey")
    def reset_allow_generate_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowGenerateKey", []))

    @jsii.member(jsii_name="resetAllowReplaceKey")
    def reset_allow_replace_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowReplaceKey", []))

    @jsii.member(jsii_name="resetAllowStoreKey")
    def reset_allow_store_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowStoreKey", []))

    @jsii.member(jsii_name="resetAnyMount")
    def reset_any_mount(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnyMount", []))

    @jsii.member(jsii_name="resetCurve")
    def reset_curve(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCurve", []))

    @jsii.member(jsii_name="resetEndpoint")
    def reset_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpoint", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @builtins.property
    @jsii.member(jsii_name="uuid")
    def uuid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uuid"))

    @builtins.property
    @jsii.member(jsii_name="accessKeyInput")
    def access_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="allowGenerateKeyInput")
    def allow_generate_key_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowGenerateKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="allowReplaceKeyInput")
    def allow_replace_key_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowReplaceKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="allowStoreKeyInput")
    def allow_store_key_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowStoreKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="anyMountInput")
    def any_mount_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "anyMountInput"))

    @builtins.property
    @jsii.member(jsii_name="curveInput")
    def curve_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "curveInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="keyBitsInput")
    def key_bits_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyBitsInput"))

    @builtins.property
    @jsii.member(jsii_name="keyTypeInput")
    def key_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyInput")
    def kms_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="secretKeyInput")
    def secret_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="accessKey")
    def access_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessKey"))

    @access_key.setter
    def access_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysAwsOutputReference, "access_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessKey", value)

    @builtins.property
    @jsii.member(jsii_name="allowGenerateKey")
    def allow_generate_key(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowGenerateKey"))

    @allow_generate_key.setter
    def allow_generate_key(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysAwsOutputReference, "allow_generate_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowGenerateKey", value)

    @builtins.property
    @jsii.member(jsii_name="allowReplaceKey")
    def allow_replace_key(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowReplaceKey"))

    @allow_replace_key.setter
    def allow_replace_key(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysAwsOutputReference, "allow_replace_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowReplaceKey", value)

    @builtins.property
    @jsii.member(jsii_name="allowStoreKey")
    def allow_store_key(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowStoreKey"))

    @allow_store_key.setter
    def allow_store_key(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysAwsOutputReference, "allow_store_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowStoreKey", value)

    @builtins.property
    @jsii.member(jsii_name="anyMount")
    def any_mount(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "anyMount"))

    @any_mount.setter
    def any_mount(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysAwsOutputReference, "any_mount").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "anyMount", value)

    @builtins.property
    @jsii.member(jsii_name="curve")
    def curve(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "curve"))

    @curve.setter
    def curve(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysAwsOutputReference, "curve").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "curve", value)

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysAwsOutputReference, "endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="keyBits")
    def key_bits(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyBits"))

    @key_bits.setter
    def key_bits(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysAwsOutputReference, "key_bits").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyBits", value)

    @builtins.property
    @jsii.member(jsii_name="keyType")
    def key_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyType"))

    @key_type.setter
    def key_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysAwsOutputReference, "key_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyType", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKey")
    def kms_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKey"))

    @kms_key.setter
    def kms_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysAwsOutputReference, "kms_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKey", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysAwsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysAwsOutputReference, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="secretKey")
    def secret_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretKey"))

    @secret_key.setter
    def secret_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysAwsOutputReference, "secret_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ManagedKeysAws, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ManagedKeysAws, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ManagedKeysAws, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysAwsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.managedKeys.ManagedKeysAzure",
    jsii_struct_bases=[],
    name_mapping={
        "client_id": "clientId",
        "client_secret": "clientSecret",
        "key_name": "keyName",
        "key_type": "keyType",
        "name": "name",
        "tenant_id": "tenantId",
        "vault_name": "vaultName",
        "allow_generate_key": "allowGenerateKey",
        "allow_replace_key": "allowReplaceKey",
        "allow_store_key": "allowStoreKey",
        "any_mount": "anyMount",
        "environment": "environment",
        "key_bits": "keyBits",
        "resource": "resource",
    },
)
class ManagedKeysAzure:
    def __init__(
        self,
        *,
        client_id: builtins.str,
        client_secret: builtins.str,
        key_name: builtins.str,
        key_type: builtins.str,
        name: builtins.str,
        tenant_id: builtins.str,
        vault_name: builtins.str,
        allow_generate_key: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_replace_key: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_store_key: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        any_mount: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        environment: typing.Optional[builtins.str] = None,
        key_bits: typing.Optional[builtins.str] = None,
        resource: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param client_id: The client id for credentials to query the Azure APIs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#client_id ManagedKeys#client_id}
        :param client_secret: The client secret for credentials to query the Azure APIs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#client_secret ManagedKeys#client_secret}
        :param key_name: The Key Vault key to use for encryption and decryption. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#key_name ManagedKeys#key_name}
        :param key_type: The type of key to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#key_type ManagedKeys#key_type}
        :param name: A unique lowercase name that serves as identifying the key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#name ManagedKeys#name}
        :param tenant_id: The tenant id for the Azure Active Directory organization. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#tenant_id ManagedKeys#tenant_id}
        :param vault_name: The Key Vault vault to use the encryption keys for encryption and decryption. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#vault_name ManagedKeys#vault_name}
        :param allow_generate_key: If no existing key can be found in the referenced backend, instructs Vault to generate a key within the backend. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#allow_generate_key ManagedKeys#allow_generate_key}
        :param allow_replace_key: Controls the ability for Vault to replace through generation or importing a key into the configured backend even if a key is present, if set to false those operations are forbidden if a key exists. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#allow_replace_key ManagedKeys#allow_replace_key}
        :param allow_store_key: Controls the ability for Vault to import a key to the configured backend, if 'false', those operations will be forbidden. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#allow_store_key ManagedKeys#allow_store_key}
        :param any_mount: Allow usage from any mount point within the namespace if 'true'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#any_mount ManagedKeys#any_mount}
        :param environment: The Azure Cloud environment API endpoints to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#environment ManagedKeys#environment}
        :param key_bits: The size in bits for an RSA key. This field is required when 'key_type' is 'RSA' or when 'allow_generate_key' is true Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#key_bits ManagedKeys#key_bits}
        :param resource: The Azure Key Vault resource's DNS Suffix to connect to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#resource ManagedKeys#resource}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedKeysAzure.__init__)
            check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
            check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
            check_type(argname="argument key_name", value=key_name, expected_type=type_hints["key_name"])
            check_type(argname="argument key_type", value=key_type, expected_type=type_hints["key_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tenant_id", value=tenant_id, expected_type=type_hints["tenant_id"])
            check_type(argname="argument vault_name", value=vault_name, expected_type=type_hints["vault_name"])
            check_type(argname="argument allow_generate_key", value=allow_generate_key, expected_type=type_hints["allow_generate_key"])
            check_type(argname="argument allow_replace_key", value=allow_replace_key, expected_type=type_hints["allow_replace_key"])
            check_type(argname="argument allow_store_key", value=allow_store_key, expected_type=type_hints["allow_store_key"])
            check_type(argname="argument any_mount", value=any_mount, expected_type=type_hints["any_mount"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument key_bits", value=key_bits, expected_type=type_hints["key_bits"])
            check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
        self._values: typing.Dict[str, typing.Any] = {
            "client_id": client_id,
            "client_secret": client_secret,
            "key_name": key_name,
            "key_type": key_type,
            "name": name,
            "tenant_id": tenant_id,
            "vault_name": vault_name,
        }
        if allow_generate_key is not None:
            self._values["allow_generate_key"] = allow_generate_key
        if allow_replace_key is not None:
            self._values["allow_replace_key"] = allow_replace_key
        if allow_store_key is not None:
            self._values["allow_store_key"] = allow_store_key
        if any_mount is not None:
            self._values["any_mount"] = any_mount
        if environment is not None:
            self._values["environment"] = environment
        if key_bits is not None:
            self._values["key_bits"] = key_bits
        if resource is not None:
            self._values["resource"] = resource

    @builtins.property
    def client_id(self) -> builtins.str:
        '''The client id for credentials to query the Azure APIs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#client_id ManagedKeys#client_id}
        '''
        result = self._values.get("client_id")
        assert result is not None, "Required property 'client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def client_secret(self) -> builtins.str:
        '''The client secret for credentials to query the Azure APIs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#client_secret ManagedKeys#client_secret}
        '''
        result = self._values.get("client_secret")
        assert result is not None, "Required property 'client_secret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key_name(self) -> builtins.str:
        '''The Key Vault key to use for encryption and decryption.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#key_name ManagedKeys#key_name}
        '''
        result = self._values.get("key_name")
        assert result is not None, "Required property 'key_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key_type(self) -> builtins.str:
        '''The type of key to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#key_type ManagedKeys#key_type}
        '''
        result = self._values.get("key_type")
        assert result is not None, "Required property 'key_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A unique lowercase name that serves as identifying the key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#name ManagedKeys#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tenant_id(self) -> builtins.str:
        '''The tenant id for the Azure Active Directory organization.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#tenant_id ManagedKeys#tenant_id}
        '''
        result = self._values.get("tenant_id")
        assert result is not None, "Required property 'tenant_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vault_name(self) -> builtins.str:
        '''The Key Vault vault to use the encryption keys for encryption and decryption.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#vault_name ManagedKeys#vault_name}
        '''
        result = self._values.get("vault_name")
        assert result is not None, "Required property 'vault_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_generate_key(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If no existing key can be found in the referenced backend, instructs Vault to generate a key within the backend.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#allow_generate_key ManagedKeys#allow_generate_key}
        '''
        result = self._values.get("allow_generate_key")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_replace_key(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Controls the ability for Vault to replace through generation or importing a key into the configured backend even if a key is present, if set to false those operations are forbidden if a key exists.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#allow_replace_key ManagedKeys#allow_replace_key}
        '''
        result = self._values.get("allow_replace_key")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_store_key(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Controls the ability for Vault to import a key to the configured backend, if 'false', those operations will be forbidden.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#allow_store_key ManagedKeys#allow_store_key}
        '''
        result = self._values.get("allow_store_key")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def any_mount(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Allow usage from any mount point within the namespace if 'true'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#any_mount ManagedKeys#any_mount}
        '''
        result = self._values.get("any_mount")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def environment(self) -> typing.Optional[builtins.str]:
        '''The Azure Cloud environment API endpoints to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#environment ManagedKeys#environment}
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_bits(self) -> typing.Optional[builtins.str]:
        '''The size in bits for an RSA key.

        This field is required when 'key_type' is 'RSA' or when 'allow_generate_key' is true

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#key_bits ManagedKeys#key_bits}
        '''
        result = self._values.get("key_bits")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource(self) -> typing.Optional[builtins.str]:
        '''The Azure Key Vault resource's DNS Suffix to connect to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#resource ManagedKeys#resource}
        '''
        result = self._values.get("resource")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedKeysAzure(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManagedKeysAzureList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.managedKeys.ManagedKeysAzureList",
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
            type_hints = typing.get_type_hints(ManagedKeysAzureList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ManagedKeysAzureOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedKeysAzureList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ManagedKeysAzureOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysAzureList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ManagedKeysAzureList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ManagedKeysAzureList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedKeysAzure]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedKeysAzure]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedKeysAzure]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysAzureList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ManagedKeysAzureOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.managedKeys.ManagedKeysAzureOutputReference",
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
            type_hints = typing.get_type_hints(ManagedKeysAzureOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAllowGenerateKey")
    def reset_allow_generate_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowGenerateKey", []))

    @jsii.member(jsii_name="resetAllowReplaceKey")
    def reset_allow_replace_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowReplaceKey", []))

    @jsii.member(jsii_name="resetAllowStoreKey")
    def reset_allow_store_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowStoreKey", []))

    @jsii.member(jsii_name="resetAnyMount")
    def reset_any_mount(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnyMount", []))

    @jsii.member(jsii_name="resetEnvironment")
    def reset_environment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnvironment", []))

    @jsii.member(jsii_name="resetKeyBits")
    def reset_key_bits(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyBits", []))

    @jsii.member(jsii_name="resetResource")
    def reset_resource(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResource", []))

    @builtins.property
    @jsii.member(jsii_name="uuid")
    def uuid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uuid"))

    @builtins.property
    @jsii.member(jsii_name="allowGenerateKeyInput")
    def allow_generate_key_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowGenerateKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="allowReplaceKeyInput")
    def allow_replace_key_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowReplaceKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="allowStoreKeyInput")
    def allow_store_key_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowStoreKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="anyMountInput")
    def any_mount_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "anyMountInput"))

    @builtins.property
    @jsii.member(jsii_name="clientIdInput")
    def client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="clientSecretInput")
    def client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentInput")
    def environment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentInput"))

    @builtins.property
    @jsii.member(jsii_name="keyBitsInput")
    def key_bits_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyBitsInput"))

    @builtins.property
    @jsii.member(jsii_name="keyNameInput")
    def key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="keyTypeInput")
    def key_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceInput")
    def resource_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceInput"))

    @builtins.property
    @jsii.member(jsii_name="tenantIdInput")
    def tenant_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenantIdInput"))

    @builtins.property
    @jsii.member(jsii_name="vaultNameInput")
    def vault_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vaultNameInput"))

    @builtins.property
    @jsii.member(jsii_name="allowGenerateKey")
    def allow_generate_key(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowGenerateKey"))

    @allow_generate_key.setter
    def allow_generate_key(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysAzureOutputReference, "allow_generate_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowGenerateKey", value)

    @builtins.property
    @jsii.member(jsii_name="allowReplaceKey")
    def allow_replace_key(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowReplaceKey"))

    @allow_replace_key.setter
    def allow_replace_key(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysAzureOutputReference, "allow_replace_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowReplaceKey", value)

    @builtins.property
    @jsii.member(jsii_name="allowStoreKey")
    def allow_store_key(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowStoreKey"))

    @allow_store_key.setter
    def allow_store_key(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysAzureOutputReference, "allow_store_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowStoreKey", value)

    @builtins.property
    @jsii.member(jsii_name="anyMount")
    def any_mount(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "anyMount"))

    @any_mount.setter
    def any_mount(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysAzureOutputReference, "any_mount").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "anyMount", value)

    @builtins.property
    @jsii.member(jsii_name="clientId")
    def client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientId"))

    @client_id.setter
    def client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysAzureOutputReference, "client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientId", value)

    @builtins.property
    @jsii.member(jsii_name="clientSecret")
    def client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clientSecret"))

    @client_secret.setter
    def client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysAzureOutputReference, "client_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="environment")
    def environment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "environment"))

    @environment.setter
    def environment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysAzureOutputReference, "environment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environment", value)

    @builtins.property
    @jsii.member(jsii_name="keyBits")
    def key_bits(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyBits"))

    @key_bits.setter
    def key_bits(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysAzureOutputReference, "key_bits").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyBits", value)

    @builtins.property
    @jsii.member(jsii_name="keyName")
    def key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyName"))

    @key_name.setter
    def key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysAzureOutputReference, "key_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyName", value)

    @builtins.property
    @jsii.member(jsii_name="keyType")
    def key_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyType"))

    @key_type.setter
    def key_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysAzureOutputReference, "key_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysAzureOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resource")
    def resource(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resource"))

    @resource.setter
    def resource(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysAzureOutputReference, "resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resource", value)

    @builtins.property
    @jsii.member(jsii_name="tenantId")
    def tenant_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenantId"))

    @tenant_id.setter
    def tenant_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysAzureOutputReference, "tenant_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenantId", value)

    @builtins.property
    @jsii.member(jsii_name="vaultName")
    def vault_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vaultName"))

    @vault_name.setter
    def vault_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysAzureOutputReference, "vault_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vaultName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ManagedKeysAzure, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ManagedKeysAzure, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ManagedKeysAzure, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysAzureOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.managedKeys.ManagedKeysConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "aws": "aws",
        "azure": "azure",
        "id": "id",
        "namespace": "namespace",
        "pkcs": "pkcs",
    },
)
class ManagedKeysConfig(cdktf.TerraformMetaArguments):
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
        aws: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ManagedKeysAws, typing.Dict[str, typing.Any]]]]] = None,
        azure: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[ManagedKeysAzure, typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        namespace: typing.Optional[builtins.str] = None,
        pkcs: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["ManagedKeysPkcs", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param aws: aws block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#aws ManagedKeys#aws}
        :param azure: azure block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#azure ManagedKeys#azure}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#id ManagedKeys#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param namespace: Target namespace. (requires Enterprise). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#namespace ManagedKeys#namespace}
        :param pkcs: pkcs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#pkcs ManagedKeys#pkcs}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(ManagedKeysConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument aws", value=aws, expected_type=type_hints["aws"])
            check_type(argname="argument azure", value=azure, expected_type=type_hints["azure"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
            check_type(argname="argument pkcs", value=pkcs, expected_type=type_hints["pkcs"])
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
        if aws is not None:
            self._values["aws"] = aws
        if azure is not None:
            self._values["azure"] = azure
        if id is not None:
            self._values["id"] = id
        if namespace is not None:
            self._values["namespace"] = namespace
        if pkcs is not None:
            self._values["pkcs"] = pkcs

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
    def aws(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedKeysAws]]]:
        '''aws block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#aws ManagedKeys#aws}
        '''
        result = self._values.get("aws")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedKeysAws]]], result)

    @builtins.property
    def azure(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedKeysAzure]]]:
        '''azure block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#azure ManagedKeys#azure}
        '''
        result = self._values.get("azure")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedKeysAzure]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#id ManagedKeys#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def namespace(self) -> typing.Optional[builtins.str]:
        '''Target namespace. (requires Enterprise).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#namespace ManagedKeys#namespace}
        '''
        result = self._values.get("namespace")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pkcs(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ManagedKeysPkcs"]]]:
        '''pkcs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#pkcs ManagedKeys#pkcs}
        '''
        result = self._values.get("pkcs")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["ManagedKeysPkcs"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedKeysConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-vault.managedKeys.ManagedKeysPkcs",
    jsii_struct_bases=[],
    name_mapping={
        "key_id": "keyId",
        "key_label": "keyLabel",
        "library": "library",
        "mechanism": "mechanism",
        "name": "name",
        "pin": "pin",
        "allow_generate_key": "allowGenerateKey",
        "allow_replace_key": "allowReplaceKey",
        "allow_store_key": "allowStoreKey",
        "any_mount": "anyMount",
        "curve": "curve",
        "force_rw_session": "forceRwSession",
        "key_bits": "keyBits",
        "slot": "slot",
        "token_label": "tokenLabel",
    },
)
class ManagedKeysPkcs:
    def __init__(
        self,
        *,
        key_id: builtins.str,
        key_label: builtins.str,
        library: builtins.str,
        mechanism: builtins.str,
        name: builtins.str,
        pin: builtins.str,
        allow_generate_key: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_replace_key: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_store_key: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        any_mount: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        curve: typing.Optional[builtins.str] = None,
        force_rw_session: typing.Optional[builtins.str] = None,
        key_bits: typing.Optional[builtins.str] = None,
        slot: typing.Optional[builtins.str] = None,
        token_label: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key_id: The id of a PKCS#11 key to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#key_id ManagedKeys#key_id}
        :param key_label: The label of the key to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#key_label ManagedKeys#key_label}
        :param library: The name of the kms_library stanza to use from Vault's config to lookup the local library path. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#library ManagedKeys#library}
        :param mechanism: The encryption/decryption mechanism to use, specified as a hexadecimal (prefixed by 0x) string. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#mechanism ManagedKeys#mechanism}
        :param name: A unique lowercase name that serves as identifying the key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#name ManagedKeys#name}
        :param pin: The PIN for login. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#pin ManagedKeys#pin}
        :param allow_generate_key: If no existing key can be found in the referenced backend, instructs Vault to generate a key within the backend. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#allow_generate_key ManagedKeys#allow_generate_key}
        :param allow_replace_key: Controls the ability for Vault to replace through generation or importing a key into the configured backend even if a key is present, if set to false those operations are forbidden if a key exists. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#allow_replace_key ManagedKeys#allow_replace_key}
        :param allow_store_key: Controls the ability for Vault to import a key to the configured backend, if 'false', those operations will be forbidden. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#allow_store_key ManagedKeys#allow_store_key}
        :param any_mount: Allow usage from any mount point within the namespace if 'true'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#any_mount ManagedKeys#any_mount}
        :param curve: Supplies the curve value when using the 'CKM_ECDSA' mechanism. Required if 'allow_generate_key' is true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#curve ManagedKeys#curve}
        :param force_rw_session: Force all operations to open up a read-write session to the HSM. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#force_rw_session ManagedKeys#force_rw_session}
        :param key_bits: Supplies the size in bits of the key when using 'CKM_RSA_PKCS_PSS', 'CKM_RSA_PKCS_OAEP' or 'CKM_RSA_PKCS' as a value for 'mechanism'. Required if 'allow_generate_key' is true Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#key_bits ManagedKeys#key_bits}
        :param slot: The slot number to use, specified as a string in a decimal format (e.g. '2305843009213693953'). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#slot ManagedKeys#slot}
        :param token_label: The slot token label to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#token_label ManagedKeys#token_label}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedKeysPkcs.__init__)
            check_type(argname="argument key_id", value=key_id, expected_type=type_hints["key_id"])
            check_type(argname="argument key_label", value=key_label, expected_type=type_hints["key_label"])
            check_type(argname="argument library", value=library, expected_type=type_hints["library"])
            check_type(argname="argument mechanism", value=mechanism, expected_type=type_hints["mechanism"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument pin", value=pin, expected_type=type_hints["pin"])
            check_type(argname="argument allow_generate_key", value=allow_generate_key, expected_type=type_hints["allow_generate_key"])
            check_type(argname="argument allow_replace_key", value=allow_replace_key, expected_type=type_hints["allow_replace_key"])
            check_type(argname="argument allow_store_key", value=allow_store_key, expected_type=type_hints["allow_store_key"])
            check_type(argname="argument any_mount", value=any_mount, expected_type=type_hints["any_mount"])
            check_type(argname="argument curve", value=curve, expected_type=type_hints["curve"])
            check_type(argname="argument force_rw_session", value=force_rw_session, expected_type=type_hints["force_rw_session"])
            check_type(argname="argument key_bits", value=key_bits, expected_type=type_hints["key_bits"])
            check_type(argname="argument slot", value=slot, expected_type=type_hints["slot"])
            check_type(argname="argument token_label", value=token_label, expected_type=type_hints["token_label"])
        self._values: typing.Dict[str, typing.Any] = {
            "key_id": key_id,
            "key_label": key_label,
            "library": library,
            "mechanism": mechanism,
            "name": name,
            "pin": pin,
        }
        if allow_generate_key is not None:
            self._values["allow_generate_key"] = allow_generate_key
        if allow_replace_key is not None:
            self._values["allow_replace_key"] = allow_replace_key
        if allow_store_key is not None:
            self._values["allow_store_key"] = allow_store_key
        if any_mount is not None:
            self._values["any_mount"] = any_mount
        if curve is not None:
            self._values["curve"] = curve
        if force_rw_session is not None:
            self._values["force_rw_session"] = force_rw_session
        if key_bits is not None:
            self._values["key_bits"] = key_bits
        if slot is not None:
            self._values["slot"] = slot
        if token_label is not None:
            self._values["token_label"] = token_label

    @builtins.property
    def key_id(self) -> builtins.str:
        '''The id of a PKCS#11 key to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#key_id ManagedKeys#key_id}
        '''
        result = self._values.get("key_id")
        assert result is not None, "Required property 'key_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key_label(self) -> builtins.str:
        '''The label of the key to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#key_label ManagedKeys#key_label}
        '''
        result = self._values.get("key_label")
        assert result is not None, "Required property 'key_label' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def library(self) -> builtins.str:
        '''The name of the kms_library stanza to use from Vault's config to lookup the local library path.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#library ManagedKeys#library}
        '''
        result = self._values.get("library")
        assert result is not None, "Required property 'library' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mechanism(self) -> builtins.str:
        '''The encryption/decryption mechanism to use, specified as a hexadecimal (prefixed by 0x) string.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#mechanism ManagedKeys#mechanism}
        '''
        result = self._values.get("mechanism")
        assert result is not None, "Required property 'mechanism' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A unique lowercase name that serves as identifying the key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#name ManagedKeys#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pin(self) -> builtins.str:
        '''The PIN for login.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#pin ManagedKeys#pin}
        '''
        result = self._values.get("pin")
        assert result is not None, "Required property 'pin' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_generate_key(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If no existing key can be found in the referenced backend, instructs Vault to generate a key within the backend.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#allow_generate_key ManagedKeys#allow_generate_key}
        '''
        result = self._values.get("allow_generate_key")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_replace_key(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Controls the ability for Vault to replace through generation or importing a key into the configured backend even if a key is present, if set to false those operations are forbidden if a key exists.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#allow_replace_key ManagedKeys#allow_replace_key}
        '''
        result = self._values.get("allow_replace_key")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_store_key(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Controls the ability for Vault to import a key to the configured backend, if 'false', those operations will be forbidden.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#allow_store_key ManagedKeys#allow_store_key}
        '''
        result = self._values.get("allow_store_key")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def any_mount(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Allow usage from any mount point within the namespace if 'true'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#any_mount ManagedKeys#any_mount}
        '''
        result = self._values.get("any_mount")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def curve(self) -> typing.Optional[builtins.str]:
        '''Supplies the curve value when using the 'CKM_ECDSA' mechanism. Required if 'allow_generate_key' is true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#curve ManagedKeys#curve}
        '''
        result = self._values.get("curve")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def force_rw_session(self) -> typing.Optional[builtins.str]:
        '''Force all operations to open up a read-write session to the HSM.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#force_rw_session ManagedKeys#force_rw_session}
        '''
        result = self._values.get("force_rw_session")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_bits(self) -> typing.Optional[builtins.str]:
        '''Supplies the size in bits of the key when using 'CKM_RSA_PKCS_PSS', 'CKM_RSA_PKCS_OAEP' or 'CKM_RSA_PKCS' as a value for 'mechanism'.

        Required if 'allow_generate_key' is true

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#key_bits ManagedKeys#key_bits}
        '''
        result = self._values.get("key_bits")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def slot(self) -> typing.Optional[builtins.str]:
        '''The slot number to use, specified as a string in a decimal format (e.g. '2305843009213693953').

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#slot ManagedKeys#slot}
        '''
        result = self._values.get("slot")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def token_label(self) -> typing.Optional[builtins.str]:
        '''The slot token label to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vault/r/managed_keys#token_label ManagedKeys#token_label}
        '''
        result = self._values.get("token_label")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ManagedKeysPkcs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ManagedKeysPkcsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.managedKeys.ManagedKeysPkcsList",
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
            type_hints = typing.get_type_hints(ManagedKeysPkcsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "ManagedKeysPkcsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ManagedKeysPkcsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("ManagedKeysPkcsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysPkcsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(ManagedKeysPkcsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(ManagedKeysPkcsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedKeysPkcs]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedKeysPkcs]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[ManagedKeysPkcs]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysPkcsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class ManagedKeysPkcsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vault.managedKeys.ManagedKeysPkcsOutputReference",
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
            type_hints = typing.get_type_hints(ManagedKeysPkcsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAllowGenerateKey")
    def reset_allow_generate_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowGenerateKey", []))

    @jsii.member(jsii_name="resetAllowReplaceKey")
    def reset_allow_replace_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowReplaceKey", []))

    @jsii.member(jsii_name="resetAllowStoreKey")
    def reset_allow_store_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowStoreKey", []))

    @jsii.member(jsii_name="resetAnyMount")
    def reset_any_mount(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnyMount", []))

    @jsii.member(jsii_name="resetCurve")
    def reset_curve(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCurve", []))

    @jsii.member(jsii_name="resetForceRwSession")
    def reset_force_rw_session(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceRwSession", []))

    @jsii.member(jsii_name="resetKeyBits")
    def reset_key_bits(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyBits", []))

    @jsii.member(jsii_name="resetSlot")
    def reset_slot(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSlot", []))

    @jsii.member(jsii_name="resetTokenLabel")
    def reset_token_label(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTokenLabel", []))

    @builtins.property
    @jsii.member(jsii_name="uuid")
    def uuid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uuid"))

    @builtins.property
    @jsii.member(jsii_name="allowGenerateKeyInput")
    def allow_generate_key_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowGenerateKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="allowReplaceKeyInput")
    def allow_replace_key_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowReplaceKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="allowStoreKeyInput")
    def allow_store_key_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowStoreKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="anyMountInput")
    def any_mount_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "anyMountInput"))

    @builtins.property
    @jsii.member(jsii_name="curveInput")
    def curve_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "curveInput"))

    @builtins.property
    @jsii.member(jsii_name="forceRwSessionInput")
    def force_rw_session_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "forceRwSessionInput"))

    @builtins.property
    @jsii.member(jsii_name="keyBitsInput")
    def key_bits_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyBitsInput"))

    @builtins.property
    @jsii.member(jsii_name="keyIdInput")
    def key_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyIdInput"))

    @builtins.property
    @jsii.member(jsii_name="keyLabelInput")
    def key_label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyLabelInput"))

    @builtins.property
    @jsii.member(jsii_name="libraryInput")
    def library_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "libraryInput"))

    @builtins.property
    @jsii.member(jsii_name="mechanismInput")
    def mechanism_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mechanismInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="pinInput")
    def pin_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pinInput"))

    @builtins.property
    @jsii.member(jsii_name="slotInput")
    def slot_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "slotInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenLabelInput")
    def token_label_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenLabelInput"))

    @builtins.property
    @jsii.member(jsii_name="allowGenerateKey")
    def allow_generate_key(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowGenerateKey"))

    @allow_generate_key.setter
    def allow_generate_key(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysPkcsOutputReference, "allow_generate_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowGenerateKey", value)

    @builtins.property
    @jsii.member(jsii_name="allowReplaceKey")
    def allow_replace_key(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowReplaceKey"))

    @allow_replace_key.setter
    def allow_replace_key(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysPkcsOutputReference, "allow_replace_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowReplaceKey", value)

    @builtins.property
    @jsii.member(jsii_name="allowStoreKey")
    def allow_store_key(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowStoreKey"))

    @allow_store_key.setter
    def allow_store_key(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysPkcsOutputReference, "allow_store_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowStoreKey", value)

    @builtins.property
    @jsii.member(jsii_name="anyMount")
    def any_mount(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "anyMount"))

    @any_mount.setter
    def any_mount(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysPkcsOutputReference, "any_mount").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "anyMount", value)

    @builtins.property
    @jsii.member(jsii_name="curve")
    def curve(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "curve"))

    @curve.setter
    def curve(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysPkcsOutputReference, "curve").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "curve", value)

    @builtins.property
    @jsii.member(jsii_name="forceRwSession")
    def force_rw_session(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "forceRwSession"))

    @force_rw_session.setter
    def force_rw_session(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysPkcsOutputReference, "force_rw_session").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceRwSession", value)

    @builtins.property
    @jsii.member(jsii_name="keyBits")
    def key_bits(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyBits"))

    @key_bits.setter
    def key_bits(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysPkcsOutputReference, "key_bits").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyBits", value)

    @builtins.property
    @jsii.member(jsii_name="keyId")
    def key_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyId"))

    @key_id.setter
    def key_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysPkcsOutputReference, "key_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyId", value)

    @builtins.property
    @jsii.member(jsii_name="keyLabel")
    def key_label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyLabel"))

    @key_label.setter
    def key_label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysPkcsOutputReference, "key_label").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyLabel", value)

    @builtins.property
    @jsii.member(jsii_name="library")
    def library(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "library"))

    @library.setter
    def library(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysPkcsOutputReference, "library").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "library", value)

    @builtins.property
    @jsii.member(jsii_name="mechanism")
    def mechanism(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mechanism"))

    @mechanism.setter
    def mechanism(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysPkcsOutputReference, "mechanism").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mechanism", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysPkcsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="pin")
    def pin(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "pin"))

    @pin.setter
    def pin(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysPkcsOutputReference, "pin").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pin", value)

    @builtins.property
    @jsii.member(jsii_name="slot")
    def slot(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "slot"))

    @slot.setter
    def slot(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysPkcsOutputReference, "slot").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "slot", value)

    @builtins.property
    @jsii.member(jsii_name="tokenLabel")
    def token_label(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tokenLabel"))

    @token_label.setter
    def token_label(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysPkcsOutputReference, "token_label").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tokenLabel", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[ManagedKeysPkcs, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[ManagedKeysPkcs, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[ManagedKeysPkcs, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ManagedKeysPkcsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ManagedKeys",
    "ManagedKeysAws",
    "ManagedKeysAwsList",
    "ManagedKeysAwsOutputReference",
    "ManagedKeysAzure",
    "ManagedKeysAzureList",
    "ManagedKeysAzureOutputReference",
    "ManagedKeysConfig",
    "ManagedKeysPkcs",
    "ManagedKeysPkcsList",
    "ManagedKeysPkcsOutputReference",
]

publication.publish()
