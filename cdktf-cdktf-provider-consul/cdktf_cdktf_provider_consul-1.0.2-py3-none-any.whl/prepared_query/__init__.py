'''
# `consul_prepared_query`

Refer to the Terraform Registory for docs: [`consul_prepared_query`](https://www.terraform.io/docs/providers/consul/r/prepared_query).
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


class PreparedQuery(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-consul.preparedQuery.PreparedQuery",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/consul/r/prepared_query consul_prepared_query}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        service: builtins.str,
        connect: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        datacenter: typing.Optional[builtins.str] = None,
        dns: typing.Optional[typing.Union["PreparedQueryDns", typing.Dict[str, typing.Any]]] = None,
        failover: typing.Optional[typing.Union["PreparedQueryFailover", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        ignore_check_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        near: typing.Optional[builtins.str] = None,
        node_meta: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        only_passing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        service_meta: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        session: typing.Optional[builtins.str] = None,
        stored_token: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        template: typing.Optional[typing.Union["PreparedQueryTemplate", typing.Dict[str, typing.Any]]] = None,
        token: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/consul/r/prepared_query consul_prepared_query} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#name PreparedQuery#name}.
        :param service: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#service PreparedQuery#service}.
        :param connect: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#connect PreparedQuery#connect}.
        :param datacenter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#datacenter PreparedQuery#datacenter}.
        :param dns: dns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#dns PreparedQuery#dns}
        :param failover: failover block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#failover PreparedQuery#failover}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#id PreparedQuery#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ignore_check_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#ignore_check_ids PreparedQuery#ignore_check_ids}.
        :param near: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#near PreparedQuery#near}.
        :param node_meta: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#node_meta PreparedQuery#node_meta}.
        :param only_passing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#only_passing PreparedQuery#only_passing}.
        :param service_meta: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#service_meta PreparedQuery#service_meta}.
        :param session: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#session PreparedQuery#session}.
        :param stored_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#stored_token PreparedQuery#stored_token}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#tags PreparedQuery#tags}.
        :param template: template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#template PreparedQuery#template}
        :param token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#token PreparedQuery#token}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PreparedQuery.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = PreparedQueryConfig(
            name=name,
            service=service,
            connect=connect,
            datacenter=datacenter,
            dns=dns,
            failover=failover,
            id=id,
            ignore_check_ids=ignore_check_ids,
            near=near,
            node_meta=node_meta,
            only_passing=only_passing,
            service_meta=service_meta,
            session=session,
            stored_token=stored_token,
            tags=tags,
            template=template,
            token=token,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putDns")
    def put_dns(self, *, ttl: typing.Optional[builtins.str] = None) -> None:
        '''
        :param ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#ttl PreparedQuery#ttl}.
        '''
        value = PreparedQueryDns(ttl=ttl)

        return typing.cast(None, jsii.invoke(self, "putDns", [value]))

    @jsii.member(jsii_name="putFailover")
    def put_failover(
        self,
        *,
        datacenters: typing.Optional[typing.Sequence[builtins.str]] = None,
        nearest_n: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param datacenters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#datacenters PreparedQuery#datacenters}.
        :param nearest_n: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#nearest_n PreparedQuery#nearest_n}.
        '''
        value = PreparedQueryFailover(datacenters=datacenters, nearest_n=nearest_n)

        return typing.cast(None, jsii.invoke(self, "putFailover", [value]))

    @jsii.member(jsii_name="putTemplate")
    def put_template(self, *, regexp: builtins.str, type: builtins.str) -> None:
        '''
        :param regexp: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#regexp PreparedQuery#regexp}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#type PreparedQuery#type}.
        '''
        value = PreparedQueryTemplate(regexp=regexp, type=type)

        return typing.cast(None, jsii.invoke(self, "putTemplate", [value]))

    @jsii.member(jsii_name="resetConnect")
    def reset_connect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnect", []))

    @jsii.member(jsii_name="resetDatacenter")
    def reset_datacenter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatacenter", []))

    @jsii.member(jsii_name="resetDns")
    def reset_dns(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDns", []))

    @jsii.member(jsii_name="resetFailover")
    def reset_failover(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailover", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIgnoreCheckIds")
    def reset_ignore_check_ids(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreCheckIds", []))

    @jsii.member(jsii_name="resetNear")
    def reset_near(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNear", []))

    @jsii.member(jsii_name="resetNodeMeta")
    def reset_node_meta(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeMeta", []))

    @jsii.member(jsii_name="resetOnlyPassing")
    def reset_only_passing(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnlyPassing", []))

    @jsii.member(jsii_name="resetServiceMeta")
    def reset_service_meta(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceMeta", []))

    @jsii.member(jsii_name="resetSession")
    def reset_session(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSession", []))

    @jsii.member(jsii_name="resetStoredToken")
    def reset_stored_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStoredToken", []))

    @jsii.member(jsii_name="resetTags")
    def reset_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTags", []))

    @jsii.member(jsii_name="resetTemplate")
    def reset_template(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTemplate", []))

    @jsii.member(jsii_name="resetToken")
    def reset_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetToken", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="dns")
    def dns(self) -> "PreparedQueryDnsOutputReference":
        return typing.cast("PreparedQueryDnsOutputReference", jsii.get(self, "dns"))

    @builtins.property
    @jsii.member(jsii_name="failover")
    def failover(self) -> "PreparedQueryFailoverOutputReference":
        return typing.cast("PreparedQueryFailoverOutputReference", jsii.get(self, "failover"))

    @builtins.property
    @jsii.member(jsii_name="template")
    def template(self) -> "PreparedQueryTemplateOutputReference":
        return typing.cast("PreparedQueryTemplateOutputReference", jsii.get(self, "template"))

    @builtins.property
    @jsii.member(jsii_name="connectInput")
    def connect_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "connectInput"))

    @builtins.property
    @jsii.member(jsii_name="datacenterInput")
    def datacenter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datacenterInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsInput")
    def dns_input(self) -> typing.Optional["PreparedQueryDns"]:
        return typing.cast(typing.Optional["PreparedQueryDns"], jsii.get(self, "dnsInput"))

    @builtins.property
    @jsii.member(jsii_name="failoverInput")
    def failover_input(self) -> typing.Optional["PreparedQueryFailover"]:
        return typing.cast(typing.Optional["PreparedQueryFailover"], jsii.get(self, "failoverInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreCheckIdsInput")
    def ignore_check_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "ignoreCheckIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="nearInput")
    def near_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nearInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeMetaInput")
    def node_meta_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "nodeMetaInput"))

    @builtins.property
    @jsii.member(jsii_name="onlyPassingInput")
    def only_passing_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "onlyPassingInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceMetaInput")
    def service_meta_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "serviceMetaInput"))

    @builtins.property
    @jsii.member(jsii_name="sessionInput")
    def session_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sessionInput"))

    @builtins.property
    @jsii.member(jsii_name="storedTokenInput")
    def stored_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storedTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="tagsInput")
    def tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "tagsInput"))

    @builtins.property
    @jsii.member(jsii_name="templateInput")
    def template_input(self) -> typing.Optional["PreparedQueryTemplate"]:
        return typing.cast(typing.Optional["PreparedQueryTemplate"], jsii.get(self, "templateInput"))

    @builtins.property
    @jsii.member(jsii_name="tokenInput")
    def token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenInput"))

    @builtins.property
    @jsii.member(jsii_name="connect")
    def connect(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "connect"))

    @connect.setter
    def connect(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PreparedQuery, "connect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connect", value)

    @builtins.property
    @jsii.member(jsii_name="datacenter")
    def datacenter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datacenter"))

    @datacenter.setter
    def datacenter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PreparedQuery, "datacenter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datacenter", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PreparedQuery, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreCheckIds")
    def ignore_check_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ignoreCheckIds"))

    @ignore_check_ids.setter
    def ignore_check_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PreparedQuery, "ignore_check_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreCheckIds", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PreparedQuery, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="near")
    def near(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "near"))

    @near.setter
    def near(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PreparedQuery, "near").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "near", value)

    @builtins.property
    @jsii.member(jsii_name="nodeMeta")
    def node_meta(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "nodeMeta"))

    @node_meta.setter
    def node_meta(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PreparedQuery, "node_meta").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeMeta", value)

    @builtins.property
    @jsii.member(jsii_name="onlyPassing")
    def only_passing(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "onlyPassing"))

    @only_passing.setter
    def only_passing(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PreparedQuery, "only_passing").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onlyPassing", value)

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "service"))

    @service.setter
    def service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PreparedQuery, "service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)

    @builtins.property
    @jsii.member(jsii_name="serviceMeta")
    def service_meta(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "serviceMeta"))

    @service_meta.setter
    def service_meta(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PreparedQuery, "service_meta").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceMeta", value)

    @builtins.property
    @jsii.member(jsii_name="session")
    def session(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "session"))

    @session.setter
    def session(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PreparedQuery, "session").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "session", value)

    @builtins.property
    @jsii.member(jsii_name="storedToken")
    def stored_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storedToken"))

    @stored_token.setter
    def stored_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PreparedQuery, "stored_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storedToken", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PreparedQuery, "tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "token"))

    @token.setter
    def token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PreparedQuery, "token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "token", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-consul.preparedQuery.PreparedQueryConfig",
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
        "service": "service",
        "connect": "connect",
        "datacenter": "datacenter",
        "dns": "dns",
        "failover": "failover",
        "id": "id",
        "ignore_check_ids": "ignoreCheckIds",
        "near": "near",
        "node_meta": "nodeMeta",
        "only_passing": "onlyPassing",
        "service_meta": "serviceMeta",
        "session": "session",
        "stored_token": "storedToken",
        "tags": "tags",
        "template": "template",
        "token": "token",
    },
)
class PreparedQueryConfig(cdktf.TerraformMetaArguments):
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
        service: builtins.str,
        connect: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        datacenter: typing.Optional[builtins.str] = None,
        dns: typing.Optional[typing.Union["PreparedQueryDns", typing.Dict[str, typing.Any]]] = None,
        failover: typing.Optional[typing.Union["PreparedQueryFailover", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        ignore_check_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        near: typing.Optional[builtins.str] = None,
        node_meta: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        only_passing: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        service_meta: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        session: typing.Optional[builtins.str] = None,
        stored_token: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        template: typing.Optional[typing.Union["PreparedQueryTemplate", typing.Dict[str, typing.Any]]] = None,
        token: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#name PreparedQuery#name}.
        :param service: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#service PreparedQuery#service}.
        :param connect: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#connect PreparedQuery#connect}.
        :param datacenter: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#datacenter PreparedQuery#datacenter}.
        :param dns: dns block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#dns PreparedQuery#dns}
        :param failover: failover block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#failover PreparedQuery#failover}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#id PreparedQuery#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param ignore_check_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#ignore_check_ids PreparedQuery#ignore_check_ids}.
        :param near: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#near PreparedQuery#near}.
        :param node_meta: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#node_meta PreparedQuery#node_meta}.
        :param only_passing: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#only_passing PreparedQuery#only_passing}.
        :param service_meta: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#service_meta PreparedQuery#service_meta}.
        :param session: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#session PreparedQuery#session}.
        :param stored_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#stored_token PreparedQuery#stored_token}.
        :param tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#tags PreparedQuery#tags}.
        :param template: template block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#template PreparedQuery#template}
        :param token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#token PreparedQuery#token}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(dns, dict):
            dns = PreparedQueryDns(**dns)
        if isinstance(failover, dict):
            failover = PreparedQueryFailover(**failover)
        if isinstance(template, dict):
            template = PreparedQueryTemplate(**template)
        if __debug__:
            type_hints = typing.get_type_hints(PreparedQueryConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument connect", value=connect, expected_type=type_hints["connect"])
            check_type(argname="argument datacenter", value=datacenter, expected_type=type_hints["datacenter"])
            check_type(argname="argument dns", value=dns, expected_type=type_hints["dns"])
            check_type(argname="argument failover", value=failover, expected_type=type_hints["failover"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ignore_check_ids", value=ignore_check_ids, expected_type=type_hints["ignore_check_ids"])
            check_type(argname="argument near", value=near, expected_type=type_hints["near"])
            check_type(argname="argument node_meta", value=node_meta, expected_type=type_hints["node_meta"])
            check_type(argname="argument only_passing", value=only_passing, expected_type=type_hints["only_passing"])
            check_type(argname="argument service_meta", value=service_meta, expected_type=type_hints["service_meta"])
            check_type(argname="argument session", value=session, expected_type=type_hints["session"])
            check_type(argname="argument stored_token", value=stored_token, expected_type=type_hints["stored_token"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument template", value=template, expected_type=type_hints["template"])
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "service": service,
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
        if connect is not None:
            self._values["connect"] = connect
        if datacenter is not None:
            self._values["datacenter"] = datacenter
        if dns is not None:
            self._values["dns"] = dns
        if failover is not None:
            self._values["failover"] = failover
        if id is not None:
            self._values["id"] = id
        if ignore_check_ids is not None:
            self._values["ignore_check_ids"] = ignore_check_ids
        if near is not None:
            self._values["near"] = near
        if node_meta is not None:
            self._values["node_meta"] = node_meta
        if only_passing is not None:
            self._values["only_passing"] = only_passing
        if service_meta is not None:
            self._values["service_meta"] = service_meta
        if session is not None:
            self._values["session"] = session
        if stored_token is not None:
            self._values["stored_token"] = stored_token
        if tags is not None:
            self._values["tags"] = tags
        if template is not None:
            self._values["template"] = template
        if token is not None:
            self._values["token"] = token

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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#name PreparedQuery#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#service PreparedQuery#service}.'''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connect(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#connect PreparedQuery#connect}.'''
        result = self._values.get("connect")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def datacenter(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#datacenter PreparedQuery#datacenter}.'''
        result = self._values.get("datacenter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dns(self) -> typing.Optional["PreparedQueryDns"]:
        '''dns block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#dns PreparedQuery#dns}
        '''
        result = self._values.get("dns")
        return typing.cast(typing.Optional["PreparedQueryDns"], result)

    @builtins.property
    def failover(self) -> typing.Optional["PreparedQueryFailover"]:
        '''failover block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#failover PreparedQuery#failover}
        '''
        result = self._values.get("failover")
        return typing.cast(typing.Optional["PreparedQueryFailover"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#id PreparedQuery#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ignore_check_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#ignore_check_ids PreparedQuery#ignore_check_ids}.'''
        result = self._values.get("ignore_check_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def near(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#near PreparedQuery#near}.'''
        result = self._values.get("near")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def node_meta(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#node_meta PreparedQuery#node_meta}.'''
        result = self._values.get("node_meta")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def only_passing(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#only_passing PreparedQuery#only_passing}.'''
        result = self._values.get("only_passing")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def service_meta(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#service_meta PreparedQuery#service_meta}.'''
        result = self._values.get("service_meta")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def session(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#session PreparedQuery#session}.'''
        result = self._values.get("session")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stored_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#stored_token PreparedQuery#stored_token}.'''
        result = self._values.get("stored_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#tags PreparedQuery#tags}.'''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def template(self) -> typing.Optional["PreparedQueryTemplate"]:
        '''template block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#template PreparedQuery#template}
        '''
        result = self._values.get("template")
        return typing.cast(typing.Optional["PreparedQueryTemplate"], result)

    @builtins.property
    def token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#token PreparedQuery#token}.'''
        result = self._values.get("token")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PreparedQueryConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-consul.preparedQuery.PreparedQueryDns",
    jsii_struct_bases=[],
    name_mapping={"ttl": "ttl"},
)
class PreparedQueryDns:
    def __init__(self, *, ttl: typing.Optional[builtins.str] = None) -> None:
        '''
        :param ttl: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#ttl PreparedQuery#ttl}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PreparedQueryDns.__init__)
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
        self._values: typing.Dict[str, typing.Any] = {}
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def ttl(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#ttl PreparedQuery#ttl}.'''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PreparedQueryDns(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PreparedQueryDnsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-consul.preparedQuery.PreparedQueryDnsOutputReference",
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
            type_hints = typing.get_type_hints(PreparedQueryDnsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetTtl")
    def reset_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTtl", []))

    @builtins.property
    @jsii.member(jsii_name="ttlInput")
    def ttl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ttlInput"))

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ttl"))

    @ttl.setter
    def ttl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PreparedQueryDnsOutputReference, "ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ttl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PreparedQueryDns]:
        return typing.cast(typing.Optional[PreparedQueryDns], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[PreparedQueryDns]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PreparedQueryDnsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-consul.preparedQuery.PreparedQueryFailover",
    jsii_struct_bases=[],
    name_mapping={"datacenters": "datacenters", "nearest_n": "nearestN"},
)
class PreparedQueryFailover:
    def __init__(
        self,
        *,
        datacenters: typing.Optional[typing.Sequence[builtins.str]] = None,
        nearest_n: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param datacenters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#datacenters PreparedQuery#datacenters}.
        :param nearest_n: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#nearest_n PreparedQuery#nearest_n}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PreparedQueryFailover.__init__)
            check_type(argname="argument datacenters", value=datacenters, expected_type=type_hints["datacenters"])
            check_type(argname="argument nearest_n", value=nearest_n, expected_type=type_hints["nearest_n"])
        self._values: typing.Dict[str, typing.Any] = {}
        if datacenters is not None:
            self._values["datacenters"] = datacenters
        if nearest_n is not None:
            self._values["nearest_n"] = nearest_n

    @builtins.property
    def datacenters(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#datacenters PreparedQuery#datacenters}.'''
        result = self._values.get("datacenters")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def nearest_n(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#nearest_n PreparedQuery#nearest_n}.'''
        result = self._values.get("nearest_n")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PreparedQueryFailover(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PreparedQueryFailoverOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-consul.preparedQuery.PreparedQueryFailoverOutputReference",
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
            type_hints = typing.get_type_hints(PreparedQueryFailoverOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDatacenters")
    def reset_datacenters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatacenters", []))

    @jsii.member(jsii_name="resetNearestN")
    def reset_nearest_n(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNearestN", []))

    @builtins.property
    @jsii.member(jsii_name="datacentersInput")
    def datacenters_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "datacentersInput"))

    @builtins.property
    @jsii.member(jsii_name="nearestNInput")
    def nearest_n_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "nearestNInput"))

    @builtins.property
    @jsii.member(jsii_name="datacenters")
    def datacenters(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "datacenters"))

    @datacenters.setter
    def datacenters(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PreparedQueryFailoverOutputReference, "datacenters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datacenters", value)

    @builtins.property
    @jsii.member(jsii_name="nearestN")
    def nearest_n(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "nearestN"))

    @nearest_n.setter
    def nearest_n(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PreparedQueryFailoverOutputReference, "nearest_n").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nearestN", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PreparedQueryFailover]:
        return typing.cast(typing.Optional[PreparedQueryFailover], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[PreparedQueryFailover]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PreparedQueryFailoverOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-consul.preparedQuery.PreparedQueryTemplate",
    jsii_struct_bases=[],
    name_mapping={"regexp": "regexp", "type": "type"},
)
class PreparedQueryTemplate:
    def __init__(self, *, regexp: builtins.str, type: builtins.str) -> None:
        '''
        :param regexp: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#regexp PreparedQuery#regexp}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#type PreparedQuery#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(PreparedQueryTemplate.__init__)
            check_type(argname="argument regexp", value=regexp, expected_type=type_hints["regexp"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "regexp": regexp,
            "type": type,
        }

    @builtins.property
    def regexp(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#regexp PreparedQuery#regexp}.'''
        result = self._values.get("regexp")
        assert result is not None, "Required property 'regexp' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/consul/r/prepared_query#type PreparedQuery#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PreparedQueryTemplate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class PreparedQueryTemplateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-consul.preparedQuery.PreparedQueryTemplateOutputReference",
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
            type_hints = typing.get_type_hints(PreparedQueryTemplateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="regexpInput")
    def regexp_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regexpInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="regexp")
    def regexp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regexp"))

    @regexp.setter
    def regexp(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PreparedQueryTemplateOutputReference, "regexp").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regexp", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PreparedQueryTemplateOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[PreparedQueryTemplate]:
        return typing.cast(typing.Optional[PreparedQueryTemplate], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[PreparedQueryTemplate]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(PreparedQueryTemplateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "PreparedQuery",
    "PreparedQueryConfig",
    "PreparedQueryDns",
    "PreparedQueryDnsOutputReference",
    "PreparedQueryFailover",
    "PreparedQueryFailoverOutputReference",
    "PreparedQueryTemplate",
    "PreparedQueryTemplateOutputReference",
]

publication.publish()
