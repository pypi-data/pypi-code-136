'''
# `cloudflare_custom_ssl`

Refer to the Terraform Registory for docs: [`cloudflare_custom_ssl`](https://www.terraform.io/docs/providers/cloudflare/r/custom_ssl).
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


class CustomSsl(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.customSsl.CustomSsl",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/cloudflare/r/custom_ssl cloudflare_custom_ssl}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        zone_id: builtins.str,
        custom_ssl_options: typing.Optional[typing.Union["CustomSslCustomSslOptions", typing.Dict[str, typing.Any]]] = None,
        custom_ssl_priority: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CustomSslCustomSslPriority", typing.Dict[str, typing.Any]]]]] = None,
        id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/cloudflare/r/custom_ssl cloudflare_custom_ssl} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param zone_id: The zone identifier to target for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/custom_ssl#zone_id CustomSsl#zone_id}
        :param custom_ssl_options: custom_ssl_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/custom_ssl#custom_ssl_options CustomSsl#custom_ssl_options}
        :param custom_ssl_priority: custom_ssl_priority block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/custom_ssl#custom_ssl_priority CustomSsl#custom_ssl_priority}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/custom_ssl#id CustomSsl#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CustomSsl.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = CustomSslConfig(
            zone_id=zone_id,
            custom_ssl_options=custom_ssl_options,
            custom_ssl_priority=custom_ssl_priority,
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

    @jsii.member(jsii_name="putCustomSslOptions")
    def put_custom_ssl_options(
        self,
        *,
        bundle_method: typing.Optional[builtins.str] = None,
        certificate: typing.Optional[builtins.str] = None,
        geo_restrictions: typing.Optional[builtins.str] = None,
        private_key: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bundle_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/custom_ssl#bundle_method CustomSsl#bundle_method}.
        :param certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/custom_ssl#certificate CustomSsl#certificate}.
        :param geo_restrictions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/custom_ssl#geo_restrictions CustomSsl#geo_restrictions}.
        :param private_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/custom_ssl#private_key CustomSsl#private_key}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/custom_ssl#type CustomSsl#type}.
        '''
        value = CustomSslCustomSslOptions(
            bundle_method=bundle_method,
            certificate=certificate,
            geo_restrictions=geo_restrictions,
            private_key=private_key,
            type=type,
        )

        return typing.cast(None, jsii.invoke(self, "putCustomSslOptions", [value]))

    @jsii.member(jsii_name="putCustomSslPriority")
    def put_custom_ssl_priority(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CustomSslCustomSslPriority", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CustomSsl.put_custom_ssl_priority)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCustomSslPriority", [value]))

    @jsii.member(jsii_name="resetCustomSslOptions")
    def reset_custom_ssl_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomSslOptions", []))

    @jsii.member(jsii_name="resetCustomSslPriority")
    def reset_custom_ssl_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomSslPriority", []))

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
    @jsii.member(jsii_name="customSslOptions")
    def custom_ssl_options(self) -> "CustomSslCustomSslOptionsOutputReference":
        return typing.cast("CustomSslCustomSslOptionsOutputReference", jsii.get(self, "customSslOptions"))

    @builtins.property
    @jsii.member(jsii_name="customSslPriority")
    def custom_ssl_priority(self) -> "CustomSslCustomSslPriorityList":
        return typing.cast("CustomSslCustomSslPriorityList", jsii.get(self, "customSslPriority"))

    @builtins.property
    @jsii.member(jsii_name="expiresOn")
    def expires_on(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expiresOn"))

    @builtins.property
    @jsii.member(jsii_name="hosts")
    def hosts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "hosts"))

    @builtins.property
    @jsii.member(jsii_name="issuer")
    def issuer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "issuer"))

    @builtins.property
    @jsii.member(jsii_name="modifiedOn")
    def modified_on(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "modifiedOn"))

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @builtins.property
    @jsii.member(jsii_name="signature")
    def signature(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signature"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="uploadedOn")
    def uploaded_on(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "uploadedOn"))

    @builtins.property
    @jsii.member(jsii_name="customSslOptionsInput")
    def custom_ssl_options_input(self) -> typing.Optional["CustomSslCustomSslOptions"]:
        return typing.cast(typing.Optional["CustomSslCustomSslOptions"], jsii.get(self, "customSslOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="customSslPriorityInput")
    def custom_ssl_priority_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CustomSslCustomSslPriority"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CustomSslCustomSslPriority"]]], jsii.get(self, "customSslPriorityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneIdInput")
    def zone_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneIdInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CustomSsl, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="zoneId")
    def zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zoneId"))

    @zone_id.setter
    def zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CustomSsl, "zone_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.customSsl.CustomSslConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "zone_id": "zoneId",
        "custom_ssl_options": "customSslOptions",
        "custom_ssl_priority": "customSslPriority",
        "id": "id",
    },
)
class CustomSslConfig(cdktf.TerraformMetaArguments):
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
        zone_id: builtins.str,
        custom_ssl_options: typing.Optional[typing.Union["CustomSslCustomSslOptions", typing.Dict[str, typing.Any]]] = None,
        custom_ssl_priority: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["CustomSslCustomSslPriority", typing.Dict[str, typing.Any]]]]] = None,
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
        :param zone_id: The zone identifier to target for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/custom_ssl#zone_id CustomSsl#zone_id}
        :param custom_ssl_options: custom_ssl_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/custom_ssl#custom_ssl_options CustomSsl#custom_ssl_options}
        :param custom_ssl_priority: custom_ssl_priority block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/custom_ssl#custom_ssl_priority CustomSsl#custom_ssl_priority}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/custom_ssl#id CustomSsl#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(custom_ssl_options, dict):
            custom_ssl_options = CustomSslCustomSslOptions(**custom_ssl_options)
        if __debug__:
            type_hints = typing.get_type_hints(CustomSslConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument zone_id", value=zone_id, expected_type=type_hints["zone_id"])
            check_type(argname="argument custom_ssl_options", value=custom_ssl_options, expected_type=type_hints["custom_ssl_options"])
            check_type(argname="argument custom_ssl_priority", value=custom_ssl_priority, expected_type=type_hints["custom_ssl_priority"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        self._values: typing.Dict[str, typing.Any] = {
            "zone_id": zone_id,
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
        if custom_ssl_options is not None:
            self._values["custom_ssl_options"] = custom_ssl_options
        if custom_ssl_priority is not None:
            self._values["custom_ssl_priority"] = custom_ssl_priority
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
    def zone_id(self) -> builtins.str:
        '''The zone identifier to target for the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/custom_ssl#zone_id CustomSsl#zone_id}
        '''
        result = self._values.get("zone_id")
        assert result is not None, "Required property 'zone_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_ssl_options(self) -> typing.Optional["CustomSslCustomSslOptions"]:
        '''custom_ssl_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/custom_ssl#custom_ssl_options CustomSsl#custom_ssl_options}
        '''
        result = self._values.get("custom_ssl_options")
        return typing.cast(typing.Optional["CustomSslCustomSslOptions"], result)

    @builtins.property
    def custom_ssl_priority(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CustomSslCustomSslPriority"]]]:
        '''custom_ssl_priority block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/custom_ssl#custom_ssl_priority CustomSsl#custom_ssl_priority}
        '''
        result = self._values.get("custom_ssl_priority")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["CustomSslCustomSslPriority"]]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/custom_ssl#id CustomSsl#id}.

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
        return "CustomSslConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.customSsl.CustomSslCustomSslOptions",
    jsii_struct_bases=[],
    name_mapping={
        "bundle_method": "bundleMethod",
        "certificate": "certificate",
        "geo_restrictions": "geoRestrictions",
        "private_key": "privateKey",
        "type": "type",
    },
)
class CustomSslCustomSslOptions:
    def __init__(
        self,
        *,
        bundle_method: typing.Optional[builtins.str] = None,
        certificate: typing.Optional[builtins.str] = None,
        geo_restrictions: typing.Optional[builtins.str] = None,
        private_key: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bundle_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/custom_ssl#bundle_method CustomSsl#bundle_method}.
        :param certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/custom_ssl#certificate CustomSsl#certificate}.
        :param geo_restrictions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/custom_ssl#geo_restrictions CustomSsl#geo_restrictions}.
        :param private_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/custom_ssl#private_key CustomSsl#private_key}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/custom_ssl#type CustomSsl#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CustomSslCustomSslOptions.__init__)
            check_type(argname="argument bundle_method", value=bundle_method, expected_type=type_hints["bundle_method"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument geo_restrictions", value=geo_restrictions, expected_type=type_hints["geo_restrictions"])
            check_type(argname="argument private_key", value=private_key, expected_type=type_hints["private_key"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if bundle_method is not None:
            self._values["bundle_method"] = bundle_method
        if certificate is not None:
            self._values["certificate"] = certificate
        if geo_restrictions is not None:
            self._values["geo_restrictions"] = geo_restrictions
        if private_key is not None:
            self._values["private_key"] = private_key
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def bundle_method(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/custom_ssl#bundle_method CustomSsl#bundle_method}.'''
        result = self._values.get("bundle_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/custom_ssl#certificate CustomSsl#certificate}.'''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def geo_restrictions(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/custom_ssl#geo_restrictions CustomSsl#geo_restrictions}.'''
        result = self._values.get("geo_restrictions")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/custom_ssl#private_key CustomSsl#private_key}.'''
        result = self._values.get("private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/custom_ssl#type CustomSsl#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomSslCustomSslOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CustomSslCustomSslOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.customSsl.CustomSslCustomSslOptionsOutputReference",
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
            type_hints = typing.get_type_hints(CustomSslCustomSslOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBundleMethod")
    def reset_bundle_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBundleMethod", []))

    @jsii.member(jsii_name="resetCertificate")
    def reset_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificate", []))

    @jsii.member(jsii_name="resetGeoRestrictions")
    def reset_geo_restrictions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGeoRestrictions", []))

    @jsii.member(jsii_name="resetPrivateKey")
    def reset_private_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateKey", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="bundleMethodInput")
    def bundle_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bundleMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="geoRestrictionsInput")
    def geo_restrictions_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "geoRestrictionsInput"))

    @builtins.property
    @jsii.member(jsii_name="privateKeyInput")
    def private_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="bundleMethod")
    def bundle_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bundleMethod"))

    @bundle_method.setter
    def bundle_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CustomSslCustomSslOptionsOutputReference, "bundle_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bundleMethod", value)

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CustomSslCustomSslOptionsOutputReference, "certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificate", value)

    @builtins.property
    @jsii.member(jsii_name="geoRestrictions")
    def geo_restrictions(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "geoRestrictions"))

    @geo_restrictions.setter
    def geo_restrictions(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CustomSslCustomSslOptionsOutputReference, "geo_restrictions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "geoRestrictions", value)

    @builtins.property
    @jsii.member(jsii_name="privateKey")
    def private_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "privateKey"))

    @private_key.setter
    def private_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CustomSslCustomSslOptionsOutputReference, "private_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKey", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CustomSslCustomSslOptionsOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[CustomSslCustomSslOptions]:
        return typing.cast(typing.Optional[CustomSslCustomSslOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[CustomSslCustomSslOptions]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CustomSslCustomSslOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.customSsl.CustomSslCustomSslPriority",
    jsii_struct_bases=[],
    name_mapping={"id": "id", "priority": "priority"},
)
class CustomSslCustomSslPriority:
    def __init__(
        self,
        *,
        id: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/custom_ssl#id CustomSsl#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/custom_ssl#priority CustomSsl#priority}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CustomSslCustomSslPriority.__init__)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
        self._values: typing.Dict[str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if priority is not None:
            self._values["priority"] = priority

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/custom_ssl#id CustomSsl#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/custom_ssl#priority CustomSsl#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomSslCustomSslPriority(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CustomSslCustomSslPriorityList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.customSsl.CustomSslCustomSslPriorityList",
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
            type_hints = typing.get_type_hints(CustomSslCustomSslPriorityList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "CustomSslCustomSslPriorityOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(CustomSslCustomSslPriorityList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("CustomSslCustomSslPriorityOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CustomSslCustomSslPriorityList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(CustomSslCustomSslPriorityList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(CustomSslCustomSslPriorityList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CustomSslCustomSslPriority]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CustomSslCustomSslPriority]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[CustomSslCustomSslPriority]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CustomSslCustomSslPriorityList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class CustomSslCustomSslPriorityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.customSsl.CustomSslCustomSslPriorityOutputReference",
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
            type_hints = typing.get_type_hints(CustomSslCustomSslPriorityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CustomSslCustomSslPriorityOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CustomSslCustomSslPriorityOutputReference, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[CustomSslCustomSslPriority, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[CustomSslCustomSslPriority, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[CustomSslCustomSslPriority, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(CustomSslCustomSslPriorityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "CustomSsl",
    "CustomSslConfig",
    "CustomSslCustomSslOptions",
    "CustomSslCustomSslOptionsOutputReference",
    "CustomSslCustomSslPriority",
    "CustomSslCustomSslPriorityList",
    "CustomSslCustomSslPriorityOutputReference",
]

publication.publish()
