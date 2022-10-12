'''
# `google_compute_firewall`

Refer to the Terraform Registory for docs: [`google_compute_firewall`](https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall).
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


class GoogleComputeFirewall(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeFirewall.GoogleComputeFirewall",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall google_compute_firewall}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        network: builtins.str,
        allow: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeFirewallAllow", typing.Dict[str, typing.Any]]]]] = None,
        deny: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeFirewallDeny", typing.Dict[str, typing.Any]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        destination_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
        direction: typing.Optional[builtins.str] = None,
        disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_logging: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        log_config: typing.Optional[typing.Union["GoogleComputeFirewallLogConfig", typing.Dict[str, typing.Any]]] = None,
        priority: typing.Optional[jsii.Number] = None,
        project: typing.Optional[builtins.str] = None,
        source_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_service_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        target_service_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
        target_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeFirewallTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall google_compute_firewall} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#name GoogleComputeFirewall#name}
        :param network: The name or self_link of the network to attach this firewall to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#network GoogleComputeFirewall#network}
        :param allow: allow block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#allow GoogleComputeFirewall#allow}
        :param deny: deny block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#deny GoogleComputeFirewall#deny}
        :param description: An optional description of this resource. Provide this property when you create the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#description GoogleComputeFirewall#description}
        :param destination_ranges: If destination ranges are specified, the firewall will apply only to traffic that has destination IP address in these ranges. These ranges must be expressed in CIDR format. Only IPv4 is supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#destination_ranges GoogleComputeFirewall#destination_ranges}
        :param direction: Direction of traffic to which this firewall applies; default is INGRESS. Note: For INGRESS traffic, it is NOT supported to specify destinationRanges; For EGRESS traffic, it is NOT supported to specify 'source_ranges' OR 'source_tags'. For INGRESS traffic, one of 'source_ranges', 'source_tags' or 'source_service_accounts' is required. Possible values: ["INGRESS", "EGRESS"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#direction GoogleComputeFirewall#direction}
        :param disabled: Denotes whether the firewall rule is disabled, i.e not applied to the network it is associated with. When set to true, the firewall rule is not enforced and the network behaves as if it did not exist. If this is unspecified, the firewall rule will be enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#disabled GoogleComputeFirewall#disabled}
        :param enable_logging: This field denotes whether to enable logging for a particular firewall rule. If logging is enabled, logs will be exported to Stackdriver. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#enable_logging GoogleComputeFirewall#enable_logging}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#id GoogleComputeFirewall#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param log_config: log_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#log_config GoogleComputeFirewall#log_config}
        :param priority: Priority for this rule. This is an integer between 0 and 65535, both inclusive. When not specified, the value assumed is 1000. Relative priorities determine precedence of conflicting rules. Lower value of priority implies higher precedence (eg, a rule with priority 0 has higher precedence than a rule with priority 1). DENY rules take precedence over ALLOW rules having equal priority. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#priority GoogleComputeFirewall#priority}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#project GoogleComputeFirewall#project}.
        :param source_ranges: If source ranges are specified, the firewall will apply only to traffic that has source IP address in these ranges. These ranges must be expressed in CIDR format. One or both of sourceRanges and sourceTags may be set. If both properties are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP that belongs to a tag listed in the sourceTags property. The connection does not need to match both properties for the firewall to apply. Only IPv4 is supported. For INGRESS traffic, one of 'source_ranges', 'source_tags' or 'source_service_accounts' is required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#source_ranges GoogleComputeFirewall#source_ranges}
        :param source_service_accounts: If source service accounts are specified, the firewall will apply only to traffic originating from an instance with a service account in this list. Source service accounts cannot be used to control traffic to an instance's external IP address because service accounts are associated with an instance, not an IP address. sourceRanges can be set at the same time as sourceServiceAccounts. If both are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP belongs to an instance with service account listed in sourceServiceAccount. The connection does not need to match both properties for the firewall to apply. sourceServiceAccounts cannot be used at the same time as sourceTags or targetTags. For INGRESS traffic, one of 'source_ranges', 'source_tags' or 'source_service_accounts' is required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#source_service_accounts GoogleComputeFirewall#source_service_accounts}
        :param source_tags: If source tags are specified, the firewall will apply only to traffic with source IP that belongs to a tag listed in source tags. Source tags cannot be used to control traffic to an instance's external IP address. Because tags are associated with an instance, not an IP address. One or both of sourceRanges and sourceTags may be set. If both properties are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP that belongs to a tag listed in the sourceTags property. The connection does not need to match both properties for the firewall to apply. For INGRESS traffic, one of 'source_ranges', 'source_tags' or 'source_service_accounts' is required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#source_tags GoogleComputeFirewall#source_tags}
        :param target_service_accounts: A list of service accounts indicating sets of instances located in the network that may make network connections as specified in allowed[]. targetServiceAccounts cannot be used at the same time as targetTags or sourceTags. If neither targetServiceAccounts nor targetTags are specified, the firewall rule applies to all instances on the specified network. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#target_service_accounts GoogleComputeFirewall#target_service_accounts}
        :param target_tags: A list of instance tags indicating sets of instances located in the network that may make network connections as specified in allowed[]. If no targetTags are specified, the firewall rule applies to all instances on the specified network. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#target_tags GoogleComputeFirewall#target_tags}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#timeouts GoogleComputeFirewall#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeFirewall.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleComputeFirewallConfig(
            name=name,
            network=network,
            allow=allow,
            deny=deny,
            description=description,
            destination_ranges=destination_ranges,
            direction=direction,
            disabled=disabled,
            enable_logging=enable_logging,
            id=id,
            log_config=log_config,
            priority=priority,
            project=project,
            source_ranges=source_ranges,
            source_service_accounts=source_service_accounts,
            source_tags=source_tags,
            target_service_accounts=target_service_accounts,
            target_tags=target_tags,
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

    @jsii.member(jsii_name="putAllow")
    def put_allow(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeFirewallAllow", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeFirewall.put_allow)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putAllow", [value]))

    @jsii.member(jsii_name="putDeny")
    def put_deny(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeFirewallDeny", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeFirewall.put_deny)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putDeny", [value]))

    @jsii.member(jsii_name="putLogConfig")
    def put_log_config(self, *, metadata: builtins.str) -> None:
        '''
        :param metadata: This field denotes whether to include or exclude metadata for firewall logs. Possible values: ["EXCLUDE_ALL_METADATA", "INCLUDE_ALL_METADATA"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#metadata GoogleComputeFirewall#metadata}
        '''
        value = GoogleComputeFirewallLogConfig(metadata=metadata)

        return typing.cast(None, jsii.invoke(self, "putLogConfig", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#create GoogleComputeFirewall#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#delete GoogleComputeFirewall#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#update GoogleComputeFirewall#update}.
        '''
        value = GoogleComputeFirewallTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAllow")
    def reset_allow(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllow", []))

    @jsii.member(jsii_name="resetDeny")
    def reset_deny(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeny", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetDestinationRanges")
    def reset_destination_ranges(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationRanges", []))

    @jsii.member(jsii_name="resetDirection")
    def reset_direction(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDirection", []))

    @jsii.member(jsii_name="resetDisabled")
    def reset_disabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDisabled", []))

    @jsii.member(jsii_name="resetEnableLogging")
    def reset_enable_logging(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableLogging", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLogConfig")
    def reset_log_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogConfig", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetSourceRanges")
    def reset_source_ranges(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceRanges", []))

    @jsii.member(jsii_name="resetSourceServiceAccounts")
    def reset_source_service_accounts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceServiceAccounts", []))

    @jsii.member(jsii_name="resetSourceTags")
    def reset_source_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceTags", []))

    @jsii.member(jsii_name="resetTargetServiceAccounts")
    def reset_target_service_accounts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetServiceAccounts", []))

    @jsii.member(jsii_name="resetTargetTags")
    def reset_target_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTargetTags", []))

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
    @jsii.member(jsii_name="allow")
    def allow(self) -> "GoogleComputeFirewallAllowList":
        return typing.cast("GoogleComputeFirewallAllowList", jsii.get(self, "allow"))

    @builtins.property
    @jsii.member(jsii_name="creationTimestamp")
    def creation_timestamp(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "creationTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="deny")
    def deny(self) -> "GoogleComputeFirewallDenyList":
        return typing.cast("GoogleComputeFirewallDenyList", jsii.get(self, "deny"))

    @builtins.property
    @jsii.member(jsii_name="logConfig")
    def log_config(self) -> "GoogleComputeFirewallLogConfigOutputReference":
        return typing.cast("GoogleComputeFirewallLogConfigOutputReference", jsii.get(self, "logConfig"))

    @builtins.property
    @jsii.member(jsii_name="selfLink")
    def self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfLink"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleComputeFirewallTimeoutsOutputReference":
        return typing.cast("GoogleComputeFirewallTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="allowInput")
    def allow_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeFirewallAllow"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeFirewallAllow"]]], jsii.get(self, "allowInput"))

    @builtins.property
    @jsii.member(jsii_name="denyInput")
    def deny_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeFirewallDeny"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeFirewallDeny"]]], jsii.get(self, "denyInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationRangesInput")
    def destination_ranges_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "destinationRangesInput"))

    @builtins.property
    @jsii.member(jsii_name="directionInput")
    def direction_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "directionInput"))

    @builtins.property
    @jsii.member(jsii_name="disabledInput")
    def disabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "disabledInput"))

    @builtins.property
    @jsii.member(jsii_name="enableLoggingInput")
    def enable_logging_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableLoggingInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="logConfigInput")
    def log_config_input(self) -> typing.Optional["GoogleComputeFirewallLogConfig"]:
        return typing.cast(typing.Optional["GoogleComputeFirewallLogConfig"], jsii.get(self, "logConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="networkInput")
    def network_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceRangesInput")
    def source_ranges_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourceRangesInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceServiceAccountsInput")
    def source_service_accounts_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourceServiceAccountsInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceTagsInput")
    def source_tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourceTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="targetServiceAccountsInput")
    def target_service_accounts_input(
        self,
    ) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "targetServiceAccountsInput"))

    @builtins.property
    @jsii.member(jsii_name="targetTagsInput")
    def target_tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "targetTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleComputeFirewallTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleComputeFirewallTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewall, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="destinationRanges")
    def destination_ranges(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "destinationRanges"))

    @destination_ranges.setter
    def destination_ranges(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewall, "destination_ranges").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationRanges", value)

    @builtins.property
    @jsii.member(jsii_name="direction")
    def direction(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "direction"))

    @direction.setter
    def direction(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewall, "direction").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "direction", value)

    @builtins.property
    @jsii.member(jsii_name="disabled")
    def disabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "disabled"))

    @disabled.setter
    def disabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewall, "disabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disabled", value)

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
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewall, "enable_logging").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableLogging", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewall, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewall, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="network")
    def network(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "network"))

    @network.setter
    def network(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewall, "network").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "network", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewall, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewall, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="sourceRanges")
    def source_ranges(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourceRanges"))

    @source_ranges.setter
    def source_ranges(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewall, "source_ranges").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceRanges", value)

    @builtins.property
    @jsii.member(jsii_name="sourceServiceAccounts")
    def source_service_accounts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourceServiceAccounts"))

    @source_service_accounts.setter
    def source_service_accounts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewall, "source_service_accounts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceServiceAccounts", value)

    @builtins.property
    @jsii.member(jsii_name="sourceTags")
    def source_tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourceTags"))

    @source_tags.setter
    def source_tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewall, "source_tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceTags", value)

    @builtins.property
    @jsii.member(jsii_name="targetServiceAccounts")
    def target_service_accounts(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "targetServiceAccounts"))

    @target_service_accounts.setter
    def target_service_accounts(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewall, "target_service_accounts").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetServiceAccounts", value)

    @builtins.property
    @jsii.member(jsii_name="targetTags")
    def target_tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "targetTags"))

    @target_tags.setter
    def target_tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewall, "target_tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetTags", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeFirewall.GoogleComputeFirewallAllow",
    jsii_struct_bases=[],
    name_mapping={"protocol": "protocol", "ports": "ports"},
)
class GoogleComputeFirewallAllow:
    def __init__(
        self,
        *,
        protocol: builtins.str,
        ports: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param protocol: The IP protocol to which this rule applies. The protocol type is required when creating a firewall rule. This value can either be one of the following well known protocol strings (tcp, udp, icmp, esp, ah, sctp, ipip, all), or the IP protocol number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#protocol GoogleComputeFirewall#protocol}
        :param ports: An optional list of ports to which this rule applies. This field is only applicable for UDP or TCP protocol. Each entry must be either an integer or a range. If not specified, this rule applies to connections through any port. Example inputs include: ["22"], ["80","443"], and ["12345-12349"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#ports GoogleComputeFirewall#ports}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeFirewallAllow.__init__)
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument ports", value=ports, expected_type=type_hints["ports"])
        self._values: typing.Dict[str, typing.Any] = {
            "protocol": protocol,
        }
        if ports is not None:
            self._values["ports"] = ports

    @builtins.property
    def protocol(self) -> builtins.str:
        '''The IP protocol to which this rule applies.

        The protocol type is
        required when creating a firewall rule. This value can either be
        one of the following well known protocol strings (tcp, udp,
        icmp, esp, ah, sctp, ipip, all), or the IP protocol number.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#protocol GoogleComputeFirewall#protocol}
        '''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ports(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An optional list of ports to which this rule applies.

        This field
        is only applicable for UDP or TCP protocol. Each entry must be
        either an integer or a range. If not specified, this rule
        applies to connections through any port.

        Example inputs include: ["22"], ["80","443"], and
        ["12345-12349"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#ports GoogleComputeFirewall#ports}
        '''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeFirewallAllow(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeFirewallAllowList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeFirewall.GoogleComputeFirewallAllowList",
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
            type_hints = typing.get_type_hints(GoogleComputeFirewallAllowList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GoogleComputeFirewallAllowOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeFirewallAllowList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeFirewallAllowOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallAllowList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallAllowList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallAllowList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeFirewallAllow]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeFirewallAllow]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeFirewallAllow]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallAllowList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeFirewallAllowOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeFirewall.GoogleComputeFirewallAllowOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeFirewallAllowOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPorts")
    def reset_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPorts", []))

    @builtins.property
    @jsii.member(jsii_name="portsInput")
    def ports_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "portsInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="ports")
    def ports(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ports"))

    @ports.setter
    def ports(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallAllowOutputReference, "ports").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ports", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallAllowOutputReference, "protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeFirewallAllow, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeFirewallAllow, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeFirewallAllow, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallAllowOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeFirewall.GoogleComputeFirewallConfig",
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
        "network": "network",
        "allow": "allow",
        "deny": "deny",
        "description": "description",
        "destination_ranges": "destinationRanges",
        "direction": "direction",
        "disabled": "disabled",
        "enable_logging": "enableLogging",
        "id": "id",
        "log_config": "logConfig",
        "priority": "priority",
        "project": "project",
        "source_ranges": "sourceRanges",
        "source_service_accounts": "sourceServiceAccounts",
        "source_tags": "sourceTags",
        "target_service_accounts": "targetServiceAccounts",
        "target_tags": "targetTags",
        "timeouts": "timeouts",
    },
)
class GoogleComputeFirewallConfig(cdktf.TerraformMetaArguments):
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
        network: builtins.str,
        allow: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union[GoogleComputeFirewallAllow, typing.Dict[str, typing.Any]]]]] = None,
        deny: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleComputeFirewallDeny", typing.Dict[str, typing.Any]]]]] = None,
        description: typing.Optional[builtins.str] = None,
        destination_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
        direction: typing.Optional[builtins.str] = None,
        disabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        enable_logging: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        log_config: typing.Optional[typing.Union["GoogleComputeFirewallLogConfig", typing.Dict[str, typing.Any]]] = None,
        priority: typing.Optional[jsii.Number] = None,
        project: typing.Optional[builtins.str] = None,
        source_ranges: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_service_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        target_service_accounts: typing.Optional[typing.Sequence[builtins.str]] = None,
        target_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["GoogleComputeFirewallTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#name GoogleComputeFirewall#name}
        :param network: The name or self_link of the network to attach this firewall to. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#network GoogleComputeFirewall#network}
        :param allow: allow block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#allow GoogleComputeFirewall#allow}
        :param deny: deny block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#deny GoogleComputeFirewall#deny}
        :param description: An optional description of this resource. Provide this property when you create the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#description GoogleComputeFirewall#description}
        :param destination_ranges: If destination ranges are specified, the firewall will apply only to traffic that has destination IP address in these ranges. These ranges must be expressed in CIDR format. Only IPv4 is supported. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#destination_ranges GoogleComputeFirewall#destination_ranges}
        :param direction: Direction of traffic to which this firewall applies; default is INGRESS. Note: For INGRESS traffic, it is NOT supported to specify destinationRanges; For EGRESS traffic, it is NOT supported to specify 'source_ranges' OR 'source_tags'. For INGRESS traffic, one of 'source_ranges', 'source_tags' or 'source_service_accounts' is required. Possible values: ["INGRESS", "EGRESS"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#direction GoogleComputeFirewall#direction}
        :param disabled: Denotes whether the firewall rule is disabled, i.e not applied to the network it is associated with. When set to true, the firewall rule is not enforced and the network behaves as if it did not exist. If this is unspecified, the firewall rule will be enabled. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#disabled GoogleComputeFirewall#disabled}
        :param enable_logging: This field denotes whether to enable logging for a particular firewall rule. If logging is enabled, logs will be exported to Stackdriver. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#enable_logging GoogleComputeFirewall#enable_logging}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#id GoogleComputeFirewall#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param log_config: log_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#log_config GoogleComputeFirewall#log_config}
        :param priority: Priority for this rule. This is an integer between 0 and 65535, both inclusive. When not specified, the value assumed is 1000. Relative priorities determine precedence of conflicting rules. Lower value of priority implies higher precedence (eg, a rule with priority 0 has higher precedence than a rule with priority 1). DENY rules take precedence over ALLOW rules having equal priority. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#priority GoogleComputeFirewall#priority}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#project GoogleComputeFirewall#project}.
        :param source_ranges: If source ranges are specified, the firewall will apply only to traffic that has source IP address in these ranges. These ranges must be expressed in CIDR format. One or both of sourceRanges and sourceTags may be set. If both properties are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP that belongs to a tag listed in the sourceTags property. The connection does not need to match both properties for the firewall to apply. Only IPv4 is supported. For INGRESS traffic, one of 'source_ranges', 'source_tags' or 'source_service_accounts' is required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#source_ranges GoogleComputeFirewall#source_ranges}
        :param source_service_accounts: If source service accounts are specified, the firewall will apply only to traffic originating from an instance with a service account in this list. Source service accounts cannot be used to control traffic to an instance's external IP address because service accounts are associated with an instance, not an IP address. sourceRanges can be set at the same time as sourceServiceAccounts. If both are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP belongs to an instance with service account listed in sourceServiceAccount. The connection does not need to match both properties for the firewall to apply. sourceServiceAccounts cannot be used at the same time as sourceTags or targetTags. For INGRESS traffic, one of 'source_ranges', 'source_tags' or 'source_service_accounts' is required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#source_service_accounts GoogleComputeFirewall#source_service_accounts}
        :param source_tags: If source tags are specified, the firewall will apply only to traffic with source IP that belongs to a tag listed in source tags. Source tags cannot be used to control traffic to an instance's external IP address. Because tags are associated with an instance, not an IP address. One or both of sourceRanges and sourceTags may be set. If both properties are set, the firewall will apply to traffic that has source IP address within sourceRanges OR the source IP that belongs to a tag listed in the sourceTags property. The connection does not need to match both properties for the firewall to apply. For INGRESS traffic, one of 'source_ranges', 'source_tags' or 'source_service_accounts' is required. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#source_tags GoogleComputeFirewall#source_tags}
        :param target_service_accounts: A list of service accounts indicating sets of instances located in the network that may make network connections as specified in allowed[]. targetServiceAccounts cannot be used at the same time as targetTags or sourceTags. If neither targetServiceAccounts nor targetTags are specified, the firewall rule applies to all instances on the specified network. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#target_service_accounts GoogleComputeFirewall#target_service_accounts}
        :param target_tags: A list of instance tags indicating sets of instances located in the network that may make network connections as specified in allowed[]. If no targetTags are specified, the firewall rule applies to all instances on the specified network. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#target_tags GoogleComputeFirewall#target_tags}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#timeouts GoogleComputeFirewall#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(log_config, dict):
            log_config = GoogleComputeFirewallLogConfig(**log_config)
        if isinstance(timeouts, dict):
            timeouts = GoogleComputeFirewallTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeFirewallConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network", value=network, expected_type=type_hints["network"])
            check_type(argname="argument allow", value=allow, expected_type=type_hints["allow"])
            check_type(argname="argument deny", value=deny, expected_type=type_hints["deny"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument destination_ranges", value=destination_ranges, expected_type=type_hints["destination_ranges"])
            check_type(argname="argument direction", value=direction, expected_type=type_hints["direction"])
            check_type(argname="argument disabled", value=disabled, expected_type=type_hints["disabled"])
            check_type(argname="argument enable_logging", value=enable_logging, expected_type=type_hints["enable_logging"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument log_config", value=log_config, expected_type=type_hints["log_config"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument source_ranges", value=source_ranges, expected_type=type_hints["source_ranges"])
            check_type(argname="argument source_service_accounts", value=source_service_accounts, expected_type=type_hints["source_service_accounts"])
            check_type(argname="argument source_tags", value=source_tags, expected_type=type_hints["source_tags"])
            check_type(argname="argument target_service_accounts", value=target_service_accounts, expected_type=type_hints["target_service_accounts"])
            check_type(argname="argument target_tags", value=target_tags, expected_type=type_hints["target_tags"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "network": network,
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
        if allow is not None:
            self._values["allow"] = allow
        if deny is not None:
            self._values["deny"] = deny
        if description is not None:
            self._values["description"] = description
        if destination_ranges is not None:
            self._values["destination_ranges"] = destination_ranges
        if direction is not None:
            self._values["direction"] = direction
        if disabled is not None:
            self._values["disabled"] = disabled
        if enable_logging is not None:
            self._values["enable_logging"] = enable_logging
        if id is not None:
            self._values["id"] = id
        if log_config is not None:
            self._values["log_config"] = log_config
        if priority is not None:
            self._values["priority"] = priority
        if project is not None:
            self._values["project"] = project
        if source_ranges is not None:
            self._values["source_ranges"] = source_ranges
        if source_service_accounts is not None:
            self._values["source_service_accounts"] = source_service_accounts
        if source_tags is not None:
            self._values["source_tags"] = source_tags
        if target_service_accounts is not None:
            self._values["target_service_accounts"] = target_service_accounts
        if target_tags is not None:
            self._values["target_tags"] = target_tags
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
    def name(self) -> builtins.str:
        '''Name of the resource.

        Provided by the client when the resource is
        created. The name must be 1-63 characters long, and comply with
        RFC1035. Specifically, the name must be 1-63 characters long and match
        the regular expression '`a-z <%5B-a-z0-9%5D*%5Ba-z0-9%5D>`_?' which means the
        first character must be a lowercase letter, and all following
        characters must be a dash, lowercase letter, or digit, except the last
        character, which cannot be a dash.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#name GoogleComputeFirewall#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network(self) -> builtins.str:
        '''The name or self_link of the network to attach this firewall to.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#network GoogleComputeFirewall#network}
        '''
        result = self._values.get("network")
        assert result is not None, "Required property 'network' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeFirewallAllow]]]:
        '''allow block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#allow GoogleComputeFirewall#allow}
        '''
        result = self._values.get("allow")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeFirewallAllow]]], result)

    @builtins.property
    def deny(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeFirewallDeny"]]]:
        '''deny block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#deny GoogleComputeFirewall#deny}
        '''
        result = self._values.get("deny")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleComputeFirewallDeny"]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''An optional description of this resource. Provide this property when you create the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#description GoogleComputeFirewall#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def destination_ranges(self) -> typing.Optional[typing.List[builtins.str]]:
        '''If destination ranges are specified, the firewall will apply only to traffic that has destination IP address in these ranges.

        These ranges
        must be expressed in CIDR format. Only IPv4 is supported.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#destination_ranges GoogleComputeFirewall#destination_ranges}
        '''
        result = self._values.get("destination_ranges")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def direction(self) -> typing.Optional[builtins.str]:
        '''Direction of traffic to which this firewall applies;

        default is
        INGRESS. Note: For INGRESS traffic, it is NOT supported to specify
        destinationRanges; For EGRESS traffic, it is NOT supported to specify
        'source_ranges' OR 'source_tags'. For INGRESS traffic, one of 'source_ranges',
        'source_tags' or 'source_service_accounts' is required. Possible values: ["INGRESS", "EGRESS"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#direction GoogleComputeFirewall#direction}
        '''
        result = self._values.get("direction")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Denotes whether the firewall rule is disabled, i.e not applied to the network it is associated with. When set to true, the firewall rule is not enforced and the network behaves as if it did not exist. If this is unspecified, the firewall rule will be enabled.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#disabled GoogleComputeFirewall#disabled}
        '''
        result = self._values.get("disabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def enable_logging(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''This field denotes whether to enable logging for a particular firewall rule.

        If logging is enabled, logs will be exported to Stackdriver.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#enable_logging GoogleComputeFirewall#enable_logging}
        '''
        result = self._values.get("enable_logging")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#id GoogleComputeFirewall#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_config(self) -> typing.Optional["GoogleComputeFirewallLogConfig"]:
        '''log_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#log_config GoogleComputeFirewall#log_config}
        '''
        result = self._values.get("log_config")
        return typing.cast(typing.Optional["GoogleComputeFirewallLogConfig"], result)

    @builtins.property
    def priority(self) -> typing.Optional[jsii.Number]:
        '''Priority for this rule.

        This is an integer between 0 and 65535, both
        inclusive. When not specified, the value assumed is 1000. Relative
        priorities determine precedence of conflicting rules. Lower value of
        priority implies higher precedence (eg, a rule with priority 0 has
        higher precedence than a rule with priority 1). DENY rules take
        precedence over ALLOW rules having equal priority.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#priority GoogleComputeFirewall#priority}
        '''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#project GoogleComputeFirewall#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_ranges(self) -> typing.Optional[typing.List[builtins.str]]:
        '''If source ranges are specified, the firewall will apply only to traffic that has source IP address in these ranges.

        These ranges must
        be expressed in CIDR format. One or both of sourceRanges and
        sourceTags may be set. If both properties are set, the firewall will
        apply to traffic that has source IP address within sourceRanges OR the
        source IP that belongs to a tag listed in the sourceTags property. The
        connection does not need to match both properties for the firewall to
        apply. Only IPv4 is supported. For INGRESS traffic, one of 'source_ranges',
        'source_tags' or 'source_service_accounts' is required.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#source_ranges GoogleComputeFirewall#source_ranges}
        '''
        result = self._values.get("source_ranges")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def source_service_accounts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''If source service accounts are specified, the firewall will apply only to traffic originating from an instance with a service account in this list.

        Source service accounts cannot be used to control traffic to an
        instance's external IP address because service accounts are associated
        with an instance, not an IP address. sourceRanges can be set at the
        same time as sourceServiceAccounts. If both are set, the firewall will
        apply to traffic that has source IP address within sourceRanges OR the
        source IP belongs to an instance with service account listed in
        sourceServiceAccount. The connection does not need to match both
        properties for the firewall to apply. sourceServiceAccounts cannot be
        used at the same time as sourceTags or targetTags. For INGRESS traffic,
        one of 'source_ranges', 'source_tags' or 'source_service_accounts' is required.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#source_service_accounts GoogleComputeFirewall#source_service_accounts}
        '''
        result = self._values.get("source_service_accounts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def source_tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''If source tags are specified, the firewall will apply only to traffic with source IP that belongs to a tag listed in source tags.

        Source
        tags cannot be used to control traffic to an instance's external IP
        address. Because tags are associated with an instance, not an IP
        address. One or both of sourceRanges and sourceTags may be set. If
        both properties are set, the firewall will apply to traffic that has
        source IP address within sourceRanges OR the source IP that belongs to
        a tag listed in the sourceTags property. The connection does not need
        to match both properties for the firewall to apply. For INGRESS traffic,
        one of 'source_ranges', 'source_tags' or 'source_service_accounts' is required.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#source_tags GoogleComputeFirewall#source_tags}
        '''
        result = self._values.get("source_tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def target_service_accounts(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of service accounts indicating sets of instances located in the network that may make network connections as specified in allowed[].

        targetServiceAccounts cannot be used at the same time as targetTags or
        sourceTags. If neither targetServiceAccounts nor targetTags are
        specified, the firewall rule applies to all instances on the specified
        network.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#target_service_accounts GoogleComputeFirewall#target_service_accounts}
        '''
        result = self._values.get("target_service_accounts")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def target_tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of instance tags indicating sets of instances located in the network that may make network connections as specified in allowed[].

        If no targetTags are specified, the firewall rule applies to all
        instances on the specified network.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#target_tags GoogleComputeFirewall#target_tags}
        '''
        result = self._values.get("target_tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleComputeFirewallTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#timeouts GoogleComputeFirewall#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleComputeFirewallTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeFirewallConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeFirewall.GoogleComputeFirewallDeny",
    jsii_struct_bases=[],
    name_mapping={"protocol": "protocol", "ports": "ports"},
)
class GoogleComputeFirewallDeny:
    def __init__(
        self,
        *,
        protocol: builtins.str,
        ports: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param protocol: The IP protocol to which this rule applies. The protocol type is required when creating a firewall rule. This value can either be one of the following well known protocol strings (tcp, udp, icmp, esp, ah, sctp, ipip, all), or the IP protocol number. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#protocol GoogleComputeFirewall#protocol}
        :param ports: An optional list of ports to which this rule applies. This field is only applicable for UDP or TCP protocol. Each entry must be either an integer or a range. If not specified, this rule applies to connections through any port. Example inputs include: ["22"], ["80","443"], and ["12345-12349"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#ports GoogleComputeFirewall#ports}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeFirewallDeny.__init__)
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument ports", value=ports, expected_type=type_hints["ports"])
        self._values: typing.Dict[str, typing.Any] = {
            "protocol": protocol,
        }
        if ports is not None:
            self._values["ports"] = ports

    @builtins.property
    def protocol(self) -> builtins.str:
        '''The IP protocol to which this rule applies.

        The protocol type is
        required when creating a firewall rule. This value can either be
        one of the following well known protocol strings (tcp, udp,
        icmp, esp, ah, sctp, ipip, all), or the IP protocol number.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#protocol GoogleComputeFirewall#protocol}
        '''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def ports(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An optional list of ports to which this rule applies.

        This field
        is only applicable for UDP or TCP protocol. Each entry must be
        either an integer or a range. If not specified, this rule
        applies to connections through any port.

        Example inputs include: ["22"], ["80","443"], and
        ["12345-12349"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#ports GoogleComputeFirewall#ports}
        '''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeFirewallDeny(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeFirewallDenyList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeFirewall.GoogleComputeFirewallDenyList",
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
            type_hints = typing.get_type_hints(GoogleComputeFirewallDenyList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GoogleComputeFirewallDenyOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeFirewallDenyList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleComputeFirewallDenyOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallDenyList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallDenyList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallDenyList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeFirewallDeny]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeFirewallDeny]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleComputeFirewallDeny]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallDenyList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleComputeFirewallDenyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeFirewall.GoogleComputeFirewallDenyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeFirewallDenyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetPorts")
    def reset_ports(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPorts", []))

    @builtins.property
    @jsii.member(jsii_name="portsInput")
    def ports_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "portsInput"))

    @builtins.property
    @jsii.member(jsii_name="protocolInput")
    def protocol_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolInput"))

    @builtins.property
    @jsii.member(jsii_name="ports")
    def ports(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "ports"))

    @ports.setter
    def ports(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallDenyOutputReference, "ports").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ports", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallDenyOutputReference, "protocol").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeFirewallDeny, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeFirewallDeny, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeFirewallDeny, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallDenyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeFirewall.GoogleComputeFirewallLogConfig",
    jsii_struct_bases=[],
    name_mapping={"metadata": "metadata"},
)
class GoogleComputeFirewallLogConfig:
    def __init__(self, *, metadata: builtins.str) -> None:
        '''
        :param metadata: This field denotes whether to include or exclude metadata for firewall logs. Possible values: ["EXCLUDE_ALL_METADATA", "INCLUDE_ALL_METADATA"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#metadata GoogleComputeFirewall#metadata}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeFirewallLogConfig.__init__)
            check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
        self._values: typing.Dict[str, typing.Any] = {
            "metadata": metadata,
        }

    @builtins.property
    def metadata(self) -> builtins.str:
        '''This field denotes whether to include or exclude metadata for firewall logs. Possible values: ["EXCLUDE_ALL_METADATA", "INCLUDE_ALL_METADATA"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#metadata GoogleComputeFirewall#metadata}
        '''
        result = self._values.get("metadata")
        assert result is not None, "Required property 'metadata' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeFirewallLogConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeFirewallLogConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeFirewall.GoogleComputeFirewallLogConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeFirewallLogConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="metadataInput")
    def metadata_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metadataInput"))

    @builtins.property
    @jsii.member(jsii_name="metadata")
    def metadata(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "metadata"))

    @metadata.setter
    def metadata(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallLogConfigOutputReference, "metadata").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadata", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleComputeFirewallLogConfig]:
        return typing.cast(typing.Optional[GoogleComputeFirewallLogConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleComputeFirewallLogConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallLogConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleComputeFirewall.GoogleComputeFirewallTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleComputeFirewallTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#create GoogleComputeFirewall#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#delete GoogleComputeFirewall#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#update GoogleComputeFirewall#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleComputeFirewallTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#create GoogleComputeFirewall#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#delete GoogleComputeFirewall#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_compute_firewall#update GoogleComputeFirewall#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleComputeFirewallTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleComputeFirewallTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleComputeFirewall.GoogleComputeFirewallTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleComputeFirewallTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleComputeFirewallTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleComputeFirewallTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleComputeFirewallTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleComputeFirewallTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleComputeFirewall",
    "GoogleComputeFirewallAllow",
    "GoogleComputeFirewallAllowList",
    "GoogleComputeFirewallAllowOutputReference",
    "GoogleComputeFirewallConfig",
    "GoogleComputeFirewallDeny",
    "GoogleComputeFirewallDenyList",
    "GoogleComputeFirewallDenyOutputReference",
    "GoogleComputeFirewallLogConfig",
    "GoogleComputeFirewallLogConfigOutputReference",
    "GoogleComputeFirewallTimeouts",
    "GoogleComputeFirewallTimeoutsOutputReference",
]

publication.publish()
