'''
# `cloudflare_record`

Refer to the Terraform Registory for docs: [`cloudflare_record`](https://www.terraform.io/docs/providers/cloudflare/r/record).
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


class Record(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.record.Record",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/cloudflare/r/record cloudflare_record}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        type: builtins.str,
        zone_id: builtins.str,
        allow_overwrite: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        data: typing.Optional[typing.Union["RecordData", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        proxied: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["RecordTimeouts", typing.Dict[str, typing.Any]]] = None,
        ttl: typing.Optional[jsii.Number] = None,
        value: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/cloudflare/r/record cloudflare_record} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#name Record#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#type Record#type}.
        :param zone_id: The zone identifier to target for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#zone_id Record#zone_id}
        :param allow_overwrite: Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#allow_overwrite Record#allow_overwrite}
        :param data: data block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#data Record#data}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#id Record#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#priority Record#priority}.
        :param proxied: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#proxied Record#proxied}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#timeouts Record#timeouts}
        :param ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#ttl Record#ttl}.
        :param value: Conflicts with ``data``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#value Record#value}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Record.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = RecordConfig(
            name=name,
            type=type,
            zone_id=zone_id,
            allow_overwrite=allow_overwrite,
            data=data,
            id=id,
            priority=priority,
            proxied=proxied,
            timeouts=timeouts,
            ttl=ttl,
            value=value,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putData")
    def put_data(
        self,
        *,
        algorithm: typing.Optional[jsii.Number] = None,
        altitude: typing.Optional[jsii.Number] = None,
        certificate: typing.Optional[builtins.str] = None,
        content: typing.Optional[builtins.str] = None,
        digest: typing.Optional[builtins.str] = None,
        digest_type: typing.Optional[jsii.Number] = None,
        fingerprint: typing.Optional[builtins.str] = None,
        flags: typing.Optional[builtins.str] = None,
        key_tag: typing.Optional[jsii.Number] = None,
        lat_degrees: typing.Optional[jsii.Number] = None,
        lat_direction: typing.Optional[builtins.str] = None,
        lat_minutes: typing.Optional[jsii.Number] = None,
        lat_seconds: typing.Optional[jsii.Number] = None,
        long_degrees: typing.Optional[jsii.Number] = None,
        long_direction: typing.Optional[builtins.str] = None,
        long_minutes: typing.Optional[jsii.Number] = None,
        long_seconds: typing.Optional[jsii.Number] = None,
        matching_type: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        order: typing.Optional[jsii.Number] = None,
        port: typing.Optional[jsii.Number] = None,
        precision_horz: typing.Optional[jsii.Number] = None,
        precision_vert: typing.Optional[jsii.Number] = None,
        preference: typing.Optional[jsii.Number] = None,
        priority: typing.Optional[jsii.Number] = None,
        proto: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[jsii.Number] = None,
        public_key: typing.Optional[builtins.str] = None,
        regex: typing.Optional[builtins.str] = None,
        replacement: typing.Optional[builtins.str] = None,
        selector: typing.Optional[jsii.Number] = None,
        service: typing.Optional[builtins.str] = None,
        size: typing.Optional[jsii.Number] = None,
        tag: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
        type: typing.Optional[jsii.Number] = None,
        usage: typing.Optional[jsii.Number] = None,
        value: typing.Optional[builtins.str] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param algorithm: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#algorithm Record#algorithm}.
        :param altitude: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#altitude Record#altitude}.
        :param certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#certificate Record#certificate}.
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#content Record#content}.
        :param digest: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#digest Record#digest}.
        :param digest_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#digest_type Record#digest_type}.
        :param fingerprint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#fingerprint Record#fingerprint}.
        :param flags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#flags Record#flags}.
        :param key_tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#key_tag Record#key_tag}.
        :param lat_degrees: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#lat_degrees Record#lat_degrees}.
        :param lat_direction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#lat_direction Record#lat_direction}.
        :param lat_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#lat_minutes Record#lat_minutes}.
        :param lat_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#lat_seconds Record#lat_seconds}.
        :param long_degrees: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#long_degrees Record#long_degrees}.
        :param long_direction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#long_direction Record#long_direction}.
        :param long_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#long_minutes Record#long_minutes}.
        :param long_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#long_seconds Record#long_seconds}.
        :param matching_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#matching_type Record#matching_type}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#name Record#name}.
        :param order: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#order Record#order}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#port Record#port}.
        :param precision_horz: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#precision_horz Record#precision_horz}.
        :param precision_vert: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#precision_vert Record#precision_vert}.
        :param preference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#preference Record#preference}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#priority Record#priority}.
        :param proto: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#proto Record#proto}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#protocol Record#protocol}.
        :param public_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#public_key Record#public_key}.
        :param regex: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#regex Record#regex}.
        :param replacement: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#replacement Record#replacement}.
        :param selector: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#selector Record#selector}.
        :param service: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#service Record#service}.
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#size Record#size}.
        :param tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#tag Record#tag}.
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#target Record#target}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#type Record#type}.
        :param usage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#usage Record#usage}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#value Record#value}.
        :param weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#weight Record#weight}.
        '''
        value_ = RecordData(
            algorithm=algorithm,
            altitude=altitude,
            certificate=certificate,
            content=content,
            digest=digest,
            digest_type=digest_type,
            fingerprint=fingerprint,
            flags=flags,
            key_tag=key_tag,
            lat_degrees=lat_degrees,
            lat_direction=lat_direction,
            lat_minutes=lat_minutes,
            lat_seconds=lat_seconds,
            long_degrees=long_degrees,
            long_direction=long_direction,
            long_minutes=long_minutes,
            long_seconds=long_seconds,
            matching_type=matching_type,
            name=name,
            order=order,
            port=port,
            precision_horz=precision_horz,
            precision_vert=precision_vert,
            preference=preference,
            priority=priority,
            proto=proto,
            protocol=protocol,
            public_key=public_key,
            regex=regex,
            replacement=replacement,
            selector=selector,
            service=service,
            size=size,
            tag=tag,
            target=target,
            type=type,
            usage=usage,
            value=value,
            weight=weight,
        )

        return typing.cast(None, jsii.invoke(self, "putData", [value_]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#create Record#create}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#update Record#update}.
        '''
        value = RecordTimeouts(create=create, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAllowOverwrite")
    def reset_allow_overwrite(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowOverwrite", []))

    @jsii.member(jsii_name="resetData")
    def reset_data(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetData", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetProxied")
    def reset_proxied(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProxied", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetTtl")
    def reset_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTtl", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="createdOn")
    def created_on(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdOn"))

    @builtins.property
    @jsii.member(jsii_name="data")
    def data(self) -> "RecordDataOutputReference":
        return typing.cast("RecordDataOutputReference", jsii.get(self, "data"))

    @builtins.property
    @jsii.member(jsii_name="hostname")
    def hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "hostname"))

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> cdktf.StringMap:
        return typing.cast(cdktf.StringMap, jsii.get(self, "metadata"))

    @builtins.property
    @jsii.member(jsii_name="modifiedOn")
    def modified_on(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "modifiedOn"))

    @builtins.property
    @jsii.member(jsii_name="proxiable")
    def proxiable(self) -> cdktf.IResolvable:
        return typing.cast(cdktf.IResolvable, jsii.get(self, "proxiable"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "RecordTimeoutsOutputReference":
        return typing.cast("RecordTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="allowOverwriteInput")
    def allow_overwrite_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowOverwriteInput"))

    @builtins.property
    @jsii.member(jsii_name="dataInput")
    def data_input(self) -> typing.Optional["RecordData"]:
        return typing.cast(typing.Optional["RecordData"], jsii.get(self, "dataInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="proxiedInput")
    def proxied_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "proxiedInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["RecordTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["RecordTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="ttlInput")
    def ttl_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ttlInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneIdInput")
    def zone_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneIdInput"))

    @builtins.property
    @jsii.member(jsii_name="allowOverwrite")
    def allow_overwrite(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowOverwrite"))

    @allow_overwrite.setter
    def allow_overwrite(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Record, "allow_overwrite").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowOverwrite", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Record, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Record, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Record, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="proxied")
    def proxied(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "proxied"))

    @proxied.setter
    def proxied(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Record, "proxied").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "proxied", value)

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "ttl"))

    @ttl.setter
    def ttl(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Record, "ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ttl", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Record, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Record, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="zoneId")
    def zone_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zoneId"))

    @zone_id.setter
    def zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Record, "zone_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zoneId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.record.RecordConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "name": "name",
        "type": "type",
        "zone_id": "zoneId",
        "allow_overwrite": "allowOverwrite",
        "data": "data",
        "id": "id",
        "priority": "priority",
        "proxied": "proxied",
        "timeouts": "timeouts",
        "ttl": "ttl",
        "value": "value",
    },
)
class RecordConfig(cdktf.TerraformMetaArguments):
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
        name: builtins.str,
        type: builtins.str,
        zone_id: builtins.str,
        allow_overwrite: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        data: typing.Optional[typing.Union["RecordData", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        priority: typing.Optional[jsii.Number] = None,
        proxied: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["RecordTimeouts", typing.Dict[str, typing.Any]]] = None,
        ttl: typing.Optional[jsii.Number] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#name Record#name}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#type Record#type}.
        :param zone_id: The zone identifier to target for the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#zone_id Record#zone_id}
        :param allow_overwrite: Defaults to ``false``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#allow_overwrite Record#allow_overwrite}
        :param data: data block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#data Record#data}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#id Record#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#priority Record#priority}.
        :param proxied: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#proxied Record#proxied}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#timeouts Record#timeouts}
        :param ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#ttl Record#ttl}.
        :param value: Conflicts with ``data``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#value Record#value}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(data, dict):
            data = RecordData(**data)
        if isinstance(timeouts, dict):
            timeouts = RecordTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(RecordConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument zone_id", value=zone_id, expected_type=type_hints["zone_id"])
            check_type(argname="argument allow_overwrite", value=allow_overwrite, expected_type=type_hints["allow_overwrite"])
            check_type(argname="argument data", value=data, expected_type=type_hints["data"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument proxied", value=proxied, expected_type=type_hints["proxied"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "type": type,
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
        if allow_overwrite is not None:
            self._values["allow_overwrite"] = allow_overwrite
        if data is not None:
            self._values["data"] = data
        if id is not None:
            self._values["id"] = id
        if priority is not None:
            self._values["priority"] = priority
        if proxied is not None:
            self._values["proxied"] = proxied
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if ttl is not None:
            self._values["ttl"] = ttl
        if value is not None:
            self._values["value"] = value

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
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#name Record#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#type Record#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def zone_id(self) -> builtins.str:
        '''The zone identifier to target for the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#zone_id Record#zone_id}
        '''
        result = self._values.get("zone_id")
        assert result is not None, "Required property 'zone_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_overwrite(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Defaults to ``false``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#allow_overwrite Record#allow_overwrite}
        '''
        result = self._values.get("allow_overwrite")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def data(self) -> typing.Optional["RecordData"]:
        '''data block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#data Record#data}
        '''
        result = self._values.get("data")
        return typing.cast(typing.Optional["RecordData"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#id Record#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#priority Record#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def proxied(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#proxied Record#proxied}.'''
        result = self._values.get("proxied")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["RecordTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#timeouts Record#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["RecordTimeouts"], result)

    @builtins.property
    def ttl(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#ttl Record#ttl}.'''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Conflicts with ``data``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#value Record#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RecordConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.record.RecordData",
    jsii_struct_bases=[],
    name_mapping={
        "algorithm": "algorithm",
        "altitude": "altitude",
        "certificate": "certificate",
        "content": "content",
        "digest": "digest",
        "digest_type": "digestType",
        "fingerprint": "fingerprint",
        "flags": "flags",
        "key_tag": "keyTag",
        "lat_degrees": "latDegrees",
        "lat_direction": "latDirection",
        "lat_minutes": "latMinutes",
        "lat_seconds": "latSeconds",
        "long_degrees": "longDegrees",
        "long_direction": "longDirection",
        "long_minutes": "longMinutes",
        "long_seconds": "longSeconds",
        "matching_type": "matchingType",
        "name": "name",
        "order": "order",
        "port": "port",
        "precision_horz": "precisionHorz",
        "precision_vert": "precisionVert",
        "preference": "preference",
        "priority": "priority",
        "proto": "proto",
        "protocol": "protocol",
        "public_key": "publicKey",
        "regex": "regex",
        "replacement": "replacement",
        "selector": "selector",
        "service": "service",
        "size": "size",
        "tag": "tag",
        "target": "target",
        "type": "type",
        "usage": "usage",
        "value": "value",
        "weight": "weight",
    },
)
class RecordData:
    def __init__(
        self,
        *,
        algorithm: typing.Optional[jsii.Number] = None,
        altitude: typing.Optional[jsii.Number] = None,
        certificate: typing.Optional[builtins.str] = None,
        content: typing.Optional[builtins.str] = None,
        digest: typing.Optional[builtins.str] = None,
        digest_type: typing.Optional[jsii.Number] = None,
        fingerprint: typing.Optional[builtins.str] = None,
        flags: typing.Optional[builtins.str] = None,
        key_tag: typing.Optional[jsii.Number] = None,
        lat_degrees: typing.Optional[jsii.Number] = None,
        lat_direction: typing.Optional[builtins.str] = None,
        lat_minutes: typing.Optional[jsii.Number] = None,
        lat_seconds: typing.Optional[jsii.Number] = None,
        long_degrees: typing.Optional[jsii.Number] = None,
        long_direction: typing.Optional[builtins.str] = None,
        long_minutes: typing.Optional[jsii.Number] = None,
        long_seconds: typing.Optional[jsii.Number] = None,
        matching_type: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        order: typing.Optional[jsii.Number] = None,
        port: typing.Optional[jsii.Number] = None,
        precision_horz: typing.Optional[jsii.Number] = None,
        precision_vert: typing.Optional[jsii.Number] = None,
        preference: typing.Optional[jsii.Number] = None,
        priority: typing.Optional[jsii.Number] = None,
        proto: typing.Optional[builtins.str] = None,
        protocol: typing.Optional[jsii.Number] = None,
        public_key: typing.Optional[builtins.str] = None,
        regex: typing.Optional[builtins.str] = None,
        replacement: typing.Optional[builtins.str] = None,
        selector: typing.Optional[jsii.Number] = None,
        service: typing.Optional[builtins.str] = None,
        size: typing.Optional[jsii.Number] = None,
        tag: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
        type: typing.Optional[jsii.Number] = None,
        usage: typing.Optional[jsii.Number] = None,
        value: typing.Optional[builtins.str] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param algorithm: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#algorithm Record#algorithm}.
        :param altitude: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#altitude Record#altitude}.
        :param certificate: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#certificate Record#certificate}.
        :param content: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#content Record#content}.
        :param digest: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#digest Record#digest}.
        :param digest_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#digest_type Record#digest_type}.
        :param fingerprint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#fingerprint Record#fingerprint}.
        :param flags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#flags Record#flags}.
        :param key_tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#key_tag Record#key_tag}.
        :param lat_degrees: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#lat_degrees Record#lat_degrees}.
        :param lat_direction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#lat_direction Record#lat_direction}.
        :param lat_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#lat_minutes Record#lat_minutes}.
        :param lat_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#lat_seconds Record#lat_seconds}.
        :param long_degrees: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#long_degrees Record#long_degrees}.
        :param long_direction: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#long_direction Record#long_direction}.
        :param long_minutes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#long_minutes Record#long_minutes}.
        :param long_seconds: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#long_seconds Record#long_seconds}.
        :param matching_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#matching_type Record#matching_type}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#name Record#name}.
        :param order: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#order Record#order}.
        :param port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#port Record#port}.
        :param precision_horz: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#precision_horz Record#precision_horz}.
        :param precision_vert: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#precision_vert Record#precision_vert}.
        :param preference: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#preference Record#preference}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#priority Record#priority}.
        :param proto: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#proto Record#proto}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#protocol Record#protocol}.
        :param public_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#public_key Record#public_key}.
        :param regex: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#regex Record#regex}.
        :param replacement: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#replacement Record#replacement}.
        :param selector: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#selector Record#selector}.
        :param service: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#service Record#service}.
        :param size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#size Record#size}.
        :param tag: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#tag Record#tag}.
        :param target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#target Record#target}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#type Record#type}.
        :param usage: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#usage Record#usage}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#value Record#value}.
        :param weight: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#weight Record#weight}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RecordData.__init__)
            check_type(argname="argument algorithm", value=algorithm, expected_type=type_hints["algorithm"])
            check_type(argname="argument altitude", value=altitude, expected_type=type_hints["altitude"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument digest", value=digest, expected_type=type_hints["digest"])
            check_type(argname="argument digest_type", value=digest_type, expected_type=type_hints["digest_type"])
            check_type(argname="argument fingerprint", value=fingerprint, expected_type=type_hints["fingerprint"])
            check_type(argname="argument flags", value=flags, expected_type=type_hints["flags"])
            check_type(argname="argument key_tag", value=key_tag, expected_type=type_hints["key_tag"])
            check_type(argname="argument lat_degrees", value=lat_degrees, expected_type=type_hints["lat_degrees"])
            check_type(argname="argument lat_direction", value=lat_direction, expected_type=type_hints["lat_direction"])
            check_type(argname="argument lat_minutes", value=lat_minutes, expected_type=type_hints["lat_minutes"])
            check_type(argname="argument lat_seconds", value=lat_seconds, expected_type=type_hints["lat_seconds"])
            check_type(argname="argument long_degrees", value=long_degrees, expected_type=type_hints["long_degrees"])
            check_type(argname="argument long_direction", value=long_direction, expected_type=type_hints["long_direction"])
            check_type(argname="argument long_minutes", value=long_minutes, expected_type=type_hints["long_minutes"])
            check_type(argname="argument long_seconds", value=long_seconds, expected_type=type_hints["long_seconds"])
            check_type(argname="argument matching_type", value=matching_type, expected_type=type_hints["matching_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument order", value=order, expected_type=type_hints["order"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument precision_horz", value=precision_horz, expected_type=type_hints["precision_horz"])
            check_type(argname="argument precision_vert", value=precision_vert, expected_type=type_hints["precision_vert"])
            check_type(argname="argument preference", value=preference, expected_type=type_hints["preference"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument proto", value=proto, expected_type=type_hints["proto"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument public_key", value=public_key, expected_type=type_hints["public_key"])
            check_type(argname="argument regex", value=regex, expected_type=type_hints["regex"])
            check_type(argname="argument replacement", value=replacement, expected_type=type_hints["replacement"])
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument usage", value=usage, expected_type=type_hints["usage"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[str, typing.Any] = {}
        if algorithm is not None:
            self._values["algorithm"] = algorithm
        if altitude is not None:
            self._values["altitude"] = altitude
        if certificate is not None:
            self._values["certificate"] = certificate
        if content is not None:
            self._values["content"] = content
        if digest is not None:
            self._values["digest"] = digest
        if digest_type is not None:
            self._values["digest_type"] = digest_type
        if fingerprint is not None:
            self._values["fingerprint"] = fingerprint
        if flags is not None:
            self._values["flags"] = flags
        if key_tag is not None:
            self._values["key_tag"] = key_tag
        if lat_degrees is not None:
            self._values["lat_degrees"] = lat_degrees
        if lat_direction is not None:
            self._values["lat_direction"] = lat_direction
        if lat_minutes is not None:
            self._values["lat_minutes"] = lat_minutes
        if lat_seconds is not None:
            self._values["lat_seconds"] = lat_seconds
        if long_degrees is not None:
            self._values["long_degrees"] = long_degrees
        if long_direction is not None:
            self._values["long_direction"] = long_direction
        if long_minutes is not None:
            self._values["long_minutes"] = long_minutes
        if long_seconds is not None:
            self._values["long_seconds"] = long_seconds
        if matching_type is not None:
            self._values["matching_type"] = matching_type
        if name is not None:
            self._values["name"] = name
        if order is not None:
            self._values["order"] = order
        if port is not None:
            self._values["port"] = port
        if precision_horz is not None:
            self._values["precision_horz"] = precision_horz
        if precision_vert is not None:
            self._values["precision_vert"] = precision_vert
        if preference is not None:
            self._values["preference"] = preference
        if priority is not None:
            self._values["priority"] = priority
        if proto is not None:
            self._values["proto"] = proto
        if protocol is not None:
            self._values["protocol"] = protocol
        if public_key is not None:
            self._values["public_key"] = public_key
        if regex is not None:
            self._values["regex"] = regex
        if replacement is not None:
            self._values["replacement"] = replacement
        if selector is not None:
            self._values["selector"] = selector
        if service is not None:
            self._values["service"] = service
        if size is not None:
            self._values["size"] = size
        if tag is not None:
            self._values["tag"] = tag
        if target is not None:
            self._values["target"] = target
        if type is not None:
            self._values["type"] = type
        if usage is not None:
            self._values["usage"] = usage
        if value is not None:
            self._values["value"] = value
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def algorithm(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#algorithm Record#algorithm}.'''
        result = self._values.get("algorithm")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def altitude(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#altitude Record#altitude}.'''
        result = self._values.get("altitude")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def certificate(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#certificate Record#certificate}.'''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#content Record#content}.'''
        result = self._values.get("content")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def digest(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#digest Record#digest}.'''
        result = self._values.get("digest")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def digest_type(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#digest_type Record#digest_type}.'''
        result = self._values.get("digest_type")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def fingerprint(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#fingerprint Record#fingerprint}.'''
        result = self._values.get("fingerprint")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def flags(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#flags Record#flags}.'''
        result = self._values.get("flags")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_tag(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#key_tag Record#key_tag}.'''
        result = self._values.get("key_tag")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def lat_degrees(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#lat_degrees Record#lat_degrees}.'''
        result = self._values.get("lat_degrees")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def lat_direction(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#lat_direction Record#lat_direction}.'''
        result = self._values.get("lat_direction")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lat_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#lat_minutes Record#lat_minutes}.'''
        result = self._values.get("lat_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def lat_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#lat_seconds Record#lat_seconds}.'''
        result = self._values.get("lat_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def long_degrees(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#long_degrees Record#long_degrees}.'''
        result = self._values.get("long_degrees")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def long_direction(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#long_direction Record#long_direction}.'''
        result = self._values.get("long_direction")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def long_minutes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#long_minutes Record#long_minutes}.'''
        result = self._values.get("long_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def long_seconds(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#long_seconds Record#long_seconds}.'''
        result = self._values.get("long_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def matching_type(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#matching_type Record#matching_type}.'''
        result = self._values.get("matching_type")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#name Record#name}.'''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def order(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#order Record#order}.'''
        result = self._values.get("order")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#port Record#port}.'''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def precision_horz(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#precision_horz Record#precision_horz}.'''
        result = self._values.get("precision_horz")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def precision_vert(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#precision_vert Record#precision_vert}.'''
        result = self._values.get("precision_vert")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def preference(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#preference Record#preference}.'''
        result = self._values.get("preference")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#priority Record#priority}.'''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def proto(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#proto Record#proto}.'''
        result = self._values.get("proto")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocol(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#protocol Record#protocol}.'''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def public_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#public_key Record#public_key}.'''
        result = self._values.get("public_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def regex(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#regex Record#regex}.'''
        result = self._values.get("regex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replacement(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#replacement Record#replacement}.'''
        result = self._values.get("replacement")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def selector(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#selector Record#selector}.'''
        result = self._values.get("selector")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def service(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#service Record#service}.'''
        result = self._values.get("service")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def size(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#size Record#size}.'''
        result = self._values.get("size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tag(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#tag Record#tag}.'''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#target Record#target}.'''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#type Record#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def usage(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#usage Record#usage}.'''
        result = self._values.get("usage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#value Record#value}.'''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#weight Record#weight}.'''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RecordData(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RecordDataOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.record.RecordDataOutputReference",
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
            type_hints = typing.get_type_hints(RecordDataOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAlgorithm")
    def reset_algorithm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlgorithm", []))

    @jsii.member(jsii_name="resetAltitude")
    def reset_altitude(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAltitude", []))

    @jsii.member(jsii_name="resetCertificate")
    def reset_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificate", []))

    @jsii.member(jsii_name="resetContent")
    def reset_content(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContent", []))

    @jsii.member(jsii_name="resetDigest")
    def reset_digest(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDigest", []))

    @jsii.member(jsii_name="resetDigestType")
    def reset_digest_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDigestType", []))

    @jsii.member(jsii_name="resetFingerprint")
    def reset_fingerprint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFingerprint", []))

    @jsii.member(jsii_name="resetFlags")
    def reset_flags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFlags", []))

    @jsii.member(jsii_name="resetKeyTag")
    def reset_key_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyTag", []))

    @jsii.member(jsii_name="resetLatDegrees")
    def reset_lat_degrees(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLatDegrees", []))

    @jsii.member(jsii_name="resetLatDirection")
    def reset_lat_direction(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLatDirection", []))

    @jsii.member(jsii_name="resetLatMinutes")
    def reset_lat_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLatMinutes", []))

    @jsii.member(jsii_name="resetLatSeconds")
    def reset_lat_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLatSeconds", []))

    @jsii.member(jsii_name="resetLongDegrees")
    def reset_long_degrees(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLongDegrees", []))

    @jsii.member(jsii_name="resetLongDirection")
    def reset_long_direction(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLongDirection", []))

    @jsii.member(jsii_name="resetLongMinutes")
    def reset_long_minutes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLongMinutes", []))

    @jsii.member(jsii_name="resetLongSeconds")
    def reset_long_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLongSeconds", []))

    @jsii.member(jsii_name="resetMatchingType")
    def reset_matching_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchingType", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetOrder")
    def reset_order(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrder", []))

    @jsii.member(jsii_name="resetPort")
    def reset_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPort", []))

    @jsii.member(jsii_name="resetPrecisionHorz")
    def reset_precision_horz(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrecisionHorz", []))

    @jsii.member(jsii_name="resetPrecisionVert")
    def reset_precision_vert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrecisionVert", []))

    @jsii.member(jsii_name="resetPreference")
    def reset_preference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreference", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetProto")
    def reset_proto(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProto", []))

    @jsii.member(jsii_name="resetProtocol")
    def reset_protocol(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtocol", []))

    @jsii.member(jsii_name="resetPublicKey")
    def reset_public_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicKey", []))

    @jsii.member(jsii_name="resetRegex")
    def reset_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegex", []))

    @jsii.member(jsii_name="resetReplacement")
    def reset_replacement(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReplacement", []))

    @jsii.member(jsii_name="resetSelector")
    def reset_selector(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSelector", []))

    @jsii.member(jsii_name="resetService")
    def reset_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetService", []))

    @jsii.member(jsii_name="resetSize")
    def reset_size(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSize", []))

    @jsii.member(jsii_name="resetTag")
    def reset_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTag", []))

    @jsii.member(jsii_name="resetTarget")
    def reset_target(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTarget", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetUsage")
    def reset_usage(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsage", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @jsii.member(jsii_name="resetWeight")
    def reset_weight(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWeight", []))

    @builtins.property
    @jsii.member(jsii_name="algorithmInput")
    def algorithm_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "algorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="altitudeInput")
    def altitude_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "altitudeInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="digestInput")
    def digest_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "digestInput"))

    @builtins.property
    @jsii.member(jsii_name="digestTypeInput")
    def digest_type_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "digestTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="fingerprintInput")
    def fingerprint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fingerprintInput"))

    @builtins.property
    @jsii.member(jsii_name="flagsInput")
    def flags_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "flagsInput"))

    @builtins.property
    @jsii.member(jsii_name="keyTagInput")
    def key_tag_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "keyTagInput"))

    @builtins.property
    @jsii.member(jsii_name="latDegreesInput")
    def lat_degrees_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "latDegreesInput"))

    @builtins.property
    @jsii.member(jsii_name="latDirectionInput")
    def lat_direction_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "latDirectionInput"))

    @builtins.property
    @jsii.member(jsii_name="latMinutesInput")
    def lat_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "latMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="latSecondsInput")
    def lat_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "latSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="longDegreesInput")
    def long_degrees_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "longDegreesInput"))

    @builtins.property
    @jsii.member(jsii_name="longDirectionInput")
    def long_direction_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "longDirectionInput"))

    @builtins.property
    @jsii.member(jsii_name="longMinutesInput")
    def long_minutes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "longMinutesInput"))

    @builtins.property
    @jsii.member(jsii_name="longSecondsInput")
    def long_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "longSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="matchingTypeInput")
    def matching_type_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "matchingTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="orderInput")
    def order_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "orderInput"))

    @builtins.property
    @jsii.member(jsii_name="portInput")
    def port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "portInput"))

    @builtins.property
    @jsii.member(jsii_name="precisionHorzInput")
    def precision_horz_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "precisionHorzInput"))

    @builtins.property
    @jsii.member(jsii_name="precisionVertInput")
    def precision_vert_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "precisionVertInput"))

    @builtins.property
    @jsii.member(jsii_name="preferenceInput")
    def preference_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "preferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="protoInput")
    def proto_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protoInput"))

    @builtins.property
    @jsii.member(jsii_name="publicKeyInput")
    def public_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="regexInput")
    def regex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regexInput"))

    @builtins.property
    @jsii.member(jsii_name="replacementInput")
    def replacement_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replacementInput"))

    @builtins.property
    @jsii.member(jsii_name="selectorInput")
    def selector_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "selectorInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="sizeInput")
    def size_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sizeInput"))

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="targetInput")
    def target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="usageInput")
    def usage_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "usageInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="weightInput")
    def weight_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weightInput"))

    @builtins.property
    @jsii.member(jsii_name="algorithm")
    def algorithm(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "algorithm"))

    @algorithm.setter
    def algorithm(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "algorithm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "algorithm", value)

    @builtins.property
    @jsii.member(jsii_name="altitude")
    def altitude(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "altitude"))

    @altitude.setter
    def altitude(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "altitude").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "altitude", value)

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "certificate").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificate", value)

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="digest")
    def digest(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "digest"))

    @digest.setter
    def digest(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "digest").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "digest", value)

    @builtins.property
    @jsii.member(jsii_name="digestType")
    def digest_type(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "digestType"))

    @digest_type.setter
    def digest_type(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "digest_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "digestType", value)

    @builtins.property
    @jsii.member(jsii_name="fingerprint")
    def fingerprint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fingerprint"))

    @fingerprint.setter
    def fingerprint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "fingerprint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fingerprint", value)

    @builtins.property
    @jsii.member(jsii_name="flags")
    def flags(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "flags"))

    @flags.setter
    def flags(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "flags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flags", value)

    @builtins.property
    @jsii.member(jsii_name="keyTag")
    def key_tag(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "keyTag"))

    @key_tag.setter
    def key_tag(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "key_tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyTag", value)

    @builtins.property
    @jsii.member(jsii_name="latDegrees")
    def lat_degrees(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "latDegrees"))

    @lat_degrees.setter
    def lat_degrees(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "lat_degrees").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "latDegrees", value)

    @builtins.property
    @jsii.member(jsii_name="latDirection")
    def lat_direction(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "latDirection"))

    @lat_direction.setter
    def lat_direction(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "lat_direction").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "latDirection", value)

    @builtins.property
    @jsii.member(jsii_name="latMinutes")
    def lat_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "latMinutes"))

    @lat_minutes.setter
    def lat_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "lat_minutes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "latMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="latSeconds")
    def lat_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "latSeconds"))

    @lat_seconds.setter
    def lat_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "lat_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "latSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="longDegrees")
    def long_degrees(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "longDegrees"))

    @long_degrees.setter
    def long_degrees(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "long_degrees").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "longDegrees", value)

    @builtins.property
    @jsii.member(jsii_name="longDirection")
    def long_direction(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "longDirection"))

    @long_direction.setter
    def long_direction(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "long_direction").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "longDirection", value)

    @builtins.property
    @jsii.member(jsii_name="longMinutes")
    def long_minutes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "longMinutes"))

    @long_minutes.setter
    def long_minutes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "long_minutes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "longMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="longSeconds")
    def long_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "longSeconds"))

    @long_seconds.setter
    def long_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "long_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "longSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="matchingType")
    def matching_type(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "matchingType"))

    @matching_type.setter
    def matching_type(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "matching_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchingType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="order")
    def order(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "order"))

    @order.setter
    def order(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "order").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "order", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "port"))

    @port.setter
    def port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="precisionHorz")
    def precision_horz(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "precisionHorz"))

    @precision_horz.setter
    def precision_horz(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "precision_horz").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "precisionHorz", value)

    @builtins.property
    @jsii.member(jsii_name="precisionVert")
    def precision_vert(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "precisionVert"))

    @precision_vert.setter
    def precision_vert(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "precision_vert").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "precisionVert", value)

    @builtins.property
    @jsii.member(jsii_name="preference")
    def preference(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "preference"))

    @preference.setter
    def preference(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "preference").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preference", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="proto")
    def proto(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "proto"))

    @proto.setter
    def proto(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "proto").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "proto", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="publicKey")
    def public_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicKey"))

    @public_key.setter
    def public_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "public_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicKey", value)

    @builtins.property
    @jsii.member(jsii_name="regex")
    def regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regex"))

    @regex.setter
    def regex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "regex").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regex", value)

    @builtins.property
    @jsii.member(jsii_name="replacement")
    def replacement(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "replacement"))

    @replacement.setter
    def replacement(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "replacement").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replacement", value)

    @builtins.property
    @jsii.member(jsii_name="selector")
    def selector(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "selector"))

    @selector.setter
    def selector(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "selector").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "selector", value)

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "service"))

    @service.setter
    def service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)

    @builtins.property
    @jsii.member(jsii_name="size")
    def size(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "size"))

    @size.setter
    def size(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "size", value)

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tag"))

    @tag.setter
    def tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tag", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "target"))

    @target.setter
    def target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "type"))

    @type.setter
    def type(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="usage")
    def usage(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "usage"))

    @usage.setter
    def usage(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "usage").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usage", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "weight").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weight", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[RecordData]:
        return typing.cast(typing.Optional[RecordData], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[RecordData]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordDataOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.record.RecordTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "update": "update"},
)
class RecordTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#create Record#create}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#update Record#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(RecordTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#create Record#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/record#update Record#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RecordTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RecordTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.record.RecordTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(RecordTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

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
            type_hints = typing.get_type_hints(getattr(RecordTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[RecordTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[RecordTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[RecordTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(RecordTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "Record",
    "RecordConfig",
    "RecordData",
    "RecordDataOutputReference",
    "RecordTimeouts",
    "RecordTimeoutsOutputReference",
]

publication.publish()
