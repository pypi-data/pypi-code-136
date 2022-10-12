'''
# `google_dns_managed_zone`

Refer to the Terraform Registory for docs: [`google_dns_managed_zone`](https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone).
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


class GoogleDnsManagedZone(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDnsManagedZone.GoogleDnsManagedZone",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone google_dns_managed_zone}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        dns_name: builtins.str,
        name: builtins.str,
        cloud_logging_config: typing.Optional[typing.Union["GoogleDnsManagedZoneCloudLoggingConfig", typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        dnssec_config: typing.Optional[typing.Union["GoogleDnsManagedZoneDnssecConfig", typing.Dict[str, typing.Any]]] = None,
        force_destroy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        forwarding_config: typing.Optional[typing.Union["GoogleDnsManagedZoneForwardingConfig", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        peering_config: typing.Optional[typing.Union["GoogleDnsManagedZonePeeringConfig", typing.Dict[str, typing.Any]]] = None,
        private_visibility_config: typing.Optional[typing.Union["GoogleDnsManagedZonePrivateVisibilityConfig", typing.Dict[str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        reverse_lookup: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        service_directory_config: typing.Optional[typing.Union["GoogleDnsManagedZoneServiceDirectoryConfig", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleDnsManagedZoneTimeouts", typing.Dict[str, typing.Any]]] = None,
        visibility: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone google_dns_managed_zone} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param dns_name: The DNS name of this managed zone, for instance "example.com.". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#dns_name GoogleDnsManagedZone#dns_name}
        :param name: User assigned name for this resource. Must be unique within the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#name GoogleDnsManagedZone#name}
        :param cloud_logging_config: cloud_logging_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#cloud_logging_config GoogleDnsManagedZone#cloud_logging_config}
        :param description: A textual description field. Defaults to 'Managed by Terraform'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#description GoogleDnsManagedZone#description}
        :param dnssec_config: dnssec_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#dnssec_config GoogleDnsManagedZone#dnssec_config}
        :param force_destroy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#force_destroy GoogleDnsManagedZone#force_destroy}.
        :param forwarding_config: forwarding_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#forwarding_config GoogleDnsManagedZone#forwarding_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#id GoogleDnsManagedZone#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: A set of key/value label pairs to assign to this ManagedZone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#labels GoogleDnsManagedZone#labels}
        :param peering_config: peering_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#peering_config GoogleDnsManagedZone#peering_config}
        :param private_visibility_config: private_visibility_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#private_visibility_config GoogleDnsManagedZone#private_visibility_config}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#project GoogleDnsManagedZone#project}.
        :param reverse_lookup: Specifies if this is a managed reverse lookup zone. If true, Cloud DNS will resolve reverse lookup queries using automatically configured records for VPC resources. This only applies to networks listed under 'private_visibility_config'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#reverse_lookup GoogleDnsManagedZone#reverse_lookup}
        :param service_directory_config: service_directory_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#service_directory_config GoogleDnsManagedZone#service_directory_config}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#timeouts GoogleDnsManagedZone#timeouts}
        :param visibility: The zone's visibility: public zones are exposed to the Internet, while private zones are visible only to Virtual Private Cloud resources. Default value: "public" Possible values: ["private", "public"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#visibility GoogleDnsManagedZone#visibility}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDnsManagedZone.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleDnsManagedZoneConfig(
            dns_name=dns_name,
            name=name,
            cloud_logging_config=cloud_logging_config,
            description=description,
            dnssec_config=dnssec_config,
            force_destroy=force_destroy,
            forwarding_config=forwarding_config,
            id=id,
            labels=labels,
            peering_config=peering_config,
            private_visibility_config=private_visibility_config,
            project=project,
            reverse_lookup=reverse_lookup,
            service_directory_config=service_directory_config,
            timeouts=timeouts,
            visibility=visibility,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCloudLoggingConfig")
    def put_cloud_logging_config(
        self,
        *,
        enable_logging: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enable_logging: If set, enable query logging for this ManagedZone. False by default, making logging opt-in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#enable_logging GoogleDnsManagedZone#enable_logging}
        '''
        value = GoogleDnsManagedZoneCloudLoggingConfig(enable_logging=enable_logging)

        return typing.cast(None, jsii.invoke(self, "putCloudLoggingConfig", [value]))

    @jsii.member(jsii_name="putDnssecConfig")
    def put_dnssec_config(
        self,
        *,
        default_key_specs: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDnsManagedZoneDnssecConfigDefaultKeySpecs", typing.Dict[str, typing.Any]]]]] = None,
        kind: typing.Optional[builtins.str] = None,
        non_existence: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param default_key_specs: default_key_specs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#default_key_specs GoogleDnsManagedZone#default_key_specs}
        :param kind: Identifies what kind of resource this is. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#kind GoogleDnsManagedZone#kind}
        :param non_existence: Specifies the mechanism used to provide authenticated denial-of-existence responses. non_existence can only be updated when the state is 'off'. Possible values: ["nsec", "nsec3"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#non_existence GoogleDnsManagedZone#non_existence}
        :param state: Specifies whether DNSSEC is enabled, and what mode it is in Possible values: ["off", "on", "transfer"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#state GoogleDnsManagedZone#state}
        '''
        value = GoogleDnsManagedZoneDnssecConfig(
            default_key_specs=default_key_specs,
            kind=kind,
            non_existence=non_existence,
            state=state,
        )

        return typing.cast(None, jsii.invoke(self, "putDnssecConfig", [value]))

    @jsii.member(jsii_name="putForwardingConfig")
    def put_forwarding_config(
        self,
        *,
        target_name_servers: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDnsManagedZoneForwardingConfigTargetNameServers", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param target_name_servers: target_name_servers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#target_name_servers GoogleDnsManagedZone#target_name_servers}
        '''
        value = GoogleDnsManagedZoneForwardingConfig(
            target_name_servers=target_name_servers
        )

        return typing.cast(None, jsii.invoke(self, "putForwardingConfig", [value]))

    @jsii.member(jsii_name="putPeeringConfig")
    def put_peering_config(
        self,
        *,
        target_network: typing.Union["GoogleDnsManagedZonePeeringConfigTargetNetwork", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param target_network: target_network block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#target_network GoogleDnsManagedZone#target_network}
        '''
        value = GoogleDnsManagedZonePeeringConfig(target_network=target_network)

        return typing.cast(None, jsii.invoke(self, "putPeeringConfig", [value]))

    @jsii.member(jsii_name="putPrivateVisibilityConfig")
    def put_private_visibility_config(
        self,
        *,
        networks: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDnsManagedZonePrivateVisibilityConfigNetworks", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param networks: networks block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#networks GoogleDnsManagedZone#networks}
        '''
        value = GoogleDnsManagedZonePrivateVisibilityConfig(networks=networks)

        return typing.cast(None, jsii.invoke(self, "putPrivateVisibilityConfig", [value]))

    @jsii.member(jsii_name="putServiceDirectoryConfig")
    def put_service_directory_config(
        self,
        *,
        namespace: typing.Union["GoogleDnsManagedZoneServiceDirectoryConfigNamespace", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param namespace: namespace block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#namespace GoogleDnsManagedZone#namespace}
        '''
        value = GoogleDnsManagedZoneServiceDirectoryConfig(namespace=namespace)

        return typing.cast(None, jsii.invoke(self, "putServiceDirectoryConfig", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#create GoogleDnsManagedZone#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#delete GoogleDnsManagedZone#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#update GoogleDnsManagedZone#update}.
        '''
        value = GoogleDnsManagedZoneTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCloudLoggingConfig")
    def reset_cloud_logging_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCloudLoggingConfig", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDnssecConfig")
    def reset_dnssec_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDnssecConfig", []))

    @jsii.member(jsii_name="resetForceDestroy")
    def reset_force_destroy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceDestroy", []))

    @jsii.member(jsii_name="resetForwardingConfig")
    def reset_forwarding_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForwardingConfig", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetPeeringConfig")
    def reset_peering_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPeeringConfig", []))

    @jsii.member(jsii_name="resetPrivateVisibilityConfig")
    def reset_private_visibility_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrivateVisibilityConfig", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetReverseLookup")
    def reset_reverse_lookup(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReverseLookup", []))

    @jsii.member(jsii_name="resetServiceDirectoryConfig")
    def reset_service_directory_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServiceDirectoryConfig", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetVisibility")
    def reset_visibility(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVisibility", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="cloudLoggingConfig")
    def cloud_logging_config(
        self,
    ) -> "GoogleDnsManagedZoneCloudLoggingConfigOutputReference":
        return typing.cast("GoogleDnsManagedZoneCloudLoggingConfigOutputReference", jsii.get(self, "cloudLoggingConfig"))

    @builtins.property
    @jsii.member(jsii_name="creationTime")
    def creation_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "creationTime"))

    @builtins.property
    @jsii.member(jsii_name="dnssecConfig")
    def dnssec_config(self) -> "GoogleDnsManagedZoneDnssecConfigOutputReference":
        return typing.cast("GoogleDnsManagedZoneDnssecConfigOutputReference", jsii.get(self, "dnssecConfig"))

    @builtins.property
    @jsii.member(jsii_name="forwardingConfig")
    def forwarding_config(
        self,
    ) -> "GoogleDnsManagedZoneForwardingConfigOutputReference":
        return typing.cast("GoogleDnsManagedZoneForwardingConfigOutputReference", jsii.get(self, "forwardingConfig"))

    @builtins.property
    @jsii.member(jsii_name="managedZoneId")
    def managed_zone_id(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "managedZoneId"))

    @builtins.property
    @jsii.member(jsii_name="nameServers")
    def name_servers(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "nameServers"))

    @builtins.property
    @jsii.member(jsii_name="peeringConfig")
    def peering_config(self) -> "GoogleDnsManagedZonePeeringConfigOutputReference":
        return typing.cast("GoogleDnsManagedZonePeeringConfigOutputReference", jsii.get(self, "peeringConfig"))

    @builtins.property
    @jsii.member(jsii_name="privateVisibilityConfig")
    def private_visibility_config(
        self,
    ) -> "GoogleDnsManagedZonePrivateVisibilityConfigOutputReference":
        return typing.cast("GoogleDnsManagedZonePrivateVisibilityConfigOutputReference", jsii.get(self, "privateVisibilityConfig"))

    @builtins.property
    @jsii.member(jsii_name="serviceDirectoryConfig")
    def service_directory_config(
        self,
    ) -> "GoogleDnsManagedZoneServiceDirectoryConfigOutputReference":
        return typing.cast("GoogleDnsManagedZoneServiceDirectoryConfigOutputReference", jsii.get(self, "serviceDirectoryConfig"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleDnsManagedZoneTimeoutsOutputReference":
        return typing.cast("GoogleDnsManagedZoneTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="cloudLoggingConfigInput")
    def cloud_logging_config_input(
        self,
    ) -> typing.Optional["GoogleDnsManagedZoneCloudLoggingConfig"]:
        return typing.cast(typing.Optional["GoogleDnsManagedZoneCloudLoggingConfig"], jsii.get(self, "cloudLoggingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="dnsNameInput")
    def dns_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dnsNameInput"))

    @builtins.property
    @jsii.member(jsii_name="dnssecConfigInput")
    def dnssec_config_input(
        self,
    ) -> typing.Optional["GoogleDnsManagedZoneDnssecConfig"]:
        return typing.cast(typing.Optional["GoogleDnsManagedZoneDnssecConfig"], jsii.get(self, "dnssecConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="forceDestroyInput")
    def force_destroy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "forceDestroyInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardingConfigInput")
    def forwarding_config_input(
        self,
    ) -> typing.Optional["GoogleDnsManagedZoneForwardingConfig"]:
        return typing.cast(typing.Optional["GoogleDnsManagedZoneForwardingConfig"], jsii.get(self, "forwardingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="peeringConfigInput")
    def peering_config_input(
        self,
    ) -> typing.Optional["GoogleDnsManagedZonePeeringConfig"]:
        return typing.cast(typing.Optional["GoogleDnsManagedZonePeeringConfig"], jsii.get(self, "peeringConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="privateVisibilityConfigInput")
    def private_visibility_config_input(
        self,
    ) -> typing.Optional["GoogleDnsManagedZonePrivateVisibilityConfig"]:
        return typing.cast(typing.Optional["GoogleDnsManagedZonePrivateVisibilityConfig"], jsii.get(self, "privateVisibilityConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="reverseLookupInput")
    def reverse_lookup_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "reverseLookupInput"))

    @builtins.property
    @jsii.member(jsii_name="serviceDirectoryConfigInput")
    def service_directory_config_input(
        self,
    ) -> typing.Optional["GoogleDnsManagedZoneServiceDirectoryConfig"]:
        return typing.cast(typing.Optional["GoogleDnsManagedZoneServiceDirectoryConfig"], jsii.get(self, "serviceDirectoryConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleDnsManagedZoneTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleDnsManagedZoneTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="visibilityInput")
    def visibility_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "visibilityInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZone, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="dnsName")
    def dns_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dnsName"))

    @dns_name.setter
    def dns_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZone, "dns_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dnsName", value)

    @builtins.property
    @jsii.member(jsii_name="forceDestroy")
    def force_destroy(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "forceDestroy"))

    @force_destroy.setter
    def force_destroy(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZone, "force_destroy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceDestroy", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZone, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZone, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZone, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZone, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="reverseLookup")
    def reverse_lookup(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "reverseLookup"))

    @reverse_lookup.setter
    def reverse_lookup(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZone, "reverse_lookup").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reverseLookup", value)

    @builtins.property
    @jsii.member(jsii_name="visibility")
    def visibility(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "visibility"))

    @visibility.setter
    def visibility(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZone, "visibility").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "visibility", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDnsManagedZone.GoogleDnsManagedZoneCloudLoggingConfig",
    jsii_struct_bases=[],
    name_mapping={"enable_logging": "enableLogging"},
)
class GoogleDnsManagedZoneCloudLoggingConfig:
    def __init__(
        self,
        *,
        enable_logging: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enable_logging: If set, enable query logging for this ManagedZone. False by default, making logging opt-in. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#enable_logging GoogleDnsManagedZone#enable_logging}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDnsManagedZoneCloudLoggingConfig.__init__)
            check_type(argname="argument enable_logging", value=enable_logging, expected_type=type_hints["enable_logging"])
        self._values: typing.Dict[str, typing.Any] = {
            "enable_logging": enable_logging,
        }

    @builtins.property
    def enable_logging(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''If set, enable query logging for this ManagedZone. False by default, making logging opt-in.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#enable_logging GoogleDnsManagedZone#enable_logging}
        '''
        result = self._values.get("enable_logging")
        assert result is not None, "Required property 'enable_logging' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDnsManagedZoneCloudLoggingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDnsManagedZoneCloudLoggingConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDnsManagedZone.GoogleDnsManagedZoneCloudLoggingConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDnsManagedZoneCloudLoggingConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="enableLoggingInput")
    def enable_logging_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableLoggingInput"))

    @builtins.property
    @jsii.member(jsii_name="enableLogging")
    def enable_logging(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableLogging"))

    @enable_logging.setter
    def enable_logging(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZoneCloudLoggingConfigOutputReference, "enable_logging").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableLogging", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleDnsManagedZoneCloudLoggingConfig]:
        return typing.cast(typing.Optional[GoogleDnsManagedZoneCloudLoggingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDnsManagedZoneCloudLoggingConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZoneCloudLoggingConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDnsManagedZone.GoogleDnsManagedZoneConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "dns_name": "dnsName",
        "name": "name",
        "cloud_logging_config": "cloudLoggingConfig",
        "description": "description",
        "dnssec_config": "dnssecConfig",
        "force_destroy": "forceDestroy",
        "forwarding_config": "forwardingConfig",
        "id": "id",
        "labels": "labels",
        "peering_config": "peeringConfig",
        "private_visibility_config": "privateVisibilityConfig",
        "project": "project",
        "reverse_lookup": "reverseLookup",
        "service_directory_config": "serviceDirectoryConfig",
        "timeouts": "timeouts",
        "visibility": "visibility",
    },
)
class GoogleDnsManagedZoneConfig(cdktf.TerraformMetaArguments):
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
        dns_name: builtins.str,
        name: builtins.str,
        cloud_logging_config: typing.Optional[typing.Union[GoogleDnsManagedZoneCloudLoggingConfig, typing.Dict[str, typing.Any]]] = None,
        description: typing.Optional[builtins.str] = None,
        dnssec_config: typing.Optional[typing.Union["GoogleDnsManagedZoneDnssecConfig", typing.Dict[str, typing.Any]]] = None,
        force_destroy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        forwarding_config: typing.Optional[typing.Union["GoogleDnsManagedZoneForwardingConfig", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        peering_config: typing.Optional[typing.Union["GoogleDnsManagedZonePeeringConfig", typing.Dict[str, typing.Any]]] = None,
        private_visibility_config: typing.Optional[typing.Union["GoogleDnsManagedZonePrivateVisibilityConfig", typing.Dict[str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        reverse_lookup: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        service_directory_config: typing.Optional[typing.Union["GoogleDnsManagedZoneServiceDirectoryConfig", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleDnsManagedZoneTimeouts", typing.Dict[str, typing.Any]]] = None,
        visibility: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param dns_name: The DNS name of this managed zone, for instance "example.com.". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#dns_name GoogleDnsManagedZone#dns_name}
        :param name: User assigned name for this resource. Must be unique within the project. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#name GoogleDnsManagedZone#name}
        :param cloud_logging_config: cloud_logging_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#cloud_logging_config GoogleDnsManagedZone#cloud_logging_config}
        :param description: A textual description field. Defaults to 'Managed by Terraform'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#description GoogleDnsManagedZone#description}
        :param dnssec_config: dnssec_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#dnssec_config GoogleDnsManagedZone#dnssec_config}
        :param force_destroy: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#force_destroy GoogleDnsManagedZone#force_destroy}.
        :param forwarding_config: forwarding_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#forwarding_config GoogleDnsManagedZone#forwarding_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#id GoogleDnsManagedZone#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: A set of key/value label pairs to assign to this ManagedZone. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#labels GoogleDnsManagedZone#labels}
        :param peering_config: peering_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#peering_config GoogleDnsManagedZone#peering_config}
        :param private_visibility_config: private_visibility_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#private_visibility_config GoogleDnsManagedZone#private_visibility_config}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#project GoogleDnsManagedZone#project}.
        :param reverse_lookup: Specifies if this is a managed reverse lookup zone. If true, Cloud DNS will resolve reverse lookup queries using automatically configured records for VPC resources. This only applies to networks listed under 'private_visibility_config'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#reverse_lookup GoogleDnsManagedZone#reverse_lookup}
        :param service_directory_config: service_directory_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#service_directory_config GoogleDnsManagedZone#service_directory_config}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#timeouts GoogleDnsManagedZone#timeouts}
        :param visibility: The zone's visibility: public zones are exposed to the Internet, while private zones are visible only to Virtual Private Cloud resources. Default value: "public" Possible values: ["private", "public"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#visibility GoogleDnsManagedZone#visibility}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(cloud_logging_config, dict):
            cloud_logging_config = GoogleDnsManagedZoneCloudLoggingConfig(**cloud_logging_config)
        if isinstance(dnssec_config, dict):
            dnssec_config = GoogleDnsManagedZoneDnssecConfig(**dnssec_config)
        if isinstance(forwarding_config, dict):
            forwarding_config = GoogleDnsManagedZoneForwardingConfig(**forwarding_config)
        if isinstance(peering_config, dict):
            peering_config = GoogleDnsManagedZonePeeringConfig(**peering_config)
        if isinstance(private_visibility_config, dict):
            private_visibility_config = GoogleDnsManagedZonePrivateVisibilityConfig(**private_visibility_config)
        if isinstance(service_directory_config, dict):
            service_directory_config = GoogleDnsManagedZoneServiceDirectoryConfig(**service_directory_config)
        if isinstance(timeouts, dict):
            timeouts = GoogleDnsManagedZoneTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDnsManagedZoneConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument dns_name", value=dns_name, expected_type=type_hints["dns_name"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument cloud_logging_config", value=cloud_logging_config, expected_type=type_hints["cloud_logging_config"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument dnssec_config", value=dnssec_config, expected_type=type_hints["dnssec_config"])
            check_type(argname="argument force_destroy", value=force_destroy, expected_type=type_hints["force_destroy"])
            check_type(argname="argument forwarding_config", value=forwarding_config, expected_type=type_hints["forwarding_config"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument peering_config", value=peering_config, expected_type=type_hints["peering_config"])
            check_type(argname="argument private_visibility_config", value=private_visibility_config, expected_type=type_hints["private_visibility_config"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument reverse_lookup", value=reverse_lookup, expected_type=type_hints["reverse_lookup"])
            check_type(argname="argument service_directory_config", value=service_directory_config, expected_type=type_hints["service_directory_config"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument visibility", value=visibility, expected_type=type_hints["visibility"])
        self._values: typing.Dict[str, typing.Any] = {
            "dns_name": dns_name,
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
        if cloud_logging_config is not None:
            self._values["cloud_logging_config"] = cloud_logging_config
        if description is not None:
            self._values["description"] = description
        if dnssec_config is not None:
            self._values["dnssec_config"] = dnssec_config
        if force_destroy is not None:
            self._values["force_destroy"] = force_destroy
        if forwarding_config is not None:
            self._values["forwarding_config"] = forwarding_config
        if id is not None:
            self._values["id"] = id
        if labels is not None:
            self._values["labels"] = labels
        if peering_config is not None:
            self._values["peering_config"] = peering_config
        if private_visibility_config is not None:
            self._values["private_visibility_config"] = private_visibility_config
        if project is not None:
            self._values["project"] = project
        if reverse_lookup is not None:
            self._values["reverse_lookup"] = reverse_lookup
        if service_directory_config is not None:
            self._values["service_directory_config"] = service_directory_config
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if visibility is not None:
            self._values["visibility"] = visibility

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
    def dns_name(self) -> builtins.str:
        '''The DNS name of this managed zone, for instance "example.com.".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#dns_name GoogleDnsManagedZone#dns_name}
        '''
        result = self._values.get("dns_name")
        assert result is not None, "Required property 'dns_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''User assigned name for this resource. Must be unique within the project.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#name GoogleDnsManagedZone#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cloud_logging_config(
        self,
    ) -> typing.Optional[GoogleDnsManagedZoneCloudLoggingConfig]:
        '''cloud_logging_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#cloud_logging_config GoogleDnsManagedZone#cloud_logging_config}
        '''
        result = self._values.get("cloud_logging_config")
        return typing.cast(typing.Optional[GoogleDnsManagedZoneCloudLoggingConfig], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A textual description field. Defaults to 'Managed by Terraform'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#description GoogleDnsManagedZone#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dnssec_config(self) -> typing.Optional["GoogleDnsManagedZoneDnssecConfig"]:
        '''dnssec_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#dnssec_config GoogleDnsManagedZone#dnssec_config}
        '''
        result = self._values.get("dnssec_config")
        return typing.cast(typing.Optional["GoogleDnsManagedZoneDnssecConfig"], result)

    @builtins.property
    def force_destroy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#force_destroy GoogleDnsManagedZone#force_destroy}.'''
        result = self._values.get("force_destroy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def forwarding_config(
        self,
    ) -> typing.Optional["GoogleDnsManagedZoneForwardingConfig"]:
        '''forwarding_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#forwarding_config GoogleDnsManagedZone#forwarding_config}
        '''
        result = self._values.get("forwarding_config")
        return typing.cast(typing.Optional["GoogleDnsManagedZoneForwardingConfig"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#id GoogleDnsManagedZone#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A set of key/value label pairs to assign to this ManagedZone.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#labels GoogleDnsManagedZone#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def peering_config(self) -> typing.Optional["GoogleDnsManagedZonePeeringConfig"]:
        '''peering_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#peering_config GoogleDnsManagedZone#peering_config}
        '''
        result = self._values.get("peering_config")
        return typing.cast(typing.Optional["GoogleDnsManagedZonePeeringConfig"], result)

    @builtins.property
    def private_visibility_config(
        self,
    ) -> typing.Optional["GoogleDnsManagedZonePrivateVisibilityConfig"]:
        '''private_visibility_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#private_visibility_config GoogleDnsManagedZone#private_visibility_config}
        '''
        result = self._values.get("private_visibility_config")
        return typing.cast(typing.Optional["GoogleDnsManagedZonePrivateVisibilityConfig"], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#project GoogleDnsManagedZone#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def reverse_lookup(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies if this is a managed reverse lookup zone.

        If true, Cloud DNS will resolve reverse
        lookup queries using automatically configured records for VPC resources. This only applies
        to networks listed under 'private_visibility_config'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#reverse_lookup GoogleDnsManagedZone#reverse_lookup}
        '''
        result = self._values.get("reverse_lookup")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def service_directory_config(
        self,
    ) -> typing.Optional["GoogleDnsManagedZoneServiceDirectoryConfig"]:
        '''service_directory_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#service_directory_config GoogleDnsManagedZone#service_directory_config}
        '''
        result = self._values.get("service_directory_config")
        return typing.cast(typing.Optional["GoogleDnsManagedZoneServiceDirectoryConfig"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleDnsManagedZoneTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#timeouts GoogleDnsManagedZone#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleDnsManagedZoneTimeouts"], result)

    @builtins.property
    def visibility(self) -> typing.Optional[builtins.str]:
        '''The zone's visibility: public zones are exposed to the Internet, while private zones are visible only to Virtual Private Cloud resources.

        Default value: "public" Possible values: ["private", "public"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#visibility GoogleDnsManagedZone#visibility}
        '''
        result = self._values.get("visibility")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDnsManagedZoneConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDnsManagedZone.GoogleDnsManagedZoneDnssecConfig",
    jsii_struct_bases=[],
    name_mapping={
        "default_key_specs": "defaultKeySpecs",
        "kind": "kind",
        "non_existence": "nonExistence",
        "state": "state",
    },
)
class GoogleDnsManagedZoneDnssecConfig:
    def __init__(
        self,
        *,
        default_key_specs: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDnsManagedZoneDnssecConfigDefaultKeySpecs", typing.Dict[str, typing.Any]]]]] = None,
        kind: typing.Optional[builtins.str] = None,
        non_existence: typing.Optional[builtins.str] = None,
        state: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param default_key_specs: default_key_specs block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#default_key_specs GoogleDnsManagedZone#default_key_specs}
        :param kind: Identifies what kind of resource this is. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#kind GoogleDnsManagedZone#kind}
        :param non_existence: Specifies the mechanism used to provide authenticated denial-of-existence responses. non_existence can only be updated when the state is 'off'. Possible values: ["nsec", "nsec3"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#non_existence GoogleDnsManagedZone#non_existence}
        :param state: Specifies whether DNSSEC is enabled, and what mode it is in Possible values: ["off", "on", "transfer"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#state GoogleDnsManagedZone#state}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDnsManagedZoneDnssecConfig.__init__)
            check_type(argname="argument default_key_specs", value=default_key_specs, expected_type=type_hints["default_key_specs"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
            check_type(argname="argument non_existence", value=non_existence, expected_type=type_hints["non_existence"])
            check_type(argname="argument state", value=state, expected_type=type_hints["state"])
        self._values: typing.Dict[str, typing.Any] = {}
        if default_key_specs is not None:
            self._values["default_key_specs"] = default_key_specs
        if kind is not None:
            self._values["kind"] = kind
        if non_existence is not None:
            self._values["non_existence"] = non_existence
        if state is not None:
            self._values["state"] = state

    @builtins.property
    def default_key_specs(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDnsManagedZoneDnssecConfigDefaultKeySpecs"]]]:
        '''default_key_specs block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#default_key_specs GoogleDnsManagedZone#default_key_specs}
        '''
        result = self._values.get("default_key_specs")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDnsManagedZoneDnssecConfigDefaultKeySpecs"]]], result)

    @builtins.property
    def kind(self) -> typing.Optional[builtins.str]:
        '''Identifies what kind of resource this is.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#kind GoogleDnsManagedZone#kind}
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def non_existence(self) -> typing.Optional[builtins.str]:
        '''Specifies the mechanism used to provide authenticated denial-of-existence responses.

        non_existence can only be updated when the state is 'off'. Possible values: ["nsec", "nsec3"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#non_existence GoogleDnsManagedZone#non_existence}
        '''
        result = self._values.get("non_existence")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def state(self) -> typing.Optional[builtins.str]:
        '''Specifies whether DNSSEC is enabled, and what mode it is in Possible values: ["off", "on", "transfer"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#state GoogleDnsManagedZone#state}
        '''
        result = self._values.get("state")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDnsManagedZoneDnssecConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDnsManagedZone.GoogleDnsManagedZoneDnssecConfigDefaultKeySpecs",
    jsii_struct_bases=[],
    name_mapping={
        "algorithm": "algorithm",
        "key_length": "keyLength",
        "key_type": "keyType",
        "kind": "kind",
    },
)
class GoogleDnsManagedZoneDnssecConfigDefaultKeySpecs:
    def __init__(
        self,
        *,
        algorithm: typing.Optional[builtins.str] = None,
        key_length: typing.Optional[jsii.Number] = None,
        key_type: typing.Optional[builtins.str] = None,
        kind: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param algorithm: String mnemonic specifying the DNSSEC algorithm of this key Possible values: ["ecdsap256sha256", "ecdsap384sha384", "rsasha1", "rsasha256", "rsasha512"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#algorithm GoogleDnsManagedZone#algorithm}
        :param key_length: Length of the keys in bits. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#key_length GoogleDnsManagedZone#key_length}
        :param key_type: Specifies whether this is a key signing key (KSK) or a zone signing key (ZSK). Key signing keys have the Secure Entry Point flag set and, when active, will only be used to sign resource record sets of type DNSKEY. Zone signing keys do not have the Secure Entry Point flag set and will be used to sign all other types of resource record sets. Possible values: ["keySigning", "zoneSigning"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#key_type GoogleDnsManagedZone#key_type}
        :param kind: Identifies what kind of resource this is. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#kind GoogleDnsManagedZone#kind}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDnsManagedZoneDnssecConfigDefaultKeySpecs.__init__)
            check_type(argname="argument algorithm", value=algorithm, expected_type=type_hints["algorithm"])
            check_type(argname="argument key_length", value=key_length, expected_type=type_hints["key_length"])
            check_type(argname="argument key_type", value=key_type, expected_type=type_hints["key_type"])
            check_type(argname="argument kind", value=kind, expected_type=type_hints["kind"])
        self._values: typing.Dict[str, typing.Any] = {}
        if algorithm is not None:
            self._values["algorithm"] = algorithm
        if key_length is not None:
            self._values["key_length"] = key_length
        if key_type is not None:
            self._values["key_type"] = key_type
        if kind is not None:
            self._values["kind"] = kind

    @builtins.property
    def algorithm(self) -> typing.Optional[builtins.str]:
        '''String mnemonic specifying the DNSSEC algorithm of this key Possible values: ["ecdsap256sha256", "ecdsap384sha384", "rsasha1", "rsasha256", "rsasha512"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#algorithm GoogleDnsManagedZone#algorithm}
        '''
        result = self._values.get("algorithm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_length(self) -> typing.Optional[jsii.Number]:
        '''Length of the keys in bits.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#key_length GoogleDnsManagedZone#key_length}
        '''
        result = self._values.get("key_length")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def key_type(self) -> typing.Optional[builtins.str]:
        '''Specifies whether this is a key signing key (KSK) or a zone signing key (ZSK).

        Key signing keys have the Secure Entry
        Point flag set and, when active, will only be used to sign
        resource record sets of type DNSKEY. Zone signing keys do
        not have the Secure Entry Point flag set and will be used
        to sign all other types of resource record sets. Possible values: ["keySigning", "zoneSigning"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#key_type GoogleDnsManagedZone#key_type}
        '''
        result = self._values.get("key_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kind(self) -> typing.Optional[builtins.str]:
        '''Identifies what kind of resource this is.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#kind GoogleDnsManagedZone#kind}
        '''
        result = self._values.get("kind")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDnsManagedZoneDnssecConfigDefaultKeySpecs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDnsManagedZoneDnssecConfigDefaultKeySpecsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDnsManagedZone.GoogleDnsManagedZoneDnssecConfigDefaultKeySpecsList",
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
            type_hints = typing.get_type_hints(GoogleDnsManagedZoneDnssecConfigDefaultKeySpecsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDnsManagedZoneDnssecConfigDefaultKeySpecsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDnsManagedZoneDnssecConfigDefaultKeySpecsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDnsManagedZoneDnssecConfigDefaultKeySpecsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZoneDnssecConfigDefaultKeySpecsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZoneDnssecConfigDefaultKeySpecsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZoneDnssecConfigDefaultKeySpecsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDnsManagedZoneDnssecConfigDefaultKeySpecs]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDnsManagedZoneDnssecConfigDefaultKeySpecs]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDnsManagedZoneDnssecConfigDefaultKeySpecs]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZoneDnssecConfigDefaultKeySpecsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDnsManagedZoneDnssecConfigDefaultKeySpecsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDnsManagedZone.GoogleDnsManagedZoneDnssecConfigDefaultKeySpecsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDnsManagedZoneDnssecConfigDefaultKeySpecsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetAlgorithm")
    def reset_algorithm(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAlgorithm", []))

    @jsii.member(jsii_name="resetKeyLength")
    def reset_key_length(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyLength", []))

    @jsii.member(jsii_name="resetKeyType")
    def reset_key_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyType", []))

    @jsii.member(jsii_name="resetKind")
    def reset_kind(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKind", []))

    @builtins.property
    @jsii.member(jsii_name="algorithmInput")
    def algorithm_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "algorithmInput"))

    @builtins.property
    @jsii.member(jsii_name="keyLengthInput")
    def key_length_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "keyLengthInput"))

    @builtins.property
    @jsii.member(jsii_name="keyTypeInput")
    def key_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="algorithm")
    def algorithm(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "algorithm"))

    @algorithm.setter
    def algorithm(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZoneDnssecConfigDefaultKeySpecsOutputReference, "algorithm").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "algorithm", value)

    @builtins.property
    @jsii.member(jsii_name="keyLength")
    def key_length(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "keyLength"))

    @key_length.setter
    def key_length(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZoneDnssecConfigDefaultKeySpecsOutputReference, "key_length").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyLength", value)

    @builtins.property
    @jsii.member(jsii_name="keyType")
    def key_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyType"))

    @key_type.setter
    def key_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZoneDnssecConfigDefaultKeySpecsOutputReference, "key_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyType", value)

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZoneDnssecConfigDefaultKeySpecsOutputReference, "kind").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDnsManagedZoneDnssecConfigDefaultKeySpecs, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDnsManagedZoneDnssecConfigDefaultKeySpecs, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDnsManagedZoneDnssecConfigDefaultKeySpecs, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZoneDnssecConfigDefaultKeySpecsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDnsManagedZoneDnssecConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDnsManagedZone.GoogleDnsManagedZoneDnssecConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDnsManagedZoneDnssecConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDefaultKeySpecs")
    def put_default_key_specs(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleDnsManagedZoneDnssecConfigDefaultKeySpecs, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDnsManagedZoneDnssecConfigOutputReference.put_default_key_specs)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDefaultKeySpecs", [value]))

    @jsii.member(jsii_name="resetDefaultKeySpecs")
    def reset_default_key_specs(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultKeySpecs", []))

    @jsii.member(jsii_name="resetKind")
    def reset_kind(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKind", []))

    @jsii.member(jsii_name="resetNonExistence")
    def reset_non_existence(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNonExistence", []))

    @jsii.member(jsii_name="resetState")
    def reset_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetState", []))

    @builtins.property
    @jsii.member(jsii_name="defaultKeySpecs")
    def default_key_specs(self) -> GoogleDnsManagedZoneDnssecConfigDefaultKeySpecsList:
        return typing.cast(GoogleDnsManagedZoneDnssecConfigDefaultKeySpecsList, jsii.get(self, "defaultKeySpecs"))

    @builtins.property
    @jsii.member(jsii_name="defaultKeySpecsInput")
    def default_key_specs_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDnsManagedZoneDnssecConfigDefaultKeySpecs]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDnsManagedZoneDnssecConfigDefaultKeySpecs]]], jsii.get(self, "defaultKeySpecsInput"))

    @builtins.property
    @jsii.member(jsii_name="kindInput")
    def kind_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kindInput"))

    @builtins.property
    @jsii.member(jsii_name="nonExistenceInput")
    def non_existence_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nonExistenceInput"))

    @builtins.property
    @jsii.member(jsii_name="stateInput")
    def state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stateInput"))

    @builtins.property
    @jsii.member(jsii_name="kind")
    def kind(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kind"))

    @kind.setter
    def kind(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZoneDnssecConfigOutputReference, "kind").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kind", value)

    @builtins.property
    @jsii.member(jsii_name="nonExistence")
    def non_existence(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nonExistence"))

    @non_existence.setter
    def non_existence(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZoneDnssecConfigOutputReference, "non_existence").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nonExistence", value)

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @state.setter
    def state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZoneDnssecConfigOutputReference, "state").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "state", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleDnsManagedZoneDnssecConfig]:
        return typing.cast(typing.Optional[GoogleDnsManagedZoneDnssecConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDnsManagedZoneDnssecConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZoneDnssecConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDnsManagedZone.GoogleDnsManagedZoneForwardingConfig",
    jsii_struct_bases=[],
    name_mapping={"target_name_servers": "targetNameServers"},
)
class GoogleDnsManagedZoneForwardingConfig:
    def __init__(
        self,
        *,
        target_name_servers: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDnsManagedZoneForwardingConfigTargetNameServers", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param target_name_servers: target_name_servers block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#target_name_servers GoogleDnsManagedZone#target_name_servers}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDnsManagedZoneForwardingConfig.__init__)
            check_type(argname="argument target_name_servers", value=target_name_servers, expected_type=type_hints["target_name_servers"])
        self._values: typing.Dict[str, typing.Any] = {
            "target_name_servers": target_name_servers,
        }

    @builtins.property
    def target_name_servers(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["GoogleDnsManagedZoneForwardingConfigTargetNameServers"]]:
        '''target_name_servers block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#target_name_servers GoogleDnsManagedZone#target_name_servers}
        '''
        result = self._values.get("target_name_servers")
        assert result is not None, "Required property 'target_name_servers' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["GoogleDnsManagedZoneForwardingConfigTargetNameServers"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDnsManagedZoneForwardingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDnsManagedZoneForwardingConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDnsManagedZone.GoogleDnsManagedZoneForwardingConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDnsManagedZoneForwardingConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTargetNameServers")
    def put_target_name_servers(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDnsManagedZoneForwardingConfigTargetNameServers", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDnsManagedZoneForwardingConfigOutputReference.put_target_name_servers)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putTargetNameServers", [value]))

    @builtins.property
    @jsii.member(jsii_name="targetNameServers")
    def target_name_servers(
        self,
    ) -> "GoogleDnsManagedZoneForwardingConfigTargetNameServersList":
        return typing.cast("GoogleDnsManagedZoneForwardingConfigTargetNameServersList", jsii.get(self, "targetNameServers"))

    @builtins.property
    @jsii.member(jsii_name="targetNameServersInput")
    def target_name_servers_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDnsManagedZoneForwardingConfigTargetNameServers"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleDnsManagedZoneForwardingConfigTargetNameServers"]]], jsii.get(self, "targetNameServersInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleDnsManagedZoneForwardingConfig]:
        return typing.cast(typing.Optional[GoogleDnsManagedZoneForwardingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDnsManagedZoneForwardingConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZoneForwardingConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDnsManagedZone.GoogleDnsManagedZoneForwardingConfigTargetNameServers",
    jsii_struct_bases=[],
    name_mapping={"ipv4_address": "ipv4Address", "forwarding_path": "forwardingPath"},
)
class GoogleDnsManagedZoneForwardingConfigTargetNameServers:
    def __init__(
        self,
        *,
        ipv4_address: builtins.str,
        forwarding_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param ipv4_address: IPv4 address of a target name server. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#ipv4_address GoogleDnsManagedZone#ipv4_address}
        :param forwarding_path: Forwarding path for this TargetNameServer. If unset or 'default' Cloud DNS will make forwarding decision based on address ranges, i.e. RFC1918 addresses go to the VPC, Non-RFC1918 addresses go to the Internet. When set to 'private', Cloud DNS will always send queries through VPC for this target Possible values: ["default", "private"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#forwarding_path GoogleDnsManagedZone#forwarding_path}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDnsManagedZoneForwardingConfigTargetNameServers.__init__)
            check_type(argname="argument ipv4_address", value=ipv4_address, expected_type=type_hints["ipv4_address"])
            check_type(argname="argument forwarding_path", value=forwarding_path, expected_type=type_hints["forwarding_path"])
        self._values: typing.Dict[str, typing.Any] = {
            "ipv4_address": ipv4_address,
        }
        if forwarding_path is not None:
            self._values["forwarding_path"] = forwarding_path

    @builtins.property
    def ipv4_address(self) -> builtins.str:
        '''IPv4 address of a target name server.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#ipv4_address GoogleDnsManagedZone#ipv4_address}
        '''
        result = self._values.get("ipv4_address")
        assert result is not None, "Required property 'ipv4_address' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def forwarding_path(self) -> typing.Optional[builtins.str]:
        '''Forwarding path for this TargetNameServer.

        If unset or 'default' Cloud DNS will make forwarding
        decision based on address ranges, i.e. RFC1918 addresses go to the VPC, Non-RFC1918 addresses go
        to the Internet. When set to 'private', Cloud DNS will always send queries through VPC for this target Possible values: ["default", "private"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#forwarding_path GoogleDnsManagedZone#forwarding_path}
        '''
        result = self._values.get("forwarding_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDnsManagedZoneForwardingConfigTargetNameServers(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDnsManagedZoneForwardingConfigTargetNameServersList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDnsManagedZone.GoogleDnsManagedZoneForwardingConfigTargetNameServersList",
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
            type_hints = typing.get_type_hints(GoogleDnsManagedZoneForwardingConfigTargetNameServersList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDnsManagedZoneForwardingConfigTargetNameServersOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDnsManagedZoneForwardingConfigTargetNameServersList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDnsManagedZoneForwardingConfigTargetNameServersOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZoneForwardingConfigTargetNameServersList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZoneForwardingConfigTargetNameServersList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZoneForwardingConfigTargetNameServersList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDnsManagedZoneForwardingConfigTargetNameServers]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDnsManagedZoneForwardingConfigTargetNameServers]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDnsManagedZoneForwardingConfigTargetNameServers]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZoneForwardingConfigTargetNameServersList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDnsManagedZoneForwardingConfigTargetNameServersOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDnsManagedZone.GoogleDnsManagedZoneForwardingConfigTargetNameServersOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDnsManagedZoneForwardingConfigTargetNameServersOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetForwardingPath")
    def reset_forwarding_path(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForwardingPath", []))

    @builtins.property
    @jsii.member(jsii_name="forwardingPathInput")
    def forwarding_path_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "forwardingPathInput"))

    @builtins.property
    @jsii.member(jsii_name="ipv4AddressInput")
    def ipv4_address_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipv4AddressInput"))

    @builtins.property
    @jsii.member(jsii_name="forwardingPath")
    def forwarding_path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "forwardingPath"))

    @forwarding_path.setter
    def forwarding_path(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZoneForwardingConfigTargetNameServersOutputReference, "forwarding_path").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forwardingPath", value)

    @builtins.property
    @jsii.member(jsii_name="ipv4Address")
    def ipv4_address(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "ipv4Address"))

    @ipv4_address.setter
    def ipv4_address(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZoneForwardingConfigTargetNameServersOutputReference, "ipv4_address").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipv4Address", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDnsManagedZoneForwardingConfigTargetNameServers, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDnsManagedZoneForwardingConfigTargetNameServers, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDnsManagedZoneForwardingConfigTargetNameServers, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZoneForwardingConfigTargetNameServersOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDnsManagedZone.GoogleDnsManagedZonePeeringConfig",
    jsii_struct_bases=[],
    name_mapping={"target_network": "targetNetwork"},
)
class GoogleDnsManagedZonePeeringConfig:
    def __init__(
        self,
        *,
        target_network: typing.Union["GoogleDnsManagedZonePeeringConfigTargetNetwork", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param target_network: target_network block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#target_network GoogleDnsManagedZone#target_network}
        '''
        if isinstance(target_network, dict):
            target_network = GoogleDnsManagedZonePeeringConfigTargetNetwork(**target_network)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDnsManagedZonePeeringConfig.__init__)
            check_type(argname="argument target_network", value=target_network, expected_type=type_hints["target_network"])
        self._values: typing.Dict[str, typing.Any] = {
            "target_network": target_network,
        }

    @builtins.property
    def target_network(self) -> "GoogleDnsManagedZonePeeringConfigTargetNetwork":
        '''target_network block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#target_network GoogleDnsManagedZone#target_network}
        '''
        result = self._values.get("target_network")
        assert result is not None, "Required property 'target_network' is missing"
        return typing.cast("GoogleDnsManagedZonePeeringConfigTargetNetwork", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDnsManagedZonePeeringConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDnsManagedZonePeeringConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDnsManagedZone.GoogleDnsManagedZonePeeringConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDnsManagedZonePeeringConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putTargetNetwork")
    def put_target_network(self, *, network_url: builtins.str) -> None:
        '''
        :param network_url: The id or fully qualified URL of the VPC network to forward queries to. This should be formatted like 'projects/{project}/global/networks/{network}' or 'https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#network_url GoogleDnsManagedZone#network_url}
        '''
        value = GoogleDnsManagedZonePeeringConfigTargetNetwork(network_url=network_url)

        return typing.cast(None, jsii.invoke(self, "putTargetNetwork", [value]))

    @builtins.property
    @jsii.member(jsii_name="targetNetwork")
    def target_network(
        self,
    ) -> "GoogleDnsManagedZonePeeringConfigTargetNetworkOutputReference":
        return typing.cast("GoogleDnsManagedZonePeeringConfigTargetNetworkOutputReference", jsii.get(self, "targetNetwork"))

    @builtins.property
    @jsii.member(jsii_name="targetNetworkInput")
    def target_network_input(
        self,
    ) -> typing.Optional["GoogleDnsManagedZonePeeringConfigTargetNetwork"]:
        return typing.cast(typing.Optional["GoogleDnsManagedZonePeeringConfigTargetNetwork"], jsii.get(self, "targetNetworkInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleDnsManagedZonePeeringConfig]:
        return typing.cast(typing.Optional[GoogleDnsManagedZonePeeringConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDnsManagedZonePeeringConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZonePeeringConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDnsManagedZone.GoogleDnsManagedZonePeeringConfigTargetNetwork",
    jsii_struct_bases=[],
    name_mapping={"network_url": "networkUrl"},
)
class GoogleDnsManagedZonePeeringConfigTargetNetwork:
    def __init__(self, *, network_url: builtins.str) -> None:
        '''
        :param network_url: The id or fully qualified URL of the VPC network to forward queries to. This should be formatted like 'projects/{project}/global/networks/{network}' or 'https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#network_url GoogleDnsManagedZone#network_url}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDnsManagedZonePeeringConfigTargetNetwork.__init__)
            check_type(argname="argument network_url", value=network_url, expected_type=type_hints["network_url"])
        self._values: typing.Dict[str, typing.Any] = {
            "network_url": network_url,
        }

    @builtins.property
    def network_url(self) -> builtins.str:
        '''The id or fully qualified URL of the VPC network to forward queries to.

        This should be formatted like 'projects/{project}/global/networks/{network}' or
        'https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}'

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#network_url GoogleDnsManagedZone#network_url}
        '''
        result = self._values.get("network_url")
        assert result is not None, "Required property 'network_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDnsManagedZonePeeringConfigTargetNetwork(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDnsManagedZonePeeringConfigTargetNetworkOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDnsManagedZone.GoogleDnsManagedZonePeeringConfigTargetNetworkOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDnsManagedZonePeeringConfigTargetNetworkOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="networkUrlInput")
    def network_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="networkUrl")
    def network_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkUrl"))

    @network_url.setter
    def network_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZonePeeringConfigTargetNetworkOutputReference, "network_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDnsManagedZonePeeringConfigTargetNetwork]:
        return typing.cast(typing.Optional[GoogleDnsManagedZonePeeringConfigTargetNetwork], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDnsManagedZonePeeringConfigTargetNetwork],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZonePeeringConfigTargetNetworkOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDnsManagedZone.GoogleDnsManagedZonePrivateVisibilityConfig",
    jsii_struct_bases=[],
    name_mapping={"networks": "networks"},
)
class GoogleDnsManagedZonePrivateVisibilityConfig:
    def __init__(
        self,
        *,
        networks: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleDnsManagedZonePrivateVisibilityConfigNetworks", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param networks: networks block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#networks GoogleDnsManagedZone#networks}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDnsManagedZonePrivateVisibilityConfig.__init__)
            check_type(argname="argument networks", value=networks, expected_type=type_hints["networks"])
        self._values: typing.Dict[str, typing.Any] = {
            "networks": networks,
        }

    @builtins.property
    def networks(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["GoogleDnsManagedZonePrivateVisibilityConfigNetworks"]]:
        '''networks block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#networks GoogleDnsManagedZone#networks}
        '''
        result = self._values.get("networks")
        assert result is not None, "Required property 'networks' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["GoogleDnsManagedZonePrivateVisibilityConfigNetworks"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDnsManagedZonePrivateVisibilityConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDnsManagedZone.GoogleDnsManagedZonePrivateVisibilityConfigNetworks",
    jsii_struct_bases=[],
    name_mapping={"network_url": "networkUrl"},
)
class GoogleDnsManagedZonePrivateVisibilityConfigNetworks:
    def __init__(self, *, network_url: builtins.str) -> None:
        '''
        :param network_url: The id or fully qualified URL of the VPC network to bind to. This should be formatted like 'projects/{project}/global/networks/{network}' or 'https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#network_url GoogleDnsManagedZone#network_url}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDnsManagedZonePrivateVisibilityConfigNetworks.__init__)
            check_type(argname="argument network_url", value=network_url, expected_type=type_hints["network_url"])
        self._values: typing.Dict[str, typing.Any] = {
            "network_url": network_url,
        }

    @builtins.property
    def network_url(self) -> builtins.str:
        '''The id or fully qualified URL of the VPC network to bind to. This should be formatted like 'projects/{project}/global/networks/{network}' or 'https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#network_url GoogleDnsManagedZone#network_url}
        '''
        result = self._values.get("network_url")
        assert result is not None, "Required property 'network_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDnsManagedZonePrivateVisibilityConfigNetworks(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDnsManagedZonePrivateVisibilityConfigNetworksList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDnsManagedZone.GoogleDnsManagedZonePrivateVisibilityConfigNetworksList",
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
            type_hints = typing.get_type_hints(GoogleDnsManagedZonePrivateVisibilityConfigNetworksList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleDnsManagedZonePrivateVisibilityConfigNetworksOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDnsManagedZonePrivateVisibilityConfigNetworksList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDnsManagedZonePrivateVisibilityConfigNetworksOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZonePrivateVisibilityConfigNetworksList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZonePrivateVisibilityConfigNetworksList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZonePrivateVisibilityConfigNetworksList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDnsManagedZonePrivateVisibilityConfigNetworks]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDnsManagedZonePrivateVisibilityConfigNetworks]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDnsManagedZonePrivateVisibilityConfigNetworks]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZonePrivateVisibilityConfigNetworksList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDnsManagedZonePrivateVisibilityConfigNetworksOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDnsManagedZone.GoogleDnsManagedZonePrivateVisibilityConfigNetworksOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDnsManagedZonePrivateVisibilityConfigNetworksOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="networkUrlInput")
    def network_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="networkUrl")
    def network_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "networkUrl"))

    @network_url.setter
    def network_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZonePrivateVisibilityConfigNetworksOutputReference, "network_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDnsManagedZonePrivateVisibilityConfigNetworks, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDnsManagedZonePrivateVisibilityConfigNetworks, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDnsManagedZonePrivateVisibilityConfigNetworks, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZonePrivateVisibilityConfigNetworksOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDnsManagedZonePrivateVisibilityConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDnsManagedZone.GoogleDnsManagedZonePrivateVisibilityConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDnsManagedZonePrivateVisibilityConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putNetworks")
    def put_networks(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleDnsManagedZonePrivateVisibilityConfigNetworks, typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDnsManagedZonePrivateVisibilityConfigOutputReference.put_networks)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putNetworks", [value]))

    @builtins.property
    @jsii.member(jsii_name="networks")
    def networks(self) -> GoogleDnsManagedZonePrivateVisibilityConfigNetworksList:
        return typing.cast(GoogleDnsManagedZonePrivateVisibilityConfigNetworksList, jsii.get(self, "networks"))

    @builtins.property
    @jsii.member(jsii_name="networksInput")
    def networks_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDnsManagedZonePrivateVisibilityConfigNetworks]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleDnsManagedZonePrivateVisibilityConfigNetworks]]], jsii.get(self, "networksInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDnsManagedZonePrivateVisibilityConfig]:
        return typing.cast(typing.Optional[GoogleDnsManagedZonePrivateVisibilityConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDnsManagedZonePrivateVisibilityConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZonePrivateVisibilityConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDnsManagedZone.GoogleDnsManagedZoneServiceDirectoryConfig",
    jsii_struct_bases=[],
    name_mapping={"namespace": "namespace"},
)
class GoogleDnsManagedZoneServiceDirectoryConfig:
    def __init__(
        self,
        *,
        namespace: typing.Union["GoogleDnsManagedZoneServiceDirectoryConfigNamespace", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param namespace: namespace block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#namespace GoogleDnsManagedZone#namespace}
        '''
        if isinstance(namespace, dict):
            namespace = GoogleDnsManagedZoneServiceDirectoryConfigNamespace(**namespace)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDnsManagedZoneServiceDirectoryConfig.__init__)
            check_type(argname="argument namespace", value=namespace, expected_type=type_hints["namespace"])
        self._values: typing.Dict[str, typing.Any] = {
            "namespace": namespace,
        }

    @builtins.property
    def namespace(self) -> "GoogleDnsManagedZoneServiceDirectoryConfigNamespace":
        '''namespace block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#namespace GoogleDnsManagedZone#namespace}
        '''
        result = self._values.get("namespace")
        assert result is not None, "Required property 'namespace' is missing"
        return typing.cast("GoogleDnsManagedZoneServiceDirectoryConfigNamespace", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDnsManagedZoneServiceDirectoryConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDnsManagedZone.GoogleDnsManagedZoneServiceDirectoryConfigNamespace",
    jsii_struct_bases=[],
    name_mapping={"namespace_url": "namespaceUrl"},
)
class GoogleDnsManagedZoneServiceDirectoryConfigNamespace:
    def __init__(self, *, namespace_url: builtins.str) -> None:
        '''
        :param namespace_url: The fully qualified or partial URL of the service directory namespace that should be associated with the zone. This should be formatted like 'https://servicedirectory.googleapis.com/v1/projects/{project}/locations/{location}/namespaces/{namespace_id}' or simply 'projects/{project}/locations/{location}/namespaces/{namespace_id}' Ignored for 'public' visibility zones. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#namespace_url GoogleDnsManagedZone#namespace_url}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDnsManagedZoneServiceDirectoryConfigNamespace.__init__)
            check_type(argname="argument namespace_url", value=namespace_url, expected_type=type_hints["namespace_url"])
        self._values: typing.Dict[str, typing.Any] = {
            "namespace_url": namespace_url,
        }

    @builtins.property
    def namespace_url(self) -> builtins.str:
        '''The fully qualified or partial URL of the service directory namespace that should be associated with the zone.

        This should be formatted like
        'https://servicedirectory.googleapis.com/v1/projects/{project}/locations/{location}/namespaces/{namespace_id}'
        or simply 'projects/{project}/locations/{location}/namespaces/{namespace_id}'
        Ignored for 'public' visibility zones.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#namespace_url GoogleDnsManagedZone#namespace_url}
        '''
        result = self._values.get("namespace_url")
        assert result is not None, "Required property 'namespace_url' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDnsManagedZoneServiceDirectoryConfigNamespace(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDnsManagedZoneServiceDirectoryConfigNamespaceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDnsManagedZone.GoogleDnsManagedZoneServiceDirectoryConfigNamespaceOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDnsManagedZoneServiceDirectoryConfigNamespaceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="namespaceUrlInput")
    def namespace_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "namespaceUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="namespaceUrl")
    def namespace_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "namespaceUrl"))

    @namespace_url.setter
    def namespace_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZoneServiceDirectoryConfigNamespaceOutputReference, "namespace_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "namespaceUrl", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDnsManagedZoneServiceDirectoryConfigNamespace]:
        return typing.cast(typing.Optional[GoogleDnsManagedZoneServiceDirectoryConfigNamespace], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDnsManagedZoneServiceDirectoryConfigNamespace],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZoneServiceDirectoryConfigNamespaceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDnsManagedZoneServiceDirectoryConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDnsManagedZone.GoogleDnsManagedZoneServiceDirectoryConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDnsManagedZoneServiceDirectoryConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putNamespace")
    def put_namespace(self, *, namespace_url: builtins.str) -> None:
        '''
        :param namespace_url: The fully qualified or partial URL of the service directory namespace that should be associated with the zone. This should be formatted like 'https://servicedirectory.googleapis.com/v1/projects/{project}/locations/{location}/namespaces/{namespace_id}' or simply 'projects/{project}/locations/{location}/namespaces/{namespace_id}' Ignored for 'public' visibility zones. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#namespace_url GoogleDnsManagedZone#namespace_url}
        '''
        value = GoogleDnsManagedZoneServiceDirectoryConfigNamespace(
            namespace_url=namespace_url
        )

        return typing.cast(None, jsii.invoke(self, "putNamespace", [value]))

    @builtins.property
    @jsii.member(jsii_name="namespace")
    def namespace(
        self,
    ) -> GoogleDnsManagedZoneServiceDirectoryConfigNamespaceOutputReference:
        return typing.cast(GoogleDnsManagedZoneServiceDirectoryConfigNamespaceOutputReference, jsii.get(self, "namespace"))

    @builtins.property
    @jsii.member(jsii_name="namespaceInput")
    def namespace_input(
        self,
    ) -> typing.Optional[GoogleDnsManagedZoneServiceDirectoryConfigNamespace]:
        return typing.cast(typing.Optional[GoogleDnsManagedZoneServiceDirectoryConfigNamespace], jsii.get(self, "namespaceInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDnsManagedZoneServiceDirectoryConfig]:
        return typing.cast(typing.Optional[GoogleDnsManagedZoneServiceDirectoryConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDnsManagedZoneServiceDirectoryConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZoneServiceDirectoryConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDnsManagedZone.GoogleDnsManagedZoneTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleDnsManagedZoneTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#create GoogleDnsManagedZone#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#delete GoogleDnsManagedZone#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#update GoogleDnsManagedZone#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDnsManagedZoneTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#create GoogleDnsManagedZone#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#delete GoogleDnsManagedZone#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dns_managed_zone#update GoogleDnsManagedZone#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDnsManagedZoneTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDnsManagedZoneTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDnsManagedZone.GoogleDnsManagedZoneTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDnsManagedZoneTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

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
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZoneTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZoneTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZoneTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDnsManagedZoneTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDnsManagedZoneTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDnsManagedZoneTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDnsManagedZoneTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleDnsManagedZone",
    "GoogleDnsManagedZoneCloudLoggingConfig",
    "GoogleDnsManagedZoneCloudLoggingConfigOutputReference",
    "GoogleDnsManagedZoneConfig",
    "GoogleDnsManagedZoneDnssecConfig",
    "GoogleDnsManagedZoneDnssecConfigDefaultKeySpecs",
    "GoogleDnsManagedZoneDnssecConfigDefaultKeySpecsList",
    "GoogleDnsManagedZoneDnssecConfigDefaultKeySpecsOutputReference",
    "GoogleDnsManagedZoneDnssecConfigOutputReference",
    "GoogleDnsManagedZoneForwardingConfig",
    "GoogleDnsManagedZoneForwardingConfigOutputReference",
    "GoogleDnsManagedZoneForwardingConfigTargetNameServers",
    "GoogleDnsManagedZoneForwardingConfigTargetNameServersList",
    "GoogleDnsManagedZoneForwardingConfigTargetNameServersOutputReference",
    "GoogleDnsManagedZonePeeringConfig",
    "GoogleDnsManagedZonePeeringConfigOutputReference",
    "GoogleDnsManagedZonePeeringConfigTargetNetwork",
    "GoogleDnsManagedZonePeeringConfigTargetNetworkOutputReference",
    "GoogleDnsManagedZonePrivateVisibilityConfig",
    "GoogleDnsManagedZonePrivateVisibilityConfigNetworks",
    "GoogleDnsManagedZonePrivateVisibilityConfigNetworksList",
    "GoogleDnsManagedZonePrivateVisibilityConfigNetworksOutputReference",
    "GoogleDnsManagedZonePrivateVisibilityConfigOutputReference",
    "GoogleDnsManagedZoneServiceDirectoryConfig",
    "GoogleDnsManagedZoneServiceDirectoryConfigNamespace",
    "GoogleDnsManagedZoneServiceDirectoryConfigNamespaceOutputReference",
    "GoogleDnsManagedZoneServiceDirectoryConfigOutputReference",
    "GoogleDnsManagedZoneTimeouts",
    "GoogleDnsManagedZoneTimeoutsOutputReference",
]

publication.publish()
