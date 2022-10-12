'''
# `data_ionoscloud_application_loadbalancer`

Refer to the Terraform Registory for docs: [`data_ionoscloud_application_loadbalancer`](https://www.terraform.io/docs/providers/ionoscloud/d/application_loadbalancer).
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


class DataIonoscloudApplicationLoadbalancer(
    cdktf.TerraformDataSource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.dataIonoscloudApplicationLoadbalancer.DataIonoscloudApplicationLoadbalancer",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/ionoscloud/d/application_loadbalancer ionoscloud_application_loadbalancer}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        datacenter_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        partial_match: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["DataIonoscloudApplicationLoadbalancerTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/ionoscloud/d/application_loadbalancer ionoscloud_application_loadbalancer} Data Source.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param datacenter_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/d/application_loadbalancer#datacenter_id DataIonoscloudApplicationLoadbalancer#datacenter_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/d/application_loadbalancer#id DataIonoscloudApplicationLoadbalancer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: The name of the Application Load Balancer. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/d/application_loadbalancer#name DataIonoscloudApplicationLoadbalancer#name}
        :param partial_match: Whether partial matching is allowed or not when using name argument. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/d/application_loadbalancer#partial_match DataIonoscloudApplicationLoadbalancer#partial_match}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/d/application_loadbalancer#timeouts DataIonoscloudApplicationLoadbalancer#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataIonoscloudApplicationLoadbalancer.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataIonoscloudApplicationLoadbalancerConfig(
            datacenter_id=datacenter_id,
            id=id,
            name=name,
            partial_match=partial_match,
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

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        default: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/d/application_loadbalancer#create DataIonoscloudApplicationLoadbalancer#create}.
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/d/application_loadbalancer#default DataIonoscloudApplicationLoadbalancer#default}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/d/application_loadbalancer#delete DataIonoscloudApplicationLoadbalancer#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/d/application_loadbalancer#update DataIonoscloudApplicationLoadbalancer#update}.
        '''
        value = DataIonoscloudApplicationLoadbalancerTimeouts(
            create=create, default=default, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetPartialMatch")
    def reset_partial_match(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPartialMatch", []))

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
    @jsii.member(jsii_name="ips")
    def ips(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ips"))

    @builtins.property
    @jsii.member(jsii_name="lbPrivateIps")
    def lb_private_ips(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "lbPrivateIps"))

    @builtins.property
    @jsii.member(jsii_name="listenerLan")
    def listener_lan(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "listenerLan"))

    @builtins.property
    @jsii.member(jsii_name="targetLan")
    def target_lan(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetLan"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(
        self,
    ) -> "DataIonoscloudApplicationLoadbalancerTimeoutsOutputReference":
        return typing.cast("DataIonoscloudApplicationLoadbalancerTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="datacenterIdInput")
    def datacenter_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datacenterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="partialMatchInput")
    def partial_match_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "partialMatchInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DataIonoscloudApplicationLoadbalancerTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DataIonoscloudApplicationLoadbalancerTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="datacenterId")
    def datacenter_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datacenterId"))

    @datacenter_id.setter
    def datacenter_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataIonoscloudApplicationLoadbalancer, "datacenter_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datacenterId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataIonoscloudApplicationLoadbalancer, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataIonoscloudApplicationLoadbalancer, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="partialMatch")
    def partial_match(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "partialMatch"))

    @partial_match.setter
    def partial_match(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataIonoscloudApplicationLoadbalancer, "partial_match").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partialMatch", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-ionoscloud.dataIonoscloudApplicationLoadbalancer.DataIonoscloudApplicationLoadbalancerConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "datacenter_id": "datacenterId",
        "id": "id",
        "name": "name",
        "partial_match": "partialMatch",
        "timeouts": "timeouts",
    },
)
class DataIonoscloudApplicationLoadbalancerConfig(cdktf.TerraformMetaArguments):
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
        datacenter_id: builtins.str,
        id: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        partial_match: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        timeouts: typing.Optional[typing.Union["DataIonoscloudApplicationLoadbalancerTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param datacenter_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/d/application_loadbalancer#datacenter_id DataIonoscloudApplicationLoadbalancer#datacenter_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/d/application_loadbalancer#id DataIonoscloudApplicationLoadbalancer#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param name: The name of the Application Load Balancer. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/d/application_loadbalancer#name DataIonoscloudApplicationLoadbalancer#name}
        :param partial_match: Whether partial matching is allowed or not when using name argument. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/d/application_loadbalancer#partial_match DataIonoscloudApplicationLoadbalancer#partial_match}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/d/application_loadbalancer#timeouts DataIonoscloudApplicationLoadbalancer#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = DataIonoscloudApplicationLoadbalancerTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(DataIonoscloudApplicationLoadbalancerConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument datacenter_id", value=datacenter_id, expected_type=type_hints["datacenter_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument partial_match", value=partial_match, expected_type=type_hints["partial_match"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "datacenter_id": datacenter_id,
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
        if name is not None:
            self._values["name"] = name
        if partial_match is not None:
            self._values["partial_match"] = partial_match
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
    def datacenter_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/d/application_loadbalancer#datacenter_id DataIonoscloudApplicationLoadbalancer#datacenter_id}.'''
        result = self._values.get("datacenter_id")
        assert result is not None, "Required property 'datacenter_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/d/application_loadbalancer#id DataIonoscloudApplicationLoadbalancer#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the Application Load Balancer.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/d/application_loadbalancer#name DataIonoscloudApplicationLoadbalancer#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def partial_match(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether partial matching is allowed or not when using name argument.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/d/application_loadbalancer#partial_match DataIonoscloudApplicationLoadbalancer#partial_match}
        '''
        result = self._values.get("partial_match")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def timeouts(
        self,
    ) -> typing.Optional["DataIonoscloudApplicationLoadbalancerTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/d/application_loadbalancer#timeouts DataIonoscloudApplicationLoadbalancer#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DataIonoscloudApplicationLoadbalancerTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataIonoscloudApplicationLoadbalancerConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-ionoscloud.dataIonoscloudApplicationLoadbalancer.DataIonoscloudApplicationLoadbalancerTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "default": "default",
        "delete": "delete",
        "update": "update",
    },
)
class DataIonoscloudApplicationLoadbalancerTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        default: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/d/application_loadbalancer#create DataIonoscloudApplicationLoadbalancer#create}.
        :param default: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/d/application_loadbalancer#default DataIonoscloudApplicationLoadbalancer#default}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/d/application_loadbalancer#delete DataIonoscloudApplicationLoadbalancer#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/d/application_loadbalancer#update DataIonoscloudApplicationLoadbalancer#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataIonoscloudApplicationLoadbalancerTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument default", value=default, expected_type=type_hints["default"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if default is not None:
            self._values["default"] = default
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/d/application_loadbalancer#create DataIonoscloudApplicationLoadbalancer#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/d/application_loadbalancer#default DataIonoscloudApplicationLoadbalancer#default}.'''
        result = self._values.get("default")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/d/application_loadbalancer#delete DataIonoscloudApplicationLoadbalancer#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/ionoscloud/d/application_loadbalancer#update DataIonoscloudApplicationLoadbalancer#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataIonoscloudApplicationLoadbalancerTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataIonoscloudApplicationLoadbalancerTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-ionoscloud.dataIonoscloudApplicationLoadbalancer.DataIonoscloudApplicationLoadbalancerTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(DataIonoscloudApplicationLoadbalancerTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDefault")
    def reset_default(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefault", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultInput")
    def default_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

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
            type_hints = typing.get_type_hints(getattr(DataIonoscloudApplicationLoadbalancerTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="default")
    def default(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "default"))

    @default.setter
    def default(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataIonoscloudApplicationLoadbalancerTimeoutsOutputReference, "default").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "default", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataIonoscloudApplicationLoadbalancerTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataIonoscloudApplicationLoadbalancerTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataIonoscloudApplicationLoadbalancerTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataIonoscloudApplicationLoadbalancerTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataIonoscloudApplicationLoadbalancerTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataIonoscloudApplicationLoadbalancerTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataIonoscloudApplicationLoadbalancer",
    "DataIonoscloudApplicationLoadbalancerConfig",
    "DataIonoscloudApplicationLoadbalancerTimeouts",
    "DataIonoscloudApplicationLoadbalancerTimeoutsOutputReference",
]

publication.publish()
