'''
# `cloudflare_worker_script`

Refer to the Terraform Registory for docs: [`cloudflare_worker_script`](https://www.terraform.io/docs/providers/cloudflare/r/worker_script).
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


class WorkerScript(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.workerScript.WorkerScript",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script cloudflare_worker_script}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        content: builtins.str,
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        kv_namespace_binding: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkerScriptKvNamespaceBinding", typing.Dict[str, typing.Any]]]]] = None,
        module: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        plain_text_binding: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkerScriptPlainTextBinding", typing.Dict[str, typing.Any]]]]] = None,
        r2_bucket_binding: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkerScriptR2BucketBinding", typing.Dict[str, typing.Any]]]]] = None,
        secret_text_binding: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkerScriptSecretTextBinding", typing.Dict[str, typing.Any]]]]] = None,
        service_binding: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkerScriptServiceBinding", typing.Dict[str, typing.Any]]]]] = None,
        webassembly_binding: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkerScriptWebassemblyBinding", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script cloudflare_worker_script} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param content: The script content. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#content WorkerScript#content}
        :param name: The name for the script. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#name WorkerScript#name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#id WorkerScript#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kv_namespace_binding: kv_namespace_binding block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#kv_namespace_binding WorkerScript#kv_namespace_binding}
        :param module: Whether to upload Worker as a module. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#module WorkerScript#module}
        :param plain_text_binding: plain_text_binding block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#plain_text_binding WorkerScript#plain_text_binding}
        :param r2_bucket_binding: r2_bucket_binding block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#r2_bucket_binding WorkerScript#r2_bucket_binding}
        :param secret_text_binding: secret_text_binding block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#secret_text_binding WorkerScript#secret_text_binding}
        :param service_binding: service_binding block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#service_binding WorkerScript#service_binding}
        :param webassembly_binding: webassembly_binding block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#webassembly_binding WorkerScript#webassembly_binding}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WorkerScript.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = WorkerScriptConfig(
            content=content,
            name=name,
            id=id,
            kv_namespace_binding=kv_namespace_binding,
            module=module,
            plain_text_binding=plain_text_binding,
            r2_bucket_binding=r2_bucket_binding,
            secret_text_binding=secret_text_binding,
            service_binding=service_binding,
            webassembly_binding=webassembly_binding,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putKvNamespaceBinding")
    def put_kv_namespace_binding(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkerScriptKvNamespaceBinding", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WorkerScript.put_kv_namespace_binding)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putKvNamespaceBinding", [value]))

    @jsii.member(jsii_name="putPlainTextBinding")
    def put_plain_text_binding(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkerScriptPlainTextBinding", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WorkerScript.put_plain_text_binding)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putPlainTextBinding", [value]))

    @jsii.member(jsii_name="putR2BucketBinding")
    def put_r2_bucket_binding(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkerScriptR2BucketBinding", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WorkerScript.put_r2_bucket_binding)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putR2BucketBinding", [value]))

    @jsii.member(jsii_name="putSecretTextBinding")
    def put_secret_text_binding(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkerScriptSecretTextBinding", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WorkerScript.put_secret_text_binding)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSecretTextBinding", [value]))

    @jsii.member(jsii_name="putServiceBinding")
    def put_service_binding(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkerScriptServiceBinding", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WorkerScript.put_service_binding)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putServiceBinding", [value]))

    @jsii.member(jsii_name="putWebassemblyBinding")
    def put_webassembly_binding(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkerScriptWebassemblyBinding", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WorkerScript.put_webassembly_binding)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWebassemblyBinding", [value]))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetKvNamespaceBinding")
    def reset_kv_namespace_binding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKvNamespaceBinding", []))

    @jsii.member(jsii_name="resetModule")
    def reset_module(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetModule", []))

    @jsii.member(jsii_name="resetPlainTextBinding")
    def reset_plain_text_binding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPlainTextBinding", []))

    @jsii.member(jsii_name="resetR2BucketBinding")
    def reset_r2_bucket_binding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetR2BucketBinding", []))

    @jsii.member(jsii_name="resetSecretTextBinding")
    def reset_secret_text_binding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecretTextBinding", []))

    @jsii.member(jsii_name="resetServiceBinding")
    def reset_service_binding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceBinding", []))

    @jsii.member(jsii_name="resetWebassemblyBinding")
    def reset_webassembly_binding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebassemblyBinding", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="kvNamespaceBinding")
    def kv_namespace_binding(self) -> "WorkerScriptKvNamespaceBindingList":
        return typing.cast("WorkerScriptKvNamespaceBindingList", jsii.get(self, "kvNamespaceBinding"))

    @builtins.property
    @jsii.member(jsii_name="plainTextBinding")
    def plain_text_binding(self) -> "WorkerScriptPlainTextBindingList":
        return typing.cast("WorkerScriptPlainTextBindingList", jsii.get(self, "plainTextBinding"))

    @builtins.property
    @jsii.member(jsii_name="r2BucketBinding")
    def r2_bucket_binding(self) -> "WorkerScriptR2BucketBindingList":
        return typing.cast("WorkerScriptR2BucketBindingList", jsii.get(self, "r2BucketBinding"))

    @builtins.property
    @jsii.member(jsii_name="secretTextBinding")
    def secret_text_binding(self) -> "WorkerScriptSecretTextBindingList":
        return typing.cast("WorkerScriptSecretTextBindingList", jsii.get(self, "secretTextBinding"))

    @builtins.property
    @jsii.member(jsii_name="serviceBinding")
    def service_binding(self) -> "WorkerScriptServiceBindingList":
        return typing.cast("WorkerScriptServiceBindingList", jsii.get(self, "serviceBinding"))

    @builtins.property
    @jsii.member(jsii_name="webassemblyBinding")
    def webassembly_binding(self) -> "WorkerScriptWebassemblyBindingList":
        return typing.cast("WorkerScriptWebassemblyBindingList", jsii.get(self, "webassemblyBinding"))

    @builtins.property
    @jsii.member(jsii_name="contentInput")
    def content_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="kvNamespaceBindingInput")
    def kv_namespace_binding_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkerScriptKvNamespaceBinding"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkerScriptKvNamespaceBinding"]]], jsii.get(self, "kvNamespaceBindingInput"))

    @builtins.property
    @jsii.member(jsii_name="moduleInput")
    def module_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "moduleInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="plainTextBindingInput")
    def plain_text_binding_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkerScriptPlainTextBinding"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkerScriptPlainTextBinding"]]], jsii.get(self, "plainTextBindingInput"))

    @builtins.property
    @jsii.member(jsii_name="r2BucketBindingInput")
    def r2_bucket_binding_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkerScriptR2BucketBinding"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkerScriptR2BucketBinding"]]], jsii.get(self, "r2BucketBindingInput"))

    @builtins.property
    @jsii.member(jsii_name="secretTextBindingInput")
    def secret_text_binding_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkerScriptSecretTextBinding"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkerScriptSecretTextBinding"]]], jsii.get(self, "secretTextBindingInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceBindingInput")
    def service_binding_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkerScriptServiceBinding"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkerScriptServiceBinding"]]], jsii.get(self, "serviceBindingInput"))

    @builtins.property
    @jsii.member(jsii_name="webassemblyBindingInput")
    def webassembly_binding_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkerScriptWebassemblyBinding"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkerScriptWebassemblyBinding"]]], jsii.get(self, "webassemblyBindingInput"))

    @builtins.property
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScript, "content").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScript, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="module")
    def module(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "module"))

    @module.setter
    def module(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScript, "module").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "module", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScript, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.workerScript.WorkerScriptConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "content": "content",
        "name": "name",
        "id": "id",
        "kv_namespace_binding": "kvNamespaceBinding",
        "module": "module",
        "plain_text_binding": "plainTextBinding",
        "r2_bucket_binding": "r2BucketBinding",
        "secret_text_binding": "secretTextBinding",
        "service_binding": "serviceBinding",
        "webassembly_binding": "webassemblyBinding",
    },
)
class WorkerScriptConfig(cdktf.TerraformMetaArguments):
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
        content: builtins.str,
        name: builtins.str,
        id: typing.Optional[builtins.str] = None,
        kv_namespace_binding: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkerScriptKvNamespaceBinding", typing.Dict[str, typing.Any]]]]] = None,
        module: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        plain_text_binding: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkerScriptPlainTextBinding", typing.Dict[str, typing.Any]]]]] = None,
        r2_bucket_binding: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkerScriptR2BucketBinding", typing.Dict[str, typing.Any]]]]] = None,
        secret_text_binding: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkerScriptSecretTextBinding", typing.Dict[str, typing.Any]]]]] = None,
        service_binding: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkerScriptServiceBinding", typing.Dict[str, typing.Any]]]]] = None,
        webassembly_binding: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["WorkerScriptWebassemblyBinding", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param content: The script content. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#content WorkerScript#content}
        :param name: The name for the script. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#name WorkerScript#name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#id WorkerScript#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param kv_namespace_binding: kv_namespace_binding block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#kv_namespace_binding WorkerScript#kv_namespace_binding}
        :param module: Whether to upload Worker as a module. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#module WorkerScript#module}
        :param plain_text_binding: plain_text_binding block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#plain_text_binding WorkerScript#plain_text_binding}
        :param r2_bucket_binding: r2_bucket_binding block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#r2_bucket_binding WorkerScript#r2_bucket_binding}
        :param secret_text_binding: secret_text_binding block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#secret_text_binding WorkerScript#secret_text_binding}
        :param service_binding: service_binding block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#service_binding WorkerScript#service_binding}
        :param webassembly_binding: webassembly_binding block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#webassembly_binding WorkerScript#webassembly_binding}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(WorkerScriptConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument kv_namespace_binding", value=kv_namespace_binding, expected_type=type_hints["kv_namespace_binding"])
            check_type(argname="argument module", value=module, expected_type=type_hints["module"])
            check_type(argname="argument plain_text_binding", value=plain_text_binding, expected_type=type_hints["plain_text_binding"])
            check_type(argname="argument r2_bucket_binding", value=r2_bucket_binding, expected_type=type_hints["r2_bucket_binding"])
            check_type(argname="argument secret_text_binding", value=secret_text_binding, expected_type=type_hints["secret_text_binding"])
            check_type(argname="argument service_binding", value=service_binding, expected_type=type_hints["service_binding"])
            check_type(argname="argument webassembly_binding", value=webassembly_binding, expected_type=type_hints["webassembly_binding"])
        self._values: typing.Dict[str, typing.Any] = {
            "content": content,
            "name": name,
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
        if kv_namespace_binding is not None:
            self._values["kv_namespace_binding"] = kv_namespace_binding
        if module is not None:
            self._values["module"] = module
        if plain_text_binding is not None:
            self._values["plain_text_binding"] = plain_text_binding
        if r2_bucket_binding is not None:
            self._values["r2_bucket_binding"] = r2_bucket_binding
        if secret_text_binding is not None:
            self._values["secret_text_binding"] = secret_text_binding
        if service_binding is not None:
            self._values["service_binding"] = service_binding
        if webassembly_binding is not None:
            self._values["webassembly_binding"] = webassembly_binding

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
    def content(self) -> builtins.str:
        '''The script content.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#content WorkerScript#content}
        '''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name for the script.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#name WorkerScript#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#id WorkerScript#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kv_namespace_binding(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkerScriptKvNamespaceBinding"]]]:
        '''kv_namespace_binding block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#kv_namespace_binding WorkerScript#kv_namespace_binding}
        '''
        result = self._values.get("kv_namespace_binding")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkerScriptKvNamespaceBinding"]]], result)

    @builtins.property
    def module(self) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to upload Worker as a module.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#module WorkerScript#module}
        '''
        result = self._values.get("module")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def plain_text_binding(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkerScriptPlainTextBinding"]]]:
        '''plain_text_binding block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#plain_text_binding WorkerScript#plain_text_binding}
        '''
        result = self._values.get("plain_text_binding")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkerScriptPlainTextBinding"]]], result)

    @builtins.property
    def r2_bucket_binding(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkerScriptR2BucketBinding"]]]:
        '''r2_bucket_binding block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#r2_bucket_binding WorkerScript#r2_bucket_binding}
        '''
        result = self._values.get("r2_bucket_binding")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkerScriptR2BucketBinding"]]], result)

    @builtins.property
    def secret_text_binding(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkerScriptSecretTextBinding"]]]:
        '''secret_text_binding block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#secret_text_binding WorkerScript#secret_text_binding}
        '''
        result = self._values.get("secret_text_binding")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkerScriptSecretTextBinding"]]], result)

    @builtins.property
    def service_binding(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkerScriptServiceBinding"]]]:
        '''service_binding block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#service_binding WorkerScript#service_binding}
        '''
        result = self._values.get("service_binding")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkerScriptServiceBinding"]]], result)

    @builtins.property
    def webassembly_binding(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkerScriptWebassemblyBinding"]]]:
        '''webassembly_binding block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#webassembly_binding WorkerScript#webassembly_binding}
        '''
        result = self._values.get("webassembly_binding")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["WorkerScriptWebassemblyBinding"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkerScriptConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.workerScript.WorkerScriptKvNamespaceBinding",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "namespace_id": "namespaceId"},
)
class WorkerScriptKvNamespaceBinding:
    def __init__(self, *, name: builtins.str, namespace_id: builtins.str) -> None:
        '''
        :param name: The global variable for the binding in your Worker code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#name WorkerScript#name}
        :param namespace_id: ID of the KV namespace you want to use. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#namespace_id WorkerScript#namespace_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WorkerScriptKvNamespaceBinding.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument namespace_id", value=namespace_id, expected_type=type_hints["namespace_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "namespace_id": namespace_id,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''The global variable for the binding in your Worker code.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#name WorkerScript#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def namespace_id(self) -> builtins.str:
        '''ID of the KV namespace you want to use.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#namespace_id WorkerScript#namespace_id}
        '''
        result = self._values.get("namespace_id")
        assert result is not None, "Required property 'namespace_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkerScriptKvNamespaceBinding(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WorkerScriptKvNamespaceBindingList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.workerScript.WorkerScriptKvNamespaceBindingList",
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
            type_hints = typing.get_type_hints(WorkerScriptKvNamespaceBindingList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WorkerScriptKvNamespaceBindingOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WorkerScriptKvNamespaceBindingList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WorkerScriptKvNamespaceBindingOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScriptKvNamespaceBindingList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(WorkerScriptKvNamespaceBindingList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(WorkerScriptKvNamespaceBindingList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkerScriptKvNamespaceBinding]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkerScriptKvNamespaceBinding]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkerScriptKvNamespaceBinding]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScriptKvNamespaceBindingList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WorkerScriptKvNamespaceBindingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.workerScript.WorkerScriptKvNamespaceBindingOutputReference",
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
            type_hints = typing.get_type_hints(WorkerScriptKvNamespaceBindingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceIdInput")
    def namespace_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScriptKvNamespaceBindingOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="namespaceId")
    def namespace_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespaceId"))

    @namespace_id.setter
    def namespace_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScriptKvNamespaceBindingOutputReference, "namespace_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespaceId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WorkerScriptKvNamespaceBinding, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WorkerScriptKvNamespaceBinding, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WorkerScriptKvNamespaceBinding, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScriptKvNamespaceBindingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.workerScript.WorkerScriptPlainTextBinding",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "text": "text"},
)
class WorkerScriptPlainTextBinding:
    def __init__(self, *, name: builtins.str, text: builtins.str) -> None:
        '''
        :param name: The global variable for the binding in your Worker code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#name WorkerScript#name}
        :param text: The plain text you want to store. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#text WorkerScript#text}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WorkerScriptPlainTextBinding.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument text", value=text, expected_type=type_hints["text"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "text": text,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''The global variable for the binding in your Worker code.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#name WorkerScript#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def text(self) -> builtins.str:
        '''The plain text you want to store.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#text WorkerScript#text}
        '''
        result = self._values.get("text")
        assert result is not None, "Required property 'text' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkerScriptPlainTextBinding(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WorkerScriptPlainTextBindingList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.workerScript.WorkerScriptPlainTextBindingList",
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
            type_hints = typing.get_type_hints(WorkerScriptPlainTextBindingList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "WorkerScriptPlainTextBindingOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WorkerScriptPlainTextBindingList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WorkerScriptPlainTextBindingOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScriptPlainTextBindingList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(WorkerScriptPlainTextBindingList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(WorkerScriptPlainTextBindingList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkerScriptPlainTextBinding]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkerScriptPlainTextBinding]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkerScriptPlainTextBinding]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScriptPlainTextBindingList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WorkerScriptPlainTextBindingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.workerScript.WorkerScriptPlainTextBindingOutputReference",
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
            type_hints = typing.get_type_hints(WorkerScriptPlainTextBindingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="textInput")
    def text_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "textInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScriptPlainTextBindingOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="text")
    def text(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "text"))

    @text.setter
    def text(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScriptPlainTextBindingOutputReference, "text").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "text", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WorkerScriptPlainTextBinding, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WorkerScriptPlainTextBinding, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WorkerScriptPlainTextBinding, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScriptPlainTextBindingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.workerScript.WorkerScriptR2BucketBinding",
    jsii_struct_bases=[],
    name_mapping={"bucket_name": "bucketName", "name": "name"},
)
class WorkerScriptR2BucketBinding:
    def __init__(self, *, bucket_name: builtins.str, name: builtins.str) -> None:
        '''
        :param bucket_name: The name of the Bucket to bind to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#bucket_name WorkerScript#bucket_name}
        :param name: The global variable for the binding in your Worker code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#name WorkerScript#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WorkerScriptR2BucketBinding.__init__)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "bucket_name": bucket_name,
            "name": name,
        }

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''The name of the Bucket to bind to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#bucket_name WorkerScript#bucket_name}
        '''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The global variable for the binding in your Worker code.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#name WorkerScript#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkerScriptR2BucketBinding(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WorkerScriptR2BucketBindingList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.workerScript.WorkerScriptR2BucketBindingList",
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
            type_hints = typing.get_type_hints(WorkerScriptR2BucketBindingList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "WorkerScriptR2BucketBindingOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WorkerScriptR2BucketBindingList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WorkerScriptR2BucketBindingOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScriptR2BucketBindingList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(WorkerScriptR2BucketBindingList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(WorkerScriptR2BucketBindingList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkerScriptR2BucketBinding]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkerScriptR2BucketBinding]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkerScriptR2BucketBinding]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScriptR2BucketBindingList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WorkerScriptR2BucketBindingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.workerScript.WorkerScriptR2BucketBindingOutputReference",
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
            type_hints = typing.get_type_hints(WorkerScriptR2BucketBindingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="bucketNameInput")
    def bucket_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "bucketNameInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="bucketName")
    def bucket_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "bucketName"))

    @bucket_name.setter
    def bucket_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScriptR2BucketBindingOutputReference, "bucket_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bucketName", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScriptR2BucketBindingOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WorkerScriptR2BucketBinding, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WorkerScriptR2BucketBinding, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WorkerScriptR2BucketBinding, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScriptR2BucketBindingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.workerScript.WorkerScriptSecretTextBinding",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "text": "text"},
)
class WorkerScriptSecretTextBinding:
    def __init__(self, *, name: builtins.str, text: builtins.str) -> None:
        '''
        :param name: The global variable for the binding in your Worker code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#name WorkerScript#name}
        :param text: The secret text you want to store. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#text WorkerScript#text}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WorkerScriptSecretTextBinding.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument text", value=text, expected_type=type_hints["text"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "text": text,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''The global variable for the binding in your Worker code.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#name WorkerScript#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def text(self) -> builtins.str:
        '''The secret text you want to store.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#text WorkerScript#text}
        '''
        result = self._values.get("text")
        assert result is not None, "Required property 'text' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkerScriptSecretTextBinding(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WorkerScriptSecretTextBindingList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.workerScript.WorkerScriptSecretTextBindingList",
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
            type_hints = typing.get_type_hints(WorkerScriptSecretTextBindingList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "WorkerScriptSecretTextBindingOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WorkerScriptSecretTextBindingList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WorkerScriptSecretTextBindingOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScriptSecretTextBindingList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(WorkerScriptSecretTextBindingList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(WorkerScriptSecretTextBindingList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkerScriptSecretTextBinding]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkerScriptSecretTextBinding]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkerScriptSecretTextBinding]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScriptSecretTextBindingList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WorkerScriptSecretTextBindingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.workerScript.WorkerScriptSecretTextBindingOutputReference",
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
            type_hints = typing.get_type_hints(WorkerScriptSecretTextBindingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="textInput")
    def text_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "textInput"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScriptSecretTextBindingOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="text")
    def text(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "text"))

    @text.setter
    def text(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScriptSecretTextBindingOutputReference, "text").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "text", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WorkerScriptSecretTextBinding, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WorkerScriptSecretTextBinding, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WorkerScriptSecretTextBinding, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScriptSecretTextBindingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.workerScript.WorkerScriptServiceBinding",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "service": "service", "environment": "environment"},
)
class WorkerScriptServiceBinding:
    def __init__(
        self,
        *,
        name: builtins.str,
        service: builtins.str,
        environment: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: The global variable for the binding in your Worker code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#name WorkerScript#name}
        :param service: The name of the Worker to bind to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#service WorkerScript#service}
        :param environment: The name of the Worker environment to bind to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#environment WorkerScript#environment}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WorkerScriptServiceBinding.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "service": service,
        }
        if environment is not None:
            self._values["environment"] = environment

    @builtins.property
    def name(self) -> builtins.str:
        '''The global variable for the binding in your Worker code.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#name WorkerScript#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service(self) -> builtins.str:
        '''The name of the Worker to bind to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#service WorkerScript#service}
        '''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment(self) -> typing.Optional[builtins.str]:
        '''The name of the Worker environment to bind to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#environment WorkerScript#environment}
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkerScriptServiceBinding(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WorkerScriptServiceBindingList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.workerScript.WorkerScriptServiceBindingList",
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
            type_hints = typing.get_type_hints(WorkerScriptServiceBindingList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "WorkerScriptServiceBindingOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WorkerScriptServiceBindingList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WorkerScriptServiceBindingOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScriptServiceBindingList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(WorkerScriptServiceBindingList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(WorkerScriptServiceBindingList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkerScriptServiceBinding]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkerScriptServiceBinding]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkerScriptServiceBinding]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScriptServiceBindingList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WorkerScriptServiceBindingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.workerScript.WorkerScriptServiceBindingOutputReference",
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
            type_hints = typing.get_type_hints(WorkerScriptServiceBindingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEnvironment")
    def reset_environment(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnvironment", []))

    @builtins.property
    @jsii.member(jsii_name="environmentInput")
    def environment_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "environmentInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceInput")
    def service_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceInput"))

    @builtins.property
    @jsii.member(jsii_name="environment")
    def environment(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "environment"))

    @environment.setter
    def environment(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScriptServiceBindingOutputReference, "environment").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environment", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScriptServiceBindingOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "service"))

    @service.setter
    def service(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScriptServiceBindingOutputReference, "service").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WorkerScriptServiceBinding, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WorkerScriptServiceBinding, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WorkerScriptServiceBinding, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScriptServiceBindingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-cloudflare.workerScript.WorkerScriptWebassemblyBinding",
    jsii_struct_bases=[],
    name_mapping={"module": "module", "name": "name"},
)
class WorkerScriptWebassemblyBinding:
    def __init__(self, *, module: builtins.str, name: builtins.str) -> None:
        '''
        :param module: The base64 encoded wasm module you want to store. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#module WorkerScript#module}
        :param name: The global variable for the binding in your Worker code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#name WorkerScript#name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WorkerScriptWebassemblyBinding.__init__)
            check_type(argname="argument module", value=module, expected_type=type_hints["module"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        self._values: typing.Dict[str, typing.Any] = {
            "module": module,
            "name": name,
        }

    @builtins.property
    def module(self) -> builtins.str:
        '''The base64 encoded wasm module you want to store.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#module WorkerScript#module}
        '''
        result = self._values.get("module")
        assert result is not None, "Required property 'module' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The global variable for the binding in your Worker code.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/cloudflare/r/worker_script#name WorkerScript#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkerScriptWebassemblyBinding(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WorkerScriptWebassemblyBindingList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.workerScript.WorkerScriptWebassemblyBindingList",
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
            type_hints = typing.get_type_hints(WorkerScriptWebassemblyBindingList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "WorkerScriptWebassemblyBindingOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(WorkerScriptWebassemblyBindingList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("WorkerScriptWebassemblyBindingOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScriptWebassemblyBindingList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(WorkerScriptWebassemblyBindingList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(WorkerScriptWebassemblyBindingList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkerScriptWebassemblyBinding]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkerScriptWebassemblyBinding]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[WorkerScriptWebassemblyBinding]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScriptWebassemblyBindingList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class WorkerScriptWebassemblyBindingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-cloudflare.workerScript.WorkerScriptWebassemblyBindingOutputReference",
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
            type_hints = typing.get_type_hints(WorkerScriptWebassemblyBindingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="moduleInput")
    def module_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "moduleInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="module")
    def module(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "module"))

    @module.setter
    def module(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScriptWebassemblyBindingOutputReference, "module").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "module", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScriptWebassemblyBindingOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[WorkerScriptWebassemblyBinding, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[WorkerScriptWebassemblyBinding, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[WorkerScriptWebassemblyBinding, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(WorkerScriptWebassemblyBindingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "WorkerScript",
    "WorkerScriptConfig",
    "WorkerScriptKvNamespaceBinding",
    "WorkerScriptKvNamespaceBindingList",
    "WorkerScriptKvNamespaceBindingOutputReference",
    "WorkerScriptPlainTextBinding",
    "WorkerScriptPlainTextBindingList",
    "WorkerScriptPlainTextBindingOutputReference",
    "WorkerScriptR2BucketBinding",
    "WorkerScriptR2BucketBindingList",
    "WorkerScriptR2BucketBindingOutputReference",
    "WorkerScriptSecretTextBinding",
    "WorkerScriptSecretTextBindingList",
    "WorkerScriptSecretTextBindingOutputReference",
    "WorkerScriptServiceBinding",
    "WorkerScriptServiceBindingList",
    "WorkerScriptServiceBindingOutputReference",
    "WorkerScriptWebassemblyBinding",
    "WorkerScriptWebassemblyBindingList",
    "WorkerScriptWebassemblyBindingOutputReference",
]

publication.publish()
