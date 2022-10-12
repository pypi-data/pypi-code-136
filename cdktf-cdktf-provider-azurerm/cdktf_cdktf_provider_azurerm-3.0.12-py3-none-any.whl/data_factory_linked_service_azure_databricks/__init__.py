'''
# `azurerm_data_factory_linked_service_azure_databricks`

Refer to the Terraform Registory for docs: [`azurerm_data_factory_linked_service_azure_databricks`](https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks).
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


class DataFactoryLinkedServiceAzureDatabricks(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryLinkedServiceAzureDatabricks.DataFactoryLinkedServiceAzureDatabricks",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks azurerm_data_factory_linked_service_azure_databricks}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        adb_domain: builtins.str,
        data_factory_id: builtins.str,
        name: builtins.str,
        access_token: typing.Optional[builtins.str] = None,
        additional_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        annotations: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        existing_cluster_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        instance_pool: typing.Optional[typing.Union["DataFactoryLinkedServiceAzureDatabricksInstancePool", typing.Dict[str, typing.Any]]] = None,
        integration_runtime_name: typing.Optional[builtins.str] = None,
        key_vault_password: typing.Optional[typing.Union["DataFactoryLinkedServiceAzureDatabricksKeyVaultPassword", typing.Dict[str, typing.Any]]] = None,
        msi_work_space_resource_id: typing.Optional[builtins.str] = None,
        new_cluster_config: typing.Optional[typing.Union["DataFactoryLinkedServiceAzureDatabricksNewClusterConfig", typing.Dict[str, typing.Any]]] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["DataFactoryLinkedServiceAzureDatabricksTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks azurerm_data_factory_linked_service_azure_databricks} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param adb_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#adb_domain DataFactoryLinkedServiceAzureDatabricks#adb_domain}.
        :param data_factory_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#data_factory_id DataFactoryLinkedServiceAzureDatabricks#data_factory_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#name DataFactoryLinkedServiceAzureDatabricks#name}.
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#access_token DataFactoryLinkedServiceAzureDatabricks#access_token}.
        :param additional_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#additional_properties DataFactoryLinkedServiceAzureDatabricks#additional_properties}.
        :param annotations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#annotations DataFactoryLinkedServiceAzureDatabricks#annotations}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#description DataFactoryLinkedServiceAzureDatabricks#description}.
        :param existing_cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#existing_cluster_id DataFactoryLinkedServiceAzureDatabricks#existing_cluster_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#id DataFactoryLinkedServiceAzureDatabricks#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_pool: instance_pool block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#instance_pool DataFactoryLinkedServiceAzureDatabricks#instance_pool}
        :param integration_runtime_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#integration_runtime_name DataFactoryLinkedServiceAzureDatabricks#integration_runtime_name}.
        :param key_vault_password: key_vault_password block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#key_vault_password DataFactoryLinkedServiceAzureDatabricks#key_vault_password}
        :param msi_work_space_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#msi_work_space_resource_id DataFactoryLinkedServiceAzureDatabricks#msi_work_space_resource_id}.
        :param new_cluster_config: new_cluster_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#new_cluster_config DataFactoryLinkedServiceAzureDatabricks#new_cluster_config}
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#parameters DataFactoryLinkedServiceAzureDatabricks#parameters}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#timeouts DataFactoryLinkedServiceAzureDatabricks#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryLinkedServiceAzureDatabricks.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = DataFactoryLinkedServiceAzureDatabricksConfig(
            adb_domain=adb_domain,
            data_factory_id=data_factory_id,
            name=name,
            access_token=access_token,
            additional_properties=additional_properties,
            annotations=annotations,
            description=description,
            existing_cluster_id=existing_cluster_id,
            id=id,
            instance_pool=instance_pool,
            integration_runtime_name=integration_runtime_name,
            key_vault_password=key_vault_password,
            msi_work_space_resource_id=msi_work_space_resource_id,
            new_cluster_config=new_cluster_config,
            parameters=parameters,
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

    @jsii.member(jsii_name="putInstancePool")
    def put_instance_pool(
        self,
        *,
        cluster_version: builtins.str,
        instance_pool_id: builtins.str,
        max_number_of_workers: typing.Optional[jsii.Number] = None,
        min_number_of_workers: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cluster_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#cluster_version DataFactoryLinkedServiceAzureDatabricks#cluster_version}.
        :param instance_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#instance_pool_id DataFactoryLinkedServiceAzureDatabricks#instance_pool_id}.
        :param max_number_of_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#max_number_of_workers DataFactoryLinkedServiceAzureDatabricks#max_number_of_workers}.
        :param min_number_of_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#min_number_of_workers DataFactoryLinkedServiceAzureDatabricks#min_number_of_workers}.
        '''
        value = DataFactoryLinkedServiceAzureDatabricksInstancePool(
            cluster_version=cluster_version,
            instance_pool_id=instance_pool_id,
            max_number_of_workers=max_number_of_workers,
            min_number_of_workers=min_number_of_workers,
        )

        return typing.cast(None, jsii.invoke(self, "putInstancePool", [value]))

    @jsii.member(jsii_name="putKeyVaultPassword")
    def put_key_vault_password(
        self,
        *,
        linked_service_name: builtins.str,
        secret_name: builtins.str,
    ) -> None:
        '''
        :param linked_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#linked_service_name DataFactoryLinkedServiceAzureDatabricks#linked_service_name}.
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#secret_name DataFactoryLinkedServiceAzureDatabricks#secret_name}.
        '''
        value = DataFactoryLinkedServiceAzureDatabricksKeyVaultPassword(
            linked_service_name=linked_service_name, secret_name=secret_name
        )

        return typing.cast(None, jsii.invoke(self, "putKeyVaultPassword", [value]))

    @jsii.member(jsii_name="putNewClusterConfig")
    def put_new_cluster_config(
        self,
        *,
        cluster_version: builtins.str,
        node_type: builtins.str,
        custom_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        driver_node_type: typing.Optional[builtins.str] = None,
        init_scripts: typing.Optional[typing.Sequence[builtins.str]] = None,
        log_destination: typing.Optional[builtins.str] = None,
        max_number_of_workers: typing.Optional[jsii.Number] = None,
        min_number_of_workers: typing.Optional[jsii.Number] = None,
        spark_config: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        spark_environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param cluster_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#cluster_version DataFactoryLinkedServiceAzureDatabricks#cluster_version}.
        :param node_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#node_type DataFactoryLinkedServiceAzureDatabricks#node_type}.
        :param custom_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#custom_tags DataFactoryLinkedServiceAzureDatabricks#custom_tags}.
        :param driver_node_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#driver_node_type DataFactoryLinkedServiceAzureDatabricks#driver_node_type}.
        :param init_scripts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#init_scripts DataFactoryLinkedServiceAzureDatabricks#init_scripts}.
        :param log_destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#log_destination DataFactoryLinkedServiceAzureDatabricks#log_destination}.
        :param max_number_of_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#max_number_of_workers DataFactoryLinkedServiceAzureDatabricks#max_number_of_workers}.
        :param min_number_of_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#min_number_of_workers DataFactoryLinkedServiceAzureDatabricks#min_number_of_workers}.
        :param spark_config: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#spark_config DataFactoryLinkedServiceAzureDatabricks#spark_config}.
        :param spark_environment_variables: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#spark_environment_variables DataFactoryLinkedServiceAzureDatabricks#spark_environment_variables}.
        '''
        value = DataFactoryLinkedServiceAzureDatabricksNewClusterConfig(
            cluster_version=cluster_version,
            node_type=node_type,
            custom_tags=custom_tags,
            driver_node_type=driver_node_type,
            init_scripts=init_scripts,
            log_destination=log_destination,
            max_number_of_workers=max_number_of_workers,
            min_number_of_workers=min_number_of_workers,
            spark_config=spark_config,
            spark_environment_variables=spark_environment_variables,
        )

        return typing.cast(None, jsii.invoke(self, "putNewClusterConfig", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#create DataFactoryLinkedServiceAzureDatabricks#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#delete DataFactoryLinkedServiceAzureDatabricks#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#read DataFactoryLinkedServiceAzureDatabricks#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#update DataFactoryLinkedServiceAzureDatabricks#update}.
        '''
        value = DataFactoryLinkedServiceAzureDatabricksTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAccessToken")
    def reset_access_token(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccessToken", []))

    @jsii.member(jsii_name="resetAdditionalProperties")
    def reset_additional_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAdditionalProperties", []))

    @jsii.member(jsii_name="resetAnnotations")
    def reset_annotations(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAnnotations", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetExistingClusterId")
    def reset_existing_cluster_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExistingClusterId", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetInstancePool")
    def reset_instance_pool(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInstancePool", []))

    @jsii.member(jsii_name="resetIntegrationRuntimeName")
    def reset_integration_runtime_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIntegrationRuntimeName", []))

    @jsii.member(jsii_name="resetKeyVaultPassword")
    def reset_key_vault_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyVaultPassword", []))

    @jsii.member(jsii_name="resetMsiWorkSpaceResourceId")
    def reset_msi_work_space_resource_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMsiWorkSpaceResourceId", []))

    @jsii.member(jsii_name="resetNewClusterConfig")
    def reset_new_cluster_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNewClusterConfig", []))

    @jsii.member(jsii_name="resetParameters")
    def reset_parameters(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameters", []))

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
    @jsii.member(jsii_name="instancePool")
    def instance_pool(
        self,
    ) -> "DataFactoryLinkedServiceAzureDatabricksInstancePoolOutputReference":
        return typing.cast("DataFactoryLinkedServiceAzureDatabricksInstancePoolOutputReference", jsii.get(self, "instancePool"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultPassword")
    def key_vault_password(
        self,
    ) -> "DataFactoryLinkedServiceAzureDatabricksKeyVaultPasswordOutputReference":
        return typing.cast("DataFactoryLinkedServiceAzureDatabricksKeyVaultPasswordOutputReference", jsii.get(self, "keyVaultPassword"))

    @builtins.property
    @jsii.member(jsii_name="newClusterConfig")
    def new_cluster_config(
        self,
    ) -> "DataFactoryLinkedServiceAzureDatabricksNewClusterConfigOutputReference":
        return typing.cast("DataFactoryLinkedServiceAzureDatabricksNewClusterConfigOutputReference", jsii.get(self, "newClusterConfig"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(
        self,
    ) -> "DataFactoryLinkedServiceAzureDatabricksTimeoutsOutputReference":
        return typing.cast("DataFactoryLinkedServiceAzureDatabricksTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="accessTokenInput")
    def access_token_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessTokenInput"))

    @builtins.property
    @jsii.member(jsii_name="adbDomainInput")
    def adb_domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "adbDomainInput"))

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
    @jsii.member(jsii_name="existingClusterIdInput")
    def existing_cluster_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "existingClusterIdInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="instancePoolInput")
    def instance_pool_input(
        self,
    ) -> typing.Optional["DataFactoryLinkedServiceAzureDatabricksInstancePool"]:
        return typing.cast(typing.Optional["DataFactoryLinkedServiceAzureDatabricksInstancePool"], jsii.get(self, "instancePoolInput"))

    @builtins.property
    @jsii.member(jsii_name="integrationRuntimeNameInput")
    def integration_runtime_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "integrationRuntimeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="keyVaultPasswordInput")
    def key_vault_password_input(
        self,
    ) -> typing.Optional["DataFactoryLinkedServiceAzureDatabricksKeyVaultPassword"]:
        return typing.cast(typing.Optional["DataFactoryLinkedServiceAzureDatabricksKeyVaultPassword"], jsii.get(self, "keyVaultPasswordInput"))

    @builtins.property
    @jsii.member(jsii_name="msiWorkSpaceResourceIdInput")
    def msi_work_space_resource_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "msiWorkSpaceResourceIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="newClusterConfigInput")
    def new_cluster_config_input(
        self,
    ) -> typing.Optional["DataFactoryLinkedServiceAzureDatabricksNewClusterConfig"]:
        return typing.cast(typing.Optional["DataFactoryLinkedServiceAzureDatabricksNewClusterConfig"], jsii.get(self, "newClusterConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="parametersInput")
    def parameters_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "parametersInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["DataFactoryLinkedServiceAzureDatabricksTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["DataFactoryLinkedServiceAzureDatabricksTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="accessToken")
    def access_token(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accessToken"))

    @access_token.setter
    def access_token(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricks, "access_token").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessToken", value)

    @builtins.property
    @jsii.member(jsii_name="adbDomain")
    def adb_domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "adbDomain"))

    @adb_domain.setter
    def adb_domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricks, "adb_domain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "adbDomain", value)

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
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricks, "additional_properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalProperties", value)

    @builtins.property
    @jsii.member(jsii_name="annotations")
    def annotations(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "annotations"))

    @annotations.setter
    def annotations(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricks, "annotations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "annotations", value)

    @builtins.property
    @jsii.member(jsii_name="dataFactoryId")
    def data_factory_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataFactoryId"))

    @data_factory_id.setter
    def data_factory_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricks, "data_factory_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataFactoryId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricks, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="existingClusterId")
    def existing_cluster_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "existingClusterId"))

    @existing_cluster_id.setter
    def existing_cluster_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricks, "existing_cluster_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "existingClusterId", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricks, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="integrationRuntimeName")
    def integration_runtime_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "integrationRuntimeName"))

    @integration_runtime_name.setter
    def integration_runtime_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricks, "integration_runtime_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "integrationRuntimeName", value)

    @builtins.property
    @jsii.member(jsii_name="msiWorkSpaceResourceId")
    def msi_work_space_resource_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "msiWorkSpaceResourceId"))

    @msi_work_space_resource_id.setter
    def msi_work_space_resource_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricks, "msi_work_space_resource_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "msiWorkSpaceResourceId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricks, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricks, "parameters").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryLinkedServiceAzureDatabricks.DataFactoryLinkedServiceAzureDatabricksConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "adb_domain": "adbDomain",
        "data_factory_id": "dataFactoryId",
        "name": "name",
        "access_token": "accessToken",
        "additional_properties": "additionalProperties",
        "annotations": "annotations",
        "description": "description",
        "existing_cluster_id": "existingClusterId",
        "id": "id",
        "instance_pool": "instancePool",
        "integration_runtime_name": "integrationRuntimeName",
        "key_vault_password": "keyVaultPassword",
        "msi_work_space_resource_id": "msiWorkSpaceResourceId",
        "new_cluster_config": "newClusterConfig",
        "parameters": "parameters",
        "timeouts": "timeouts",
    },
)
class DataFactoryLinkedServiceAzureDatabricksConfig(cdktf.TerraformMetaArguments):
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
        adb_domain: builtins.str,
        data_factory_id: builtins.str,
        name: builtins.str,
        access_token: typing.Optional[builtins.str] = None,
        additional_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        annotations: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        existing_cluster_id: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        instance_pool: typing.Optional[typing.Union["DataFactoryLinkedServiceAzureDatabricksInstancePool", typing.Dict[str, typing.Any]]] = None,
        integration_runtime_name: typing.Optional[builtins.str] = None,
        key_vault_password: typing.Optional[typing.Union["DataFactoryLinkedServiceAzureDatabricksKeyVaultPassword", typing.Dict[str, typing.Any]]] = None,
        msi_work_space_resource_id: typing.Optional[builtins.str] = None,
        new_cluster_config: typing.Optional[typing.Union["DataFactoryLinkedServiceAzureDatabricksNewClusterConfig", typing.Dict[str, typing.Any]]] = None,
        parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["DataFactoryLinkedServiceAzureDatabricksTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param adb_domain: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#adb_domain DataFactoryLinkedServiceAzureDatabricks#adb_domain}.
        :param data_factory_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#data_factory_id DataFactoryLinkedServiceAzureDatabricks#data_factory_id}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#name DataFactoryLinkedServiceAzureDatabricks#name}.
        :param access_token: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#access_token DataFactoryLinkedServiceAzureDatabricks#access_token}.
        :param additional_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#additional_properties DataFactoryLinkedServiceAzureDatabricks#additional_properties}.
        :param annotations: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#annotations DataFactoryLinkedServiceAzureDatabricks#annotations}.
        :param description: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#description DataFactoryLinkedServiceAzureDatabricks#description}.
        :param existing_cluster_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#existing_cluster_id DataFactoryLinkedServiceAzureDatabricks#existing_cluster_id}.
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#id DataFactoryLinkedServiceAzureDatabricks#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param instance_pool: instance_pool block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#instance_pool DataFactoryLinkedServiceAzureDatabricks#instance_pool}
        :param integration_runtime_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#integration_runtime_name DataFactoryLinkedServiceAzureDatabricks#integration_runtime_name}.
        :param key_vault_password: key_vault_password block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#key_vault_password DataFactoryLinkedServiceAzureDatabricks#key_vault_password}
        :param msi_work_space_resource_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#msi_work_space_resource_id DataFactoryLinkedServiceAzureDatabricks#msi_work_space_resource_id}.
        :param new_cluster_config: new_cluster_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#new_cluster_config DataFactoryLinkedServiceAzureDatabricks#new_cluster_config}
        :param parameters: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#parameters DataFactoryLinkedServiceAzureDatabricks#parameters}.
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#timeouts DataFactoryLinkedServiceAzureDatabricks#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(instance_pool, dict):
            instance_pool = DataFactoryLinkedServiceAzureDatabricksInstancePool(**instance_pool)
        if isinstance(key_vault_password, dict):
            key_vault_password = DataFactoryLinkedServiceAzureDatabricksKeyVaultPassword(**key_vault_password)
        if isinstance(new_cluster_config, dict):
            new_cluster_config = DataFactoryLinkedServiceAzureDatabricksNewClusterConfig(**new_cluster_config)
        if isinstance(timeouts, dict):
            timeouts = DataFactoryLinkedServiceAzureDatabricksTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryLinkedServiceAzureDatabricksConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument adb_domain", value=adb_domain, expected_type=type_hints["adb_domain"])
            check_type(argname="argument data_factory_id", value=data_factory_id, expected_type=type_hints["data_factory_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
            check_type(argname="argument additional_properties", value=additional_properties, expected_type=type_hints["additional_properties"])
            check_type(argname="argument annotations", value=annotations, expected_type=type_hints["annotations"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument existing_cluster_id", value=existing_cluster_id, expected_type=type_hints["existing_cluster_id"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument instance_pool", value=instance_pool, expected_type=type_hints["instance_pool"])
            check_type(argname="argument integration_runtime_name", value=integration_runtime_name, expected_type=type_hints["integration_runtime_name"])
            check_type(argname="argument key_vault_password", value=key_vault_password, expected_type=type_hints["key_vault_password"])
            check_type(argname="argument msi_work_space_resource_id", value=msi_work_space_resource_id, expected_type=type_hints["msi_work_space_resource_id"])
            check_type(argname="argument new_cluster_config", value=new_cluster_config, expected_type=type_hints["new_cluster_config"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "adb_domain": adb_domain,
            "data_factory_id": data_factory_id,
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
        if access_token is not None:
            self._values["access_token"] = access_token
        if additional_properties is not None:
            self._values["additional_properties"] = additional_properties
        if annotations is not None:
            self._values["annotations"] = annotations
        if description is not None:
            self._values["description"] = description
        if existing_cluster_id is not None:
            self._values["existing_cluster_id"] = existing_cluster_id
        if id is not None:
            self._values["id"] = id
        if instance_pool is not None:
            self._values["instance_pool"] = instance_pool
        if integration_runtime_name is not None:
            self._values["integration_runtime_name"] = integration_runtime_name
        if key_vault_password is not None:
            self._values["key_vault_password"] = key_vault_password
        if msi_work_space_resource_id is not None:
            self._values["msi_work_space_resource_id"] = msi_work_space_resource_id
        if new_cluster_config is not None:
            self._values["new_cluster_config"] = new_cluster_config
        if parameters is not None:
            self._values["parameters"] = parameters
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
    def adb_domain(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#adb_domain DataFactoryLinkedServiceAzureDatabricks#adb_domain}.'''
        result = self._values.get("adb_domain")
        assert result is not None, "Required property 'adb_domain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_factory_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#data_factory_id DataFactoryLinkedServiceAzureDatabricks#data_factory_id}.'''
        result = self._values.get("data_factory_id")
        assert result is not None, "Required property 'data_factory_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#name DataFactoryLinkedServiceAzureDatabricks#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_token(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#access_token DataFactoryLinkedServiceAzureDatabricks#access_token}.'''
        result = self._values.get("access_token")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def additional_properties(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#additional_properties DataFactoryLinkedServiceAzureDatabricks#additional_properties}.'''
        result = self._values.get("additional_properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def annotations(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#annotations DataFactoryLinkedServiceAzureDatabricks#annotations}.'''
        result = self._values.get("annotations")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#description DataFactoryLinkedServiceAzureDatabricks#description}.'''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def existing_cluster_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#existing_cluster_id DataFactoryLinkedServiceAzureDatabricks#existing_cluster_id}.'''
        result = self._values.get("existing_cluster_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#id DataFactoryLinkedServiceAzureDatabricks#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_pool(
        self,
    ) -> typing.Optional["DataFactoryLinkedServiceAzureDatabricksInstancePool"]:
        '''instance_pool block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#instance_pool DataFactoryLinkedServiceAzureDatabricks#instance_pool}
        '''
        result = self._values.get("instance_pool")
        return typing.cast(typing.Optional["DataFactoryLinkedServiceAzureDatabricksInstancePool"], result)

    @builtins.property
    def integration_runtime_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#integration_runtime_name DataFactoryLinkedServiceAzureDatabricks#integration_runtime_name}.'''
        result = self._values.get("integration_runtime_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_vault_password(
        self,
    ) -> typing.Optional["DataFactoryLinkedServiceAzureDatabricksKeyVaultPassword"]:
        '''key_vault_password block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#key_vault_password DataFactoryLinkedServiceAzureDatabricks#key_vault_password}
        '''
        result = self._values.get("key_vault_password")
        return typing.cast(typing.Optional["DataFactoryLinkedServiceAzureDatabricksKeyVaultPassword"], result)

    @builtins.property
    def msi_work_space_resource_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#msi_work_space_resource_id DataFactoryLinkedServiceAzureDatabricks#msi_work_space_resource_id}.'''
        result = self._values.get("msi_work_space_resource_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def new_cluster_config(
        self,
    ) -> typing.Optional["DataFactoryLinkedServiceAzureDatabricksNewClusterConfig"]:
        '''new_cluster_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#new_cluster_config DataFactoryLinkedServiceAzureDatabricks#new_cluster_config}
        '''
        result = self._values.get("new_cluster_config")
        return typing.cast(typing.Optional["DataFactoryLinkedServiceAzureDatabricksNewClusterConfig"], result)

    @builtins.property
    def parameters(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#parameters DataFactoryLinkedServiceAzureDatabricks#parameters}.'''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(
        self,
    ) -> typing.Optional["DataFactoryLinkedServiceAzureDatabricksTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#timeouts DataFactoryLinkedServiceAzureDatabricks#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["DataFactoryLinkedServiceAzureDatabricksTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryLinkedServiceAzureDatabricksConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryLinkedServiceAzureDatabricks.DataFactoryLinkedServiceAzureDatabricksInstancePool",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_version": "clusterVersion",
        "instance_pool_id": "instancePoolId",
        "max_number_of_workers": "maxNumberOfWorkers",
        "min_number_of_workers": "minNumberOfWorkers",
    },
)
class DataFactoryLinkedServiceAzureDatabricksInstancePool:
    def __init__(
        self,
        *,
        cluster_version: builtins.str,
        instance_pool_id: builtins.str,
        max_number_of_workers: typing.Optional[jsii.Number] = None,
        min_number_of_workers: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param cluster_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#cluster_version DataFactoryLinkedServiceAzureDatabricks#cluster_version}.
        :param instance_pool_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#instance_pool_id DataFactoryLinkedServiceAzureDatabricks#instance_pool_id}.
        :param max_number_of_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#max_number_of_workers DataFactoryLinkedServiceAzureDatabricks#max_number_of_workers}.
        :param min_number_of_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#min_number_of_workers DataFactoryLinkedServiceAzureDatabricks#min_number_of_workers}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryLinkedServiceAzureDatabricksInstancePool.__init__)
            check_type(argname="argument cluster_version", value=cluster_version, expected_type=type_hints["cluster_version"])
            check_type(argname="argument instance_pool_id", value=instance_pool_id, expected_type=type_hints["instance_pool_id"])
            check_type(argname="argument max_number_of_workers", value=max_number_of_workers, expected_type=type_hints["max_number_of_workers"])
            check_type(argname="argument min_number_of_workers", value=min_number_of_workers, expected_type=type_hints["min_number_of_workers"])
        self._values: typing.Dict[str, typing.Any] = {
            "cluster_version": cluster_version,
            "instance_pool_id": instance_pool_id,
        }
        if max_number_of_workers is not None:
            self._values["max_number_of_workers"] = max_number_of_workers
        if min_number_of_workers is not None:
            self._values["min_number_of_workers"] = min_number_of_workers

    @builtins.property
    def cluster_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#cluster_version DataFactoryLinkedServiceAzureDatabricks#cluster_version}.'''
        result = self._values.get("cluster_version")
        assert result is not None, "Required property 'cluster_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_pool_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#instance_pool_id DataFactoryLinkedServiceAzureDatabricks#instance_pool_id}.'''
        result = self._values.get("instance_pool_id")
        assert result is not None, "Required property 'instance_pool_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def max_number_of_workers(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#max_number_of_workers DataFactoryLinkedServiceAzureDatabricks#max_number_of_workers}.'''
        result = self._values.get("max_number_of_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_number_of_workers(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#min_number_of_workers DataFactoryLinkedServiceAzureDatabricks#min_number_of_workers}.'''
        result = self._values.get("min_number_of_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryLinkedServiceAzureDatabricksInstancePool(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataFactoryLinkedServiceAzureDatabricksInstancePoolOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryLinkedServiceAzureDatabricks.DataFactoryLinkedServiceAzureDatabricksInstancePoolOutputReference",
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
            type_hints = typing.get_type_hints(DataFactoryLinkedServiceAzureDatabricksInstancePoolOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMaxNumberOfWorkers")
    def reset_max_number_of_workers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxNumberOfWorkers", []))

    @jsii.member(jsii_name="resetMinNumberOfWorkers")
    def reset_min_number_of_workers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinNumberOfWorkers", []))

    @builtins.property
    @jsii.member(jsii_name="clusterVersionInput")
    def cluster_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="instancePoolIdInput")
    def instance_pool_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instancePoolIdInput"))

    @builtins.property
    @jsii.member(jsii_name="maxNumberOfWorkersInput")
    def max_number_of_workers_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxNumberOfWorkersInput"))

    @builtins.property
    @jsii.member(jsii_name="minNumberOfWorkersInput")
    def min_number_of_workers_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minNumberOfWorkersInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterVersion")
    def cluster_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterVersion"))

    @cluster_version.setter
    def cluster_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricksInstancePoolOutputReference, "cluster_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterVersion", value)

    @builtins.property
    @jsii.member(jsii_name="instancePoolId")
    def instance_pool_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "instancePoolId"))

    @instance_pool_id.setter
    def instance_pool_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricksInstancePoolOutputReference, "instance_pool_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instancePoolId", value)

    @builtins.property
    @jsii.member(jsii_name="maxNumberOfWorkers")
    def max_number_of_workers(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxNumberOfWorkers"))

    @max_number_of_workers.setter
    def max_number_of_workers(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricksInstancePoolOutputReference, "max_number_of_workers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxNumberOfWorkers", value)

    @builtins.property
    @jsii.member(jsii_name="minNumberOfWorkers")
    def min_number_of_workers(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minNumberOfWorkers"))

    @min_number_of_workers.setter
    def min_number_of_workers(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricksInstancePoolOutputReference, "min_number_of_workers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minNumberOfWorkers", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataFactoryLinkedServiceAzureDatabricksInstancePool]:
        return typing.cast(typing.Optional[DataFactoryLinkedServiceAzureDatabricksInstancePool], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataFactoryLinkedServiceAzureDatabricksInstancePool],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricksInstancePoolOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryLinkedServiceAzureDatabricks.DataFactoryLinkedServiceAzureDatabricksKeyVaultPassword",
    jsii_struct_bases=[],
    name_mapping={
        "linked_service_name": "linkedServiceName",
        "secret_name": "secretName",
    },
)
class DataFactoryLinkedServiceAzureDatabricksKeyVaultPassword:
    def __init__(
        self,
        *,
        linked_service_name: builtins.str,
        secret_name: builtins.str,
    ) -> None:
        '''
        :param linked_service_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#linked_service_name DataFactoryLinkedServiceAzureDatabricks#linked_service_name}.
        :param secret_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#secret_name DataFactoryLinkedServiceAzureDatabricks#secret_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryLinkedServiceAzureDatabricksKeyVaultPassword.__init__)
            check_type(argname="argument linked_service_name", value=linked_service_name, expected_type=type_hints["linked_service_name"])
            check_type(argname="argument secret_name", value=secret_name, expected_type=type_hints["secret_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "linked_service_name": linked_service_name,
            "secret_name": secret_name,
        }

    @builtins.property
    def linked_service_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#linked_service_name DataFactoryLinkedServiceAzureDatabricks#linked_service_name}.'''
        result = self._values.get("linked_service_name")
        assert result is not None, "Required property 'linked_service_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def secret_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#secret_name DataFactoryLinkedServiceAzureDatabricks#secret_name}.'''
        result = self._values.get("secret_name")
        assert result is not None, "Required property 'secret_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryLinkedServiceAzureDatabricksKeyVaultPassword(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataFactoryLinkedServiceAzureDatabricksKeyVaultPasswordOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryLinkedServiceAzureDatabricks.DataFactoryLinkedServiceAzureDatabricksKeyVaultPasswordOutputReference",
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
            type_hints = typing.get_type_hints(DataFactoryLinkedServiceAzureDatabricksKeyVaultPasswordOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="linkedServiceNameInput")
    def linked_service_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "linkedServiceNameInput"))

    @builtins.property
    @jsii.member(jsii_name="secretNameInput")
    def secret_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secretNameInput"))

    @builtins.property
    @jsii.member(jsii_name="linkedServiceName")
    def linked_service_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "linkedServiceName"))

    @linked_service_name.setter
    def linked_service_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricksKeyVaultPasswordOutputReference, "linked_service_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "linkedServiceName", value)

    @builtins.property
    @jsii.member(jsii_name="secretName")
    def secret_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secretName"))

    @secret_name.setter
    def secret_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricksKeyVaultPasswordOutputReference, "secret_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secretName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataFactoryLinkedServiceAzureDatabricksKeyVaultPassword]:
        return typing.cast(typing.Optional[DataFactoryLinkedServiceAzureDatabricksKeyVaultPassword], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataFactoryLinkedServiceAzureDatabricksKeyVaultPassword],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricksKeyVaultPasswordOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryLinkedServiceAzureDatabricks.DataFactoryLinkedServiceAzureDatabricksNewClusterConfig",
    jsii_struct_bases=[],
    name_mapping={
        "cluster_version": "clusterVersion",
        "node_type": "nodeType",
        "custom_tags": "customTags",
        "driver_node_type": "driverNodeType",
        "init_scripts": "initScripts",
        "log_destination": "logDestination",
        "max_number_of_workers": "maxNumberOfWorkers",
        "min_number_of_workers": "minNumberOfWorkers",
        "spark_config": "sparkConfig",
        "spark_environment_variables": "sparkEnvironmentVariables",
    },
)
class DataFactoryLinkedServiceAzureDatabricksNewClusterConfig:
    def __init__(
        self,
        *,
        cluster_version: builtins.str,
        node_type: builtins.str,
        custom_tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        driver_node_type: typing.Optional[builtins.str] = None,
        init_scripts: typing.Optional[typing.Sequence[builtins.str]] = None,
        log_destination: typing.Optional[builtins.str] = None,
        max_number_of_workers: typing.Optional[jsii.Number] = None,
        min_number_of_workers: typing.Optional[jsii.Number] = None,
        spark_config: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        spark_environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param cluster_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#cluster_version DataFactoryLinkedServiceAzureDatabricks#cluster_version}.
        :param node_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#node_type DataFactoryLinkedServiceAzureDatabricks#node_type}.
        :param custom_tags: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#custom_tags DataFactoryLinkedServiceAzureDatabricks#custom_tags}.
        :param driver_node_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#driver_node_type DataFactoryLinkedServiceAzureDatabricks#driver_node_type}.
        :param init_scripts: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#init_scripts DataFactoryLinkedServiceAzureDatabricks#init_scripts}.
        :param log_destination: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#log_destination DataFactoryLinkedServiceAzureDatabricks#log_destination}.
        :param max_number_of_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#max_number_of_workers DataFactoryLinkedServiceAzureDatabricks#max_number_of_workers}.
        :param min_number_of_workers: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#min_number_of_workers DataFactoryLinkedServiceAzureDatabricks#min_number_of_workers}.
        :param spark_config: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#spark_config DataFactoryLinkedServiceAzureDatabricks#spark_config}.
        :param spark_environment_variables: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#spark_environment_variables DataFactoryLinkedServiceAzureDatabricks#spark_environment_variables}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryLinkedServiceAzureDatabricksNewClusterConfig.__init__)
            check_type(argname="argument cluster_version", value=cluster_version, expected_type=type_hints["cluster_version"])
            check_type(argname="argument node_type", value=node_type, expected_type=type_hints["node_type"])
            check_type(argname="argument custom_tags", value=custom_tags, expected_type=type_hints["custom_tags"])
            check_type(argname="argument driver_node_type", value=driver_node_type, expected_type=type_hints["driver_node_type"])
            check_type(argname="argument init_scripts", value=init_scripts, expected_type=type_hints["init_scripts"])
            check_type(argname="argument log_destination", value=log_destination, expected_type=type_hints["log_destination"])
            check_type(argname="argument max_number_of_workers", value=max_number_of_workers, expected_type=type_hints["max_number_of_workers"])
            check_type(argname="argument min_number_of_workers", value=min_number_of_workers, expected_type=type_hints["min_number_of_workers"])
            check_type(argname="argument spark_config", value=spark_config, expected_type=type_hints["spark_config"])
            check_type(argname="argument spark_environment_variables", value=spark_environment_variables, expected_type=type_hints["spark_environment_variables"])
        self._values: typing.Dict[str, typing.Any] = {
            "cluster_version": cluster_version,
            "node_type": node_type,
        }
        if custom_tags is not None:
            self._values["custom_tags"] = custom_tags
        if driver_node_type is not None:
            self._values["driver_node_type"] = driver_node_type
        if init_scripts is not None:
            self._values["init_scripts"] = init_scripts
        if log_destination is not None:
            self._values["log_destination"] = log_destination
        if max_number_of_workers is not None:
            self._values["max_number_of_workers"] = max_number_of_workers
        if min_number_of_workers is not None:
            self._values["min_number_of_workers"] = min_number_of_workers
        if spark_config is not None:
            self._values["spark_config"] = spark_config
        if spark_environment_variables is not None:
            self._values["spark_environment_variables"] = spark_environment_variables

    @builtins.property
    def cluster_version(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#cluster_version DataFactoryLinkedServiceAzureDatabricks#cluster_version}.'''
        result = self._values.get("cluster_version")
        assert result is not None, "Required property 'cluster_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def node_type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#node_type DataFactoryLinkedServiceAzureDatabricks#node_type}.'''
        result = self._values.get("node_type")
        assert result is not None, "Required property 'node_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_tags(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#custom_tags DataFactoryLinkedServiceAzureDatabricks#custom_tags}.'''
        result = self._values.get("custom_tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def driver_node_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#driver_node_type DataFactoryLinkedServiceAzureDatabricks#driver_node_type}.'''
        result = self._values.get("driver_node_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def init_scripts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#init_scripts DataFactoryLinkedServiceAzureDatabricks#init_scripts}.'''
        result = self._values.get("init_scripts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def log_destination(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#log_destination DataFactoryLinkedServiceAzureDatabricks#log_destination}.'''
        result = self._values.get("log_destination")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_number_of_workers(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#max_number_of_workers DataFactoryLinkedServiceAzureDatabricks#max_number_of_workers}.'''
        result = self._values.get("max_number_of_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_number_of_workers(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#min_number_of_workers DataFactoryLinkedServiceAzureDatabricks#min_number_of_workers}.'''
        result = self._values.get("min_number_of_workers")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def spark_config(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#spark_config DataFactoryLinkedServiceAzureDatabricks#spark_config}.'''
        result = self._values.get("spark_config")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def spark_environment_variables(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#spark_environment_variables DataFactoryLinkedServiceAzureDatabricks#spark_environment_variables}.'''
        result = self._values.get("spark_environment_variables")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryLinkedServiceAzureDatabricksNewClusterConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataFactoryLinkedServiceAzureDatabricksNewClusterConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryLinkedServiceAzureDatabricks.DataFactoryLinkedServiceAzureDatabricksNewClusterConfigOutputReference",
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
            type_hints = typing.get_type_hints(DataFactoryLinkedServiceAzureDatabricksNewClusterConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCustomTags")
    def reset_custom_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomTags", []))

    @jsii.member(jsii_name="resetDriverNodeType")
    def reset_driver_node_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDriverNodeType", []))

    @jsii.member(jsii_name="resetInitScripts")
    def reset_init_scripts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInitScripts", []))

    @jsii.member(jsii_name="resetLogDestination")
    def reset_log_destination(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogDestination", []))

    @jsii.member(jsii_name="resetMaxNumberOfWorkers")
    def reset_max_number_of_workers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxNumberOfWorkers", []))

    @jsii.member(jsii_name="resetMinNumberOfWorkers")
    def reset_min_number_of_workers(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMinNumberOfWorkers", []))

    @jsii.member(jsii_name="resetSparkConfig")
    def reset_spark_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSparkConfig", []))

    @jsii.member(jsii_name="resetSparkEnvironmentVariables")
    def reset_spark_environment_variables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSparkEnvironmentVariables", []))

    @builtins.property
    @jsii.member(jsii_name="clusterVersionInput")
    def cluster_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="customTagsInput")
    def custom_tags_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "customTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="driverNodeTypeInput")
    def driver_node_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "driverNodeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="initScriptsInput")
    def init_scripts_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "initScriptsInput"))

    @builtins.property
    @jsii.member(jsii_name="logDestinationInput")
    def log_destination_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logDestinationInput"))

    @builtins.property
    @jsii.member(jsii_name="maxNumberOfWorkersInput")
    def max_number_of_workers_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxNumberOfWorkersInput"))

    @builtins.property
    @jsii.member(jsii_name="minNumberOfWorkersInput")
    def min_number_of_workers_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minNumberOfWorkersInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeTypeInput")
    def node_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nodeTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="sparkConfigInput")
    def spark_config_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "sparkConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="sparkEnvironmentVariablesInput")
    def spark_environment_variables_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "sparkEnvironmentVariablesInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterVersion")
    def cluster_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterVersion"))

    @cluster_version.setter
    def cluster_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricksNewClusterConfigOutputReference, "cluster_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterVersion", value)

    @builtins.property
    @jsii.member(jsii_name="customTags")
    def custom_tags(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "customTags"))

    @custom_tags.setter
    def custom_tags(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricksNewClusterConfigOutputReference, "custom_tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customTags", value)

    @builtins.property
    @jsii.member(jsii_name="driverNodeType")
    def driver_node_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "driverNodeType"))

    @driver_node_type.setter
    def driver_node_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricksNewClusterConfigOutputReference, "driver_node_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driverNodeType", value)

    @builtins.property
    @jsii.member(jsii_name="initScripts")
    def init_scripts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "initScripts"))

    @init_scripts.setter
    def init_scripts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricksNewClusterConfigOutputReference, "init_scripts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "initScripts", value)

    @builtins.property
    @jsii.member(jsii_name="logDestination")
    def log_destination(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logDestination"))

    @log_destination.setter
    def log_destination(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricksNewClusterConfigOutputReference, "log_destination").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logDestination", value)

    @builtins.property
    @jsii.member(jsii_name="maxNumberOfWorkers")
    def max_number_of_workers(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxNumberOfWorkers"))

    @max_number_of_workers.setter
    def max_number_of_workers(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricksNewClusterConfigOutputReference, "max_number_of_workers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxNumberOfWorkers", value)

    @builtins.property
    @jsii.member(jsii_name="minNumberOfWorkers")
    def min_number_of_workers(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "minNumberOfWorkers"))

    @min_number_of_workers.setter
    def min_number_of_workers(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricksNewClusterConfigOutputReference, "min_number_of_workers").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minNumberOfWorkers", value)

    @builtins.property
    @jsii.member(jsii_name="nodeType")
    def node_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nodeType"))

    @node_type.setter
    def node_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricksNewClusterConfigOutputReference, "node_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeType", value)

    @builtins.property
    @jsii.member(jsii_name="sparkConfig")
    def spark_config(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "sparkConfig"))

    @spark_config.setter
    def spark_config(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricksNewClusterConfigOutputReference, "spark_config").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sparkConfig", value)

    @builtins.property
    @jsii.member(jsii_name="sparkEnvironmentVariables")
    def spark_environment_variables(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "sparkEnvironmentVariables"))

    @spark_environment_variables.setter
    def spark_environment_variables(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricksNewClusterConfigOutputReference, "spark_environment_variables").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sparkEnvironmentVariables", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[DataFactoryLinkedServiceAzureDatabricksNewClusterConfig]:
        return typing.cast(typing.Optional[DataFactoryLinkedServiceAzureDatabricksNewClusterConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[DataFactoryLinkedServiceAzureDatabricksNewClusterConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricksNewClusterConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.dataFactoryLinkedServiceAzureDatabricks.DataFactoryLinkedServiceAzureDatabricksTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class DataFactoryLinkedServiceAzureDatabricksTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#create DataFactoryLinkedServiceAzureDatabricks#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#delete DataFactoryLinkedServiceAzureDatabricks#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#read DataFactoryLinkedServiceAzureDatabricks#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#update DataFactoryLinkedServiceAzureDatabricks#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(DataFactoryLinkedServiceAzureDatabricksTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#create DataFactoryLinkedServiceAzureDatabricks#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#delete DataFactoryLinkedServiceAzureDatabricks#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#read DataFactoryLinkedServiceAzureDatabricks#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/data_factory_linked_service_azure_databricks#update DataFactoryLinkedServiceAzureDatabricks#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DataFactoryLinkedServiceAzureDatabricksTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DataFactoryLinkedServiceAzureDatabricksTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.dataFactoryLinkedServiceAzureDatabricks.DataFactoryLinkedServiceAzureDatabricksTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(DataFactoryLinkedServiceAzureDatabricksTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricksTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricksTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricksTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricksTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[DataFactoryLinkedServiceAzureDatabricksTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[DataFactoryLinkedServiceAzureDatabricksTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[DataFactoryLinkedServiceAzureDatabricksTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(DataFactoryLinkedServiceAzureDatabricksTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "DataFactoryLinkedServiceAzureDatabricks",
    "DataFactoryLinkedServiceAzureDatabricksConfig",
    "DataFactoryLinkedServiceAzureDatabricksInstancePool",
    "DataFactoryLinkedServiceAzureDatabricksInstancePoolOutputReference",
    "DataFactoryLinkedServiceAzureDatabricksKeyVaultPassword",
    "DataFactoryLinkedServiceAzureDatabricksKeyVaultPasswordOutputReference",
    "DataFactoryLinkedServiceAzureDatabricksNewClusterConfig",
    "DataFactoryLinkedServiceAzureDatabricksNewClusterConfigOutputReference",
    "DataFactoryLinkedServiceAzureDatabricksTimeouts",
    "DataFactoryLinkedServiceAzureDatabricksTimeoutsOutputReference",
]

publication.publish()
