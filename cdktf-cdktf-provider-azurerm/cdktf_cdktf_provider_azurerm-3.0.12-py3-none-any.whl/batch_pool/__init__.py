'''
# `azurerm_batch_pool`

Refer to the Terraform Registory for docs: [`azurerm_batch_pool`](https://www.terraform.io/docs/providers/azurerm/r/batch_pool).
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


class BatchPool(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPool",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool azurerm_batch_pool}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        account_name: builtins.str,
        name: builtins.str,
        node_agent_sku_id: builtins.str,
        resource_group_name: builtins.str,
        storage_image_reference: typing.Union["BatchPoolStorageImageReference", typing.Dict[str, typing.Any]],
        vm_size: builtins.str,
        auto_scale: typing.Optional[typing.Union["BatchPoolAutoScale", typing.Dict[str, typing.Any]]] = None,
        certificate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolCertificate", typing.Dict[str, typing.Any]]]]] = None,
        container_configuration: typing.Optional[typing.Union["BatchPoolContainerConfiguration", typing.Dict[str, typing.Any]]] = None,
        data_disks: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolDataDisks", typing.Dict[str, typing.Any]]]]] = None,
        disk_encryption: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolDiskEncryption", typing.Dict[str, typing.Any]]]]] = None,
        display_name: typing.Optional[builtins.str] = None,
        extensions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolExtensions", typing.Dict[str, typing.Any]]]]] = None,
        fixed_scale: typing.Optional[typing.Union["BatchPoolFixedScale", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["BatchPoolIdentity", typing.Dict[str, typing.Any]]] = None,
        inter_node_communication: typing.Optional[builtins.str] = None,
        license_type: typing.Optional[builtins.str] = None,
        max_tasks_per_node: typing.Optional[jsii.Number] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        mount: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolMount", typing.Dict[str, typing.Any]]]]] = None,
        network_configuration: typing.Optional[typing.Union["BatchPoolNetworkConfiguration", typing.Dict[str, typing.Any]]] = None,
        node_placement: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolNodePlacement", typing.Dict[str, typing.Any]]]]] = None,
        os_disk_placement: typing.Optional[builtins.str] = None,
        start_task: typing.Optional[typing.Union["BatchPoolStartTask", typing.Dict[str, typing.Any]]] = None,
        stop_pending_resize_operation: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        task_scheduling_policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolTaskSchedulingPolicy", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["BatchPoolTimeouts", typing.Dict[str, typing.Any]]] = None,
        user_accounts: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolUserAccounts", typing.Dict[str, typing.Any]]]]] = None,
        windows: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolWindows", typing.Dict[str, typing.Any]]]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool azurerm_batch_pool} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#account_name BatchPool#account_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#name BatchPool#name}.
        :param node_agent_sku_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#node_agent_sku_id BatchPool#node_agent_sku_id}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#resource_group_name BatchPool#resource_group_name}.
        :param storage_image_reference: storage_image_reference block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#storage_image_reference BatchPool#storage_image_reference}
        :param vm_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#vm_size BatchPool#vm_size}.
        :param auto_scale: auto_scale block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#auto_scale BatchPool#auto_scale}
        :param certificate: certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#certificate BatchPool#certificate}
        :param container_configuration: container_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#container_configuration BatchPool#container_configuration}
        :param data_disks: data_disks block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#data_disks BatchPool#data_disks}
        :param disk_encryption: disk_encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#disk_encryption BatchPool#disk_encryption}
        :param display_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#display_name BatchPool#display_name}.
        :param extensions: extensions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#extensions BatchPool#extensions}
        :param fixed_scale: fixed_scale block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#fixed_scale BatchPool#fixed_scale}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#id BatchPool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#identity BatchPool#identity}
        :param inter_node_communication: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#inter_node_communication BatchPool#inter_node_communication}.
        :param license_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#license_type BatchPool#license_type}.
        :param max_tasks_per_node: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#max_tasks_per_node BatchPool#max_tasks_per_node}.
        :param metadata: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#metadata BatchPool#metadata}.
        :param mount: mount block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#mount BatchPool#mount}
        :param network_configuration: network_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#network_configuration BatchPool#network_configuration}
        :param node_placement: node_placement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#node_placement BatchPool#node_placement}
        :param os_disk_placement: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#os_disk_placement BatchPool#os_disk_placement}.
        :param start_task: start_task block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#start_task BatchPool#start_task}
        :param stop_pending_resize_operation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#stop_pending_resize_operation BatchPool#stop_pending_resize_operation}.
        :param task_scheduling_policy: task_scheduling_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#task_scheduling_policy BatchPool#task_scheduling_policy}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#timeouts BatchPool#timeouts}
        :param user_accounts: user_accounts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#user_accounts BatchPool#user_accounts}
        :param windows: windows block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#windows BatchPool#windows}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPool.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = BatchPoolConfig(
            account_name=account_name,
            name=name,
            node_agent_sku_id=node_agent_sku_id,
            resource_group_name=resource_group_name,
            storage_image_reference=storage_image_reference,
            vm_size=vm_size,
            auto_scale=auto_scale,
            certificate=certificate,
            container_configuration=container_configuration,
            data_disks=data_disks,
            disk_encryption=disk_encryption,
            display_name=display_name,
            extensions=extensions,
            fixed_scale=fixed_scale,
            id=id,
            identity=identity,
            inter_node_communication=inter_node_communication,
            license_type=license_type,
            max_tasks_per_node=max_tasks_per_node,
            metadata=metadata,
            mount=mount,
            network_configuration=network_configuration,
            node_placement=node_placement,
            os_disk_placement=os_disk_placement,
            start_task=start_task,
            stop_pending_resize_operation=stop_pending_resize_operation,
            task_scheduling_policy=task_scheduling_policy,
            timeouts=timeouts,
            user_accounts=user_accounts,
            windows=windows,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putAutoScale")
    def put_auto_scale(
        self,
        *,
        formula: builtins.str,
        evaluation_interval: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param formula: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#formula BatchPool#formula}.
        :param evaluation_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#evaluation_interval BatchPool#evaluation_interval}.
        '''
        value = BatchPoolAutoScale(
            formula=formula, evaluation_interval=evaluation_interval
        )

        return typing.cast(None, jsii.invoke(self, "putAutoScale", [value]))

    @jsii.member(jsii_name="putCertificate")
    def put_certificate(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolCertificate", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPool.put_certificate)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCertificate", [value]))

    @jsii.member(jsii_name="putContainerConfiguration")
    def put_container_configuration(
        self,
        *,
        container_image_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        container_registries: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolContainerConfigurationContainerRegistries", typing.Dict[str, typing.Any]]]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param container_image_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#container_image_names BatchPool#container_image_names}.
        :param container_registries: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#container_registries BatchPool#container_registries}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#type BatchPool#type}.
        '''
        value = BatchPoolContainerConfiguration(
            container_image_names=container_image_names,
            container_registries=container_registries,
            type=type,
        )

        return typing.cast(None, jsii.invoke(self, "putContainerConfiguration", [value]))

    @jsii.member(jsii_name="putDataDisks")
    def put_data_disks(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolDataDisks", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPool.put_data_disks)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDataDisks", [value]))

    @jsii.member(jsii_name="putDiskEncryption")
    def put_disk_encryption(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolDiskEncryption", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPool.put_disk_encryption)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDiskEncryption", [value]))

    @jsii.member(jsii_name="putExtensions")
    def put_extensions(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolExtensions", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPool.put_extensions)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putExtensions", [value]))

    @jsii.member(jsii_name="putFixedScale")
    def put_fixed_scale(
        self,
        *,
        node_deallocation_method: typing.Optional[builtins.str] = None,
        resize_timeout: typing.Optional[builtins.str] = None,
        target_dedicated_nodes: typing.Optional[jsii.Number] = None,
        target_low_priority_nodes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param node_deallocation_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#node_deallocation_method BatchPool#node_deallocation_method}.
        :param resize_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#resize_timeout BatchPool#resize_timeout}.
        :param target_dedicated_nodes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#target_dedicated_nodes BatchPool#target_dedicated_nodes}.
        :param target_low_priority_nodes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#target_low_priority_nodes BatchPool#target_low_priority_nodes}.
        '''
        value = BatchPoolFixedScale(
            node_deallocation_method=node_deallocation_method,
            resize_timeout=resize_timeout,
            target_dedicated_nodes=target_dedicated_nodes,
            target_low_priority_nodes=target_low_priority_nodes,
        )

        return typing.cast(None, jsii.invoke(self, "putFixedScale", [value]))

    @jsii.member(jsii_name="putIdentity")
    def put_identity(
        self,
        *,
        identity_ids: typing.Sequence[builtins.str],
        type: builtins.str,
    ) -> None:
        '''
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#identity_ids BatchPool#identity_ids}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#type BatchPool#type}.
        '''
        value = BatchPoolIdentity(identity_ids=identity_ids, type=type)

        return typing.cast(None, jsii.invoke(self, "putIdentity", [value]))

    @jsii.member(jsii_name="putMount")
    def put_mount(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolMount", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPool.put_mount)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putMount", [value]))

    @jsii.member(jsii_name="putNetworkConfiguration")
    def put_network_configuration(
        self,
        *,
        subnet_id: builtins.str,
        dynamic_vnet_assignment_scope: typing.Optional[builtins.str] = None,
        endpoint_configuration: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolNetworkConfigurationEndpointConfiguration", typing.Dict[str, typing.Any]]]]] = None,
        public_address_provisioning_type: typing.Optional[builtins.str] = None,
        public_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#subnet_id BatchPool#subnet_id}.
        :param dynamic_vnet_assignment_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#dynamic_vnet_assignment_scope BatchPool#dynamic_vnet_assignment_scope}.
        :param endpoint_configuration: endpoint_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#endpoint_configuration BatchPool#endpoint_configuration}
        :param public_address_provisioning_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#public_address_provisioning_type BatchPool#public_address_provisioning_type}.
        :param public_ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#public_ips BatchPool#public_ips}.
        '''
        value = BatchPoolNetworkConfiguration(
            subnet_id=subnet_id,
            dynamic_vnet_assignment_scope=dynamic_vnet_assignment_scope,
            endpoint_configuration=endpoint_configuration,
            public_address_provisioning_type=public_address_provisioning_type,
            public_ips=public_ips,
        )

        return typing.cast(None, jsii.invoke(self, "putNetworkConfiguration", [value]))

    @jsii.member(jsii_name="putNodePlacement")
    def put_node_placement(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolNodePlacement", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPool.put_node_placement)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNodePlacement", [value]))

    @jsii.member(jsii_name="putStartTask")
    def put_start_task(
        self,
        *,
        command_line: builtins.str,
        user_identity: typing.Union["BatchPoolStartTaskUserIdentity", typing.Dict[str, typing.Any]],
        common_environment_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        container: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolStartTaskContainer", typing.Dict[str, typing.Any]]]]] = None,
        resource_file: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolStartTaskResourceFile", typing.Dict[str, typing.Any]]]]] = None,
        task_retry_maximum: typing.Optional[jsii.Number] = None,
        wait_for_success: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param command_line: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#command_line BatchPool#command_line}.
        :param user_identity: user_identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#user_identity BatchPool#user_identity}
        :param common_environment_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#common_environment_properties BatchPool#common_environment_properties}.
        :param container: container block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#container BatchPool#container}
        :param resource_file: resource_file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#resource_file BatchPool#resource_file}
        :param task_retry_maximum: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#task_retry_maximum BatchPool#task_retry_maximum}.
        :param wait_for_success: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#wait_for_success BatchPool#wait_for_success}.
        '''
        value = BatchPoolStartTask(
            command_line=command_line,
            user_identity=user_identity,
            common_environment_properties=common_environment_properties,
            container=container,
            resource_file=resource_file,
            task_retry_maximum=task_retry_maximum,
            wait_for_success=wait_for_success,
        )

        return typing.cast(None, jsii.invoke(self, "putStartTask", [value]))

    @jsii.member(jsii_name="putStorageImageReference")
    def put_storage_image_reference(
        self,
        *,
        id: typing.Optional[builtins.str] = None,
        offer: typing.Optional[builtins.str] = None,
        publisher: typing.Optional[builtins.str] = None,
        sku: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#id BatchPool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param offer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#offer BatchPool#offer}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#publisher BatchPool#publisher}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#sku BatchPool#sku}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#version BatchPool#version}.
        '''
        value = BatchPoolStorageImageReference(
            id=id, offer=offer, publisher=publisher, sku=sku, version=version
        )

        return typing.cast(None, jsii.invoke(self, "putStorageImageReference", [value]))

    @jsii.member(jsii_name="putTaskSchedulingPolicy")
    def put_task_scheduling_policy(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolTaskSchedulingPolicy", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPool.put_task_scheduling_policy)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTaskSchedulingPolicy", [value]))

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
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#create BatchPool#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#delete BatchPool#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#read BatchPool#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#update BatchPool#update}.
        '''
        value = BatchPoolTimeouts(
            create=create, delete=delete, read=read, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putUserAccounts")
    def put_user_accounts(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolUserAccounts", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPool.put_user_accounts)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUserAccounts", [value]))

    @jsii.member(jsii_name="putWindows")
    def put_windows(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolWindows", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPool.put_windows)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWindows", [value]))

    @jsii.member(jsii_name="resetAutoScale")
    def reset_auto_scale(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoScale", []))

    @jsii.member(jsii_name="resetCertificate")
    def reset_certificate(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCertificate", []))

    @jsii.member(jsii_name="resetContainerConfiguration")
    def reset_container_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerConfiguration", []))

    @jsii.member(jsii_name="resetDataDisks")
    def reset_data_disks(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDataDisks", []))

    @jsii.member(jsii_name="resetDiskEncryption")
    def reset_disk_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDiskEncryption", []))

    @jsii.member(jsii_name="resetDisplayName")
    def reset_display_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisplayName", []))

    @jsii.member(jsii_name="resetExtensions")
    def reset_extensions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtensions", []))

    @jsii.member(jsii_name="resetFixedScale")
    def reset_fixed_scale(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFixedScale", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetIdentity")
    def reset_identity(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentity", []))

    @jsii.member(jsii_name="resetInterNodeCommunication")
    def reset_inter_node_communication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInterNodeCommunication", []))

    @jsii.member(jsii_name="resetLicenseType")
    def reset_license_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLicenseType", []))

    @jsii.member(jsii_name="resetMaxTasksPerNode")
    def reset_max_tasks_per_node(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxTasksPerNode", []))

    @jsii.member(jsii_name="resetMetadata")
    def reset_metadata(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMetadata", []))

    @jsii.member(jsii_name="resetMount")
    def reset_mount(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMount", []))

    @jsii.member(jsii_name="resetNetworkConfiguration")
    def reset_network_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkConfiguration", []))

    @jsii.member(jsii_name="resetNodePlacement")
    def reset_node_placement(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodePlacement", []))

    @jsii.member(jsii_name="resetOsDiskPlacement")
    def reset_os_disk_placement(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOsDiskPlacement", []))

    @jsii.member(jsii_name="resetStartTask")
    def reset_start_task(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStartTask", []))

    @jsii.member(jsii_name="resetStopPendingResizeOperation")
    def reset_stop_pending_resize_operation(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStopPendingResizeOperation", []))

    @jsii.member(jsii_name="resetTaskSchedulingPolicy")
    def reset_task_scheduling_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTaskSchedulingPolicy", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetUserAccounts")
    def reset_user_accounts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserAccounts", []))

    @jsii.member(jsii_name="resetWindows")
    def reset_windows(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWindows", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="autoScale")
    def auto_scale(self) -> "BatchPoolAutoScaleOutputReference":
        return typing.cast("BatchPoolAutoScaleOutputReference", jsii.get(self, "autoScale"))

    @builtins.property
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> "BatchPoolCertificateList":
        return typing.cast("BatchPoolCertificateList", jsii.get(self, "certificate"))

    @builtins.property
    @jsii.member(jsii_name="containerConfiguration")
    def container_configuration(
        self,
    ) -> "BatchPoolContainerConfigurationOutputReference":
        return typing.cast("BatchPoolContainerConfigurationOutputReference", jsii.get(self, "containerConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="dataDisks")
    def data_disks(self) -> "BatchPoolDataDisksList":
        return typing.cast("BatchPoolDataDisksList", jsii.get(self, "dataDisks"))

    @builtins.property
    @jsii.member(jsii_name="diskEncryption")
    def disk_encryption(self) -> "BatchPoolDiskEncryptionList":
        return typing.cast("BatchPoolDiskEncryptionList", jsii.get(self, "diskEncryption"))

    @builtins.property
    @jsii.member(jsii_name="extensions")
    def extensions(self) -> "BatchPoolExtensionsList":
        return typing.cast("BatchPoolExtensionsList", jsii.get(self, "extensions"))

    @builtins.property
    @jsii.member(jsii_name="fixedScale")
    def fixed_scale(self) -> "BatchPoolFixedScaleOutputReference":
        return typing.cast("BatchPoolFixedScaleOutputReference", jsii.get(self, "fixedScale"))

    @builtins.property
    @jsii.member(jsii_name="identity")
    def identity(self) -> "BatchPoolIdentityOutputReference":
        return typing.cast("BatchPoolIdentityOutputReference", jsii.get(self, "identity"))

    @builtins.property
    @jsii.member(jsii_name="mount")
    def mount(self) -> "BatchPoolMountList":
        return typing.cast("BatchPoolMountList", jsii.get(self, "mount"))

    @builtins.property
    @jsii.member(jsii_name="networkConfiguration")
    def network_configuration(self) -> "BatchPoolNetworkConfigurationOutputReference":
        return typing.cast("BatchPoolNetworkConfigurationOutputReference", jsii.get(self, "networkConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="nodePlacement")
    def node_placement(self) -> "BatchPoolNodePlacementList":
        return typing.cast("BatchPoolNodePlacementList", jsii.get(self, "nodePlacement"))

    @builtins.property
    @jsii.member(jsii_name="startTask")
    def start_task(self) -> "BatchPoolStartTaskOutputReference":
        return typing.cast("BatchPoolStartTaskOutputReference", jsii.get(self, "startTask"))

    @builtins.property
    @jsii.member(jsii_name="storageImageReference")
    def storage_image_reference(
        self,
    ) -> "BatchPoolStorageImageReferenceOutputReference":
        return typing.cast("BatchPoolStorageImageReferenceOutputReference", jsii.get(self, "storageImageReference"))

    @builtins.property
    @jsii.member(jsii_name="taskSchedulingPolicy")
    def task_scheduling_policy(self) -> "BatchPoolTaskSchedulingPolicyList":
        return typing.cast("BatchPoolTaskSchedulingPolicyList", jsii.get(self, "taskSchedulingPolicy"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "BatchPoolTimeoutsOutputReference":
        return typing.cast("BatchPoolTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="userAccounts")
    def user_accounts(self) -> "BatchPoolUserAccountsList":
        return typing.cast("BatchPoolUserAccountsList", jsii.get(self, "userAccounts"))

    @builtins.property
    @jsii.member(jsii_name="windows")
    def windows(self) -> "BatchPoolWindowsList":
        return typing.cast("BatchPoolWindowsList", jsii.get(self, "windows"))

    @builtins.property
    @jsii.member(jsii_name="accountNameInput")
    def account_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountNameInput"))

    @builtins.property
    @jsii.member(jsii_name="autoScaleInput")
    def auto_scale_input(self) -> typing.Optional["BatchPoolAutoScale"]:
        return typing.cast(typing.Optional["BatchPoolAutoScale"], jsii.get(self, "autoScaleInput"))

    @builtins.property
    @jsii.member(jsii_name="certificateInput")
    def certificate_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolCertificate"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolCertificate"]]], jsii.get(self, "certificateInput"))

    @builtins.property
    @jsii.member(jsii_name="containerConfigurationInput")
    def container_configuration_input(
        self,
    ) -> typing.Optional["BatchPoolContainerConfiguration"]:
        return typing.cast(typing.Optional["BatchPoolContainerConfiguration"], jsii.get(self, "containerConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="dataDisksInput")
    def data_disks_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolDataDisks"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolDataDisks"]]], jsii.get(self, "dataDisksInput"))

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionInput")
    def disk_encryption_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolDiskEncryption"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolDiskEncryption"]]], jsii.get(self, "diskEncryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="displayNameInput")
    def display_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayNameInput"))

    @builtins.property
    @jsii.member(jsii_name="extensionsInput")
    def extensions_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolExtensions"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolExtensions"]]], jsii.get(self, "extensionsInput"))

    @builtins.property
    @jsii.member(jsii_name="fixedScaleInput")
    def fixed_scale_input(self) -> typing.Optional["BatchPoolFixedScale"]:
        return typing.cast(typing.Optional["BatchPoolFixedScale"], jsii.get(self, "fixedScaleInput"))

    @builtins.property
    @jsii.member(jsii_name="identityInput")
    def identity_input(self) -> typing.Optional["BatchPoolIdentity"]:
        return typing.cast(typing.Optional["BatchPoolIdentity"], jsii.get(self, "identityInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="interNodeCommunicationInput")
    def inter_node_communication_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "interNodeCommunicationInput"))

    @builtins.property
    @jsii.member(jsii_name="licenseTypeInput")
    def license_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "licenseTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="maxTasksPerNodeInput")
    def max_tasks_per_node_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxTasksPerNodeInput"))

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="mountInput")
    def mount_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolMount"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolMount"]]], jsii.get(self, "mountInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkConfigurationInput")
    def network_configuration_input(
        self,
    ) -> typing.Optional["BatchPoolNetworkConfiguration"]:
        return typing.cast(typing.Optional["BatchPoolNetworkConfiguration"], jsii.get(self, "networkConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeAgentSkuIdInput")
    def node_agent_sku_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nodeAgentSkuIdInput"))

    @builtins.property
    @jsii.member(jsii_name="nodePlacementInput")
    def node_placement_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolNodePlacement"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolNodePlacement"]]], jsii.get(self, "nodePlacementInput"))

    @builtins.property
    @jsii.member(jsii_name="osDiskPlacementInput")
    def os_disk_placement_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "osDiskPlacementInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceGroupNameInput")
    def resource_group_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceGroupNameInput"))

    @builtins.property
    @jsii.member(jsii_name="startTaskInput")
    def start_task_input(self) -> typing.Optional["BatchPoolStartTask"]:
        return typing.cast(typing.Optional["BatchPoolStartTask"], jsii.get(self, "startTaskInput"))

    @builtins.property
    @jsii.member(jsii_name="stopPendingResizeOperationInput")
    def stop_pending_resize_operation_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "stopPendingResizeOperationInput"))

    @builtins.property
    @jsii.member(jsii_name="storageImageReferenceInput")
    def storage_image_reference_input(
        self,
    ) -> typing.Optional["BatchPoolStorageImageReference"]:
        return typing.cast(typing.Optional["BatchPoolStorageImageReference"], jsii.get(self, "storageImageReferenceInput"))

    @builtins.property
    @jsii.member(jsii_name="taskSchedulingPolicyInput")
    def task_scheduling_policy_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolTaskSchedulingPolicy"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolTaskSchedulingPolicy"]]], jsii.get(self, "taskSchedulingPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["BatchPoolTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["BatchPoolTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="userAccountsInput")
    def user_accounts_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolUserAccounts"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolUserAccounts"]]], jsii.get(self, "userAccountsInput"))

    @builtins.property
    @jsii.member(jsii_name="vmSizeInput")
    def vm_size_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vmSizeInput"))

    @builtins.property
    @jsii.member(jsii_name="windowsInput")
    def windows_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolWindows"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolWindows"]]], jsii.get(self, "windowsInput"))

    @builtins.property
    @jsii.member(jsii_name="accountName")
    def account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountName"))

    @account_name.setter
    def account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPool, "account_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountName", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPool, "display_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPool, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="interNodeCommunication")
    def inter_node_communication(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "interNodeCommunication"))

    @inter_node_communication.setter
    def inter_node_communication(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPool, "inter_node_communication").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interNodeCommunication", value)

    @builtins.property
    @jsii.member(jsii_name="licenseType")
    def license_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "licenseType"))

    @license_type.setter
    def license_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPool, "license_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "licenseType", value)

    @builtins.property
    @jsii.member(jsii_name="maxTasksPerNode")
    def max_tasks_per_node(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxTasksPerNode"))

    @max_tasks_per_node.setter
    def max_tasks_per_node(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPool, "max_tasks_per_node").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxTasksPerNode", value)

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "metadata"))

    @metadata.setter
    def metadata(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPool, "metadata").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPool, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="nodeAgentSkuId")
    def node_agent_sku_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nodeAgentSkuId"))

    @node_agent_sku_id.setter
    def node_agent_sku_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPool, "node_agent_sku_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeAgentSkuId", value)

    @builtins.property
    @jsii.member(jsii_name="osDiskPlacement")
    def os_disk_placement(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "osDiskPlacement"))

    @os_disk_placement.setter
    def os_disk_placement(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPool, "os_disk_placement").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "osDiskPlacement", value)

    @builtins.property
    @jsii.member(jsii_name="resourceGroupName")
    def resource_group_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceGroupName"))

    @resource_group_name.setter
    def resource_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPool, "resource_group_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="stopPendingResizeOperation")
    def stop_pending_resize_operation(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "stopPendingResizeOperation"))

    @stop_pending_resize_operation.setter
    def stop_pending_resize_operation(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPool, "stop_pending_resize_operation").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stopPendingResizeOperation", value)

    @builtins.property
    @jsii.member(jsii_name="vmSize")
    def vm_size(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "vmSize"))

    @vm_size.setter
    def vm_size(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPool, "vm_size").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vmSize", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolAutoScale",
    jsii_struct_bases=[],
    name_mapping={"formula": "formula", "evaluation_interval": "evaluationInterval"},
)
class BatchPoolAutoScale:
    def __init__(
        self,
        *,
        formula: builtins.str,
        evaluation_interval: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param formula: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#formula BatchPool#formula}.
        :param evaluation_interval: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#evaluation_interval BatchPool#evaluation_interval}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolAutoScale.__init__)
            check_type(argname="argument formula", value=formula, expected_type=type_hints["formula"])
            check_type(argname="argument evaluation_interval", value=evaluation_interval, expected_type=type_hints["evaluation_interval"])
        self._values: typing.Dict[str, typing.Any] = {
            "formula": formula,
        }
        if evaluation_interval is not None:
            self._values["evaluation_interval"] = evaluation_interval

    @builtins.property
    def formula(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#formula BatchPool#formula}.'''
        result = self._values.get("formula")
        assert result is not None, "Required property 'formula' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def evaluation_interval(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#evaluation_interval BatchPool#evaluation_interval}.'''
        result = self._values.get("evaluation_interval")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchPoolAutoScale(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BatchPoolAutoScaleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolAutoScaleOutputReference",
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
            type_hints = typing.get_type_hints(BatchPoolAutoScaleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEvaluationInterval")
    def reset_evaluation_interval(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEvaluationInterval", []))

    @builtins.property
    @jsii.member(jsii_name="evaluationIntervalInput")
    def evaluation_interval_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "evaluationIntervalInput"))

    @builtins.property
    @jsii.member(jsii_name="formulaInput")
    def formula_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "formulaInput"))

    @builtins.property
    @jsii.member(jsii_name="evaluationInterval")
    def evaluation_interval(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "evaluationInterval"))

    @evaluation_interval.setter
    def evaluation_interval(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolAutoScaleOutputReference, "evaluation_interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "evaluationInterval", value)

    @builtins.property
    @jsii.member(jsii_name="formula")
    def formula(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "formula"))

    @formula.setter
    def formula(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolAutoScaleOutputReference, "formula").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "formula", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[BatchPoolAutoScale]:
        return typing.cast(typing.Optional[BatchPoolAutoScale], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[BatchPoolAutoScale]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolAutoScaleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolCertificate",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "store_location": "storeLocation",
        "store_name": "storeName",
        "visibility": "visibility",
    },
)
class BatchPoolCertificate:
    def __init__(
        self,
        *,
        id: builtins.str,
        store_location: builtins.str,
        store_name: typing.Optional[builtins.str] = None,
        visibility: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#id BatchPool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param store_location: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#store_location BatchPool#store_location}.
        :param store_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#store_name BatchPool#store_name}.
        :param visibility: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#visibility BatchPool#visibility}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolCertificate.__init__)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument store_location", value=store_location, expected_type=type_hints["store_location"])
            check_type(argname="argument store_name", value=store_name, expected_type=type_hints["store_name"])
            check_type(argname="argument visibility", value=visibility, expected_type=type_hints["visibility"])
        self._values: typing.Dict[str, typing.Any] = {
            "id": id,
            "store_location": store_location,
        }
        if store_name is not None:
            self._values["store_name"] = store_name
        if visibility is not None:
            self._values["visibility"] = visibility

    @builtins.property
    def id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#id BatchPool#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        assert result is not None, "Required property 'id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def store_location(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#store_location BatchPool#store_location}.'''
        result = self._values.get("store_location")
        assert result is not None, "Required property 'store_location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def store_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#store_name BatchPool#store_name}.'''
        result = self._values.get("store_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def visibility(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#visibility BatchPool#visibility}.'''
        result = self._values.get("visibility")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchPoolCertificate(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BatchPoolCertificateList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolCertificateList",
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
            type_hints = typing.get_type_hints(BatchPoolCertificateList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "BatchPoolCertificateOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolCertificateList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BatchPoolCertificateOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolCertificateList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolCertificateList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolCertificateList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolCertificate]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolCertificate]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolCertificate]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolCertificateList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BatchPoolCertificateOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolCertificateOutputReference",
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
            type_hints = typing.get_type_hints(BatchPoolCertificateOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetStoreName")
    def reset_store_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStoreName", []))

    @jsii.member(jsii_name="resetVisibility")
    def reset_visibility(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVisibility", []))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="storeLocationInput")
    def store_location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storeLocationInput"))

    @builtins.property
    @jsii.member(jsii_name="storeNameInput")
    def store_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storeNameInput"))

    @builtins.property
    @jsii.member(jsii_name="visibilityInput")
    def visibility_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "visibilityInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolCertificateOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="storeLocation")
    def store_location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storeLocation"))

    @store_location.setter
    def store_location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolCertificateOutputReference, "store_location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storeLocation", value)

    @builtins.property
    @jsii.member(jsii_name="storeName")
    def store_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storeName"))

    @store_name.setter
    def store_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolCertificateOutputReference, "store_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storeName", value)

    @builtins.property
    @jsii.member(jsii_name="visibility")
    def visibility(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "visibility"))

    @visibility.setter
    def visibility(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolCertificateOutputReference, "visibility").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "visibility", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BatchPoolCertificate, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BatchPoolCertificate, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BatchPoolCertificate, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolCertificateOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "account_name": "accountName",
        "name": "name",
        "node_agent_sku_id": "nodeAgentSkuId",
        "resource_group_name": "resourceGroupName",
        "storage_image_reference": "storageImageReference",
        "vm_size": "vmSize",
        "auto_scale": "autoScale",
        "certificate": "certificate",
        "container_configuration": "containerConfiguration",
        "data_disks": "dataDisks",
        "disk_encryption": "diskEncryption",
        "display_name": "displayName",
        "extensions": "extensions",
        "fixed_scale": "fixedScale",
        "id": "id",
        "identity": "identity",
        "inter_node_communication": "interNodeCommunication",
        "license_type": "licenseType",
        "max_tasks_per_node": "maxTasksPerNode",
        "metadata": "metadata",
        "mount": "mount",
        "network_configuration": "networkConfiguration",
        "node_placement": "nodePlacement",
        "os_disk_placement": "osDiskPlacement",
        "start_task": "startTask",
        "stop_pending_resize_operation": "stopPendingResizeOperation",
        "task_scheduling_policy": "taskSchedulingPolicy",
        "timeouts": "timeouts",
        "user_accounts": "userAccounts",
        "windows": "windows",
    },
)
class BatchPoolConfig(cdktf.TerraformMetaArguments):
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
        account_name: builtins.str,
        name: builtins.str,
        node_agent_sku_id: builtins.str,
        resource_group_name: builtins.str,
        storage_image_reference: typing.Union["BatchPoolStorageImageReference", typing.Dict[str, typing.Any]],
        vm_size: builtins.str,
        auto_scale: typing.Optional[typing.Union[BatchPoolAutoScale, typing.Dict[str, typing.Any]]] = None,
        certificate: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[BatchPoolCertificate, typing.Dict[str, typing.Any]]]]] = None,
        container_configuration: typing.Optional[typing.Union["BatchPoolContainerConfiguration", typing.Dict[str, typing.Any]]] = None,
        data_disks: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolDataDisks", typing.Dict[str, typing.Any]]]]] = None,
        disk_encryption: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolDiskEncryption", typing.Dict[str, typing.Any]]]]] = None,
        display_name: typing.Optional[builtins.str] = None,
        extensions: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolExtensions", typing.Dict[str, typing.Any]]]]] = None,
        fixed_scale: typing.Optional[typing.Union["BatchPoolFixedScale", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        identity: typing.Optional[typing.Union["BatchPoolIdentity", typing.Dict[str, typing.Any]]] = None,
        inter_node_communication: typing.Optional[builtins.str] = None,
        license_type: typing.Optional[builtins.str] = None,
        max_tasks_per_node: typing.Optional[jsii.Number] = None,
        metadata: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        mount: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolMount", typing.Dict[str, typing.Any]]]]] = None,
        network_configuration: typing.Optional[typing.Union["BatchPoolNetworkConfiguration", typing.Dict[str, typing.Any]]] = None,
        node_placement: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolNodePlacement", typing.Dict[str, typing.Any]]]]] = None,
        os_disk_placement: typing.Optional[builtins.str] = None,
        start_task: typing.Optional[typing.Union["BatchPoolStartTask", typing.Dict[str, typing.Any]]] = None,
        stop_pending_resize_operation: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        task_scheduling_policy: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolTaskSchedulingPolicy", typing.Dict[str, typing.Any]]]]] = None,
        timeouts: typing.Optional[typing.Union["BatchPoolTimeouts", typing.Dict[str, typing.Any]]] = None,
        user_accounts: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolUserAccounts", typing.Dict[str, typing.Any]]]]] = None,
        windows: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolWindows", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#account_name BatchPool#account_name}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#name BatchPool#name}.
        :param node_agent_sku_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#node_agent_sku_id BatchPool#node_agent_sku_id}.
        :param resource_group_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#resource_group_name BatchPool#resource_group_name}.
        :param storage_image_reference: storage_image_reference block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#storage_image_reference BatchPool#storage_image_reference}
        :param vm_size: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#vm_size BatchPool#vm_size}.
        :param auto_scale: auto_scale block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#auto_scale BatchPool#auto_scale}
        :param certificate: certificate block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#certificate BatchPool#certificate}
        :param container_configuration: container_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#container_configuration BatchPool#container_configuration}
        :param data_disks: data_disks block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#data_disks BatchPool#data_disks}
        :param disk_encryption: disk_encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#disk_encryption BatchPool#disk_encryption}
        :param display_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#display_name BatchPool#display_name}.
        :param extensions: extensions block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#extensions BatchPool#extensions}
        :param fixed_scale: fixed_scale block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#fixed_scale BatchPool#fixed_scale}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#id BatchPool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param identity: identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#identity BatchPool#identity}
        :param inter_node_communication: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#inter_node_communication BatchPool#inter_node_communication}.
        :param license_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#license_type BatchPool#license_type}.
        :param max_tasks_per_node: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#max_tasks_per_node BatchPool#max_tasks_per_node}.
        :param metadata: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#metadata BatchPool#metadata}.
        :param mount: mount block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#mount BatchPool#mount}
        :param network_configuration: network_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#network_configuration BatchPool#network_configuration}
        :param node_placement: node_placement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#node_placement BatchPool#node_placement}
        :param os_disk_placement: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#os_disk_placement BatchPool#os_disk_placement}.
        :param start_task: start_task block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#start_task BatchPool#start_task}
        :param stop_pending_resize_operation: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#stop_pending_resize_operation BatchPool#stop_pending_resize_operation}.
        :param task_scheduling_policy: task_scheduling_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#task_scheduling_policy BatchPool#task_scheduling_policy}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#timeouts BatchPool#timeouts}
        :param user_accounts: user_accounts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#user_accounts BatchPool#user_accounts}
        :param windows: windows block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#windows BatchPool#windows}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(storage_image_reference, dict):
            storage_image_reference = BatchPoolStorageImageReference(**storage_image_reference)
        if isinstance(auto_scale, dict):
            auto_scale = BatchPoolAutoScale(**auto_scale)
        if isinstance(container_configuration, dict):
            container_configuration = BatchPoolContainerConfiguration(**container_configuration)
        if isinstance(fixed_scale, dict):
            fixed_scale = BatchPoolFixedScale(**fixed_scale)
        if isinstance(identity, dict):
            identity = BatchPoolIdentity(**identity)
        if isinstance(network_configuration, dict):
            network_configuration = BatchPoolNetworkConfiguration(**network_configuration)
        if isinstance(start_task, dict):
            start_task = BatchPoolStartTask(**start_task)
        if isinstance(timeouts, dict):
            timeouts = BatchPoolTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument account_name", value=account_name, expected_type=type_hints["account_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument node_agent_sku_id", value=node_agent_sku_id, expected_type=type_hints["node_agent_sku_id"])
            check_type(argname="argument resource_group_name", value=resource_group_name, expected_type=type_hints["resource_group_name"])
            check_type(argname="argument storage_image_reference", value=storage_image_reference, expected_type=type_hints["storage_image_reference"])
            check_type(argname="argument vm_size", value=vm_size, expected_type=type_hints["vm_size"])
            check_type(argname="argument auto_scale", value=auto_scale, expected_type=type_hints["auto_scale"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument container_configuration", value=container_configuration, expected_type=type_hints["container_configuration"])
            check_type(argname="argument data_disks", value=data_disks, expected_type=type_hints["data_disks"])
            check_type(argname="argument disk_encryption", value=disk_encryption, expected_type=type_hints["disk_encryption"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument extensions", value=extensions, expected_type=type_hints["extensions"])
            check_type(argname="argument fixed_scale", value=fixed_scale, expected_type=type_hints["fixed_scale"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument inter_node_communication", value=inter_node_communication, expected_type=type_hints["inter_node_communication"])
            check_type(argname="argument license_type", value=license_type, expected_type=type_hints["license_type"])
            check_type(argname="argument max_tasks_per_node", value=max_tasks_per_node, expected_type=type_hints["max_tasks_per_node"])
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            check_type(argname="argument mount", value=mount, expected_type=type_hints["mount"])
            check_type(argname="argument network_configuration", value=network_configuration, expected_type=type_hints["network_configuration"])
            check_type(argname="argument node_placement", value=node_placement, expected_type=type_hints["node_placement"])
            check_type(argname="argument os_disk_placement", value=os_disk_placement, expected_type=type_hints["os_disk_placement"])
            check_type(argname="argument start_task", value=start_task, expected_type=type_hints["start_task"])
            check_type(argname="argument stop_pending_resize_operation", value=stop_pending_resize_operation, expected_type=type_hints["stop_pending_resize_operation"])
            check_type(argname="argument task_scheduling_policy", value=task_scheduling_policy, expected_type=type_hints["task_scheduling_policy"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument user_accounts", value=user_accounts, expected_type=type_hints["user_accounts"])
            check_type(argname="argument windows", value=windows, expected_type=type_hints["windows"])
        self._values: typing.Dict[str, typing.Any] = {
            "account_name": account_name,
            "name": name,
            "node_agent_sku_id": node_agent_sku_id,
            "resource_group_name": resource_group_name,
            "storage_image_reference": storage_image_reference,
            "vm_size": vm_size,
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
        if auto_scale is not None:
            self._values["auto_scale"] = auto_scale
        if certificate is not None:
            self._values["certificate"] = certificate
        if container_configuration is not None:
            self._values["container_configuration"] = container_configuration
        if data_disks is not None:
            self._values["data_disks"] = data_disks
        if disk_encryption is not None:
            self._values["disk_encryption"] = disk_encryption
        if display_name is not None:
            self._values["display_name"] = display_name
        if extensions is not None:
            self._values["extensions"] = extensions
        if fixed_scale is not None:
            self._values["fixed_scale"] = fixed_scale
        if id is not None:
            self._values["id"] = id
        if identity is not None:
            self._values["identity"] = identity
        if inter_node_communication is not None:
            self._values["inter_node_communication"] = inter_node_communication
        if license_type is not None:
            self._values["license_type"] = license_type
        if max_tasks_per_node is not None:
            self._values["max_tasks_per_node"] = max_tasks_per_node
        if metadata is not None:
            self._values["metadata"] = metadata
        if mount is not None:
            self._values["mount"] = mount
        if network_configuration is not None:
            self._values["network_configuration"] = network_configuration
        if node_placement is not None:
            self._values["node_placement"] = node_placement
        if os_disk_placement is not None:
            self._values["os_disk_placement"] = os_disk_placement
        if start_task is not None:
            self._values["start_task"] = start_task
        if stop_pending_resize_operation is not None:
            self._values["stop_pending_resize_operation"] = stop_pending_resize_operation
        if task_scheduling_policy is not None:
            self._values["task_scheduling_policy"] = task_scheduling_policy
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if user_accounts is not None:
            self._values["user_accounts"] = user_accounts
        if windows is not None:
            self._values["windows"] = windows

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
    def account_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#account_name BatchPool#account_name}.'''
        result = self._values.get("account_name")
        assert result is not None, "Required property 'account_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#name BatchPool#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def node_agent_sku_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#node_agent_sku_id BatchPool#node_agent_sku_id}.'''
        result = self._values.get("node_agent_sku_id")
        assert result is not None, "Required property 'node_agent_sku_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_group_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#resource_group_name BatchPool#resource_group_name}.'''
        result = self._values.get("resource_group_name")
        assert result is not None, "Required property 'resource_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_image_reference(self) -> "BatchPoolStorageImageReference":
        '''storage_image_reference block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#storage_image_reference BatchPool#storage_image_reference}
        '''
        result = self._values.get("storage_image_reference")
        assert result is not None, "Required property 'storage_image_reference' is missing"
        return typing.cast("BatchPoolStorageImageReference", result)

    @builtins.property
    def vm_size(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#vm_size BatchPool#vm_size}.'''
        result = self._values.get("vm_size")
        assert result is not None, "Required property 'vm_size' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_scale(self) -> typing.Optional[BatchPoolAutoScale]:
        '''auto_scale block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#auto_scale BatchPool#auto_scale}
        '''
        result = self._values.get("auto_scale")
        return typing.cast(typing.Optional[BatchPoolAutoScale], result)

    @builtins.property
    def certificate(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolCertificate]]]:
        '''certificate block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#certificate BatchPool#certificate}
        '''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolCertificate]]], result)

    @builtins.property
    def container_configuration(
        self,
    ) -> typing.Optional["BatchPoolContainerConfiguration"]:
        '''container_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#container_configuration BatchPool#container_configuration}
        '''
        result = self._values.get("container_configuration")
        return typing.cast(typing.Optional["BatchPoolContainerConfiguration"], result)

    @builtins.property
    def data_disks(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolDataDisks"]]]:
        '''data_disks block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#data_disks BatchPool#data_disks}
        '''
        result = self._values.get("data_disks")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolDataDisks"]]], result)

    @builtins.property
    def disk_encryption(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolDiskEncryption"]]]:
        '''disk_encryption block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#disk_encryption BatchPool#disk_encryption}
        '''
        result = self._values.get("disk_encryption")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolDiskEncryption"]]], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#display_name BatchPool#display_name}.'''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extensions(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolExtensions"]]]:
        '''extensions block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#extensions BatchPool#extensions}
        '''
        result = self._values.get("extensions")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolExtensions"]]], result)

    @builtins.property
    def fixed_scale(self) -> typing.Optional["BatchPoolFixedScale"]:
        '''fixed_scale block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#fixed_scale BatchPool#fixed_scale}
        '''
        result = self._values.get("fixed_scale")
        return typing.cast(typing.Optional["BatchPoolFixedScale"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#id BatchPool#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity(self) -> typing.Optional["BatchPoolIdentity"]:
        '''identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#identity BatchPool#identity}
        '''
        result = self._values.get("identity")
        return typing.cast(typing.Optional["BatchPoolIdentity"], result)

    @builtins.property
    def inter_node_communication(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#inter_node_communication BatchPool#inter_node_communication}.'''
        result = self._values.get("inter_node_communication")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def license_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#license_type BatchPool#license_type}.'''
        result = self._values.get("license_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_tasks_per_node(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#max_tasks_per_node BatchPool#max_tasks_per_node}.'''
        result = self._values.get("max_tasks_per_node")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def metadata(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#metadata BatchPool#metadata}.'''
        result = self._values.get("metadata")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def mount(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolMount"]]]:
        '''mount block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#mount BatchPool#mount}
        '''
        result = self._values.get("mount")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolMount"]]], result)

    @builtins.property
    def network_configuration(self) -> typing.Optional["BatchPoolNetworkConfiguration"]:
        '''network_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#network_configuration BatchPool#network_configuration}
        '''
        result = self._values.get("network_configuration")
        return typing.cast(typing.Optional["BatchPoolNetworkConfiguration"], result)

    @builtins.property
    def node_placement(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolNodePlacement"]]]:
        '''node_placement block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#node_placement BatchPool#node_placement}
        '''
        result = self._values.get("node_placement")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolNodePlacement"]]], result)

    @builtins.property
    def os_disk_placement(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#os_disk_placement BatchPool#os_disk_placement}.'''
        result = self._values.get("os_disk_placement")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def start_task(self) -> typing.Optional["BatchPoolStartTask"]:
        '''start_task block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#start_task BatchPool#start_task}
        '''
        result = self._values.get("start_task")
        return typing.cast(typing.Optional["BatchPoolStartTask"], result)

    @builtins.property
    def stop_pending_resize_operation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#stop_pending_resize_operation BatchPool#stop_pending_resize_operation}.'''
        result = self._values.get("stop_pending_resize_operation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def task_scheduling_policy(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolTaskSchedulingPolicy"]]]:
        '''task_scheduling_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#task_scheduling_policy BatchPool#task_scheduling_policy}
        '''
        result = self._values.get("task_scheduling_policy")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolTaskSchedulingPolicy"]]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["BatchPoolTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#timeouts BatchPool#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["BatchPoolTimeouts"], result)

    @builtins.property
    def user_accounts(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolUserAccounts"]]]:
        '''user_accounts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#user_accounts BatchPool#user_accounts}
        '''
        result = self._values.get("user_accounts")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolUserAccounts"]]], result)

    @builtins.property
    def windows(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolWindows"]]]:
        '''windows block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#windows BatchPool#windows}
        '''
        result = self._values.get("windows")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolWindows"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchPoolConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolContainerConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "container_image_names": "containerImageNames",
        "container_registries": "containerRegistries",
        "type": "type",
    },
)
class BatchPoolContainerConfiguration:
    def __init__(
        self,
        *,
        container_image_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        container_registries: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolContainerConfigurationContainerRegistries", typing.Dict[str, typing.Any]]]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param container_image_names: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#container_image_names BatchPool#container_image_names}.
        :param container_registries: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#container_registries BatchPool#container_registries}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#type BatchPool#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolContainerConfiguration.__init__)
            check_type(argname="argument container_image_names", value=container_image_names, expected_type=type_hints["container_image_names"])
            check_type(argname="argument container_registries", value=container_registries, expected_type=type_hints["container_registries"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if container_image_names is not None:
            self._values["container_image_names"] = container_image_names
        if container_registries is not None:
            self._values["container_registries"] = container_registries
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def container_image_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#container_image_names BatchPool#container_image_names}.'''
        result = self._values.get("container_image_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def container_registries(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolContainerConfigurationContainerRegistries"]]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#container_registries BatchPool#container_registries}.'''
        result = self._values.get("container_registries")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolContainerConfigurationContainerRegistries"]]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#type BatchPool#type}.'''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchPoolContainerConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolContainerConfigurationContainerRegistries",
    jsii_struct_bases=[],
    name_mapping={
        "password": "password",
        "registry_server": "registryServer",
        "user_assigned_identity_id": "userAssignedIdentityId",
        "user_name": "userName",
    },
)
class BatchPoolContainerConfigurationContainerRegistries:
    def __init__(
        self,
        *,
        password: typing.Optional[builtins.str] = None,
        registry_server: typing.Optional[builtins.str] = None,
        user_assigned_identity_id: typing.Optional[builtins.str] = None,
        user_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#password BatchPool#password}.
        :param registry_server: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#registry_server BatchPool#registry_server}.
        :param user_assigned_identity_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#user_assigned_identity_id BatchPool#user_assigned_identity_id}.
        :param user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#user_name BatchPool#user_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolContainerConfigurationContainerRegistries.__init__)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument registry_server", value=registry_server, expected_type=type_hints["registry_server"])
            check_type(argname="argument user_assigned_identity_id", value=user_assigned_identity_id, expected_type=type_hints["user_assigned_identity_id"])
            check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if password is not None:
            self._values["password"] = password
        if registry_server is not None:
            self._values["registry_server"] = registry_server
        if user_assigned_identity_id is not None:
            self._values["user_assigned_identity_id"] = user_assigned_identity_id
        if user_name is not None:
            self._values["user_name"] = user_name

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#password BatchPool#password}.'''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def registry_server(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#registry_server BatchPool#registry_server}.'''
        result = self._values.get("registry_server")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_assigned_identity_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#user_assigned_identity_id BatchPool#user_assigned_identity_id}.'''
        result = self._values.get("user_assigned_identity_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#user_name BatchPool#user_name}.'''
        result = self._values.get("user_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchPoolContainerConfigurationContainerRegistries(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BatchPoolContainerConfigurationContainerRegistriesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolContainerConfigurationContainerRegistriesList",
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
            type_hints = typing.get_type_hints(BatchPoolContainerConfigurationContainerRegistriesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "BatchPoolContainerConfigurationContainerRegistriesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolContainerConfigurationContainerRegistriesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BatchPoolContainerConfigurationContainerRegistriesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolContainerConfigurationContainerRegistriesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolContainerConfigurationContainerRegistriesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolContainerConfigurationContainerRegistriesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolContainerConfigurationContainerRegistries]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolContainerConfigurationContainerRegistries]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolContainerConfigurationContainerRegistries]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolContainerConfigurationContainerRegistriesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BatchPoolContainerConfigurationContainerRegistriesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolContainerConfigurationContainerRegistriesOutputReference",
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
            type_hints = typing.get_type_hints(BatchPoolContainerConfigurationContainerRegistriesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetRegistryServer")
    def reset_registry_server(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegistryServer", []))

    @jsii.member(jsii_name="resetUserAssignedIdentityId")
    def reset_user_assigned_identity_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserAssignedIdentityId", []))

    @jsii.member(jsii_name="resetUserName")
    def reset_user_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserName", []))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="registryServerInput")
    def registry_server_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "registryServerInput"))

    @builtins.property
    @jsii.member(jsii_name="userAssignedIdentityIdInput")
    def user_assigned_identity_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userAssignedIdentityIdInput"))

    @builtins.property
    @jsii.member(jsii_name="userNameInput")
    def user_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userNameInput"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolContainerConfigurationContainerRegistriesOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="registryServer")
    def registry_server(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registryServer"))

    @registry_server.setter
    def registry_server(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolContainerConfigurationContainerRegistriesOutputReference, "registry_server").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registryServer", value)

    @builtins.property
    @jsii.member(jsii_name="userAssignedIdentityId")
    def user_assigned_identity_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userAssignedIdentityId"))

    @user_assigned_identity_id.setter
    def user_assigned_identity_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolContainerConfigurationContainerRegistriesOutputReference, "user_assigned_identity_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userAssignedIdentityId", value)

    @builtins.property
    @jsii.member(jsii_name="userName")
    def user_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userName"))

    @user_name.setter
    def user_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolContainerConfigurationContainerRegistriesOutputReference, "user_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BatchPoolContainerConfigurationContainerRegistries, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BatchPoolContainerConfigurationContainerRegistries, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BatchPoolContainerConfigurationContainerRegistries, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolContainerConfigurationContainerRegistriesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BatchPoolContainerConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolContainerConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(BatchPoolContainerConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putContainerRegistries")
    def put_container_registries(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[BatchPoolContainerConfigurationContainerRegistries, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolContainerConfigurationOutputReference.put_container_registries)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putContainerRegistries", [value]))

    @jsii.member(jsii_name="resetContainerImageNames")
    def reset_container_image_names(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerImageNames", []))

    @jsii.member(jsii_name="resetContainerRegistries")
    def reset_container_registries(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainerRegistries", []))

    @jsii.member(jsii_name="resetType")
    def reset_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetType", []))

    @builtins.property
    @jsii.member(jsii_name="containerRegistries")
    def container_registries(
        self,
    ) -> BatchPoolContainerConfigurationContainerRegistriesList:
        return typing.cast(BatchPoolContainerConfigurationContainerRegistriesList, jsii.get(self, "containerRegistries"))

    @builtins.property
    @jsii.member(jsii_name="containerImageNamesInput")
    def container_image_names_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "containerImageNamesInput"))

    @builtins.property
    @jsii.member(jsii_name="containerRegistriesInput")
    def container_registries_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolContainerConfigurationContainerRegistries]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolContainerConfigurationContainerRegistries]]], jsii.get(self, "containerRegistriesInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="containerImageNames")
    def container_image_names(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "containerImageNames"))

    @container_image_names.setter
    def container_image_names(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolContainerConfigurationOutputReference, "container_image_names").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerImageNames", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolContainerConfigurationOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[BatchPoolContainerConfiguration]:
        return typing.cast(typing.Optional[BatchPoolContainerConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BatchPoolContainerConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolContainerConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolDataDisks",
    jsii_struct_bases=[],
    name_mapping={
        "disk_size_gb": "diskSizeGb",
        "lun": "lun",
        "caching": "caching",
        "storage_account_type": "storageAccountType",
    },
)
class BatchPoolDataDisks:
    def __init__(
        self,
        *,
        disk_size_gb: jsii.Number,
        lun: jsii.Number,
        caching: typing.Optional[builtins.str] = None,
        storage_account_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param disk_size_gb: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#disk_size_gb BatchPool#disk_size_gb}.
        :param lun: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#lun BatchPool#lun}.
        :param caching: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#caching BatchPool#caching}.
        :param storage_account_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#storage_account_type BatchPool#storage_account_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolDataDisks.__init__)
            check_type(argname="argument disk_size_gb", value=disk_size_gb, expected_type=type_hints["disk_size_gb"])
            check_type(argname="argument lun", value=lun, expected_type=type_hints["lun"])
            check_type(argname="argument caching", value=caching, expected_type=type_hints["caching"])
            check_type(argname="argument storage_account_type", value=storage_account_type, expected_type=type_hints["storage_account_type"])
        self._values: typing.Dict[str, typing.Any] = {
            "disk_size_gb": disk_size_gb,
            "lun": lun,
        }
        if caching is not None:
            self._values["caching"] = caching
        if storage_account_type is not None:
            self._values["storage_account_type"] = storage_account_type

    @builtins.property
    def disk_size_gb(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#disk_size_gb BatchPool#disk_size_gb}.'''
        result = self._values.get("disk_size_gb")
        assert result is not None, "Required property 'disk_size_gb' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def lun(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#lun BatchPool#lun}.'''
        result = self._values.get("lun")
        assert result is not None, "Required property 'lun' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def caching(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#caching BatchPool#caching}.'''
        result = self._values.get("caching")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_account_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#storage_account_type BatchPool#storage_account_type}.'''
        result = self._values.get("storage_account_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchPoolDataDisks(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BatchPoolDataDisksList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolDataDisksList",
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
            type_hints = typing.get_type_hints(BatchPoolDataDisksList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "BatchPoolDataDisksOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolDataDisksList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BatchPoolDataDisksOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolDataDisksList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolDataDisksList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolDataDisksList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolDataDisks]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolDataDisks]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolDataDisks]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolDataDisksList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BatchPoolDataDisksOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolDataDisksOutputReference",
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
            type_hints = typing.get_type_hints(BatchPoolDataDisksOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetCaching")
    def reset_caching(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCaching", []))

    @jsii.member(jsii_name="resetStorageAccountType")
    def reset_storage_account_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageAccountType", []))

    @builtins.property
    @jsii.member(jsii_name="cachingInput")
    def caching_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cachingInput"))

    @builtins.property
    @jsii.member(jsii_name="diskSizeGbInput")
    def disk_size_gb_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "diskSizeGbInput"))

    @builtins.property
    @jsii.member(jsii_name="lunInput")
    def lun_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "lunInput"))

    @builtins.property
    @jsii.member(jsii_name="storageAccountTypeInput")
    def storage_account_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageAccountTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="caching")
    def caching(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "caching"))

    @caching.setter
    def caching(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolDataDisksOutputReference, "caching").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "caching", value)

    @builtins.property
    @jsii.member(jsii_name="diskSizeGb")
    def disk_size_gb(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "diskSizeGb"))

    @disk_size_gb.setter
    def disk_size_gb(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolDataDisksOutputReference, "disk_size_gb").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskSizeGb", value)

    @builtins.property
    @jsii.member(jsii_name="lun")
    def lun(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lun"))

    @lun.setter
    def lun(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolDataDisksOutputReference, "lun").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lun", value)

    @builtins.property
    @jsii.member(jsii_name="storageAccountType")
    def storage_account_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageAccountType"))

    @storage_account_type.setter
    def storage_account_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolDataDisksOutputReference, "storage_account_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageAccountType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BatchPoolDataDisks, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BatchPoolDataDisks, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BatchPoolDataDisks, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolDataDisksOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolDiskEncryption",
    jsii_struct_bases=[],
    name_mapping={"disk_encryption_target": "diskEncryptionTarget"},
)
class BatchPoolDiskEncryption:
    def __init__(self, *, disk_encryption_target: builtins.str) -> None:
        '''
        :param disk_encryption_target: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#disk_encryption_target BatchPool#disk_encryption_target}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolDiskEncryption.__init__)
            check_type(argname="argument disk_encryption_target", value=disk_encryption_target, expected_type=type_hints["disk_encryption_target"])
        self._values: typing.Dict[str, typing.Any] = {
            "disk_encryption_target": disk_encryption_target,
        }

    @builtins.property
    def disk_encryption_target(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#disk_encryption_target BatchPool#disk_encryption_target}.'''
        result = self._values.get("disk_encryption_target")
        assert result is not None, "Required property 'disk_encryption_target' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchPoolDiskEncryption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BatchPoolDiskEncryptionList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolDiskEncryptionList",
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
            type_hints = typing.get_type_hints(BatchPoolDiskEncryptionList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "BatchPoolDiskEncryptionOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolDiskEncryptionList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BatchPoolDiskEncryptionOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolDiskEncryptionList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolDiskEncryptionList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolDiskEncryptionList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolDiskEncryption]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolDiskEncryption]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolDiskEncryption]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolDiskEncryptionList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BatchPoolDiskEncryptionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolDiskEncryptionOutputReference",
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
            type_hints = typing.get_type_hints(BatchPoolDiskEncryptionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionTargetInput")
    def disk_encryption_target_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "diskEncryptionTargetInput"))

    @builtins.property
    @jsii.member(jsii_name="diskEncryptionTarget")
    def disk_encryption_target(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "diskEncryptionTarget"))

    @disk_encryption_target.setter
    def disk_encryption_target(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolDiskEncryptionOutputReference, "disk_encryption_target").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "diskEncryptionTarget", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BatchPoolDiskEncryption, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BatchPoolDiskEncryption, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BatchPoolDiskEncryption, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolDiskEncryptionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolExtensions",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "publisher": "publisher",
        "type": "type",
        "auto_upgrade_minor_version": "autoUpgradeMinorVersion",
        "protected_settings": "protectedSettings",
        "provision_after_extensions": "provisionAfterExtensions",
        "settings_json": "settingsJson",
        "type_handler_version": "typeHandlerVersion",
    },
)
class BatchPoolExtensions:
    def __init__(
        self,
        *,
        name: builtins.str,
        publisher: builtins.str,
        type: builtins.str,
        auto_upgrade_minor_version: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        protected_settings: typing.Optional[builtins.str] = None,
        provision_after_extensions: typing.Optional[typing.Sequence[builtins.str]] = None,
        settings_json: typing.Optional[builtins.str] = None,
        type_handler_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#name BatchPool#name}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#publisher BatchPool#publisher}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#type BatchPool#type}.
        :param auto_upgrade_minor_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#auto_upgrade_minor_version BatchPool#auto_upgrade_minor_version}.
        :param protected_settings: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#protected_settings BatchPool#protected_settings}.
        :param provision_after_extensions: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#provision_after_extensions BatchPool#provision_after_extensions}.
        :param settings_json: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#settings_json BatchPool#settings_json}.
        :param type_handler_version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#type_handler_version BatchPool#type_handler_version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolExtensions.__init__)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument publisher", value=publisher, expected_type=type_hints["publisher"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument auto_upgrade_minor_version", value=auto_upgrade_minor_version, expected_type=type_hints["auto_upgrade_minor_version"])
            check_type(argname="argument protected_settings", value=protected_settings, expected_type=type_hints["protected_settings"])
            check_type(argname="argument provision_after_extensions", value=provision_after_extensions, expected_type=type_hints["provision_after_extensions"])
            check_type(argname="argument settings_json", value=settings_json, expected_type=type_hints["settings_json"])
            check_type(argname="argument type_handler_version", value=type_handler_version, expected_type=type_hints["type_handler_version"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "publisher": publisher,
            "type": type,
        }
        if auto_upgrade_minor_version is not None:
            self._values["auto_upgrade_minor_version"] = auto_upgrade_minor_version
        if protected_settings is not None:
            self._values["protected_settings"] = protected_settings
        if provision_after_extensions is not None:
            self._values["provision_after_extensions"] = provision_after_extensions
        if settings_json is not None:
            self._values["settings_json"] = settings_json
        if type_handler_version is not None:
            self._values["type_handler_version"] = type_handler_version

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#name BatchPool#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def publisher(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#publisher BatchPool#publisher}.'''
        result = self._values.get("publisher")
        assert result is not None, "Required property 'publisher' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#type BatchPool#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_upgrade_minor_version(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#auto_upgrade_minor_version BatchPool#auto_upgrade_minor_version}.'''
        result = self._values.get("auto_upgrade_minor_version")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def protected_settings(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#protected_settings BatchPool#protected_settings}.'''
        result = self._values.get("protected_settings")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provision_after_extensions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#provision_after_extensions BatchPool#provision_after_extensions}.'''
        result = self._values.get("provision_after_extensions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def settings_json(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#settings_json BatchPool#settings_json}.'''
        result = self._values.get("settings_json")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type_handler_version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#type_handler_version BatchPool#type_handler_version}.'''
        result = self._values.get("type_handler_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchPoolExtensions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BatchPoolExtensionsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolExtensionsList",
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
            type_hints = typing.get_type_hints(BatchPoolExtensionsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "BatchPoolExtensionsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolExtensionsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BatchPoolExtensionsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolExtensionsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolExtensionsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolExtensionsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolExtensions]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolExtensions]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolExtensions]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolExtensionsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BatchPoolExtensionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolExtensionsOutputReference",
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
            type_hints = typing.get_type_hints(BatchPoolExtensionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAutoUpgradeMinorVersion")
    def reset_auto_upgrade_minor_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoUpgradeMinorVersion", []))

    @jsii.member(jsii_name="resetProtectedSettings")
    def reset_protected_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProtectedSettings", []))

    @jsii.member(jsii_name="resetProvisionAfterExtensions")
    def reset_provision_after_extensions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProvisionAfterExtensions", []))

    @jsii.member(jsii_name="resetSettingsJson")
    def reset_settings_json(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSettingsJson", []))

    @jsii.member(jsii_name="resetTypeHandlerVersion")
    def reset_type_handler_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTypeHandlerVersion", []))

    @builtins.property
    @jsii.member(jsii_name="autoUpgradeMinorVersionInput")
    def auto_upgrade_minor_version_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autoUpgradeMinorVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="protectedSettingsInput")
    def protected_settings_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protectedSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="provisionAfterExtensionsInput")
    def provision_after_extensions_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "provisionAfterExtensionsInput"))

    @builtins.property
    @jsii.member(jsii_name="publisherInput")
    def publisher_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publisherInput"))

    @builtins.property
    @jsii.member(jsii_name="settingsJsonInput")
    def settings_json_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "settingsJsonInput"))

    @builtins.property
    @jsii.member(jsii_name="typeHandlerVersionInput")
    def type_handler_version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeHandlerVersionInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="autoUpgradeMinorVersion")
    def auto_upgrade_minor_version(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autoUpgradeMinorVersion"))

    @auto_upgrade_minor_version.setter
    def auto_upgrade_minor_version(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolExtensionsOutputReference, "auto_upgrade_minor_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoUpgradeMinorVersion", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolExtensionsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="protectedSettings")
    def protected_settings(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protectedSettings"))

    @protected_settings.setter
    def protected_settings(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolExtensionsOutputReference, "protected_settings").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protectedSettings", value)

    @builtins.property
    @jsii.member(jsii_name="provisionAfterExtensions")
    def provision_after_extensions(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "provisionAfterExtensions"))

    @provision_after_extensions.setter
    def provision_after_extensions(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolExtensionsOutputReference, "provision_after_extensions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisionAfterExtensions", value)

    @builtins.property
    @jsii.member(jsii_name="publisher")
    def publisher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publisher"))

    @publisher.setter
    def publisher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolExtensionsOutputReference, "publisher").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publisher", value)

    @builtins.property
    @jsii.member(jsii_name="settingsJson")
    def settings_json(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "settingsJson"))

    @settings_json.setter
    def settings_json(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolExtensionsOutputReference, "settings_json").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "settingsJson", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolExtensionsOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="typeHandlerVersion")
    def type_handler_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "typeHandlerVersion"))

    @type_handler_version.setter
    def type_handler_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolExtensionsOutputReference, "type_handler_version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "typeHandlerVersion", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BatchPoolExtensions, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BatchPoolExtensions, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BatchPoolExtensions, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolExtensionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolFixedScale",
    jsii_struct_bases=[],
    name_mapping={
        "node_deallocation_method": "nodeDeallocationMethod",
        "resize_timeout": "resizeTimeout",
        "target_dedicated_nodes": "targetDedicatedNodes",
        "target_low_priority_nodes": "targetLowPriorityNodes",
    },
)
class BatchPoolFixedScale:
    def __init__(
        self,
        *,
        node_deallocation_method: typing.Optional[builtins.str] = None,
        resize_timeout: typing.Optional[builtins.str] = None,
        target_dedicated_nodes: typing.Optional[jsii.Number] = None,
        target_low_priority_nodes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param node_deallocation_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#node_deallocation_method BatchPool#node_deallocation_method}.
        :param resize_timeout: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#resize_timeout BatchPool#resize_timeout}.
        :param target_dedicated_nodes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#target_dedicated_nodes BatchPool#target_dedicated_nodes}.
        :param target_low_priority_nodes: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#target_low_priority_nodes BatchPool#target_low_priority_nodes}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolFixedScale.__init__)
            check_type(argname="argument node_deallocation_method", value=node_deallocation_method, expected_type=type_hints["node_deallocation_method"])
            check_type(argname="argument resize_timeout", value=resize_timeout, expected_type=type_hints["resize_timeout"])
            check_type(argname="argument target_dedicated_nodes", value=target_dedicated_nodes, expected_type=type_hints["target_dedicated_nodes"])
            check_type(argname="argument target_low_priority_nodes", value=target_low_priority_nodes, expected_type=type_hints["target_low_priority_nodes"])
        self._values: typing.Dict[str, typing.Any] = {}
        if node_deallocation_method is not None:
            self._values["node_deallocation_method"] = node_deallocation_method
        if resize_timeout is not None:
            self._values["resize_timeout"] = resize_timeout
        if target_dedicated_nodes is not None:
            self._values["target_dedicated_nodes"] = target_dedicated_nodes
        if target_low_priority_nodes is not None:
            self._values["target_low_priority_nodes"] = target_low_priority_nodes

    @builtins.property
    def node_deallocation_method(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#node_deallocation_method BatchPool#node_deallocation_method}.'''
        result = self._values.get("node_deallocation_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resize_timeout(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#resize_timeout BatchPool#resize_timeout}.'''
        result = self._values.get("resize_timeout")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target_dedicated_nodes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#target_dedicated_nodes BatchPool#target_dedicated_nodes}.'''
        result = self._values.get("target_dedicated_nodes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target_low_priority_nodes(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#target_low_priority_nodes BatchPool#target_low_priority_nodes}.'''
        result = self._values.get("target_low_priority_nodes")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchPoolFixedScale(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BatchPoolFixedScaleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolFixedScaleOutputReference",
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
            type_hints = typing.get_type_hints(BatchPoolFixedScaleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetNodeDeallocationMethod")
    def reset_node_deallocation_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeDeallocationMethod", []))

    @jsii.member(jsii_name="resetResizeTimeout")
    def reset_resize_timeout(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResizeTimeout", []))

    @jsii.member(jsii_name="resetTargetDedicatedNodes")
    def reset_target_dedicated_nodes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetDedicatedNodes", []))

    @jsii.member(jsii_name="resetTargetLowPriorityNodes")
    def reset_target_low_priority_nodes(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetLowPriorityNodes", []))

    @builtins.property
    @jsii.member(jsii_name="nodeDeallocationMethodInput")
    def node_deallocation_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nodeDeallocationMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="resizeTimeoutInput")
    def resize_timeout_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resizeTimeoutInput"))

    @builtins.property
    @jsii.member(jsii_name="targetDedicatedNodesInput")
    def target_dedicated_nodes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetDedicatedNodesInput"))

    @builtins.property
    @jsii.member(jsii_name="targetLowPriorityNodesInput")
    def target_low_priority_nodes_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "targetLowPriorityNodesInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeDeallocationMethod")
    def node_deallocation_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nodeDeallocationMethod"))

    @node_deallocation_method.setter
    def node_deallocation_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolFixedScaleOutputReference, "node_deallocation_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeDeallocationMethod", value)

    @builtins.property
    @jsii.member(jsii_name="resizeTimeout")
    def resize_timeout(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resizeTimeout"))

    @resize_timeout.setter
    def resize_timeout(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolFixedScaleOutputReference, "resize_timeout").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resizeTimeout", value)

    @builtins.property
    @jsii.member(jsii_name="targetDedicatedNodes")
    def target_dedicated_nodes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetDedicatedNodes"))

    @target_dedicated_nodes.setter
    def target_dedicated_nodes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolFixedScaleOutputReference, "target_dedicated_nodes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetDedicatedNodes", value)

    @builtins.property
    @jsii.member(jsii_name="targetLowPriorityNodes")
    def target_low_priority_nodes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "targetLowPriorityNodes"))

    @target_low_priority_nodes.setter
    def target_low_priority_nodes(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolFixedScaleOutputReference, "target_low_priority_nodes").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetLowPriorityNodes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[BatchPoolFixedScale]:
        return typing.cast(typing.Optional[BatchPoolFixedScale], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[BatchPoolFixedScale]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolFixedScaleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolIdentity",
    jsii_struct_bases=[],
    name_mapping={"identity_ids": "identityIds", "type": "type"},
)
class BatchPoolIdentity:
    def __init__(
        self,
        *,
        identity_ids: typing.Sequence[builtins.str],
        type: builtins.str,
    ) -> None:
        '''
        :param identity_ids: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#identity_ids BatchPool#identity_ids}.
        :param type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#type BatchPool#type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolIdentity.__init__)
            check_type(argname="argument identity_ids", value=identity_ids, expected_type=type_hints["identity_ids"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[str, typing.Any] = {
            "identity_ids": identity_ids,
            "type": type,
        }

    @builtins.property
    def identity_ids(self) -> typing.List[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#identity_ids BatchPool#identity_ids}.'''
        result = self._values.get("identity_ids")
        assert result is not None, "Required property 'identity_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def type(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#type BatchPool#type}.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchPoolIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BatchPoolIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolIdentityOutputReference",
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
            type_hints = typing.get_type_hints(BatchPoolIdentityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="identityIdsInput")
    def identity_ids_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "identityIdsInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="identityIds")
    def identity_ids(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "identityIds"))

    @identity_ids.setter
    def identity_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolIdentityOutputReference, "identity_ids").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityIds", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolIdentityOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[BatchPoolIdentity]:
        return typing.cast(typing.Optional[BatchPoolIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[BatchPoolIdentity]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolMount",
    jsii_struct_bases=[],
    name_mapping={
        "azure_blob_file_system": "azureBlobFileSystem",
        "azure_file_share": "azureFileShare",
        "cifs_mount": "cifsMount",
        "nfs_mount": "nfsMount",
    },
)
class BatchPoolMount:
    def __init__(
        self,
        *,
        azure_blob_file_system: typing.Optional[typing.Union["BatchPoolMountAzureBlobFileSystem", typing.Dict[str, typing.Any]]] = None,
        azure_file_share: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolMountAzureFileShare", typing.Dict[str, typing.Any]]]]] = None,
        cifs_mount: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolMountCifsMount", typing.Dict[str, typing.Any]]]]] = None,
        nfs_mount: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolMountNfsMount", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param azure_blob_file_system: azure_blob_file_system block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#azure_blob_file_system BatchPool#azure_blob_file_system}
        :param azure_file_share: azure_file_share block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#azure_file_share BatchPool#azure_file_share}
        :param cifs_mount: cifs_mount block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#cifs_mount BatchPool#cifs_mount}
        :param nfs_mount: nfs_mount block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#nfs_mount BatchPool#nfs_mount}
        '''
        if isinstance(azure_blob_file_system, dict):
            azure_blob_file_system = BatchPoolMountAzureBlobFileSystem(**azure_blob_file_system)
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolMount.__init__)
            check_type(argname="argument azure_blob_file_system", value=azure_blob_file_system, expected_type=type_hints["azure_blob_file_system"])
            check_type(argname="argument azure_file_share", value=azure_file_share, expected_type=type_hints["azure_file_share"])
            check_type(argname="argument cifs_mount", value=cifs_mount, expected_type=type_hints["cifs_mount"])
            check_type(argname="argument nfs_mount", value=nfs_mount, expected_type=type_hints["nfs_mount"])
        self._values: typing.Dict[str, typing.Any] = {}
        if azure_blob_file_system is not None:
            self._values["azure_blob_file_system"] = azure_blob_file_system
        if azure_file_share is not None:
            self._values["azure_file_share"] = azure_file_share
        if cifs_mount is not None:
            self._values["cifs_mount"] = cifs_mount
        if nfs_mount is not None:
            self._values["nfs_mount"] = nfs_mount

    @builtins.property
    def azure_blob_file_system(
        self,
    ) -> typing.Optional["BatchPoolMountAzureBlobFileSystem"]:
        '''azure_blob_file_system block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#azure_blob_file_system BatchPool#azure_blob_file_system}
        '''
        result = self._values.get("azure_blob_file_system")
        return typing.cast(typing.Optional["BatchPoolMountAzureBlobFileSystem"], result)

    @builtins.property
    def azure_file_share(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolMountAzureFileShare"]]]:
        '''azure_file_share block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#azure_file_share BatchPool#azure_file_share}
        '''
        result = self._values.get("azure_file_share")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolMountAzureFileShare"]]], result)

    @builtins.property
    def cifs_mount(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolMountCifsMount"]]]:
        '''cifs_mount block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#cifs_mount BatchPool#cifs_mount}
        '''
        result = self._values.get("cifs_mount")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolMountCifsMount"]]], result)

    @builtins.property
    def nfs_mount(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolMountNfsMount"]]]:
        '''nfs_mount block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#nfs_mount BatchPool#nfs_mount}
        '''
        result = self._values.get("nfs_mount")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolMountNfsMount"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchPoolMount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolMountAzureBlobFileSystem",
    jsii_struct_bases=[],
    name_mapping={
        "account_name": "accountName",
        "container_name": "containerName",
        "relative_mount_path": "relativeMountPath",
        "account_key": "accountKey",
        "blobfuse_options": "blobfuseOptions",
        "identity_id": "identityId",
        "sas_key": "sasKey",
    },
)
class BatchPoolMountAzureBlobFileSystem:
    def __init__(
        self,
        *,
        account_name: builtins.str,
        container_name: builtins.str,
        relative_mount_path: builtins.str,
        account_key: typing.Optional[builtins.str] = None,
        blobfuse_options: typing.Optional[builtins.str] = None,
        identity_id: typing.Optional[builtins.str] = None,
        sas_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#account_name BatchPool#account_name}.
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#container_name BatchPool#container_name}.
        :param relative_mount_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#relative_mount_path BatchPool#relative_mount_path}.
        :param account_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#account_key BatchPool#account_key}.
        :param blobfuse_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#blobfuse_options BatchPool#blobfuse_options}.
        :param identity_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#identity_id BatchPool#identity_id}.
        :param sas_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#sas_key BatchPool#sas_key}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolMountAzureBlobFileSystem.__init__)
            check_type(argname="argument account_name", value=account_name, expected_type=type_hints["account_name"])
            check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
            check_type(argname="argument relative_mount_path", value=relative_mount_path, expected_type=type_hints["relative_mount_path"])
            check_type(argname="argument account_key", value=account_key, expected_type=type_hints["account_key"])
            check_type(argname="argument blobfuse_options", value=blobfuse_options, expected_type=type_hints["blobfuse_options"])
            check_type(argname="argument identity_id", value=identity_id, expected_type=type_hints["identity_id"])
            check_type(argname="argument sas_key", value=sas_key, expected_type=type_hints["sas_key"])
        self._values: typing.Dict[str, typing.Any] = {
            "account_name": account_name,
            "container_name": container_name,
            "relative_mount_path": relative_mount_path,
        }
        if account_key is not None:
            self._values["account_key"] = account_key
        if blobfuse_options is not None:
            self._values["blobfuse_options"] = blobfuse_options
        if identity_id is not None:
            self._values["identity_id"] = identity_id
        if sas_key is not None:
            self._values["sas_key"] = sas_key

    @builtins.property
    def account_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#account_name BatchPool#account_name}.'''
        result = self._values.get("account_name")
        assert result is not None, "Required property 'account_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def container_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#container_name BatchPool#container_name}.'''
        result = self._values.get("container_name")
        assert result is not None, "Required property 'container_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def relative_mount_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#relative_mount_path BatchPool#relative_mount_path}.'''
        result = self._values.get("relative_mount_path")
        assert result is not None, "Required property 'relative_mount_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#account_key BatchPool#account_key}.'''
        result = self._values.get("account_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def blobfuse_options(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#blobfuse_options BatchPool#blobfuse_options}.'''
        result = self._values.get("blobfuse_options")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#identity_id BatchPool#identity_id}.'''
        result = self._values.get("identity_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sas_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#sas_key BatchPool#sas_key}.'''
        result = self._values.get("sas_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchPoolMountAzureBlobFileSystem(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BatchPoolMountAzureBlobFileSystemOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolMountAzureBlobFileSystemOutputReference",
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
            type_hints = typing.get_type_hints(BatchPoolMountAzureBlobFileSystemOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAccountKey")
    def reset_account_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAccountKey", []))

    @jsii.member(jsii_name="resetBlobfuseOptions")
    def reset_blobfuse_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlobfuseOptions", []))

    @jsii.member(jsii_name="resetIdentityId")
    def reset_identity_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIdentityId", []))

    @jsii.member(jsii_name="resetSasKey")
    def reset_sas_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSasKey", []))

    @builtins.property
    @jsii.member(jsii_name="accountKeyInput")
    def account_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="accountNameInput")
    def account_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountNameInput"))

    @builtins.property
    @jsii.member(jsii_name="blobfuseOptionsInput")
    def blobfuse_options_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "blobfuseOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="containerNameInput")
    def container_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "containerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="identityIdInput")
    def identity_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityIdInput"))

    @builtins.property
    @jsii.member(jsii_name="relativeMountPathInput")
    def relative_mount_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "relativeMountPathInput"))

    @builtins.property
    @jsii.member(jsii_name="sasKeyInput")
    def sas_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sasKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="accountKey")
    def account_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountKey"))

    @account_key.setter
    def account_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolMountAzureBlobFileSystemOutputReference, "account_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountKey", value)

    @builtins.property
    @jsii.member(jsii_name="accountName")
    def account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountName"))

    @account_name.setter
    def account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolMountAzureBlobFileSystemOutputReference, "account_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountName", value)

    @builtins.property
    @jsii.member(jsii_name="blobfuseOptions")
    def blobfuse_options(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "blobfuseOptions"))

    @blobfuse_options.setter
    def blobfuse_options(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolMountAzureBlobFileSystemOutputReference, "blobfuse_options").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blobfuseOptions", value)

    @builtins.property
    @jsii.member(jsii_name="containerName")
    def container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "containerName"))

    @container_name.setter
    def container_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolMountAzureBlobFileSystemOutputReference, "container_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerName", value)

    @builtins.property
    @jsii.member(jsii_name="identityId")
    def identity_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "identityId"))

    @identity_id.setter
    def identity_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolMountAzureBlobFileSystemOutputReference, "identity_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityId", value)

    @builtins.property
    @jsii.member(jsii_name="relativeMountPath")
    def relative_mount_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "relativeMountPath"))

    @relative_mount_path.setter
    def relative_mount_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolMountAzureBlobFileSystemOutputReference, "relative_mount_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "relativeMountPath", value)

    @builtins.property
    @jsii.member(jsii_name="sasKey")
    def sas_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sasKey"))

    @sas_key.setter
    def sas_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolMountAzureBlobFileSystemOutputReference, "sas_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sasKey", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[BatchPoolMountAzureBlobFileSystem]:
        return typing.cast(typing.Optional[BatchPoolMountAzureBlobFileSystem], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BatchPoolMountAzureBlobFileSystem],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolMountAzureBlobFileSystemOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolMountAzureFileShare",
    jsii_struct_bases=[],
    name_mapping={
        "account_key": "accountKey",
        "account_name": "accountName",
        "azure_file_url": "azureFileUrl",
        "relative_mount_path": "relativeMountPath",
        "mount_options": "mountOptions",
    },
)
class BatchPoolMountAzureFileShare:
    def __init__(
        self,
        *,
        account_key: builtins.str,
        account_name: builtins.str,
        azure_file_url: builtins.str,
        relative_mount_path: builtins.str,
        mount_options: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param account_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#account_key BatchPool#account_key}.
        :param account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#account_name BatchPool#account_name}.
        :param azure_file_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#azure_file_url BatchPool#azure_file_url}.
        :param relative_mount_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#relative_mount_path BatchPool#relative_mount_path}.
        :param mount_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#mount_options BatchPool#mount_options}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolMountAzureFileShare.__init__)
            check_type(argname="argument account_key", value=account_key, expected_type=type_hints["account_key"])
            check_type(argname="argument account_name", value=account_name, expected_type=type_hints["account_name"])
            check_type(argname="argument azure_file_url", value=azure_file_url, expected_type=type_hints["azure_file_url"])
            check_type(argname="argument relative_mount_path", value=relative_mount_path, expected_type=type_hints["relative_mount_path"])
            check_type(argname="argument mount_options", value=mount_options, expected_type=type_hints["mount_options"])
        self._values: typing.Dict[str, typing.Any] = {
            "account_key": account_key,
            "account_name": account_name,
            "azure_file_url": azure_file_url,
            "relative_mount_path": relative_mount_path,
        }
        if mount_options is not None:
            self._values["mount_options"] = mount_options

    @builtins.property
    def account_key(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#account_key BatchPool#account_key}.'''
        result = self._values.get("account_key")
        assert result is not None, "Required property 'account_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#account_name BatchPool#account_name}.'''
        result = self._values.get("account_name")
        assert result is not None, "Required property 'account_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def azure_file_url(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#azure_file_url BatchPool#azure_file_url}.'''
        result = self._values.get("azure_file_url")
        assert result is not None, "Required property 'azure_file_url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def relative_mount_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#relative_mount_path BatchPool#relative_mount_path}.'''
        result = self._values.get("relative_mount_path")
        assert result is not None, "Required property 'relative_mount_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mount_options(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#mount_options BatchPool#mount_options}.'''
        result = self._values.get("mount_options")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchPoolMountAzureFileShare(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BatchPoolMountAzureFileShareList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolMountAzureFileShareList",
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
            type_hints = typing.get_type_hints(BatchPoolMountAzureFileShareList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "BatchPoolMountAzureFileShareOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolMountAzureFileShareList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BatchPoolMountAzureFileShareOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolMountAzureFileShareList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolMountAzureFileShareList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolMountAzureFileShareList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolMountAzureFileShare]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolMountAzureFileShare]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolMountAzureFileShare]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolMountAzureFileShareList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BatchPoolMountAzureFileShareOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolMountAzureFileShareOutputReference",
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
            type_hints = typing.get_type_hints(BatchPoolMountAzureFileShareOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMountOptions")
    def reset_mount_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMountOptions", []))

    @builtins.property
    @jsii.member(jsii_name="accountKeyInput")
    def account_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="accountNameInput")
    def account_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountNameInput"))

    @builtins.property
    @jsii.member(jsii_name="azureFileUrlInput")
    def azure_file_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "azureFileUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="mountOptionsInput")
    def mount_options_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mountOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="relativeMountPathInput")
    def relative_mount_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "relativeMountPathInput"))

    @builtins.property
    @jsii.member(jsii_name="accountKey")
    def account_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountKey"))

    @account_key.setter
    def account_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolMountAzureFileShareOutputReference, "account_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountKey", value)

    @builtins.property
    @jsii.member(jsii_name="accountName")
    def account_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "accountName"))

    @account_name.setter
    def account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolMountAzureFileShareOutputReference, "account_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountName", value)

    @builtins.property
    @jsii.member(jsii_name="azureFileUrl")
    def azure_file_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "azureFileUrl"))

    @azure_file_url.setter
    def azure_file_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolMountAzureFileShareOutputReference, "azure_file_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "azureFileUrl", value)

    @builtins.property
    @jsii.member(jsii_name="mountOptions")
    def mount_options(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mountOptions"))

    @mount_options.setter
    def mount_options(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolMountAzureFileShareOutputReference, "mount_options").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountOptions", value)

    @builtins.property
    @jsii.member(jsii_name="relativeMountPath")
    def relative_mount_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "relativeMountPath"))

    @relative_mount_path.setter
    def relative_mount_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolMountAzureFileShareOutputReference, "relative_mount_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "relativeMountPath", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BatchPoolMountAzureFileShare, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BatchPoolMountAzureFileShare, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BatchPoolMountAzureFileShare, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolMountAzureFileShareOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolMountCifsMount",
    jsii_struct_bases=[],
    name_mapping={
        "password": "password",
        "relative_mount_path": "relativeMountPath",
        "source": "source",
        "user_name": "userName",
        "mount_options": "mountOptions",
    },
)
class BatchPoolMountCifsMount:
    def __init__(
        self,
        *,
        password: builtins.str,
        relative_mount_path: builtins.str,
        source: builtins.str,
        user_name: builtins.str,
        mount_options: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#password BatchPool#password}.
        :param relative_mount_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#relative_mount_path BatchPool#relative_mount_path}.
        :param source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#source BatchPool#source}.
        :param user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#user_name BatchPool#user_name}.
        :param mount_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#mount_options BatchPool#mount_options}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolMountCifsMount.__init__)
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument relative_mount_path", value=relative_mount_path, expected_type=type_hints["relative_mount_path"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
            check_type(argname="argument mount_options", value=mount_options, expected_type=type_hints["mount_options"])
        self._values: typing.Dict[str, typing.Any] = {
            "password": password,
            "relative_mount_path": relative_mount_path,
            "source": source,
            "user_name": user_name,
        }
        if mount_options is not None:
            self._values["mount_options"] = mount_options

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#password BatchPool#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def relative_mount_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#relative_mount_path BatchPool#relative_mount_path}.'''
        result = self._values.get("relative_mount_path")
        assert result is not None, "Required property 'relative_mount_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#source BatchPool#source}.'''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#user_name BatchPool#user_name}.'''
        result = self._values.get("user_name")
        assert result is not None, "Required property 'user_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mount_options(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#mount_options BatchPool#mount_options}.'''
        result = self._values.get("mount_options")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchPoolMountCifsMount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BatchPoolMountCifsMountList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolMountCifsMountList",
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
            type_hints = typing.get_type_hints(BatchPoolMountCifsMountList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "BatchPoolMountCifsMountOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolMountCifsMountList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BatchPoolMountCifsMountOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolMountCifsMountList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolMountCifsMountList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolMountCifsMountList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolMountCifsMount]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolMountCifsMount]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolMountCifsMount]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolMountCifsMountList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BatchPoolMountCifsMountOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolMountCifsMountOutputReference",
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
            type_hints = typing.get_type_hints(BatchPoolMountCifsMountOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMountOptions")
    def reset_mount_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMountOptions", []))

    @builtins.property
    @jsii.member(jsii_name="mountOptionsInput")
    def mount_options_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mountOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="relativeMountPathInput")
    def relative_mount_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "relativeMountPathInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="userNameInput")
    def user_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userNameInput"))

    @builtins.property
    @jsii.member(jsii_name="mountOptions")
    def mount_options(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mountOptions"))

    @mount_options.setter
    def mount_options(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolMountCifsMountOutputReference, "mount_options").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountOptions", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolMountCifsMountOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="relativeMountPath")
    def relative_mount_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "relativeMountPath"))

    @relative_mount_path.setter
    def relative_mount_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolMountCifsMountOutputReference, "relative_mount_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "relativeMountPath", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolMountCifsMountOutputReference, "source").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="userName")
    def user_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userName"))

    @user_name.setter
    def user_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolMountCifsMountOutputReference, "user_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BatchPoolMountCifsMount, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BatchPoolMountCifsMount, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BatchPoolMountCifsMount, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolMountCifsMountOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BatchPoolMountList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolMountList",
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
            type_hints = typing.get_type_hints(BatchPoolMountList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "BatchPoolMountOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolMountList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BatchPoolMountOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolMountList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolMountList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolMountList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolMount]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolMount]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolMount]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolMountList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolMountNfsMount",
    jsii_struct_bases=[],
    name_mapping={
        "relative_mount_path": "relativeMountPath",
        "source": "source",
        "mount_options": "mountOptions",
    },
)
class BatchPoolMountNfsMount:
    def __init__(
        self,
        *,
        relative_mount_path: builtins.str,
        source: builtins.str,
        mount_options: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param relative_mount_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#relative_mount_path BatchPool#relative_mount_path}.
        :param source: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#source BatchPool#source}.
        :param mount_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#mount_options BatchPool#mount_options}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolMountNfsMount.__init__)
            check_type(argname="argument relative_mount_path", value=relative_mount_path, expected_type=type_hints["relative_mount_path"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument mount_options", value=mount_options, expected_type=type_hints["mount_options"])
        self._values: typing.Dict[str, typing.Any] = {
            "relative_mount_path": relative_mount_path,
            "source": source,
        }
        if mount_options is not None:
            self._values["mount_options"] = mount_options

    @builtins.property
    def relative_mount_path(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#relative_mount_path BatchPool#relative_mount_path}.'''
        result = self._values.get("relative_mount_path")
        assert result is not None, "Required property 'relative_mount_path' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#source BatchPool#source}.'''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def mount_options(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#mount_options BatchPool#mount_options}.'''
        result = self._values.get("mount_options")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchPoolMountNfsMount(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BatchPoolMountNfsMountList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolMountNfsMountList",
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
            type_hints = typing.get_type_hints(BatchPoolMountNfsMountList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "BatchPoolMountNfsMountOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolMountNfsMountList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BatchPoolMountNfsMountOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolMountNfsMountList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolMountNfsMountList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolMountNfsMountList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolMountNfsMount]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolMountNfsMount]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolMountNfsMount]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolMountNfsMountList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BatchPoolMountNfsMountOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolMountNfsMountOutputReference",
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
            type_hints = typing.get_type_hints(BatchPoolMountNfsMountOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMountOptions")
    def reset_mount_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMountOptions", []))

    @builtins.property
    @jsii.member(jsii_name="mountOptionsInput")
    def mount_options_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mountOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="relativeMountPathInput")
    def relative_mount_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "relativeMountPathInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceInput")
    def source_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceInput"))

    @builtins.property
    @jsii.member(jsii_name="mountOptions")
    def mount_options(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mountOptions"))

    @mount_options.setter
    def mount_options(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolMountNfsMountOutputReference, "mount_options").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mountOptions", value)

    @builtins.property
    @jsii.member(jsii_name="relativeMountPath")
    def relative_mount_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "relativeMountPath"))

    @relative_mount_path.setter
    def relative_mount_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolMountNfsMountOutputReference, "relative_mount_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "relativeMountPath", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "source"))

    @source.setter
    def source(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolMountNfsMountOutputReference, "source").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BatchPoolMountNfsMount, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BatchPoolMountNfsMount, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BatchPoolMountNfsMount, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolMountNfsMountOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BatchPoolMountOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolMountOutputReference",
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
            type_hints = typing.get_type_hints(BatchPoolMountOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAzureBlobFileSystem")
    def put_azure_blob_file_system(
        self,
        *,
        account_name: builtins.str,
        container_name: builtins.str,
        relative_mount_path: builtins.str,
        account_key: typing.Optional[builtins.str] = None,
        blobfuse_options: typing.Optional[builtins.str] = None,
        identity_id: typing.Optional[builtins.str] = None,
        sas_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param account_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#account_name BatchPool#account_name}.
        :param container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#container_name BatchPool#container_name}.
        :param relative_mount_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#relative_mount_path BatchPool#relative_mount_path}.
        :param account_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#account_key BatchPool#account_key}.
        :param blobfuse_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#blobfuse_options BatchPool#blobfuse_options}.
        :param identity_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#identity_id BatchPool#identity_id}.
        :param sas_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#sas_key BatchPool#sas_key}.
        '''
        value = BatchPoolMountAzureBlobFileSystem(
            account_name=account_name,
            container_name=container_name,
            relative_mount_path=relative_mount_path,
            account_key=account_key,
            blobfuse_options=blobfuse_options,
            identity_id=identity_id,
            sas_key=sas_key,
        )

        return typing.cast(None, jsii.invoke(self, "putAzureBlobFileSystem", [value]))

    @jsii.member(jsii_name="putAzureFileShare")
    def put_azure_file_share(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[BatchPoolMountAzureFileShare, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolMountOutputReference.put_azure_file_share)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAzureFileShare", [value]))

    @jsii.member(jsii_name="putCifsMount")
    def put_cifs_mount(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[BatchPoolMountCifsMount, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolMountOutputReference.put_cifs_mount)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCifsMount", [value]))

    @jsii.member(jsii_name="putNfsMount")
    def put_nfs_mount(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[BatchPoolMountNfsMount, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolMountOutputReference.put_nfs_mount)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNfsMount", [value]))

    @jsii.member(jsii_name="resetAzureBlobFileSystem")
    def reset_azure_blob_file_system(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureBlobFileSystem", []))

    @jsii.member(jsii_name="resetAzureFileShare")
    def reset_azure_file_share(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAzureFileShare", []))

    @jsii.member(jsii_name="resetCifsMount")
    def reset_cifs_mount(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCifsMount", []))

    @jsii.member(jsii_name="resetNfsMount")
    def reset_nfs_mount(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNfsMount", []))

    @builtins.property
    @jsii.member(jsii_name="azureBlobFileSystem")
    def azure_blob_file_system(
        self,
    ) -> BatchPoolMountAzureBlobFileSystemOutputReference:
        return typing.cast(BatchPoolMountAzureBlobFileSystemOutputReference, jsii.get(self, "azureBlobFileSystem"))

    @builtins.property
    @jsii.member(jsii_name="azureFileShare")
    def azure_file_share(self) -> BatchPoolMountAzureFileShareList:
        return typing.cast(BatchPoolMountAzureFileShareList, jsii.get(self, "azureFileShare"))

    @builtins.property
    @jsii.member(jsii_name="cifsMount")
    def cifs_mount(self) -> BatchPoolMountCifsMountList:
        return typing.cast(BatchPoolMountCifsMountList, jsii.get(self, "cifsMount"))

    @builtins.property
    @jsii.member(jsii_name="nfsMount")
    def nfs_mount(self) -> BatchPoolMountNfsMountList:
        return typing.cast(BatchPoolMountNfsMountList, jsii.get(self, "nfsMount"))

    @builtins.property
    @jsii.member(jsii_name="azureBlobFileSystemInput")
    def azure_blob_file_system_input(
        self,
    ) -> typing.Optional[BatchPoolMountAzureBlobFileSystem]:
        return typing.cast(typing.Optional[BatchPoolMountAzureBlobFileSystem], jsii.get(self, "azureBlobFileSystemInput"))

    @builtins.property
    @jsii.member(jsii_name="azureFileShareInput")
    def azure_file_share_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolMountAzureFileShare]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolMountAzureFileShare]]], jsii.get(self, "azureFileShareInput"))

    @builtins.property
    @jsii.member(jsii_name="cifsMountInput")
    def cifs_mount_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolMountCifsMount]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolMountCifsMount]]], jsii.get(self, "cifsMountInput"))

    @builtins.property
    @jsii.member(jsii_name="nfsMountInput")
    def nfs_mount_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolMountNfsMount]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolMountNfsMount]]], jsii.get(self, "nfsMountInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BatchPoolMount, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BatchPoolMount, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BatchPoolMount, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolMountOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolNetworkConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "subnet_id": "subnetId",
        "dynamic_vnet_assignment_scope": "dynamicVnetAssignmentScope",
        "endpoint_configuration": "endpointConfiguration",
        "public_address_provisioning_type": "publicAddressProvisioningType",
        "public_ips": "publicIps",
    },
)
class BatchPoolNetworkConfiguration:
    def __init__(
        self,
        *,
        subnet_id: builtins.str,
        dynamic_vnet_assignment_scope: typing.Optional[builtins.str] = None,
        endpoint_configuration: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolNetworkConfigurationEndpointConfiguration", typing.Dict[str, typing.Any]]]]] = None,
        public_address_provisioning_type: typing.Optional[builtins.str] = None,
        public_ips: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param subnet_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#subnet_id BatchPool#subnet_id}.
        :param dynamic_vnet_assignment_scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#dynamic_vnet_assignment_scope BatchPool#dynamic_vnet_assignment_scope}.
        :param endpoint_configuration: endpoint_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#endpoint_configuration BatchPool#endpoint_configuration}
        :param public_address_provisioning_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#public_address_provisioning_type BatchPool#public_address_provisioning_type}.
        :param public_ips: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#public_ips BatchPool#public_ips}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolNetworkConfiguration.__init__)
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
            check_type(argname="argument dynamic_vnet_assignment_scope", value=dynamic_vnet_assignment_scope, expected_type=type_hints["dynamic_vnet_assignment_scope"])
            check_type(argname="argument endpoint_configuration", value=endpoint_configuration, expected_type=type_hints["endpoint_configuration"])
            check_type(argname="argument public_address_provisioning_type", value=public_address_provisioning_type, expected_type=type_hints["public_address_provisioning_type"])
            check_type(argname="argument public_ips", value=public_ips, expected_type=type_hints["public_ips"])
        self._values: typing.Dict[str, typing.Any] = {
            "subnet_id": subnet_id,
        }
        if dynamic_vnet_assignment_scope is not None:
            self._values["dynamic_vnet_assignment_scope"] = dynamic_vnet_assignment_scope
        if endpoint_configuration is not None:
            self._values["endpoint_configuration"] = endpoint_configuration
        if public_address_provisioning_type is not None:
            self._values["public_address_provisioning_type"] = public_address_provisioning_type
        if public_ips is not None:
            self._values["public_ips"] = public_ips

    @builtins.property
    def subnet_id(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#subnet_id BatchPool#subnet_id}.'''
        result = self._values.get("subnet_id")
        assert result is not None, "Required property 'subnet_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dynamic_vnet_assignment_scope(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#dynamic_vnet_assignment_scope BatchPool#dynamic_vnet_assignment_scope}.'''
        result = self._values.get("dynamic_vnet_assignment_scope")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint_configuration(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolNetworkConfigurationEndpointConfiguration"]]]:
        '''endpoint_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#endpoint_configuration BatchPool#endpoint_configuration}
        '''
        result = self._values.get("endpoint_configuration")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolNetworkConfigurationEndpointConfiguration"]]], result)

    @builtins.property
    def public_address_provisioning_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#public_address_provisioning_type BatchPool#public_address_provisioning_type}.'''
        result = self._values.get("public_address_provisioning_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_ips(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#public_ips BatchPool#public_ips}.'''
        result = self._values.get("public_ips")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchPoolNetworkConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolNetworkConfigurationEndpointConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "backend_port": "backendPort",
        "frontend_port_range": "frontendPortRange",
        "name": "name",
        "protocol": "protocol",
        "network_security_group_rules": "networkSecurityGroupRules",
    },
)
class BatchPoolNetworkConfigurationEndpointConfiguration:
    def __init__(
        self,
        *,
        backend_port: jsii.Number,
        frontend_port_range: builtins.str,
        name: builtins.str,
        protocol: builtins.str,
        network_security_group_rules: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRules", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param backend_port: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#backend_port BatchPool#backend_port}.
        :param frontend_port_range: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#frontend_port_range BatchPool#frontend_port_range}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#name BatchPool#name}.
        :param protocol: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#protocol BatchPool#protocol}.
        :param network_security_group_rules: network_security_group_rules block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#network_security_group_rules BatchPool#network_security_group_rules}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolNetworkConfigurationEndpointConfiguration.__init__)
            check_type(argname="argument backend_port", value=backend_port, expected_type=type_hints["backend_port"])
            check_type(argname="argument frontend_port_range", value=frontend_port_range, expected_type=type_hints["frontend_port_range"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument network_security_group_rules", value=network_security_group_rules, expected_type=type_hints["network_security_group_rules"])
        self._values: typing.Dict[str, typing.Any] = {
            "backend_port": backend_port,
            "frontend_port_range": frontend_port_range,
            "name": name,
            "protocol": protocol,
        }
        if network_security_group_rules is not None:
            self._values["network_security_group_rules"] = network_security_group_rules

    @builtins.property
    def backend_port(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#backend_port BatchPool#backend_port}.'''
        result = self._values.get("backend_port")
        assert result is not None, "Required property 'backend_port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def frontend_port_range(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#frontend_port_range BatchPool#frontend_port_range}.'''
        result = self._values.get("frontend_port_range")
        assert result is not None, "Required property 'frontend_port_range' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#name BatchPool#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#protocol BatchPool#protocol}.'''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_security_group_rules(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRules"]]]:
        '''network_security_group_rules block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#network_security_group_rules BatchPool#network_security_group_rules}
        '''
        result = self._values.get("network_security_group_rules")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRules"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchPoolNetworkConfigurationEndpointConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BatchPoolNetworkConfigurationEndpointConfigurationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolNetworkConfigurationEndpointConfigurationList",
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
            type_hints = typing.get_type_hints(BatchPoolNetworkConfigurationEndpointConfigurationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "BatchPoolNetworkConfigurationEndpointConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolNetworkConfigurationEndpointConfigurationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BatchPoolNetworkConfigurationEndpointConfigurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolNetworkConfigurationEndpointConfigurationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolNetworkConfigurationEndpointConfigurationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolNetworkConfigurationEndpointConfigurationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolNetworkConfigurationEndpointConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolNetworkConfigurationEndpointConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolNetworkConfigurationEndpointConfiguration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolNetworkConfigurationEndpointConfigurationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRules",
    jsii_struct_bases=[],
    name_mapping={
        "access": "access",
        "priority": "priority",
        "source_address_prefix": "sourceAddressPrefix",
        "source_port_ranges": "sourcePortRanges",
    },
)
class BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRules:
    def __init__(
        self,
        *,
        access: builtins.str,
        priority: jsii.Number,
        source_address_prefix: builtins.str,
        source_port_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param access: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#access BatchPool#access}.
        :param priority: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#priority BatchPool#priority}.
        :param source_address_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#source_address_prefix BatchPool#source_address_prefix}.
        :param source_port_ranges: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#source_port_ranges BatchPool#source_port_ranges}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRules.__init__)
            check_type(argname="argument access", value=access, expected_type=type_hints["access"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument source_address_prefix", value=source_address_prefix, expected_type=type_hints["source_address_prefix"])
            check_type(argname="argument source_port_ranges", value=source_port_ranges, expected_type=type_hints["source_port_ranges"])
        self._values: typing.Dict[str, typing.Any] = {
            "access": access,
            "priority": priority,
            "source_address_prefix": source_address_prefix,
        }
        if source_port_ranges is not None:
            self._values["source_port_ranges"] = source_port_ranges

    @builtins.property
    def access(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#access BatchPool#access}.'''
        result = self._values.get("access")
        assert result is not None, "Required property 'access' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def priority(self) -> jsii.Number:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#priority BatchPool#priority}.'''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def source_address_prefix(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#source_address_prefix BatchPool#source_address_prefix}.'''
        result = self._values.get("source_address_prefix")
        assert result is not None, "Required property 'source_address_prefix' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_port_ranges(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#source_port_ranges BatchPool#source_port_ranges}.'''
        result = self._values.get("source_port_ranges")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRules(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRulesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRulesList",
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
            type_hints = typing.get_type_hints(BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRulesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRulesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRulesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRulesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRulesList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRulesList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRulesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRules]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRules]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRules]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRulesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRulesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRulesOutputReference",
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
            type_hints = typing.get_type_hints(BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRulesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetSourcePortRanges")
    def reset_source_port_ranges(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourcePortRanges", []))

    @builtins.property
    @jsii.member(jsii_name="accessInput")
    def access_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceAddressPrefixInput")
    def source_address_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceAddressPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="sourcePortRangesInput")
    def source_port_ranges_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourcePortRangesInput"))

    @builtins.property
    @jsii.member(jsii_name="access")
    def access(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "access"))

    @access.setter
    def access(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRulesOutputReference, "access").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "access", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRulesOutputReference, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="sourceAddressPrefix")
    def source_address_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceAddressPrefix"))

    @source_address_prefix.setter
    def source_address_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRulesOutputReference, "source_address_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceAddressPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="sourcePortRanges")
    def source_port_ranges(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourcePortRanges"))

    @source_port_ranges.setter
    def source_port_ranges(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRulesOutputReference, "source_port_ranges").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourcePortRanges", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRules, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRules, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRules, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRulesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BatchPoolNetworkConfigurationEndpointConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolNetworkConfigurationEndpointConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(BatchPoolNetworkConfigurationEndpointConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putNetworkSecurityGroupRules")
    def put_network_security_group_rules(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRules, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolNetworkConfigurationEndpointConfigurationOutputReference.put_network_security_group_rules)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNetworkSecurityGroupRules", [value]))

    @jsii.member(jsii_name="resetNetworkSecurityGroupRules")
    def reset_network_security_group_rules(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNetworkSecurityGroupRules", []))

    @builtins.property
    @jsii.member(jsii_name="networkSecurityGroupRules")
    def network_security_group_rules(
        self,
    ) -> BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRulesList:
        return typing.cast(BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRulesList, jsii.get(self, "networkSecurityGroupRules"))

    @builtins.property
    @jsii.member(jsii_name="backendPortInput")
    def backend_port_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "backendPortInput"))

    @builtins.property
    @jsii.member(jsii_name="frontendPortRangeInput")
    def frontend_port_range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "frontendPortRangeInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkSecurityGroupRulesInput")
    def network_security_group_rules_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRules]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRules]]], jsii.get(self, "networkSecurityGroupRulesInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="backendPort")
    def backend_port(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "backendPort"))

    @backend_port.setter
    def backend_port(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolNetworkConfigurationEndpointConfigurationOutputReference, "backend_port").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backendPort", value)

    @builtins.property
    @jsii.member(jsii_name="frontendPortRange")
    def frontend_port_range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "frontendPortRange"))

    @frontend_port_range.setter
    def frontend_port_range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolNetworkConfigurationEndpointConfigurationOutputReference, "frontend_port_range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "frontendPortRange", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolNetworkConfigurationEndpointConfigurationOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolNetworkConfigurationEndpointConfigurationOutputReference, "protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BatchPoolNetworkConfigurationEndpointConfiguration, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BatchPoolNetworkConfigurationEndpointConfiguration, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BatchPoolNetworkConfigurationEndpointConfiguration, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolNetworkConfigurationEndpointConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BatchPoolNetworkConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolNetworkConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(BatchPoolNetworkConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putEndpointConfiguration")
    def put_endpoint_configuration(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[BatchPoolNetworkConfigurationEndpointConfiguration, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolNetworkConfigurationOutputReference.put_endpoint_configuration)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putEndpointConfiguration", [value]))

    @jsii.member(jsii_name="resetDynamicVnetAssignmentScope")
    def reset_dynamic_vnet_assignment_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDynamicVnetAssignmentScope", []))

    @jsii.member(jsii_name="resetEndpointConfiguration")
    def reset_endpoint_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndpointConfiguration", []))

    @jsii.member(jsii_name="resetPublicAddressProvisioningType")
    def reset_public_address_provisioning_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicAddressProvisioningType", []))

    @jsii.member(jsii_name="resetPublicIps")
    def reset_public_ips(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicIps", []))

    @builtins.property
    @jsii.member(jsii_name="endpointConfiguration")
    def endpoint_configuration(
        self,
    ) -> BatchPoolNetworkConfigurationEndpointConfigurationList:
        return typing.cast(BatchPoolNetworkConfigurationEndpointConfigurationList, jsii.get(self, "endpointConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="dynamicVnetAssignmentScopeInput")
    def dynamic_vnet_assignment_scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dynamicVnetAssignmentScopeInput"))

    @builtins.property
    @jsii.member(jsii_name="endpointConfigurationInput")
    def endpoint_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolNetworkConfigurationEndpointConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolNetworkConfigurationEndpointConfiguration]]], jsii.get(self, "endpointConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="publicAddressProvisioningTypeInput")
    def public_address_provisioning_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicAddressProvisioningTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="publicIpsInput")
    def public_ips_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "publicIpsInput"))

    @builtins.property
    @jsii.member(jsii_name="subnetIdInput")
    def subnet_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="dynamicVnetAssignmentScope")
    def dynamic_vnet_assignment_scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dynamicVnetAssignmentScope"))

    @dynamic_vnet_assignment_scope.setter
    def dynamic_vnet_assignment_scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolNetworkConfigurationOutputReference, "dynamic_vnet_assignment_scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dynamicVnetAssignmentScope", value)

    @builtins.property
    @jsii.member(jsii_name="publicAddressProvisioningType")
    def public_address_provisioning_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicAddressProvisioningType"))

    @public_address_provisioning_type.setter
    def public_address_provisioning_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolNetworkConfigurationOutputReference, "public_address_provisioning_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicAddressProvisioningType", value)

    @builtins.property
    @jsii.member(jsii_name="publicIps")
    def public_ips(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "publicIps"))

    @public_ips.setter
    def public_ips(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolNetworkConfigurationOutputReference, "public_ips").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicIps", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolNetworkConfigurationOutputReference, "subnet_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[BatchPoolNetworkConfiguration]:
        return typing.cast(typing.Optional[BatchPoolNetworkConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BatchPoolNetworkConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolNetworkConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolNodePlacement",
    jsii_struct_bases=[],
    name_mapping={"policy": "policy"},
)
class BatchPoolNodePlacement:
    def __init__(self, *, policy: typing.Optional[builtins.str] = None) -> None:
        '''
        :param policy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#policy BatchPool#policy}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolNodePlacement.__init__)
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
        self._values: typing.Dict[str, typing.Any] = {}
        if policy is not None:
            self._values["policy"] = policy

    @builtins.property
    def policy(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#policy BatchPool#policy}.'''
        result = self._values.get("policy")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchPoolNodePlacement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BatchPoolNodePlacementList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolNodePlacementList",
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
            type_hints = typing.get_type_hints(BatchPoolNodePlacementList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "BatchPoolNodePlacementOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolNodePlacementList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BatchPoolNodePlacementOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolNodePlacementList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolNodePlacementList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolNodePlacementList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolNodePlacement]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolNodePlacement]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolNodePlacement]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolNodePlacementList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BatchPoolNodePlacementOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolNodePlacementOutputReference",
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
            type_hints = typing.get_type_hints(BatchPoolNodePlacementOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPolicy")
    def reset_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPolicy", []))

    @builtins.property
    @jsii.member(jsii_name="policyInput")
    def policy_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyInput"))

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "policy"))

    @policy.setter
    def policy(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolNodePlacementOutputReference, "policy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policy", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BatchPoolNodePlacement, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BatchPoolNodePlacement, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BatchPoolNodePlacement, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolNodePlacementOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolStartTask",
    jsii_struct_bases=[],
    name_mapping={
        "command_line": "commandLine",
        "user_identity": "userIdentity",
        "common_environment_properties": "commonEnvironmentProperties",
        "container": "container",
        "resource_file": "resourceFile",
        "task_retry_maximum": "taskRetryMaximum",
        "wait_for_success": "waitForSuccess",
    },
)
class BatchPoolStartTask:
    def __init__(
        self,
        *,
        command_line: builtins.str,
        user_identity: typing.Union["BatchPoolStartTaskUserIdentity", typing.Dict[str, typing.Any]],
        common_environment_properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        container: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolStartTaskContainer", typing.Dict[str, typing.Any]]]]] = None,
        resource_file: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolStartTaskResourceFile", typing.Dict[str, typing.Any]]]]] = None,
        task_retry_maximum: typing.Optional[jsii.Number] = None,
        wait_for_success: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param command_line: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#command_line BatchPool#command_line}.
        :param user_identity: user_identity block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#user_identity BatchPool#user_identity}
        :param common_environment_properties: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#common_environment_properties BatchPool#common_environment_properties}.
        :param container: container block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#container BatchPool#container}
        :param resource_file: resource_file block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#resource_file BatchPool#resource_file}
        :param task_retry_maximum: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#task_retry_maximum BatchPool#task_retry_maximum}.
        :param wait_for_success: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#wait_for_success BatchPool#wait_for_success}.
        '''
        if isinstance(user_identity, dict):
            user_identity = BatchPoolStartTaskUserIdentity(**user_identity)
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolStartTask.__init__)
            check_type(argname="argument command_line", value=command_line, expected_type=type_hints["command_line"])
            check_type(argname="argument user_identity", value=user_identity, expected_type=type_hints["user_identity"])
            check_type(argname="argument common_environment_properties", value=common_environment_properties, expected_type=type_hints["common_environment_properties"])
            check_type(argname="argument container", value=container, expected_type=type_hints["container"])
            check_type(argname="argument resource_file", value=resource_file, expected_type=type_hints["resource_file"])
            check_type(argname="argument task_retry_maximum", value=task_retry_maximum, expected_type=type_hints["task_retry_maximum"])
            check_type(argname="argument wait_for_success", value=wait_for_success, expected_type=type_hints["wait_for_success"])
        self._values: typing.Dict[str, typing.Any] = {
            "command_line": command_line,
            "user_identity": user_identity,
        }
        if common_environment_properties is not None:
            self._values["common_environment_properties"] = common_environment_properties
        if container is not None:
            self._values["container"] = container
        if resource_file is not None:
            self._values["resource_file"] = resource_file
        if task_retry_maximum is not None:
            self._values["task_retry_maximum"] = task_retry_maximum
        if wait_for_success is not None:
            self._values["wait_for_success"] = wait_for_success

    @builtins.property
    def command_line(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#command_line BatchPool#command_line}.'''
        result = self._values.get("command_line")
        assert result is not None, "Required property 'command_line' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_identity(self) -> "BatchPoolStartTaskUserIdentity":
        '''user_identity block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#user_identity BatchPool#user_identity}
        '''
        result = self._values.get("user_identity")
        assert result is not None, "Required property 'user_identity' is missing"
        return typing.cast("BatchPoolStartTaskUserIdentity", result)

    @builtins.property
    def common_environment_properties(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#common_environment_properties BatchPool#common_environment_properties}.'''
        result = self._values.get("common_environment_properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def container(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolStartTaskContainer"]]]:
        '''container block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#container BatchPool#container}
        '''
        result = self._values.get("container")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolStartTaskContainer"]]], result)

    @builtins.property
    def resource_file(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolStartTaskResourceFile"]]]:
        '''resource_file block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#resource_file BatchPool#resource_file}
        '''
        result = self._values.get("resource_file")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolStartTaskResourceFile"]]], result)

    @builtins.property
    def task_retry_maximum(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#task_retry_maximum BatchPool#task_retry_maximum}.'''
        result = self._values.get("task_retry_maximum")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def wait_for_success(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#wait_for_success BatchPool#wait_for_success}.'''
        result = self._values.get("wait_for_success")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchPoolStartTask(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolStartTaskContainer",
    jsii_struct_bases=[],
    name_mapping={
        "image_name": "imageName",
        "registry": "registry",
        "run_options": "runOptions",
        "working_directory": "workingDirectory",
    },
)
class BatchPoolStartTaskContainer:
    def __init__(
        self,
        *,
        image_name: builtins.str,
        registry: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolStartTaskContainerRegistry", typing.Dict[str, typing.Any]]]]] = None,
        run_options: typing.Optional[builtins.str] = None,
        working_directory: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param image_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#image_name BatchPool#image_name}.
        :param registry: registry block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#registry BatchPool#registry}
        :param run_options: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#run_options BatchPool#run_options}.
        :param working_directory: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#working_directory BatchPool#working_directory}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolStartTaskContainer.__init__)
            check_type(argname="argument image_name", value=image_name, expected_type=type_hints["image_name"])
            check_type(argname="argument registry", value=registry, expected_type=type_hints["registry"])
            check_type(argname="argument run_options", value=run_options, expected_type=type_hints["run_options"])
            check_type(argname="argument working_directory", value=working_directory, expected_type=type_hints["working_directory"])
        self._values: typing.Dict[str, typing.Any] = {
            "image_name": image_name,
        }
        if registry is not None:
            self._values["registry"] = registry
        if run_options is not None:
            self._values["run_options"] = run_options
        if working_directory is not None:
            self._values["working_directory"] = working_directory

    @builtins.property
    def image_name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#image_name BatchPool#image_name}.'''
        result = self._values.get("image_name")
        assert result is not None, "Required property 'image_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def registry(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolStartTaskContainerRegistry"]]]:
        '''registry block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#registry BatchPool#registry}
        '''
        result = self._values.get("registry")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolStartTaskContainerRegistry"]]], result)

    @builtins.property
    def run_options(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#run_options BatchPool#run_options}.'''
        result = self._values.get("run_options")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def working_directory(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#working_directory BatchPool#working_directory}.'''
        result = self._values.get("working_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchPoolStartTaskContainer(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BatchPoolStartTaskContainerList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolStartTaskContainerList",
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
            type_hints = typing.get_type_hints(BatchPoolStartTaskContainerList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "BatchPoolStartTaskContainerOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolStartTaskContainerList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BatchPoolStartTaskContainerOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskContainerList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskContainerList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskContainerList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolStartTaskContainer]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolStartTaskContainer]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolStartTaskContainer]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskContainerList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BatchPoolStartTaskContainerOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolStartTaskContainerOutputReference",
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
            type_hints = typing.get_type_hints(BatchPoolStartTaskContainerOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putRegistry")
    def put_registry(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolStartTaskContainerRegistry", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolStartTaskContainerOutputReference.put_registry)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putRegistry", [value]))

    @jsii.member(jsii_name="resetRegistry")
    def reset_registry(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegistry", []))

    @jsii.member(jsii_name="resetRunOptions")
    def reset_run_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRunOptions", []))

    @jsii.member(jsii_name="resetWorkingDirectory")
    def reset_working_directory(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWorkingDirectory", []))

    @builtins.property
    @jsii.member(jsii_name="registry")
    def registry(self) -> "BatchPoolStartTaskContainerRegistryList":
        return typing.cast("BatchPoolStartTaskContainerRegistryList", jsii.get(self, "registry"))

    @builtins.property
    @jsii.member(jsii_name="imageNameInput")
    def image_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageNameInput"))

    @builtins.property
    @jsii.member(jsii_name="registryInput")
    def registry_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolStartTaskContainerRegistry"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolStartTaskContainerRegistry"]]], jsii.get(self, "registryInput"))

    @builtins.property
    @jsii.member(jsii_name="runOptionsInput")
    def run_options_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="workingDirectoryInput")
    def working_directory_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "workingDirectoryInput"))

    @builtins.property
    @jsii.member(jsii_name="imageName")
    def image_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "imageName"))

    @image_name.setter
    def image_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskContainerOutputReference, "image_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageName", value)

    @builtins.property
    @jsii.member(jsii_name="runOptions")
    def run_options(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "runOptions"))

    @run_options.setter
    def run_options(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskContainerOutputReference, "run_options").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runOptions", value)

    @builtins.property
    @jsii.member(jsii_name="workingDirectory")
    def working_directory(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "workingDirectory"))

    @working_directory.setter
    def working_directory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskContainerOutputReference, "working_directory").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workingDirectory", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BatchPoolStartTaskContainer, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BatchPoolStartTaskContainer, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BatchPoolStartTaskContainer, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskContainerOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolStartTaskContainerRegistry",
    jsii_struct_bases=[],
    name_mapping={
        "registry_server": "registryServer",
        "password": "password",
        "user_assigned_identity_id": "userAssignedIdentityId",
        "user_name": "userName",
    },
)
class BatchPoolStartTaskContainerRegistry:
    def __init__(
        self,
        *,
        registry_server: builtins.str,
        password: typing.Optional[builtins.str] = None,
        user_assigned_identity_id: typing.Optional[builtins.str] = None,
        user_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param registry_server: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#registry_server BatchPool#registry_server}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#password BatchPool#password}.
        :param user_assigned_identity_id: The User Assigned Identity to use for Container Registry access. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#user_assigned_identity_id BatchPool#user_assigned_identity_id}
        :param user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#user_name BatchPool#user_name}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolStartTaskContainerRegistry.__init__)
            check_type(argname="argument registry_server", value=registry_server, expected_type=type_hints["registry_server"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument user_assigned_identity_id", value=user_assigned_identity_id, expected_type=type_hints["user_assigned_identity_id"])
            check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "registry_server": registry_server,
        }
        if password is not None:
            self._values["password"] = password
        if user_assigned_identity_id is not None:
            self._values["user_assigned_identity_id"] = user_assigned_identity_id
        if user_name is not None:
            self._values["user_name"] = user_name

    @builtins.property
    def registry_server(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#registry_server BatchPool#registry_server}.'''
        result = self._values.get("registry_server")
        assert result is not None, "Required property 'registry_server' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#password BatchPool#password}.'''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_assigned_identity_id(self) -> typing.Optional[builtins.str]:
        '''The User Assigned Identity to use for Container Registry access.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#user_assigned_identity_id BatchPool#user_assigned_identity_id}
        '''
        result = self._values.get("user_assigned_identity_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#user_name BatchPool#user_name}.'''
        result = self._values.get("user_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchPoolStartTaskContainerRegistry(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BatchPoolStartTaskContainerRegistryList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolStartTaskContainerRegistryList",
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
            type_hints = typing.get_type_hints(BatchPoolStartTaskContainerRegistryList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "BatchPoolStartTaskContainerRegistryOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolStartTaskContainerRegistryList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BatchPoolStartTaskContainerRegistryOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskContainerRegistryList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskContainerRegistryList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskContainerRegistryList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolStartTaskContainerRegistry]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolStartTaskContainerRegistry]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolStartTaskContainerRegistry]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskContainerRegistryList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BatchPoolStartTaskContainerRegistryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolStartTaskContainerRegistryOutputReference",
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
            type_hints = typing.get_type_hints(BatchPoolStartTaskContainerRegistryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetUserAssignedIdentityId")
    def reset_user_assigned_identity_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserAssignedIdentityId", []))

    @jsii.member(jsii_name="resetUserName")
    def reset_user_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserName", []))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="registryServerInput")
    def registry_server_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "registryServerInput"))

    @builtins.property
    @jsii.member(jsii_name="userAssignedIdentityIdInput")
    def user_assigned_identity_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userAssignedIdentityIdInput"))

    @builtins.property
    @jsii.member(jsii_name="userNameInput")
    def user_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userNameInput"))

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskContainerRegistryOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="registryServer")
    def registry_server(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "registryServer"))

    @registry_server.setter
    def registry_server(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskContainerRegistryOutputReference, "registry_server").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registryServer", value)

    @builtins.property
    @jsii.member(jsii_name="userAssignedIdentityId")
    def user_assigned_identity_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userAssignedIdentityId"))

    @user_assigned_identity_id.setter
    def user_assigned_identity_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskContainerRegistryOutputReference, "user_assigned_identity_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userAssignedIdentityId", value)

    @builtins.property
    @jsii.member(jsii_name="userName")
    def user_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userName"))

    @user_name.setter
    def user_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskContainerRegistryOutputReference, "user_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BatchPoolStartTaskContainerRegistry, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BatchPoolStartTaskContainerRegistry, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BatchPoolStartTaskContainerRegistry, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskContainerRegistryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BatchPoolStartTaskOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolStartTaskOutputReference",
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
            type_hints = typing.get_type_hints(BatchPoolStartTaskOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putContainer")
    def put_container(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[BatchPoolStartTaskContainer, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolStartTaskOutputReference.put_container)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putContainer", [value]))

    @jsii.member(jsii_name="putResourceFile")
    def put_resource_file(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolStartTaskResourceFile", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolStartTaskOutputReference.put_resource_file)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putResourceFile", [value]))

    @jsii.member(jsii_name="putUserIdentity")
    def put_user_identity(
        self,
        *,
        auto_user: typing.Optional[typing.Union["BatchPoolStartTaskUserIdentityAutoUser", typing.Dict[str, typing.Any]]] = None,
        user_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auto_user: auto_user block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#auto_user BatchPool#auto_user}
        :param user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#user_name BatchPool#user_name}.
        '''
        value = BatchPoolStartTaskUserIdentity(
            auto_user=auto_user, user_name=user_name
        )

        return typing.cast(None, jsii.invoke(self, "putUserIdentity", [value]))

    @jsii.member(jsii_name="resetCommonEnvironmentProperties")
    def reset_common_environment_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCommonEnvironmentProperties", []))

    @jsii.member(jsii_name="resetContainer")
    def reset_container(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContainer", []))

    @jsii.member(jsii_name="resetResourceFile")
    def reset_resource_file(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceFile", []))

    @jsii.member(jsii_name="resetTaskRetryMaximum")
    def reset_task_retry_maximum(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTaskRetryMaximum", []))

    @jsii.member(jsii_name="resetWaitForSuccess")
    def reset_wait_for_success(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWaitForSuccess", []))

    @builtins.property
    @jsii.member(jsii_name="container")
    def container(self) -> BatchPoolStartTaskContainerList:
        return typing.cast(BatchPoolStartTaskContainerList, jsii.get(self, "container"))

    @builtins.property
    @jsii.member(jsii_name="resourceFile")
    def resource_file(self) -> "BatchPoolStartTaskResourceFileList":
        return typing.cast("BatchPoolStartTaskResourceFileList", jsii.get(self, "resourceFile"))

    @builtins.property
    @jsii.member(jsii_name="userIdentity")
    def user_identity(self) -> "BatchPoolStartTaskUserIdentityOutputReference":
        return typing.cast("BatchPoolStartTaskUserIdentityOutputReference", jsii.get(self, "userIdentity"))

    @builtins.property
    @jsii.member(jsii_name="commandLineInput")
    def command_line_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "commandLineInput"))

    @builtins.property
    @jsii.member(jsii_name="commonEnvironmentPropertiesInput")
    def common_environment_properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "commonEnvironmentPropertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="containerInput")
    def container_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolStartTaskContainer]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolStartTaskContainer]]], jsii.get(self, "containerInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceFileInput")
    def resource_file_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolStartTaskResourceFile"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolStartTaskResourceFile"]]], jsii.get(self, "resourceFileInput"))

    @builtins.property
    @jsii.member(jsii_name="taskRetryMaximumInput")
    def task_retry_maximum_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "taskRetryMaximumInput"))

    @builtins.property
    @jsii.member(jsii_name="userIdentityInput")
    def user_identity_input(self) -> typing.Optional["BatchPoolStartTaskUserIdentity"]:
        return typing.cast(typing.Optional["BatchPoolStartTaskUserIdentity"], jsii.get(self, "userIdentityInput"))

    @builtins.property
    @jsii.member(jsii_name="waitForSuccessInput")
    def wait_for_success_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "waitForSuccessInput"))

    @builtins.property
    @jsii.member(jsii_name="commandLine")
    def command_line(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "commandLine"))

    @command_line.setter
    def command_line(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskOutputReference, "command_line").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commandLine", value)

    @builtins.property
    @jsii.member(jsii_name="commonEnvironmentProperties")
    def common_environment_properties(
        self,
    ) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "commonEnvironmentProperties"))

    @common_environment_properties.setter
    def common_environment_properties(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskOutputReference, "common_environment_properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "commonEnvironmentProperties", value)

    @builtins.property
    @jsii.member(jsii_name="taskRetryMaximum")
    def task_retry_maximum(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "taskRetryMaximum"))

    @task_retry_maximum.setter
    def task_retry_maximum(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskOutputReference, "task_retry_maximum").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskRetryMaximum", value)

    @builtins.property
    @jsii.member(jsii_name="waitForSuccess")
    def wait_for_success(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "waitForSuccess"))

    @wait_for_success.setter
    def wait_for_success(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskOutputReference, "wait_for_success").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "waitForSuccess", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[BatchPoolStartTask]:
        return typing.cast(typing.Optional[BatchPoolStartTask], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[BatchPoolStartTask]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolStartTaskResourceFile",
    jsii_struct_bases=[],
    name_mapping={
        "auto_storage_container_name": "autoStorageContainerName",
        "blob_prefix": "blobPrefix",
        "file_mode": "fileMode",
        "file_path": "filePath",
        "http_url": "httpUrl",
        "storage_container_url": "storageContainerUrl",
        "user_assigned_identity_id": "userAssignedIdentityId",
    },
)
class BatchPoolStartTaskResourceFile:
    def __init__(
        self,
        *,
        auto_storage_container_name: typing.Optional[builtins.str] = None,
        blob_prefix: typing.Optional[builtins.str] = None,
        file_mode: typing.Optional[builtins.str] = None,
        file_path: typing.Optional[builtins.str] = None,
        http_url: typing.Optional[builtins.str] = None,
        storage_container_url: typing.Optional[builtins.str] = None,
        user_assigned_identity_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auto_storage_container_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#auto_storage_container_name BatchPool#auto_storage_container_name}.
        :param blob_prefix: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#blob_prefix BatchPool#blob_prefix}.
        :param file_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#file_mode BatchPool#file_mode}.
        :param file_path: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#file_path BatchPool#file_path}.
        :param http_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#http_url BatchPool#http_url}.
        :param storage_container_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#storage_container_url BatchPool#storage_container_url}.
        :param user_assigned_identity_id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#user_assigned_identity_id BatchPool#user_assigned_identity_id}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolStartTaskResourceFile.__init__)
            check_type(argname="argument auto_storage_container_name", value=auto_storage_container_name, expected_type=type_hints["auto_storage_container_name"])
            check_type(argname="argument blob_prefix", value=blob_prefix, expected_type=type_hints["blob_prefix"])
            check_type(argname="argument file_mode", value=file_mode, expected_type=type_hints["file_mode"])
            check_type(argname="argument file_path", value=file_path, expected_type=type_hints["file_path"])
            check_type(argname="argument http_url", value=http_url, expected_type=type_hints["http_url"])
            check_type(argname="argument storage_container_url", value=storage_container_url, expected_type=type_hints["storage_container_url"])
            check_type(argname="argument user_assigned_identity_id", value=user_assigned_identity_id, expected_type=type_hints["user_assigned_identity_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if auto_storage_container_name is not None:
            self._values["auto_storage_container_name"] = auto_storage_container_name
        if blob_prefix is not None:
            self._values["blob_prefix"] = blob_prefix
        if file_mode is not None:
            self._values["file_mode"] = file_mode
        if file_path is not None:
            self._values["file_path"] = file_path
        if http_url is not None:
            self._values["http_url"] = http_url
        if storage_container_url is not None:
            self._values["storage_container_url"] = storage_container_url
        if user_assigned_identity_id is not None:
            self._values["user_assigned_identity_id"] = user_assigned_identity_id

    @builtins.property
    def auto_storage_container_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#auto_storage_container_name BatchPool#auto_storage_container_name}.'''
        result = self._values.get("auto_storage_container_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def blob_prefix(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#blob_prefix BatchPool#blob_prefix}.'''
        result = self._values.get("blob_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_mode(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#file_mode BatchPool#file_mode}.'''
        result = self._values.get("file_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def file_path(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#file_path BatchPool#file_path}.'''
        result = self._values.get("file_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#http_url BatchPool#http_url}.'''
        result = self._values.get("http_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_container_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#storage_container_url BatchPool#storage_container_url}.'''
        result = self._values.get("storage_container_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_assigned_identity_id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#user_assigned_identity_id BatchPool#user_assigned_identity_id}.'''
        result = self._values.get("user_assigned_identity_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchPoolStartTaskResourceFile(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BatchPoolStartTaskResourceFileList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolStartTaskResourceFileList",
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
            type_hints = typing.get_type_hints(BatchPoolStartTaskResourceFileList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "BatchPoolStartTaskResourceFileOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolStartTaskResourceFileList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BatchPoolStartTaskResourceFileOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskResourceFileList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskResourceFileList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskResourceFileList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolStartTaskResourceFile]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolStartTaskResourceFile]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolStartTaskResourceFile]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskResourceFileList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BatchPoolStartTaskResourceFileOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolStartTaskResourceFileOutputReference",
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
            type_hints = typing.get_type_hints(BatchPoolStartTaskResourceFileOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAutoStorageContainerName")
    def reset_auto_storage_container_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoStorageContainerName", []))

    @jsii.member(jsii_name="resetBlobPrefix")
    def reset_blob_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBlobPrefix", []))

    @jsii.member(jsii_name="resetFileMode")
    def reset_file_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileMode", []))

    @jsii.member(jsii_name="resetFilePath")
    def reset_file_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFilePath", []))

    @jsii.member(jsii_name="resetHttpUrl")
    def reset_http_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHttpUrl", []))

    @jsii.member(jsii_name="resetStorageContainerUrl")
    def reset_storage_container_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageContainerUrl", []))

    @jsii.member(jsii_name="resetUserAssignedIdentityId")
    def reset_user_assigned_identity_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserAssignedIdentityId", []))

    @builtins.property
    @jsii.member(jsii_name="autoStorageContainerNameInput")
    def auto_storage_container_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoStorageContainerNameInput"))

    @builtins.property
    @jsii.member(jsii_name="blobPrefixInput")
    def blob_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "blobPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="fileModeInput")
    def file_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fileModeInput"))

    @builtins.property
    @jsii.member(jsii_name="filePathInput")
    def file_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "filePathInput"))

    @builtins.property
    @jsii.member(jsii_name="httpUrlInput")
    def http_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "httpUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="storageContainerUrlInput")
    def storage_container_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageContainerUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="userAssignedIdentityIdInput")
    def user_assigned_identity_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userAssignedIdentityIdInput"))

    @builtins.property
    @jsii.member(jsii_name="autoStorageContainerName")
    def auto_storage_container_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "autoStorageContainerName"))

    @auto_storage_container_name.setter
    def auto_storage_container_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskResourceFileOutputReference, "auto_storage_container_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoStorageContainerName", value)

    @builtins.property
    @jsii.member(jsii_name="blobPrefix")
    def blob_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "blobPrefix"))

    @blob_prefix.setter
    def blob_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskResourceFileOutputReference, "blob_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blobPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="fileMode")
    def file_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fileMode"))

    @file_mode.setter
    def file_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskResourceFileOutputReference, "file_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileMode", value)

    @builtins.property
    @jsii.member(jsii_name="filePath")
    def file_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "filePath"))

    @file_path.setter
    def file_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskResourceFileOutputReference, "file_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filePath", value)

    @builtins.property
    @jsii.member(jsii_name="httpUrl")
    def http_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "httpUrl"))

    @http_url.setter
    def http_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskResourceFileOutputReference, "http_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpUrl", value)

    @builtins.property
    @jsii.member(jsii_name="storageContainerUrl")
    def storage_container_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageContainerUrl"))

    @storage_container_url.setter
    def storage_container_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskResourceFileOutputReference, "storage_container_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageContainerUrl", value)

    @builtins.property
    @jsii.member(jsii_name="userAssignedIdentityId")
    def user_assigned_identity_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userAssignedIdentityId"))

    @user_assigned_identity_id.setter
    def user_assigned_identity_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskResourceFileOutputReference, "user_assigned_identity_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userAssignedIdentityId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BatchPoolStartTaskResourceFile, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BatchPoolStartTaskResourceFile, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BatchPoolStartTaskResourceFile, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskResourceFileOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolStartTaskUserIdentity",
    jsii_struct_bases=[],
    name_mapping={"auto_user": "autoUser", "user_name": "userName"},
)
class BatchPoolStartTaskUserIdentity:
    def __init__(
        self,
        *,
        auto_user: typing.Optional[typing.Union["BatchPoolStartTaskUserIdentityAutoUser", typing.Dict[str, typing.Any]]] = None,
        user_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param auto_user: auto_user block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#auto_user BatchPool#auto_user}
        :param user_name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#user_name BatchPool#user_name}.
        '''
        if isinstance(auto_user, dict):
            auto_user = BatchPoolStartTaskUserIdentityAutoUser(**auto_user)
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolStartTaskUserIdentity.__init__)
            check_type(argname="argument auto_user", value=auto_user, expected_type=type_hints["auto_user"])
            check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
        self._values: typing.Dict[str, typing.Any] = {}
        if auto_user is not None:
            self._values["auto_user"] = auto_user
        if user_name is not None:
            self._values["user_name"] = user_name

    @builtins.property
    def auto_user(self) -> typing.Optional["BatchPoolStartTaskUserIdentityAutoUser"]:
        '''auto_user block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#auto_user BatchPool#auto_user}
        '''
        result = self._values.get("auto_user")
        return typing.cast(typing.Optional["BatchPoolStartTaskUserIdentityAutoUser"], result)

    @builtins.property
    def user_name(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#user_name BatchPool#user_name}.'''
        result = self._values.get("user_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchPoolStartTaskUserIdentity(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolStartTaskUserIdentityAutoUser",
    jsii_struct_bases=[],
    name_mapping={"elevation_level": "elevationLevel", "scope": "scope"},
)
class BatchPoolStartTaskUserIdentityAutoUser:
    def __init__(
        self,
        *,
        elevation_level: typing.Optional[builtins.str] = None,
        scope: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param elevation_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#elevation_level BatchPool#elevation_level}.
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#scope BatchPool#scope}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolStartTaskUserIdentityAutoUser.__init__)
            check_type(argname="argument elevation_level", value=elevation_level, expected_type=type_hints["elevation_level"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        self._values: typing.Dict[str, typing.Any] = {}
        if elevation_level is not None:
            self._values["elevation_level"] = elevation_level
        if scope is not None:
            self._values["scope"] = scope

    @builtins.property
    def elevation_level(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#elevation_level BatchPool#elevation_level}.'''
        result = self._values.get("elevation_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scope(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#scope BatchPool#scope}.'''
        result = self._values.get("scope")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchPoolStartTaskUserIdentityAutoUser(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BatchPoolStartTaskUserIdentityAutoUserOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolStartTaskUserIdentityAutoUserOutputReference",
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
            type_hints = typing.get_type_hints(BatchPoolStartTaskUserIdentityAutoUserOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetElevationLevel")
    def reset_elevation_level(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetElevationLevel", []))

    @jsii.member(jsii_name="resetScope")
    def reset_scope(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScope", []))

    @builtins.property
    @jsii.member(jsii_name="elevationLevelInput")
    def elevation_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "elevationLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="scopeInput")
    def scope_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scopeInput"))

    @builtins.property
    @jsii.member(jsii_name="elevationLevel")
    def elevation_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "elevationLevel"))

    @elevation_level.setter
    def elevation_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskUserIdentityAutoUserOutputReference, "elevation_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elevationLevel", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskUserIdentityAutoUserOutputReference, "scope").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[BatchPoolStartTaskUserIdentityAutoUser]:
        return typing.cast(typing.Optional[BatchPoolStartTaskUserIdentityAutoUser], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BatchPoolStartTaskUserIdentityAutoUser],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskUserIdentityAutoUserOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BatchPoolStartTaskUserIdentityOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolStartTaskUserIdentityOutputReference",
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
            type_hints = typing.get_type_hints(BatchPoolStartTaskUserIdentityOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putAutoUser")
    def put_auto_user(
        self,
        *,
        elevation_level: typing.Optional[builtins.str] = None,
        scope: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param elevation_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#elevation_level BatchPool#elevation_level}.
        :param scope: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#scope BatchPool#scope}.
        '''
        value = BatchPoolStartTaskUserIdentityAutoUser(
            elevation_level=elevation_level, scope=scope
        )

        return typing.cast(None, jsii.invoke(self, "putAutoUser", [value]))

    @jsii.member(jsii_name="resetAutoUser")
    def reset_auto_user(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutoUser", []))

    @jsii.member(jsii_name="resetUserName")
    def reset_user_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserName", []))

    @builtins.property
    @jsii.member(jsii_name="autoUser")
    def auto_user(self) -> BatchPoolStartTaskUserIdentityAutoUserOutputReference:
        return typing.cast(BatchPoolStartTaskUserIdentityAutoUserOutputReference, jsii.get(self, "autoUser"))

    @builtins.property
    @jsii.member(jsii_name="autoUserInput")
    def auto_user_input(
        self,
    ) -> typing.Optional[BatchPoolStartTaskUserIdentityAutoUser]:
        return typing.cast(typing.Optional[BatchPoolStartTaskUserIdentityAutoUser], jsii.get(self, "autoUserInput"))

    @builtins.property
    @jsii.member(jsii_name="userNameInput")
    def user_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userNameInput"))

    @builtins.property
    @jsii.member(jsii_name="userName")
    def user_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userName"))

    @user_name.setter
    def user_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskUserIdentityOutputReference, "user_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[BatchPoolStartTaskUserIdentity]:
        return typing.cast(typing.Optional[BatchPoolStartTaskUserIdentity], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BatchPoolStartTaskUserIdentity],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStartTaskUserIdentityOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolStorageImageReference",
    jsii_struct_bases=[],
    name_mapping={
        "id": "id",
        "offer": "offer",
        "publisher": "publisher",
        "sku": "sku",
        "version": "version",
    },
)
class BatchPoolStorageImageReference:
    def __init__(
        self,
        *,
        id: typing.Optional[builtins.str] = None,
        offer: typing.Optional[builtins.str] = None,
        publisher: typing.Optional[builtins.str] = None,
        sku: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#id BatchPool#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param offer: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#offer BatchPool#offer}.
        :param publisher: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#publisher BatchPool#publisher}.
        :param sku: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#sku BatchPool#sku}.
        :param version: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#version BatchPool#version}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolStorageImageReference.__init__)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument offer", value=offer, expected_type=type_hints["offer"])
            check_type(argname="argument publisher", value=publisher, expected_type=type_hints["publisher"])
            check_type(argname="argument sku", value=sku, expected_type=type_hints["sku"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[str, typing.Any] = {}
        if id is not None:
            self._values["id"] = id
        if offer is not None:
            self._values["offer"] = offer
        if publisher is not None:
            self._values["publisher"] = publisher
        if sku is not None:
            self._values["sku"] = sku
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#id BatchPool#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def offer(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#offer BatchPool#offer}.'''
        result = self._values.get("offer")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def publisher(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#publisher BatchPool#publisher}.'''
        result = self._values.get("publisher")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sku(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#sku BatchPool#sku}.'''
        result = self._values.get("sku")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#version BatchPool#version}.'''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchPoolStorageImageReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BatchPoolStorageImageReferenceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolStorageImageReferenceOutputReference",
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
            type_hints = typing.get_type_hints(BatchPoolStorageImageReferenceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetOffer")
    def reset_offer(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOffer", []))

    @jsii.member(jsii_name="resetPublisher")
    def reset_publisher(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublisher", []))

    @jsii.member(jsii_name="resetSku")
    def reset_sku(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSku", []))

    @jsii.member(jsii_name="resetVersion")
    def reset_version(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersion", []))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="offerInput")
    def offer_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "offerInput"))

    @builtins.property
    @jsii.member(jsii_name="publisherInput")
    def publisher_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publisherInput"))

    @builtins.property
    @jsii.member(jsii_name="skuInput")
    def sku_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "skuInput"))

    @builtins.property
    @jsii.member(jsii_name="versionInput")
    def version_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStorageImageReferenceOutputReference, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="offer")
    def offer(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "offer"))

    @offer.setter
    def offer(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStorageImageReferenceOutputReference, "offer").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "offer", value)

    @builtins.property
    @jsii.member(jsii_name="publisher")
    def publisher(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publisher"))

    @publisher.setter
    def publisher(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStorageImageReferenceOutputReference, "publisher").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publisher", value)

    @builtins.property
    @jsii.member(jsii_name="sku")
    def sku(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sku"))

    @sku.setter
    def sku(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStorageImageReferenceOutputReference, "sku").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sku", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStorageImageReferenceOutputReference, "version").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[BatchPoolStorageImageReference]:
        return typing.cast(typing.Optional[BatchPoolStorageImageReference], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[BatchPoolStorageImageReference],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolStorageImageReferenceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolTaskSchedulingPolicy",
    jsii_struct_bases=[],
    name_mapping={"node_fill_type": "nodeFillType"},
)
class BatchPoolTaskSchedulingPolicy:
    def __init__(self, *, node_fill_type: typing.Optional[builtins.str] = None) -> None:
        '''
        :param node_fill_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#node_fill_type BatchPool#node_fill_type}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolTaskSchedulingPolicy.__init__)
            check_type(argname="argument node_fill_type", value=node_fill_type, expected_type=type_hints["node_fill_type"])
        self._values: typing.Dict[str, typing.Any] = {}
        if node_fill_type is not None:
            self._values["node_fill_type"] = node_fill_type

    @builtins.property
    def node_fill_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#node_fill_type BatchPool#node_fill_type}.'''
        result = self._values.get("node_fill_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchPoolTaskSchedulingPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BatchPoolTaskSchedulingPolicyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolTaskSchedulingPolicyList",
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
            type_hints = typing.get_type_hints(BatchPoolTaskSchedulingPolicyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "BatchPoolTaskSchedulingPolicyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolTaskSchedulingPolicyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BatchPoolTaskSchedulingPolicyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolTaskSchedulingPolicyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolTaskSchedulingPolicyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolTaskSchedulingPolicyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolTaskSchedulingPolicy]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolTaskSchedulingPolicy]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolTaskSchedulingPolicy]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolTaskSchedulingPolicyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BatchPoolTaskSchedulingPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolTaskSchedulingPolicyOutputReference",
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
            type_hints = typing.get_type_hints(BatchPoolTaskSchedulingPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetNodeFillType")
    def reset_node_fill_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNodeFillType", []))

    @builtins.property
    @jsii.member(jsii_name="nodeFillTypeInput")
    def node_fill_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nodeFillTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="nodeFillType")
    def node_fill_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nodeFillType"))

    @node_fill_type.setter
    def node_fill_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolTaskSchedulingPolicyOutputReference, "node_fill_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nodeFillType", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BatchPoolTaskSchedulingPolicy, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BatchPoolTaskSchedulingPolicy, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BatchPoolTaskSchedulingPolicy, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolTaskSchedulingPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolTimeouts",
    jsii_struct_bases=[],
    name_mapping={
        "create": "create",
        "delete": "delete",
        "read": "read",
        "update": "update",
    },
)
class BatchPoolTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#create BatchPool#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#delete BatchPool#delete}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#read BatchPool#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#update BatchPool#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#create BatchPool#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#delete BatchPool#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#read BatchPool#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#update BatchPool#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchPoolTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BatchPoolTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(BatchPoolTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BatchPoolTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BatchPoolTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BatchPoolTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolUserAccounts",
    jsii_struct_bases=[],
    name_mapping={
        "elevation_level": "elevationLevel",
        "name": "name",
        "password": "password",
        "linux_user_configuration": "linuxUserConfiguration",
        "windows_user_configuration": "windowsUserConfiguration",
    },
)
class BatchPoolUserAccounts:
    def __init__(
        self,
        *,
        elevation_level: builtins.str,
        name: builtins.str,
        password: builtins.str,
        linux_user_configuration: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolUserAccountsLinuxUserConfiguration", typing.Dict[str, typing.Any]]]]] = None,
        windows_user_configuration: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolUserAccountsWindowsUserConfiguration", typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''
        :param elevation_level: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#elevation_level BatchPool#elevation_level}.
        :param name: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#name BatchPool#name}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#password BatchPool#password}.
        :param linux_user_configuration: linux_user_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#linux_user_configuration BatchPool#linux_user_configuration}
        :param windows_user_configuration: windows_user_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#windows_user_configuration BatchPool#windows_user_configuration}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolUserAccounts.__init__)
            check_type(argname="argument elevation_level", value=elevation_level, expected_type=type_hints["elevation_level"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument linux_user_configuration", value=linux_user_configuration, expected_type=type_hints["linux_user_configuration"])
            check_type(argname="argument windows_user_configuration", value=windows_user_configuration, expected_type=type_hints["windows_user_configuration"])
        self._values: typing.Dict[str, typing.Any] = {
            "elevation_level": elevation_level,
            "name": name,
            "password": password,
        }
        if linux_user_configuration is not None:
            self._values["linux_user_configuration"] = linux_user_configuration
        if windows_user_configuration is not None:
            self._values["windows_user_configuration"] = windows_user_configuration

    @builtins.property
    def elevation_level(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#elevation_level BatchPool#elevation_level}.'''
        result = self._values.get("elevation_level")
        assert result is not None, "Required property 'elevation_level' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#name BatchPool#name}.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def password(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#password BatchPool#password}.'''
        result = self._values.get("password")
        assert result is not None, "Required property 'password' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def linux_user_configuration(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolUserAccountsLinuxUserConfiguration"]]]:
        '''linux_user_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#linux_user_configuration BatchPool#linux_user_configuration}
        '''
        result = self._values.get("linux_user_configuration")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolUserAccountsLinuxUserConfiguration"]]], result)

    @builtins.property
    def windows_user_configuration(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolUserAccountsWindowsUserConfiguration"]]]:
        '''windows_user_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#windows_user_configuration BatchPool#windows_user_configuration}
        '''
        result = self._values.get("windows_user_configuration")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolUserAccountsWindowsUserConfiguration"]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchPoolUserAccounts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolUserAccountsLinuxUserConfiguration",
    jsii_struct_bases=[],
    name_mapping={"gid": "gid", "ssh_private_key": "sshPrivateKey", "uid": "uid"},
)
class BatchPoolUserAccountsLinuxUserConfiguration:
    def __init__(
        self,
        *,
        gid: typing.Optional[jsii.Number] = None,
        ssh_private_key: typing.Optional[builtins.str] = None,
        uid: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param gid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#gid BatchPool#gid}.
        :param ssh_private_key: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#ssh_private_key BatchPool#ssh_private_key}.
        :param uid: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#uid BatchPool#uid}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolUserAccountsLinuxUserConfiguration.__init__)
            check_type(argname="argument gid", value=gid, expected_type=type_hints["gid"])
            check_type(argname="argument ssh_private_key", value=ssh_private_key, expected_type=type_hints["ssh_private_key"])
            check_type(argname="argument uid", value=uid, expected_type=type_hints["uid"])
        self._values: typing.Dict[str, typing.Any] = {}
        if gid is not None:
            self._values["gid"] = gid
        if ssh_private_key is not None:
            self._values["ssh_private_key"] = ssh_private_key
        if uid is not None:
            self._values["uid"] = uid

    @builtins.property
    def gid(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#gid BatchPool#gid}.'''
        result = self._values.get("gid")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ssh_private_key(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#ssh_private_key BatchPool#ssh_private_key}.'''
        result = self._values.get("ssh_private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def uid(self) -> typing.Optional[jsii.Number]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#uid BatchPool#uid}.'''
        result = self._values.get("uid")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchPoolUserAccountsLinuxUserConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BatchPoolUserAccountsLinuxUserConfigurationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolUserAccountsLinuxUserConfigurationList",
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
            type_hints = typing.get_type_hints(BatchPoolUserAccountsLinuxUserConfigurationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "BatchPoolUserAccountsLinuxUserConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolUserAccountsLinuxUserConfigurationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BatchPoolUserAccountsLinuxUserConfigurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolUserAccountsLinuxUserConfigurationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolUserAccountsLinuxUserConfigurationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolUserAccountsLinuxUserConfigurationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolUserAccountsLinuxUserConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolUserAccountsLinuxUserConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolUserAccountsLinuxUserConfiguration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolUserAccountsLinuxUserConfigurationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BatchPoolUserAccountsLinuxUserConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolUserAccountsLinuxUserConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(BatchPoolUserAccountsLinuxUserConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetGid")
    def reset_gid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGid", []))

    @jsii.member(jsii_name="resetSshPrivateKey")
    def reset_ssh_private_key(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSshPrivateKey", []))

    @jsii.member(jsii_name="resetUid")
    def reset_uid(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUid", []))

    @builtins.property
    @jsii.member(jsii_name="gidInput")
    def gid_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "gidInput"))

    @builtins.property
    @jsii.member(jsii_name="sshPrivateKeyInput")
    def ssh_private_key_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sshPrivateKeyInput"))

    @builtins.property
    @jsii.member(jsii_name="uidInput")
    def uid_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "uidInput"))

    @builtins.property
    @jsii.member(jsii_name="gid")
    def gid(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "gid"))

    @gid.setter
    def gid(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolUserAccountsLinuxUserConfigurationOutputReference, "gid").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gid", value)

    @builtins.property
    @jsii.member(jsii_name="sshPrivateKey")
    def ssh_private_key(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sshPrivateKey"))

    @ssh_private_key.setter
    def ssh_private_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolUserAccountsLinuxUserConfigurationOutputReference, "ssh_private_key").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sshPrivateKey", value)

    @builtins.property
    @jsii.member(jsii_name="uid")
    def uid(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "uid"))

    @uid.setter
    def uid(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolUserAccountsLinuxUserConfigurationOutputReference, "uid").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uid", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BatchPoolUserAccountsLinuxUserConfiguration, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BatchPoolUserAccountsLinuxUserConfiguration, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BatchPoolUserAccountsLinuxUserConfiguration, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolUserAccountsLinuxUserConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BatchPoolUserAccountsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolUserAccountsList",
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
            type_hints = typing.get_type_hints(BatchPoolUserAccountsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "BatchPoolUserAccountsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolUserAccountsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BatchPoolUserAccountsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolUserAccountsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolUserAccountsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolUserAccountsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolUserAccounts]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolUserAccounts]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolUserAccounts]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolUserAccountsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BatchPoolUserAccountsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolUserAccountsOutputReference",
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
            type_hints = typing.get_type_hints(BatchPoolUserAccountsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putLinuxUserConfiguration")
    def put_linux_user_configuration(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[BatchPoolUserAccountsLinuxUserConfiguration, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolUserAccountsOutputReference.put_linux_user_configuration)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLinuxUserConfiguration", [value]))

    @jsii.member(jsii_name="putWindowsUserConfiguration")
    def put_windows_user_configuration(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["BatchPoolUserAccountsWindowsUserConfiguration", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolUserAccountsOutputReference.put_windows_user_configuration)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putWindowsUserConfiguration", [value]))

    @jsii.member(jsii_name="resetLinuxUserConfiguration")
    def reset_linux_user_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLinuxUserConfiguration", []))

    @jsii.member(jsii_name="resetWindowsUserConfiguration")
    def reset_windows_user_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWindowsUserConfiguration", []))

    @builtins.property
    @jsii.member(jsii_name="linuxUserConfiguration")
    def linux_user_configuration(
        self,
    ) -> BatchPoolUserAccountsLinuxUserConfigurationList:
        return typing.cast(BatchPoolUserAccountsLinuxUserConfigurationList, jsii.get(self, "linuxUserConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="windowsUserConfiguration")
    def windows_user_configuration(
        self,
    ) -> "BatchPoolUserAccountsWindowsUserConfigurationList":
        return typing.cast("BatchPoolUserAccountsWindowsUserConfigurationList", jsii.get(self, "windowsUserConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="elevationLevelInput")
    def elevation_level_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "elevationLevelInput"))

    @builtins.property
    @jsii.member(jsii_name="linuxUserConfigurationInput")
    def linux_user_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolUserAccountsLinuxUserConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolUserAccountsLinuxUserConfiguration]]], jsii.get(self, "linuxUserConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="windowsUserConfigurationInput")
    def windows_user_configuration_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolUserAccountsWindowsUserConfiguration"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["BatchPoolUserAccountsWindowsUserConfiguration"]]], jsii.get(self, "windowsUserConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="elevationLevel")
    def elevation_level(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "elevationLevel"))

    @elevation_level.setter
    def elevation_level(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolUserAccountsOutputReference, "elevation_level").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elevationLevel", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolUserAccountsOutputReference, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolUserAccountsOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BatchPoolUserAccounts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BatchPoolUserAccounts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BatchPoolUserAccounts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolUserAccountsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolUserAccountsWindowsUserConfiguration",
    jsii_struct_bases=[],
    name_mapping={"login_mode": "loginMode"},
)
class BatchPoolUserAccountsWindowsUserConfiguration:
    def __init__(self, *, login_mode: builtins.str) -> None:
        '''
        :param login_mode: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#login_mode BatchPool#login_mode}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolUserAccountsWindowsUserConfiguration.__init__)
            check_type(argname="argument login_mode", value=login_mode, expected_type=type_hints["login_mode"])
        self._values: typing.Dict[str, typing.Any] = {
            "login_mode": login_mode,
        }

    @builtins.property
    def login_mode(self) -> builtins.str:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#login_mode BatchPool#login_mode}.'''
        result = self._values.get("login_mode")
        assert result is not None, "Required property 'login_mode' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchPoolUserAccountsWindowsUserConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BatchPoolUserAccountsWindowsUserConfigurationList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolUserAccountsWindowsUserConfigurationList",
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
            type_hints = typing.get_type_hints(BatchPoolUserAccountsWindowsUserConfigurationList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "BatchPoolUserAccountsWindowsUserConfigurationOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolUserAccountsWindowsUserConfigurationList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BatchPoolUserAccountsWindowsUserConfigurationOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolUserAccountsWindowsUserConfigurationList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolUserAccountsWindowsUserConfigurationList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolUserAccountsWindowsUserConfigurationList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolUserAccountsWindowsUserConfiguration]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolUserAccountsWindowsUserConfiguration]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolUserAccountsWindowsUserConfiguration]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolUserAccountsWindowsUserConfigurationList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BatchPoolUserAccountsWindowsUserConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolUserAccountsWindowsUserConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(BatchPoolUserAccountsWindowsUserConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="loginModeInput")
    def login_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loginModeInput"))

    @builtins.property
    @jsii.member(jsii_name="loginMode")
    def login_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "loginMode"))

    @login_mode.setter
    def login_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolUserAccountsWindowsUserConfigurationOutputReference, "login_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loginMode", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BatchPoolUserAccountsWindowsUserConfiguration, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BatchPoolUserAccountsWindowsUserConfiguration, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BatchPoolUserAccountsWindowsUserConfiguration, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolUserAccountsWindowsUserConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolWindows",
    jsii_struct_bases=[],
    name_mapping={"enable_automatic_updates": "enableAutomaticUpdates"},
)
class BatchPoolWindows:
    def __init__(
        self,
        *,
        enable_automatic_updates: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param enable_automatic_updates: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#enable_automatic_updates BatchPool#enable_automatic_updates}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolWindows.__init__)
            check_type(argname="argument enable_automatic_updates", value=enable_automatic_updates, expected_type=type_hints["enable_automatic_updates"])
        self._values: typing.Dict[str, typing.Any] = {}
        if enable_automatic_updates is not None:
            self._values["enable_automatic_updates"] = enable_automatic_updates

    @builtins.property
    def enable_automatic_updates(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/azurerm/r/batch_pool#enable_automatic_updates BatchPool#enable_automatic_updates}.'''
        result = self._values.get("enable_automatic_updates")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BatchPoolWindows(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class BatchPoolWindowsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolWindowsList",
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
            type_hints = typing.get_type_hints(BatchPoolWindowsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "BatchPoolWindowsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(BatchPoolWindowsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("BatchPoolWindowsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolWindowsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolWindowsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(BatchPoolWindowsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolWindows]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolWindows]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[BatchPoolWindows]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolWindowsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class BatchPoolWindowsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-azurerm.batchPool.BatchPoolWindowsOutputReference",
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
            type_hints = typing.get_type_hints(BatchPoolWindowsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetEnableAutomaticUpdates")
    def reset_enable_automatic_updates(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableAutomaticUpdates", []))

    @builtins.property
    @jsii.member(jsii_name="enableAutomaticUpdatesInput")
    def enable_automatic_updates_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableAutomaticUpdatesInput"))

    @builtins.property
    @jsii.member(jsii_name="enableAutomaticUpdates")
    def enable_automatic_updates(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableAutomaticUpdates"))

    @enable_automatic_updates.setter
    def enable_automatic_updates(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolWindowsOutputReference, "enable_automatic_updates").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableAutomaticUpdates", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[BatchPoolWindows, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[BatchPoolWindows, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[BatchPoolWindows, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(BatchPoolWindowsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "BatchPool",
    "BatchPoolAutoScale",
    "BatchPoolAutoScaleOutputReference",
    "BatchPoolCertificate",
    "BatchPoolCertificateList",
    "BatchPoolCertificateOutputReference",
    "BatchPoolConfig",
    "BatchPoolContainerConfiguration",
    "BatchPoolContainerConfigurationContainerRegistries",
    "BatchPoolContainerConfigurationContainerRegistriesList",
    "BatchPoolContainerConfigurationContainerRegistriesOutputReference",
    "BatchPoolContainerConfigurationOutputReference",
    "BatchPoolDataDisks",
    "BatchPoolDataDisksList",
    "BatchPoolDataDisksOutputReference",
    "BatchPoolDiskEncryption",
    "BatchPoolDiskEncryptionList",
    "BatchPoolDiskEncryptionOutputReference",
    "BatchPoolExtensions",
    "BatchPoolExtensionsList",
    "BatchPoolExtensionsOutputReference",
    "BatchPoolFixedScale",
    "BatchPoolFixedScaleOutputReference",
    "BatchPoolIdentity",
    "BatchPoolIdentityOutputReference",
    "BatchPoolMount",
    "BatchPoolMountAzureBlobFileSystem",
    "BatchPoolMountAzureBlobFileSystemOutputReference",
    "BatchPoolMountAzureFileShare",
    "BatchPoolMountAzureFileShareList",
    "BatchPoolMountAzureFileShareOutputReference",
    "BatchPoolMountCifsMount",
    "BatchPoolMountCifsMountList",
    "BatchPoolMountCifsMountOutputReference",
    "BatchPoolMountList",
    "BatchPoolMountNfsMount",
    "BatchPoolMountNfsMountList",
    "BatchPoolMountNfsMountOutputReference",
    "BatchPoolMountOutputReference",
    "BatchPoolNetworkConfiguration",
    "BatchPoolNetworkConfigurationEndpointConfiguration",
    "BatchPoolNetworkConfigurationEndpointConfigurationList",
    "BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRules",
    "BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRulesList",
    "BatchPoolNetworkConfigurationEndpointConfigurationNetworkSecurityGroupRulesOutputReference",
    "BatchPoolNetworkConfigurationEndpointConfigurationOutputReference",
    "BatchPoolNetworkConfigurationOutputReference",
    "BatchPoolNodePlacement",
    "BatchPoolNodePlacementList",
    "BatchPoolNodePlacementOutputReference",
    "BatchPoolStartTask",
    "BatchPoolStartTaskContainer",
    "BatchPoolStartTaskContainerList",
    "BatchPoolStartTaskContainerOutputReference",
    "BatchPoolStartTaskContainerRegistry",
    "BatchPoolStartTaskContainerRegistryList",
    "BatchPoolStartTaskContainerRegistryOutputReference",
    "BatchPoolStartTaskOutputReference",
    "BatchPoolStartTaskResourceFile",
    "BatchPoolStartTaskResourceFileList",
    "BatchPoolStartTaskResourceFileOutputReference",
    "BatchPoolStartTaskUserIdentity",
    "BatchPoolStartTaskUserIdentityAutoUser",
    "BatchPoolStartTaskUserIdentityAutoUserOutputReference",
    "BatchPoolStartTaskUserIdentityOutputReference",
    "BatchPoolStorageImageReference",
    "BatchPoolStorageImageReferenceOutputReference",
    "BatchPoolTaskSchedulingPolicy",
    "BatchPoolTaskSchedulingPolicyList",
    "BatchPoolTaskSchedulingPolicyOutputReference",
    "BatchPoolTimeouts",
    "BatchPoolTimeoutsOutputReference",
    "BatchPoolUserAccounts",
    "BatchPoolUserAccountsLinuxUserConfiguration",
    "BatchPoolUserAccountsLinuxUserConfigurationList",
    "BatchPoolUserAccountsLinuxUserConfigurationOutputReference",
    "BatchPoolUserAccountsList",
    "BatchPoolUserAccountsOutputReference",
    "BatchPoolUserAccountsWindowsUserConfiguration",
    "BatchPoolUserAccountsWindowsUserConfigurationList",
    "BatchPoolUserAccountsWindowsUserConfigurationOutputReference",
    "BatchPoolWindows",
    "BatchPoolWindowsList",
    "BatchPoolWindowsOutputReference",
]

publication.publish()
