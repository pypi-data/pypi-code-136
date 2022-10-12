'''
# `google_storage_bucket`

Refer to the Terraform Registory for docs: [`google_storage_bucket`](https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket).
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


class GoogleStorageBucket(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleStorageBucket.GoogleStorageBucket",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket google_storage_bucket}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location: builtins.str,
        name: builtins.str,
        cors: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleStorageBucketCors", typing.Dict[str, typing.Any]]]]] = None,
        custom_placement_config: typing.Optional[typing.Union["GoogleStorageBucketCustomPlacementConfig", typing.Dict[str, typing.Any]]] = None,
        default_event_based_hold: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        encryption: typing.Optional[typing.Union["GoogleStorageBucketEncryption", typing.Dict[str, typing.Any]]] = None,
        force_destroy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        lifecycle_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleStorageBucketLifecycleRule", typing.Dict[str, typing.Any]]]]] = None,
        logging: typing.Optional[typing.Union["GoogleStorageBucketLogging", typing.Dict[str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        public_access_prevention: typing.Optional[builtins.str] = None,
        requester_pays: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        retention_policy: typing.Optional[typing.Union["GoogleStorageBucketRetentionPolicy", typing.Dict[str, typing.Any]]] = None,
        storage_class: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleStorageBucketTimeouts", typing.Dict[str, typing.Any]]] = None,
        uniform_bucket_level_access: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        versioning: typing.Optional[typing.Union["GoogleStorageBucketVersioning", typing.Dict[str, typing.Any]]] = None,
        website: typing.Optional[typing.Union["GoogleStorageBucketWebsite", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket google_storage_bucket} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location: The Google Cloud Storage location. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#location GoogleStorageBucket#location}
        :param name: The name of the bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#name GoogleStorageBucket#name}
        :param cors: cors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#cors GoogleStorageBucket#cors}
        :param custom_placement_config: custom_placement_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#custom_placement_config GoogleStorageBucket#custom_placement_config}
        :param default_event_based_hold: Whether or not to automatically apply an eventBasedHold to new objects added to the bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#default_event_based_hold GoogleStorageBucket#default_event_based_hold}
        :param encryption: encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#encryption GoogleStorageBucket#encryption}
        :param force_destroy: When deleting a bucket, this boolean option will delete all contained objects. If you try to delete a bucket that contains objects, Terraform will fail that run. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#force_destroy GoogleStorageBucket#force_destroy}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#id GoogleStorageBucket#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: A set of key/value label pairs to assign to the bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#labels GoogleStorageBucket#labels}
        :param lifecycle_rule: lifecycle_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#lifecycle_rule GoogleStorageBucket#lifecycle_rule}
        :param logging: logging block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#logging GoogleStorageBucket#logging}
        :param project: The ID of the project in which the resource belongs. If it is not provided, the provider project is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#project GoogleStorageBucket#project}
        :param public_access_prevention: Prevents public access to a bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#public_access_prevention GoogleStorageBucket#public_access_prevention}
        :param requester_pays: Enables Requester Pays on a storage bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#requester_pays GoogleStorageBucket#requester_pays}
        :param retention_policy: retention_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#retention_policy GoogleStorageBucket#retention_policy}
        :param storage_class: The Storage Class of the new bucket. Supported values include: STANDARD, MULTI_REGIONAL, REGIONAL, NEARLINE, COLDLINE, ARCHIVE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#storage_class GoogleStorageBucket#storage_class}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#timeouts GoogleStorageBucket#timeouts}
        :param uniform_bucket_level_access: Enables uniform bucket-level access on a bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#uniform_bucket_level_access GoogleStorageBucket#uniform_bucket_level_access}
        :param versioning: versioning block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#versioning GoogleStorageBucket#versioning}
        :param website: website block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#website GoogleStorageBucket#website}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleStorageBucket.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleStorageBucketConfig(
            location=location,
            name=name,
            cors=cors,
            custom_placement_config=custom_placement_config,
            default_event_based_hold=default_event_based_hold,
            encryption=encryption,
            force_destroy=force_destroy,
            id=id,
            labels=labels,
            lifecycle_rule=lifecycle_rule,
            logging=logging,
            project=project,
            public_access_prevention=public_access_prevention,
            requester_pays=requester_pays,
            retention_policy=retention_policy,
            storage_class=storage_class,
            timeouts=timeouts,
            uniform_bucket_level_access=uniform_bucket_level_access,
            versioning=versioning,
            website=website,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCors")
    def put_cors(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleStorageBucketCors", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleStorageBucket.put_cors)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putCors", [value]))

    @jsii.member(jsii_name="putCustomPlacementConfig")
    def put_custom_placement_config(
        self,
        *,
        data_locations: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param data_locations: The list of individual regions that comprise a dual-region bucket. See the docs for a list of acceptable regions. Note: If any of the data_locations changes, it will recreate the bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#data_locations GoogleStorageBucket#data_locations}
        '''
        value = GoogleStorageBucketCustomPlacementConfig(data_locations=data_locations)

        return typing.cast(None, jsii.invoke(self, "putCustomPlacementConfig", [value]))

    @jsii.member(jsii_name="putEncryption")
    def put_encryption(self, *, default_kms_key_name: builtins.str) -> None:
        '''
        :param default_kms_key_name: A Cloud KMS key that will be used to encrypt objects inserted into this bucket, if no encryption method is specified. You must pay attention to whether the crypto key is available in the location that this bucket is created in. See the docs for more details. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#default_kms_key_name GoogleStorageBucket#default_kms_key_name}
        '''
        value = GoogleStorageBucketEncryption(
            default_kms_key_name=default_kms_key_name
        )

        return typing.cast(None, jsii.invoke(self, "putEncryption", [value]))

    @jsii.member(jsii_name="putLifecycleRule")
    def put_lifecycle_rule(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleStorageBucketLifecycleRule", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleStorageBucket.put_lifecycle_rule)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putLifecycleRule", [value]))

    @jsii.member(jsii_name="putLogging")
    def put_logging(
        self,
        *,
        log_bucket: builtins.str,
        log_object_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param log_bucket: The bucket that will receive log objects. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#log_bucket GoogleStorageBucket#log_bucket}
        :param log_object_prefix: The object prefix for log objects. If it's not provided, by default Google Cloud Storage sets this to this bucket's name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#log_object_prefix GoogleStorageBucket#log_object_prefix}
        '''
        value = GoogleStorageBucketLogging(
            log_bucket=log_bucket, log_object_prefix=log_object_prefix
        )

        return typing.cast(None, jsii.invoke(self, "putLogging", [value]))

    @jsii.member(jsii_name="putRetentionPolicy")
    def put_retention_policy(
        self,
        *,
        retention_period: jsii.Number,
        is_locked: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param retention_period: The period of time, in seconds, that objects in the bucket must be retained and cannot be deleted, overwritten, or archived. The value must be less than 3,155,760,000 seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#retention_period GoogleStorageBucket#retention_period}
        :param is_locked: If set to true, the bucket will be locked and permanently restrict edits to the bucket's retention policy. Caution: Locking a bucket is an irreversible action. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#is_locked GoogleStorageBucket#is_locked}
        '''
        value = GoogleStorageBucketRetentionPolicy(
            retention_period=retention_period, is_locked=is_locked
        )

        return typing.cast(None, jsii.invoke(self, "putRetentionPolicy", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#create GoogleStorageBucket#create}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#read GoogleStorageBucket#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#update GoogleStorageBucket#update}.
        '''
        value = GoogleStorageBucketTimeouts(create=create, read=read, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="putVersioning")
    def put_versioning(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled: While set to true, versioning is fully enabled for this bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#enabled GoogleStorageBucket#enabled}
        '''
        value = GoogleStorageBucketVersioning(enabled=enabled)

        return typing.cast(None, jsii.invoke(self, "putVersioning", [value]))

    @jsii.member(jsii_name="putWebsite")
    def put_website(
        self,
        *,
        main_page_suffix: typing.Optional[builtins.str] = None,
        not_found_page: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param main_page_suffix: Behaves as the bucket's directory index where missing objects are treated as potential directories. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#main_page_suffix GoogleStorageBucket#main_page_suffix}
        :param not_found_page: The custom object to return when a requested resource is not found. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#not_found_page GoogleStorageBucket#not_found_page}
        '''
        value = GoogleStorageBucketWebsite(
            main_page_suffix=main_page_suffix, not_found_page=not_found_page
        )

        return typing.cast(None, jsii.invoke(self, "putWebsite", [value]))

    @jsii.member(jsii_name="resetCors")
    def reset_cors(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCors", []))

    @jsii.member(jsii_name="resetCustomPlacementConfig")
    def reset_custom_placement_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomPlacementConfig", []))

    @jsii.member(jsii_name="resetDefaultEventBasedHold")
    def reset_default_event_based_hold(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultEventBasedHold", []))

    @jsii.member(jsii_name="resetEncryption")
    def reset_encryption(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryption", []))

    @jsii.member(jsii_name="resetForceDestroy")
    def reset_force_destroy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceDestroy", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetLifecycleRule")
    def reset_lifecycle_rule(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLifecycleRule", []))

    @jsii.member(jsii_name="resetLogging")
    def reset_logging(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogging", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetPublicAccessPrevention")
    def reset_public_access_prevention(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublicAccessPrevention", []))

    @jsii.member(jsii_name="resetRequesterPays")
    def reset_requester_pays(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequesterPays", []))

    @jsii.member(jsii_name="resetRetentionPolicy")
    def reset_retention_policy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRetentionPolicy", []))

    @jsii.member(jsii_name="resetStorageClass")
    def reset_storage_class(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageClass", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="resetUniformBucketLevelAccess")
    def reset_uniform_bucket_level_access(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUniformBucketLevelAccess", []))

    @jsii.member(jsii_name="resetVersioning")
    def reset_versioning(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetVersioning", []))

    @jsii.member(jsii_name="resetWebsite")
    def reset_website(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWebsite", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="cors")
    def cors(self) -> "GoogleStorageBucketCorsList":
        return typing.cast("GoogleStorageBucketCorsList", jsii.get(self, "cors"))

    @builtins.property
    @jsii.member(jsii_name="customPlacementConfig")
    def custom_placement_config(
        self,
    ) -> "GoogleStorageBucketCustomPlacementConfigOutputReference":
        return typing.cast("GoogleStorageBucketCustomPlacementConfigOutputReference", jsii.get(self, "customPlacementConfig"))

    @builtins.property
    @jsii.member(jsii_name="encryption")
    def encryption(self) -> "GoogleStorageBucketEncryptionOutputReference":
        return typing.cast("GoogleStorageBucketEncryptionOutputReference", jsii.get(self, "encryption"))

    @builtins.property
    @jsii.member(jsii_name="lifecycleRule")
    def lifecycle_rule(self) -> "GoogleStorageBucketLifecycleRuleList":
        return typing.cast("GoogleStorageBucketLifecycleRuleList", jsii.get(self, "lifecycleRule"))

    @builtins.property
    @jsii.member(jsii_name="logging")
    def logging(self) -> "GoogleStorageBucketLoggingOutputReference":
        return typing.cast("GoogleStorageBucketLoggingOutputReference", jsii.get(self, "logging"))

    @builtins.property
    @jsii.member(jsii_name="retentionPolicy")
    def retention_policy(self) -> "GoogleStorageBucketRetentionPolicyOutputReference":
        return typing.cast("GoogleStorageBucketRetentionPolicyOutputReference", jsii.get(self, "retentionPolicy"))

    @builtins.property
    @jsii.member(jsii_name="selfLink")
    def self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfLink"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleStorageBucketTimeoutsOutputReference":
        return typing.cast("GoogleStorageBucketTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @builtins.property
    @jsii.member(jsii_name="versioning")
    def versioning(self) -> "GoogleStorageBucketVersioningOutputReference":
        return typing.cast("GoogleStorageBucketVersioningOutputReference", jsii.get(self, "versioning"))

    @builtins.property
    @jsii.member(jsii_name="website")
    def website(self) -> "GoogleStorageBucketWebsiteOutputReference":
        return typing.cast("GoogleStorageBucketWebsiteOutputReference", jsii.get(self, "website"))

    @builtins.property
    @jsii.member(jsii_name="corsInput")
    def cors_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleStorageBucketCors"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleStorageBucketCors"]]], jsii.get(self, "corsInput"))

    @builtins.property
    @jsii.member(jsii_name="customPlacementConfigInput")
    def custom_placement_config_input(
        self,
    ) -> typing.Optional["GoogleStorageBucketCustomPlacementConfig"]:
        return typing.cast(typing.Optional["GoogleStorageBucketCustomPlacementConfig"], jsii.get(self, "customPlacementConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultEventBasedHoldInput")
    def default_event_based_hold_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "defaultEventBasedHoldInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionInput")
    def encryption_input(self) -> typing.Optional["GoogleStorageBucketEncryption"]:
        return typing.cast(typing.Optional["GoogleStorageBucketEncryption"], jsii.get(self, "encryptionInput"))

    @builtins.property
    @jsii.member(jsii_name="forceDestroyInput")
    def force_destroy_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "forceDestroyInput"))

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
    @jsii.member(jsii_name="lifecycleRuleInput")
    def lifecycle_rule_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleStorageBucketLifecycleRule"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleStorageBucketLifecycleRule"]]], jsii.get(self, "lifecycleRuleInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingInput")
    def logging_input(self) -> typing.Optional["GoogleStorageBucketLogging"]:
        return typing.cast(typing.Optional["GoogleStorageBucketLogging"], jsii.get(self, "loggingInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="publicAccessPreventionInput")
    def public_access_prevention_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publicAccessPreventionInput"))

    @builtins.property
    @jsii.member(jsii_name="requesterPaysInput")
    def requester_pays_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requesterPaysInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionPolicyInput")
    def retention_policy_input(
        self,
    ) -> typing.Optional["GoogleStorageBucketRetentionPolicy"]:
        return typing.cast(typing.Optional["GoogleStorageBucketRetentionPolicy"], jsii.get(self, "retentionPolicyInput"))

    @builtins.property
    @jsii.member(jsii_name="storageClassInput")
    def storage_class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageClassInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleStorageBucketTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleStorageBucketTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="uniformBucketLevelAccessInput")
    def uniform_bucket_level_access_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "uniformBucketLevelAccessInput"))

    @builtins.property
    @jsii.member(jsii_name="versioningInput")
    def versioning_input(self) -> typing.Optional["GoogleStorageBucketVersioning"]:
        return typing.cast(typing.Optional["GoogleStorageBucketVersioning"], jsii.get(self, "versioningInput"))

    @builtins.property
    @jsii.member(jsii_name="websiteInput")
    def website_input(self) -> typing.Optional["GoogleStorageBucketWebsite"]:
        return typing.cast(typing.Optional["GoogleStorageBucketWebsite"], jsii.get(self, "websiteInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultEventBasedHold")
    def default_event_based_hold(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "defaultEventBasedHold"))

    @default_event_based_hold.setter
    def default_event_based_hold(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucket, "default_event_based_hold").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultEventBasedHold", value)

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
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucket, "force_destroy").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceDestroy", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucket, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucket, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucket, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucket, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucket, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="publicAccessPrevention")
    def public_access_prevention(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publicAccessPrevention"))

    @public_access_prevention.setter
    def public_access_prevention(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucket, "public_access_prevention").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publicAccessPrevention", value)

    @builtins.property
    @jsii.member(jsii_name="requesterPays")
    def requester_pays(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "requesterPays"))

    @requester_pays.setter
    def requester_pays(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucket, "requester_pays").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requesterPays", value)

    @builtins.property
    @jsii.member(jsii_name="storageClass")
    def storage_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageClass"))

    @storage_class.setter
    def storage_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucket, "storage_class").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageClass", value)

    @builtins.property
    @jsii.member(jsii_name="uniformBucketLevelAccess")
    def uniform_bucket_level_access(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "uniformBucketLevelAccess"))

    @uniform_bucket_level_access.setter
    def uniform_bucket_level_access(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucket, "uniform_bucket_level_access").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uniformBucketLevelAccess", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleStorageBucket.GoogleStorageBucketConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "location": "location",
        "name": "name",
        "cors": "cors",
        "custom_placement_config": "customPlacementConfig",
        "default_event_based_hold": "defaultEventBasedHold",
        "encryption": "encryption",
        "force_destroy": "forceDestroy",
        "id": "id",
        "labels": "labels",
        "lifecycle_rule": "lifecycleRule",
        "logging": "logging",
        "project": "project",
        "public_access_prevention": "publicAccessPrevention",
        "requester_pays": "requesterPays",
        "retention_policy": "retentionPolicy",
        "storage_class": "storageClass",
        "timeouts": "timeouts",
        "uniform_bucket_level_access": "uniformBucketLevelAccess",
        "versioning": "versioning",
        "website": "website",
    },
)
class GoogleStorageBucketConfig(cdktf.TerraformMetaArguments):
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
        location: builtins.str,
        name: builtins.str,
        cors: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleStorageBucketCors", typing.Dict[str, typing.Any]]]]] = None,
        custom_placement_config: typing.Optional[typing.Union["GoogleStorageBucketCustomPlacementConfig", typing.Dict[str, typing.Any]]] = None,
        default_event_based_hold: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        encryption: typing.Optional[typing.Union["GoogleStorageBucketEncryption", typing.Dict[str, typing.Any]]] = None,
        force_destroy: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        lifecycle_rule: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleStorageBucketLifecycleRule", typing.Dict[str, typing.Any]]]]] = None,
        logging: typing.Optional[typing.Union["GoogleStorageBucketLogging", typing.Dict[str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        public_access_prevention: typing.Optional[builtins.str] = None,
        requester_pays: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        retention_policy: typing.Optional[typing.Union["GoogleStorageBucketRetentionPolicy", typing.Dict[str, typing.Any]]] = None,
        storage_class: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleStorageBucketTimeouts", typing.Dict[str, typing.Any]]] = None,
        uniform_bucket_level_access: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        versioning: typing.Optional[typing.Union["GoogleStorageBucketVersioning", typing.Dict[str, typing.Any]]] = None,
        website: typing.Optional[typing.Union["GoogleStorageBucketWebsite", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location: The Google Cloud Storage location. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#location GoogleStorageBucket#location}
        :param name: The name of the bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#name GoogleStorageBucket#name}
        :param cors: cors block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#cors GoogleStorageBucket#cors}
        :param custom_placement_config: custom_placement_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#custom_placement_config GoogleStorageBucket#custom_placement_config}
        :param default_event_based_hold: Whether or not to automatically apply an eventBasedHold to new objects added to the bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#default_event_based_hold GoogleStorageBucket#default_event_based_hold}
        :param encryption: encryption block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#encryption GoogleStorageBucket#encryption}
        :param force_destroy: When deleting a bucket, this boolean option will delete all contained objects. If you try to delete a bucket that contains objects, Terraform will fail that run. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#force_destroy GoogleStorageBucket#force_destroy}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#id GoogleStorageBucket#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: A set of key/value label pairs to assign to the bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#labels GoogleStorageBucket#labels}
        :param lifecycle_rule: lifecycle_rule block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#lifecycle_rule GoogleStorageBucket#lifecycle_rule}
        :param logging: logging block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#logging GoogleStorageBucket#logging}
        :param project: The ID of the project in which the resource belongs. If it is not provided, the provider project is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#project GoogleStorageBucket#project}
        :param public_access_prevention: Prevents public access to a bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#public_access_prevention GoogleStorageBucket#public_access_prevention}
        :param requester_pays: Enables Requester Pays on a storage bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#requester_pays GoogleStorageBucket#requester_pays}
        :param retention_policy: retention_policy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#retention_policy GoogleStorageBucket#retention_policy}
        :param storage_class: The Storage Class of the new bucket. Supported values include: STANDARD, MULTI_REGIONAL, REGIONAL, NEARLINE, COLDLINE, ARCHIVE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#storage_class GoogleStorageBucket#storage_class}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#timeouts GoogleStorageBucket#timeouts}
        :param uniform_bucket_level_access: Enables uniform bucket-level access on a bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#uniform_bucket_level_access GoogleStorageBucket#uniform_bucket_level_access}
        :param versioning: versioning block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#versioning GoogleStorageBucket#versioning}
        :param website: website block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#website GoogleStorageBucket#website}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(custom_placement_config, dict):
            custom_placement_config = GoogleStorageBucketCustomPlacementConfig(**custom_placement_config)
        if isinstance(encryption, dict):
            encryption = GoogleStorageBucketEncryption(**encryption)
        if isinstance(logging, dict):
            logging = GoogleStorageBucketLogging(**logging)
        if isinstance(retention_policy, dict):
            retention_policy = GoogleStorageBucketRetentionPolicy(**retention_policy)
        if isinstance(timeouts, dict):
            timeouts = GoogleStorageBucketTimeouts(**timeouts)
        if isinstance(versioning, dict):
            versioning = GoogleStorageBucketVersioning(**versioning)
        if isinstance(website, dict):
            website = GoogleStorageBucketWebsite(**website)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleStorageBucketConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument cors", value=cors, expected_type=type_hints["cors"])
            check_type(argname="argument custom_placement_config", value=custom_placement_config, expected_type=type_hints["custom_placement_config"])
            check_type(argname="argument default_event_based_hold", value=default_event_based_hold, expected_type=type_hints["default_event_based_hold"])
            check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
            check_type(argname="argument force_destroy", value=force_destroy, expected_type=type_hints["force_destroy"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument lifecycle_rule", value=lifecycle_rule, expected_type=type_hints["lifecycle_rule"])
            check_type(argname="argument logging", value=logging, expected_type=type_hints["logging"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument public_access_prevention", value=public_access_prevention, expected_type=type_hints["public_access_prevention"])
            check_type(argname="argument requester_pays", value=requester_pays, expected_type=type_hints["requester_pays"])
            check_type(argname="argument retention_policy", value=retention_policy, expected_type=type_hints["retention_policy"])
            check_type(argname="argument storage_class", value=storage_class, expected_type=type_hints["storage_class"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
            check_type(argname="argument uniform_bucket_level_access", value=uniform_bucket_level_access, expected_type=type_hints["uniform_bucket_level_access"])
            check_type(argname="argument versioning", value=versioning, expected_type=type_hints["versioning"])
            check_type(argname="argument website", value=website, expected_type=type_hints["website"])
        self._values: typing.Dict[str, typing.Any] = {
            "location": location,
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
        if cors is not None:
            self._values["cors"] = cors
        if custom_placement_config is not None:
            self._values["custom_placement_config"] = custom_placement_config
        if default_event_based_hold is not None:
            self._values["default_event_based_hold"] = default_event_based_hold
        if encryption is not None:
            self._values["encryption"] = encryption
        if force_destroy is not None:
            self._values["force_destroy"] = force_destroy
        if id is not None:
            self._values["id"] = id
        if labels is not None:
            self._values["labels"] = labels
        if lifecycle_rule is not None:
            self._values["lifecycle_rule"] = lifecycle_rule
        if logging is not None:
            self._values["logging"] = logging
        if project is not None:
            self._values["project"] = project
        if public_access_prevention is not None:
            self._values["public_access_prevention"] = public_access_prevention
        if requester_pays is not None:
            self._values["requester_pays"] = requester_pays
        if retention_policy is not None:
            self._values["retention_policy"] = retention_policy
        if storage_class is not None:
            self._values["storage_class"] = storage_class
        if timeouts is not None:
            self._values["timeouts"] = timeouts
        if uniform_bucket_level_access is not None:
            self._values["uniform_bucket_level_access"] = uniform_bucket_level_access
        if versioning is not None:
            self._values["versioning"] = versioning
        if website is not None:
            self._values["website"] = website

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
    def location(self) -> builtins.str:
        '''The Google Cloud Storage location.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#location GoogleStorageBucket#location}
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the bucket.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#name GoogleStorageBucket#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cors(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleStorageBucketCors"]]]:
        '''cors block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#cors GoogleStorageBucket#cors}
        '''
        result = self._values.get("cors")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleStorageBucketCors"]]], result)

    @builtins.property
    def custom_placement_config(
        self,
    ) -> typing.Optional["GoogleStorageBucketCustomPlacementConfig"]:
        '''custom_placement_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#custom_placement_config GoogleStorageBucket#custom_placement_config}
        '''
        result = self._values.get("custom_placement_config")
        return typing.cast(typing.Optional["GoogleStorageBucketCustomPlacementConfig"], result)

    @builtins.property
    def default_event_based_hold(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether or not to automatically apply an eventBasedHold to new objects added to the bucket.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#default_event_based_hold GoogleStorageBucket#default_event_based_hold}
        '''
        result = self._values.get("default_event_based_hold")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def encryption(self) -> typing.Optional["GoogleStorageBucketEncryption"]:
        '''encryption block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#encryption GoogleStorageBucket#encryption}
        '''
        result = self._values.get("encryption")
        return typing.cast(typing.Optional["GoogleStorageBucketEncryption"], result)

    @builtins.property
    def force_destroy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''When deleting a bucket, this boolean option will delete all contained objects.

        If you try to delete a bucket that contains objects, Terraform will fail that run.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#force_destroy GoogleStorageBucket#force_destroy}
        '''
        result = self._values.get("force_destroy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#id GoogleStorageBucket#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A set of key/value label pairs to assign to the bucket.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#labels GoogleStorageBucket#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def lifecycle_rule(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleStorageBucketLifecycleRule"]]]:
        '''lifecycle_rule block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#lifecycle_rule GoogleStorageBucket#lifecycle_rule}
        '''
        result = self._values.get("lifecycle_rule")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleStorageBucketLifecycleRule"]]], result)

    @builtins.property
    def logging(self) -> typing.Optional["GoogleStorageBucketLogging"]:
        '''logging block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#logging GoogleStorageBucket#logging}
        '''
        result = self._values.get("logging")
        return typing.cast(typing.Optional["GoogleStorageBucketLogging"], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''The ID of the project in which the resource belongs.

        If it is not provided, the provider project is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#project GoogleStorageBucket#project}
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def public_access_prevention(self) -> typing.Optional[builtins.str]:
        '''Prevents public access to a bucket.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#public_access_prevention GoogleStorageBucket#public_access_prevention}
        '''
        result = self._values.get("public_access_prevention")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def requester_pays(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enables Requester Pays on a storage bucket.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#requester_pays GoogleStorageBucket#requester_pays}
        '''
        result = self._values.get("requester_pays")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def retention_policy(self) -> typing.Optional["GoogleStorageBucketRetentionPolicy"]:
        '''retention_policy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#retention_policy GoogleStorageBucket#retention_policy}
        '''
        result = self._values.get("retention_policy")
        return typing.cast(typing.Optional["GoogleStorageBucketRetentionPolicy"], result)

    @builtins.property
    def storage_class(self) -> typing.Optional[builtins.str]:
        '''The Storage Class of the new bucket. Supported values include: STANDARD, MULTI_REGIONAL, REGIONAL, NEARLINE, COLDLINE, ARCHIVE.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#storage_class GoogleStorageBucket#storage_class}
        '''
        result = self._values.get("storage_class")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleStorageBucketTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#timeouts GoogleStorageBucket#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleStorageBucketTimeouts"], result)

    @builtins.property
    def uniform_bucket_level_access(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Enables uniform bucket-level access on a bucket.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#uniform_bucket_level_access GoogleStorageBucket#uniform_bucket_level_access}
        '''
        result = self._values.get("uniform_bucket_level_access")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def versioning(self) -> typing.Optional["GoogleStorageBucketVersioning"]:
        '''versioning block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#versioning GoogleStorageBucket#versioning}
        '''
        result = self._values.get("versioning")
        return typing.cast(typing.Optional["GoogleStorageBucketVersioning"], result)

    @builtins.property
    def website(self) -> typing.Optional["GoogleStorageBucketWebsite"]:
        '''website block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#website GoogleStorageBucket#website}
        '''
        result = self._values.get("website")
        return typing.cast(typing.Optional["GoogleStorageBucketWebsite"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleStorageBucketConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleStorageBucket.GoogleStorageBucketCors",
    jsii_struct_bases=[],
    name_mapping={
        "max_age_seconds": "maxAgeSeconds",
        "method": "method",
        "origin": "origin",
        "response_header": "responseHeader",
    },
)
class GoogleStorageBucketCors:
    def __init__(
        self,
        *,
        max_age_seconds: typing.Optional[jsii.Number] = None,
        method: typing.Optional[typing.Sequence[builtins.str]] = None,
        origin: typing.Optional[typing.Sequence[builtins.str]] = None,
        response_header: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param max_age_seconds: The value, in seconds, to return in the Access-Control-Max-Age header used in preflight responses. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#max_age_seconds GoogleStorageBucket#max_age_seconds}
        :param method: The list of HTTP methods on which to include CORS response headers, (GET, OPTIONS, POST, etc) Note: "*" is permitted in the list of methods, and means "any method". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#method GoogleStorageBucket#method}
        :param origin: The list of Origins eligible to receive CORS response headers. Note: "*" is permitted in the list of origins, and means "any Origin". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#origin GoogleStorageBucket#origin}
        :param response_header: The list of HTTP headers other than the simple response headers to give permission for the user-agent to share across domains. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#response_header GoogleStorageBucket#response_header}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleStorageBucketCors.__init__)
            check_type(argname="argument max_age_seconds", value=max_age_seconds, expected_type=type_hints["max_age_seconds"])
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument origin", value=origin, expected_type=type_hints["origin"])
            check_type(argname="argument response_header", value=response_header, expected_type=type_hints["response_header"])
        self._values: typing.Dict[str, typing.Any] = {}
        if max_age_seconds is not None:
            self._values["max_age_seconds"] = max_age_seconds
        if method is not None:
            self._values["method"] = method
        if origin is not None:
            self._values["origin"] = origin
        if response_header is not None:
            self._values["response_header"] = response_header

    @builtins.property
    def max_age_seconds(self) -> typing.Optional[jsii.Number]:
        '''The value, in seconds, to return in the Access-Control-Max-Age header used in preflight responses.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#max_age_seconds GoogleStorageBucket#max_age_seconds}
        '''
        result = self._values.get("max_age_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def method(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of HTTP methods on which to include CORS response headers, (GET, OPTIONS, POST, etc) Note: "*" is permitted in the list of methods, and means "any method".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#method GoogleStorageBucket#method}
        '''
        result = self._values.get("method")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def origin(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of Origins eligible to receive CORS response headers.

        Note: "*" is permitted in the list of origins, and means "any Origin".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#origin GoogleStorageBucket#origin}
        '''
        result = self._values.get("origin")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def response_header(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of HTTP headers other than the simple response headers to give permission for the user-agent to share across domains.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#response_header GoogleStorageBucket#response_header}
        '''
        result = self._values.get("response_header")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleStorageBucketCors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleStorageBucketCorsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleStorageBucket.GoogleStorageBucketCorsList",
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
            type_hints = typing.get_type_hints(GoogleStorageBucketCorsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GoogleStorageBucketCorsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleStorageBucketCorsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleStorageBucketCorsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketCorsList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketCorsList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketCorsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleStorageBucketCors]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleStorageBucketCors]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleStorageBucketCors]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketCorsList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleStorageBucketCorsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleStorageBucket.GoogleStorageBucketCorsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleStorageBucketCorsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetMaxAgeSeconds")
    def reset_max_age_seconds(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxAgeSeconds", []))

    @jsii.member(jsii_name="resetMethod")
    def reset_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMethod", []))

    @jsii.member(jsii_name="resetOrigin")
    def reset_origin(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOrigin", []))

    @jsii.member(jsii_name="resetResponseHeader")
    def reset_response_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResponseHeader", []))

    @builtins.property
    @jsii.member(jsii_name="maxAgeSecondsInput")
    def max_age_seconds_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxAgeSecondsInput"))

    @builtins.property
    @jsii.member(jsii_name="methodInput")
    def method_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "methodInput"))

    @builtins.property
    @jsii.member(jsii_name="originInput")
    def origin_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "originInput"))

    @builtins.property
    @jsii.member(jsii_name="responseHeaderInput")
    def response_header_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "responseHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="maxAgeSeconds")
    def max_age_seconds(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxAgeSeconds"))

    @max_age_seconds.setter
    def max_age_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketCorsOutputReference, "max_age_seconds").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxAgeSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="method")
    def method(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "method"))

    @method.setter
    def method(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketCorsOutputReference, "method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "method", value)

    @builtins.property
    @jsii.member(jsii_name="origin")
    def origin(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "origin"))

    @origin.setter
    def origin(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketCorsOutputReference, "origin").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "origin", value)

    @builtins.property
    @jsii.member(jsii_name="responseHeader")
    def response_header(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "responseHeader"))

    @response_header.setter
    def response_header(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketCorsOutputReference, "response_header").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseHeader", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleStorageBucketCors, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleStorageBucketCors, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleStorageBucketCors, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketCorsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleStorageBucket.GoogleStorageBucketCustomPlacementConfig",
    jsii_struct_bases=[],
    name_mapping={"data_locations": "dataLocations"},
)
class GoogleStorageBucketCustomPlacementConfig:
    def __init__(self, *, data_locations: typing.Sequence[builtins.str]) -> None:
        '''
        :param data_locations: The list of individual regions that comprise a dual-region bucket. See the docs for a list of acceptable regions. Note: If any of the data_locations changes, it will recreate the bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#data_locations GoogleStorageBucket#data_locations}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleStorageBucketCustomPlacementConfig.__init__)
            check_type(argname="argument data_locations", value=data_locations, expected_type=type_hints["data_locations"])
        self._values: typing.Dict[str, typing.Any] = {
            "data_locations": data_locations,
        }

    @builtins.property
    def data_locations(self) -> typing.List[builtins.str]:
        '''The list of individual regions that comprise a dual-region bucket.

        See the docs for a list of acceptable regions. Note: If any of the data_locations changes, it will recreate the bucket.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#data_locations GoogleStorageBucket#data_locations}
        '''
        result = self._values.get("data_locations")
        assert result is not None, "Required property 'data_locations' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleStorageBucketCustomPlacementConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleStorageBucketCustomPlacementConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleStorageBucket.GoogleStorageBucketCustomPlacementConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleStorageBucketCustomPlacementConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="dataLocationsInput")
    def data_locations_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dataLocationsInput"))

    @builtins.property
    @jsii.member(jsii_name="dataLocations")
    def data_locations(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "dataLocations"))

    @data_locations.setter
    def data_locations(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketCustomPlacementConfigOutputReference, "data_locations").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataLocations", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleStorageBucketCustomPlacementConfig]:
        return typing.cast(typing.Optional[GoogleStorageBucketCustomPlacementConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleStorageBucketCustomPlacementConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketCustomPlacementConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleStorageBucket.GoogleStorageBucketEncryption",
    jsii_struct_bases=[],
    name_mapping={"default_kms_key_name": "defaultKmsKeyName"},
)
class GoogleStorageBucketEncryption:
    def __init__(self, *, default_kms_key_name: builtins.str) -> None:
        '''
        :param default_kms_key_name: A Cloud KMS key that will be used to encrypt objects inserted into this bucket, if no encryption method is specified. You must pay attention to whether the crypto key is available in the location that this bucket is created in. See the docs for more details. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#default_kms_key_name GoogleStorageBucket#default_kms_key_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleStorageBucketEncryption.__init__)
            check_type(argname="argument default_kms_key_name", value=default_kms_key_name, expected_type=type_hints["default_kms_key_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "default_kms_key_name": default_kms_key_name,
        }

    @builtins.property
    def default_kms_key_name(self) -> builtins.str:
        '''A Cloud KMS key that will be used to encrypt objects inserted into this bucket, if no encryption method is specified.

        You must pay attention to whether the crypto key is available in the location that this bucket is created in. See the docs for more details.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#default_kms_key_name GoogleStorageBucket#default_kms_key_name}
        '''
        result = self._values.get("default_kms_key_name")
        assert result is not None, "Required property 'default_kms_key_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleStorageBucketEncryption(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleStorageBucketEncryptionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleStorageBucket.GoogleStorageBucketEncryptionOutputReference",
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
            type_hints = typing.get_type_hints(GoogleStorageBucketEncryptionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="defaultKmsKeyNameInput")
    def default_kms_key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultKmsKeyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultKmsKeyName")
    def default_kms_key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultKmsKeyName"))

    @default_kms_key_name.setter
    def default_kms_key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketEncryptionOutputReference, "default_kms_key_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultKmsKeyName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleStorageBucketEncryption]:
        return typing.cast(typing.Optional[GoogleStorageBucketEncryption], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleStorageBucketEncryption],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketEncryptionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleStorageBucket.GoogleStorageBucketLifecycleRule",
    jsii_struct_bases=[],
    name_mapping={"action": "action", "condition": "condition"},
)
class GoogleStorageBucketLifecycleRule:
    def __init__(
        self,
        *,
        action: typing.Union["GoogleStorageBucketLifecycleRuleAction", typing.Dict[str, typing.Any]],
        condition: typing.Union["GoogleStorageBucketLifecycleRuleCondition", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param action: action block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#action GoogleStorageBucket#action}
        :param condition: condition block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#condition GoogleStorageBucket#condition}
        '''
        if isinstance(action, dict):
            action = GoogleStorageBucketLifecycleRuleAction(**action)
        if isinstance(condition, dict):
            condition = GoogleStorageBucketLifecycleRuleCondition(**condition)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleStorageBucketLifecycleRule.__init__)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
            "condition": condition,
        }

    @builtins.property
    def action(self) -> "GoogleStorageBucketLifecycleRuleAction":
        '''action block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#action GoogleStorageBucket#action}
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast("GoogleStorageBucketLifecycleRuleAction", result)

    @builtins.property
    def condition(self) -> "GoogleStorageBucketLifecycleRuleCondition":
        '''condition block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#condition GoogleStorageBucket#condition}
        '''
        result = self._values.get("condition")
        assert result is not None, "Required property 'condition' is missing"
        return typing.cast("GoogleStorageBucketLifecycleRuleCondition", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleStorageBucketLifecycleRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleStorageBucket.GoogleStorageBucketLifecycleRuleAction",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "storage_class": "storageClass"},
)
class GoogleStorageBucketLifecycleRuleAction:
    def __init__(
        self,
        *,
        type: builtins.str,
        storage_class: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: The type of the action of this Lifecycle Rule. Supported values include: Delete and SetStorageClass. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#type GoogleStorageBucket#type}
        :param storage_class: The target Storage Class of objects affected by this Lifecycle Rule. Supported values include: MULTI_REGIONAL, REGIONAL, NEARLINE, COLDLINE, ARCHIVE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#storage_class GoogleStorageBucket#storage_class}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleStorageBucketLifecycleRuleAction.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument storage_class", value=storage_class, expected_type=type_hints["storage_class"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if storage_class is not None:
            self._values["storage_class"] = storage_class

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of the action of this Lifecycle Rule. Supported values include: Delete and SetStorageClass.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#type GoogleStorageBucket#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_class(self) -> typing.Optional[builtins.str]:
        '''The target Storage Class of objects affected by this Lifecycle Rule. Supported values include: MULTI_REGIONAL, REGIONAL, NEARLINE, COLDLINE, ARCHIVE.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#storage_class GoogleStorageBucket#storage_class}
        '''
        result = self._values.get("storage_class")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleStorageBucketLifecycleRuleAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleStorageBucketLifecycleRuleActionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleStorageBucket.GoogleStorageBucketLifecycleRuleActionOutputReference",
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
            type_hints = typing.get_type_hints(GoogleStorageBucketLifecycleRuleActionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetStorageClass")
    def reset_storage_class(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStorageClass", []))

    @builtins.property
    @jsii.member(jsii_name="storageClassInput")
    def storage_class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "storageClassInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="storageClass")
    def storage_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "storageClass"))

    @storage_class.setter
    def storage_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketLifecycleRuleActionOutputReference, "storage_class").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageClass", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketLifecycleRuleActionOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleStorageBucketLifecycleRuleAction]:
        return typing.cast(typing.Optional[GoogleStorageBucketLifecycleRuleAction], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleStorageBucketLifecycleRuleAction],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketLifecycleRuleActionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleStorageBucket.GoogleStorageBucketLifecycleRuleCondition",
    jsii_struct_bases=[],
    name_mapping={
        "age": "age",
        "created_before": "createdBefore",
        "custom_time_before": "customTimeBefore",
        "days_since_custom_time": "daysSinceCustomTime",
        "days_since_noncurrent_time": "daysSinceNoncurrentTime",
        "matches_prefix": "matchesPrefix",
        "matches_storage_class": "matchesStorageClass",
        "matches_suffix": "matchesSuffix",
        "noncurrent_time_before": "noncurrentTimeBefore",
        "num_newer_versions": "numNewerVersions",
        "with_state": "withState",
    },
)
class GoogleStorageBucketLifecycleRuleCondition:
    def __init__(
        self,
        *,
        age: typing.Optional[jsii.Number] = None,
        created_before: typing.Optional[builtins.str] = None,
        custom_time_before: typing.Optional[builtins.str] = None,
        days_since_custom_time: typing.Optional[jsii.Number] = None,
        days_since_noncurrent_time: typing.Optional[jsii.Number] = None,
        matches_prefix: typing.Optional[typing.Sequence[builtins.str]] = None,
        matches_storage_class: typing.Optional[typing.Sequence[builtins.str]] = None,
        matches_suffix: typing.Optional[typing.Sequence[builtins.str]] = None,
        noncurrent_time_before: typing.Optional[builtins.str] = None,
        num_newer_versions: typing.Optional[jsii.Number] = None,
        with_state: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param age: Minimum age of an object in days to satisfy this condition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#age GoogleStorageBucket#age}
        :param created_before: Creation date of an object in RFC 3339 (e.g. 2017-06-13) to satisfy this condition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#created_before GoogleStorageBucket#created_before}
        :param custom_time_before: Creation date of an object in RFC 3339 (e.g. 2017-06-13) to satisfy this condition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#custom_time_before GoogleStorageBucket#custom_time_before}
        :param days_since_custom_time: Number of days elapsed since the user-specified timestamp set on an object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#days_since_custom_time GoogleStorageBucket#days_since_custom_time}
        :param days_since_noncurrent_time: Number of days elapsed since the noncurrent timestamp of an object. This condition is relevant only for versioned objects. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#days_since_noncurrent_time GoogleStorageBucket#days_since_noncurrent_time}
        :param matches_prefix: One or more matching name prefixes to satisfy this condition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#matches_prefix GoogleStorageBucket#matches_prefix}
        :param matches_storage_class: Storage Class of objects to satisfy this condition. Supported values include: MULTI_REGIONAL, REGIONAL, NEARLINE, COLDLINE, ARCHIVE, STANDARD, DURABLE_REDUCED_AVAILABILITY. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#matches_storage_class GoogleStorageBucket#matches_storage_class}
        :param matches_suffix: One or more matching name suffixes to satisfy this condition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#matches_suffix GoogleStorageBucket#matches_suffix}
        :param noncurrent_time_before: Creation date of an object in RFC 3339 (e.g. 2017-06-13) to satisfy this condition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#noncurrent_time_before GoogleStorageBucket#noncurrent_time_before}
        :param num_newer_versions: Relevant only for versioned objects. The number of newer versions of an object to satisfy this condition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#num_newer_versions GoogleStorageBucket#num_newer_versions}
        :param with_state: Match to live and/or archived objects. Unversioned buckets have only live objects. Supported values include: "LIVE", "ARCHIVED", "ANY". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#with_state GoogleStorageBucket#with_state}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleStorageBucketLifecycleRuleCondition.__init__)
            check_type(argname="argument age", value=age, expected_type=type_hints["age"])
            check_type(argname="argument created_before", value=created_before, expected_type=type_hints["created_before"])
            check_type(argname="argument custom_time_before", value=custom_time_before, expected_type=type_hints["custom_time_before"])
            check_type(argname="argument days_since_custom_time", value=days_since_custom_time, expected_type=type_hints["days_since_custom_time"])
            check_type(argname="argument days_since_noncurrent_time", value=days_since_noncurrent_time, expected_type=type_hints["days_since_noncurrent_time"])
            check_type(argname="argument matches_prefix", value=matches_prefix, expected_type=type_hints["matches_prefix"])
            check_type(argname="argument matches_storage_class", value=matches_storage_class, expected_type=type_hints["matches_storage_class"])
            check_type(argname="argument matches_suffix", value=matches_suffix, expected_type=type_hints["matches_suffix"])
            check_type(argname="argument noncurrent_time_before", value=noncurrent_time_before, expected_type=type_hints["noncurrent_time_before"])
            check_type(argname="argument num_newer_versions", value=num_newer_versions, expected_type=type_hints["num_newer_versions"])
            check_type(argname="argument with_state", value=with_state, expected_type=type_hints["with_state"])
        self._values: typing.Dict[str, typing.Any] = {}
        if age is not None:
            self._values["age"] = age
        if created_before is not None:
            self._values["created_before"] = created_before
        if custom_time_before is not None:
            self._values["custom_time_before"] = custom_time_before
        if days_since_custom_time is not None:
            self._values["days_since_custom_time"] = days_since_custom_time
        if days_since_noncurrent_time is not None:
            self._values["days_since_noncurrent_time"] = days_since_noncurrent_time
        if matches_prefix is not None:
            self._values["matches_prefix"] = matches_prefix
        if matches_storage_class is not None:
            self._values["matches_storage_class"] = matches_storage_class
        if matches_suffix is not None:
            self._values["matches_suffix"] = matches_suffix
        if noncurrent_time_before is not None:
            self._values["noncurrent_time_before"] = noncurrent_time_before
        if num_newer_versions is not None:
            self._values["num_newer_versions"] = num_newer_versions
        if with_state is not None:
            self._values["with_state"] = with_state

    @builtins.property
    def age(self) -> typing.Optional[jsii.Number]:
        '''Minimum age of an object in days to satisfy this condition.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#age GoogleStorageBucket#age}
        '''
        result = self._values.get("age")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def created_before(self) -> typing.Optional[builtins.str]:
        '''Creation date of an object in RFC 3339 (e.g. 2017-06-13) to satisfy this condition.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#created_before GoogleStorageBucket#created_before}
        '''
        result = self._values.get("created_before")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_time_before(self) -> typing.Optional[builtins.str]:
        '''Creation date of an object in RFC 3339 (e.g. 2017-06-13) to satisfy this condition.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#custom_time_before GoogleStorageBucket#custom_time_before}
        '''
        result = self._values.get("custom_time_before")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def days_since_custom_time(self) -> typing.Optional[jsii.Number]:
        '''Number of days elapsed since the user-specified timestamp set on an object.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#days_since_custom_time GoogleStorageBucket#days_since_custom_time}
        '''
        result = self._values.get("days_since_custom_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def days_since_noncurrent_time(self) -> typing.Optional[jsii.Number]:
        '''Number of days elapsed since the noncurrent timestamp of an object. This 							condition is relevant only for versioned objects.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#days_since_noncurrent_time GoogleStorageBucket#days_since_noncurrent_time}
        '''
        result = self._values.get("days_since_noncurrent_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def matches_prefix(self) -> typing.Optional[typing.List[builtins.str]]:
        '''One or more matching name prefixes to satisfy this condition.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#matches_prefix GoogleStorageBucket#matches_prefix}
        '''
        result = self._values.get("matches_prefix")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def matches_storage_class(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Storage Class of objects to satisfy this condition. Supported values include: MULTI_REGIONAL, REGIONAL, NEARLINE, COLDLINE, ARCHIVE, STANDARD, DURABLE_REDUCED_AVAILABILITY.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#matches_storage_class GoogleStorageBucket#matches_storage_class}
        '''
        result = self._values.get("matches_storage_class")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def matches_suffix(self) -> typing.Optional[typing.List[builtins.str]]:
        '''One or more matching name suffixes to satisfy this condition.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#matches_suffix GoogleStorageBucket#matches_suffix}
        '''
        result = self._values.get("matches_suffix")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def noncurrent_time_before(self) -> typing.Optional[builtins.str]:
        '''Creation date of an object in RFC 3339 (e.g. 2017-06-13) to satisfy this condition.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#noncurrent_time_before GoogleStorageBucket#noncurrent_time_before}
        '''
        result = self._values.get("noncurrent_time_before")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def num_newer_versions(self) -> typing.Optional[jsii.Number]:
        '''Relevant only for versioned objects. The number of newer versions of an object to satisfy this condition.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#num_newer_versions GoogleStorageBucket#num_newer_versions}
        '''
        result = self._values.get("num_newer_versions")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def with_state(self) -> typing.Optional[builtins.str]:
        '''Match to live and/or archived objects. Unversioned buckets have only live objects. Supported values include: "LIVE", "ARCHIVED", "ANY".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#with_state GoogleStorageBucket#with_state}
        '''
        result = self._values.get("with_state")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleStorageBucketLifecycleRuleCondition(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleStorageBucketLifecycleRuleConditionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleStorageBucket.GoogleStorageBucketLifecycleRuleConditionOutputReference",
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
            type_hints = typing.get_type_hints(GoogleStorageBucketLifecycleRuleConditionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAge")
    def reset_age(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAge", []))

    @jsii.member(jsii_name="resetCreatedBefore")
    def reset_created_before(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreatedBefore", []))

    @jsii.member(jsii_name="resetCustomTimeBefore")
    def reset_custom_time_before(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCustomTimeBefore", []))

    @jsii.member(jsii_name="resetDaysSinceCustomTime")
    def reset_days_since_custom_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDaysSinceCustomTime", []))

    @jsii.member(jsii_name="resetDaysSinceNoncurrentTime")
    def reset_days_since_noncurrent_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDaysSinceNoncurrentTime", []))

    @jsii.member(jsii_name="resetMatchesPrefix")
    def reset_matches_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchesPrefix", []))

    @jsii.member(jsii_name="resetMatchesStorageClass")
    def reset_matches_storage_class(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchesStorageClass", []))

    @jsii.member(jsii_name="resetMatchesSuffix")
    def reset_matches_suffix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMatchesSuffix", []))

    @jsii.member(jsii_name="resetNoncurrentTimeBefore")
    def reset_noncurrent_time_before(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNoncurrentTimeBefore", []))

    @jsii.member(jsii_name="resetNumNewerVersions")
    def reset_num_newer_versions(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNumNewerVersions", []))

    @jsii.member(jsii_name="resetWithState")
    def reset_with_state(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWithState", []))

    @builtins.property
    @jsii.member(jsii_name="ageInput")
    def age_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ageInput"))

    @builtins.property
    @jsii.member(jsii_name="createdBeforeInput")
    def created_before_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createdBeforeInput"))

    @builtins.property
    @jsii.member(jsii_name="customTimeBeforeInput")
    def custom_time_before_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customTimeBeforeInput"))

    @builtins.property
    @jsii.member(jsii_name="daysSinceCustomTimeInput")
    def days_since_custom_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "daysSinceCustomTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="daysSinceNoncurrentTimeInput")
    def days_since_noncurrent_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "daysSinceNoncurrentTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="matchesPrefixInput")
    def matches_prefix_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchesPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="matchesStorageClassInput")
    def matches_storage_class_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchesStorageClassInput"))

    @builtins.property
    @jsii.member(jsii_name="matchesSuffixInput")
    def matches_suffix_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "matchesSuffixInput"))

    @builtins.property
    @jsii.member(jsii_name="noncurrentTimeBeforeInput")
    def noncurrent_time_before_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "noncurrentTimeBeforeInput"))

    @builtins.property
    @jsii.member(jsii_name="numNewerVersionsInput")
    def num_newer_versions_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "numNewerVersionsInput"))

    @builtins.property
    @jsii.member(jsii_name="withStateInput")
    def with_state_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "withStateInput"))

    @builtins.property
    @jsii.member(jsii_name="age")
    def age(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "age"))

    @age.setter
    def age(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketLifecycleRuleConditionOutputReference, "age").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "age", value)

    @builtins.property
    @jsii.member(jsii_name="createdBefore")
    def created_before(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createdBefore"))

    @created_before.setter
    def created_before(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketLifecycleRuleConditionOutputReference, "created_before").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createdBefore", value)

    @builtins.property
    @jsii.member(jsii_name="customTimeBefore")
    def custom_time_before(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "customTimeBefore"))

    @custom_time_before.setter
    def custom_time_before(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketLifecycleRuleConditionOutputReference, "custom_time_before").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customTimeBefore", value)

    @builtins.property
    @jsii.member(jsii_name="daysSinceCustomTime")
    def days_since_custom_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "daysSinceCustomTime"))

    @days_since_custom_time.setter
    def days_since_custom_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketLifecycleRuleConditionOutputReference, "days_since_custom_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "daysSinceCustomTime", value)

    @builtins.property
    @jsii.member(jsii_name="daysSinceNoncurrentTime")
    def days_since_noncurrent_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "daysSinceNoncurrentTime"))

    @days_since_noncurrent_time.setter
    def days_since_noncurrent_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketLifecycleRuleConditionOutputReference, "days_since_noncurrent_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "daysSinceNoncurrentTime", value)

    @builtins.property
    @jsii.member(jsii_name="matchesPrefix")
    def matches_prefix(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchesPrefix"))

    @matches_prefix.setter
    def matches_prefix(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketLifecycleRuleConditionOutputReference, "matches_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchesPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="matchesStorageClass")
    def matches_storage_class(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchesStorageClass"))

    @matches_storage_class.setter
    def matches_storage_class(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketLifecycleRuleConditionOutputReference, "matches_storage_class").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchesStorageClass", value)

    @builtins.property
    @jsii.member(jsii_name="matchesSuffix")
    def matches_suffix(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "matchesSuffix"))

    @matches_suffix.setter
    def matches_suffix(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketLifecycleRuleConditionOutputReference, "matches_suffix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "matchesSuffix", value)

    @builtins.property
    @jsii.member(jsii_name="noncurrentTimeBefore")
    def noncurrent_time_before(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "noncurrentTimeBefore"))

    @noncurrent_time_before.setter
    def noncurrent_time_before(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketLifecycleRuleConditionOutputReference, "noncurrent_time_before").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "noncurrentTimeBefore", value)

    @builtins.property
    @jsii.member(jsii_name="numNewerVersions")
    def num_newer_versions(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numNewerVersions"))

    @num_newer_versions.setter
    def num_newer_versions(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketLifecycleRuleConditionOutputReference, "num_newer_versions").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "numNewerVersions", value)

    @builtins.property
    @jsii.member(jsii_name="withState")
    def with_state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "withState"))

    @with_state.setter
    def with_state(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketLifecycleRuleConditionOutputReference, "with_state").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "withState", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleStorageBucketLifecycleRuleCondition]:
        return typing.cast(typing.Optional[GoogleStorageBucketLifecycleRuleCondition], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleStorageBucketLifecycleRuleCondition],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketLifecycleRuleConditionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleStorageBucketLifecycleRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleStorageBucket.GoogleStorageBucketLifecycleRuleList",
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
            type_hints = typing.get_type_hints(GoogleStorageBucketLifecycleRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleStorageBucketLifecycleRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleStorageBucketLifecycleRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleStorageBucketLifecycleRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketLifecycleRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketLifecycleRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketLifecycleRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleStorageBucketLifecycleRule]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleStorageBucketLifecycleRule]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleStorageBucketLifecycleRule]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketLifecycleRuleList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleStorageBucketLifecycleRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleStorageBucket.GoogleStorageBucketLifecycleRuleOutputReference",
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
            type_hints = typing.get_type_hints(GoogleStorageBucketLifecycleRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="putAction")
    def put_action(
        self,
        *,
        type: builtins.str,
        storage_class: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: The type of the action of this Lifecycle Rule. Supported values include: Delete and SetStorageClass. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#type GoogleStorageBucket#type}
        :param storage_class: The target Storage Class of objects affected by this Lifecycle Rule. Supported values include: MULTI_REGIONAL, REGIONAL, NEARLINE, COLDLINE, ARCHIVE. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#storage_class GoogleStorageBucket#storage_class}
        '''
        value = GoogleStorageBucketLifecycleRuleAction(
            type=type, storage_class=storage_class
        )

        return typing.cast(None, jsii.invoke(self, "putAction", [value]))

    @jsii.member(jsii_name="putCondition")
    def put_condition(
        self,
        *,
        age: typing.Optional[jsii.Number] = None,
        created_before: typing.Optional[builtins.str] = None,
        custom_time_before: typing.Optional[builtins.str] = None,
        days_since_custom_time: typing.Optional[jsii.Number] = None,
        days_since_noncurrent_time: typing.Optional[jsii.Number] = None,
        matches_prefix: typing.Optional[typing.Sequence[builtins.str]] = None,
        matches_storage_class: typing.Optional[typing.Sequence[builtins.str]] = None,
        matches_suffix: typing.Optional[typing.Sequence[builtins.str]] = None,
        noncurrent_time_before: typing.Optional[builtins.str] = None,
        num_newer_versions: typing.Optional[jsii.Number] = None,
        with_state: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param age: Minimum age of an object in days to satisfy this condition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#age GoogleStorageBucket#age}
        :param created_before: Creation date of an object in RFC 3339 (e.g. 2017-06-13) to satisfy this condition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#created_before GoogleStorageBucket#created_before}
        :param custom_time_before: Creation date of an object in RFC 3339 (e.g. 2017-06-13) to satisfy this condition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#custom_time_before GoogleStorageBucket#custom_time_before}
        :param days_since_custom_time: Number of days elapsed since the user-specified timestamp set on an object. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#days_since_custom_time GoogleStorageBucket#days_since_custom_time}
        :param days_since_noncurrent_time: Number of days elapsed since the noncurrent timestamp of an object. This condition is relevant only for versioned objects. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#days_since_noncurrent_time GoogleStorageBucket#days_since_noncurrent_time}
        :param matches_prefix: One or more matching name prefixes to satisfy this condition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#matches_prefix GoogleStorageBucket#matches_prefix}
        :param matches_storage_class: Storage Class of objects to satisfy this condition. Supported values include: MULTI_REGIONAL, REGIONAL, NEARLINE, COLDLINE, ARCHIVE, STANDARD, DURABLE_REDUCED_AVAILABILITY. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#matches_storage_class GoogleStorageBucket#matches_storage_class}
        :param matches_suffix: One or more matching name suffixes to satisfy this condition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#matches_suffix GoogleStorageBucket#matches_suffix}
        :param noncurrent_time_before: Creation date of an object in RFC 3339 (e.g. 2017-06-13) to satisfy this condition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#noncurrent_time_before GoogleStorageBucket#noncurrent_time_before}
        :param num_newer_versions: Relevant only for versioned objects. The number of newer versions of an object to satisfy this condition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#num_newer_versions GoogleStorageBucket#num_newer_versions}
        :param with_state: Match to live and/or archived objects. Unversioned buckets have only live objects. Supported values include: "LIVE", "ARCHIVED", "ANY". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#with_state GoogleStorageBucket#with_state}
        '''
        value = GoogleStorageBucketLifecycleRuleCondition(
            age=age,
            created_before=created_before,
            custom_time_before=custom_time_before,
            days_since_custom_time=days_since_custom_time,
            days_since_noncurrent_time=days_since_noncurrent_time,
            matches_prefix=matches_prefix,
            matches_storage_class=matches_storage_class,
            matches_suffix=matches_suffix,
            noncurrent_time_before=noncurrent_time_before,
            num_newer_versions=num_newer_versions,
            with_state=with_state,
        )

        return typing.cast(None, jsii.invoke(self, "putCondition", [value]))

    @builtins.property
    @jsii.member(jsii_name="action")
    def action(self) -> GoogleStorageBucketLifecycleRuleActionOutputReference:
        return typing.cast(GoogleStorageBucketLifecycleRuleActionOutputReference, jsii.get(self, "action"))

    @builtins.property
    @jsii.member(jsii_name="condition")
    def condition(self) -> GoogleStorageBucketLifecycleRuleConditionOutputReference:
        return typing.cast(GoogleStorageBucketLifecycleRuleConditionOutputReference, jsii.get(self, "condition"))

    @builtins.property
    @jsii.member(jsii_name="actionInput")
    def action_input(self) -> typing.Optional[GoogleStorageBucketLifecycleRuleAction]:
        return typing.cast(typing.Optional[GoogleStorageBucketLifecycleRuleAction], jsii.get(self, "actionInput"))

    @builtins.property
    @jsii.member(jsii_name="conditionInput")
    def condition_input(
        self,
    ) -> typing.Optional[GoogleStorageBucketLifecycleRuleCondition]:
        return typing.cast(typing.Optional[GoogleStorageBucketLifecycleRuleCondition], jsii.get(self, "conditionInput"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleStorageBucketLifecycleRule, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleStorageBucketLifecycleRule, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleStorageBucketLifecycleRule, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketLifecycleRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleStorageBucket.GoogleStorageBucketLogging",
    jsii_struct_bases=[],
    name_mapping={"log_bucket": "logBucket", "log_object_prefix": "logObjectPrefix"},
)
class GoogleStorageBucketLogging:
    def __init__(
        self,
        *,
        log_bucket: builtins.str,
        log_object_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param log_bucket: The bucket that will receive log objects. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#log_bucket GoogleStorageBucket#log_bucket}
        :param log_object_prefix: The object prefix for log objects. If it's not provided, by default Google Cloud Storage sets this to this bucket's name. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#log_object_prefix GoogleStorageBucket#log_object_prefix}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleStorageBucketLogging.__init__)
            check_type(argname="argument log_bucket", value=log_bucket, expected_type=type_hints["log_bucket"])
            check_type(argname="argument log_object_prefix", value=log_object_prefix, expected_type=type_hints["log_object_prefix"])
        self._values: typing.Dict[str, typing.Any] = {
            "log_bucket": log_bucket,
        }
        if log_object_prefix is not None:
            self._values["log_object_prefix"] = log_object_prefix

    @builtins.property
    def log_bucket(self) -> builtins.str:
        '''The bucket that will receive log objects.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#log_bucket GoogleStorageBucket#log_bucket}
        '''
        result = self._values.get("log_bucket")
        assert result is not None, "Required property 'log_bucket' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_object_prefix(self) -> typing.Optional[builtins.str]:
        '''The object prefix for log objects.

        If it's not provided, by default Google Cloud Storage sets this to this bucket's name.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#log_object_prefix GoogleStorageBucket#log_object_prefix}
        '''
        result = self._values.get("log_object_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleStorageBucketLogging(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleStorageBucketLoggingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleStorageBucket.GoogleStorageBucketLoggingOutputReference",
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
            type_hints = typing.get_type_hints(GoogleStorageBucketLoggingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetLogObjectPrefix")
    def reset_log_object_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogObjectPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="logBucketInput")
    def log_bucket_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logBucketInput"))

    @builtins.property
    @jsii.member(jsii_name="logObjectPrefixInput")
    def log_object_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logObjectPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="logBucket")
    def log_bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logBucket"))

    @log_bucket.setter
    def log_bucket(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketLoggingOutputReference, "log_bucket").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logBucket", value)

    @builtins.property
    @jsii.member(jsii_name="logObjectPrefix")
    def log_object_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logObjectPrefix"))

    @log_object_prefix.setter
    def log_object_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketLoggingOutputReference, "log_object_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logObjectPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleStorageBucketLogging]:
        return typing.cast(typing.Optional[GoogleStorageBucketLogging], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleStorageBucketLogging],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketLoggingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleStorageBucket.GoogleStorageBucketRetentionPolicy",
    jsii_struct_bases=[],
    name_mapping={"retention_period": "retentionPeriod", "is_locked": "isLocked"},
)
class GoogleStorageBucketRetentionPolicy:
    def __init__(
        self,
        *,
        retention_period: jsii.Number,
        is_locked: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param retention_period: The period of time, in seconds, that objects in the bucket must be retained and cannot be deleted, overwritten, or archived. The value must be less than 3,155,760,000 seconds. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#retention_period GoogleStorageBucket#retention_period}
        :param is_locked: If set to true, the bucket will be locked and permanently restrict edits to the bucket's retention policy. Caution: Locking a bucket is an irreversible action. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#is_locked GoogleStorageBucket#is_locked}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleStorageBucketRetentionPolicy.__init__)
            check_type(argname="argument retention_period", value=retention_period, expected_type=type_hints["retention_period"])
            check_type(argname="argument is_locked", value=is_locked, expected_type=type_hints["is_locked"])
        self._values: typing.Dict[str, typing.Any] = {
            "retention_period": retention_period,
        }
        if is_locked is not None:
            self._values["is_locked"] = is_locked

    @builtins.property
    def retention_period(self) -> jsii.Number:
        '''The period of time, in seconds, that objects in the bucket must be retained and cannot be deleted, overwritten, or archived.

        The value must be less than 3,155,760,000 seconds.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#retention_period GoogleStorageBucket#retention_period}
        '''
        result = self._values.get("retention_period")
        assert result is not None, "Required property 'retention_period' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def is_locked(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If set to true, the bucket will be locked and permanently restrict edits to the bucket's retention policy.

        Caution: Locking a bucket is an irreversible action.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#is_locked GoogleStorageBucket#is_locked}
        '''
        result = self._values.get("is_locked")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleStorageBucketRetentionPolicy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleStorageBucketRetentionPolicyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleStorageBucket.GoogleStorageBucketRetentionPolicyOutputReference",
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
            type_hints = typing.get_type_hints(GoogleStorageBucketRetentionPolicyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetIsLocked")
    def reset_is_locked(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIsLocked", []))

    @builtins.property
    @jsii.member(jsii_name="isLockedInput")
    def is_locked_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "isLockedInput"))

    @builtins.property
    @jsii.member(jsii_name="retentionPeriodInput")
    def retention_period_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "retentionPeriodInput"))

    @builtins.property
    @jsii.member(jsii_name="isLocked")
    def is_locked(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "isLocked"))

    @is_locked.setter
    def is_locked(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketRetentionPolicyOutputReference, "is_locked").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "isLocked", value)

    @builtins.property
    @jsii.member(jsii_name="retentionPeriod")
    def retention_period(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "retentionPeriod"))

    @retention_period.setter
    def retention_period(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketRetentionPolicyOutputReference, "retention_period").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleStorageBucketRetentionPolicy]:
        return typing.cast(typing.Optional[GoogleStorageBucketRetentionPolicy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleStorageBucketRetentionPolicy],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketRetentionPolicyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleStorageBucket.GoogleStorageBucketTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "read": "read", "update": "update"},
)
class GoogleStorageBucketTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        read: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#create GoogleStorageBucket#create}.
        :param read: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#read GoogleStorageBucket#read}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#update GoogleStorageBucket#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleStorageBucketTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument read", value=read, expected_type=type_hints["read"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if read is not None:
            self._values["read"] = read
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#create GoogleStorageBucket#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def read(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#read GoogleStorageBucket#read}.'''
        result = self._values.get("read")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#update GoogleStorageBucket#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleStorageBucketTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleStorageBucketTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleStorageBucket.GoogleStorageBucketTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleStorageBucketTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

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
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="read")
    def read(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "read"))

    @read.setter
    def read(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketTimeoutsOutputReference, "read").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "read", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleStorageBucketTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleStorageBucketTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleStorageBucketTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleStorageBucket.GoogleStorageBucketVersioning",
    jsii_struct_bases=[],
    name_mapping={"enabled": "enabled"},
)
class GoogleStorageBucketVersioning:
    def __init__(
        self,
        *,
        enabled: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param enabled: While set to true, versioning is fully enabled for this bucket. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#enabled GoogleStorageBucket#enabled}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleStorageBucketVersioning.__init__)
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "enabled": enabled,
        }

    @builtins.property
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''While set to true, versioning is fully enabled for this bucket.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#enabled GoogleStorageBucket#enabled}
        '''
        result = self._values.get("enabled")
        assert result is not None, "Required property 'enabled' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleStorageBucketVersioning(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleStorageBucketVersioningOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleStorageBucket.GoogleStorageBucketVersioningOutputReference",
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
            type_hints = typing.get_type_hints(GoogleStorageBucketVersioningOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

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
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketVersioningOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleStorageBucketVersioning]:
        return typing.cast(typing.Optional[GoogleStorageBucketVersioning], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleStorageBucketVersioning],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketVersioningOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleStorageBucket.GoogleStorageBucketWebsite",
    jsii_struct_bases=[],
    name_mapping={
        "main_page_suffix": "mainPageSuffix",
        "not_found_page": "notFoundPage",
    },
)
class GoogleStorageBucketWebsite:
    def __init__(
        self,
        *,
        main_page_suffix: typing.Optional[builtins.str] = None,
        not_found_page: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param main_page_suffix: Behaves as the bucket's directory index where missing objects are treated as potential directories. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#main_page_suffix GoogleStorageBucket#main_page_suffix}
        :param not_found_page: The custom object to return when a requested resource is not found. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#not_found_page GoogleStorageBucket#not_found_page}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleStorageBucketWebsite.__init__)
            check_type(argname="argument main_page_suffix", value=main_page_suffix, expected_type=type_hints["main_page_suffix"])
            check_type(argname="argument not_found_page", value=not_found_page, expected_type=type_hints["not_found_page"])
        self._values: typing.Dict[str, typing.Any] = {}
        if main_page_suffix is not None:
            self._values["main_page_suffix"] = main_page_suffix
        if not_found_page is not None:
            self._values["not_found_page"] = not_found_page

    @builtins.property
    def main_page_suffix(self) -> typing.Optional[builtins.str]:
        '''Behaves as the bucket's directory index where missing objects are treated as potential directories.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#main_page_suffix GoogleStorageBucket#main_page_suffix}
        '''
        result = self._values.get("main_page_suffix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def not_found_page(self) -> typing.Optional[builtins.str]:
        '''The custom object to return when a requested resource is not found.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_storage_bucket#not_found_page GoogleStorageBucket#not_found_page}
        '''
        result = self._values.get("not_found_page")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleStorageBucketWebsite(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleStorageBucketWebsiteOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleStorageBucket.GoogleStorageBucketWebsiteOutputReference",
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
            type_hints = typing.get_type_hints(GoogleStorageBucketWebsiteOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMainPageSuffix")
    def reset_main_page_suffix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMainPageSuffix", []))

    @jsii.member(jsii_name="resetNotFoundPage")
    def reset_not_found_page(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNotFoundPage", []))

    @builtins.property
    @jsii.member(jsii_name="mainPageSuffixInput")
    def main_page_suffix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mainPageSuffixInput"))

    @builtins.property
    @jsii.member(jsii_name="notFoundPageInput")
    def not_found_page_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notFoundPageInput"))

    @builtins.property
    @jsii.member(jsii_name="mainPageSuffix")
    def main_page_suffix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mainPageSuffix"))

    @main_page_suffix.setter
    def main_page_suffix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketWebsiteOutputReference, "main_page_suffix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mainPageSuffix", value)

    @builtins.property
    @jsii.member(jsii_name="notFoundPage")
    def not_found_page(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "notFoundPage"))

    @not_found_page.setter
    def not_found_page(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketWebsiteOutputReference, "not_found_page").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notFoundPage", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleStorageBucketWebsite]:
        return typing.cast(typing.Optional[GoogleStorageBucketWebsite], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleStorageBucketWebsite],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleStorageBucketWebsiteOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleStorageBucket",
    "GoogleStorageBucketConfig",
    "GoogleStorageBucketCors",
    "GoogleStorageBucketCorsList",
    "GoogleStorageBucketCorsOutputReference",
    "GoogleStorageBucketCustomPlacementConfig",
    "GoogleStorageBucketCustomPlacementConfigOutputReference",
    "GoogleStorageBucketEncryption",
    "GoogleStorageBucketEncryptionOutputReference",
    "GoogleStorageBucketLifecycleRule",
    "GoogleStorageBucketLifecycleRuleAction",
    "GoogleStorageBucketLifecycleRuleActionOutputReference",
    "GoogleStorageBucketLifecycleRuleCondition",
    "GoogleStorageBucketLifecycleRuleConditionOutputReference",
    "GoogleStorageBucketLifecycleRuleList",
    "GoogleStorageBucketLifecycleRuleOutputReference",
    "GoogleStorageBucketLogging",
    "GoogleStorageBucketLoggingOutputReference",
    "GoogleStorageBucketRetentionPolicy",
    "GoogleStorageBucketRetentionPolicyOutputReference",
    "GoogleStorageBucketTimeouts",
    "GoogleStorageBucketTimeoutsOutputReference",
    "GoogleStorageBucketVersioning",
    "GoogleStorageBucketVersioningOutputReference",
    "GoogleStorageBucketWebsite",
    "GoogleStorageBucketWebsiteOutputReference",
]

publication.publish()
