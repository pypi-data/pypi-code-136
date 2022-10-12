'''
# `digitalocean_app`

Refer to the Terraform Registory for docs: [`digitalocean_app`](https://www.terraform.io/docs/providers/digitalocean/r/app).
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


class App(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.App",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/digitalocean/r/app digitalocean_app}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        id: typing.Optional[builtins.str] = None,
        spec: typing.Optional[typing.Union["AppSpec", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["AppTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/digitalocean/r/app digitalocean_app} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#id App#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#spec App#spec}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#timeouts App#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(App.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = AppConfig(
            id=id,
            spec=spec,
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

    @jsii.member(jsii_name="putSpec")
    def put_spec(
        self,
        *,
        name: builtins.str,
        alert: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecAlert", typing.Dict[str, typing.Any]]]]] = None,
        database: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecDatabase", typing.Dict[str, typing.Any]]]]] = None,
        domain: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecDomain", typing.Dict[str, typing.Any]]]]] = None,
        domains: typing.Optional[typing.Sequence[builtins.str]] = None,
        env: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecEnv", typing.Dict[str, typing.Any]]]]] = None,
        function: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecFunction", typing.Dict[str, typing.Any]]]]] = None,
        job: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecJob", typing.Dict[str, typing.Any]]]]] = None,
        region: typing.Optional[builtins.str] = None,
        service: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecService", typing.Dict[str, typing.Any]]]]] = None,
        static_site: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecStaticSite", typing.Dict[str, typing.Any]]]]] = None,
        worker: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecWorker", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name: The name of the app. Must be unique across all apps in the same account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#name App#name}
        :param alert: alert block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#alert App#alert}
        :param database: database block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#database App#database}
        :param domain: domain block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#domain App#domain}
        :param domains: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#domains App#domains}.
        :param env: env block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#env App#env}
        :param function: function block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#function App#function}
        :param job: job block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#job App#job}
        :param region: The slug for the DigitalOcean data center region hosting the app. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#region App#region}
        :param service: service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#service App#service}
        :param static_site: static_site block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#static_site App#static_site}
        :param worker: worker block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#worker App#worker}
        '''
        value = AppSpec(
            name=name,
            alert=alert,
            database=database,
            domain=domain,
            domains=domains,
            env=env,
            function=function,
            job=job,
            region=region,
            service=service,
            static_site=static_site,
            worker=worker,
        )

        return typing.cast(None, jsii.invoke(self, "putSpec", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(self, *, create: typing.Optional[builtins.str] = None) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#create App#create}.
        '''
        value = AppTimeouts(create=create)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetSpec")
    def reset_spec(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSpec", []))

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
    @jsii.member(jsii_name="activeDeploymentId")
    def active_deployment_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "activeDeploymentId"))

    @builtins.property
    @jsii.member(jsii_name="createdAt")
    def created_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdAt"))

    @builtins.property
    @jsii.member(jsii_name="defaultIngress")
    def default_ingress(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultIngress"))

    @builtins.property
    @jsii.member(jsii_name="liveUrl")
    def live_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "liveUrl"))

    @builtins.property
    @jsii.member(jsii_name="spec")
    def spec(self) -> "AppSpecOutputReference":
        return typing.cast("AppSpecOutputReference", jsii.get(self, "spec"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "AppTimeoutsOutputReference":
        return typing.cast("AppTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="updatedAt")
    def updated_at(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "updatedAt"))

    @builtins.property
    @jsii.member(jsii_name="urn")
    def urn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "urn"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="specInput")
    def spec_input(self) -> typing.Optional["AppSpec"]:
        return typing.cast(typing.Optional["AppSpec"], jsii.get(self, "specInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["AppTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["AppTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(App, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "id": "id",
        "spec": "spec",
        "timeouts": "timeouts",
    },
)
class AppConfig(cdktf.TerraformMetaArguments):
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
        id: typing.Optional[builtins.str] = None,
        spec: typing.Optional[typing.Union["AppSpec", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["AppTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#id App#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param spec: spec block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#spec App#spec}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#timeouts App#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(spec, dict):
            spec = AppSpec(**spec)
        if isinstance(timeouts, dict):
            timeouts = AppTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(AppConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument spec", value=spec, expected_type=type_hints["spec"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
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
        if id is not None:
            self._values["id"] = id
        if spec is not None:
            self._values["spec"] = spec
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
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#id App#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def spec(self) -> typing.Optional["AppSpec"]:
        '''spec block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#spec App#spec}
        '''
        result = self._values.get("spec")
        return typing.cast(typing.Optional["AppSpec"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["AppTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#timeouts App#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["AppTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpec",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "alert": "alert",
        "database": "database",
        "domain": "domain",
        "domains": "domains",
        "env": "env",
        "function": "function",
        "job": "job",
        "region": "region",
        "service": "service",
        "static_site": "staticSite",
        "worker": "worker",
    },
)
class AppSpec:
    def __init__(
        self,
        *,
        name: builtins.str,
        alert: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecAlert", typing.Dict[str, typing.Any]]]]] = None,
        database: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecDatabase", typing.Dict[str, typing.Any]]]]] = None,
        domain: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecDomain", typing.Dict[str, typing.Any]]]]] = None,
        domains: typing.Optional[typing.Sequence[builtins.str]] = None,
        env: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecEnv", typing.Dict[str, typing.Any]]]]] = None,
        function: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecFunction", typing.Dict[str, typing.Any]]]]] = None,
        job: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecJob", typing.Dict[str, typing.Any]]]]] = None,
        region: typing.Optional[builtins.str] = None,
        service: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecService", typing.Dict[str, typing.Any]]]]] = None,
        static_site: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecStaticSite", typing.Dict[str, typing.Any]]]]] = None,
        worker: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecWorker", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param name: The name of the app. Must be unique across all apps in the same account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#name App#name}
        :param alert: alert block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#alert App#alert}
        :param database: database block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#database App#database}
        :param domain: domain block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#domain App#domain}
        :param domains: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#domains App#domains}.
        :param env: env block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#env App#env}
        :param function: function block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#function App#function}
        :param job: job block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#job App#job}
        :param region: The slug for the DigitalOcean data center region hosting the app. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#region App#region}
        :param service: service block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#service App#service}
        :param static_site: static_site block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#static_site App#static_site}
        :param worker: worker block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#worker App#worker}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpec.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument alert", value=alert, expected_type=type_hints["alert"])
            check_type(argname="argument database", value=database, expected_type=type_hints["database"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument domains", value=domains, expected_type=type_hints["domains"])
            check_type(argname="argument env", value=env, expected_type=type_hints["env"])
            check_type(argname="argument function", value=function, expected_type=type_hints["function"])
            check_type(argname="argument job", value=job, expected_type=type_hints["job"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument static_site", value=static_site, expected_type=type_hints["static_site"])
            check_type(argname="argument worker", value=worker, expected_type=type_hints["worker"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if alert is not None:
            self._values["alert"] = alert
        if database is not None:
            self._values["database"] = database
        if domain is not None:
            self._values["domain"] = domain
        if domains is not None:
            self._values["domains"] = domains
        if env is not None:
            self._values["env"] = env
        if function is not None:
            self._values["function"] = function
        if job is not None:
            self._values["job"] = job
        if region is not None:
            self._values["region"] = region
        if service is not None:
            self._values["service"] = service
        if static_site is not None:
            self._values["static_site"] = static_site
        if worker is not None:
            self._values["worker"] = worker

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the app. Must be unique across all apps in the same account.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#name App#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alert(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecAlert"]]]:
        '''alert block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#alert App#alert}
        '''
        result = self._values.get("alert")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecAlert"]]], result)

    @builtins.property
    def database(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecDatabase"]]]:
        '''database block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#database App#database}
        '''
        result = self._values.get("database")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecDatabase"]]], result)

    @builtins.property
    def domain(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecDomain"]]]:
        '''domain block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#domain App#domain}
        '''
        result = self._values.get("domain")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecDomain"]]], result)

    @builtins.property
    def domains(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#domains App#domains}.'''
        result = self._values.get("domains")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def env(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecEnv"]]]:
        '''env block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#env App#env}
        '''
        result = self._values.get("env")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecEnv"]]], result)

    @builtins.property
    def function(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecFunction"]]]:
        '''function block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#function App#function}
        '''
        result = self._values.get("function")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecFunction"]]], result)

    @builtins.property
    def job(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecJob"]]]:
        '''job block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#job App#job}
        '''
        result = self._values.get("job")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecJob"]]], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The slug for the DigitalOcean data center region hosting the app.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#region App#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecService"]]]:
        '''service block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#service App#service}
        '''
        result = self._values.get("service")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecService"]]], result)

    @builtins.property
    def static_site(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecStaticSite"]]]:
        '''static_site block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#static_site App#static_site}
        '''
        result = self._values.get("static_site")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecStaticSite"]]], result)

    @builtins.property
    def worker(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecWorker"]]]:
        '''worker block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#worker App#worker}
        '''
        result = self._values.get("worker")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecWorker"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpec(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecAlert",
    jsii_struct_bases=[],
    name_mapping={"rule": "rule", "disabled": "disabled"},
)
class AppSpecAlert:
    def __init__(
        self,
        *,
        rule: builtins.str,
        disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param rule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#rule App#rule}.
        :param disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#disabled App#disabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecAlert.__init__)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "rule": rule,
        }
        if disabled is not None:
            self._values["disabled"] = disabled

    @builtins.property
    def rule(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#rule App#rule}.'''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#disabled App#disabled}.'''
        result = self._values.get("disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecAlert(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecAlertList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecAlertList",
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
            type_hints = typing.get_type_hints(AppSpecAlertList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AppSpecAlertOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecAlertList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppSpecAlertOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecAlertList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecAlertList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecAlertList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecAlert]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecAlert]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecAlert]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecAlertList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecAlertOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecAlertOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecAlertOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDisabled")
    def reset_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisabled", []))

    @builtins.property
    @jsii.member(jsii_name="disabledInput")
    def disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disabledInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="disabled")
    def disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disabled"))

    @disabled.setter
    def disabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecAlertOutputReference, "disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rule"))

    @rule.setter
    def rule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecAlertOutputReference, "rule").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppSpecAlert, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppSpecAlert, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppSpecAlert, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecAlertOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecDatabase",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_name": "clusterName",
        "db_name": "dbName",
        "db_user": "dbUser",
        "engine": "engine",
        "name": "name",
        "production": "production",
        "version": "version",
    },
)
class AppSpecDatabase:
    def __init__(
        self,
        *,
        cluster_name: typing.Optional[builtins.str] = None,
        db_name: typing.Optional[builtins.str] = None,
        db_user: typing.Optional[builtins.str] = None,
        engine: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        production: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param cluster_name: The name of the underlying DigitalOcean DBaaS cluster. This is required for production databases. For dev databases, if cluster_name is not set, a new cluster will be provisioned. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#cluster_name App#cluster_name}
        :param db_name: The name of the MySQL or PostgreSQL database to configure. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#db_name App#db_name}
        :param db_user: The name of the MySQL or PostgreSQL user to configure. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#db_user App#db_user}
        :param engine: The database engine to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#engine App#engine}
        :param name: The name of the component. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#name App#name}
        :param production: Whether this is a production or dev database. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#production App#production}
        :param version: The version of the database engine. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#version App#version}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecDatabase.__init__)
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
            check_type(argname="argument db_name", value=db_name, expected_type=type_hints["db_name"])
            check_type(argname="argument db_user", value=db_user, expected_type=type_hints["db_user"])
            check_type(argname="argument engine", value=engine, expected_type=type_hints["engine"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument production", value=production, expected_type=type_hints["production"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {}
        if cluster_name is not None:
            self._values["cluster_name"] = cluster_name
        if db_name is not None:
            self._values["db_name"] = db_name
        if db_user is not None:
            self._values["db_user"] = db_user
        if engine is not None:
            self._values["engine"] = engine
        if name is not None:
            self._values["name"] = name
        if production is not None:
            self._values["production"] = production
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def cluster_name(self) -> typing.Optional[builtins.str]:
        '''The name of the underlying DigitalOcean DBaaS cluster.

        This is required for production databases. For dev databases, if cluster_name is not set, a new cluster will be provisioned.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#cluster_name App#cluster_name}
        '''
        result = self._values.get("cluster_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def db_name(self) -> typing.Optional[builtins.str]:
        '''The name of the MySQL or PostgreSQL database to configure.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#db_name App#db_name}
        '''
        result = self._values.get("db_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def db_user(self) -> typing.Optional[builtins.str]:
        '''The name of the MySQL or PostgreSQL user to configure.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#db_user App#db_user}
        '''
        result = self._values.get("db_user")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def engine(self) -> typing.Optional[builtins.str]:
        '''The database engine to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#engine App#engine}
        '''
        result = self._values.get("engine")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the component.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#name App#name}
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def production(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether this is a production or dev database.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#production App#production}
        '''
        result = self._values.get("production")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''The version of the database engine.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#version App#version}
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecDatabase(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecDatabaseList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecDatabaseList",
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
            type_hints = typing.get_type_hints(AppSpecDatabaseList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AppSpecDatabaseOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecDatabaseList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppSpecDatabaseOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecDatabaseList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecDatabaseList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecDatabaseList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecDatabase]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecDatabase]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecDatabase]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecDatabaseList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecDatabaseOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecDatabaseOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecDatabaseOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetClusterName")
    def reset_cluster_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClusterName", []))

    @jsii.member(jsii_name="resetDbName")
    def reset_db_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDbName", []))

    @jsii.member(jsii_name="resetDbUser")
    def reset_db_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDbUser", []))

    @jsii.member(jsii_name="resetEngine")
    def reset_engine(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEngine", []))

    @jsii.member(jsii_name="resetName")
    def reset_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetName", []))

    @jsii.member(jsii_name="resetProduction")
    def reset_production(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProduction", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @builtins.property
    @jsii.member(jsii_name="clusterNameInput")
    def cluster_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterNameInput"))

    @builtins.property
    @jsii.member(jsii_name="dbNameInput")
    def db_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbNameInput"))

    @builtins.property
    @jsii.member(jsii_name="dbUserInput")
    def db_user_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dbUserInput"))

    @builtins.property
    @jsii.member(jsii_name="engineInput")
    def engine_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engineInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="productionInput")
    def production_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "productionInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterName"))

    @cluster_name.setter
    def cluster_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecDatabaseOutputReference, "cluster_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterName", value)

    @builtins.property
    @jsii.member(jsii_name="dbName")
    def db_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dbName"))

    @db_name.setter
    def db_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecDatabaseOutputReference, "db_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbName", value)

    @builtins.property
    @jsii.member(jsii_name="dbUser")
    def db_user(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dbUser"))

    @db_user.setter
    def db_user(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecDatabaseOutputReference, "db_user").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dbUser", value)

    @builtins.property
    @jsii.member(jsii_name="engine")
    def engine(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "engine"))

    @engine.setter
    def engine(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecDatabaseOutputReference, "engine").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engine", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecDatabaseOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="production")
    def production(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "production"))

    @production.setter
    def production(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecDatabaseOutputReference, "production").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "production", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecDatabaseOutputReference, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppSpecDatabase, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppSpecDatabase, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppSpecDatabase, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecDatabaseOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecDomain",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "type": "type",
        "wildcard": "wildcard",
        "zone": "zone",
    },
)
class AppSpecDomain:
    def __init__(
        self,
        *,
        name: builtins.str,
        type: typing.Optional[builtins.str] = None,
        wildcard: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: The hostname for the domain. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#name App#name}
        :param type: The type of the domain. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#type App#type}
        :param wildcard: Indicates whether the domain includes all sub-domains, in addition to the given domain. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#wildcard App#wildcard}
        :param zone: If the domain uses DigitalOcean DNS and you would like App Platform to automatically manage it for you, set this to the name of the domain on your account. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#zone App#zone}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecDomain.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument wildcard", value=wildcard, expected_type=type_hints["wildcard"])
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if type is not None:
            self._values["type"] = type
        if wildcard is not None:
            self._values["wildcard"] = wildcard
        if zone is not None:
            self._values["zone"] = zone

    @builtins.property
    def name(self) -> builtins.str:
        '''The hostname for the domain.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#name App#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of the domain.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#type App#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def wildcard(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates whether the domain includes all sub-domains, in addition to the given domain.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#wildcard App#wildcard}
        '''
        result = self._values.get("wildcard")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def zone(self) -> typing.Optional[builtins.str]:
        '''If the domain uses DigitalOcean DNS and you would like App Platform to automatically manage it for you, set this to the name of the domain on your account.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#zone App#zone}
        '''
        result = self._values.get("zone")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecDomain(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecDomainList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecDomainList",
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
            type_hints = typing.get_type_hints(AppSpecDomainList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AppSpecDomainOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecDomainList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppSpecDomainOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecDomainList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecDomainList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecDomainList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecDomain]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecDomain]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecDomain]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecDomainList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecDomainOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecDomainOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecDomainOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetWildcard")
    def reset_wildcard(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWildcard", []))

    @jsii.member(jsii_name="resetZone")
    def reset_zone(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetZone", []))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="wildcardInput")
    def wildcard_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "wildcardInput"))

    @builtins.property
    @jsii.member(jsii_name="zoneInput")
    def zone_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "zoneInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecDomainOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecDomainOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="wildcard")
    def wildcard(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "wildcard"))

    @wildcard.setter
    def wildcard(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecDomainOutputReference, "wildcard").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wildcard", value)

    @builtins.property
    @jsii.member(jsii_name="zone")
    def zone(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "zone"))

    @zone.setter
    def zone(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecDomainOutputReference, "zone").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "zone", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppSpecDomain, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppSpecDomain, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppSpecDomain, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecDomainOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecEnv",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "scope": "scope", "type": "type", "value": "value"},
)
class AppSpecEnv:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        scope: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: The name of the environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#key App#key}
        :param scope: The visibility scope of the environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#scope App#scope}
        :param type: The type of the environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#type App#type}
        :param value: The value of the environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#value App#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecEnv.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if scope is not None:
            self._values["scope"] = scope
        if type is not None:
            self._values["type"] = type
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The name of the environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#key App#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scope(self) -> typing.Optional[builtins.str]:
        '''The visibility scope of the environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#scope App#scope}
        '''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of the environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#type App#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''The value of the environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#value App#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecEnv(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecEnvList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecEnvList",
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
            type_hints = typing.get_type_hints(AppSpecEnvList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AppSpecEnvOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecEnvList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppSpecEnvOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecEnvList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecEnvList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecEnvList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecEnv]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecEnv]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecEnv]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecEnvList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecEnvOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecEnvOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecEnvOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetScope")
    def reset_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScope", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="scopeInput")
    def scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scopeInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecEnvOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecEnvOutputReference, "scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecEnvOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecEnvOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppSpecEnv, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppSpecEnv, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppSpecEnv, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecEnvOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecFunction",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "alert": "alert",
        "cors": "cors",
        "env": "env",
        "git": "git",
        "github": "github",
        "gitlab": "gitlab",
        "log_destination": "logDestination",
        "routes": "routes",
        "source_dir": "sourceDir",
    },
)
class AppSpecFunction:
    def __init__(
        self,
        *,
        name: builtins.str,
        alert: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecFunctionAlert", typing.Dict[str, typing.Any]]]]] = None,
        cors: typing.Optional[typing.Union["AppSpecFunctionCors", typing.Dict[str, typing.Any]]] = None,
        env: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecFunctionEnv", typing.Dict[str, typing.Any]]]]] = None,
        git: typing.Optional[typing.Union["AppSpecFunctionGit", typing.Dict[str, typing.Any]]] = None,
        github: typing.Optional[typing.Union["AppSpecFunctionGithub", typing.Dict[str, typing.Any]]] = None,
        gitlab: typing.Optional[typing.Union["AppSpecFunctionGitlab", typing.Dict[str, typing.Any]]] = None,
        log_destination: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecFunctionLogDestination", typing.Dict[str, typing.Any]]]]] = None,
        routes: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecFunctionRoutes", typing.Dict[str, typing.Any]]]]] = None,
        source_dir: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: The name of the component. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#name App#name}
        :param alert: alert block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#alert App#alert}
        :param cors: cors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#cors App#cors}
        :param env: env block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#env App#env}
        :param git: git block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#git App#git}
        :param github: github block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#github App#github}
        :param gitlab: gitlab block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#gitlab App#gitlab}
        :param log_destination: log_destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#log_destination App#log_destination}
        :param routes: routes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#routes App#routes}
        :param source_dir: An optional path to the working directory to use for the build. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#source_dir App#source_dir}
        '''
        if isinstance(cors, dict):
            cors = AppSpecFunctionCors(**cors)
        if isinstance(git, dict):
            git = AppSpecFunctionGit(**git)
        if isinstance(github, dict):
            github = AppSpecFunctionGithub(**github)
        if isinstance(gitlab, dict):
            gitlab = AppSpecFunctionGitlab(**gitlab)
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecFunction.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument alert", value=alert, expected_type=type_hints["alert"])
            check_type(argname="argument cors", value=cors, expected_type=type_hints["cors"])
            check_type(argname="argument env", value=env, expected_type=type_hints["env"])
            check_type(argname="argument git", value=git, expected_type=type_hints["git"])
            check_type(argname="argument github", value=github, expected_type=type_hints["github"])
            check_type(argname="argument gitlab", value=gitlab, expected_type=type_hints["gitlab"])
            check_type(argname="argument log_destination", value=log_destination, expected_type=type_hints["log_destination"])
            check_type(argname="argument routes", value=routes, expected_type=type_hints["routes"])
            check_type(argname="argument source_dir", value=source_dir, expected_type=type_hints["source_dir"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if alert is not None:
            self._values["alert"] = alert
        if cors is not None:
            self._values["cors"] = cors
        if env is not None:
            self._values["env"] = env
        if git is not None:
            self._values["git"] = git
        if github is not None:
            self._values["github"] = github
        if gitlab is not None:
            self._values["gitlab"] = gitlab
        if log_destination is not None:
            self._values["log_destination"] = log_destination
        if routes is not None:
            self._values["routes"] = routes
        if source_dir is not None:
            self._values["source_dir"] = source_dir

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the component.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#name App#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alert(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecFunctionAlert"]]]:
        '''alert block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#alert App#alert}
        '''
        result = self._values.get("alert")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecFunctionAlert"]]], result)

    @builtins.property
    def cors(self) -> typing.Optional["AppSpecFunctionCors"]:
        '''cors block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#cors App#cors}
        '''
        result = self._values.get("cors")
        return typing.cast(typing.Optional["AppSpecFunctionCors"], result)

    @builtins.property
    def env(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecFunctionEnv"]]]:
        '''env block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#env App#env}
        '''
        result = self._values.get("env")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecFunctionEnv"]]], result)

    @builtins.property
    def git(self) -> typing.Optional["AppSpecFunctionGit"]:
        '''git block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#git App#git}
        '''
        result = self._values.get("git")
        return typing.cast(typing.Optional["AppSpecFunctionGit"], result)

    @builtins.property
    def github(self) -> typing.Optional["AppSpecFunctionGithub"]:
        '''github block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#github App#github}
        '''
        result = self._values.get("github")
        return typing.cast(typing.Optional["AppSpecFunctionGithub"], result)

    @builtins.property
    def gitlab(self) -> typing.Optional["AppSpecFunctionGitlab"]:
        '''gitlab block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#gitlab App#gitlab}
        '''
        result = self._values.get("gitlab")
        return typing.cast(typing.Optional["AppSpecFunctionGitlab"], result)

    @builtins.property
    def log_destination(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecFunctionLogDestination"]]]:
        '''log_destination block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#log_destination App#log_destination}
        '''
        result = self._values.get("log_destination")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecFunctionLogDestination"]]], result)

    @builtins.property
    def routes(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecFunctionRoutes"]]]:
        '''routes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#routes App#routes}
        '''
        result = self._values.get("routes")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecFunctionRoutes"]]], result)

    @builtins.property
    def source_dir(self) -> typing.Optional[builtins.str]:
        '''An optional path to the working directory to use for the build.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#source_dir App#source_dir}
        '''
        result = self._values.get("source_dir")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecFunction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecFunctionAlert",
    jsii_struct_bases=[],
    name_mapping={
        "operator": "operator",
        "rule": "rule",
        "value": "value",
        "window": "window",
        "disabled": "disabled",
    },
)
class AppSpecFunctionAlert:
    def __init__(
        self,
        *,
        operator: builtins.str,
        rule: builtins.str,
        value: jsii.Number,
        window: builtins.str,
        disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#operator App#operator}.
        :param rule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#rule App#rule}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#value App#value}.
        :param window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#window App#window}.
        :param disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#disabled App#disabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecFunctionAlert.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument window", value=window, expected_type=type_hints["window"])
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
            "rule": rule,
            "value": value,
            "window": window,
        }
        if disabled is not None:
            self._values["disabled"] = disabled

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#operator App#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#rule App#rule}.'''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#value App#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def window(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#window App#window}.'''
        result = self._values.get("window")
        assert result is not None, "Required property 'window' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#disabled App#disabled}.'''
        result = self._values.get("disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecFunctionAlert(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecFunctionAlertList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecFunctionAlertList",
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
            type_hints = typing.get_type_hints(AppSpecFunctionAlertList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AppSpecFunctionAlertOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecFunctionAlertList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppSpecFunctionAlertOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionAlertList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionAlertList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionAlertList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecFunctionAlert]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecFunctionAlert]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecFunctionAlert]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionAlertList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecFunctionAlertOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecFunctionAlertOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecFunctionAlertOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDisabled")
    def reset_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisabled", []))

    @builtins.property
    @jsii.member(jsii_name="disabledInput")
    def disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disabledInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="windowInput")
    def window_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "windowInput"))

    @builtins.property
    @jsii.member(jsii_name="disabled")
    def disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disabled"))

    @disabled.setter
    def disabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionAlertOutputReference, "disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionAlertOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rule"))

    @rule.setter
    def rule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionAlertOutputReference, "rule").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionAlertOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="window")
    def window(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "window"))

    @window.setter
    def window(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionAlertOutputReference, "window").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "window", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppSpecFunctionAlert, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppSpecFunctionAlert, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppSpecFunctionAlert, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionAlertOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecFunctionCors",
    jsii_struct_bases=[],
    name_mapping={
        "allow_credentials": "allowCredentials",
        "allow_headers": "allowHeaders",
        "allow_methods": "allowMethods",
        "allow_origins": "allowOrigins",
        "expose_headers": "exposeHeaders",
        "max_age": "maxAge",
    },
)
class AppSpecFunctionCors:
    def __init__(
        self,
        *,
        allow_credentials: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_methods: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_origins: typing.Optional[typing.Union["AppSpecFunctionCorsAllowOrigins", typing.Dict[str, typing.Any]]] = None,
        expose_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        max_age: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allow_credentials: Whether browsers should expose the response to the client-side JavaScript code when the request’s credentials mode is ``include``. This configures the Access-Control-Allow-Credentials header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_credentials App#allow_credentials}
        :param allow_headers: The set of allowed HTTP request headers. This configures the Access-Control-Allow-Headers header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_headers App#allow_headers}
        :param allow_methods: The set of allowed HTTP methods. This configures the Access-Control-Allow-Methods header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_methods App#allow_methods}
        :param allow_origins: allow_origins block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_origins App#allow_origins}
        :param expose_headers: The set of HTTP response headers that browsers are allowed to access. This configures the Access-Control-Expose-Headers header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#expose_headers App#expose_headers}
        :param max_age: An optional duration specifying how long browsers can cache the results of a preflight request. This configures the Access-Control-Max-Age header. Example: ``5h30m``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#max_age App#max_age}
        '''
        if isinstance(allow_origins, dict):
            allow_origins = AppSpecFunctionCorsAllowOrigins(**allow_origins)
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecFunctionCors.__init__)
            check_type(argname="argument allow_credentials", value=allow_credentials, expected_type=type_hints["allow_credentials"])
            check_type(argname="argument allow_headers", value=allow_headers, expected_type=type_hints["allow_headers"])
            check_type(argname="argument allow_methods", value=allow_methods, expected_type=type_hints["allow_methods"])
            check_type(argname="argument allow_origins", value=allow_origins, expected_type=type_hints["allow_origins"])
            check_type(argname="argument expose_headers", value=expose_headers, expected_type=type_hints["expose_headers"])
            check_type(argname="argument max_age", value=max_age, expected_type=type_hints["max_age"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allow_credentials is not None:
            self._values["allow_credentials"] = allow_credentials
        if allow_headers is not None:
            self._values["allow_headers"] = allow_headers
        if allow_methods is not None:
            self._values["allow_methods"] = allow_methods
        if allow_origins is not None:
            self._values["allow_origins"] = allow_origins
        if expose_headers is not None:
            self._values["expose_headers"] = expose_headers
        if max_age is not None:
            self._values["max_age"] = max_age

    @builtins.property
    def allow_credentials(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether browsers should expose the response to the client-side JavaScript code when the request’s credentials mode is ``include``.

        This configures the Access-Control-Allow-Credentials header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_credentials App#allow_credentials}
        '''
        result = self._values.get("allow_credentials")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The set of allowed HTTP request headers. This configures the Access-Control-Allow-Headers header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_headers App#allow_headers}
        '''
        result = self._values.get("allow_headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allow_methods(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The set of allowed HTTP methods. This configures the Access-Control-Allow-Methods header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_methods App#allow_methods}
        '''
        result = self._values.get("allow_methods")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allow_origins(self) -> typing.Optional["AppSpecFunctionCorsAllowOrigins"]:
        '''allow_origins block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_origins App#allow_origins}
        '''
        result = self._values.get("allow_origins")
        return typing.cast(typing.Optional["AppSpecFunctionCorsAllowOrigins"], result)

    @builtins.property
    def expose_headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The set of HTTP response headers that browsers are allowed to access. This configures the Access-Control-Expose-Headers header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#expose_headers App#expose_headers}
        '''
        result = self._values.get("expose_headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def max_age(self) -> typing.Optional[builtins.str]:
        '''An optional duration specifying how long browsers can cache the results of a preflight request.

        This configures the Access-Control-Max-Age header. Example: ``5h30m``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#max_age App#max_age}
        '''
        result = self._values.get("max_age")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecFunctionCors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecFunctionCorsAllowOrigins",
    jsii_struct_bases=[],
    name_mapping={"exact": "exact", "prefix": "prefix", "regex": "regex"},
)
class AppSpecFunctionCorsAllowOrigins:
    def __init__(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        regex: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param exact: Exact string match. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#exact App#exact}
        :param prefix: Prefix-based match. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#prefix App#prefix}
        :param regex: RE2 style regex-based match. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#regex App#regex}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecFunctionCorsAllowOrigins.__init__)
            check_type(argname="argument exact", value=exact, expected_type=type_hints["exact"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument regex", value=regex, expected_type=type_hints["regex"])
        self._values: typing.Dict[str, typing.Any] = {}
        if exact is not None:
            self._values["exact"] = exact
        if prefix is not None:
            self._values["prefix"] = prefix
        if regex is not None:
            self._values["regex"] = regex

    @builtins.property
    def exact(self) -> typing.Optional[builtins.str]:
        '''Exact string match.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#exact App#exact}
        '''
        result = self._values.get("exact")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Prefix-based match.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#prefix App#prefix}
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def regex(self) -> typing.Optional[builtins.str]:
        '''RE2 style regex-based match.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#regex App#regex}
        '''
        result = self._values.get("regex")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecFunctionCorsAllowOrigins(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecFunctionCorsAllowOriginsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecFunctionCorsAllowOriginsOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecFunctionCorsAllowOriginsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExact")
    def reset_exact(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExact", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @jsii.member(jsii_name="resetRegex")
    def reset_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegex", []))

    @builtins.property
    @jsii.member(jsii_name="exactInput")
    def exact_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "exactInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="regexInput")
    def regex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regexInput"))

    @builtins.property
    @jsii.member(jsii_name="exact")
    def exact(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "exact"))

    @exact.setter
    def exact(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionCorsAllowOriginsOutputReference, "exact").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exact", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionCorsAllowOriginsOutputReference, "prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="regex")
    def regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regex"))

    @regex.setter
    def regex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionCorsAllowOriginsOutputReference, "regex").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regex", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecFunctionCorsAllowOrigins]:
        return typing.cast(typing.Optional[AppSpecFunctionCorsAllowOrigins], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppSpecFunctionCorsAllowOrigins],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionCorsAllowOriginsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecFunctionCorsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecFunctionCorsOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecFunctionCorsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAllowOrigins")
    def put_allow_origins(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        regex: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param exact: Exact string match. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#exact App#exact}
        :param prefix: Prefix-based match. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#prefix App#prefix}
        :param regex: RE2 style regex-based match. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#regex App#regex}
        '''
        value = AppSpecFunctionCorsAllowOrigins(
            exact=exact, prefix=prefix, regex=regex
        )

        return typing.cast(None, jsii.invoke(self, "putAllowOrigins", [value]))

    @jsii.member(jsii_name="resetAllowCredentials")
    def reset_allow_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowCredentials", []))

    @jsii.member(jsii_name="resetAllowHeaders")
    def reset_allow_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowHeaders", []))

    @jsii.member(jsii_name="resetAllowMethods")
    def reset_allow_methods(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowMethods", []))

    @jsii.member(jsii_name="resetAllowOrigins")
    def reset_allow_origins(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowOrigins", []))

    @jsii.member(jsii_name="resetExposeHeaders")
    def reset_expose_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExposeHeaders", []))

    @jsii.member(jsii_name="resetMaxAge")
    def reset_max_age(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxAge", []))

    @builtins.property
    @jsii.member(jsii_name="allowOrigins")
    def allow_origins(self) -> AppSpecFunctionCorsAllowOriginsOutputReference:
        return typing.cast(AppSpecFunctionCorsAllowOriginsOutputReference, jsii.get(self, "allowOrigins"))

    @builtins.property
    @jsii.member(jsii_name="allowCredentialsInput")
    def allow_credentials_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowCredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowHeadersInput")
    def allow_headers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="allowMethodsInput")
    def allow_methods_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowMethodsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowOriginsInput")
    def allow_origins_input(self) -> typing.Optional[AppSpecFunctionCorsAllowOrigins]:
        return typing.cast(typing.Optional[AppSpecFunctionCorsAllowOrigins], jsii.get(self, "allowOriginsInput"))

    @builtins.property
    @jsii.member(jsii_name="exposeHeadersInput")
    def expose_headers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exposeHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="maxAgeInput")
    def max_age_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxAgeInput"))

    @builtins.property
    @jsii.member(jsii_name="allowCredentials")
    def allow_credentials(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowCredentials"))

    @allow_credentials.setter
    def allow_credentials(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionCorsOutputReference, "allow_credentials").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowCredentials", value)

    @builtins.property
    @jsii.member(jsii_name="allowHeaders")
    def allow_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowHeaders"))

    @allow_headers.setter
    def allow_headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionCorsOutputReference, "allow_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="allowMethods")
    def allow_methods(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowMethods"))

    @allow_methods.setter
    def allow_methods(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionCorsOutputReference, "allow_methods").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowMethods", value)

    @builtins.property
    @jsii.member(jsii_name="exposeHeaders")
    def expose_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exposeHeaders"))

    @expose_headers.setter
    def expose_headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionCorsOutputReference, "expose_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exposeHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="maxAge")
    def max_age(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxAge"))

    @max_age.setter
    def max_age(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionCorsOutputReference, "max_age").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAge", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecFunctionCors]:
        return typing.cast(typing.Optional[AppSpecFunctionCors], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppSpecFunctionCors]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionCorsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecFunctionEnv",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "scope": "scope", "type": "type", "value": "value"},
)
class AppSpecFunctionEnv:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        scope: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: The name of the environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#key App#key}
        :param scope: The visibility scope of the environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#scope App#scope}
        :param type: The type of the environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#type App#type}
        :param value: The value of the environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#value App#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecFunctionEnv.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if scope is not None:
            self._values["scope"] = scope
        if type is not None:
            self._values["type"] = type
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The name of the environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#key App#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scope(self) -> typing.Optional[builtins.str]:
        '''The visibility scope of the environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#scope App#scope}
        '''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of the environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#type App#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''The value of the environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#value App#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecFunctionEnv(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecFunctionEnvList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecFunctionEnvList",
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
            type_hints = typing.get_type_hints(AppSpecFunctionEnvList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AppSpecFunctionEnvOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecFunctionEnvList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppSpecFunctionEnvOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionEnvList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionEnvList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionEnvList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecFunctionEnv]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecFunctionEnv]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecFunctionEnv]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionEnvList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecFunctionEnvOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecFunctionEnvOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecFunctionEnvOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetScope")
    def reset_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScope", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="scopeInput")
    def scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scopeInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionEnvOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionEnvOutputReference, "scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionEnvOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionEnvOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppSpecFunctionEnv, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppSpecFunctionEnv, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppSpecFunctionEnv, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionEnvOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecFunctionGit",
    jsii_struct_bases=[],
    name_mapping={"branch": "branch", "repo_clone_url": "repoCloneUrl"},
)
class AppSpecFunctionGit:
    def __init__(
        self,
        *,
        branch: typing.Optional[builtins.str] = None,
        repo_clone_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: The name of the branch to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        :param repo_clone_url: The clone URL of the repo. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo_clone_url App#repo_clone_url}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecFunctionGit.__init__)
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
            check_type(argname="argument repo_clone_url", value=repo_clone_url, expected_type=type_hints["repo_clone_url"])
        self._values: typing.Dict[str, typing.Any] = {}
        if branch is not None:
            self._values["branch"] = branch
        if repo_clone_url is not None:
            self._values["repo_clone_url"] = repo_clone_url

    @builtins.property
    def branch(self) -> typing.Optional[builtins.str]:
        '''The name of the branch to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        '''
        result = self._values.get("branch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def repo_clone_url(self) -> typing.Optional[builtins.str]:
        '''The clone URL of the repo.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo_clone_url App#repo_clone_url}
        '''
        result = self._values.get("repo_clone_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecFunctionGit(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecFunctionGitOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecFunctionGitOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecFunctionGitOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBranch")
    def reset_branch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBranch", []))

    @jsii.member(jsii_name="resetRepoCloneUrl")
    def reset_repo_clone_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepoCloneUrl", []))

    @builtins.property
    @jsii.member(jsii_name="branchInput")
    def branch_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "branchInput"))

    @builtins.property
    @jsii.member(jsii_name="repoCloneUrlInput")
    def repo_clone_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repoCloneUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="branch")
    def branch(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "branch"))

    @branch.setter
    def branch(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionGitOutputReference, "branch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "branch", value)

    @builtins.property
    @jsii.member(jsii_name="repoCloneUrl")
    def repo_clone_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repoCloneUrl"))

    @repo_clone_url.setter
    def repo_clone_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionGitOutputReference, "repo_clone_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repoCloneUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecFunctionGit]:
        return typing.cast(typing.Optional[AppSpecFunctionGit], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppSpecFunctionGit]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionGitOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecFunctionGithub",
    jsii_struct_bases=[],
    name_mapping={
        "branch": "branch",
        "deploy_on_push": "deployOnPush",
        "repo": "repo",
    },
)
class AppSpecFunctionGithub:
    def __init__(
        self,
        *,
        branch: typing.Optional[builtins.str] = None,
        deploy_on_push: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: The name of the branch to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        :param deploy_on_push: Whether to automatically deploy new commits made to the repo. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        :param repo: The name of the repo in the format ``owner/repo``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo App#repo}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecFunctionGithub.__init__)
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
            check_type(argname="argument deploy_on_push", value=deploy_on_push, expected_type=type_hints["deploy_on_push"])
            check_type(argname="argument repo", value=repo, expected_type=type_hints["repo"])
        self._values: typing.Dict[str, typing.Any] = {}
        if branch is not None:
            self._values["branch"] = branch
        if deploy_on_push is not None:
            self._values["deploy_on_push"] = deploy_on_push
        if repo is not None:
            self._values["repo"] = repo

    @builtins.property
    def branch(self) -> typing.Optional[builtins.str]:
        '''The name of the branch to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        '''
        result = self._values.get("branch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deploy_on_push(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to automatically deploy new commits made to the repo.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        '''
        result = self._values.get("deploy_on_push")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def repo(self) -> typing.Optional[builtins.str]:
        '''The name of the repo in the format ``owner/repo``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo App#repo}
        '''
        result = self._values.get("repo")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecFunctionGithub(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecFunctionGithubOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecFunctionGithubOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecFunctionGithubOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBranch")
    def reset_branch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBranch", []))

    @jsii.member(jsii_name="resetDeployOnPush")
    def reset_deploy_on_push(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeployOnPush", []))

    @jsii.member(jsii_name="resetRepo")
    def reset_repo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepo", []))

    @builtins.property
    @jsii.member(jsii_name="branchInput")
    def branch_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "branchInput"))

    @builtins.property
    @jsii.member(jsii_name="deployOnPushInput")
    def deploy_on_push_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deployOnPushInput"))

    @builtins.property
    @jsii.member(jsii_name="repoInput")
    def repo_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repoInput"))

    @builtins.property
    @jsii.member(jsii_name="branch")
    def branch(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "branch"))

    @branch.setter
    def branch(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionGithubOutputReference, "branch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "branch", value)

    @builtins.property
    @jsii.member(jsii_name="deployOnPush")
    def deploy_on_push(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "deployOnPush"))

    @deploy_on_push.setter
    def deploy_on_push(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionGithubOutputReference, "deploy_on_push").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deployOnPush", value)

    @builtins.property
    @jsii.member(jsii_name="repo")
    def repo(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repo"))

    @repo.setter
    def repo(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionGithubOutputReference, "repo").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repo", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecFunctionGithub]:
        return typing.cast(typing.Optional[AppSpecFunctionGithub], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppSpecFunctionGithub]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionGithubOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecFunctionGitlab",
    jsii_struct_bases=[],
    name_mapping={
        "branch": "branch",
        "deploy_on_push": "deployOnPush",
        "repo": "repo",
    },
)
class AppSpecFunctionGitlab:
    def __init__(
        self,
        *,
        branch: typing.Optional[builtins.str] = None,
        deploy_on_push: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: The name of the branch to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        :param deploy_on_push: Whether to automatically deploy new commits made to the repo. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        :param repo: The name of the repo in the format ``owner/repo``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo App#repo}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecFunctionGitlab.__init__)
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
            check_type(argname="argument deploy_on_push", value=deploy_on_push, expected_type=type_hints["deploy_on_push"])
            check_type(argname="argument repo", value=repo, expected_type=type_hints["repo"])
        self._values: typing.Dict[str, typing.Any] = {}
        if branch is not None:
            self._values["branch"] = branch
        if deploy_on_push is not None:
            self._values["deploy_on_push"] = deploy_on_push
        if repo is not None:
            self._values["repo"] = repo

    @builtins.property
    def branch(self) -> typing.Optional[builtins.str]:
        '''The name of the branch to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        '''
        result = self._values.get("branch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deploy_on_push(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to automatically deploy new commits made to the repo.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        '''
        result = self._values.get("deploy_on_push")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def repo(self) -> typing.Optional[builtins.str]:
        '''The name of the repo in the format ``owner/repo``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo App#repo}
        '''
        result = self._values.get("repo")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecFunctionGitlab(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecFunctionGitlabOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecFunctionGitlabOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecFunctionGitlabOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBranch")
    def reset_branch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBranch", []))

    @jsii.member(jsii_name="resetDeployOnPush")
    def reset_deploy_on_push(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeployOnPush", []))

    @jsii.member(jsii_name="resetRepo")
    def reset_repo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepo", []))

    @builtins.property
    @jsii.member(jsii_name="branchInput")
    def branch_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "branchInput"))

    @builtins.property
    @jsii.member(jsii_name="deployOnPushInput")
    def deploy_on_push_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deployOnPushInput"))

    @builtins.property
    @jsii.member(jsii_name="repoInput")
    def repo_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repoInput"))

    @builtins.property
    @jsii.member(jsii_name="branch")
    def branch(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "branch"))

    @branch.setter
    def branch(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionGitlabOutputReference, "branch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "branch", value)

    @builtins.property
    @jsii.member(jsii_name="deployOnPush")
    def deploy_on_push(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "deployOnPush"))

    @deploy_on_push.setter
    def deploy_on_push(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionGitlabOutputReference, "deploy_on_push").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deployOnPush", value)

    @builtins.property
    @jsii.member(jsii_name="repo")
    def repo(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repo"))

    @repo.setter
    def repo(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionGitlabOutputReference, "repo").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repo", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecFunctionGitlab]:
        return typing.cast(typing.Optional[AppSpecFunctionGitlab], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppSpecFunctionGitlab]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionGitlabOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecFunctionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecFunctionList",
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
            type_hints = typing.get_type_hints(AppSpecFunctionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AppSpecFunctionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecFunctionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppSpecFunctionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecFunction]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecFunction]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecFunction]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecFunctionLogDestination",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "datadog": "datadog",
        "logtail": "logtail",
        "papertrail": "papertrail",
    },
)
class AppSpecFunctionLogDestination:
    def __init__(
        self,
        *,
        name: builtins.str,
        datadog: typing.Optional[typing.Union["AppSpecFunctionLogDestinationDatadog", typing.Dict[str, typing.Any]]] = None,
        logtail: typing.Optional[typing.Union["AppSpecFunctionLogDestinationLogtail", typing.Dict[str, typing.Any]]] = None,
        papertrail: typing.Optional[typing.Union["AppSpecFunctionLogDestinationPapertrail", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: Name of the log destination. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#name App#name}
        :param datadog: datadog block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#datadog App#datadog}
        :param logtail: logtail block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#logtail App#logtail}
        :param papertrail: papertrail block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#papertrail App#papertrail}
        '''
        if isinstance(datadog, dict):
            datadog = AppSpecFunctionLogDestinationDatadog(**datadog)
        if isinstance(logtail, dict):
            logtail = AppSpecFunctionLogDestinationLogtail(**logtail)
        if isinstance(papertrail, dict):
            papertrail = AppSpecFunctionLogDestinationPapertrail(**papertrail)
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecFunctionLogDestination.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument datadog", value=datadog, expected_type=type_hints["datadog"])
            check_type(argname="argument logtail", value=logtail, expected_type=type_hints["logtail"])
            check_type(argname="argument papertrail", value=papertrail, expected_type=type_hints["papertrail"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if datadog is not None:
            self._values["datadog"] = datadog
        if logtail is not None:
            self._values["logtail"] = logtail
        if papertrail is not None:
            self._values["papertrail"] = papertrail

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the log destination.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#name App#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def datadog(self) -> typing.Optional["AppSpecFunctionLogDestinationDatadog"]:
        '''datadog block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#datadog App#datadog}
        '''
        result = self._values.get("datadog")
        return typing.cast(typing.Optional["AppSpecFunctionLogDestinationDatadog"], result)

    @builtins.property
    def logtail(self) -> typing.Optional["AppSpecFunctionLogDestinationLogtail"]:
        '''logtail block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#logtail App#logtail}
        '''
        result = self._values.get("logtail")
        return typing.cast(typing.Optional["AppSpecFunctionLogDestinationLogtail"], result)

    @builtins.property
    def papertrail(self) -> typing.Optional["AppSpecFunctionLogDestinationPapertrail"]:
        '''papertrail block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#papertrail App#papertrail}
        '''
        result = self._values.get("papertrail")
        return typing.cast(typing.Optional["AppSpecFunctionLogDestinationPapertrail"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecFunctionLogDestination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecFunctionLogDestinationDatadog",
    jsii_struct_bases=[],
    name_mapping={"api_key": "apiKey", "endpoint": "endpoint"},
)
class AppSpecFunctionLogDestinationDatadog:
    def __init__(
        self,
        *,
        api_key: builtins.str,
        endpoint: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param api_key: Datadog API key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#api_key App#api_key}
        :param endpoint: Datadog HTTP log intake endpoint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#endpoint App#endpoint}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecFunctionLogDestinationDatadog.__init__)
            check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
        self._values: typing.Dict[str, typing.Any] = {
            "api_key": api_key,
        }
        if endpoint is not None:
            self._values["endpoint"] = endpoint

    @builtins.property
    def api_key(self) -> builtins.str:
        '''Datadog API key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#api_key App#api_key}
        '''
        result = self._values.get("api_key")
        assert result is not None, "Required property 'api_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoint(self) -> typing.Optional[builtins.str]:
        '''Datadog HTTP log intake endpoint.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#endpoint App#endpoint}
        '''
        result = self._values.get("endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecFunctionLogDestinationDatadog(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecFunctionLogDestinationDatadogOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecFunctionLogDestinationDatadogOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecFunctionLogDestinationDatadogOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEndpoint")
    def reset_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpoint", []))

    @builtins.property
    @jsii.member(jsii_name="apiKeyInput")
    def api_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="apiKey")
    def api_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiKey"))

    @api_key.setter
    def api_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionLogDestinationDatadogOutputReference, "api_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiKey", value)

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionLogDestinationDatadogOutputReference, "endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecFunctionLogDestinationDatadog]:
        return typing.cast(typing.Optional[AppSpecFunctionLogDestinationDatadog], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppSpecFunctionLogDestinationDatadog],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionLogDestinationDatadogOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecFunctionLogDestinationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecFunctionLogDestinationList",
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
            type_hints = typing.get_type_hints(AppSpecFunctionLogDestinationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AppSpecFunctionLogDestinationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecFunctionLogDestinationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppSpecFunctionLogDestinationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionLogDestinationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionLogDestinationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionLogDestinationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecFunctionLogDestination]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecFunctionLogDestination]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecFunctionLogDestination]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionLogDestinationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecFunctionLogDestinationLogtail",
    jsii_struct_bases=[],
    name_mapping={"token": "token"},
)
class AppSpecFunctionLogDestinationLogtail:
    def __init__(self, *, token: builtins.str) -> None:
        '''
        :param token: Logtail token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#token App#token}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecFunctionLogDestinationLogtail.__init__)
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
        self._values: typing.Dict[str, typing.Any] = {
            "token": token,
        }

    @builtins.property
    def token(self) -> builtins.str:
        '''Logtail token.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#token App#token}
        '''
        result = self._values.get("token")
        assert result is not None, "Required property 'token' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecFunctionLogDestinationLogtail(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecFunctionLogDestinationLogtailOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecFunctionLogDestinationLogtailOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecFunctionLogDestinationLogtailOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="tokenInput")
    def token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenInput"))

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "token"))

    @token.setter
    def token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionLogDestinationLogtailOutputReference, "token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "token", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecFunctionLogDestinationLogtail]:
        return typing.cast(typing.Optional[AppSpecFunctionLogDestinationLogtail], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppSpecFunctionLogDestinationLogtail],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionLogDestinationLogtailOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecFunctionLogDestinationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecFunctionLogDestinationOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecFunctionLogDestinationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDatadog")
    def put_datadog(
        self,
        *,
        api_key: builtins.str,
        endpoint: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param api_key: Datadog API key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#api_key App#api_key}
        :param endpoint: Datadog HTTP log intake endpoint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#endpoint App#endpoint}
        '''
        value = AppSpecFunctionLogDestinationDatadog(
            api_key=api_key, endpoint=endpoint
        )

        return typing.cast(None, jsii.invoke(self, "putDatadog", [value]))

    @jsii.member(jsii_name="putLogtail")
    def put_logtail(self, *, token: builtins.str) -> None:
        '''
        :param token: Logtail token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#token App#token}
        '''
        value = AppSpecFunctionLogDestinationLogtail(token=token)

        return typing.cast(None, jsii.invoke(self, "putLogtail", [value]))

    @jsii.member(jsii_name="putPapertrail")
    def put_papertrail(self, *, endpoint: builtins.str) -> None:
        '''
        :param endpoint: Papertrail syslog endpoint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#endpoint App#endpoint}
        '''
        value = AppSpecFunctionLogDestinationPapertrail(endpoint=endpoint)

        return typing.cast(None, jsii.invoke(self, "putPapertrail", [value]))

    @jsii.member(jsii_name="resetDatadog")
    def reset_datadog(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatadog", []))

    @jsii.member(jsii_name="resetLogtail")
    def reset_logtail(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogtail", []))

    @jsii.member(jsii_name="resetPapertrail")
    def reset_papertrail(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPapertrail", []))

    @builtins.property
    @jsii.member(jsii_name="datadog")
    def datadog(self) -> AppSpecFunctionLogDestinationDatadogOutputReference:
        return typing.cast(AppSpecFunctionLogDestinationDatadogOutputReference, jsii.get(self, "datadog"))

    @builtins.property
    @jsii.member(jsii_name="logtail")
    def logtail(self) -> AppSpecFunctionLogDestinationLogtailOutputReference:
        return typing.cast(AppSpecFunctionLogDestinationLogtailOutputReference, jsii.get(self, "logtail"))

    @builtins.property
    @jsii.member(jsii_name="papertrail")
    def papertrail(self) -> "AppSpecFunctionLogDestinationPapertrailOutputReference":
        return typing.cast("AppSpecFunctionLogDestinationPapertrailOutputReference", jsii.get(self, "papertrail"))

    @builtins.property
    @jsii.member(jsii_name="datadogInput")
    def datadog_input(self) -> typing.Optional[AppSpecFunctionLogDestinationDatadog]:
        return typing.cast(typing.Optional[AppSpecFunctionLogDestinationDatadog], jsii.get(self, "datadogInput"))

    @builtins.property
    @jsii.member(jsii_name="logtailInput")
    def logtail_input(self) -> typing.Optional[AppSpecFunctionLogDestinationLogtail]:
        return typing.cast(typing.Optional[AppSpecFunctionLogDestinationLogtail], jsii.get(self, "logtailInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="papertrailInput")
    def papertrail_input(
        self,
    ) -> typing.Optional["AppSpecFunctionLogDestinationPapertrail"]:
        return typing.cast(typing.Optional["AppSpecFunctionLogDestinationPapertrail"], jsii.get(self, "papertrailInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionLogDestinationOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppSpecFunctionLogDestination, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppSpecFunctionLogDestination, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppSpecFunctionLogDestination, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionLogDestinationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecFunctionLogDestinationPapertrail",
    jsii_struct_bases=[],
    name_mapping={"endpoint": "endpoint"},
)
class AppSpecFunctionLogDestinationPapertrail:
    def __init__(self, *, endpoint: builtins.str) -> None:
        '''
        :param endpoint: Papertrail syslog endpoint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#endpoint App#endpoint}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecFunctionLogDestinationPapertrail.__init__)
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
        self._values: typing.Dict[str, typing.Any] = {
            "endpoint": endpoint,
        }

    @builtins.property
    def endpoint(self) -> builtins.str:
        '''Papertrail syslog endpoint.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#endpoint App#endpoint}
        '''
        result = self._values.get("endpoint")
        assert result is not None, "Required property 'endpoint' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecFunctionLogDestinationPapertrail(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecFunctionLogDestinationPapertrailOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecFunctionLogDestinationPapertrailOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecFunctionLogDestinationPapertrailOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionLogDestinationPapertrailOutputReference, "endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[AppSpecFunctionLogDestinationPapertrail]:
        return typing.cast(typing.Optional[AppSpecFunctionLogDestinationPapertrail], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppSpecFunctionLogDestinationPapertrail],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionLogDestinationPapertrailOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecFunctionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecFunctionOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecFunctionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAlert")
    def put_alert(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppSpecFunctionAlert, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecFunctionOutputReference.put_alert)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAlert", [value]))

    @jsii.member(jsii_name="putCors")
    def put_cors(
        self,
        *,
        allow_credentials: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_methods: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_origins: typing.Optional[typing.Union[AppSpecFunctionCorsAllowOrigins, typing.Dict[str, typing.Any]]] = None,
        expose_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        max_age: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allow_credentials: Whether browsers should expose the response to the client-side JavaScript code when the request’s credentials mode is ``include``. This configures the Access-Control-Allow-Credentials header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_credentials App#allow_credentials}
        :param allow_headers: The set of allowed HTTP request headers. This configures the Access-Control-Allow-Headers header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_headers App#allow_headers}
        :param allow_methods: The set of allowed HTTP methods. This configures the Access-Control-Allow-Methods header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_methods App#allow_methods}
        :param allow_origins: allow_origins block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_origins App#allow_origins}
        :param expose_headers: The set of HTTP response headers that browsers are allowed to access. This configures the Access-Control-Expose-Headers header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#expose_headers App#expose_headers}
        :param max_age: An optional duration specifying how long browsers can cache the results of a preflight request. This configures the Access-Control-Max-Age header. Example: ``5h30m``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#max_age App#max_age}
        '''
        value = AppSpecFunctionCors(
            allow_credentials=allow_credentials,
            allow_headers=allow_headers,
            allow_methods=allow_methods,
            allow_origins=allow_origins,
            expose_headers=expose_headers,
            max_age=max_age,
        )

        return typing.cast(None, jsii.invoke(self, "putCors", [value]))

    @jsii.member(jsii_name="putEnv")
    def put_env(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppSpecFunctionEnv, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecFunctionOutputReference.put_env)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEnv", [value]))

    @jsii.member(jsii_name="putGit")
    def put_git(
        self,
        *,
        branch: typing.Optional[builtins.str] = None,
        repo_clone_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: The name of the branch to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        :param repo_clone_url: The clone URL of the repo. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo_clone_url App#repo_clone_url}
        '''
        value = AppSpecFunctionGit(branch=branch, repo_clone_url=repo_clone_url)

        return typing.cast(None, jsii.invoke(self, "putGit", [value]))

    @jsii.member(jsii_name="putGithub")
    def put_github(
        self,
        *,
        branch: typing.Optional[builtins.str] = None,
        deploy_on_push: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: The name of the branch to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        :param deploy_on_push: Whether to automatically deploy new commits made to the repo. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        :param repo: The name of the repo in the format ``owner/repo``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo App#repo}
        '''
        value = AppSpecFunctionGithub(
            branch=branch, deploy_on_push=deploy_on_push, repo=repo
        )

        return typing.cast(None, jsii.invoke(self, "putGithub", [value]))

    @jsii.member(jsii_name="putGitlab")
    def put_gitlab(
        self,
        *,
        branch: typing.Optional[builtins.str] = None,
        deploy_on_push: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: The name of the branch to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        :param deploy_on_push: Whether to automatically deploy new commits made to the repo. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        :param repo: The name of the repo in the format ``owner/repo``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo App#repo}
        '''
        value = AppSpecFunctionGitlab(
            branch=branch, deploy_on_push=deploy_on_push, repo=repo
        )

        return typing.cast(None, jsii.invoke(self, "putGitlab", [value]))

    @jsii.member(jsii_name="putLogDestination")
    def put_log_destination(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppSpecFunctionLogDestination, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecFunctionOutputReference.put_log_destination)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLogDestination", [value]))

    @jsii.member(jsii_name="putRoutes")
    def put_routes(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecFunctionRoutes", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecFunctionOutputReference.put_routes)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRoutes", [value]))

    @jsii.member(jsii_name="resetAlert")
    def reset_alert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlert", []))

    @jsii.member(jsii_name="resetCors")
    def reset_cors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCors", []))

    @jsii.member(jsii_name="resetEnv")
    def reset_env(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnv", []))

    @jsii.member(jsii_name="resetGit")
    def reset_git(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGit", []))

    @jsii.member(jsii_name="resetGithub")
    def reset_github(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGithub", []))

    @jsii.member(jsii_name="resetGitlab")
    def reset_gitlab(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGitlab", []))

    @jsii.member(jsii_name="resetLogDestination")
    def reset_log_destination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogDestination", []))

    @jsii.member(jsii_name="resetRoutes")
    def reset_routes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoutes", []))

    @jsii.member(jsii_name="resetSourceDir")
    def reset_source_dir(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceDir", []))

    @builtins.property
    @jsii.member(jsii_name="alert")
    def alert(self) -> AppSpecFunctionAlertList:
        return typing.cast(AppSpecFunctionAlertList, jsii.get(self, "alert"))

    @builtins.property
    @jsii.member(jsii_name="cors")
    def cors(self) -> AppSpecFunctionCorsOutputReference:
        return typing.cast(AppSpecFunctionCorsOutputReference, jsii.get(self, "cors"))

    @builtins.property
    @jsii.member(jsii_name="env")
    def env(self) -> AppSpecFunctionEnvList:
        return typing.cast(AppSpecFunctionEnvList, jsii.get(self, "env"))

    @builtins.property
    @jsii.member(jsii_name="git")
    def git(self) -> AppSpecFunctionGitOutputReference:
        return typing.cast(AppSpecFunctionGitOutputReference, jsii.get(self, "git"))

    @builtins.property
    @jsii.member(jsii_name="github")
    def github(self) -> AppSpecFunctionGithubOutputReference:
        return typing.cast(AppSpecFunctionGithubOutputReference, jsii.get(self, "github"))

    @builtins.property
    @jsii.member(jsii_name="gitlab")
    def gitlab(self) -> AppSpecFunctionGitlabOutputReference:
        return typing.cast(AppSpecFunctionGitlabOutputReference, jsii.get(self, "gitlab"))

    @builtins.property
    @jsii.member(jsii_name="logDestination")
    def log_destination(self) -> AppSpecFunctionLogDestinationList:
        return typing.cast(AppSpecFunctionLogDestinationList, jsii.get(self, "logDestination"))

    @builtins.property
    @jsii.member(jsii_name="routes")
    def routes(self) -> "AppSpecFunctionRoutesList":
        return typing.cast("AppSpecFunctionRoutesList", jsii.get(self, "routes"))

    @builtins.property
    @jsii.member(jsii_name="alertInput")
    def alert_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecFunctionAlert]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecFunctionAlert]]], jsii.get(self, "alertInput"))

    @builtins.property
    @jsii.member(jsii_name="corsInput")
    def cors_input(self) -> typing.Optional[AppSpecFunctionCors]:
        return typing.cast(typing.Optional[AppSpecFunctionCors], jsii.get(self, "corsInput"))

    @builtins.property
    @jsii.member(jsii_name="envInput")
    def env_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecFunctionEnv]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecFunctionEnv]]], jsii.get(self, "envInput"))

    @builtins.property
    @jsii.member(jsii_name="githubInput")
    def github_input(self) -> typing.Optional[AppSpecFunctionGithub]:
        return typing.cast(typing.Optional[AppSpecFunctionGithub], jsii.get(self, "githubInput"))

    @builtins.property
    @jsii.member(jsii_name="gitInput")
    def git_input(self) -> typing.Optional[AppSpecFunctionGit]:
        return typing.cast(typing.Optional[AppSpecFunctionGit], jsii.get(self, "gitInput"))

    @builtins.property
    @jsii.member(jsii_name="gitlabInput")
    def gitlab_input(self) -> typing.Optional[AppSpecFunctionGitlab]:
        return typing.cast(typing.Optional[AppSpecFunctionGitlab], jsii.get(self, "gitlabInput"))

    @builtins.property
    @jsii.member(jsii_name="logDestinationInput")
    def log_destination_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecFunctionLogDestination]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecFunctionLogDestination]]], jsii.get(self, "logDestinationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="routesInput")
    def routes_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecFunctionRoutes"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecFunctionRoutes"]]], jsii.get(self, "routesInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceDirInput")
    def source_dir_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceDirInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="sourceDir")
    def source_dir(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceDir"))

    @source_dir.setter
    def source_dir(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionOutputReference, "source_dir").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceDir", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppSpecFunction, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppSpecFunction, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppSpecFunction, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecFunctionRoutes",
    jsii_struct_bases=[],
    name_mapping={"path": "path", "preserve_path_prefix": "preservePathPrefix"},
)
class AppSpecFunctionRoutes:
    def __init__(
        self,
        *,
        path: typing.Optional[builtins.str] = None,
        preserve_path_prefix: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param path: Path specifies an route by HTTP path prefix. Paths must start with / and must be unique within the app. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#path App#path}
        :param preserve_path_prefix: An optional flag to preserve the path that is forwarded to the backend service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#preserve_path_prefix App#preserve_path_prefix}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecFunctionRoutes.__init__)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument preserve_path_prefix", value=preserve_path_prefix, expected_type=type_hints["preserve_path_prefix"])
        self._values: typing.Dict[str, typing.Any] = {}
        if path is not None:
            self._values["path"] = path
        if preserve_path_prefix is not None:
            self._values["preserve_path_prefix"] = preserve_path_prefix

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Path specifies an route by HTTP path prefix.

        Paths must start with / and must be unique within the app.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#path App#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preserve_path_prefix(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''An optional flag to preserve the path that is forwarded to the backend service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#preserve_path_prefix App#preserve_path_prefix}
        '''
        result = self._values.get("preserve_path_prefix")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecFunctionRoutes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecFunctionRoutesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecFunctionRoutesList",
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
            type_hints = typing.get_type_hints(AppSpecFunctionRoutesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AppSpecFunctionRoutesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecFunctionRoutesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppSpecFunctionRoutesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionRoutesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionRoutesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionRoutesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecFunctionRoutes]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecFunctionRoutes]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecFunctionRoutes]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionRoutesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecFunctionRoutesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecFunctionRoutesOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecFunctionRoutesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetPreservePathPrefix")
    def reset_preserve_path_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreservePathPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="preservePathPrefixInput")
    def preserve_path_prefix_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "preservePathPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionRoutesOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="preservePathPrefix")
    def preserve_path_prefix(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "preservePathPrefix"))

    @preserve_path_prefix.setter
    def preserve_path_prefix(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionRoutesOutputReference, "preserve_path_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preservePathPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppSpecFunctionRoutes, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppSpecFunctionRoutes, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppSpecFunctionRoutes, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecFunctionRoutesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecJob",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "alert": "alert",
        "build_command": "buildCommand",
        "dockerfile_path": "dockerfilePath",
        "env": "env",
        "environment_slug": "environmentSlug",
        "git": "git",
        "github": "github",
        "gitlab": "gitlab",
        "image": "image",
        "instance_count": "instanceCount",
        "instance_size_slug": "instanceSizeSlug",
        "kind": "kind",
        "log_destination": "logDestination",
        "run_command": "runCommand",
        "source_dir": "sourceDir",
    },
)
class AppSpecJob:
    def __init__(
        self,
        *,
        name: builtins.str,
        alert: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecJobAlert", typing.Dict[str, typing.Any]]]]] = None,
        build_command: typing.Optional[builtins.str] = None,
        dockerfile_path: typing.Optional[builtins.str] = None,
        env: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecJobEnv", typing.Dict[str, typing.Any]]]]] = None,
        environment_slug: typing.Optional[builtins.str] = None,
        git: typing.Optional[typing.Union["AppSpecJobGit", typing.Dict[str, typing.Any]]] = None,
        github: typing.Optional[typing.Union["AppSpecJobGithub", typing.Dict[str, typing.Any]]] = None,
        gitlab: typing.Optional[typing.Union["AppSpecJobGitlab", typing.Dict[str, typing.Any]]] = None,
        image: typing.Optional[typing.Union["AppSpecJobImage", typing.Dict[str, typing.Any]]] = None,
        instance_count: typing.Optional[jsii.Number] = None,
        instance_size_slug: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
        log_destination: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecJobLogDestination", typing.Dict[str, typing.Any]]]]] = None,
        run_command: typing.Optional[builtins.str] = None,
        source_dir: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: The name of the component. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#name App#name}
        :param alert: alert block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#alert App#alert}
        :param build_command: An optional build command to run while building this component from source. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#build_command App#build_command}
        :param dockerfile_path: The path to a Dockerfile relative to the root of the repo. If set, overrides usage of buildpacks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#dockerfile_path App#dockerfile_path}
        :param env: env block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#env App#env}
        :param environment_slug: An environment slug describing the type of this app. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#environment_slug App#environment_slug}
        :param git: git block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#git App#git}
        :param github: github block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#github App#github}
        :param gitlab: gitlab block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#gitlab App#gitlab}
        :param image: image block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#image App#image}
        :param instance_count: The amount of instances that this component should be scaled to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#instance_count App#instance_count}
        :param instance_size_slug: The instance size to use for this component. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#instance_size_slug App#instance_size_slug}
        :param kind: The type of job and when it will be run during the deployment process. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#kind App#kind}
        :param log_destination: log_destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#log_destination App#log_destination}
        :param run_command: An optional run command to override the component's default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#run_command App#run_command}
        :param source_dir: An optional path to the working directory to use for the build. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#source_dir App#source_dir}
        '''
        if isinstance(git, dict):
            git = AppSpecJobGit(**git)
        if isinstance(github, dict):
            github = AppSpecJobGithub(**github)
        if isinstance(gitlab, dict):
            gitlab = AppSpecJobGitlab(**gitlab)
        if isinstance(image, dict):
            image = AppSpecJobImage(**image)
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecJob.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument alert", value=alert, expected_type=type_hints["alert"])
            check_type(argname="argument build_command", value=build_command, expected_type=type_hints["build_command"])
            check_type(argname="argument dockerfile_path", value=dockerfile_path, expected_type=type_hints["dockerfile_path"])
            check_type(argname="argument env", value=env, expected_type=type_hints["env"])
            check_type(argname="argument environment_slug", value=environment_slug, expected_type=type_hints["environment_slug"])
            check_type(argname="argument git", value=git, expected_type=type_hints["git"])
            check_type(argname="argument github", value=github, expected_type=type_hints["github"])
            check_type(argname="argument gitlab", value=gitlab, expected_type=type_hints["gitlab"])
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument instance_count", value=instance_count, expected_type=type_hints["instance_count"])
            check_type(argname="argument instance_size_slug", value=instance_size_slug, expected_type=type_hints["instance_size_slug"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument log_destination", value=log_destination, expected_type=type_hints["log_destination"])
            check_type(argname="argument run_command", value=run_command, expected_type=type_hints["run_command"])
            check_type(argname="argument source_dir", value=source_dir, expected_type=type_hints["source_dir"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if alert is not None:
            self._values["alert"] = alert
        if build_command is not None:
            self._values["build_command"] = build_command
        if dockerfile_path is not None:
            self._values["dockerfile_path"] = dockerfile_path
        if env is not None:
            self._values["env"] = env
        if environment_slug is not None:
            self._values["environment_slug"] = environment_slug
        if git is not None:
            self._values["git"] = git
        if github is not None:
            self._values["github"] = github
        if gitlab is not None:
            self._values["gitlab"] = gitlab
        if image is not None:
            self._values["image"] = image
        if instance_count is not None:
            self._values["instance_count"] = instance_count
        if instance_size_slug is not None:
            self._values["instance_size_slug"] = instance_size_slug
        if kind is not None:
            self._values["kind"] = kind
        if log_destination is not None:
            self._values["log_destination"] = log_destination
        if run_command is not None:
            self._values["run_command"] = run_command
        if source_dir is not None:
            self._values["source_dir"] = source_dir

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the component.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#name App#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alert(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecJobAlert"]]]:
        '''alert block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#alert App#alert}
        '''
        result = self._values.get("alert")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecJobAlert"]]], result)

    @builtins.property
    def build_command(self) -> typing.Optional[builtins.str]:
        '''An optional build command to run while building this component from source.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#build_command App#build_command}
        '''
        result = self._values.get("build_command")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dockerfile_path(self) -> typing.Optional[builtins.str]:
        '''The path to a Dockerfile relative to the root of the repo. If set, overrides usage of buildpacks.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#dockerfile_path App#dockerfile_path}
        '''
        result = self._values.get("dockerfile_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def env(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecJobEnv"]]]:
        '''env block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#env App#env}
        '''
        result = self._values.get("env")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecJobEnv"]]], result)

    @builtins.property
    def environment_slug(self) -> typing.Optional[builtins.str]:
        '''An environment slug describing the type of this app.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#environment_slug App#environment_slug}
        '''
        result = self._values.get("environment_slug")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def git(self) -> typing.Optional["AppSpecJobGit"]:
        '''git block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#git App#git}
        '''
        result = self._values.get("git")
        return typing.cast(typing.Optional["AppSpecJobGit"], result)

    @builtins.property
    def github(self) -> typing.Optional["AppSpecJobGithub"]:
        '''github block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#github App#github}
        '''
        result = self._values.get("github")
        return typing.cast(typing.Optional["AppSpecJobGithub"], result)

    @builtins.property
    def gitlab(self) -> typing.Optional["AppSpecJobGitlab"]:
        '''gitlab block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#gitlab App#gitlab}
        '''
        result = self._values.get("gitlab")
        return typing.cast(typing.Optional["AppSpecJobGitlab"], result)

    @builtins.property
    def image(self) -> typing.Optional["AppSpecJobImage"]:
        '''image block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#image App#image}
        '''
        result = self._values.get("image")
        return typing.cast(typing.Optional["AppSpecJobImage"], result)

    @builtins.property
    def instance_count(self) -> typing.Optional[jsii.Number]:
        '''The amount of instances that this component should be scaled to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#instance_count App#instance_count}
        '''
        result = self._values.get("instance_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def instance_size_slug(self) -> typing.Optional[builtins.str]:
        '''The instance size to use for this component.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#instance_size_slug App#instance_size_slug}
        '''
        result = self._values.get("instance_size_slug")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional[builtins.str]:
        '''The type of job and when it will be run during the deployment process.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#kind App#kind}
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_destination(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecJobLogDestination"]]]:
        '''log_destination block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#log_destination App#log_destination}
        '''
        result = self._values.get("log_destination")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecJobLogDestination"]]], result)

    @builtins.property
    def run_command(self) -> typing.Optional[builtins.str]:
        '''An optional run command to override the component's default.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#run_command App#run_command}
        '''
        result = self._values.get("run_command")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_dir(self) -> typing.Optional[builtins.str]:
        '''An optional path to the working directory to use for the build.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#source_dir App#source_dir}
        '''
        result = self._values.get("source_dir")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecJob(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecJobAlert",
    jsii_struct_bases=[],
    name_mapping={
        "operator": "operator",
        "rule": "rule",
        "value": "value",
        "window": "window",
        "disabled": "disabled",
    },
)
class AppSpecJobAlert:
    def __init__(
        self,
        *,
        operator: builtins.str,
        rule: builtins.str,
        value: jsii.Number,
        window: builtins.str,
        disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#operator App#operator}.
        :param rule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#rule App#rule}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#value App#value}.
        :param window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#window App#window}.
        :param disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#disabled App#disabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecJobAlert.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument window", value=window, expected_type=type_hints["window"])
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
            "rule": rule,
            "value": value,
            "window": window,
        }
        if disabled is not None:
            self._values["disabled"] = disabled

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#operator App#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#rule App#rule}.'''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#value App#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def window(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#window App#window}.'''
        result = self._values.get("window")
        assert result is not None, "Required property 'window' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#disabled App#disabled}.'''
        result = self._values.get("disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecJobAlert(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecJobAlertList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecJobAlertList",
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
            type_hints = typing.get_type_hints(AppSpecJobAlertList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AppSpecJobAlertOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecJobAlertList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppSpecJobAlertOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobAlertList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecJobAlertList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecJobAlertList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecJobAlert]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecJobAlert]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecJobAlert]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobAlertList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecJobAlertOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecJobAlertOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecJobAlertOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDisabled")
    def reset_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisabled", []))

    @builtins.property
    @jsii.member(jsii_name="disabledInput")
    def disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disabledInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="windowInput")
    def window_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "windowInput"))

    @builtins.property
    @jsii.member(jsii_name="disabled")
    def disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disabled"))

    @disabled.setter
    def disabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobAlertOutputReference, "disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobAlertOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rule"))

    @rule.setter
    def rule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobAlertOutputReference, "rule").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobAlertOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="window")
    def window(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "window"))

    @window.setter
    def window(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobAlertOutputReference, "window").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "window", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppSpecJobAlert, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppSpecJobAlert, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppSpecJobAlert, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobAlertOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecJobEnv",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "scope": "scope", "type": "type", "value": "value"},
)
class AppSpecJobEnv:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        scope: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: The name of the environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#key App#key}
        :param scope: The visibility scope of the environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#scope App#scope}
        :param type: The type of the environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#type App#type}
        :param value: The value of the environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#value App#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecJobEnv.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if scope is not None:
            self._values["scope"] = scope
        if type is not None:
            self._values["type"] = type
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The name of the environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#key App#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scope(self) -> typing.Optional[builtins.str]:
        '''The visibility scope of the environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#scope App#scope}
        '''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of the environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#type App#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''The value of the environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#value App#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecJobEnv(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecJobEnvList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecJobEnvList",
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
            type_hints = typing.get_type_hints(AppSpecJobEnvList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AppSpecJobEnvOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecJobEnvList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppSpecJobEnvOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobEnvList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecJobEnvList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecJobEnvList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecJobEnv]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecJobEnv]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecJobEnv]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobEnvList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecJobEnvOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecJobEnvOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecJobEnvOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetScope")
    def reset_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScope", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="scopeInput")
    def scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scopeInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobEnvOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobEnvOutputReference, "scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobEnvOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobEnvOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppSpecJobEnv, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppSpecJobEnv, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppSpecJobEnv, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobEnvOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecJobGit",
    jsii_struct_bases=[],
    name_mapping={"branch": "branch", "repo_clone_url": "repoCloneUrl"},
)
class AppSpecJobGit:
    def __init__(
        self,
        *,
        branch: typing.Optional[builtins.str] = None,
        repo_clone_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: The name of the branch to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        :param repo_clone_url: The clone URL of the repo. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo_clone_url App#repo_clone_url}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecJobGit.__init__)
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
            check_type(argname="argument repo_clone_url", value=repo_clone_url, expected_type=type_hints["repo_clone_url"])
        self._values: typing.Dict[str, typing.Any] = {}
        if branch is not None:
            self._values["branch"] = branch
        if repo_clone_url is not None:
            self._values["repo_clone_url"] = repo_clone_url

    @builtins.property
    def branch(self) -> typing.Optional[builtins.str]:
        '''The name of the branch to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        '''
        result = self._values.get("branch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def repo_clone_url(self) -> typing.Optional[builtins.str]:
        '''The clone URL of the repo.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo_clone_url App#repo_clone_url}
        '''
        result = self._values.get("repo_clone_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecJobGit(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecJobGitOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecJobGitOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecJobGitOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBranch")
    def reset_branch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBranch", []))

    @jsii.member(jsii_name="resetRepoCloneUrl")
    def reset_repo_clone_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepoCloneUrl", []))

    @builtins.property
    @jsii.member(jsii_name="branchInput")
    def branch_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "branchInput"))

    @builtins.property
    @jsii.member(jsii_name="repoCloneUrlInput")
    def repo_clone_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repoCloneUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="branch")
    def branch(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "branch"))

    @branch.setter
    def branch(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobGitOutputReference, "branch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "branch", value)

    @builtins.property
    @jsii.member(jsii_name="repoCloneUrl")
    def repo_clone_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repoCloneUrl"))

    @repo_clone_url.setter
    def repo_clone_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobGitOutputReference, "repo_clone_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repoCloneUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecJobGit]:
        return typing.cast(typing.Optional[AppSpecJobGit], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppSpecJobGit]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobGitOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecJobGithub",
    jsii_struct_bases=[],
    name_mapping={
        "branch": "branch",
        "deploy_on_push": "deployOnPush",
        "repo": "repo",
    },
)
class AppSpecJobGithub:
    def __init__(
        self,
        *,
        branch: typing.Optional[builtins.str] = None,
        deploy_on_push: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: The name of the branch to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        :param deploy_on_push: Whether to automatically deploy new commits made to the repo. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        :param repo: The name of the repo in the format ``owner/repo``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo App#repo}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecJobGithub.__init__)
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
            check_type(argname="argument deploy_on_push", value=deploy_on_push, expected_type=type_hints["deploy_on_push"])
            check_type(argname="argument repo", value=repo, expected_type=type_hints["repo"])
        self._values: typing.Dict[str, typing.Any] = {}
        if branch is not None:
            self._values["branch"] = branch
        if deploy_on_push is not None:
            self._values["deploy_on_push"] = deploy_on_push
        if repo is not None:
            self._values["repo"] = repo

    @builtins.property
    def branch(self) -> typing.Optional[builtins.str]:
        '''The name of the branch to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        '''
        result = self._values.get("branch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deploy_on_push(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to automatically deploy new commits made to the repo.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        '''
        result = self._values.get("deploy_on_push")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def repo(self) -> typing.Optional[builtins.str]:
        '''The name of the repo in the format ``owner/repo``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo App#repo}
        '''
        result = self._values.get("repo")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecJobGithub(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecJobGithubOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecJobGithubOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecJobGithubOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBranch")
    def reset_branch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBranch", []))

    @jsii.member(jsii_name="resetDeployOnPush")
    def reset_deploy_on_push(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeployOnPush", []))

    @jsii.member(jsii_name="resetRepo")
    def reset_repo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepo", []))

    @builtins.property
    @jsii.member(jsii_name="branchInput")
    def branch_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "branchInput"))

    @builtins.property
    @jsii.member(jsii_name="deployOnPushInput")
    def deploy_on_push_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deployOnPushInput"))

    @builtins.property
    @jsii.member(jsii_name="repoInput")
    def repo_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repoInput"))

    @builtins.property
    @jsii.member(jsii_name="branch")
    def branch(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "branch"))

    @branch.setter
    def branch(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobGithubOutputReference, "branch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "branch", value)

    @builtins.property
    @jsii.member(jsii_name="deployOnPush")
    def deploy_on_push(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "deployOnPush"))

    @deploy_on_push.setter
    def deploy_on_push(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobGithubOutputReference, "deploy_on_push").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deployOnPush", value)

    @builtins.property
    @jsii.member(jsii_name="repo")
    def repo(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repo"))

    @repo.setter
    def repo(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobGithubOutputReference, "repo").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repo", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecJobGithub]:
        return typing.cast(typing.Optional[AppSpecJobGithub], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppSpecJobGithub]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobGithubOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecJobGitlab",
    jsii_struct_bases=[],
    name_mapping={
        "branch": "branch",
        "deploy_on_push": "deployOnPush",
        "repo": "repo",
    },
)
class AppSpecJobGitlab:
    def __init__(
        self,
        *,
        branch: typing.Optional[builtins.str] = None,
        deploy_on_push: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: The name of the branch to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        :param deploy_on_push: Whether to automatically deploy new commits made to the repo. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        :param repo: The name of the repo in the format ``owner/repo``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo App#repo}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecJobGitlab.__init__)
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
            check_type(argname="argument deploy_on_push", value=deploy_on_push, expected_type=type_hints["deploy_on_push"])
            check_type(argname="argument repo", value=repo, expected_type=type_hints["repo"])
        self._values: typing.Dict[str, typing.Any] = {}
        if branch is not None:
            self._values["branch"] = branch
        if deploy_on_push is not None:
            self._values["deploy_on_push"] = deploy_on_push
        if repo is not None:
            self._values["repo"] = repo

    @builtins.property
    def branch(self) -> typing.Optional[builtins.str]:
        '''The name of the branch to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        '''
        result = self._values.get("branch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deploy_on_push(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to automatically deploy new commits made to the repo.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        '''
        result = self._values.get("deploy_on_push")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def repo(self) -> typing.Optional[builtins.str]:
        '''The name of the repo in the format ``owner/repo``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo App#repo}
        '''
        result = self._values.get("repo")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecJobGitlab(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecJobGitlabOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecJobGitlabOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecJobGitlabOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBranch")
    def reset_branch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBranch", []))

    @jsii.member(jsii_name="resetDeployOnPush")
    def reset_deploy_on_push(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeployOnPush", []))

    @jsii.member(jsii_name="resetRepo")
    def reset_repo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepo", []))

    @builtins.property
    @jsii.member(jsii_name="branchInput")
    def branch_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "branchInput"))

    @builtins.property
    @jsii.member(jsii_name="deployOnPushInput")
    def deploy_on_push_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deployOnPushInput"))

    @builtins.property
    @jsii.member(jsii_name="repoInput")
    def repo_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repoInput"))

    @builtins.property
    @jsii.member(jsii_name="branch")
    def branch(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "branch"))

    @branch.setter
    def branch(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobGitlabOutputReference, "branch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "branch", value)

    @builtins.property
    @jsii.member(jsii_name="deployOnPush")
    def deploy_on_push(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "deployOnPush"))

    @deploy_on_push.setter
    def deploy_on_push(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobGitlabOutputReference, "deploy_on_push").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deployOnPush", value)

    @builtins.property
    @jsii.member(jsii_name="repo")
    def repo(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repo"))

    @repo.setter
    def repo(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobGitlabOutputReference, "repo").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repo", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecJobGitlab]:
        return typing.cast(typing.Optional[AppSpecJobGitlab], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppSpecJobGitlab]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobGitlabOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecJobImage",
    jsii_struct_bases=[],
    name_mapping={
        "registry_type": "registryType",
        "repository": "repository",
        "deploy_on_push": "deployOnPush",
        "registry": "registry",
        "tag": "tag",
    },
)
class AppSpecJobImage:
    def __init__(
        self,
        *,
        registry_type: builtins.str,
        repository: builtins.str,
        deploy_on_push: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecJobImageDeployOnPush", typing.Dict[str, typing.Any]]]]] = None,
        registry: typing.Optional[builtins.str] = None,
        tag: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param registry_type: The registry type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#registry_type App#registry_type}
        :param repository: The repository name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repository App#repository}
        :param deploy_on_push: deploy_on_push block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        :param registry: The registry name. Must be left empty for the DOCR registry type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#registry App#registry}
        :param tag: The repository tag. Defaults to latest if not provided. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#tag App#tag}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecJobImage.__init__)
            check_type(argname="argument registry_type", value=registry_type, expected_type=type_hints["registry_type"])
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
            check_type(argname="argument deploy_on_push", value=deploy_on_push, expected_type=type_hints["deploy_on_push"])
            check_type(argname="argument registry", value=registry, expected_type=type_hints["registry"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
        self._values: typing.Dict[str, typing.Any] = {
            "registry_type": registry_type,
            "repository": repository,
        }
        if deploy_on_push is not None:
            self._values["deploy_on_push"] = deploy_on_push
        if registry is not None:
            self._values["registry"] = registry
        if tag is not None:
            self._values["tag"] = tag

    @builtins.property
    def registry_type(self) -> builtins.str:
        '''The registry type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#registry_type App#registry_type}
        '''
        result = self._values.get("registry_type")
        assert result is not None, "Required property 'registry_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repository(self) -> builtins.str:
        '''The repository name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repository App#repository}
        '''
        result = self._values.get("repository")
        assert result is not None, "Required property 'repository' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def deploy_on_push(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecJobImageDeployOnPush"]]]:
        '''deploy_on_push block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        '''
        result = self._values.get("deploy_on_push")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecJobImageDeployOnPush"]]], result)

    @builtins.property
    def registry(self) -> typing.Optional[builtins.str]:
        '''The registry name. Must be left empty for the DOCR registry type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#registry App#registry}
        '''
        result = self._values.get("registry")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag(self) -> typing.Optional[builtins.str]:
        '''The repository tag. Defaults to latest if not provided.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#tag App#tag}
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecJobImage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecJobImageDeployOnPush",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class AppSpecJobImageDeployOnPush:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Whether to automatically deploy images pushed to DOCR. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#enabled App#enabled}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecJobImageDeployOnPush.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to automatically deploy images pushed to DOCR.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#enabled App#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecJobImageDeployOnPush(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecJobImageDeployOnPushList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecJobImageDeployOnPushList",
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
            type_hints = typing.get_type_hints(AppSpecJobImageDeployOnPushList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AppSpecJobImageDeployOnPushOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecJobImageDeployOnPushList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppSpecJobImageDeployOnPushOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobImageDeployOnPushList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecJobImageDeployOnPushList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecJobImageDeployOnPushList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecJobImageDeployOnPush]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecJobImageDeployOnPush]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecJobImageDeployOnPush]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobImageDeployOnPushList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecJobImageDeployOnPushOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecJobImageDeployOnPushOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecJobImageDeployOnPushOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobImageDeployOnPushOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppSpecJobImageDeployOnPush, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppSpecJobImageDeployOnPush, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppSpecJobImageDeployOnPush, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobImageDeployOnPushOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecJobImageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecJobImageOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecJobImageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDeployOnPush")
    def put_deploy_on_push(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppSpecJobImageDeployOnPush, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecJobImageOutputReference.put_deploy_on_push)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDeployOnPush", [value]))

    @jsii.member(jsii_name="resetDeployOnPush")
    def reset_deploy_on_push(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeployOnPush", []))

    @jsii.member(jsii_name="resetRegistry")
    def reset_registry(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegistry", []))

    @jsii.member(jsii_name="resetTag")
    def reset_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTag", []))

    @builtins.property
    @jsii.member(jsii_name="deployOnPush")
    def deploy_on_push(self) -> AppSpecJobImageDeployOnPushList:
        return typing.cast(AppSpecJobImageDeployOnPushList, jsii.get(self, "deployOnPush"))

    @builtins.property
    @jsii.member(jsii_name="deployOnPushInput")
    def deploy_on_push_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecJobImageDeployOnPush]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecJobImageDeployOnPush]]], jsii.get(self, "deployOnPushInput"))

    @builtins.property
    @jsii.member(jsii_name="registryInput")
    def registry_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "registryInput"))

    @builtins.property
    @jsii.member(jsii_name="registryTypeInput")
    def registry_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "registryTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="repositoryInput")
    def repository_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repositoryInput"))

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="registry")
    def registry(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registry"))

    @registry.setter
    def registry(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobImageOutputReference, "registry").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registry", value)

    @builtins.property
    @jsii.member(jsii_name="registryType")
    def registry_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registryType"))

    @registry_type.setter
    def registry_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobImageOutputReference, "registry_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registryType", value)

    @builtins.property
    @jsii.member(jsii_name="repository")
    def repository(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repository"))

    @repository.setter
    def repository(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobImageOutputReference, "repository").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repository", value)

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tag"))

    @tag.setter
    def tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobImageOutputReference, "tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tag", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecJobImage]:
        return typing.cast(typing.Optional[AppSpecJobImage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppSpecJobImage]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobImageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecJobList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecJobList",
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
            type_hints = typing.get_type_hints(AppSpecJobList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AppSpecJobOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecJobList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppSpecJobOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecJobList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecJobList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecJob]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecJob]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecJob]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecJobLogDestination",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "datadog": "datadog",
        "logtail": "logtail",
        "papertrail": "papertrail",
    },
)
class AppSpecJobLogDestination:
    def __init__(
        self,
        *,
        name: builtins.str,
        datadog: typing.Optional[typing.Union["AppSpecJobLogDestinationDatadog", typing.Dict[str, typing.Any]]] = None,
        logtail: typing.Optional[typing.Union["AppSpecJobLogDestinationLogtail", typing.Dict[str, typing.Any]]] = None,
        papertrail: typing.Optional[typing.Union["AppSpecJobLogDestinationPapertrail", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: Name of the log destination. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#name App#name}
        :param datadog: datadog block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#datadog App#datadog}
        :param logtail: logtail block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#logtail App#logtail}
        :param papertrail: papertrail block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#papertrail App#papertrail}
        '''
        if isinstance(datadog, dict):
            datadog = AppSpecJobLogDestinationDatadog(**datadog)
        if isinstance(logtail, dict):
            logtail = AppSpecJobLogDestinationLogtail(**logtail)
        if isinstance(papertrail, dict):
            papertrail = AppSpecJobLogDestinationPapertrail(**papertrail)
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecJobLogDestination.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument datadog", value=datadog, expected_type=type_hints["datadog"])
            check_type(argname="argument logtail", value=logtail, expected_type=type_hints["logtail"])
            check_type(argname="argument papertrail", value=papertrail, expected_type=type_hints["papertrail"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if datadog is not None:
            self._values["datadog"] = datadog
        if logtail is not None:
            self._values["logtail"] = logtail
        if papertrail is not None:
            self._values["papertrail"] = papertrail

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the log destination.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#name App#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def datadog(self) -> typing.Optional["AppSpecJobLogDestinationDatadog"]:
        '''datadog block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#datadog App#datadog}
        '''
        result = self._values.get("datadog")
        return typing.cast(typing.Optional["AppSpecJobLogDestinationDatadog"], result)

    @builtins.property
    def logtail(self) -> typing.Optional["AppSpecJobLogDestinationLogtail"]:
        '''logtail block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#logtail App#logtail}
        '''
        result = self._values.get("logtail")
        return typing.cast(typing.Optional["AppSpecJobLogDestinationLogtail"], result)

    @builtins.property
    def papertrail(self) -> typing.Optional["AppSpecJobLogDestinationPapertrail"]:
        '''papertrail block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#papertrail App#papertrail}
        '''
        result = self._values.get("papertrail")
        return typing.cast(typing.Optional["AppSpecJobLogDestinationPapertrail"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecJobLogDestination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecJobLogDestinationDatadog",
    jsii_struct_bases=[],
    name_mapping={"api_key": "apiKey", "endpoint": "endpoint"},
)
class AppSpecJobLogDestinationDatadog:
    def __init__(
        self,
        *,
        api_key: builtins.str,
        endpoint: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param api_key: Datadog API key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#api_key App#api_key}
        :param endpoint: Datadog HTTP log intake endpoint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#endpoint App#endpoint}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecJobLogDestinationDatadog.__init__)
            check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
        self._values: typing.Dict[str, typing.Any] = {
            "api_key": api_key,
        }
        if endpoint is not None:
            self._values["endpoint"] = endpoint

    @builtins.property
    def api_key(self) -> builtins.str:
        '''Datadog API key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#api_key App#api_key}
        '''
        result = self._values.get("api_key")
        assert result is not None, "Required property 'api_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoint(self) -> typing.Optional[builtins.str]:
        '''Datadog HTTP log intake endpoint.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#endpoint App#endpoint}
        '''
        result = self._values.get("endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecJobLogDestinationDatadog(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecJobLogDestinationDatadogOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecJobLogDestinationDatadogOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecJobLogDestinationDatadogOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEndpoint")
    def reset_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpoint", []))

    @builtins.property
    @jsii.member(jsii_name="apiKeyInput")
    def api_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="apiKey")
    def api_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiKey"))

    @api_key.setter
    def api_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobLogDestinationDatadogOutputReference, "api_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiKey", value)

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobLogDestinationDatadogOutputReference, "endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecJobLogDestinationDatadog]:
        return typing.cast(typing.Optional[AppSpecJobLogDestinationDatadog], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppSpecJobLogDestinationDatadog],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobLogDestinationDatadogOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecJobLogDestinationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecJobLogDestinationList",
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
            type_hints = typing.get_type_hints(AppSpecJobLogDestinationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AppSpecJobLogDestinationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecJobLogDestinationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppSpecJobLogDestinationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobLogDestinationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecJobLogDestinationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecJobLogDestinationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecJobLogDestination]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecJobLogDestination]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecJobLogDestination]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobLogDestinationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecJobLogDestinationLogtail",
    jsii_struct_bases=[],
    name_mapping={"token": "token"},
)
class AppSpecJobLogDestinationLogtail:
    def __init__(self, *, token: builtins.str) -> None:
        '''
        :param token: Logtail token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#token App#token}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecJobLogDestinationLogtail.__init__)
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
        self._values: typing.Dict[str, typing.Any] = {
            "token": token,
        }

    @builtins.property
    def token(self) -> builtins.str:
        '''Logtail token.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#token App#token}
        '''
        result = self._values.get("token")
        assert result is not None, "Required property 'token' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecJobLogDestinationLogtail(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecJobLogDestinationLogtailOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecJobLogDestinationLogtailOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecJobLogDestinationLogtailOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="tokenInput")
    def token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenInput"))

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "token"))

    @token.setter
    def token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobLogDestinationLogtailOutputReference, "token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "token", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecJobLogDestinationLogtail]:
        return typing.cast(typing.Optional[AppSpecJobLogDestinationLogtail], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppSpecJobLogDestinationLogtail],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobLogDestinationLogtailOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecJobLogDestinationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecJobLogDestinationOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecJobLogDestinationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDatadog")
    def put_datadog(
        self,
        *,
        api_key: builtins.str,
        endpoint: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param api_key: Datadog API key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#api_key App#api_key}
        :param endpoint: Datadog HTTP log intake endpoint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#endpoint App#endpoint}
        '''
        value = AppSpecJobLogDestinationDatadog(api_key=api_key, endpoint=endpoint)

        return typing.cast(None, jsii.invoke(self, "putDatadog", [value]))

    @jsii.member(jsii_name="putLogtail")
    def put_logtail(self, *, token: builtins.str) -> None:
        '''
        :param token: Logtail token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#token App#token}
        '''
        value = AppSpecJobLogDestinationLogtail(token=token)

        return typing.cast(None, jsii.invoke(self, "putLogtail", [value]))

    @jsii.member(jsii_name="putPapertrail")
    def put_papertrail(self, *, endpoint: builtins.str) -> None:
        '''
        :param endpoint: Papertrail syslog endpoint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#endpoint App#endpoint}
        '''
        value = AppSpecJobLogDestinationPapertrail(endpoint=endpoint)

        return typing.cast(None, jsii.invoke(self, "putPapertrail", [value]))

    @jsii.member(jsii_name="resetDatadog")
    def reset_datadog(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatadog", []))

    @jsii.member(jsii_name="resetLogtail")
    def reset_logtail(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogtail", []))

    @jsii.member(jsii_name="resetPapertrail")
    def reset_papertrail(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPapertrail", []))

    @builtins.property
    @jsii.member(jsii_name="datadog")
    def datadog(self) -> AppSpecJobLogDestinationDatadogOutputReference:
        return typing.cast(AppSpecJobLogDestinationDatadogOutputReference, jsii.get(self, "datadog"))

    @builtins.property
    @jsii.member(jsii_name="logtail")
    def logtail(self) -> AppSpecJobLogDestinationLogtailOutputReference:
        return typing.cast(AppSpecJobLogDestinationLogtailOutputReference, jsii.get(self, "logtail"))

    @builtins.property
    @jsii.member(jsii_name="papertrail")
    def papertrail(self) -> "AppSpecJobLogDestinationPapertrailOutputReference":
        return typing.cast("AppSpecJobLogDestinationPapertrailOutputReference", jsii.get(self, "papertrail"))

    @builtins.property
    @jsii.member(jsii_name="datadogInput")
    def datadog_input(self) -> typing.Optional[AppSpecJobLogDestinationDatadog]:
        return typing.cast(typing.Optional[AppSpecJobLogDestinationDatadog], jsii.get(self, "datadogInput"))

    @builtins.property
    @jsii.member(jsii_name="logtailInput")
    def logtail_input(self) -> typing.Optional[AppSpecJobLogDestinationLogtail]:
        return typing.cast(typing.Optional[AppSpecJobLogDestinationLogtail], jsii.get(self, "logtailInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="papertrailInput")
    def papertrail_input(self) -> typing.Optional["AppSpecJobLogDestinationPapertrail"]:
        return typing.cast(typing.Optional["AppSpecJobLogDestinationPapertrail"], jsii.get(self, "papertrailInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobLogDestinationOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppSpecJobLogDestination, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppSpecJobLogDestination, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppSpecJobLogDestination, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobLogDestinationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecJobLogDestinationPapertrail",
    jsii_struct_bases=[],
    name_mapping={"endpoint": "endpoint"},
)
class AppSpecJobLogDestinationPapertrail:
    def __init__(self, *, endpoint: builtins.str) -> None:
        '''
        :param endpoint: Papertrail syslog endpoint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#endpoint App#endpoint}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecJobLogDestinationPapertrail.__init__)
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
        self._values: typing.Dict[str, typing.Any] = {
            "endpoint": endpoint,
        }

    @builtins.property
    def endpoint(self) -> builtins.str:
        '''Papertrail syslog endpoint.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#endpoint App#endpoint}
        '''
        result = self._values.get("endpoint")
        assert result is not None, "Required property 'endpoint' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecJobLogDestinationPapertrail(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecJobLogDestinationPapertrailOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecJobLogDestinationPapertrailOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecJobLogDestinationPapertrailOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobLogDestinationPapertrailOutputReference, "endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecJobLogDestinationPapertrail]:
        return typing.cast(typing.Optional[AppSpecJobLogDestinationPapertrail], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppSpecJobLogDestinationPapertrail],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobLogDestinationPapertrailOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecJobOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecJobOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecJobOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAlert")
    def put_alert(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppSpecJobAlert, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecJobOutputReference.put_alert)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAlert", [value]))

    @jsii.member(jsii_name="putEnv")
    def put_env(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppSpecJobEnv, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecJobOutputReference.put_env)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEnv", [value]))

    @jsii.member(jsii_name="putGit")
    def put_git(
        self,
        *,
        branch: typing.Optional[builtins.str] = None,
        repo_clone_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: The name of the branch to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        :param repo_clone_url: The clone URL of the repo. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo_clone_url App#repo_clone_url}
        '''
        value = AppSpecJobGit(branch=branch, repo_clone_url=repo_clone_url)

        return typing.cast(None, jsii.invoke(self, "putGit", [value]))

    @jsii.member(jsii_name="putGithub")
    def put_github(
        self,
        *,
        branch: typing.Optional[builtins.str] = None,
        deploy_on_push: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: The name of the branch to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        :param deploy_on_push: Whether to automatically deploy new commits made to the repo. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        :param repo: The name of the repo in the format ``owner/repo``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo App#repo}
        '''
        value = AppSpecJobGithub(
            branch=branch, deploy_on_push=deploy_on_push, repo=repo
        )

        return typing.cast(None, jsii.invoke(self, "putGithub", [value]))

    @jsii.member(jsii_name="putGitlab")
    def put_gitlab(
        self,
        *,
        branch: typing.Optional[builtins.str] = None,
        deploy_on_push: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: The name of the branch to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        :param deploy_on_push: Whether to automatically deploy new commits made to the repo. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        :param repo: The name of the repo in the format ``owner/repo``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo App#repo}
        '''
        value = AppSpecJobGitlab(
            branch=branch, deploy_on_push=deploy_on_push, repo=repo
        )

        return typing.cast(None, jsii.invoke(self, "putGitlab", [value]))

    @jsii.member(jsii_name="putImage")
    def put_image(
        self,
        *,
        registry_type: builtins.str,
        repository: builtins.str,
        deploy_on_push: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppSpecJobImageDeployOnPush, typing.Dict[str, typing.Any]]]]] = None,
        registry: typing.Optional[builtins.str] = None,
        tag: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param registry_type: The registry type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#registry_type App#registry_type}
        :param repository: The repository name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repository App#repository}
        :param deploy_on_push: deploy_on_push block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        :param registry: The registry name. Must be left empty for the DOCR registry type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#registry App#registry}
        :param tag: The repository tag. Defaults to latest if not provided. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#tag App#tag}
        '''
        value = AppSpecJobImage(
            registry_type=registry_type,
            repository=repository,
            deploy_on_push=deploy_on_push,
            registry=registry,
            tag=tag,
        )

        return typing.cast(None, jsii.invoke(self, "putImage", [value]))

    @jsii.member(jsii_name="putLogDestination")
    def put_log_destination(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppSpecJobLogDestination, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecJobOutputReference.put_log_destination)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLogDestination", [value]))

    @jsii.member(jsii_name="resetAlert")
    def reset_alert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlert", []))

    @jsii.member(jsii_name="resetBuildCommand")
    def reset_build_command(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildCommand", []))

    @jsii.member(jsii_name="resetDockerfilePath")
    def reset_dockerfile_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDockerfilePath", []))

    @jsii.member(jsii_name="resetEnv")
    def reset_env(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnv", []))

    @jsii.member(jsii_name="resetEnvironmentSlug")
    def reset_environment_slug(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnvironmentSlug", []))

    @jsii.member(jsii_name="resetGit")
    def reset_git(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGit", []))

    @jsii.member(jsii_name="resetGithub")
    def reset_github(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGithub", []))

    @jsii.member(jsii_name="resetGitlab")
    def reset_gitlab(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGitlab", []))

    @jsii.member(jsii_name="resetImage")
    def reset_image(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImage", []))

    @jsii.member(jsii_name="resetInstanceCount")
    def reset_instance_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceCount", []))

    @jsii.member(jsii_name="resetInstanceSizeSlug")
    def reset_instance_size_slug(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceSizeSlug", []))

    @jsii.member(jsii_name="resetKind")
    def reset_kind(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKind", []))

    @jsii.member(jsii_name="resetLogDestination")
    def reset_log_destination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogDestination", []))

    @jsii.member(jsii_name="resetRunCommand")
    def reset_run_command(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRunCommand", []))

    @jsii.member(jsii_name="resetSourceDir")
    def reset_source_dir(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceDir", []))

    @builtins.property
    @jsii.member(jsii_name="alert")
    def alert(self) -> AppSpecJobAlertList:
        return typing.cast(AppSpecJobAlertList, jsii.get(self, "alert"))

    @builtins.property
    @jsii.member(jsii_name="env")
    def env(self) -> AppSpecJobEnvList:
        return typing.cast(AppSpecJobEnvList, jsii.get(self, "env"))

    @builtins.property
    @jsii.member(jsii_name="git")
    def git(self) -> AppSpecJobGitOutputReference:
        return typing.cast(AppSpecJobGitOutputReference, jsii.get(self, "git"))

    @builtins.property
    @jsii.member(jsii_name="github")
    def github(self) -> AppSpecJobGithubOutputReference:
        return typing.cast(AppSpecJobGithubOutputReference, jsii.get(self, "github"))

    @builtins.property
    @jsii.member(jsii_name="gitlab")
    def gitlab(self) -> AppSpecJobGitlabOutputReference:
        return typing.cast(AppSpecJobGitlabOutputReference, jsii.get(self, "gitlab"))

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> AppSpecJobImageOutputReference:
        return typing.cast(AppSpecJobImageOutputReference, jsii.get(self, "image"))

    @builtins.property
    @jsii.member(jsii_name="logDestination")
    def log_destination(self) -> AppSpecJobLogDestinationList:
        return typing.cast(AppSpecJobLogDestinationList, jsii.get(self, "logDestination"))

    @builtins.property
    @jsii.member(jsii_name="alertInput")
    def alert_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecJobAlert]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecJobAlert]]], jsii.get(self, "alertInput"))

    @builtins.property
    @jsii.member(jsii_name="buildCommandInput")
    def build_command_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "buildCommandInput"))

    @builtins.property
    @jsii.member(jsii_name="dockerfilePathInput")
    def dockerfile_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dockerfilePathInput"))

    @builtins.property
    @jsii.member(jsii_name="envInput")
    def env_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecJobEnv]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecJobEnv]]], jsii.get(self, "envInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentSlugInput")
    def environment_slug_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentSlugInput"))

    @builtins.property
    @jsii.member(jsii_name="githubInput")
    def github_input(self) -> typing.Optional[AppSpecJobGithub]:
        return typing.cast(typing.Optional[AppSpecJobGithub], jsii.get(self, "githubInput"))

    @builtins.property
    @jsii.member(jsii_name="gitInput")
    def git_input(self) -> typing.Optional[AppSpecJobGit]:
        return typing.cast(typing.Optional[AppSpecJobGit], jsii.get(self, "gitInput"))

    @builtins.property
    @jsii.member(jsii_name="gitlabInput")
    def gitlab_input(self) -> typing.Optional[AppSpecJobGitlab]:
        return typing.cast(typing.Optional[AppSpecJobGitlab], jsii.get(self, "gitlabInput"))

    @builtins.property
    @jsii.member(jsii_name="imageInput")
    def image_input(self) -> typing.Optional[AppSpecJobImage]:
        return typing.cast(typing.Optional[AppSpecJobImage], jsii.get(self, "imageInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceCountInput")
    def instance_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "instanceCountInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceSizeSlugInput")
    def instance_size_slug_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceSizeSlugInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="logDestinationInput")
    def log_destination_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecJobLogDestination]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecJobLogDestination]]], jsii.get(self, "logDestinationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="runCommandInput")
    def run_command_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runCommandInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceDirInput")
    def source_dir_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceDirInput"))

    @builtins.property
    @jsii.member(jsii_name="buildCommand")
    def build_command(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "buildCommand"))

    @build_command.setter
    def build_command(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobOutputReference, "build_command").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buildCommand", value)

    @builtins.property
    @jsii.member(jsii_name="dockerfilePath")
    def dockerfile_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dockerfilePath"))

    @dockerfile_path.setter
    def dockerfile_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobOutputReference, "dockerfile_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dockerfilePath", value)

    @builtins.property
    @jsii.member(jsii_name="environmentSlug")
    def environment_slug(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "environmentSlug"))

    @environment_slug.setter
    def environment_slug(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobOutputReference, "environment_slug").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentSlug", value)

    @builtins.property
    @jsii.member(jsii_name="instanceCount")
    def instance_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instanceCount"))

    @instance_count.setter
    def instance_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobOutputReference, "instance_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceCount", value)

    @builtins.property
    @jsii.member(jsii_name="instanceSizeSlug")
    def instance_size_slug(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceSizeSlug"))

    @instance_size_slug.setter
    def instance_size_slug(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobOutputReference, "instance_size_slug").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceSizeSlug", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobOutputReference, "kind").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="runCommand")
    def run_command(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runCommand"))

    @run_command.setter
    def run_command(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobOutputReference, "run_command").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runCommand", value)

    @builtins.property
    @jsii.member(jsii_name="sourceDir")
    def source_dir(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceDir"))

    @source_dir.setter
    def source_dir(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobOutputReference, "source_dir").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceDir", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppSpecJob, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppSpecJob, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppSpecJob, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecJobOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAlert")
    def put_alert(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppSpecAlert, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecOutputReference.put_alert)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAlert", [value]))

    @jsii.member(jsii_name="putDatabase")
    def put_database(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppSpecDatabase, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecOutputReference.put_database)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDatabase", [value]))

    @jsii.member(jsii_name="putDomain")
    def put_domain(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppSpecDomain, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecOutputReference.put_domain)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDomain", [value]))

    @jsii.member(jsii_name="putEnv")
    def put_env(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppSpecEnv, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecOutputReference.put_env)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEnv", [value]))

    @jsii.member(jsii_name="putFunction")
    def put_function(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppSpecFunction, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecOutputReference.put_function)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putFunction", [value]))

    @jsii.member(jsii_name="putJob")
    def put_job(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppSpecJob, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecOutputReference.put_job)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putJob", [value]))

    @jsii.member(jsii_name="putService")
    def put_service(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecService", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecOutputReference.put_service)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putService", [value]))

    @jsii.member(jsii_name="putStaticSite")
    def put_static_site(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecStaticSite", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecOutputReference.put_static_site)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putStaticSite", [value]))

    @jsii.member(jsii_name="putWorker")
    def put_worker(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecWorker", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecOutputReference.put_worker)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWorker", [value]))

    @jsii.member(jsii_name="resetAlert")
    def reset_alert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlert", []))

    @jsii.member(jsii_name="resetDatabase")
    def reset_database(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabase", []))

    @jsii.member(jsii_name="resetDomain")
    def reset_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDomain", []))

    @jsii.member(jsii_name="resetDomains")
    def reset_domains(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDomains", []))

    @jsii.member(jsii_name="resetEnv")
    def reset_env(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnv", []))

    @jsii.member(jsii_name="resetFunction")
    def reset_function(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFunction", []))

    @jsii.member(jsii_name="resetJob")
    def reset_job(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJob", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetService")
    def reset_service(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetService", []))

    @jsii.member(jsii_name="resetStaticSite")
    def reset_static_site(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStaticSite", []))

    @jsii.member(jsii_name="resetWorker")
    def reset_worker(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorker", []))

    @builtins.property
    @jsii.member(jsii_name="alert")
    def alert(self) -> AppSpecAlertList:
        return typing.cast(AppSpecAlertList, jsii.get(self, "alert"))

    @builtins.property
    @jsii.member(jsii_name="database")
    def database(self) -> AppSpecDatabaseList:
        return typing.cast(AppSpecDatabaseList, jsii.get(self, "database"))

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> AppSpecDomainList:
        return typing.cast(AppSpecDomainList, jsii.get(self, "domain"))

    @builtins.property
    @jsii.member(jsii_name="env")
    def env(self) -> AppSpecEnvList:
        return typing.cast(AppSpecEnvList, jsii.get(self, "env"))

    @builtins.property
    @jsii.member(jsii_name="function")
    def function(self) -> AppSpecFunctionList:
        return typing.cast(AppSpecFunctionList, jsii.get(self, "function"))

    @builtins.property
    @jsii.member(jsii_name="job")
    def job(self) -> AppSpecJobList:
        return typing.cast(AppSpecJobList, jsii.get(self, "job"))

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> "AppSpecServiceList":
        return typing.cast("AppSpecServiceList", jsii.get(self, "service"))

    @builtins.property
    @jsii.member(jsii_name="staticSite")
    def static_site(self) -> "AppSpecStaticSiteList":
        return typing.cast("AppSpecStaticSiteList", jsii.get(self, "staticSite"))

    @builtins.property
    @jsii.member(jsii_name="worker")
    def worker(self) -> "AppSpecWorkerList":
        return typing.cast("AppSpecWorkerList", jsii.get(self, "worker"))

    @builtins.property
    @jsii.member(jsii_name="alertInput")
    def alert_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecAlert]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecAlert]]], jsii.get(self, "alertInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseInput")
    def database_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecDatabase]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecDatabase]]], jsii.get(self, "databaseInput"))

    @builtins.property
    @jsii.member(jsii_name="domainInput")
    def domain_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecDomain]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecDomain]]], jsii.get(self, "domainInput"))

    @builtins.property
    @jsii.member(jsii_name="domainsInput")
    def domains_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "domainsInput"))

    @builtins.property
    @jsii.member(jsii_name="envInput")
    def env_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecEnv]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecEnv]]], jsii.get(self, "envInput"))

    @builtins.property
    @jsii.member(jsii_name="functionInput")
    def function_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecFunction]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecFunction]]], jsii.get(self, "functionInput"))

    @builtins.property
    @jsii.member(jsii_name="jobInput")
    def job_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecJob]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecJob]]], jsii.get(self, "jobInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecService"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecService"]]], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="staticSiteInput")
    def static_site_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecStaticSite"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecStaticSite"]]], jsii.get(self, "staticSiteInput"))

    @builtins.property
    @jsii.member(jsii_name="workerInput")
    def worker_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecWorker"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecWorker"]]], jsii.get(self, "workerInput"))

    @builtins.property
    @jsii.member(jsii_name="domains")
    def domains(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "domains"))

    @domains.setter
    def domains(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecOutputReference, "domains").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domains", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecOutputReference, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpec]:
        return typing.cast(typing.Optional[AppSpec], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppSpec]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecService",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "alert": "alert",
        "build_command": "buildCommand",
        "cors": "cors",
        "dockerfile_path": "dockerfilePath",
        "env": "env",
        "environment_slug": "environmentSlug",
        "git": "git",
        "github": "github",
        "gitlab": "gitlab",
        "health_check": "healthCheck",
        "http_port": "httpPort",
        "image": "image",
        "instance_count": "instanceCount",
        "instance_size_slug": "instanceSizeSlug",
        "internal_ports": "internalPorts",
        "log_destination": "logDestination",
        "routes": "routes",
        "run_command": "runCommand",
        "source_dir": "sourceDir",
    },
)
class AppSpecService:
    def __init__(
        self,
        *,
        name: builtins.str,
        alert: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecServiceAlert", typing.Dict[str, typing.Any]]]]] = None,
        build_command: typing.Optional[builtins.str] = None,
        cors: typing.Optional[typing.Union["AppSpecServiceCors", typing.Dict[str, typing.Any]]] = None,
        dockerfile_path: typing.Optional[builtins.str] = None,
        env: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecServiceEnv", typing.Dict[str, typing.Any]]]]] = None,
        environment_slug: typing.Optional[builtins.str] = None,
        git: typing.Optional[typing.Union["AppSpecServiceGit", typing.Dict[str, typing.Any]]] = None,
        github: typing.Optional[typing.Union["AppSpecServiceGithub", typing.Dict[str, typing.Any]]] = None,
        gitlab: typing.Optional[typing.Union["AppSpecServiceGitlab", typing.Dict[str, typing.Any]]] = None,
        health_check: typing.Optional[typing.Union["AppSpecServiceHealthCheck", typing.Dict[str, typing.Any]]] = None,
        http_port: typing.Optional[jsii.Number] = None,
        image: typing.Optional[typing.Union["AppSpecServiceImage", typing.Dict[str, typing.Any]]] = None,
        instance_count: typing.Optional[jsii.Number] = None,
        instance_size_slug: typing.Optional[builtins.str] = None,
        internal_ports: typing.Optional[typing.Sequence[jsii.Number]] = None,
        log_destination: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecServiceLogDestination", typing.Dict[str, typing.Any]]]]] = None,
        routes: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecServiceRoutes", typing.Dict[str, typing.Any]]]]] = None,
        run_command: typing.Optional[builtins.str] = None,
        source_dir: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: The name of the component. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#name App#name}
        :param alert: alert block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#alert App#alert}
        :param build_command: An optional build command to run while building this component from source. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#build_command App#build_command}
        :param cors: cors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#cors App#cors}
        :param dockerfile_path: The path to a Dockerfile relative to the root of the repo. If set, overrides usage of buildpacks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#dockerfile_path App#dockerfile_path}
        :param env: env block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#env App#env}
        :param environment_slug: An environment slug describing the type of this app. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#environment_slug App#environment_slug}
        :param git: git block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#git App#git}
        :param github: github block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#github App#github}
        :param gitlab: gitlab block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#gitlab App#gitlab}
        :param health_check: health_check block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#health_check App#health_check}
        :param http_port: The internal port on which this service's run command will listen. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#http_port App#http_port}
        :param image: image block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#image App#image}
        :param instance_count: The amount of instances that this component should be scaled to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#instance_count App#instance_count}
        :param instance_size_slug: The instance size to use for this component. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#instance_size_slug App#instance_size_slug}
        :param internal_ports: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#internal_ports App#internal_ports}.
        :param log_destination: log_destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#log_destination App#log_destination}
        :param routes: routes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#routes App#routes}
        :param run_command: An optional run command to override the component's default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#run_command App#run_command}
        :param source_dir: An optional path to the working directory to use for the build. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#source_dir App#source_dir}
        '''
        if isinstance(cors, dict):
            cors = AppSpecServiceCors(**cors)
        if isinstance(git, dict):
            git = AppSpecServiceGit(**git)
        if isinstance(github, dict):
            github = AppSpecServiceGithub(**github)
        if isinstance(gitlab, dict):
            gitlab = AppSpecServiceGitlab(**gitlab)
        if isinstance(health_check, dict):
            health_check = AppSpecServiceHealthCheck(**health_check)
        if isinstance(image, dict):
            image = AppSpecServiceImage(**image)
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecService.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument alert", value=alert, expected_type=type_hints["alert"])
            check_type(argname="argument build_command", value=build_command, expected_type=type_hints["build_command"])
            check_type(argname="argument cors", value=cors, expected_type=type_hints["cors"])
            check_type(argname="argument dockerfile_path", value=dockerfile_path, expected_type=type_hints["dockerfile_path"])
            check_type(argname="argument env", value=env, expected_type=type_hints["env"])
            check_type(argname="argument environment_slug", value=environment_slug, expected_type=type_hints["environment_slug"])
            check_type(argname="argument git", value=git, expected_type=type_hints["git"])
            check_type(argname="argument github", value=github, expected_type=type_hints["github"])
            check_type(argname="argument gitlab", value=gitlab, expected_type=type_hints["gitlab"])
            check_type(argname="argument health_check", value=health_check, expected_type=type_hints["health_check"])
            check_type(argname="argument http_port", value=http_port, expected_type=type_hints["http_port"])
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument instance_count", value=instance_count, expected_type=type_hints["instance_count"])
            check_type(argname="argument instance_size_slug", value=instance_size_slug, expected_type=type_hints["instance_size_slug"])
            check_type(argname="argument internal_ports", value=internal_ports, expected_type=type_hints["internal_ports"])
            check_type(argname="argument log_destination", value=log_destination, expected_type=type_hints["log_destination"])
            check_type(argname="argument routes", value=routes, expected_type=type_hints["routes"])
            check_type(argname="argument run_command", value=run_command, expected_type=type_hints["run_command"])
            check_type(argname="argument source_dir", value=source_dir, expected_type=type_hints["source_dir"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if alert is not None:
            self._values["alert"] = alert
        if build_command is not None:
            self._values["build_command"] = build_command
        if cors is not None:
            self._values["cors"] = cors
        if dockerfile_path is not None:
            self._values["dockerfile_path"] = dockerfile_path
        if env is not None:
            self._values["env"] = env
        if environment_slug is not None:
            self._values["environment_slug"] = environment_slug
        if git is not None:
            self._values["git"] = git
        if github is not None:
            self._values["github"] = github
        if gitlab is not None:
            self._values["gitlab"] = gitlab
        if health_check is not None:
            self._values["health_check"] = health_check
        if http_port is not None:
            self._values["http_port"] = http_port
        if image is not None:
            self._values["image"] = image
        if instance_count is not None:
            self._values["instance_count"] = instance_count
        if instance_size_slug is not None:
            self._values["instance_size_slug"] = instance_size_slug
        if internal_ports is not None:
            self._values["internal_ports"] = internal_ports
        if log_destination is not None:
            self._values["log_destination"] = log_destination
        if routes is not None:
            self._values["routes"] = routes
        if run_command is not None:
            self._values["run_command"] = run_command
        if source_dir is not None:
            self._values["source_dir"] = source_dir

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the component.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#name App#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alert(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecServiceAlert"]]]:
        '''alert block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#alert App#alert}
        '''
        result = self._values.get("alert")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecServiceAlert"]]], result)

    @builtins.property
    def build_command(self) -> typing.Optional[builtins.str]:
        '''An optional build command to run while building this component from source.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#build_command App#build_command}
        '''
        result = self._values.get("build_command")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cors(self) -> typing.Optional["AppSpecServiceCors"]:
        '''cors block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#cors App#cors}
        '''
        result = self._values.get("cors")
        return typing.cast(typing.Optional["AppSpecServiceCors"], result)

    @builtins.property
    def dockerfile_path(self) -> typing.Optional[builtins.str]:
        '''The path to a Dockerfile relative to the root of the repo. If set, overrides usage of buildpacks.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#dockerfile_path App#dockerfile_path}
        '''
        result = self._values.get("dockerfile_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def env(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecServiceEnv"]]]:
        '''env block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#env App#env}
        '''
        result = self._values.get("env")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecServiceEnv"]]], result)

    @builtins.property
    def environment_slug(self) -> typing.Optional[builtins.str]:
        '''An environment slug describing the type of this app.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#environment_slug App#environment_slug}
        '''
        result = self._values.get("environment_slug")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def git(self) -> typing.Optional["AppSpecServiceGit"]:
        '''git block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#git App#git}
        '''
        result = self._values.get("git")
        return typing.cast(typing.Optional["AppSpecServiceGit"], result)

    @builtins.property
    def github(self) -> typing.Optional["AppSpecServiceGithub"]:
        '''github block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#github App#github}
        '''
        result = self._values.get("github")
        return typing.cast(typing.Optional["AppSpecServiceGithub"], result)

    @builtins.property
    def gitlab(self) -> typing.Optional["AppSpecServiceGitlab"]:
        '''gitlab block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#gitlab App#gitlab}
        '''
        result = self._values.get("gitlab")
        return typing.cast(typing.Optional["AppSpecServiceGitlab"], result)

    @builtins.property
    def health_check(self) -> typing.Optional["AppSpecServiceHealthCheck"]:
        '''health_check block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#health_check App#health_check}
        '''
        result = self._values.get("health_check")
        return typing.cast(typing.Optional["AppSpecServiceHealthCheck"], result)

    @builtins.property
    def http_port(self) -> typing.Optional[jsii.Number]:
        '''The internal port on which this service's run command will listen.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#http_port App#http_port}
        '''
        result = self._values.get("http_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def image(self) -> typing.Optional["AppSpecServiceImage"]:
        '''image block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#image App#image}
        '''
        result = self._values.get("image")
        return typing.cast(typing.Optional["AppSpecServiceImage"], result)

    @builtins.property
    def instance_count(self) -> typing.Optional[jsii.Number]:
        '''The amount of instances that this component should be scaled to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#instance_count App#instance_count}
        '''
        result = self._values.get("instance_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def instance_size_slug(self) -> typing.Optional[builtins.str]:
        '''The instance size to use for this component.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#instance_size_slug App#instance_size_slug}
        '''
        result = self._values.get("instance_size_slug")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def internal_ports(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#internal_ports App#internal_ports}.'''
        result = self._values.get("internal_ports")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    @builtins.property
    def log_destination(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecServiceLogDestination"]]]:
        '''log_destination block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#log_destination App#log_destination}
        '''
        result = self._values.get("log_destination")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecServiceLogDestination"]]], result)

    @builtins.property
    def routes(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecServiceRoutes"]]]:
        '''routes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#routes App#routes}
        '''
        result = self._values.get("routes")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecServiceRoutes"]]], result)

    @builtins.property
    def run_command(self) -> typing.Optional[builtins.str]:
        '''An optional run command to override the component's default.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#run_command App#run_command}
        '''
        result = self._values.get("run_command")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_dir(self) -> typing.Optional[builtins.str]:
        '''An optional path to the working directory to use for the build.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#source_dir App#source_dir}
        '''
        result = self._values.get("source_dir")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecService(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceAlert",
    jsii_struct_bases=[],
    name_mapping={
        "operator": "operator",
        "rule": "rule",
        "value": "value",
        "window": "window",
        "disabled": "disabled",
    },
)
class AppSpecServiceAlert:
    def __init__(
        self,
        *,
        operator: builtins.str,
        rule: builtins.str,
        value: jsii.Number,
        window: builtins.str,
        disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#operator App#operator}.
        :param rule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#rule App#rule}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#value App#value}.
        :param window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#window App#window}.
        :param disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#disabled App#disabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecServiceAlert.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument window", value=window, expected_type=type_hints["window"])
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
            "rule": rule,
            "value": value,
            "window": window,
        }
        if disabled is not None:
            self._values["disabled"] = disabled

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#operator App#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#rule App#rule}.'''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#value App#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def window(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#window App#window}.'''
        result = self._values.get("window")
        assert result is not None, "Required property 'window' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#disabled App#disabled}.'''
        result = self._values.get("disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecServiceAlert(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecServiceAlertList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceAlertList",
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
            type_hints = typing.get_type_hints(AppSpecServiceAlertList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AppSpecServiceAlertOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecServiceAlertList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppSpecServiceAlertOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceAlertList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecServiceAlertList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecServiceAlertList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecServiceAlert]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecServiceAlert]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecServiceAlert]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceAlertList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecServiceAlertOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceAlertOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecServiceAlertOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDisabled")
    def reset_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisabled", []))

    @builtins.property
    @jsii.member(jsii_name="disabledInput")
    def disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disabledInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="windowInput")
    def window_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "windowInput"))

    @builtins.property
    @jsii.member(jsii_name="disabled")
    def disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disabled"))

    @disabled.setter
    def disabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceAlertOutputReference, "disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceAlertOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rule"))

    @rule.setter
    def rule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceAlertOutputReference, "rule").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceAlertOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="window")
    def window(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "window"))

    @window.setter
    def window(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceAlertOutputReference, "window").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "window", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppSpecServiceAlert, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppSpecServiceAlert, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppSpecServiceAlert, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceAlertOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceCors",
    jsii_struct_bases=[],
    name_mapping={
        "allow_credentials": "allowCredentials",
        "allow_headers": "allowHeaders",
        "allow_methods": "allowMethods",
        "allow_origins": "allowOrigins",
        "expose_headers": "exposeHeaders",
        "max_age": "maxAge",
    },
)
class AppSpecServiceCors:
    def __init__(
        self,
        *,
        allow_credentials: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_methods: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_origins: typing.Optional[typing.Union["AppSpecServiceCorsAllowOrigins", typing.Dict[str, typing.Any]]] = None,
        expose_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        max_age: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allow_credentials: Whether browsers should expose the response to the client-side JavaScript code when the request’s credentials mode is ``include``. This configures the Access-Control-Allow-Credentials header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_credentials App#allow_credentials}
        :param allow_headers: The set of allowed HTTP request headers. This configures the Access-Control-Allow-Headers header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_headers App#allow_headers}
        :param allow_methods: The set of allowed HTTP methods. This configures the Access-Control-Allow-Methods header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_methods App#allow_methods}
        :param allow_origins: allow_origins block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_origins App#allow_origins}
        :param expose_headers: The set of HTTP response headers that browsers are allowed to access. This configures the Access-Control-Expose-Headers header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#expose_headers App#expose_headers}
        :param max_age: An optional duration specifying how long browsers can cache the results of a preflight request. This configures the Access-Control-Max-Age header. Example: ``5h30m``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#max_age App#max_age}
        '''
        if isinstance(allow_origins, dict):
            allow_origins = AppSpecServiceCorsAllowOrigins(**allow_origins)
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecServiceCors.__init__)
            check_type(argname="argument allow_credentials", value=allow_credentials, expected_type=type_hints["allow_credentials"])
            check_type(argname="argument allow_headers", value=allow_headers, expected_type=type_hints["allow_headers"])
            check_type(argname="argument allow_methods", value=allow_methods, expected_type=type_hints["allow_methods"])
            check_type(argname="argument allow_origins", value=allow_origins, expected_type=type_hints["allow_origins"])
            check_type(argname="argument expose_headers", value=expose_headers, expected_type=type_hints["expose_headers"])
            check_type(argname="argument max_age", value=max_age, expected_type=type_hints["max_age"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allow_credentials is not None:
            self._values["allow_credentials"] = allow_credentials
        if allow_headers is not None:
            self._values["allow_headers"] = allow_headers
        if allow_methods is not None:
            self._values["allow_methods"] = allow_methods
        if allow_origins is not None:
            self._values["allow_origins"] = allow_origins
        if expose_headers is not None:
            self._values["expose_headers"] = expose_headers
        if max_age is not None:
            self._values["max_age"] = max_age

    @builtins.property
    def allow_credentials(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether browsers should expose the response to the client-side JavaScript code when the request’s credentials mode is ``include``.

        This configures the Access-Control-Allow-Credentials header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_credentials App#allow_credentials}
        '''
        result = self._values.get("allow_credentials")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The set of allowed HTTP request headers. This configures the Access-Control-Allow-Headers header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_headers App#allow_headers}
        '''
        result = self._values.get("allow_headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allow_methods(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The set of allowed HTTP methods. This configures the Access-Control-Allow-Methods header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_methods App#allow_methods}
        '''
        result = self._values.get("allow_methods")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allow_origins(self) -> typing.Optional["AppSpecServiceCorsAllowOrigins"]:
        '''allow_origins block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_origins App#allow_origins}
        '''
        result = self._values.get("allow_origins")
        return typing.cast(typing.Optional["AppSpecServiceCorsAllowOrigins"], result)

    @builtins.property
    def expose_headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The set of HTTP response headers that browsers are allowed to access. This configures the Access-Control-Expose-Headers header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#expose_headers App#expose_headers}
        '''
        result = self._values.get("expose_headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def max_age(self) -> typing.Optional[builtins.str]:
        '''An optional duration specifying how long browsers can cache the results of a preflight request.

        This configures the Access-Control-Max-Age header. Example: ``5h30m``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#max_age App#max_age}
        '''
        result = self._values.get("max_age")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecServiceCors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceCorsAllowOrigins",
    jsii_struct_bases=[],
    name_mapping={"exact": "exact", "prefix": "prefix", "regex": "regex"},
)
class AppSpecServiceCorsAllowOrigins:
    def __init__(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        regex: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param exact: Exact string match. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#exact App#exact}
        :param prefix: Prefix-based match. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#prefix App#prefix}
        :param regex: RE2 style regex-based match. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#regex App#regex}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecServiceCorsAllowOrigins.__init__)
            check_type(argname="argument exact", value=exact, expected_type=type_hints["exact"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument regex", value=regex, expected_type=type_hints["regex"])
        self._values: typing.Dict[str, typing.Any] = {}
        if exact is not None:
            self._values["exact"] = exact
        if prefix is not None:
            self._values["prefix"] = prefix
        if regex is not None:
            self._values["regex"] = regex

    @builtins.property
    def exact(self) -> typing.Optional[builtins.str]:
        '''Exact string match.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#exact App#exact}
        '''
        result = self._values.get("exact")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Prefix-based match.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#prefix App#prefix}
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def regex(self) -> typing.Optional[builtins.str]:
        '''RE2 style regex-based match.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#regex App#regex}
        '''
        result = self._values.get("regex")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecServiceCorsAllowOrigins(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecServiceCorsAllowOriginsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceCorsAllowOriginsOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecServiceCorsAllowOriginsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExact")
    def reset_exact(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExact", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @jsii.member(jsii_name="resetRegex")
    def reset_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegex", []))

    @builtins.property
    @jsii.member(jsii_name="exactInput")
    def exact_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "exactInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="regexInput")
    def regex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regexInput"))

    @builtins.property
    @jsii.member(jsii_name="exact")
    def exact(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "exact"))

    @exact.setter
    def exact(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceCorsAllowOriginsOutputReference, "exact").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exact", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceCorsAllowOriginsOutputReference, "prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="regex")
    def regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regex"))

    @regex.setter
    def regex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceCorsAllowOriginsOutputReference, "regex").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regex", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecServiceCorsAllowOrigins]:
        return typing.cast(typing.Optional[AppSpecServiceCorsAllowOrigins], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppSpecServiceCorsAllowOrigins],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceCorsAllowOriginsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecServiceCorsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceCorsOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecServiceCorsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAllowOrigins")
    def put_allow_origins(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        regex: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param exact: Exact string match. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#exact App#exact}
        :param prefix: Prefix-based match. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#prefix App#prefix}
        :param regex: RE2 style regex-based match. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#regex App#regex}
        '''
        value = AppSpecServiceCorsAllowOrigins(exact=exact, prefix=prefix, regex=regex)

        return typing.cast(None, jsii.invoke(self, "putAllowOrigins", [value]))

    @jsii.member(jsii_name="resetAllowCredentials")
    def reset_allow_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowCredentials", []))

    @jsii.member(jsii_name="resetAllowHeaders")
    def reset_allow_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowHeaders", []))

    @jsii.member(jsii_name="resetAllowMethods")
    def reset_allow_methods(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowMethods", []))

    @jsii.member(jsii_name="resetAllowOrigins")
    def reset_allow_origins(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowOrigins", []))

    @jsii.member(jsii_name="resetExposeHeaders")
    def reset_expose_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExposeHeaders", []))

    @jsii.member(jsii_name="resetMaxAge")
    def reset_max_age(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxAge", []))

    @builtins.property
    @jsii.member(jsii_name="allowOrigins")
    def allow_origins(self) -> AppSpecServiceCorsAllowOriginsOutputReference:
        return typing.cast(AppSpecServiceCorsAllowOriginsOutputReference, jsii.get(self, "allowOrigins"))

    @builtins.property
    @jsii.member(jsii_name="allowCredentialsInput")
    def allow_credentials_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowCredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowHeadersInput")
    def allow_headers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="allowMethodsInput")
    def allow_methods_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowMethodsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowOriginsInput")
    def allow_origins_input(self) -> typing.Optional[AppSpecServiceCorsAllowOrigins]:
        return typing.cast(typing.Optional[AppSpecServiceCorsAllowOrigins], jsii.get(self, "allowOriginsInput"))

    @builtins.property
    @jsii.member(jsii_name="exposeHeadersInput")
    def expose_headers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exposeHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="maxAgeInput")
    def max_age_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxAgeInput"))

    @builtins.property
    @jsii.member(jsii_name="allowCredentials")
    def allow_credentials(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowCredentials"))

    @allow_credentials.setter
    def allow_credentials(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceCorsOutputReference, "allow_credentials").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowCredentials", value)

    @builtins.property
    @jsii.member(jsii_name="allowHeaders")
    def allow_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowHeaders"))

    @allow_headers.setter
    def allow_headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceCorsOutputReference, "allow_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="allowMethods")
    def allow_methods(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowMethods"))

    @allow_methods.setter
    def allow_methods(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceCorsOutputReference, "allow_methods").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowMethods", value)

    @builtins.property
    @jsii.member(jsii_name="exposeHeaders")
    def expose_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exposeHeaders"))

    @expose_headers.setter
    def expose_headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceCorsOutputReference, "expose_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exposeHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="maxAge")
    def max_age(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxAge"))

    @max_age.setter
    def max_age(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceCorsOutputReference, "max_age").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAge", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecServiceCors]:
        return typing.cast(typing.Optional[AppSpecServiceCors], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppSpecServiceCors]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceCorsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceEnv",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "scope": "scope", "type": "type", "value": "value"},
)
class AppSpecServiceEnv:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        scope: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: The name of the environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#key App#key}
        :param scope: The visibility scope of the environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#scope App#scope}
        :param type: The type of the environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#type App#type}
        :param value: The value of the environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#value App#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecServiceEnv.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if scope is not None:
            self._values["scope"] = scope
        if type is not None:
            self._values["type"] = type
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The name of the environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#key App#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scope(self) -> typing.Optional[builtins.str]:
        '''The visibility scope of the environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#scope App#scope}
        '''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of the environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#type App#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''The value of the environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#value App#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecServiceEnv(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecServiceEnvList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceEnvList",
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
            type_hints = typing.get_type_hints(AppSpecServiceEnvList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AppSpecServiceEnvOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecServiceEnvList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppSpecServiceEnvOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceEnvList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecServiceEnvList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecServiceEnvList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecServiceEnv]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecServiceEnv]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecServiceEnv]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceEnvList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecServiceEnvOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceEnvOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecServiceEnvOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetScope")
    def reset_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScope", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="scopeInput")
    def scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scopeInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceEnvOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceEnvOutputReference, "scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceEnvOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceEnvOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppSpecServiceEnv, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppSpecServiceEnv, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppSpecServiceEnv, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceEnvOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceGit",
    jsii_struct_bases=[],
    name_mapping={"branch": "branch", "repo_clone_url": "repoCloneUrl"},
)
class AppSpecServiceGit:
    def __init__(
        self,
        *,
        branch: typing.Optional[builtins.str] = None,
        repo_clone_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: The name of the branch to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        :param repo_clone_url: The clone URL of the repo. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo_clone_url App#repo_clone_url}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecServiceGit.__init__)
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
            check_type(argname="argument repo_clone_url", value=repo_clone_url, expected_type=type_hints["repo_clone_url"])
        self._values: typing.Dict[str, typing.Any] = {}
        if branch is not None:
            self._values["branch"] = branch
        if repo_clone_url is not None:
            self._values["repo_clone_url"] = repo_clone_url

    @builtins.property
    def branch(self) -> typing.Optional[builtins.str]:
        '''The name of the branch to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        '''
        result = self._values.get("branch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def repo_clone_url(self) -> typing.Optional[builtins.str]:
        '''The clone URL of the repo.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo_clone_url App#repo_clone_url}
        '''
        result = self._values.get("repo_clone_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecServiceGit(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecServiceGitOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceGitOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecServiceGitOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBranch")
    def reset_branch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBranch", []))

    @jsii.member(jsii_name="resetRepoCloneUrl")
    def reset_repo_clone_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepoCloneUrl", []))

    @builtins.property
    @jsii.member(jsii_name="branchInput")
    def branch_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "branchInput"))

    @builtins.property
    @jsii.member(jsii_name="repoCloneUrlInput")
    def repo_clone_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repoCloneUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="branch")
    def branch(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "branch"))

    @branch.setter
    def branch(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceGitOutputReference, "branch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "branch", value)

    @builtins.property
    @jsii.member(jsii_name="repoCloneUrl")
    def repo_clone_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repoCloneUrl"))

    @repo_clone_url.setter
    def repo_clone_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceGitOutputReference, "repo_clone_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repoCloneUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecServiceGit]:
        return typing.cast(typing.Optional[AppSpecServiceGit], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppSpecServiceGit]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceGitOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceGithub",
    jsii_struct_bases=[],
    name_mapping={
        "branch": "branch",
        "deploy_on_push": "deployOnPush",
        "repo": "repo",
    },
)
class AppSpecServiceGithub:
    def __init__(
        self,
        *,
        branch: typing.Optional[builtins.str] = None,
        deploy_on_push: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: The name of the branch to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        :param deploy_on_push: Whether to automatically deploy new commits made to the repo. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        :param repo: The name of the repo in the format ``owner/repo``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo App#repo}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecServiceGithub.__init__)
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
            check_type(argname="argument deploy_on_push", value=deploy_on_push, expected_type=type_hints["deploy_on_push"])
            check_type(argname="argument repo", value=repo, expected_type=type_hints["repo"])
        self._values: typing.Dict[str, typing.Any] = {}
        if branch is not None:
            self._values["branch"] = branch
        if deploy_on_push is not None:
            self._values["deploy_on_push"] = deploy_on_push
        if repo is not None:
            self._values["repo"] = repo

    @builtins.property
    def branch(self) -> typing.Optional[builtins.str]:
        '''The name of the branch to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        '''
        result = self._values.get("branch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deploy_on_push(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to automatically deploy new commits made to the repo.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        '''
        result = self._values.get("deploy_on_push")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def repo(self) -> typing.Optional[builtins.str]:
        '''The name of the repo in the format ``owner/repo``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo App#repo}
        '''
        result = self._values.get("repo")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecServiceGithub(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecServiceGithubOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceGithubOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecServiceGithubOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBranch")
    def reset_branch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBranch", []))

    @jsii.member(jsii_name="resetDeployOnPush")
    def reset_deploy_on_push(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeployOnPush", []))

    @jsii.member(jsii_name="resetRepo")
    def reset_repo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepo", []))

    @builtins.property
    @jsii.member(jsii_name="branchInput")
    def branch_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "branchInput"))

    @builtins.property
    @jsii.member(jsii_name="deployOnPushInput")
    def deploy_on_push_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deployOnPushInput"))

    @builtins.property
    @jsii.member(jsii_name="repoInput")
    def repo_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repoInput"))

    @builtins.property
    @jsii.member(jsii_name="branch")
    def branch(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "branch"))

    @branch.setter
    def branch(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceGithubOutputReference, "branch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "branch", value)

    @builtins.property
    @jsii.member(jsii_name="deployOnPush")
    def deploy_on_push(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "deployOnPush"))

    @deploy_on_push.setter
    def deploy_on_push(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceGithubOutputReference, "deploy_on_push").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deployOnPush", value)

    @builtins.property
    @jsii.member(jsii_name="repo")
    def repo(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repo"))

    @repo.setter
    def repo(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceGithubOutputReference, "repo").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repo", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecServiceGithub]:
        return typing.cast(typing.Optional[AppSpecServiceGithub], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppSpecServiceGithub]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceGithubOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceGitlab",
    jsii_struct_bases=[],
    name_mapping={
        "branch": "branch",
        "deploy_on_push": "deployOnPush",
        "repo": "repo",
    },
)
class AppSpecServiceGitlab:
    def __init__(
        self,
        *,
        branch: typing.Optional[builtins.str] = None,
        deploy_on_push: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: The name of the branch to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        :param deploy_on_push: Whether to automatically deploy new commits made to the repo. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        :param repo: The name of the repo in the format ``owner/repo``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo App#repo}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecServiceGitlab.__init__)
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
            check_type(argname="argument deploy_on_push", value=deploy_on_push, expected_type=type_hints["deploy_on_push"])
            check_type(argname="argument repo", value=repo, expected_type=type_hints["repo"])
        self._values: typing.Dict[str, typing.Any] = {}
        if branch is not None:
            self._values["branch"] = branch
        if deploy_on_push is not None:
            self._values["deploy_on_push"] = deploy_on_push
        if repo is not None:
            self._values["repo"] = repo

    @builtins.property
    def branch(self) -> typing.Optional[builtins.str]:
        '''The name of the branch to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        '''
        result = self._values.get("branch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deploy_on_push(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to automatically deploy new commits made to the repo.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        '''
        result = self._values.get("deploy_on_push")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def repo(self) -> typing.Optional[builtins.str]:
        '''The name of the repo in the format ``owner/repo``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo App#repo}
        '''
        result = self._values.get("repo")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecServiceGitlab(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecServiceGitlabOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceGitlabOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecServiceGitlabOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBranch")
    def reset_branch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBranch", []))

    @jsii.member(jsii_name="resetDeployOnPush")
    def reset_deploy_on_push(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeployOnPush", []))

    @jsii.member(jsii_name="resetRepo")
    def reset_repo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepo", []))

    @builtins.property
    @jsii.member(jsii_name="branchInput")
    def branch_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "branchInput"))

    @builtins.property
    @jsii.member(jsii_name="deployOnPushInput")
    def deploy_on_push_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deployOnPushInput"))

    @builtins.property
    @jsii.member(jsii_name="repoInput")
    def repo_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repoInput"))

    @builtins.property
    @jsii.member(jsii_name="branch")
    def branch(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "branch"))

    @branch.setter
    def branch(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceGitlabOutputReference, "branch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "branch", value)

    @builtins.property
    @jsii.member(jsii_name="deployOnPush")
    def deploy_on_push(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "deployOnPush"))

    @deploy_on_push.setter
    def deploy_on_push(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceGitlabOutputReference, "deploy_on_push").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deployOnPush", value)

    @builtins.property
    @jsii.member(jsii_name="repo")
    def repo(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repo"))

    @repo.setter
    def repo(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceGitlabOutputReference, "repo").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repo", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecServiceGitlab]:
        return typing.cast(typing.Optional[AppSpecServiceGitlab], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppSpecServiceGitlab]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceGitlabOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceHealthCheck",
    jsii_struct_bases=[],
    name_mapping={
        "failure_threshold": "failureThreshold",
        "http_path": "httpPath",
        "initial_delay_seconds": "initialDelaySeconds",
        "period_seconds": "periodSeconds",
        "success_threshold": "successThreshold",
        "timeout_seconds": "timeoutSeconds",
    },
)
class AppSpecServiceHealthCheck:
    def __init__(
        self,
        *,
        failure_threshold: typing.Optional[jsii.Number] = None,
        http_path: typing.Optional[builtins.str] = None,
        initial_delay_seconds: typing.Optional[jsii.Number] = None,
        period_seconds: typing.Optional[jsii.Number] = None,
        success_threshold: typing.Optional[jsii.Number] = None,
        timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param failure_threshold: The number of failed health checks before considered unhealthy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#failure_threshold App#failure_threshold}
        :param http_path: The route path used for the HTTP health check ping. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#http_path App#http_path}
        :param initial_delay_seconds: The number of seconds to wait before beginning health checks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#initial_delay_seconds App#initial_delay_seconds}
        :param period_seconds: The number of seconds to wait between health checks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#period_seconds App#period_seconds}
        :param success_threshold: The number of successful health checks before considered healthy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#success_threshold App#success_threshold}
        :param timeout_seconds: The number of seconds after which the check times out. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#timeout_seconds App#timeout_seconds}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecServiceHealthCheck.__init__)
            check_type(argname="argument failure_threshold", value=failure_threshold, expected_type=type_hints["failure_threshold"])
            check_type(argname="argument http_path", value=http_path, expected_type=type_hints["http_path"])
            check_type(argname="argument initial_delay_seconds", value=initial_delay_seconds, expected_type=type_hints["initial_delay_seconds"])
            check_type(argname="argument period_seconds", value=period_seconds, expected_type=type_hints["period_seconds"])
            check_type(argname="argument success_threshold", value=success_threshold, expected_type=type_hints["success_threshold"])
            check_type(argname="argument timeout_seconds", value=timeout_seconds, expected_type=type_hints["timeout_seconds"])
        self._values: typing.Dict[str, typing.Any] = {}
        if failure_threshold is not None:
            self._values["failure_threshold"] = failure_threshold
        if http_path is not None:
            self._values["http_path"] = http_path
        if initial_delay_seconds is not None:
            self._values["initial_delay_seconds"] = initial_delay_seconds
        if period_seconds is not None:
            self._values["period_seconds"] = period_seconds
        if success_threshold is not None:
            self._values["success_threshold"] = success_threshold
        if timeout_seconds is not None:
            self._values["timeout_seconds"] = timeout_seconds

    @builtins.property
    def failure_threshold(self) -> typing.Optional[jsii.Number]:
        '''The number of failed health checks before considered unhealthy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#failure_threshold App#failure_threshold}
        '''
        result = self._values.get("failure_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def http_path(self) -> typing.Optional[builtins.str]:
        '''The route path used for the HTTP health check ping.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#http_path App#http_path}
        '''
        result = self._values.get("http_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def initial_delay_seconds(self) -> typing.Optional[jsii.Number]:
        '''The number of seconds to wait before beginning health checks.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#initial_delay_seconds App#initial_delay_seconds}
        '''
        result = self._values.get("initial_delay_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def period_seconds(self) -> typing.Optional[jsii.Number]:
        '''The number of seconds to wait between health checks.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#period_seconds App#period_seconds}
        '''
        result = self._values.get("period_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def success_threshold(self) -> typing.Optional[jsii.Number]:
        '''The number of successful health checks before considered healthy.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#success_threshold App#success_threshold}
        '''
        result = self._values.get("success_threshold")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''The number of seconds after which the check times out.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#timeout_seconds App#timeout_seconds}
        '''
        result = self._values.get("timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecServiceHealthCheck(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecServiceHealthCheckOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceHealthCheckOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecServiceHealthCheckOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetFailureThreshold")
    def reset_failure_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFailureThreshold", []))

    @jsii.member(jsii_name="resetHttpPath")
    def reset_http_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpPath", []))

    @jsii.member(jsii_name="resetInitialDelaySeconds")
    def reset_initial_delay_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitialDelaySeconds", []))

    @jsii.member(jsii_name="resetPeriodSeconds")
    def reset_period_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeriodSeconds", []))

    @jsii.member(jsii_name="resetSuccessThreshold")
    def reset_success_threshold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSuccessThreshold", []))

    @jsii.member(jsii_name="resetTimeoutSeconds")
    def reset_timeout_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeoutSeconds", []))

    @builtins.property
    @jsii.member(jsii_name="failureThresholdInput")
    def failure_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "failureThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="httpPathInput")
    def http_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpPathInput"))

    @builtins.property
    @jsii.member(jsii_name="initialDelaySecondsInput")
    def initial_delay_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "initialDelaySecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="periodSecondsInput")
    def period_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "periodSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="successThresholdInput")
    def success_threshold_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "successThresholdInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutSecondsInput")
    def timeout_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="failureThreshold")
    def failure_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "failureThreshold"))

    @failure_threshold.setter
    def failure_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceHealthCheckOutputReference, "failure_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failureThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="httpPath")
    def http_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpPath"))

    @http_path.setter
    def http_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceHealthCheckOutputReference, "http_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpPath", value)

    @builtins.property
    @jsii.member(jsii_name="initialDelaySeconds")
    def initial_delay_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "initialDelaySeconds"))

    @initial_delay_seconds.setter
    def initial_delay_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceHealthCheckOutputReference, "initial_delay_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initialDelaySeconds", value)

    @builtins.property
    @jsii.member(jsii_name="periodSeconds")
    def period_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "periodSeconds"))

    @period_seconds.setter
    def period_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceHealthCheckOutputReference, "period_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "periodSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="successThreshold")
    def success_threshold(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "successThreshold"))

    @success_threshold.setter
    def success_threshold(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceHealthCheckOutputReference, "success_threshold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "successThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutSeconds")
    def timeout_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "timeoutSeconds"))

    @timeout_seconds.setter
    def timeout_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceHealthCheckOutputReference, "timeout_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecServiceHealthCheck]:
        return typing.cast(typing.Optional[AppSpecServiceHealthCheck], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppSpecServiceHealthCheck]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceHealthCheckOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceImage",
    jsii_struct_bases=[],
    name_mapping={
        "registry_type": "registryType",
        "repository": "repository",
        "deploy_on_push": "deployOnPush",
        "registry": "registry",
        "tag": "tag",
    },
)
class AppSpecServiceImage:
    def __init__(
        self,
        *,
        registry_type: builtins.str,
        repository: builtins.str,
        deploy_on_push: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecServiceImageDeployOnPush", typing.Dict[str, typing.Any]]]]] = None,
        registry: typing.Optional[builtins.str] = None,
        tag: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param registry_type: The registry type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#registry_type App#registry_type}
        :param repository: The repository name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repository App#repository}
        :param deploy_on_push: deploy_on_push block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        :param registry: The registry name. Must be left empty for the DOCR registry type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#registry App#registry}
        :param tag: The repository tag. Defaults to latest if not provided. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#tag App#tag}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecServiceImage.__init__)
            check_type(argname="argument registry_type", value=registry_type, expected_type=type_hints["registry_type"])
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
            check_type(argname="argument deploy_on_push", value=deploy_on_push, expected_type=type_hints["deploy_on_push"])
            check_type(argname="argument registry", value=registry, expected_type=type_hints["registry"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
        self._values: typing.Dict[str, typing.Any] = {
            "registry_type": registry_type,
            "repository": repository,
        }
        if deploy_on_push is not None:
            self._values["deploy_on_push"] = deploy_on_push
        if registry is not None:
            self._values["registry"] = registry
        if tag is not None:
            self._values["tag"] = tag

    @builtins.property
    def registry_type(self) -> builtins.str:
        '''The registry type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#registry_type App#registry_type}
        '''
        result = self._values.get("registry_type")
        assert result is not None, "Required property 'registry_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repository(self) -> builtins.str:
        '''The repository name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repository App#repository}
        '''
        result = self._values.get("repository")
        assert result is not None, "Required property 'repository' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def deploy_on_push(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecServiceImageDeployOnPush"]]]:
        '''deploy_on_push block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        '''
        result = self._values.get("deploy_on_push")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecServiceImageDeployOnPush"]]], result)

    @builtins.property
    def registry(self) -> typing.Optional[builtins.str]:
        '''The registry name. Must be left empty for the DOCR registry type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#registry App#registry}
        '''
        result = self._values.get("registry")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag(self) -> typing.Optional[builtins.str]:
        '''The repository tag. Defaults to latest if not provided.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#tag App#tag}
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecServiceImage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceImageDeployOnPush",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class AppSpecServiceImageDeployOnPush:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Whether to automatically deploy images pushed to DOCR. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#enabled App#enabled}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecServiceImageDeployOnPush.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to automatically deploy images pushed to DOCR.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#enabled App#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecServiceImageDeployOnPush(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecServiceImageDeployOnPushList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceImageDeployOnPushList",
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
            type_hints = typing.get_type_hints(AppSpecServiceImageDeployOnPushList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AppSpecServiceImageDeployOnPushOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecServiceImageDeployOnPushList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppSpecServiceImageDeployOnPushOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceImageDeployOnPushList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecServiceImageDeployOnPushList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecServiceImageDeployOnPushList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecServiceImageDeployOnPush]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecServiceImageDeployOnPush]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecServiceImageDeployOnPush]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceImageDeployOnPushList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecServiceImageDeployOnPushOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceImageDeployOnPushOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecServiceImageDeployOnPushOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceImageDeployOnPushOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppSpecServiceImageDeployOnPush, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppSpecServiceImageDeployOnPush, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppSpecServiceImageDeployOnPush, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceImageDeployOnPushOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecServiceImageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceImageOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecServiceImageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDeployOnPush")
    def put_deploy_on_push(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppSpecServiceImageDeployOnPush, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecServiceImageOutputReference.put_deploy_on_push)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDeployOnPush", [value]))

    @jsii.member(jsii_name="resetDeployOnPush")
    def reset_deploy_on_push(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeployOnPush", []))

    @jsii.member(jsii_name="resetRegistry")
    def reset_registry(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegistry", []))

    @jsii.member(jsii_name="resetTag")
    def reset_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTag", []))

    @builtins.property
    @jsii.member(jsii_name="deployOnPush")
    def deploy_on_push(self) -> AppSpecServiceImageDeployOnPushList:
        return typing.cast(AppSpecServiceImageDeployOnPushList, jsii.get(self, "deployOnPush"))

    @builtins.property
    @jsii.member(jsii_name="deployOnPushInput")
    def deploy_on_push_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecServiceImageDeployOnPush]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecServiceImageDeployOnPush]]], jsii.get(self, "deployOnPushInput"))

    @builtins.property
    @jsii.member(jsii_name="registryInput")
    def registry_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "registryInput"))

    @builtins.property
    @jsii.member(jsii_name="registryTypeInput")
    def registry_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "registryTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="repositoryInput")
    def repository_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repositoryInput"))

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="registry")
    def registry(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registry"))

    @registry.setter
    def registry(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceImageOutputReference, "registry").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registry", value)

    @builtins.property
    @jsii.member(jsii_name="registryType")
    def registry_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registryType"))

    @registry_type.setter
    def registry_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceImageOutputReference, "registry_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registryType", value)

    @builtins.property
    @jsii.member(jsii_name="repository")
    def repository(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repository"))

    @repository.setter
    def repository(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceImageOutputReference, "repository").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repository", value)

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tag"))

    @tag.setter
    def tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceImageOutputReference, "tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tag", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecServiceImage]:
        return typing.cast(typing.Optional[AppSpecServiceImage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppSpecServiceImage]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceImageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecServiceList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceList",
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
            type_hints = typing.get_type_hints(AppSpecServiceList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AppSpecServiceOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecServiceList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppSpecServiceOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecServiceList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecServiceList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecService]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecService]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecService]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceLogDestination",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "datadog": "datadog",
        "logtail": "logtail",
        "papertrail": "papertrail",
    },
)
class AppSpecServiceLogDestination:
    def __init__(
        self,
        *,
        name: builtins.str,
        datadog: typing.Optional[typing.Union["AppSpecServiceLogDestinationDatadog", typing.Dict[str, typing.Any]]] = None,
        logtail: typing.Optional[typing.Union["AppSpecServiceLogDestinationLogtail", typing.Dict[str, typing.Any]]] = None,
        papertrail: typing.Optional[typing.Union["AppSpecServiceLogDestinationPapertrail", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: Name of the log destination. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#name App#name}
        :param datadog: datadog block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#datadog App#datadog}
        :param logtail: logtail block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#logtail App#logtail}
        :param papertrail: papertrail block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#papertrail App#papertrail}
        '''
        if isinstance(datadog, dict):
            datadog = AppSpecServiceLogDestinationDatadog(**datadog)
        if isinstance(logtail, dict):
            logtail = AppSpecServiceLogDestinationLogtail(**logtail)
        if isinstance(papertrail, dict):
            papertrail = AppSpecServiceLogDestinationPapertrail(**papertrail)
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecServiceLogDestination.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument datadog", value=datadog, expected_type=type_hints["datadog"])
            check_type(argname="argument logtail", value=logtail, expected_type=type_hints["logtail"])
            check_type(argname="argument papertrail", value=papertrail, expected_type=type_hints["papertrail"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if datadog is not None:
            self._values["datadog"] = datadog
        if logtail is not None:
            self._values["logtail"] = logtail
        if papertrail is not None:
            self._values["papertrail"] = papertrail

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the log destination.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#name App#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def datadog(self) -> typing.Optional["AppSpecServiceLogDestinationDatadog"]:
        '''datadog block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#datadog App#datadog}
        '''
        result = self._values.get("datadog")
        return typing.cast(typing.Optional["AppSpecServiceLogDestinationDatadog"], result)

    @builtins.property
    def logtail(self) -> typing.Optional["AppSpecServiceLogDestinationLogtail"]:
        '''logtail block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#logtail App#logtail}
        '''
        result = self._values.get("logtail")
        return typing.cast(typing.Optional["AppSpecServiceLogDestinationLogtail"], result)

    @builtins.property
    def papertrail(self) -> typing.Optional["AppSpecServiceLogDestinationPapertrail"]:
        '''papertrail block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#papertrail App#papertrail}
        '''
        result = self._values.get("papertrail")
        return typing.cast(typing.Optional["AppSpecServiceLogDestinationPapertrail"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecServiceLogDestination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceLogDestinationDatadog",
    jsii_struct_bases=[],
    name_mapping={"api_key": "apiKey", "endpoint": "endpoint"},
)
class AppSpecServiceLogDestinationDatadog:
    def __init__(
        self,
        *,
        api_key: builtins.str,
        endpoint: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param api_key: Datadog API key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#api_key App#api_key}
        :param endpoint: Datadog HTTP log intake endpoint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#endpoint App#endpoint}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecServiceLogDestinationDatadog.__init__)
            check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
        self._values: typing.Dict[str, typing.Any] = {
            "api_key": api_key,
        }
        if endpoint is not None:
            self._values["endpoint"] = endpoint

    @builtins.property
    def api_key(self) -> builtins.str:
        '''Datadog API key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#api_key App#api_key}
        '''
        result = self._values.get("api_key")
        assert result is not None, "Required property 'api_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoint(self) -> typing.Optional[builtins.str]:
        '''Datadog HTTP log intake endpoint.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#endpoint App#endpoint}
        '''
        result = self._values.get("endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecServiceLogDestinationDatadog(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecServiceLogDestinationDatadogOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceLogDestinationDatadogOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecServiceLogDestinationDatadogOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEndpoint")
    def reset_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpoint", []))

    @builtins.property
    @jsii.member(jsii_name="apiKeyInput")
    def api_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="apiKey")
    def api_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiKey"))

    @api_key.setter
    def api_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceLogDestinationDatadogOutputReference, "api_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiKey", value)

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceLogDestinationDatadogOutputReference, "endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecServiceLogDestinationDatadog]:
        return typing.cast(typing.Optional[AppSpecServiceLogDestinationDatadog], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppSpecServiceLogDestinationDatadog],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceLogDestinationDatadogOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecServiceLogDestinationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceLogDestinationList",
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
            type_hints = typing.get_type_hints(AppSpecServiceLogDestinationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AppSpecServiceLogDestinationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecServiceLogDestinationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppSpecServiceLogDestinationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceLogDestinationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecServiceLogDestinationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecServiceLogDestinationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecServiceLogDestination]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecServiceLogDestination]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecServiceLogDestination]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceLogDestinationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceLogDestinationLogtail",
    jsii_struct_bases=[],
    name_mapping={"token": "token"},
)
class AppSpecServiceLogDestinationLogtail:
    def __init__(self, *, token: builtins.str) -> None:
        '''
        :param token: Logtail token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#token App#token}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecServiceLogDestinationLogtail.__init__)
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
        self._values: typing.Dict[str, typing.Any] = {
            "token": token,
        }

    @builtins.property
    def token(self) -> builtins.str:
        '''Logtail token.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#token App#token}
        '''
        result = self._values.get("token")
        assert result is not None, "Required property 'token' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecServiceLogDestinationLogtail(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecServiceLogDestinationLogtailOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceLogDestinationLogtailOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecServiceLogDestinationLogtailOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="tokenInput")
    def token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenInput"))

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "token"))

    @token.setter
    def token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceLogDestinationLogtailOutputReference, "token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "token", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecServiceLogDestinationLogtail]:
        return typing.cast(typing.Optional[AppSpecServiceLogDestinationLogtail], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppSpecServiceLogDestinationLogtail],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceLogDestinationLogtailOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecServiceLogDestinationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceLogDestinationOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecServiceLogDestinationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDatadog")
    def put_datadog(
        self,
        *,
        api_key: builtins.str,
        endpoint: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param api_key: Datadog API key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#api_key App#api_key}
        :param endpoint: Datadog HTTP log intake endpoint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#endpoint App#endpoint}
        '''
        value = AppSpecServiceLogDestinationDatadog(api_key=api_key, endpoint=endpoint)

        return typing.cast(None, jsii.invoke(self, "putDatadog", [value]))

    @jsii.member(jsii_name="putLogtail")
    def put_logtail(self, *, token: builtins.str) -> None:
        '''
        :param token: Logtail token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#token App#token}
        '''
        value = AppSpecServiceLogDestinationLogtail(token=token)

        return typing.cast(None, jsii.invoke(self, "putLogtail", [value]))

    @jsii.member(jsii_name="putPapertrail")
    def put_papertrail(self, *, endpoint: builtins.str) -> None:
        '''
        :param endpoint: Papertrail syslog endpoint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#endpoint App#endpoint}
        '''
        value = AppSpecServiceLogDestinationPapertrail(endpoint=endpoint)

        return typing.cast(None, jsii.invoke(self, "putPapertrail", [value]))

    @jsii.member(jsii_name="resetDatadog")
    def reset_datadog(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatadog", []))

    @jsii.member(jsii_name="resetLogtail")
    def reset_logtail(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogtail", []))

    @jsii.member(jsii_name="resetPapertrail")
    def reset_papertrail(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPapertrail", []))

    @builtins.property
    @jsii.member(jsii_name="datadog")
    def datadog(self) -> AppSpecServiceLogDestinationDatadogOutputReference:
        return typing.cast(AppSpecServiceLogDestinationDatadogOutputReference, jsii.get(self, "datadog"))

    @builtins.property
    @jsii.member(jsii_name="logtail")
    def logtail(self) -> AppSpecServiceLogDestinationLogtailOutputReference:
        return typing.cast(AppSpecServiceLogDestinationLogtailOutputReference, jsii.get(self, "logtail"))

    @builtins.property
    @jsii.member(jsii_name="papertrail")
    def papertrail(self) -> "AppSpecServiceLogDestinationPapertrailOutputReference":
        return typing.cast("AppSpecServiceLogDestinationPapertrailOutputReference", jsii.get(self, "papertrail"))

    @builtins.property
    @jsii.member(jsii_name="datadogInput")
    def datadog_input(self) -> typing.Optional[AppSpecServiceLogDestinationDatadog]:
        return typing.cast(typing.Optional[AppSpecServiceLogDestinationDatadog], jsii.get(self, "datadogInput"))

    @builtins.property
    @jsii.member(jsii_name="logtailInput")
    def logtail_input(self) -> typing.Optional[AppSpecServiceLogDestinationLogtail]:
        return typing.cast(typing.Optional[AppSpecServiceLogDestinationLogtail], jsii.get(self, "logtailInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="papertrailInput")
    def papertrail_input(
        self,
    ) -> typing.Optional["AppSpecServiceLogDestinationPapertrail"]:
        return typing.cast(typing.Optional["AppSpecServiceLogDestinationPapertrail"], jsii.get(self, "papertrailInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceLogDestinationOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppSpecServiceLogDestination, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppSpecServiceLogDestination, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppSpecServiceLogDestination, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceLogDestinationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceLogDestinationPapertrail",
    jsii_struct_bases=[],
    name_mapping={"endpoint": "endpoint"},
)
class AppSpecServiceLogDestinationPapertrail:
    def __init__(self, *, endpoint: builtins.str) -> None:
        '''
        :param endpoint: Papertrail syslog endpoint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#endpoint App#endpoint}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecServiceLogDestinationPapertrail.__init__)
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
        self._values: typing.Dict[str, typing.Any] = {
            "endpoint": endpoint,
        }

    @builtins.property
    def endpoint(self) -> builtins.str:
        '''Papertrail syslog endpoint.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#endpoint App#endpoint}
        '''
        result = self._values.get("endpoint")
        assert result is not None, "Required property 'endpoint' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecServiceLogDestinationPapertrail(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecServiceLogDestinationPapertrailOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceLogDestinationPapertrailOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecServiceLogDestinationPapertrailOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceLogDestinationPapertrailOutputReference, "endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecServiceLogDestinationPapertrail]:
        return typing.cast(typing.Optional[AppSpecServiceLogDestinationPapertrail], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppSpecServiceLogDestinationPapertrail],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceLogDestinationPapertrailOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecServiceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecServiceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAlert")
    def put_alert(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppSpecServiceAlert, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecServiceOutputReference.put_alert)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAlert", [value]))

    @jsii.member(jsii_name="putCors")
    def put_cors(
        self,
        *,
        allow_credentials: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_methods: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_origins: typing.Optional[typing.Union[AppSpecServiceCorsAllowOrigins, typing.Dict[str, typing.Any]]] = None,
        expose_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        max_age: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allow_credentials: Whether browsers should expose the response to the client-side JavaScript code when the request’s credentials mode is ``include``. This configures the Access-Control-Allow-Credentials header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_credentials App#allow_credentials}
        :param allow_headers: The set of allowed HTTP request headers. This configures the Access-Control-Allow-Headers header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_headers App#allow_headers}
        :param allow_methods: The set of allowed HTTP methods. This configures the Access-Control-Allow-Methods header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_methods App#allow_methods}
        :param allow_origins: allow_origins block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_origins App#allow_origins}
        :param expose_headers: The set of HTTP response headers that browsers are allowed to access. This configures the Access-Control-Expose-Headers header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#expose_headers App#expose_headers}
        :param max_age: An optional duration specifying how long browsers can cache the results of a preflight request. This configures the Access-Control-Max-Age header. Example: ``5h30m``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#max_age App#max_age}
        '''
        value = AppSpecServiceCors(
            allow_credentials=allow_credentials,
            allow_headers=allow_headers,
            allow_methods=allow_methods,
            allow_origins=allow_origins,
            expose_headers=expose_headers,
            max_age=max_age,
        )

        return typing.cast(None, jsii.invoke(self, "putCors", [value]))

    @jsii.member(jsii_name="putEnv")
    def put_env(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppSpecServiceEnv, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecServiceOutputReference.put_env)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEnv", [value]))

    @jsii.member(jsii_name="putGit")
    def put_git(
        self,
        *,
        branch: typing.Optional[builtins.str] = None,
        repo_clone_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: The name of the branch to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        :param repo_clone_url: The clone URL of the repo. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo_clone_url App#repo_clone_url}
        '''
        value = AppSpecServiceGit(branch=branch, repo_clone_url=repo_clone_url)

        return typing.cast(None, jsii.invoke(self, "putGit", [value]))

    @jsii.member(jsii_name="putGithub")
    def put_github(
        self,
        *,
        branch: typing.Optional[builtins.str] = None,
        deploy_on_push: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: The name of the branch to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        :param deploy_on_push: Whether to automatically deploy new commits made to the repo. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        :param repo: The name of the repo in the format ``owner/repo``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo App#repo}
        '''
        value = AppSpecServiceGithub(
            branch=branch, deploy_on_push=deploy_on_push, repo=repo
        )

        return typing.cast(None, jsii.invoke(self, "putGithub", [value]))

    @jsii.member(jsii_name="putGitlab")
    def put_gitlab(
        self,
        *,
        branch: typing.Optional[builtins.str] = None,
        deploy_on_push: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: The name of the branch to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        :param deploy_on_push: Whether to automatically deploy new commits made to the repo. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        :param repo: The name of the repo in the format ``owner/repo``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo App#repo}
        '''
        value = AppSpecServiceGitlab(
            branch=branch, deploy_on_push=deploy_on_push, repo=repo
        )

        return typing.cast(None, jsii.invoke(self, "putGitlab", [value]))

    @jsii.member(jsii_name="putHealthCheck")
    def put_health_check(
        self,
        *,
        failure_threshold: typing.Optional[jsii.Number] = None,
        http_path: typing.Optional[builtins.str] = None,
        initial_delay_seconds: typing.Optional[jsii.Number] = None,
        period_seconds: typing.Optional[jsii.Number] = None,
        success_threshold: typing.Optional[jsii.Number] = None,
        timeout_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param failure_threshold: The number of failed health checks before considered unhealthy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#failure_threshold App#failure_threshold}
        :param http_path: The route path used for the HTTP health check ping. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#http_path App#http_path}
        :param initial_delay_seconds: The number of seconds to wait before beginning health checks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#initial_delay_seconds App#initial_delay_seconds}
        :param period_seconds: The number of seconds to wait between health checks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#period_seconds App#period_seconds}
        :param success_threshold: The number of successful health checks before considered healthy. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#success_threshold App#success_threshold}
        :param timeout_seconds: The number of seconds after which the check times out. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#timeout_seconds App#timeout_seconds}
        '''
        value = AppSpecServiceHealthCheck(
            failure_threshold=failure_threshold,
            http_path=http_path,
            initial_delay_seconds=initial_delay_seconds,
            period_seconds=period_seconds,
            success_threshold=success_threshold,
            timeout_seconds=timeout_seconds,
        )

        return typing.cast(None, jsii.invoke(self, "putHealthCheck", [value]))

    @jsii.member(jsii_name="putImage")
    def put_image(
        self,
        *,
        registry_type: builtins.str,
        repository: builtins.str,
        deploy_on_push: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppSpecServiceImageDeployOnPush, typing.Dict[str, typing.Any]]]]] = None,
        registry: typing.Optional[builtins.str] = None,
        tag: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param registry_type: The registry type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#registry_type App#registry_type}
        :param repository: The repository name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repository App#repository}
        :param deploy_on_push: deploy_on_push block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        :param registry: The registry name. Must be left empty for the DOCR registry type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#registry App#registry}
        :param tag: The repository tag. Defaults to latest if not provided. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#tag App#tag}
        '''
        value = AppSpecServiceImage(
            registry_type=registry_type,
            repository=repository,
            deploy_on_push=deploy_on_push,
            registry=registry,
            tag=tag,
        )

        return typing.cast(None, jsii.invoke(self, "putImage", [value]))

    @jsii.member(jsii_name="putLogDestination")
    def put_log_destination(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppSpecServiceLogDestination, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecServiceOutputReference.put_log_destination)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLogDestination", [value]))

    @jsii.member(jsii_name="putRoutes")
    def put_routes(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecServiceRoutes", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecServiceOutputReference.put_routes)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRoutes", [value]))

    @jsii.member(jsii_name="resetAlert")
    def reset_alert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlert", []))

    @jsii.member(jsii_name="resetBuildCommand")
    def reset_build_command(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildCommand", []))

    @jsii.member(jsii_name="resetCors")
    def reset_cors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCors", []))

    @jsii.member(jsii_name="resetDockerfilePath")
    def reset_dockerfile_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDockerfilePath", []))

    @jsii.member(jsii_name="resetEnv")
    def reset_env(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnv", []))

    @jsii.member(jsii_name="resetEnvironmentSlug")
    def reset_environment_slug(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnvironmentSlug", []))

    @jsii.member(jsii_name="resetGit")
    def reset_git(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGit", []))

    @jsii.member(jsii_name="resetGithub")
    def reset_github(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGithub", []))

    @jsii.member(jsii_name="resetGitlab")
    def reset_gitlab(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGitlab", []))

    @jsii.member(jsii_name="resetHealthCheck")
    def reset_health_check(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHealthCheck", []))

    @jsii.member(jsii_name="resetHttpPort")
    def reset_http_port(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpPort", []))

    @jsii.member(jsii_name="resetImage")
    def reset_image(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImage", []))

    @jsii.member(jsii_name="resetInstanceCount")
    def reset_instance_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceCount", []))

    @jsii.member(jsii_name="resetInstanceSizeSlug")
    def reset_instance_size_slug(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceSizeSlug", []))

    @jsii.member(jsii_name="resetInternalPorts")
    def reset_internal_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInternalPorts", []))

    @jsii.member(jsii_name="resetLogDestination")
    def reset_log_destination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogDestination", []))

    @jsii.member(jsii_name="resetRoutes")
    def reset_routes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoutes", []))

    @jsii.member(jsii_name="resetRunCommand")
    def reset_run_command(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRunCommand", []))

    @jsii.member(jsii_name="resetSourceDir")
    def reset_source_dir(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceDir", []))

    @builtins.property
    @jsii.member(jsii_name="alert")
    def alert(self) -> AppSpecServiceAlertList:
        return typing.cast(AppSpecServiceAlertList, jsii.get(self, "alert"))

    @builtins.property
    @jsii.member(jsii_name="cors")
    def cors(self) -> AppSpecServiceCorsOutputReference:
        return typing.cast(AppSpecServiceCorsOutputReference, jsii.get(self, "cors"))

    @builtins.property
    @jsii.member(jsii_name="env")
    def env(self) -> AppSpecServiceEnvList:
        return typing.cast(AppSpecServiceEnvList, jsii.get(self, "env"))

    @builtins.property
    @jsii.member(jsii_name="git")
    def git(self) -> AppSpecServiceGitOutputReference:
        return typing.cast(AppSpecServiceGitOutputReference, jsii.get(self, "git"))

    @builtins.property
    @jsii.member(jsii_name="github")
    def github(self) -> AppSpecServiceGithubOutputReference:
        return typing.cast(AppSpecServiceGithubOutputReference, jsii.get(self, "github"))

    @builtins.property
    @jsii.member(jsii_name="gitlab")
    def gitlab(self) -> AppSpecServiceGitlabOutputReference:
        return typing.cast(AppSpecServiceGitlabOutputReference, jsii.get(self, "gitlab"))

    @builtins.property
    @jsii.member(jsii_name="healthCheck")
    def health_check(self) -> AppSpecServiceHealthCheckOutputReference:
        return typing.cast(AppSpecServiceHealthCheckOutputReference, jsii.get(self, "healthCheck"))

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> AppSpecServiceImageOutputReference:
        return typing.cast(AppSpecServiceImageOutputReference, jsii.get(self, "image"))

    @builtins.property
    @jsii.member(jsii_name="logDestination")
    def log_destination(self) -> AppSpecServiceLogDestinationList:
        return typing.cast(AppSpecServiceLogDestinationList, jsii.get(self, "logDestination"))

    @builtins.property
    @jsii.member(jsii_name="routes")
    def routes(self) -> "AppSpecServiceRoutesList":
        return typing.cast("AppSpecServiceRoutesList", jsii.get(self, "routes"))

    @builtins.property
    @jsii.member(jsii_name="alertInput")
    def alert_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecServiceAlert]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecServiceAlert]]], jsii.get(self, "alertInput"))

    @builtins.property
    @jsii.member(jsii_name="buildCommandInput")
    def build_command_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "buildCommandInput"))

    @builtins.property
    @jsii.member(jsii_name="corsInput")
    def cors_input(self) -> typing.Optional[AppSpecServiceCors]:
        return typing.cast(typing.Optional[AppSpecServiceCors], jsii.get(self, "corsInput"))

    @builtins.property
    @jsii.member(jsii_name="dockerfilePathInput")
    def dockerfile_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dockerfilePathInput"))

    @builtins.property
    @jsii.member(jsii_name="envInput")
    def env_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecServiceEnv]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecServiceEnv]]], jsii.get(self, "envInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentSlugInput")
    def environment_slug_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentSlugInput"))

    @builtins.property
    @jsii.member(jsii_name="githubInput")
    def github_input(self) -> typing.Optional[AppSpecServiceGithub]:
        return typing.cast(typing.Optional[AppSpecServiceGithub], jsii.get(self, "githubInput"))

    @builtins.property
    @jsii.member(jsii_name="gitInput")
    def git_input(self) -> typing.Optional[AppSpecServiceGit]:
        return typing.cast(typing.Optional[AppSpecServiceGit], jsii.get(self, "gitInput"))

    @builtins.property
    @jsii.member(jsii_name="gitlabInput")
    def gitlab_input(self) -> typing.Optional[AppSpecServiceGitlab]:
        return typing.cast(typing.Optional[AppSpecServiceGitlab], jsii.get(self, "gitlabInput"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckInput")
    def health_check_input(self) -> typing.Optional[AppSpecServiceHealthCheck]:
        return typing.cast(typing.Optional[AppSpecServiceHealthCheck], jsii.get(self, "healthCheckInput"))

    @builtins.property
    @jsii.member(jsii_name="httpPortInput")
    def http_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "httpPortInput"))

    @builtins.property
    @jsii.member(jsii_name="imageInput")
    def image_input(self) -> typing.Optional[AppSpecServiceImage]:
        return typing.cast(typing.Optional[AppSpecServiceImage], jsii.get(self, "imageInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceCountInput")
    def instance_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "instanceCountInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceSizeSlugInput")
    def instance_size_slug_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceSizeSlugInput"))

    @builtins.property
    @jsii.member(jsii_name="internalPortsInput")
    def internal_ports_input(self) -> typing.Optional[typing.List[jsii.Number]]:
        return typing.cast(typing.Optional[typing.List[jsii.Number]], jsii.get(self, "internalPortsInput"))

    @builtins.property
    @jsii.member(jsii_name="logDestinationInput")
    def log_destination_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecServiceLogDestination]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecServiceLogDestination]]], jsii.get(self, "logDestinationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="routesInput")
    def routes_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecServiceRoutes"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecServiceRoutes"]]], jsii.get(self, "routesInput"))

    @builtins.property
    @jsii.member(jsii_name="runCommandInput")
    def run_command_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runCommandInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceDirInput")
    def source_dir_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceDirInput"))

    @builtins.property
    @jsii.member(jsii_name="buildCommand")
    def build_command(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "buildCommand"))

    @build_command.setter
    def build_command(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceOutputReference, "build_command").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buildCommand", value)

    @builtins.property
    @jsii.member(jsii_name="dockerfilePath")
    def dockerfile_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dockerfilePath"))

    @dockerfile_path.setter
    def dockerfile_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceOutputReference, "dockerfile_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dockerfilePath", value)

    @builtins.property
    @jsii.member(jsii_name="environmentSlug")
    def environment_slug(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "environmentSlug"))

    @environment_slug.setter
    def environment_slug(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceOutputReference, "environment_slug").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentSlug", value)

    @builtins.property
    @jsii.member(jsii_name="httpPort")
    def http_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "httpPort"))

    @http_port.setter
    def http_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceOutputReference, "http_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpPort", value)

    @builtins.property
    @jsii.member(jsii_name="instanceCount")
    def instance_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instanceCount"))

    @instance_count.setter
    def instance_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceOutputReference, "instance_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceCount", value)

    @builtins.property
    @jsii.member(jsii_name="instanceSizeSlug")
    def instance_size_slug(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceSizeSlug"))

    @instance_size_slug.setter
    def instance_size_slug(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceOutputReference, "instance_size_slug").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceSizeSlug", value)

    @builtins.property
    @jsii.member(jsii_name="internalPorts")
    def internal_ports(self) -> typing.List[jsii.Number]:
        return typing.cast(typing.List[jsii.Number], jsii.get(self, "internalPorts"))

    @internal_ports.setter
    def internal_ports(self, value: typing.List[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceOutputReference, "internal_ports").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalPorts", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="runCommand")
    def run_command(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runCommand"))

    @run_command.setter
    def run_command(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceOutputReference, "run_command").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runCommand", value)

    @builtins.property
    @jsii.member(jsii_name="sourceDir")
    def source_dir(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceDir"))

    @source_dir.setter
    def source_dir(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceOutputReference, "source_dir").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceDir", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppSpecService, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppSpecService, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppSpecService, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceRoutes",
    jsii_struct_bases=[],
    name_mapping={"path": "path", "preserve_path_prefix": "preservePathPrefix"},
)
class AppSpecServiceRoutes:
    def __init__(
        self,
        *,
        path: typing.Optional[builtins.str] = None,
        preserve_path_prefix: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param path: Path specifies an route by HTTP path prefix. Paths must start with / and must be unique within the app. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#path App#path}
        :param preserve_path_prefix: An optional flag to preserve the path that is forwarded to the backend service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#preserve_path_prefix App#preserve_path_prefix}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecServiceRoutes.__init__)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument preserve_path_prefix", value=preserve_path_prefix, expected_type=type_hints["preserve_path_prefix"])
        self._values: typing.Dict[str, typing.Any] = {}
        if path is not None:
            self._values["path"] = path
        if preserve_path_prefix is not None:
            self._values["preserve_path_prefix"] = preserve_path_prefix

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Path specifies an route by HTTP path prefix.

        Paths must start with / and must be unique within the app.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#path App#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preserve_path_prefix(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''An optional flag to preserve the path that is forwarded to the backend service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#preserve_path_prefix App#preserve_path_prefix}
        '''
        result = self._values.get("preserve_path_prefix")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecServiceRoutes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecServiceRoutesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceRoutesList",
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
            type_hints = typing.get_type_hints(AppSpecServiceRoutesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AppSpecServiceRoutesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecServiceRoutesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppSpecServiceRoutesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceRoutesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecServiceRoutesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecServiceRoutesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecServiceRoutes]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecServiceRoutes]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecServiceRoutes]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceRoutesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecServiceRoutesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecServiceRoutesOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecServiceRoutesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetPreservePathPrefix")
    def reset_preserve_path_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreservePathPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="preservePathPrefixInput")
    def preserve_path_prefix_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "preservePathPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceRoutesOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="preservePathPrefix")
    def preserve_path_prefix(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "preservePathPrefix"))

    @preserve_path_prefix.setter
    def preserve_path_prefix(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceRoutesOutputReference, "preserve_path_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preservePathPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppSpecServiceRoutes, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppSpecServiceRoutes, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppSpecServiceRoutes, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecServiceRoutesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecStaticSite",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "build_command": "buildCommand",
        "catchall_document": "catchallDocument",
        "cors": "cors",
        "dockerfile_path": "dockerfilePath",
        "env": "env",
        "environment_slug": "environmentSlug",
        "error_document": "errorDocument",
        "git": "git",
        "github": "github",
        "gitlab": "gitlab",
        "index_document": "indexDocument",
        "output_dir": "outputDir",
        "routes": "routes",
        "source_dir": "sourceDir",
    },
)
class AppSpecStaticSite:
    def __init__(
        self,
        *,
        name: builtins.str,
        build_command: typing.Optional[builtins.str] = None,
        catchall_document: typing.Optional[builtins.str] = None,
        cors: typing.Optional[typing.Union["AppSpecStaticSiteCors", typing.Dict[str, typing.Any]]] = None,
        dockerfile_path: typing.Optional[builtins.str] = None,
        env: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecStaticSiteEnv", typing.Dict[str, typing.Any]]]]] = None,
        environment_slug: typing.Optional[builtins.str] = None,
        error_document: typing.Optional[builtins.str] = None,
        git: typing.Optional[typing.Union["AppSpecStaticSiteGit", typing.Dict[str, typing.Any]]] = None,
        github: typing.Optional[typing.Union["AppSpecStaticSiteGithub", typing.Dict[str, typing.Any]]] = None,
        gitlab: typing.Optional[typing.Union["AppSpecStaticSiteGitlab", typing.Dict[str, typing.Any]]] = None,
        index_document: typing.Optional[builtins.str] = None,
        output_dir: typing.Optional[builtins.str] = None,
        routes: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecStaticSiteRoutes", typing.Dict[str, typing.Any]]]]] = None,
        source_dir: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: The name of the component. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#name App#name}
        :param build_command: An optional build command to run while building this component from source. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#build_command App#build_command}
        :param catchall_document: The name of the document to use as the fallback for any requests to documents that are not found when serving this static site. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#catchall_document App#catchall_document}
        :param cors: cors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#cors App#cors}
        :param dockerfile_path: The path to a Dockerfile relative to the root of the repo. If set, overrides usage of buildpacks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#dockerfile_path App#dockerfile_path}
        :param env: env block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#env App#env}
        :param environment_slug: An environment slug describing the type of this app. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#environment_slug App#environment_slug}
        :param error_document: The name of the error document to use when serving this static site. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#error_document App#error_document}
        :param git: git block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#git App#git}
        :param github: github block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#github App#github}
        :param gitlab: gitlab block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#gitlab App#gitlab}
        :param index_document: The name of the index document to use when serving this static site. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#index_document App#index_document}
        :param output_dir: An optional path to where the built assets will be located, relative to the build context. If not set, App Platform will automatically scan for these directory names: ``_static``, ``dist``, ``public``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#output_dir App#output_dir}
        :param routes: routes block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#routes App#routes}
        :param source_dir: An optional path to the working directory to use for the build. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#source_dir App#source_dir}
        '''
        if isinstance(cors, dict):
            cors = AppSpecStaticSiteCors(**cors)
        if isinstance(git, dict):
            git = AppSpecStaticSiteGit(**git)
        if isinstance(github, dict):
            github = AppSpecStaticSiteGithub(**github)
        if isinstance(gitlab, dict):
            gitlab = AppSpecStaticSiteGitlab(**gitlab)
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecStaticSite.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument build_command", value=build_command, expected_type=type_hints["build_command"])
            check_type(argname="argument catchall_document", value=catchall_document, expected_type=type_hints["catchall_document"])
            check_type(argname="argument cors", value=cors, expected_type=type_hints["cors"])
            check_type(argname="argument dockerfile_path", value=dockerfile_path, expected_type=type_hints["dockerfile_path"])
            check_type(argname="argument env", value=env, expected_type=type_hints["env"])
            check_type(argname="argument environment_slug", value=environment_slug, expected_type=type_hints["environment_slug"])
            check_type(argname="argument error_document", value=error_document, expected_type=type_hints["error_document"])
            check_type(argname="argument git", value=git, expected_type=type_hints["git"])
            check_type(argname="argument github", value=github, expected_type=type_hints["github"])
            check_type(argname="argument gitlab", value=gitlab, expected_type=type_hints["gitlab"])
            check_type(argname="argument index_document", value=index_document, expected_type=type_hints["index_document"])
            check_type(argname="argument output_dir", value=output_dir, expected_type=type_hints["output_dir"])
            check_type(argname="argument routes", value=routes, expected_type=type_hints["routes"])
            check_type(argname="argument source_dir", value=source_dir, expected_type=type_hints["source_dir"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if build_command is not None:
            self._values["build_command"] = build_command
        if catchall_document is not None:
            self._values["catchall_document"] = catchall_document
        if cors is not None:
            self._values["cors"] = cors
        if dockerfile_path is not None:
            self._values["dockerfile_path"] = dockerfile_path
        if env is not None:
            self._values["env"] = env
        if environment_slug is not None:
            self._values["environment_slug"] = environment_slug
        if error_document is not None:
            self._values["error_document"] = error_document
        if git is not None:
            self._values["git"] = git
        if github is not None:
            self._values["github"] = github
        if gitlab is not None:
            self._values["gitlab"] = gitlab
        if index_document is not None:
            self._values["index_document"] = index_document
        if output_dir is not None:
            self._values["output_dir"] = output_dir
        if routes is not None:
            self._values["routes"] = routes
        if source_dir is not None:
            self._values["source_dir"] = source_dir

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the component.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#name App#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def build_command(self) -> typing.Optional[builtins.str]:
        '''An optional build command to run while building this component from source.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#build_command App#build_command}
        '''
        result = self._values.get("build_command")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def catchall_document(self) -> typing.Optional[builtins.str]:
        '''The name of the document to use as the fallback for any requests to documents that are not found when serving this static site.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#catchall_document App#catchall_document}
        '''
        result = self._values.get("catchall_document")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cors(self) -> typing.Optional["AppSpecStaticSiteCors"]:
        '''cors block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#cors App#cors}
        '''
        result = self._values.get("cors")
        return typing.cast(typing.Optional["AppSpecStaticSiteCors"], result)

    @builtins.property
    def dockerfile_path(self) -> typing.Optional[builtins.str]:
        '''The path to a Dockerfile relative to the root of the repo. If set, overrides usage of buildpacks.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#dockerfile_path App#dockerfile_path}
        '''
        result = self._values.get("dockerfile_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def env(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecStaticSiteEnv"]]]:
        '''env block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#env App#env}
        '''
        result = self._values.get("env")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecStaticSiteEnv"]]], result)

    @builtins.property
    def environment_slug(self) -> typing.Optional[builtins.str]:
        '''An environment slug describing the type of this app.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#environment_slug App#environment_slug}
        '''
        result = self._values.get("environment_slug")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def error_document(self) -> typing.Optional[builtins.str]:
        '''The name of the error document to use when serving this static site.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#error_document App#error_document}
        '''
        result = self._values.get("error_document")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def git(self) -> typing.Optional["AppSpecStaticSiteGit"]:
        '''git block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#git App#git}
        '''
        result = self._values.get("git")
        return typing.cast(typing.Optional["AppSpecStaticSiteGit"], result)

    @builtins.property
    def github(self) -> typing.Optional["AppSpecStaticSiteGithub"]:
        '''github block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#github App#github}
        '''
        result = self._values.get("github")
        return typing.cast(typing.Optional["AppSpecStaticSiteGithub"], result)

    @builtins.property
    def gitlab(self) -> typing.Optional["AppSpecStaticSiteGitlab"]:
        '''gitlab block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#gitlab App#gitlab}
        '''
        result = self._values.get("gitlab")
        return typing.cast(typing.Optional["AppSpecStaticSiteGitlab"], result)

    @builtins.property
    def index_document(self) -> typing.Optional[builtins.str]:
        '''The name of the index document to use when serving this static site.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#index_document App#index_document}
        '''
        result = self._values.get("index_document")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def output_dir(self) -> typing.Optional[builtins.str]:
        '''An optional path to where the built assets will be located, relative to the build context.

        If not set, App Platform will automatically scan for these directory names: ``_static``, ``dist``, ``public``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#output_dir App#output_dir}
        '''
        result = self._values.get("output_dir")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def routes(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecStaticSiteRoutes"]]]:
        '''routes block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#routes App#routes}
        '''
        result = self._values.get("routes")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecStaticSiteRoutes"]]], result)

    @builtins.property
    def source_dir(self) -> typing.Optional[builtins.str]:
        '''An optional path to the working directory to use for the build.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#source_dir App#source_dir}
        '''
        result = self._values.get("source_dir")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecStaticSite(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecStaticSiteCors",
    jsii_struct_bases=[],
    name_mapping={
        "allow_credentials": "allowCredentials",
        "allow_headers": "allowHeaders",
        "allow_methods": "allowMethods",
        "allow_origins": "allowOrigins",
        "expose_headers": "exposeHeaders",
        "max_age": "maxAge",
    },
)
class AppSpecStaticSiteCors:
    def __init__(
        self,
        *,
        allow_credentials: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_methods: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_origins: typing.Optional[typing.Union["AppSpecStaticSiteCorsAllowOrigins", typing.Dict[str, typing.Any]]] = None,
        expose_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        max_age: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allow_credentials: Whether browsers should expose the response to the client-side JavaScript code when the request’s credentials mode is ``include``. This configures the Access-Control-Allow-Credentials header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_credentials App#allow_credentials}
        :param allow_headers: The set of allowed HTTP request headers. This configures the Access-Control-Allow-Headers header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_headers App#allow_headers}
        :param allow_methods: The set of allowed HTTP methods. This configures the Access-Control-Allow-Methods header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_methods App#allow_methods}
        :param allow_origins: allow_origins block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_origins App#allow_origins}
        :param expose_headers: The set of HTTP response headers that browsers are allowed to access. This configures the Access-Control-Expose-Headers header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#expose_headers App#expose_headers}
        :param max_age: An optional duration specifying how long browsers can cache the results of a preflight request. This configures the Access-Control-Max-Age header. Example: ``5h30m``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#max_age App#max_age}
        '''
        if isinstance(allow_origins, dict):
            allow_origins = AppSpecStaticSiteCorsAllowOrigins(**allow_origins)
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecStaticSiteCors.__init__)
            check_type(argname="argument allow_credentials", value=allow_credentials, expected_type=type_hints["allow_credentials"])
            check_type(argname="argument allow_headers", value=allow_headers, expected_type=type_hints["allow_headers"])
            check_type(argname="argument allow_methods", value=allow_methods, expected_type=type_hints["allow_methods"])
            check_type(argname="argument allow_origins", value=allow_origins, expected_type=type_hints["allow_origins"])
            check_type(argname="argument expose_headers", value=expose_headers, expected_type=type_hints["expose_headers"])
            check_type(argname="argument max_age", value=max_age, expected_type=type_hints["max_age"])
        self._values: typing.Dict[str, typing.Any] = {}
        if allow_credentials is not None:
            self._values["allow_credentials"] = allow_credentials
        if allow_headers is not None:
            self._values["allow_headers"] = allow_headers
        if allow_methods is not None:
            self._values["allow_methods"] = allow_methods
        if allow_origins is not None:
            self._values["allow_origins"] = allow_origins
        if expose_headers is not None:
            self._values["expose_headers"] = expose_headers
        if max_age is not None:
            self._values["max_age"] = max_age

    @builtins.property
    def allow_credentials(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether browsers should expose the response to the client-side JavaScript code when the request’s credentials mode is ``include``.

        This configures the Access-Control-Allow-Credentials header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_credentials App#allow_credentials}
        '''
        result = self._values.get("allow_credentials")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The set of allowed HTTP request headers. This configures the Access-Control-Allow-Headers header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_headers App#allow_headers}
        '''
        result = self._values.get("allow_headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allow_methods(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The set of allowed HTTP methods. This configures the Access-Control-Allow-Methods header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_methods App#allow_methods}
        '''
        result = self._values.get("allow_methods")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def allow_origins(self) -> typing.Optional["AppSpecStaticSiteCorsAllowOrigins"]:
        '''allow_origins block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_origins App#allow_origins}
        '''
        result = self._values.get("allow_origins")
        return typing.cast(typing.Optional["AppSpecStaticSiteCorsAllowOrigins"], result)

    @builtins.property
    def expose_headers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The set of HTTP response headers that browsers are allowed to access. This configures the Access-Control-Expose-Headers header.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#expose_headers App#expose_headers}
        '''
        result = self._values.get("expose_headers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def max_age(self) -> typing.Optional[builtins.str]:
        '''An optional duration specifying how long browsers can cache the results of a preflight request.

        This configures the Access-Control-Max-Age header. Example: ``5h30m``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#max_age App#max_age}
        '''
        result = self._values.get("max_age")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecStaticSiteCors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecStaticSiteCorsAllowOrigins",
    jsii_struct_bases=[],
    name_mapping={"exact": "exact", "prefix": "prefix", "regex": "regex"},
)
class AppSpecStaticSiteCorsAllowOrigins:
    def __init__(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        regex: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param exact: Exact string match. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#exact App#exact}
        :param prefix: Prefix-based match. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#prefix App#prefix}
        :param regex: RE2 style regex-based match. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#regex App#regex}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecStaticSiteCorsAllowOrigins.__init__)
            check_type(argname="argument exact", value=exact, expected_type=type_hints["exact"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
            check_type(argname="argument regex", value=regex, expected_type=type_hints["regex"])
        self._values: typing.Dict[str, typing.Any] = {}
        if exact is not None:
            self._values["exact"] = exact
        if prefix is not None:
            self._values["prefix"] = prefix
        if regex is not None:
            self._values["regex"] = regex

    @builtins.property
    def exact(self) -> typing.Optional[builtins.str]:
        '''Exact string match.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#exact App#exact}
        '''
        result = self._values.get("exact")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''Prefix-based match.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#prefix App#prefix}
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def regex(self) -> typing.Optional[builtins.str]:
        '''RE2 style regex-based match.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#regex App#regex}
        '''
        result = self._values.get("regex")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecStaticSiteCorsAllowOrigins(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecStaticSiteCorsAllowOriginsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecStaticSiteCorsAllowOriginsOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecStaticSiteCorsAllowOriginsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExact")
    def reset_exact(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExact", []))

    @jsii.member(jsii_name="resetPrefix")
    def reset_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrefix", []))

    @jsii.member(jsii_name="resetRegex")
    def reset_regex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegex", []))

    @builtins.property
    @jsii.member(jsii_name="exactInput")
    def exact_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "exactInput"))

    @builtins.property
    @jsii.member(jsii_name="prefixInput")
    def prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "prefixInput"))

    @builtins.property
    @jsii.member(jsii_name="regexInput")
    def regex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regexInput"))

    @builtins.property
    @jsii.member(jsii_name="exact")
    def exact(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "exact"))

    @exact.setter
    def exact(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteCorsAllowOriginsOutputReference, "exact").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exact", value)

    @builtins.property
    @jsii.member(jsii_name="prefix")
    def prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "prefix"))

    @prefix.setter
    def prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteCorsAllowOriginsOutputReference, "prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "prefix", value)

    @builtins.property
    @jsii.member(jsii_name="regex")
    def regex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "regex"))

    @regex.setter
    def regex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteCorsAllowOriginsOutputReference, "regex").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "regex", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecStaticSiteCorsAllowOrigins]:
        return typing.cast(typing.Optional[AppSpecStaticSiteCorsAllowOrigins], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppSpecStaticSiteCorsAllowOrigins],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteCorsAllowOriginsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecStaticSiteCorsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecStaticSiteCorsOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecStaticSiteCorsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAllowOrigins")
    def put_allow_origins(
        self,
        *,
        exact: typing.Optional[builtins.str] = None,
        prefix: typing.Optional[builtins.str] = None,
        regex: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param exact: Exact string match. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#exact App#exact}
        :param prefix: Prefix-based match. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#prefix App#prefix}
        :param regex: RE2 style regex-based match. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#regex App#regex}
        '''
        value = AppSpecStaticSiteCorsAllowOrigins(
            exact=exact, prefix=prefix, regex=regex
        )

        return typing.cast(None, jsii.invoke(self, "putAllowOrigins", [value]))

    @jsii.member(jsii_name="resetAllowCredentials")
    def reset_allow_credentials(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowCredentials", []))

    @jsii.member(jsii_name="resetAllowHeaders")
    def reset_allow_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowHeaders", []))

    @jsii.member(jsii_name="resetAllowMethods")
    def reset_allow_methods(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowMethods", []))

    @jsii.member(jsii_name="resetAllowOrigins")
    def reset_allow_origins(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowOrigins", []))

    @jsii.member(jsii_name="resetExposeHeaders")
    def reset_expose_headers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExposeHeaders", []))

    @jsii.member(jsii_name="resetMaxAge")
    def reset_max_age(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxAge", []))

    @builtins.property
    @jsii.member(jsii_name="allowOrigins")
    def allow_origins(self) -> AppSpecStaticSiteCorsAllowOriginsOutputReference:
        return typing.cast(AppSpecStaticSiteCorsAllowOriginsOutputReference, jsii.get(self, "allowOrigins"))

    @builtins.property
    @jsii.member(jsii_name="allowCredentialsInput")
    def allow_credentials_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowCredentialsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowHeadersInput")
    def allow_headers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="allowMethodsInput")
    def allow_methods_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "allowMethodsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowOriginsInput")
    def allow_origins_input(self) -> typing.Optional[AppSpecStaticSiteCorsAllowOrigins]:
        return typing.cast(typing.Optional[AppSpecStaticSiteCorsAllowOrigins], jsii.get(self, "allowOriginsInput"))

    @builtins.property
    @jsii.member(jsii_name="exposeHeadersInput")
    def expose_headers_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "exposeHeadersInput"))

    @builtins.property
    @jsii.member(jsii_name="maxAgeInput")
    def max_age_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maxAgeInput"))

    @builtins.property
    @jsii.member(jsii_name="allowCredentials")
    def allow_credentials(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowCredentials"))

    @allow_credentials.setter
    def allow_credentials(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteCorsOutputReference, "allow_credentials").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowCredentials", value)

    @builtins.property
    @jsii.member(jsii_name="allowHeaders")
    def allow_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowHeaders"))

    @allow_headers.setter
    def allow_headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteCorsOutputReference, "allow_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="allowMethods")
    def allow_methods(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "allowMethods"))

    @allow_methods.setter
    def allow_methods(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteCorsOutputReference, "allow_methods").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowMethods", value)

    @builtins.property
    @jsii.member(jsii_name="exposeHeaders")
    def expose_headers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "exposeHeaders"))

    @expose_headers.setter
    def expose_headers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteCorsOutputReference, "expose_headers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exposeHeaders", value)

    @builtins.property
    @jsii.member(jsii_name="maxAge")
    def max_age(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maxAge"))

    @max_age.setter
    def max_age(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteCorsOutputReference, "max_age").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAge", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecStaticSiteCors]:
        return typing.cast(typing.Optional[AppSpecStaticSiteCors], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppSpecStaticSiteCors]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteCorsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecStaticSiteEnv",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "scope": "scope", "type": "type", "value": "value"},
)
class AppSpecStaticSiteEnv:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        scope: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: The name of the environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#key App#key}
        :param scope: The visibility scope of the environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#scope App#scope}
        :param type: The type of the environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#type App#type}
        :param value: The value of the environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#value App#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecStaticSiteEnv.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if scope is not None:
            self._values["scope"] = scope
        if type is not None:
            self._values["type"] = type
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The name of the environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#key App#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scope(self) -> typing.Optional[builtins.str]:
        '''The visibility scope of the environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#scope App#scope}
        '''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of the environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#type App#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''The value of the environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#value App#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecStaticSiteEnv(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecStaticSiteEnvList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecStaticSiteEnvList",
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
            type_hints = typing.get_type_hints(AppSpecStaticSiteEnvList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AppSpecStaticSiteEnvOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecStaticSiteEnvList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppSpecStaticSiteEnvOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteEnvList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteEnvList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteEnvList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecStaticSiteEnv]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecStaticSiteEnv]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecStaticSiteEnv]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteEnvList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecStaticSiteEnvOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecStaticSiteEnvOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecStaticSiteEnvOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetScope")
    def reset_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScope", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="scopeInput")
    def scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scopeInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteEnvOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteEnvOutputReference, "scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteEnvOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteEnvOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppSpecStaticSiteEnv, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppSpecStaticSiteEnv, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppSpecStaticSiteEnv, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteEnvOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecStaticSiteGit",
    jsii_struct_bases=[],
    name_mapping={"branch": "branch", "repo_clone_url": "repoCloneUrl"},
)
class AppSpecStaticSiteGit:
    def __init__(
        self,
        *,
        branch: typing.Optional[builtins.str] = None,
        repo_clone_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: The name of the branch to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        :param repo_clone_url: The clone URL of the repo. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo_clone_url App#repo_clone_url}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecStaticSiteGit.__init__)
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
            check_type(argname="argument repo_clone_url", value=repo_clone_url, expected_type=type_hints["repo_clone_url"])
        self._values: typing.Dict[str, typing.Any] = {}
        if branch is not None:
            self._values["branch"] = branch
        if repo_clone_url is not None:
            self._values["repo_clone_url"] = repo_clone_url

    @builtins.property
    def branch(self) -> typing.Optional[builtins.str]:
        '''The name of the branch to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        '''
        result = self._values.get("branch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def repo_clone_url(self) -> typing.Optional[builtins.str]:
        '''The clone URL of the repo.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo_clone_url App#repo_clone_url}
        '''
        result = self._values.get("repo_clone_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecStaticSiteGit(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecStaticSiteGitOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecStaticSiteGitOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecStaticSiteGitOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBranch")
    def reset_branch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBranch", []))

    @jsii.member(jsii_name="resetRepoCloneUrl")
    def reset_repo_clone_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepoCloneUrl", []))

    @builtins.property
    @jsii.member(jsii_name="branchInput")
    def branch_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "branchInput"))

    @builtins.property
    @jsii.member(jsii_name="repoCloneUrlInput")
    def repo_clone_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repoCloneUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="branch")
    def branch(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "branch"))

    @branch.setter
    def branch(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteGitOutputReference, "branch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "branch", value)

    @builtins.property
    @jsii.member(jsii_name="repoCloneUrl")
    def repo_clone_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repoCloneUrl"))

    @repo_clone_url.setter
    def repo_clone_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteGitOutputReference, "repo_clone_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repoCloneUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecStaticSiteGit]:
        return typing.cast(typing.Optional[AppSpecStaticSiteGit], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppSpecStaticSiteGit]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteGitOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecStaticSiteGithub",
    jsii_struct_bases=[],
    name_mapping={
        "branch": "branch",
        "deploy_on_push": "deployOnPush",
        "repo": "repo",
    },
)
class AppSpecStaticSiteGithub:
    def __init__(
        self,
        *,
        branch: typing.Optional[builtins.str] = None,
        deploy_on_push: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: The name of the branch to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        :param deploy_on_push: Whether to automatically deploy new commits made to the repo. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        :param repo: The name of the repo in the format ``owner/repo``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo App#repo}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecStaticSiteGithub.__init__)
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
            check_type(argname="argument deploy_on_push", value=deploy_on_push, expected_type=type_hints["deploy_on_push"])
            check_type(argname="argument repo", value=repo, expected_type=type_hints["repo"])
        self._values: typing.Dict[str, typing.Any] = {}
        if branch is not None:
            self._values["branch"] = branch
        if deploy_on_push is not None:
            self._values["deploy_on_push"] = deploy_on_push
        if repo is not None:
            self._values["repo"] = repo

    @builtins.property
    def branch(self) -> typing.Optional[builtins.str]:
        '''The name of the branch to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        '''
        result = self._values.get("branch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deploy_on_push(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to automatically deploy new commits made to the repo.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        '''
        result = self._values.get("deploy_on_push")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def repo(self) -> typing.Optional[builtins.str]:
        '''The name of the repo in the format ``owner/repo``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo App#repo}
        '''
        result = self._values.get("repo")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecStaticSiteGithub(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecStaticSiteGithubOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecStaticSiteGithubOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecStaticSiteGithubOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBranch")
    def reset_branch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBranch", []))

    @jsii.member(jsii_name="resetDeployOnPush")
    def reset_deploy_on_push(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeployOnPush", []))

    @jsii.member(jsii_name="resetRepo")
    def reset_repo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepo", []))

    @builtins.property
    @jsii.member(jsii_name="branchInput")
    def branch_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "branchInput"))

    @builtins.property
    @jsii.member(jsii_name="deployOnPushInput")
    def deploy_on_push_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deployOnPushInput"))

    @builtins.property
    @jsii.member(jsii_name="repoInput")
    def repo_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repoInput"))

    @builtins.property
    @jsii.member(jsii_name="branch")
    def branch(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "branch"))

    @branch.setter
    def branch(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteGithubOutputReference, "branch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "branch", value)

    @builtins.property
    @jsii.member(jsii_name="deployOnPush")
    def deploy_on_push(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "deployOnPush"))

    @deploy_on_push.setter
    def deploy_on_push(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteGithubOutputReference, "deploy_on_push").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deployOnPush", value)

    @builtins.property
    @jsii.member(jsii_name="repo")
    def repo(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repo"))

    @repo.setter
    def repo(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteGithubOutputReference, "repo").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repo", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecStaticSiteGithub]:
        return typing.cast(typing.Optional[AppSpecStaticSiteGithub], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppSpecStaticSiteGithub]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteGithubOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecStaticSiteGitlab",
    jsii_struct_bases=[],
    name_mapping={
        "branch": "branch",
        "deploy_on_push": "deployOnPush",
        "repo": "repo",
    },
)
class AppSpecStaticSiteGitlab:
    def __init__(
        self,
        *,
        branch: typing.Optional[builtins.str] = None,
        deploy_on_push: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: The name of the branch to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        :param deploy_on_push: Whether to automatically deploy new commits made to the repo. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        :param repo: The name of the repo in the format ``owner/repo``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo App#repo}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecStaticSiteGitlab.__init__)
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
            check_type(argname="argument deploy_on_push", value=deploy_on_push, expected_type=type_hints["deploy_on_push"])
            check_type(argname="argument repo", value=repo, expected_type=type_hints["repo"])
        self._values: typing.Dict[str, typing.Any] = {}
        if branch is not None:
            self._values["branch"] = branch
        if deploy_on_push is not None:
            self._values["deploy_on_push"] = deploy_on_push
        if repo is not None:
            self._values["repo"] = repo

    @builtins.property
    def branch(self) -> typing.Optional[builtins.str]:
        '''The name of the branch to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        '''
        result = self._values.get("branch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deploy_on_push(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to automatically deploy new commits made to the repo.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        '''
        result = self._values.get("deploy_on_push")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def repo(self) -> typing.Optional[builtins.str]:
        '''The name of the repo in the format ``owner/repo``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo App#repo}
        '''
        result = self._values.get("repo")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecStaticSiteGitlab(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecStaticSiteGitlabOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecStaticSiteGitlabOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecStaticSiteGitlabOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBranch")
    def reset_branch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBranch", []))

    @jsii.member(jsii_name="resetDeployOnPush")
    def reset_deploy_on_push(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeployOnPush", []))

    @jsii.member(jsii_name="resetRepo")
    def reset_repo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepo", []))

    @builtins.property
    @jsii.member(jsii_name="branchInput")
    def branch_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "branchInput"))

    @builtins.property
    @jsii.member(jsii_name="deployOnPushInput")
    def deploy_on_push_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deployOnPushInput"))

    @builtins.property
    @jsii.member(jsii_name="repoInput")
    def repo_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repoInput"))

    @builtins.property
    @jsii.member(jsii_name="branch")
    def branch(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "branch"))

    @branch.setter
    def branch(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteGitlabOutputReference, "branch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "branch", value)

    @builtins.property
    @jsii.member(jsii_name="deployOnPush")
    def deploy_on_push(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "deployOnPush"))

    @deploy_on_push.setter
    def deploy_on_push(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteGitlabOutputReference, "deploy_on_push").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deployOnPush", value)

    @builtins.property
    @jsii.member(jsii_name="repo")
    def repo(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repo"))

    @repo.setter
    def repo(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteGitlabOutputReference, "repo").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repo", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecStaticSiteGitlab]:
        return typing.cast(typing.Optional[AppSpecStaticSiteGitlab], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppSpecStaticSiteGitlab]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteGitlabOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecStaticSiteList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecStaticSiteList",
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
            type_hints = typing.get_type_hints(AppSpecStaticSiteList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AppSpecStaticSiteOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecStaticSiteList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppSpecStaticSiteOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecStaticSite]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecStaticSite]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecStaticSite]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecStaticSiteOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecStaticSiteOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecStaticSiteOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putCors")
    def put_cors(
        self,
        *,
        allow_credentials: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_methods: typing.Optional[typing.Sequence[builtins.str]] = None,
        allow_origins: typing.Optional[typing.Union[AppSpecStaticSiteCorsAllowOrigins, typing.Dict[str, typing.Any]]] = None,
        expose_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
        max_age: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param allow_credentials: Whether browsers should expose the response to the client-side JavaScript code when the request’s credentials mode is ``include``. This configures the Access-Control-Allow-Credentials header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_credentials App#allow_credentials}
        :param allow_headers: The set of allowed HTTP request headers. This configures the Access-Control-Allow-Headers header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_headers App#allow_headers}
        :param allow_methods: The set of allowed HTTP methods. This configures the Access-Control-Allow-Methods header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_methods App#allow_methods}
        :param allow_origins: allow_origins block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#allow_origins App#allow_origins}
        :param expose_headers: The set of HTTP response headers that browsers are allowed to access. This configures the Access-Control-Expose-Headers header. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#expose_headers App#expose_headers}
        :param max_age: An optional duration specifying how long browsers can cache the results of a preflight request. This configures the Access-Control-Max-Age header. Example: ``5h30m``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#max_age App#max_age}
        '''
        value = AppSpecStaticSiteCors(
            allow_credentials=allow_credentials,
            allow_headers=allow_headers,
            allow_methods=allow_methods,
            allow_origins=allow_origins,
            expose_headers=expose_headers,
            max_age=max_age,
        )

        return typing.cast(None, jsii.invoke(self, "putCors", [value]))

    @jsii.member(jsii_name="putEnv")
    def put_env(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppSpecStaticSiteEnv, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecStaticSiteOutputReference.put_env)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEnv", [value]))

    @jsii.member(jsii_name="putGit")
    def put_git(
        self,
        *,
        branch: typing.Optional[builtins.str] = None,
        repo_clone_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: The name of the branch to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        :param repo_clone_url: The clone URL of the repo. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo_clone_url App#repo_clone_url}
        '''
        value = AppSpecStaticSiteGit(branch=branch, repo_clone_url=repo_clone_url)

        return typing.cast(None, jsii.invoke(self, "putGit", [value]))

    @jsii.member(jsii_name="putGithub")
    def put_github(
        self,
        *,
        branch: typing.Optional[builtins.str] = None,
        deploy_on_push: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: The name of the branch to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        :param deploy_on_push: Whether to automatically deploy new commits made to the repo. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        :param repo: The name of the repo in the format ``owner/repo``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo App#repo}
        '''
        value = AppSpecStaticSiteGithub(
            branch=branch, deploy_on_push=deploy_on_push, repo=repo
        )

        return typing.cast(None, jsii.invoke(self, "putGithub", [value]))

    @jsii.member(jsii_name="putGitlab")
    def put_gitlab(
        self,
        *,
        branch: typing.Optional[builtins.str] = None,
        deploy_on_push: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: The name of the branch to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        :param deploy_on_push: Whether to automatically deploy new commits made to the repo. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        :param repo: The name of the repo in the format ``owner/repo``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo App#repo}
        '''
        value = AppSpecStaticSiteGitlab(
            branch=branch, deploy_on_push=deploy_on_push, repo=repo
        )

        return typing.cast(None, jsii.invoke(self, "putGitlab", [value]))

    @jsii.member(jsii_name="putRoutes")
    def put_routes(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecStaticSiteRoutes", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecStaticSiteOutputReference.put_routes)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRoutes", [value]))

    @jsii.member(jsii_name="resetBuildCommand")
    def reset_build_command(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildCommand", []))

    @jsii.member(jsii_name="resetCatchallDocument")
    def reset_catchall_document(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCatchallDocument", []))

    @jsii.member(jsii_name="resetCors")
    def reset_cors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCors", []))

    @jsii.member(jsii_name="resetDockerfilePath")
    def reset_dockerfile_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDockerfilePath", []))

    @jsii.member(jsii_name="resetEnv")
    def reset_env(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnv", []))

    @jsii.member(jsii_name="resetEnvironmentSlug")
    def reset_environment_slug(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnvironmentSlug", []))

    @jsii.member(jsii_name="resetErrorDocument")
    def reset_error_document(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorDocument", []))

    @jsii.member(jsii_name="resetGit")
    def reset_git(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGit", []))

    @jsii.member(jsii_name="resetGithub")
    def reset_github(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGithub", []))

    @jsii.member(jsii_name="resetGitlab")
    def reset_gitlab(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGitlab", []))

    @jsii.member(jsii_name="resetIndexDocument")
    def reset_index_document(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIndexDocument", []))

    @jsii.member(jsii_name="resetOutputDir")
    def reset_output_dir(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutputDir", []))

    @jsii.member(jsii_name="resetRoutes")
    def reset_routes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRoutes", []))

    @jsii.member(jsii_name="resetSourceDir")
    def reset_source_dir(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceDir", []))

    @builtins.property
    @jsii.member(jsii_name="cors")
    def cors(self) -> AppSpecStaticSiteCorsOutputReference:
        return typing.cast(AppSpecStaticSiteCorsOutputReference, jsii.get(self, "cors"))

    @builtins.property
    @jsii.member(jsii_name="env")
    def env(self) -> AppSpecStaticSiteEnvList:
        return typing.cast(AppSpecStaticSiteEnvList, jsii.get(self, "env"))

    @builtins.property
    @jsii.member(jsii_name="git")
    def git(self) -> AppSpecStaticSiteGitOutputReference:
        return typing.cast(AppSpecStaticSiteGitOutputReference, jsii.get(self, "git"))

    @builtins.property
    @jsii.member(jsii_name="github")
    def github(self) -> AppSpecStaticSiteGithubOutputReference:
        return typing.cast(AppSpecStaticSiteGithubOutputReference, jsii.get(self, "github"))

    @builtins.property
    @jsii.member(jsii_name="gitlab")
    def gitlab(self) -> AppSpecStaticSiteGitlabOutputReference:
        return typing.cast(AppSpecStaticSiteGitlabOutputReference, jsii.get(self, "gitlab"))

    @builtins.property
    @jsii.member(jsii_name="routes")
    def routes(self) -> "AppSpecStaticSiteRoutesList":
        return typing.cast("AppSpecStaticSiteRoutesList", jsii.get(self, "routes"))

    @builtins.property
    @jsii.member(jsii_name="buildCommandInput")
    def build_command_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "buildCommandInput"))

    @builtins.property
    @jsii.member(jsii_name="catchallDocumentInput")
    def catchall_document_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "catchallDocumentInput"))

    @builtins.property
    @jsii.member(jsii_name="corsInput")
    def cors_input(self) -> typing.Optional[AppSpecStaticSiteCors]:
        return typing.cast(typing.Optional[AppSpecStaticSiteCors], jsii.get(self, "corsInput"))

    @builtins.property
    @jsii.member(jsii_name="dockerfilePathInput")
    def dockerfile_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dockerfilePathInput"))

    @builtins.property
    @jsii.member(jsii_name="envInput")
    def env_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecStaticSiteEnv]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecStaticSiteEnv]]], jsii.get(self, "envInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentSlugInput")
    def environment_slug_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentSlugInput"))

    @builtins.property
    @jsii.member(jsii_name="errorDocumentInput")
    def error_document_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "errorDocumentInput"))

    @builtins.property
    @jsii.member(jsii_name="githubInput")
    def github_input(self) -> typing.Optional[AppSpecStaticSiteGithub]:
        return typing.cast(typing.Optional[AppSpecStaticSiteGithub], jsii.get(self, "githubInput"))

    @builtins.property
    @jsii.member(jsii_name="gitInput")
    def git_input(self) -> typing.Optional[AppSpecStaticSiteGit]:
        return typing.cast(typing.Optional[AppSpecStaticSiteGit], jsii.get(self, "gitInput"))

    @builtins.property
    @jsii.member(jsii_name="gitlabInput")
    def gitlab_input(self) -> typing.Optional[AppSpecStaticSiteGitlab]:
        return typing.cast(typing.Optional[AppSpecStaticSiteGitlab], jsii.get(self, "gitlabInput"))

    @builtins.property
    @jsii.member(jsii_name="indexDocumentInput")
    def index_document_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "indexDocumentInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="outputDirInput")
    def output_dir_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outputDirInput"))

    @builtins.property
    @jsii.member(jsii_name="routesInput")
    def routes_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecStaticSiteRoutes"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecStaticSiteRoutes"]]], jsii.get(self, "routesInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceDirInput")
    def source_dir_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceDirInput"))

    @builtins.property
    @jsii.member(jsii_name="buildCommand")
    def build_command(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "buildCommand"))

    @build_command.setter
    def build_command(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteOutputReference, "build_command").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buildCommand", value)

    @builtins.property
    @jsii.member(jsii_name="catchallDocument")
    def catchall_document(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "catchallDocument"))

    @catchall_document.setter
    def catchall_document(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteOutputReference, "catchall_document").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "catchallDocument", value)

    @builtins.property
    @jsii.member(jsii_name="dockerfilePath")
    def dockerfile_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dockerfilePath"))

    @dockerfile_path.setter
    def dockerfile_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteOutputReference, "dockerfile_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dockerfilePath", value)

    @builtins.property
    @jsii.member(jsii_name="environmentSlug")
    def environment_slug(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "environmentSlug"))

    @environment_slug.setter
    def environment_slug(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteOutputReference, "environment_slug").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentSlug", value)

    @builtins.property
    @jsii.member(jsii_name="errorDocument")
    def error_document(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "errorDocument"))

    @error_document.setter
    def error_document(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteOutputReference, "error_document").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "errorDocument", value)

    @builtins.property
    @jsii.member(jsii_name="indexDocument")
    def index_document(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "indexDocument"))

    @index_document.setter
    def index_document(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteOutputReference, "index_document").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "indexDocument", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="outputDir")
    def output_dir(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outputDir"))

    @output_dir.setter
    def output_dir(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteOutputReference, "output_dir").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputDir", value)

    @builtins.property
    @jsii.member(jsii_name="sourceDir")
    def source_dir(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceDir"))

    @source_dir.setter
    def source_dir(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteOutputReference, "source_dir").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceDir", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppSpecStaticSite, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppSpecStaticSite, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppSpecStaticSite, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecStaticSiteRoutes",
    jsii_struct_bases=[],
    name_mapping={"path": "path", "preserve_path_prefix": "preservePathPrefix"},
)
class AppSpecStaticSiteRoutes:
    def __init__(
        self,
        *,
        path: typing.Optional[builtins.str] = None,
        preserve_path_prefix: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param path: Path specifies an route by HTTP path prefix. Paths must start with / and must be unique within the app. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#path App#path}
        :param preserve_path_prefix: An optional flag to preserve the path that is forwarded to the backend service. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#preserve_path_prefix App#preserve_path_prefix}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecStaticSiteRoutes.__init__)
            check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            check_type(argname="argument preserve_path_prefix", value=preserve_path_prefix, expected_type=type_hints["preserve_path_prefix"])
        self._values: typing.Dict[str, typing.Any] = {}
        if path is not None:
            self._values["path"] = path
        if preserve_path_prefix is not None:
            self._values["preserve_path_prefix"] = preserve_path_prefix

    @builtins.property
    def path(self) -> typing.Optional[builtins.str]:
        '''Path specifies an route by HTTP path prefix.

        Paths must start with / and must be unique within the app.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#path App#path}
        '''
        result = self._values.get("path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def preserve_path_prefix(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''An optional flag to preserve the path that is forwarded to the backend service.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#preserve_path_prefix App#preserve_path_prefix}
        '''
        result = self._values.get("preserve_path_prefix")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecStaticSiteRoutes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecStaticSiteRoutesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecStaticSiteRoutesList",
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
            type_hints = typing.get_type_hints(AppSpecStaticSiteRoutesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AppSpecStaticSiteRoutesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecStaticSiteRoutesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppSpecStaticSiteRoutesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteRoutesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteRoutesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteRoutesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecStaticSiteRoutes]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecStaticSiteRoutes]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecStaticSiteRoutes]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteRoutesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecStaticSiteRoutesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecStaticSiteRoutesOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecStaticSiteRoutesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPath")
    def reset_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPath", []))

    @jsii.member(jsii_name="resetPreservePathPrefix")
    def reset_preserve_path_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPreservePathPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="pathInput")
    def path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "pathInput"))

    @builtins.property
    @jsii.member(jsii_name="preservePathPrefixInput")
    def preserve_path_prefix_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "preservePathPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @path.setter
    def path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteRoutesOutputReference, "path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "path", value)

    @builtins.property
    @jsii.member(jsii_name="preservePathPrefix")
    def preserve_path_prefix(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "preservePathPrefix"))

    @preserve_path_prefix.setter
    def preserve_path_prefix(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteRoutesOutputReference, "preserve_path_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preservePathPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppSpecStaticSiteRoutes, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppSpecStaticSiteRoutes, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppSpecStaticSiteRoutes, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecStaticSiteRoutesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecWorker",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "alert": "alert",
        "build_command": "buildCommand",
        "dockerfile_path": "dockerfilePath",
        "env": "env",
        "environment_slug": "environmentSlug",
        "git": "git",
        "github": "github",
        "gitlab": "gitlab",
        "image": "image",
        "instance_count": "instanceCount",
        "instance_size_slug": "instanceSizeSlug",
        "log_destination": "logDestination",
        "run_command": "runCommand",
        "source_dir": "sourceDir",
    },
)
class AppSpecWorker:
    def __init__(
        self,
        *,
        name: builtins.str,
        alert: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecWorkerAlert", typing.Dict[str, typing.Any]]]]] = None,
        build_command: typing.Optional[builtins.str] = None,
        dockerfile_path: typing.Optional[builtins.str] = None,
        env: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecWorkerEnv", typing.Dict[str, typing.Any]]]]] = None,
        environment_slug: typing.Optional[builtins.str] = None,
        git: typing.Optional[typing.Union["AppSpecWorkerGit", typing.Dict[str, typing.Any]]] = None,
        github: typing.Optional[typing.Union["AppSpecWorkerGithub", typing.Dict[str, typing.Any]]] = None,
        gitlab: typing.Optional[typing.Union["AppSpecWorkerGitlab", typing.Dict[str, typing.Any]]] = None,
        image: typing.Optional[typing.Union["AppSpecWorkerImage", typing.Dict[str, typing.Any]]] = None,
        instance_count: typing.Optional[jsii.Number] = None,
        instance_size_slug: typing.Optional[builtins.str] = None,
        log_destination: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecWorkerLogDestination", typing.Dict[str, typing.Any]]]]] = None,
        run_command: typing.Optional[builtins.str] = None,
        source_dir: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: The name of the component. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#name App#name}
        :param alert: alert block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#alert App#alert}
        :param build_command: An optional build command to run while building this component from source. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#build_command App#build_command}
        :param dockerfile_path: The path to a Dockerfile relative to the root of the repo. If set, overrides usage of buildpacks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#dockerfile_path App#dockerfile_path}
        :param env: env block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#env App#env}
        :param environment_slug: An environment slug describing the type of this app. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#environment_slug App#environment_slug}
        :param git: git block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#git App#git}
        :param github: github block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#github App#github}
        :param gitlab: gitlab block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#gitlab App#gitlab}
        :param image: image block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#image App#image}
        :param instance_count: The amount of instances that this component should be scaled to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#instance_count App#instance_count}
        :param instance_size_slug: The instance size to use for this component. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#instance_size_slug App#instance_size_slug}
        :param log_destination: log_destination block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#log_destination App#log_destination}
        :param run_command: An optional run command to override the component's default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#run_command App#run_command}
        :param source_dir: An optional path to the working directory to use for the build. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#source_dir App#source_dir}
        '''
        if isinstance(git, dict):
            git = AppSpecWorkerGit(**git)
        if isinstance(github, dict):
            github = AppSpecWorkerGithub(**github)
        if isinstance(gitlab, dict):
            gitlab = AppSpecWorkerGitlab(**gitlab)
        if isinstance(image, dict):
            image = AppSpecWorkerImage(**image)
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecWorker.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument alert", value=alert, expected_type=type_hints["alert"])
            check_type(argname="argument build_command", value=build_command, expected_type=type_hints["build_command"])
            check_type(argname="argument dockerfile_path", value=dockerfile_path, expected_type=type_hints["dockerfile_path"])
            check_type(argname="argument env", value=env, expected_type=type_hints["env"])
            check_type(argname="argument environment_slug", value=environment_slug, expected_type=type_hints["environment_slug"])
            check_type(argname="argument git", value=git, expected_type=type_hints["git"])
            check_type(argname="argument github", value=github, expected_type=type_hints["github"])
            check_type(argname="argument gitlab", value=gitlab, expected_type=type_hints["gitlab"])
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
            check_type(argname="argument instance_count", value=instance_count, expected_type=type_hints["instance_count"])
            check_type(argname="argument instance_size_slug", value=instance_size_slug, expected_type=type_hints["instance_size_slug"])
            check_type(argname="argument log_destination", value=log_destination, expected_type=type_hints["log_destination"])
            check_type(argname="argument run_command", value=run_command, expected_type=type_hints["run_command"])
            check_type(argname="argument source_dir", value=source_dir, expected_type=type_hints["source_dir"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if alert is not None:
            self._values["alert"] = alert
        if build_command is not None:
            self._values["build_command"] = build_command
        if dockerfile_path is not None:
            self._values["dockerfile_path"] = dockerfile_path
        if env is not None:
            self._values["env"] = env
        if environment_slug is not None:
            self._values["environment_slug"] = environment_slug
        if git is not None:
            self._values["git"] = git
        if github is not None:
            self._values["github"] = github
        if gitlab is not None:
            self._values["gitlab"] = gitlab
        if image is not None:
            self._values["image"] = image
        if instance_count is not None:
            self._values["instance_count"] = instance_count
        if instance_size_slug is not None:
            self._values["instance_size_slug"] = instance_size_slug
        if log_destination is not None:
            self._values["log_destination"] = log_destination
        if run_command is not None:
            self._values["run_command"] = run_command
        if source_dir is not None:
            self._values["source_dir"] = source_dir

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the component.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#name App#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alert(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecWorkerAlert"]]]:
        '''alert block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#alert App#alert}
        '''
        result = self._values.get("alert")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecWorkerAlert"]]], result)

    @builtins.property
    def build_command(self) -> typing.Optional[builtins.str]:
        '''An optional build command to run while building this component from source.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#build_command App#build_command}
        '''
        result = self._values.get("build_command")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dockerfile_path(self) -> typing.Optional[builtins.str]:
        '''The path to a Dockerfile relative to the root of the repo. If set, overrides usage of buildpacks.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#dockerfile_path App#dockerfile_path}
        '''
        result = self._values.get("dockerfile_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def env(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecWorkerEnv"]]]:
        '''env block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#env App#env}
        '''
        result = self._values.get("env")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecWorkerEnv"]]], result)

    @builtins.property
    def environment_slug(self) -> typing.Optional[builtins.str]:
        '''An environment slug describing the type of this app.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#environment_slug App#environment_slug}
        '''
        result = self._values.get("environment_slug")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def git(self) -> typing.Optional["AppSpecWorkerGit"]:
        '''git block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#git App#git}
        '''
        result = self._values.get("git")
        return typing.cast(typing.Optional["AppSpecWorkerGit"], result)

    @builtins.property
    def github(self) -> typing.Optional["AppSpecWorkerGithub"]:
        '''github block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#github App#github}
        '''
        result = self._values.get("github")
        return typing.cast(typing.Optional["AppSpecWorkerGithub"], result)

    @builtins.property
    def gitlab(self) -> typing.Optional["AppSpecWorkerGitlab"]:
        '''gitlab block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#gitlab App#gitlab}
        '''
        result = self._values.get("gitlab")
        return typing.cast(typing.Optional["AppSpecWorkerGitlab"], result)

    @builtins.property
    def image(self) -> typing.Optional["AppSpecWorkerImage"]:
        '''image block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#image App#image}
        '''
        result = self._values.get("image")
        return typing.cast(typing.Optional["AppSpecWorkerImage"], result)

    @builtins.property
    def instance_count(self) -> typing.Optional[jsii.Number]:
        '''The amount of instances that this component should be scaled to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#instance_count App#instance_count}
        '''
        result = self._values.get("instance_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def instance_size_slug(self) -> typing.Optional[builtins.str]:
        '''The instance size to use for this component.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#instance_size_slug App#instance_size_slug}
        '''
        result = self._values.get("instance_size_slug")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_destination(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecWorkerLogDestination"]]]:
        '''log_destination block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#log_destination App#log_destination}
        '''
        result = self._values.get("log_destination")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecWorkerLogDestination"]]], result)

    @builtins.property
    def run_command(self) -> typing.Optional[builtins.str]:
        '''An optional run command to override the component's default.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#run_command App#run_command}
        '''
        result = self._values.get("run_command")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_dir(self) -> typing.Optional[builtins.str]:
        '''An optional path to the working directory to use for the build.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#source_dir App#source_dir}
        '''
        result = self._values.get("source_dir")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecWorker(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecWorkerAlert",
    jsii_struct_bases=[],
    name_mapping={
        "operator": "operator",
        "rule": "rule",
        "value": "value",
        "window": "window",
        "disabled": "disabled",
    },
)
class AppSpecWorkerAlert:
    def __init__(
        self,
        *,
        operator: builtins.str,
        rule: builtins.str,
        value: jsii.Number,
        window: builtins.str,
        disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param operator: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#operator App#operator}.
        :param rule: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#rule App#rule}.
        :param value: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#value App#value}.
        :param window: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#window App#window}.
        :param disabled: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#disabled App#disabled}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecWorkerAlert.__init__)
            check_type(argname="argument operator", value=operator, expected_type=type_hints["operator"])
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument window", value=window, expected_type=type_hints["window"])
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "operator": operator,
            "rule": rule,
            "value": value,
            "window": window,
        }
        if disabled is not None:
            self._values["disabled"] = disabled

    @builtins.property
    def operator(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#operator App#operator}.'''
        result = self._values.get("operator")
        assert result is not None, "Required property 'operator' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#rule App#rule}.'''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#value App#value}.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def window(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#window App#window}.'''
        result = self._values.get("window")
        assert result is not None, "Required property 'window' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#disabled App#disabled}.'''
        result = self._values.get("disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecWorkerAlert(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecWorkerAlertList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecWorkerAlertList",
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
            type_hints = typing.get_type_hints(AppSpecWorkerAlertList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AppSpecWorkerAlertOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecWorkerAlertList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppSpecWorkerAlertOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerAlertList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerAlertList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerAlertList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecWorkerAlert]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecWorkerAlert]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecWorkerAlert]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerAlertList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecWorkerAlertOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecWorkerAlertOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecWorkerAlertOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDisabled")
    def reset_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisabled", []))

    @builtins.property
    @jsii.member(jsii_name="disabledInput")
    def disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disabledInput"))

    @builtins.property
    @jsii.member(jsii_name="operatorInput")
    def operator_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatorInput"))

    @builtins.property
    @jsii.member(jsii_name="ruleInput")
    def rule_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="windowInput")
    def window_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "windowInput"))

    @builtins.property
    @jsii.member(jsii_name="disabled")
    def disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disabled"))

    @disabled.setter
    def disabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerAlertOutputReference, "disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

    @builtins.property
    @jsii.member(jsii_name="operator")
    def operator(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "operator"))

    @operator.setter
    def operator(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerAlertOutputReference, "operator").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operator", value)

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "rule"))

    @rule.setter
    def rule(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerAlertOutputReference, "rule").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "value"))

    @value.setter
    def value(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerAlertOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="window")
    def window(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "window"))

    @window.setter
    def window(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerAlertOutputReference, "window").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "window", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppSpecWorkerAlert, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppSpecWorkerAlert, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppSpecWorkerAlert, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerAlertOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecWorkerEnv",
    jsii_struct_bases=[],
    name_mapping={"key": "key", "scope": "scope", "type": "type", "value": "value"},
)
class AppSpecWorkerEnv:
    def __init__(
        self,
        *,
        key: typing.Optional[builtins.str] = None,
        scope: typing.Optional[builtins.str] = None,
        type: typing.Optional[builtins.str] = None,
        value: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key: The name of the environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#key App#key}
        :param scope: The visibility scope of the environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#scope App#scope}
        :param type: The type of the environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#type App#type}
        :param value: The value of the environment variable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#value App#value}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecWorkerEnv.__init__)
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key is not None:
            self._values["key"] = key
        if scope is not None:
            self._values["scope"] = scope
        if type is not None:
            self._values["type"] = type
        if value is not None:
            self._values["value"] = value

    @builtins.property
    def key(self) -> typing.Optional[builtins.str]:
        '''The name of the environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#key App#key}
        '''
        result = self._values.get("key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scope(self) -> typing.Optional[builtins.str]:
        '''The visibility scope of the environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#scope App#scope}
        '''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''The type of the environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#type App#type}
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def value(self) -> typing.Optional[builtins.str]:
        '''The value of the environment variable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#value App#value}
        '''
        result = self._values.get("value")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecWorkerEnv(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecWorkerEnvList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecWorkerEnvList",
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
            type_hints = typing.get_type_hints(AppSpecWorkerEnvList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AppSpecWorkerEnvOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecWorkerEnvList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppSpecWorkerEnvOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerEnvList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerEnvList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerEnvList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecWorkerEnv]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecWorkerEnv]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecWorkerEnv]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerEnvList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecWorkerEnvOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecWorkerEnvOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecWorkerEnvOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetKey")
    def reset_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKey", []))

    @jsii.member(jsii_name="resetScope")
    def reset_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScope", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @jsii.member(jsii_name="resetValue")
    def reset_value(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetValue", []))

    @builtins.property
    @jsii.member(jsii_name="keyInput")
    def key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyInput"))

    @builtins.property
    @jsii.member(jsii_name="scopeInput")
    def scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scopeInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="valueInput")
    def value_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "valueInput"))

    @builtins.property
    @jsii.member(jsii_name="key")
    def key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "key"))

    @key.setter
    def key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerEnvOutputReference, "key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "key", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerEnvOutputReference, "scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerEnvOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @value.setter
    def value(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerEnvOutputReference, "value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "value", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppSpecWorkerEnv, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppSpecWorkerEnv, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppSpecWorkerEnv, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerEnvOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecWorkerGit",
    jsii_struct_bases=[],
    name_mapping={"branch": "branch", "repo_clone_url": "repoCloneUrl"},
)
class AppSpecWorkerGit:
    def __init__(
        self,
        *,
        branch: typing.Optional[builtins.str] = None,
        repo_clone_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: The name of the branch to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        :param repo_clone_url: The clone URL of the repo. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo_clone_url App#repo_clone_url}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecWorkerGit.__init__)
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
            check_type(argname="argument repo_clone_url", value=repo_clone_url, expected_type=type_hints["repo_clone_url"])
        self._values: typing.Dict[str, typing.Any] = {}
        if branch is not None:
            self._values["branch"] = branch
        if repo_clone_url is not None:
            self._values["repo_clone_url"] = repo_clone_url

    @builtins.property
    def branch(self) -> typing.Optional[builtins.str]:
        '''The name of the branch to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        '''
        result = self._values.get("branch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def repo_clone_url(self) -> typing.Optional[builtins.str]:
        '''The clone URL of the repo.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo_clone_url App#repo_clone_url}
        '''
        result = self._values.get("repo_clone_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecWorkerGit(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecWorkerGitOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecWorkerGitOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecWorkerGitOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBranch")
    def reset_branch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBranch", []))

    @jsii.member(jsii_name="resetRepoCloneUrl")
    def reset_repo_clone_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepoCloneUrl", []))

    @builtins.property
    @jsii.member(jsii_name="branchInput")
    def branch_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "branchInput"))

    @builtins.property
    @jsii.member(jsii_name="repoCloneUrlInput")
    def repo_clone_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repoCloneUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="branch")
    def branch(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "branch"))

    @branch.setter
    def branch(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerGitOutputReference, "branch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "branch", value)

    @builtins.property
    @jsii.member(jsii_name="repoCloneUrl")
    def repo_clone_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repoCloneUrl"))

    @repo_clone_url.setter
    def repo_clone_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerGitOutputReference, "repo_clone_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repoCloneUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecWorkerGit]:
        return typing.cast(typing.Optional[AppSpecWorkerGit], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppSpecWorkerGit]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerGitOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecWorkerGithub",
    jsii_struct_bases=[],
    name_mapping={
        "branch": "branch",
        "deploy_on_push": "deployOnPush",
        "repo": "repo",
    },
)
class AppSpecWorkerGithub:
    def __init__(
        self,
        *,
        branch: typing.Optional[builtins.str] = None,
        deploy_on_push: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: The name of the branch to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        :param deploy_on_push: Whether to automatically deploy new commits made to the repo. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        :param repo: The name of the repo in the format ``owner/repo``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo App#repo}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecWorkerGithub.__init__)
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
            check_type(argname="argument deploy_on_push", value=deploy_on_push, expected_type=type_hints["deploy_on_push"])
            check_type(argname="argument repo", value=repo, expected_type=type_hints["repo"])
        self._values: typing.Dict[str, typing.Any] = {}
        if branch is not None:
            self._values["branch"] = branch
        if deploy_on_push is not None:
            self._values["deploy_on_push"] = deploy_on_push
        if repo is not None:
            self._values["repo"] = repo

    @builtins.property
    def branch(self) -> typing.Optional[builtins.str]:
        '''The name of the branch to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        '''
        result = self._values.get("branch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deploy_on_push(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to automatically deploy new commits made to the repo.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        '''
        result = self._values.get("deploy_on_push")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def repo(self) -> typing.Optional[builtins.str]:
        '''The name of the repo in the format ``owner/repo``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo App#repo}
        '''
        result = self._values.get("repo")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecWorkerGithub(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecWorkerGithubOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecWorkerGithubOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecWorkerGithubOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBranch")
    def reset_branch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBranch", []))

    @jsii.member(jsii_name="resetDeployOnPush")
    def reset_deploy_on_push(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeployOnPush", []))

    @jsii.member(jsii_name="resetRepo")
    def reset_repo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepo", []))

    @builtins.property
    @jsii.member(jsii_name="branchInput")
    def branch_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "branchInput"))

    @builtins.property
    @jsii.member(jsii_name="deployOnPushInput")
    def deploy_on_push_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deployOnPushInput"))

    @builtins.property
    @jsii.member(jsii_name="repoInput")
    def repo_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repoInput"))

    @builtins.property
    @jsii.member(jsii_name="branch")
    def branch(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "branch"))

    @branch.setter
    def branch(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerGithubOutputReference, "branch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "branch", value)

    @builtins.property
    @jsii.member(jsii_name="deployOnPush")
    def deploy_on_push(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "deployOnPush"))

    @deploy_on_push.setter
    def deploy_on_push(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerGithubOutputReference, "deploy_on_push").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deployOnPush", value)

    @builtins.property
    @jsii.member(jsii_name="repo")
    def repo(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repo"))

    @repo.setter
    def repo(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerGithubOutputReference, "repo").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repo", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecWorkerGithub]:
        return typing.cast(typing.Optional[AppSpecWorkerGithub], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppSpecWorkerGithub]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerGithubOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecWorkerGitlab",
    jsii_struct_bases=[],
    name_mapping={
        "branch": "branch",
        "deploy_on_push": "deployOnPush",
        "repo": "repo",
    },
)
class AppSpecWorkerGitlab:
    def __init__(
        self,
        *,
        branch: typing.Optional[builtins.str] = None,
        deploy_on_push: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: The name of the branch to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        :param deploy_on_push: Whether to automatically deploy new commits made to the repo. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        :param repo: The name of the repo in the format ``owner/repo``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo App#repo}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecWorkerGitlab.__init__)
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
            check_type(argname="argument deploy_on_push", value=deploy_on_push, expected_type=type_hints["deploy_on_push"])
            check_type(argname="argument repo", value=repo, expected_type=type_hints["repo"])
        self._values: typing.Dict[str, typing.Any] = {}
        if branch is not None:
            self._values["branch"] = branch
        if deploy_on_push is not None:
            self._values["deploy_on_push"] = deploy_on_push
        if repo is not None:
            self._values["repo"] = repo

    @builtins.property
    def branch(self) -> typing.Optional[builtins.str]:
        '''The name of the branch to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        '''
        result = self._values.get("branch")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deploy_on_push(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to automatically deploy new commits made to the repo.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        '''
        result = self._values.get("deploy_on_push")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def repo(self) -> typing.Optional[builtins.str]:
        '''The name of the repo in the format ``owner/repo``.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo App#repo}
        '''
        result = self._values.get("repo")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecWorkerGitlab(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecWorkerGitlabOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecWorkerGitlabOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecWorkerGitlabOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetBranch")
    def reset_branch(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBranch", []))

    @jsii.member(jsii_name="resetDeployOnPush")
    def reset_deploy_on_push(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeployOnPush", []))

    @jsii.member(jsii_name="resetRepo")
    def reset_repo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRepo", []))

    @builtins.property
    @jsii.member(jsii_name="branchInput")
    def branch_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "branchInput"))

    @builtins.property
    @jsii.member(jsii_name="deployOnPushInput")
    def deploy_on_push_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deployOnPushInput"))

    @builtins.property
    @jsii.member(jsii_name="repoInput")
    def repo_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repoInput"))

    @builtins.property
    @jsii.member(jsii_name="branch")
    def branch(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "branch"))

    @branch.setter
    def branch(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerGitlabOutputReference, "branch").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "branch", value)

    @builtins.property
    @jsii.member(jsii_name="deployOnPush")
    def deploy_on_push(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "deployOnPush"))

    @deploy_on_push.setter
    def deploy_on_push(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerGitlabOutputReference, "deploy_on_push").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deployOnPush", value)

    @builtins.property
    @jsii.member(jsii_name="repo")
    def repo(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repo"))

    @repo.setter
    def repo(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerGitlabOutputReference, "repo").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repo", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecWorkerGitlab]:
        return typing.cast(typing.Optional[AppSpecWorkerGitlab], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppSpecWorkerGitlab]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerGitlabOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecWorkerImage",
    jsii_struct_bases=[],
    name_mapping={
        "registry_type": "registryType",
        "repository": "repository",
        "deploy_on_push": "deployOnPush",
        "registry": "registry",
        "tag": "tag",
    },
)
class AppSpecWorkerImage:
    def __init__(
        self,
        *,
        registry_type: builtins.str,
        repository: builtins.str,
        deploy_on_push: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["AppSpecWorkerImageDeployOnPush", typing.Dict[str, typing.Any]]]]] = None,
        registry: typing.Optional[builtins.str] = None,
        tag: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param registry_type: The registry type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#registry_type App#registry_type}
        :param repository: The repository name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repository App#repository}
        :param deploy_on_push: deploy_on_push block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        :param registry: The registry name. Must be left empty for the DOCR registry type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#registry App#registry}
        :param tag: The repository tag. Defaults to latest if not provided. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#tag App#tag}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecWorkerImage.__init__)
            check_type(argname="argument registry_type", value=registry_type, expected_type=type_hints["registry_type"])
            check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
            check_type(argname="argument deploy_on_push", value=deploy_on_push, expected_type=type_hints["deploy_on_push"])
            check_type(argname="argument registry", value=registry, expected_type=type_hints["registry"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
        self._values: typing.Dict[str, typing.Any] = {
            "registry_type": registry_type,
            "repository": repository,
        }
        if deploy_on_push is not None:
            self._values["deploy_on_push"] = deploy_on_push
        if registry is not None:
            self._values["registry"] = registry
        if tag is not None:
            self._values["tag"] = tag

    @builtins.property
    def registry_type(self) -> builtins.str:
        '''The registry type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#registry_type App#registry_type}
        '''
        result = self._values.get("registry_type")
        assert result is not None, "Required property 'registry_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repository(self) -> builtins.str:
        '''The repository name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repository App#repository}
        '''
        result = self._values.get("repository")
        assert result is not None, "Required property 'repository' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def deploy_on_push(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecWorkerImageDeployOnPush"]]]:
        '''deploy_on_push block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        '''
        result = self._values.get("deploy_on_push")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["AppSpecWorkerImageDeployOnPush"]]], result)

    @builtins.property
    def registry(self) -> typing.Optional[builtins.str]:
        '''The registry name. Must be left empty for the DOCR registry type.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#registry App#registry}
        '''
        result = self._values.get("registry")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tag(self) -> typing.Optional[builtins.str]:
        '''The repository tag. Defaults to latest if not provided.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#tag App#tag}
        '''
        result = self._values.get("tag")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecWorkerImage(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecWorkerImageDeployOnPush",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class AppSpecWorkerImageDeployOnPush:
    def __init__(
        self,
        *,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enabled: Whether to automatically deploy images pushed to DOCR. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#enabled App#enabled}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecWorkerImageDeployOnPush.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to automatically deploy images pushed to DOCR.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#enabled App#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecWorkerImageDeployOnPush(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecWorkerImageDeployOnPushList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecWorkerImageDeployOnPushList",
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
            type_hints = typing.get_type_hints(AppSpecWorkerImageDeployOnPushList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "AppSpecWorkerImageDeployOnPushOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecWorkerImageDeployOnPushList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppSpecWorkerImageDeployOnPushOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerImageDeployOnPushList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerImageDeployOnPushList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerImageDeployOnPushList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecWorkerImageDeployOnPush]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecWorkerImageDeployOnPush]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecWorkerImageDeployOnPush]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerImageDeployOnPushList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecWorkerImageDeployOnPushOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecWorkerImageDeployOnPushOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecWorkerImageDeployOnPushOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerImageDeployOnPushOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppSpecWorkerImageDeployOnPush, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppSpecWorkerImageDeployOnPush, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppSpecWorkerImageDeployOnPush, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerImageDeployOnPushOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecWorkerImageOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecWorkerImageOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecWorkerImageOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDeployOnPush")
    def put_deploy_on_push(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppSpecWorkerImageDeployOnPush, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecWorkerImageOutputReference.put_deploy_on_push)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDeployOnPush", [value]))

    @jsii.member(jsii_name="resetDeployOnPush")
    def reset_deploy_on_push(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeployOnPush", []))

    @jsii.member(jsii_name="resetRegistry")
    def reset_registry(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegistry", []))

    @jsii.member(jsii_name="resetTag")
    def reset_tag(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTag", []))

    @builtins.property
    @jsii.member(jsii_name="deployOnPush")
    def deploy_on_push(self) -> AppSpecWorkerImageDeployOnPushList:
        return typing.cast(AppSpecWorkerImageDeployOnPushList, jsii.get(self, "deployOnPush"))

    @builtins.property
    @jsii.member(jsii_name="deployOnPushInput")
    def deploy_on_push_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecWorkerImageDeployOnPush]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecWorkerImageDeployOnPush]]], jsii.get(self, "deployOnPushInput"))

    @builtins.property
    @jsii.member(jsii_name="registryInput")
    def registry_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "registryInput"))

    @builtins.property
    @jsii.member(jsii_name="registryTypeInput")
    def registry_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "registryTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="repositoryInput")
    def repository_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "repositoryInput"))

    @builtins.property
    @jsii.member(jsii_name="tagInput")
    def tag_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tagInput"))

    @builtins.property
    @jsii.member(jsii_name="registry")
    def registry(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registry"))

    @registry.setter
    def registry(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerImageOutputReference, "registry").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registry", value)

    @builtins.property
    @jsii.member(jsii_name="registryType")
    def registry_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registryType"))

    @registry_type.setter
    def registry_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerImageOutputReference, "registry_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registryType", value)

    @builtins.property
    @jsii.member(jsii_name="repository")
    def repository(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "repository"))

    @repository.setter
    def repository(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerImageOutputReference, "repository").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repository", value)

    @builtins.property
    @jsii.member(jsii_name="tag")
    def tag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tag"))

    @tag.setter
    def tag(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerImageOutputReference, "tag").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tag", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecWorkerImage]:
        return typing.cast(typing.Optional[AppSpecWorkerImage], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[AppSpecWorkerImage]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerImageOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecWorkerList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecWorkerList",
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
            type_hints = typing.get_type_hints(AppSpecWorkerList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AppSpecWorkerOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecWorkerList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppSpecWorkerOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecWorker]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecWorker]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecWorker]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecWorkerLogDestination",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "datadog": "datadog",
        "logtail": "logtail",
        "papertrail": "papertrail",
    },
)
class AppSpecWorkerLogDestination:
    def __init__(
        self,
        *,
        name: builtins.str,
        datadog: typing.Optional[typing.Union["AppSpecWorkerLogDestinationDatadog", typing.Dict[str, typing.Any]]] = None,
        logtail: typing.Optional[typing.Union["AppSpecWorkerLogDestinationLogtail", typing.Dict[str, typing.Any]]] = None,
        papertrail: typing.Optional[typing.Union["AppSpecWorkerLogDestinationPapertrail", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param name: Name of the log destination. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#name App#name}
        :param datadog: datadog block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#datadog App#datadog}
        :param logtail: logtail block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#logtail App#logtail}
        :param papertrail: papertrail block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#papertrail App#papertrail}
        '''
        if isinstance(datadog, dict):
            datadog = AppSpecWorkerLogDestinationDatadog(**datadog)
        if isinstance(logtail, dict):
            logtail = AppSpecWorkerLogDestinationLogtail(**logtail)
        if isinstance(papertrail, dict):
            papertrail = AppSpecWorkerLogDestinationPapertrail(**papertrail)
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecWorkerLogDestination.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument datadog", value=datadog, expected_type=type_hints["datadog"])
            check_type(argname="argument logtail", value=logtail, expected_type=type_hints["logtail"])
            check_type(argname="argument papertrail", value=papertrail, expected_type=type_hints["papertrail"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
        }
        if datadog is not None:
            self._values["datadog"] = datadog
        if logtail is not None:
            self._values["logtail"] = logtail
        if papertrail is not None:
            self._values["papertrail"] = papertrail

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the log destination.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#name App#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def datadog(self) -> typing.Optional["AppSpecWorkerLogDestinationDatadog"]:
        '''datadog block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#datadog App#datadog}
        '''
        result = self._values.get("datadog")
        return typing.cast(typing.Optional["AppSpecWorkerLogDestinationDatadog"], result)

    @builtins.property
    def logtail(self) -> typing.Optional["AppSpecWorkerLogDestinationLogtail"]:
        '''logtail block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#logtail App#logtail}
        '''
        result = self._values.get("logtail")
        return typing.cast(typing.Optional["AppSpecWorkerLogDestinationLogtail"], result)

    @builtins.property
    def papertrail(self) -> typing.Optional["AppSpecWorkerLogDestinationPapertrail"]:
        '''papertrail block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#papertrail App#papertrail}
        '''
        result = self._values.get("papertrail")
        return typing.cast(typing.Optional["AppSpecWorkerLogDestinationPapertrail"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecWorkerLogDestination(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecWorkerLogDestinationDatadog",
    jsii_struct_bases=[],
    name_mapping={"api_key": "apiKey", "endpoint": "endpoint"},
)
class AppSpecWorkerLogDestinationDatadog:
    def __init__(
        self,
        *,
        api_key: builtins.str,
        endpoint: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param api_key: Datadog API key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#api_key App#api_key}
        :param endpoint: Datadog HTTP log intake endpoint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#endpoint App#endpoint}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecWorkerLogDestinationDatadog.__init__)
            check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
        self._values: typing.Dict[str, typing.Any] = {
            "api_key": api_key,
        }
        if endpoint is not None:
            self._values["endpoint"] = endpoint

    @builtins.property
    def api_key(self) -> builtins.str:
        '''Datadog API key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#api_key App#api_key}
        '''
        result = self._values.get("api_key")
        assert result is not None, "Required property 'api_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoint(self) -> typing.Optional[builtins.str]:
        '''Datadog HTTP log intake endpoint.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#endpoint App#endpoint}
        '''
        result = self._values.get("endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecWorkerLogDestinationDatadog(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecWorkerLogDestinationDatadogOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecWorkerLogDestinationDatadogOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecWorkerLogDestinationDatadogOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEndpoint")
    def reset_endpoint(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpoint", []))

    @builtins.property
    @jsii.member(jsii_name="apiKeyInput")
    def api_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="apiKey")
    def api_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "apiKey"))

    @api_key.setter
    def api_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerLogDestinationDatadogOutputReference, "api_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiKey", value)

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerLogDestinationDatadogOutputReference, "endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecWorkerLogDestinationDatadog]:
        return typing.cast(typing.Optional[AppSpecWorkerLogDestinationDatadog], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppSpecWorkerLogDestinationDatadog],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerLogDestinationDatadogOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecWorkerLogDestinationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecWorkerLogDestinationList",
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
            type_hints = typing.get_type_hints(AppSpecWorkerLogDestinationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "AppSpecWorkerLogDestinationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecWorkerLogDestinationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("AppSpecWorkerLogDestinationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerLogDestinationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerLogDestinationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerLogDestinationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecWorkerLogDestination]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecWorkerLogDestination]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecWorkerLogDestination]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerLogDestinationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecWorkerLogDestinationLogtail",
    jsii_struct_bases=[],
    name_mapping={"token": "token"},
)
class AppSpecWorkerLogDestinationLogtail:
    def __init__(self, *, token: builtins.str) -> None:
        '''
        :param token: Logtail token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#token App#token}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecWorkerLogDestinationLogtail.__init__)
            check_type(argname="argument token", value=token, expected_type=type_hints["token"])
        self._values: typing.Dict[str, typing.Any] = {
            "token": token,
        }

    @builtins.property
    def token(self) -> builtins.str:
        '''Logtail token.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#token App#token}
        '''
        result = self._values.get("token")
        assert result is not None, "Required property 'token' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecWorkerLogDestinationLogtail(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecWorkerLogDestinationLogtailOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecWorkerLogDestinationLogtailOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecWorkerLogDestinationLogtailOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="tokenInput")
    def token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tokenInput"))

    @builtins.property
    @jsii.member(jsii_name="token")
    def token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "token"))

    @token.setter
    def token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerLogDestinationLogtailOutputReference, "token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "token", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecWorkerLogDestinationLogtail]:
        return typing.cast(typing.Optional[AppSpecWorkerLogDestinationLogtail], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppSpecWorkerLogDestinationLogtail],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerLogDestinationLogtailOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecWorkerLogDestinationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecWorkerLogDestinationOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecWorkerLogDestinationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putDatadog")
    def put_datadog(
        self,
        *,
        api_key: builtins.str,
        endpoint: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param api_key: Datadog API key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#api_key App#api_key}
        :param endpoint: Datadog HTTP log intake endpoint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#endpoint App#endpoint}
        '''
        value = AppSpecWorkerLogDestinationDatadog(api_key=api_key, endpoint=endpoint)

        return typing.cast(None, jsii.invoke(self, "putDatadog", [value]))

    @jsii.member(jsii_name="putLogtail")
    def put_logtail(self, *, token: builtins.str) -> None:
        '''
        :param token: Logtail token. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#token App#token}
        '''
        value = AppSpecWorkerLogDestinationLogtail(token=token)

        return typing.cast(None, jsii.invoke(self, "putLogtail", [value]))

    @jsii.member(jsii_name="putPapertrail")
    def put_papertrail(self, *, endpoint: builtins.str) -> None:
        '''
        :param endpoint: Papertrail syslog endpoint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#endpoint App#endpoint}
        '''
        value = AppSpecWorkerLogDestinationPapertrail(endpoint=endpoint)

        return typing.cast(None, jsii.invoke(self, "putPapertrail", [value]))

    @jsii.member(jsii_name="resetDatadog")
    def reset_datadog(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatadog", []))

    @jsii.member(jsii_name="resetLogtail")
    def reset_logtail(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogtail", []))

    @jsii.member(jsii_name="resetPapertrail")
    def reset_papertrail(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPapertrail", []))

    @builtins.property
    @jsii.member(jsii_name="datadog")
    def datadog(self) -> AppSpecWorkerLogDestinationDatadogOutputReference:
        return typing.cast(AppSpecWorkerLogDestinationDatadogOutputReference, jsii.get(self, "datadog"))

    @builtins.property
    @jsii.member(jsii_name="logtail")
    def logtail(self) -> AppSpecWorkerLogDestinationLogtailOutputReference:
        return typing.cast(AppSpecWorkerLogDestinationLogtailOutputReference, jsii.get(self, "logtail"))

    @builtins.property
    @jsii.member(jsii_name="papertrail")
    def papertrail(self) -> "AppSpecWorkerLogDestinationPapertrailOutputReference":
        return typing.cast("AppSpecWorkerLogDestinationPapertrailOutputReference", jsii.get(self, "papertrail"))

    @builtins.property
    @jsii.member(jsii_name="datadogInput")
    def datadog_input(self) -> typing.Optional[AppSpecWorkerLogDestinationDatadog]:
        return typing.cast(typing.Optional[AppSpecWorkerLogDestinationDatadog], jsii.get(self, "datadogInput"))

    @builtins.property
    @jsii.member(jsii_name="logtailInput")
    def logtail_input(self) -> typing.Optional[AppSpecWorkerLogDestinationLogtail]:
        return typing.cast(typing.Optional[AppSpecWorkerLogDestinationLogtail], jsii.get(self, "logtailInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="papertrailInput")
    def papertrail_input(
        self,
    ) -> typing.Optional["AppSpecWorkerLogDestinationPapertrail"]:
        return typing.cast(typing.Optional["AppSpecWorkerLogDestinationPapertrail"], jsii.get(self, "papertrailInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerLogDestinationOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppSpecWorkerLogDestination, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppSpecWorkerLogDestination, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppSpecWorkerLogDestination, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerLogDestinationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecWorkerLogDestinationPapertrail",
    jsii_struct_bases=[],
    name_mapping={"endpoint": "endpoint"},
)
class AppSpecWorkerLogDestinationPapertrail:
    def __init__(self, *, endpoint: builtins.str) -> None:
        '''
        :param endpoint: Papertrail syslog endpoint. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#endpoint App#endpoint}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecWorkerLogDestinationPapertrail.__init__)
            check_type(argname="argument endpoint", value=endpoint, expected_type=type_hints["endpoint"])
        self._values: typing.Dict[str, typing.Any] = {
            "endpoint": endpoint,
        }

    @builtins.property
    def endpoint(self) -> builtins.str:
        '''Papertrail syslog endpoint.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#endpoint App#endpoint}
        '''
        result = self._values.get("endpoint")
        assert result is not None, "Required property 'endpoint' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppSpecWorkerLogDestinationPapertrail(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppSpecWorkerLogDestinationPapertrailOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecWorkerLogDestinationPapertrailOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecWorkerLogDestinationPapertrailOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="endpointInput")
    def endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointInput"))

    @builtins.property
    @jsii.member(jsii_name="endpoint")
    def endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endpoint"))

    @endpoint.setter
    def endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerLogDestinationPapertrailOutputReference, "endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpoint", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[AppSpecWorkerLogDestinationPapertrail]:
        return typing.cast(typing.Optional[AppSpecWorkerLogDestinationPapertrail], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[AppSpecWorkerLogDestinationPapertrail],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerLogDestinationPapertrailOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class AppSpecWorkerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppSpecWorkerOutputReference",
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
            type_hints = typing.get_type_hints(AppSpecWorkerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAlert")
    def put_alert(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppSpecWorkerAlert, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecWorkerOutputReference.put_alert)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAlert", [value]))

    @jsii.member(jsii_name="putEnv")
    def put_env(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppSpecWorkerEnv, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecWorkerOutputReference.put_env)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEnv", [value]))

    @jsii.member(jsii_name="putGit")
    def put_git(
        self,
        *,
        branch: typing.Optional[builtins.str] = None,
        repo_clone_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: The name of the branch to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        :param repo_clone_url: The clone URL of the repo. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo_clone_url App#repo_clone_url}
        '''
        value = AppSpecWorkerGit(branch=branch, repo_clone_url=repo_clone_url)

        return typing.cast(None, jsii.invoke(self, "putGit", [value]))

    @jsii.member(jsii_name="putGithub")
    def put_github(
        self,
        *,
        branch: typing.Optional[builtins.str] = None,
        deploy_on_push: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: The name of the branch to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        :param deploy_on_push: Whether to automatically deploy new commits made to the repo. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        :param repo: The name of the repo in the format ``owner/repo``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo App#repo}
        '''
        value = AppSpecWorkerGithub(
            branch=branch, deploy_on_push=deploy_on_push, repo=repo
        )

        return typing.cast(None, jsii.invoke(self, "putGithub", [value]))

    @jsii.member(jsii_name="putGitlab")
    def put_gitlab(
        self,
        *,
        branch: typing.Optional[builtins.str] = None,
        deploy_on_push: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        repo: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param branch: The name of the branch to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#branch App#branch}
        :param deploy_on_push: Whether to automatically deploy new commits made to the repo. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        :param repo: The name of the repo in the format ``owner/repo``. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repo App#repo}
        '''
        value = AppSpecWorkerGitlab(
            branch=branch, deploy_on_push=deploy_on_push, repo=repo
        )

        return typing.cast(None, jsii.invoke(self, "putGitlab", [value]))

    @jsii.member(jsii_name="putImage")
    def put_image(
        self,
        *,
        registry_type: builtins.str,
        repository: builtins.str,
        deploy_on_push: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppSpecWorkerImageDeployOnPush, typing.Dict[str, typing.Any]]]]] = None,
        registry: typing.Optional[builtins.str] = None,
        tag: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param registry_type: The registry type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#registry_type App#registry_type}
        :param repository: The repository name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#repository App#repository}
        :param deploy_on_push: deploy_on_push block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#deploy_on_push App#deploy_on_push}
        :param registry: The registry name. Must be left empty for the DOCR registry type. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#registry App#registry}
        :param tag: The repository tag. Defaults to latest if not provided. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#tag App#tag}
        '''
        value = AppSpecWorkerImage(
            registry_type=registry_type,
            repository=repository,
            deploy_on_push=deploy_on_push,
            registry=registry,
            tag=tag,
        )

        return typing.cast(None, jsii.invoke(self, "putImage", [value]))

    @jsii.member(jsii_name="putLogDestination")
    def put_log_destination(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[AppSpecWorkerLogDestination, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppSpecWorkerOutputReference.put_log_destination)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLogDestination", [value]))

    @jsii.member(jsii_name="resetAlert")
    def reset_alert(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlert", []))

    @jsii.member(jsii_name="resetBuildCommand")
    def reset_build_command(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBuildCommand", []))

    @jsii.member(jsii_name="resetDockerfilePath")
    def reset_dockerfile_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDockerfilePath", []))

    @jsii.member(jsii_name="resetEnv")
    def reset_env(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnv", []))

    @jsii.member(jsii_name="resetEnvironmentSlug")
    def reset_environment_slug(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnvironmentSlug", []))

    @jsii.member(jsii_name="resetGit")
    def reset_git(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGit", []))

    @jsii.member(jsii_name="resetGithub")
    def reset_github(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGithub", []))

    @jsii.member(jsii_name="resetGitlab")
    def reset_gitlab(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGitlab", []))

    @jsii.member(jsii_name="resetImage")
    def reset_image(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetImage", []))

    @jsii.member(jsii_name="resetInstanceCount")
    def reset_instance_count(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceCount", []))

    @jsii.member(jsii_name="resetInstanceSizeSlug")
    def reset_instance_size_slug(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstanceSizeSlug", []))

    @jsii.member(jsii_name="resetLogDestination")
    def reset_log_destination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogDestination", []))

    @jsii.member(jsii_name="resetRunCommand")
    def reset_run_command(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRunCommand", []))

    @jsii.member(jsii_name="resetSourceDir")
    def reset_source_dir(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceDir", []))

    @builtins.property
    @jsii.member(jsii_name="alert")
    def alert(self) -> AppSpecWorkerAlertList:
        return typing.cast(AppSpecWorkerAlertList, jsii.get(self, "alert"))

    @builtins.property
    @jsii.member(jsii_name="env")
    def env(self) -> AppSpecWorkerEnvList:
        return typing.cast(AppSpecWorkerEnvList, jsii.get(self, "env"))

    @builtins.property
    @jsii.member(jsii_name="git")
    def git(self) -> AppSpecWorkerGitOutputReference:
        return typing.cast(AppSpecWorkerGitOutputReference, jsii.get(self, "git"))

    @builtins.property
    @jsii.member(jsii_name="github")
    def github(self) -> AppSpecWorkerGithubOutputReference:
        return typing.cast(AppSpecWorkerGithubOutputReference, jsii.get(self, "github"))

    @builtins.property
    @jsii.member(jsii_name="gitlab")
    def gitlab(self) -> AppSpecWorkerGitlabOutputReference:
        return typing.cast(AppSpecWorkerGitlabOutputReference, jsii.get(self, "gitlab"))

    @builtins.property
    @jsii.member(jsii_name="image")
    def image(self) -> AppSpecWorkerImageOutputReference:
        return typing.cast(AppSpecWorkerImageOutputReference, jsii.get(self, "image"))

    @builtins.property
    @jsii.member(jsii_name="logDestination")
    def log_destination(self) -> AppSpecWorkerLogDestinationList:
        return typing.cast(AppSpecWorkerLogDestinationList, jsii.get(self, "logDestination"))

    @builtins.property
    @jsii.member(jsii_name="alertInput")
    def alert_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecWorkerAlert]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecWorkerAlert]]], jsii.get(self, "alertInput"))

    @builtins.property
    @jsii.member(jsii_name="buildCommandInput")
    def build_command_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "buildCommandInput"))

    @builtins.property
    @jsii.member(jsii_name="dockerfilePathInput")
    def dockerfile_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dockerfilePathInput"))

    @builtins.property
    @jsii.member(jsii_name="envInput")
    def env_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecWorkerEnv]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecWorkerEnv]]], jsii.get(self, "envInput"))

    @builtins.property
    @jsii.member(jsii_name="environmentSlugInput")
    def environment_slug_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentSlugInput"))

    @builtins.property
    @jsii.member(jsii_name="githubInput")
    def github_input(self) -> typing.Optional[AppSpecWorkerGithub]:
        return typing.cast(typing.Optional[AppSpecWorkerGithub], jsii.get(self, "githubInput"))

    @builtins.property
    @jsii.member(jsii_name="gitInput")
    def git_input(self) -> typing.Optional[AppSpecWorkerGit]:
        return typing.cast(typing.Optional[AppSpecWorkerGit], jsii.get(self, "gitInput"))

    @builtins.property
    @jsii.member(jsii_name="gitlabInput")
    def gitlab_input(self) -> typing.Optional[AppSpecWorkerGitlab]:
        return typing.cast(typing.Optional[AppSpecWorkerGitlab], jsii.get(self, "gitlabInput"))

    @builtins.property
    @jsii.member(jsii_name="imageInput")
    def image_input(self) -> typing.Optional[AppSpecWorkerImage]:
        return typing.cast(typing.Optional[AppSpecWorkerImage], jsii.get(self, "imageInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceCountInput")
    def instance_count_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "instanceCountInput"))

    @builtins.property
    @jsii.member(jsii_name="instanceSizeSlugInput")
    def instance_size_slug_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceSizeSlugInput"))

    @builtins.property
    @jsii.member(jsii_name="logDestinationInput")
    def log_destination_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecWorkerLogDestination]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[AppSpecWorkerLogDestination]]], jsii.get(self, "logDestinationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="runCommandInput")
    def run_command_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runCommandInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceDirInput")
    def source_dir_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceDirInput"))

    @builtins.property
    @jsii.member(jsii_name="buildCommand")
    def build_command(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "buildCommand"))

    @build_command.setter
    def build_command(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerOutputReference, "build_command").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buildCommand", value)

    @builtins.property
    @jsii.member(jsii_name="dockerfilePath")
    def dockerfile_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dockerfilePath"))

    @dockerfile_path.setter
    def dockerfile_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerOutputReference, "dockerfile_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dockerfilePath", value)

    @builtins.property
    @jsii.member(jsii_name="environmentSlug")
    def environment_slug(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "environmentSlug"))

    @environment_slug.setter
    def environment_slug(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerOutputReference, "environment_slug").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentSlug", value)

    @builtins.property
    @jsii.member(jsii_name="instanceCount")
    def instance_count(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "instanceCount"))

    @instance_count.setter
    def instance_count(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerOutputReference, "instance_count").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceCount", value)

    @builtins.property
    @jsii.member(jsii_name="instanceSizeSlug")
    def instance_size_slug(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instanceSizeSlug"))

    @instance_size_slug.setter
    def instance_size_slug(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerOutputReference, "instance_size_slug").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceSizeSlug", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="runCommand")
    def run_command(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runCommand"))

    @run_command.setter
    def run_command(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerOutputReference, "run_command").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runCommand", value)

    @builtins.property
    @jsii.member(jsii_name="sourceDir")
    def source_dir(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceDir"))

    @source_dir.setter
    def source_dir(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerOutputReference, "source_dir").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceDir", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppSpecWorker, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppSpecWorker, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppSpecWorker, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppSpecWorkerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-digitalocean.app.AppTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create"},
)
class AppTimeouts:
    def __init__(self, *, create: typing.Optional[builtins.str] = None) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#create App#create}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(AppTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/digitalocean/r/app#create App#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AppTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AppTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-digitalocean.app.AppTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(AppTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[AppTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[AppTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[AppTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(AppTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "App",
    "AppConfig",
    "AppSpec",
    "AppSpecAlert",
    "AppSpecAlertList",
    "AppSpecAlertOutputReference",
    "AppSpecDatabase",
    "AppSpecDatabaseList",
    "AppSpecDatabaseOutputReference",
    "AppSpecDomain",
    "AppSpecDomainList",
    "AppSpecDomainOutputReference",
    "AppSpecEnv",
    "AppSpecEnvList",
    "AppSpecEnvOutputReference",
    "AppSpecFunction",
    "AppSpecFunctionAlert",
    "AppSpecFunctionAlertList",
    "AppSpecFunctionAlertOutputReference",
    "AppSpecFunctionCors",
    "AppSpecFunctionCorsAllowOrigins",
    "AppSpecFunctionCorsAllowOriginsOutputReference",
    "AppSpecFunctionCorsOutputReference",
    "AppSpecFunctionEnv",
    "AppSpecFunctionEnvList",
    "AppSpecFunctionEnvOutputReference",
    "AppSpecFunctionGit",
    "AppSpecFunctionGitOutputReference",
    "AppSpecFunctionGithub",
    "AppSpecFunctionGithubOutputReference",
    "AppSpecFunctionGitlab",
    "AppSpecFunctionGitlabOutputReference",
    "AppSpecFunctionList",
    "AppSpecFunctionLogDestination",
    "AppSpecFunctionLogDestinationDatadog",
    "AppSpecFunctionLogDestinationDatadogOutputReference",
    "AppSpecFunctionLogDestinationList",
    "AppSpecFunctionLogDestinationLogtail",
    "AppSpecFunctionLogDestinationLogtailOutputReference",
    "AppSpecFunctionLogDestinationOutputReference",
    "AppSpecFunctionLogDestinationPapertrail",
    "AppSpecFunctionLogDestinationPapertrailOutputReference",
    "AppSpecFunctionOutputReference",
    "AppSpecFunctionRoutes",
    "AppSpecFunctionRoutesList",
    "AppSpecFunctionRoutesOutputReference",
    "AppSpecJob",
    "AppSpecJobAlert",
    "AppSpecJobAlertList",
    "AppSpecJobAlertOutputReference",
    "AppSpecJobEnv",
    "AppSpecJobEnvList",
    "AppSpecJobEnvOutputReference",
    "AppSpecJobGit",
    "AppSpecJobGitOutputReference",
    "AppSpecJobGithub",
    "AppSpecJobGithubOutputReference",
    "AppSpecJobGitlab",
    "AppSpecJobGitlabOutputReference",
    "AppSpecJobImage",
    "AppSpecJobImageDeployOnPush",
    "AppSpecJobImageDeployOnPushList",
    "AppSpecJobImageDeployOnPushOutputReference",
    "AppSpecJobImageOutputReference",
    "AppSpecJobList",
    "AppSpecJobLogDestination",
    "AppSpecJobLogDestinationDatadog",
    "AppSpecJobLogDestinationDatadogOutputReference",
    "AppSpecJobLogDestinationList",
    "AppSpecJobLogDestinationLogtail",
    "AppSpecJobLogDestinationLogtailOutputReference",
    "AppSpecJobLogDestinationOutputReference",
    "AppSpecJobLogDestinationPapertrail",
    "AppSpecJobLogDestinationPapertrailOutputReference",
    "AppSpecJobOutputReference",
    "AppSpecOutputReference",
    "AppSpecService",
    "AppSpecServiceAlert",
    "AppSpecServiceAlertList",
    "AppSpecServiceAlertOutputReference",
    "AppSpecServiceCors",
    "AppSpecServiceCorsAllowOrigins",
    "AppSpecServiceCorsAllowOriginsOutputReference",
    "AppSpecServiceCorsOutputReference",
    "AppSpecServiceEnv",
    "AppSpecServiceEnvList",
    "AppSpecServiceEnvOutputReference",
    "AppSpecServiceGit",
    "AppSpecServiceGitOutputReference",
    "AppSpecServiceGithub",
    "AppSpecServiceGithubOutputReference",
    "AppSpecServiceGitlab",
    "AppSpecServiceGitlabOutputReference",
    "AppSpecServiceHealthCheck",
    "AppSpecServiceHealthCheckOutputReference",
    "AppSpecServiceImage",
    "AppSpecServiceImageDeployOnPush",
    "AppSpecServiceImageDeployOnPushList",
    "AppSpecServiceImageDeployOnPushOutputReference",
    "AppSpecServiceImageOutputReference",
    "AppSpecServiceList",
    "AppSpecServiceLogDestination",
    "AppSpecServiceLogDestinationDatadog",
    "AppSpecServiceLogDestinationDatadogOutputReference",
    "AppSpecServiceLogDestinationList",
    "AppSpecServiceLogDestinationLogtail",
    "AppSpecServiceLogDestinationLogtailOutputReference",
    "AppSpecServiceLogDestinationOutputReference",
    "AppSpecServiceLogDestinationPapertrail",
    "AppSpecServiceLogDestinationPapertrailOutputReference",
    "AppSpecServiceOutputReference",
    "AppSpecServiceRoutes",
    "AppSpecServiceRoutesList",
    "AppSpecServiceRoutesOutputReference",
    "AppSpecStaticSite",
    "AppSpecStaticSiteCors",
    "AppSpecStaticSiteCorsAllowOrigins",
    "AppSpecStaticSiteCorsAllowOriginsOutputReference",
    "AppSpecStaticSiteCorsOutputReference",
    "AppSpecStaticSiteEnv",
    "AppSpecStaticSiteEnvList",
    "AppSpecStaticSiteEnvOutputReference",
    "AppSpecStaticSiteGit",
    "AppSpecStaticSiteGitOutputReference",
    "AppSpecStaticSiteGithub",
    "AppSpecStaticSiteGithubOutputReference",
    "AppSpecStaticSiteGitlab",
    "AppSpecStaticSiteGitlabOutputReference",
    "AppSpecStaticSiteList",
    "AppSpecStaticSiteOutputReference",
    "AppSpecStaticSiteRoutes",
    "AppSpecStaticSiteRoutesList",
    "AppSpecStaticSiteRoutesOutputReference",
    "AppSpecWorker",
    "AppSpecWorkerAlert",
    "AppSpecWorkerAlertList",
    "AppSpecWorkerAlertOutputReference",
    "AppSpecWorkerEnv",
    "AppSpecWorkerEnvList",
    "AppSpecWorkerEnvOutputReference",
    "AppSpecWorkerGit",
    "AppSpecWorkerGitOutputReference",
    "AppSpecWorkerGithub",
    "AppSpecWorkerGithubOutputReference",
    "AppSpecWorkerGitlab",
    "AppSpecWorkerGitlabOutputReference",
    "AppSpecWorkerImage",
    "AppSpecWorkerImageDeployOnPush",
    "AppSpecWorkerImageDeployOnPushList",
    "AppSpecWorkerImageDeployOnPushOutputReference",
    "AppSpecWorkerImageOutputReference",
    "AppSpecWorkerList",
    "AppSpecWorkerLogDestination",
    "AppSpecWorkerLogDestinationDatadog",
    "AppSpecWorkerLogDestinationDatadogOutputReference",
    "AppSpecWorkerLogDestinationList",
    "AppSpecWorkerLogDestinationLogtail",
    "AppSpecWorkerLogDestinationLogtailOutputReference",
    "AppSpecWorkerLogDestinationOutputReference",
    "AppSpecWorkerLogDestinationPapertrail",
    "AppSpecWorkerLogDestinationPapertrailOutputReference",
    "AppSpecWorkerOutputReference",
    "AppTimeouts",
    "AppTimeoutsOutputReference",
]

publication.publish()
