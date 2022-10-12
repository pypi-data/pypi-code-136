'''
# `azurerm_data_factory_linked_service_kusto`

Refer to the Terraform Registory for docs: [`azurerm_data_factory_linked_service_kusto`](https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto).
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


class DataFactoryLinkedServiceKusto(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryLinkedServiceKusto.DataFactoryLinkedServiceKusto",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto azurerm_data_factory_linked_service_kusto}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        data_factory_id: builtins.str,
        kusto_database_name: builtins.str,
        kusto_endpoint: builtins.str,
        name: builtins.str,
        additional_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        annotations: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        integration_runtime_name: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        service_principal_id: typing.Optional[builtins.str] = None,
        service_principal_key: typing.Optional[builtins.str] = None,
        tenant: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DataFactoryLinkedServiceKustoTimeouts", typing.Dict[str, typing.Any]]] = None,
        use_managed_identity: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto azurerm_data_factory_linked_service_kusto} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param data_factory_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#data_factory_id DataFactoryLinkedServiceKusto#data_factory_id}.
        :param kusto_database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#kusto_database_name DataFactoryLinkedServiceKusto#kusto_database_name}.
        :param kusto_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#kusto_endpoint DataFactoryLinkedServiceKusto#kusto_endpoint}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#name DataFactoryLinkedServiceKusto#name}.
        :param additional_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#additional_properties DataFactoryLinkedServiceKusto#additional_properties}.
        :param annotations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#annotations DataFactoryLinkedServiceKusto#annotations}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#description DataFactoryLinkedServiceKusto#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#id DataFactoryLinkedServiceKusto#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param integration_runtime_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#integration_runtime_name DataFactoryLinkedServiceKusto#integration_runtime_name}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#parameters DataFactoryLinkedServiceKusto#parameters}.
        :param service_principal_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#service_principal_id DataFactoryLinkedServiceKusto#service_principal_id}.
        :param service_principal_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#service_principal_key DataFactoryLinkedServiceKusto#service_principal_key}.
        :param tenant: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#tenant DataFactoryLinkedServiceKusto#tenant}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#timeouts DataFactoryLinkedServiceKusto#timeouts}
        :param use_managed_identity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#use_managed_identity DataFactoryLinkedServiceKusto#use_managed_identity}.
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryLinkedServiceKusto.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataFactoryLinkedServiceKustoConfig(
            data_factory_id=data_factory_id,
            kusto_database_name=kusto_database_name,
            kusto_endpoint=kusto_endpoint,
            name=name,
            additional_properties=additional_properties,
            annotations=annotations,
            description=description,
            id=id,
            integration_runtime_name=integration_runtime_name,
            parameters=parameters,
            service_principal_id=service_principal_id,
            service_principal_key=service_principal_key,
            tenant=tenant,
            timeouts=timeouts,
            use_managed_identity=use_managed_identity,
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
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#create DataFactoryLinkedServiceKusto#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#delete DataFactoryLinkedServiceKusto#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#read DataFactoryLinkedServiceKusto#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#update DataFactoryLinkedServiceKusto#update}.
        '''
        value = DataFactoryLinkedServiceKustoTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAdditionalProperties")
    def reset_additional_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalProperties", []))

    @jsii.member(jsii_name="resetAnnotations")
    def reset_annotations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnnotations", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIntegrationRuntimeName")
    def reset_integration_runtime_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIntegrationRuntimeName", []))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

    @jsii.member(jsii_name="resetServicePrincipalId")
    def reset_service_principal_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServicePrincipalId", []))

    @jsii.member(jsii_name="resetServicePrincipalKey")
    def reset_service_principal_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServicePrincipalKey", []))

    @jsii.member(jsii_name="resetTenant")
    def reset_tenant(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTenant", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetUseManagedIdentity")
    def reset_use_managed_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseManagedIdentity", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "DataFactoryLinkedServiceKustoTimeoutsOutputReference":
        return typing.cast("DataFactoryLinkedServiceKustoTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="additionalPropertiesInput")
    def additional_properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "additionalPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="annotationsInput")
    def annotations_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "annotationsInput"))

    @builtins.property
    @jsii.member(jsii_name="dataFactoryIdInput")
    def data_factory_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataFactoryIdInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="integrationRuntimeNameInput")
    def integration_runtime_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "integrationRuntimeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="kustoDatabaseNameInput")
    def kusto_database_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kustoDatabaseNameInput"))

    @builtins.property
    @jsii.member(jsii_name="kustoEndpointInput")
    def kusto_endpoint_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kustoEndpointInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="servicePrincipalIdInput")
    def service_principal_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "servicePrincipalIdInput"))

    @builtins.property
    @jsii.member(jsii_name="servicePrincipalKeyInput")
    def service_principal_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "servicePrincipalKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="tenantInput")
    def tenant_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tenantInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DataFactoryLinkedServiceKustoTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DataFactoryLinkedServiceKustoTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="useManagedIdentityInput")
    def use_managed_identity_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useManagedIdentityInput"))

    @builtins.property
    @jsii.member(jsii_name="additionalProperties")
    def additional_properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "additionalProperties"))

    @additional_properties.setter
    def additional_properties(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceKusto, "additional_properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalProperties", value)

    @builtins.property
    @jsii.member(jsii_name="annotations")
    def annotations(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "annotations"))

    @annotations.setter
    def annotations(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceKusto, "annotations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="dataFactoryId")
    def data_factory_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataFactoryId"))

    @data_factory_id.setter
    def data_factory_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceKusto, "data_factory_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataFactoryId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceKusto, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceKusto, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="integrationRuntimeName")
    def integration_runtime_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "integrationRuntimeName"))

    @integration_runtime_name.setter
    def integration_runtime_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceKusto, "integration_runtime_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "integrationRuntimeName", value)

    @builtins.property
    @jsii.member(jsii_name="kustoDatabaseName")
    def kusto_database_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kustoDatabaseName"))

    @kusto_database_name.setter
    def kusto_database_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceKusto, "kusto_database_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kustoDatabaseName", value)

    @builtins.property
    @jsii.member(jsii_name="kustoEndpoint")
    def kusto_endpoint(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kustoEndpoint"))

    @kusto_endpoint.setter
    def kusto_endpoint(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceKusto, "kusto_endpoint").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kustoEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceKusto, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceKusto, "parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="servicePrincipalId")
    def service_principal_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "servicePrincipalId"))

    @service_principal_id.setter
    def service_principal_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceKusto, "service_principal_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servicePrincipalId", value)

    @builtins.property
    @jsii.member(jsii_name="servicePrincipalKey")
    def service_principal_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "servicePrincipalKey"))

    @service_principal_key.setter
    def service_principal_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceKusto, "service_principal_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servicePrincipalKey", value)

    @builtins.property
    @jsii.member(jsii_name="tenant")
    def tenant(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tenant"))

    @tenant.setter
    def tenant(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceKusto, "tenant").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tenant", value)

    @builtins.property
    @jsii.member(jsii_name="useManagedIdentity")
    def use_managed_identity(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "useManagedIdentity"))

    @use_managed_identity.setter
    def use_managed_identity(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceKusto, "use_managed_identity").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useManagedIdentity", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryLinkedServiceKusto.DataFactoryLinkedServiceKustoConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "data_factory_id": "dataFactoryId",
        "kusto_database_name": "kustoDatabaseName",
        "kusto_endpoint": "kustoEndpoint",
        "name": "name",
        "additional_properties": "additionalProperties",
        "annotations": "annotations",
        "description": "description",
        "id": "id",
        "integration_runtime_name": "integrationRuntimeName",
        "parameters": "parameters",
        "service_principal_id": "servicePrincipalId",
        "service_principal_key": "servicePrincipalKey",
        "tenant": "tenant",
        "timeouts": "timeouts",
        "use_managed_identity": "useManagedIdentity",
    },
)
class DataFactoryLinkedServiceKustoConfig(cdktf.TerraformMetaArguments):
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
        data_factory_id: builtins.str,
        kusto_database_name: builtins.str,
        kusto_endpoint: builtins.str,
        name: builtins.str,
        additional_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        annotations: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        integration_runtime_name: typing.Optional[builtins.str] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        service_principal_id: typing.Optional[builtins.str] = None,
        service_principal_key: typing.Optional[builtins.str] = None,
        tenant: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["DataFactoryLinkedServiceKustoTimeouts", typing.Dict[str, typing.Any]]] = None,
        use_managed_identity: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param data_factory_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#data_factory_id DataFactoryLinkedServiceKusto#data_factory_id}.
        :param kusto_database_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#kusto_database_name DataFactoryLinkedServiceKusto#kusto_database_name}.
        :param kusto_endpoint: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#kusto_endpoint DataFactoryLinkedServiceKusto#kusto_endpoint}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#name DataFactoryLinkedServiceKusto#name}.
        :param additional_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#additional_properties DataFactoryLinkedServiceKusto#additional_properties}.
        :param annotations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#annotations DataFactoryLinkedServiceKusto#annotations}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#description DataFactoryLinkedServiceKusto#description}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#id DataFactoryLinkedServiceKusto#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param integration_runtime_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#integration_runtime_name DataFactoryLinkedServiceKusto#integration_runtime_name}.
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#parameters DataFactoryLinkedServiceKusto#parameters}.
        :param service_principal_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#service_principal_id DataFactoryLinkedServiceKusto#service_principal_id}.
        :param service_principal_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#service_principal_key DataFactoryLinkedServiceKusto#service_principal_key}.
        :param tenant: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#tenant DataFactoryLinkedServiceKusto#tenant}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#timeouts DataFactoryLinkedServiceKusto#timeouts}
        :param use_managed_identity: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#use_managed_identity DataFactoryLinkedServiceKusto#use_managed_identity}.
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = DataFactoryLinkedServiceKustoTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryLinkedServiceKustoConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument data_factory_id", value=data_factory_id, expected_type=type_hints["data_factory_id"])
            check_type(argname="argument kusto_database_name", value=kusto_database_name, expected_type=type_hints["kusto_database_name"])
            check_type(argname="argument kusto_endpoint", value=kusto_endpoint, expected_type=type_hints["kusto_endpoint"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument additional_properties", value=additional_properties, expected_type=type_hints["additional_properties"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument integration_runtime_name", value=integration_runtime_name, expected_type=type_hints["integration_runtime_name"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument service_principal_id", value=service_principal_id, expected_type=type_hints["service_principal_id"])
            check_type(argname="argument service_principal_key", value=service_principal_key, expected_type=type_hints["service_principal_key"])
            check_type(argname="argument tenant", value=tenant, expected_type=type_hints["tenant"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument use_managed_identity", value=use_managed_identity, expected_type=type_hints["use_managed_identity"])
        self._values: typing.Dict[str, typing.Any] = {
            "data_factory_id": data_factory_id,
            "kusto_database_name": kusto_database_name,
            "kusto_endpoint": kusto_endpoint,
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
        if additional_properties is not None:
            self._values["additional_properties"] = additional_properties
        if annotations is not None:
            self._values["annotations"] = annotations
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if integration_runtime_name is not None:
            self._values["integration_runtime_name"] = integration_runtime_name
        if parameters is not None:
            self._values["parameters"] = parameters
        if service_principal_id is not None:
            self._values["service_principal_id"] = service_principal_id
        if service_principal_key is not None:
            self._values["service_principal_key"] = service_principal_key
        if tenant is not None:
            self._values["tenant"] = tenant
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if use_managed_identity is not None:
            self._values["use_managed_identity"] = use_managed_identity

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
    def data_factory_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#data_factory_id DataFactoryLinkedServiceKusto#data_factory_id}.'''
        result = self._values.get("data_factory_id")
        assert result is not None, "Required property 'data_factory_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kusto_database_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#kusto_database_name DataFactoryLinkedServiceKusto#kusto_database_name}.'''
        result = self._values.get("kusto_database_name")
        assert result is not None, "Required property 'kusto_database_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kusto_endpoint(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#kusto_endpoint DataFactoryLinkedServiceKusto#kusto_endpoint}.'''
        result = self._values.get("kusto_endpoint")
        assert result is not None, "Required property 'kusto_endpoint' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#name DataFactoryLinkedServiceKusto#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_properties(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#additional_properties DataFactoryLinkedServiceKusto#additional_properties}.'''
        result = self._values.get("additional_properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def annotations(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#annotations DataFactoryLinkedServiceKusto#annotations}.'''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#description DataFactoryLinkedServiceKusto#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#id DataFactoryLinkedServiceKusto#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def integration_runtime_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#integration_runtime_name DataFactoryLinkedServiceKusto#integration_runtime_name}.'''
        result = self._values.get("integration_runtime_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#parameters DataFactoryLinkedServiceKusto#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def service_principal_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#service_principal_id DataFactoryLinkedServiceKusto#service_principal_id}.'''
        result = self._values.get("service_principal_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service_principal_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#service_principal_key DataFactoryLinkedServiceKusto#service_principal_key}.'''
        result = self._values.get("service_principal_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tenant(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#tenant DataFactoryLinkedServiceKusto#tenant}.'''
        result = self._values.get("tenant")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["DataFactoryLinkedServiceKustoTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#timeouts DataFactoryLinkedServiceKusto#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DataFactoryLinkedServiceKustoTimeouts"], result)

    @builtins.property
    def use_managed_identity(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#use_managed_identity DataFactoryLinkedServiceKusto#use_managed_identity}.'''
        result = self._values.get("use_managed_identity")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryLinkedServiceKustoConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryLinkedServiceKusto.DataFactoryLinkedServiceKustoTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class DataFactoryLinkedServiceKustoTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#create DataFactoryLinkedServiceKusto#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#delete DataFactoryLinkedServiceKusto#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#read DataFactoryLinkedServiceKusto#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#update DataFactoryLinkedServiceKusto#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryLinkedServiceKustoTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if read is not None:
            self._values["read"] = read
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#create DataFactoryLinkedServiceKusto#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#delete DataFactoryLinkedServiceKusto#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#read DataFactoryLinkedServiceKusto#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_kusto#update DataFactoryLinkedServiceKusto#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryLinkedServiceKustoTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataFactoryLinkedServiceKustoTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryLinkedServiceKusto.DataFactoryLinkedServiceKustoTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(DataFactoryLinkedServiceKustoTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @jsii.member(jsii_name="resetRead")
    def reset_read(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRead", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="readInput")
    def read_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "readInput"))

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
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceKustoTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceKustoTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceKustoTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceKustoTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataFactoryLinkedServiceKustoTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataFactoryLinkedServiceKustoTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataFactoryLinkedServiceKustoTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceKustoTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataFactoryLinkedServiceKusto",
    "DataFactoryLinkedServiceKustoConfig",
    "DataFactoryLinkedServiceKustoTimeouts",
    "DataFactoryLinkedServiceKustoTimeoutsOutputReference",
]

publication.publish()
