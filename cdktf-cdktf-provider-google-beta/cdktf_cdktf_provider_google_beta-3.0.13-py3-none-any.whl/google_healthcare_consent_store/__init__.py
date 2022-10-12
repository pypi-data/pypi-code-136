'''
# `google_healthcare_consent_store`

Refer to the Terraform Registory for docs: [`google_healthcare_consent_store`](https://www.terraform.io/docs/providers/google-beta/r/google_healthcare_consent_store).
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


class GoogleHealthcareConsentStore(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleHealthcareConsentStore.GoogleHealthcareConsentStore",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_healthcare_consent_store google_healthcare_consent_store}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        dataset: builtins.str,
        name: builtins.str,
        default_consent_ttl: typing.Optional[builtins.str] = None,
        enable_consent_create_on_update: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["GoogleHealthcareConsentStoreTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_healthcare_consent_store google_healthcare_consent_store} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param dataset: Identifies the dataset addressed by this request. Must be in the format 'projects/{project}/locations/{location}/datasets/{dataset}'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_healthcare_consent_store#dataset GoogleHealthcareConsentStore#dataset}
        :param name: The name of this ConsentStore, for example: "consent1". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_healthcare_consent_store#name GoogleHealthcareConsentStore#name}
        :param default_consent_ttl: Default time to live for consents in this store. Must be at least 24 hours. Updating this field will not affect the expiration time of existing consents. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_healthcare_consent_store#default_consent_ttl GoogleHealthcareConsentStore#default_consent_ttl}
        :param enable_consent_create_on_update: If true, [consents.patch] [google.cloud.healthcare.v1.consent.UpdateConsent] creates the consent if it does not already exist. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_healthcare_consent_store#enable_consent_create_on_update GoogleHealthcareConsentStore#enable_consent_create_on_update}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_healthcare_consent_store#id GoogleHealthcareConsentStore#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: User-supplied key-value pairs used to organize Consent stores. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: '[\\p{Ll}\\p{Lo}][\\p{Ll}\\p{Lo}\\p{N}_-]{0,62}' Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: '[\\p{Ll}\\p{Lo}\\p{N}_-]{0,63}' No more than 64 labels can be associated with a given store. An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_healthcare_consent_store#labels GoogleHealthcareConsentStore#labels}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_healthcare_consent_store#timeouts GoogleHealthcareConsentStore#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleHealthcareConsentStore.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleHealthcareConsentStoreConfig(
            dataset=dataset,
            name=name,
            default_consent_ttl=default_consent_ttl,
            enable_consent_create_on_update=enable_consent_create_on_update,
            id=id,
            labels=labels,
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
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_healthcare_consent_store#create GoogleHealthcareConsentStore#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_healthcare_consent_store#delete GoogleHealthcareConsentStore#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_healthcare_consent_store#update GoogleHealthcareConsentStore#update}.
        '''
        value = GoogleHealthcareConsentStoreTimeouts(
            create=create, delete=delete, update=update
        )

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetDefaultConsentTtl")
    def reset_default_consent_ttl(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultConsentTtl", []))

    @jsii.member(jsii_name="resetEnableConsentCreateOnUpdate")
    def reset_enable_consent_create_on_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableConsentCreateOnUpdate", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

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
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleHealthcareConsentStoreTimeoutsOutputReference":
        return typing.cast("GoogleHealthcareConsentStoreTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="datasetInput")
    def dataset_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultConsentTtlInput")
    def default_consent_ttl_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "defaultConsentTtlInput"))

    @builtins.property
    @jsii.member(jsii_name="enableConsentCreateOnUpdateInput")
    def enable_consent_create_on_update_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableConsentCreateOnUpdateInput"))

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
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleHealthcareConsentStoreTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleHealthcareConsentStoreTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="dataset")
    def dataset(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "dataset"))

    @dataset.setter
    def dataset(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleHealthcareConsentStore, "dataset").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataset", value)

    @builtins.property
    @jsii.member(jsii_name="defaultConsentTtl")
    def default_consent_ttl(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultConsentTtl"))

    @default_consent_ttl.setter
    def default_consent_ttl(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleHealthcareConsentStore, "default_consent_ttl").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultConsentTtl", value)

    @builtins.property
    @jsii.member(jsii_name="enableConsentCreateOnUpdate")
    def enable_consent_create_on_update(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableConsentCreateOnUpdate"))

    @enable_consent_create_on_update.setter
    def enable_consent_create_on_update(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleHealthcareConsentStore, "enable_consent_create_on_update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableConsentCreateOnUpdate", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleHealthcareConsentStore, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleHealthcareConsentStore, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleHealthcareConsentStore, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleHealthcareConsentStore.GoogleHealthcareConsentStoreConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "dataset": "dataset",
        "name": "name",
        "default_consent_ttl": "defaultConsentTtl",
        "enable_consent_create_on_update": "enableConsentCreateOnUpdate",
        "id": "id",
        "labels": "labels",
        "timeouts": "timeouts",
    },
)
class GoogleHealthcareConsentStoreConfig(cdktf.TerraformMetaArguments):
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
        dataset: builtins.str,
        name: builtins.str,
        default_consent_ttl: typing.Optional[builtins.str] = None,
        enable_consent_create_on_update: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeouts: typing.Optional[typing.Union["GoogleHealthcareConsentStoreTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param dataset: Identifies the dataset addressed by this request. Must be in the format 'projects/{project}/locations/{location}/datasets/{dataset}'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_healthcare_consent_store#dataset GoogleHealthcareConsentStore#dataset}
        :param name: The name of this ConsentStore, for example: "consent1". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_healthcare_consent_store#name GoogleHealthcareConsentStore#name}
        :param default_consent_ttl: Default time to live for consents in this store. Must be at least 24 hours. Updating this field will not affect the expiration time of existing consents. A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_healthcare_consent_store#default_consent_ttl GoogleHealthcareConsentStore#default_consent_ttl}
        :param enable_consent_create_on_update: If true, [consents.patch] [google.cloud.healthcare.v1.consent.UpdateConsent] creates the consent if it does not already exist. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_healthcare_consent_store#enable_consent_create_on_update GoogleHealthcareConsentStore#enable_consent_create_on_update}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_healthcare_consent_store#id GoogleHealthcareConsentStore#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: User-supplied key-value pairs used to organize Consent stores. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: '[\\p{Ll}\\p{Lo}][\\p{Ll}\\p{Lo}\\p{N}_-]{0,62}' Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: '[\\p{Ll}\\p{Lo}\\p{N}_-]{0,63}' No more than 64 labels can be associated with a given store. An object containing a list of "key": value pairs. Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_healthcare_consent_store#labels GoogleHealthcareConsentStore#labels}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_healthcare_consent_store#timeouts GoogleHealthcareConsentStore#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(timeouts, dict):
            timeouts = GoogleHealthcareConsentStoreTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleHealthcareConsentStoreConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument dataset", value=dataset, expected_type=type_hints["dataset"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument default_consent_ttl", value=default_consent_ttl, expected_type=type_hints["default_consent_ttl"])
            check_type(argname="argument enable_consent_create_on_update", value=enable_consent_create_on_update, expected_type=type_hints["enable_consent_create_on_update"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "dataset": dataset,
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
        if default_consent_ttl is not None:
            self._values["default_consent_ttl"] = default_consent_ttl
        if enable_consent_create_on_update is not None:
            self._values["enable_consent_create_on_update"] = enable_consent_create_on_update
        if id is not None:
            self._values["id"] = id
        if labels is not None:
            self._values["labels"] = labels
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
    def dataset(self) -> builtins.str:
        '''Identifies the dataset addressed by this request. Must be in the format 'projects/{project}/locations/{location}/datasets/{dataset}'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_healthcare_consent_store#dataset GoogleHealthcareConsentStore#dataset}
        '''
        result = self._values.get("dataset")
        assert result is not None, "Required property 'dataset' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of this ConsentStore, for example: "consent1".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_healthcare_consent_store#name GoogleHealthcareConsentStore#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_consent_ttl(self) -> typing.Optional[builtins.str]:
        '''Default time to live for consents in this store.

        Must be at least 24 hours. Updating this field will not affect the expiration time of existing consents.

        A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_healthcare_consent_store#default_consent_ttl GoogleHealthcareConsentStore#default_consent_ttl}
        '''
        result = self._values.get("default_consent_ttl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_consent_create_on_update(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true, [consents.patch] [google.cloud.healthcare.v1.consent.UpdateConsent] creates the consent if it does not already exist.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_healthcare_consent_store#enable_consent_create_on_update GoogleHealthcareConsentStore#enable_consent_create_on_update}
        '''
        result = self._values.get("enable_consent_create_on_update")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_healthcare_consent_store#id GoogleHealthcareConsentStore#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''User-supplied key-value pairs used to organize Consent stores.

        Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must
        conform to the following PCRE regular expression: '[\\p{Ll}\\p{Lo}][\\p{Ll}\\p{Lo}\\p{N}_-]{0,62}'

        Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128
        bytes, and must conform to the following PCRE regular expression: '[\\p{Ll}\\p{Lo}\\p{N}_-]{0,63}'

        No more than 64 labels can be associated with a given store.

        An object containing a list of "key": value pairs.
        Example: { "name": "wrench", "mass": "1.3kg", "count": "3" }.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_healthcare_consent_store#labels GoogleHealthcareConsentStore#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleHealthcareConsentStoreTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_healthcare_consent_store#timeouts GoogleHealthcareConsentStore#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleHealthcareConsentStoreTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleHealthcareConsentStoreConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleHealthcareConsentStore.GoogleHealthcareConsentStoreTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete", "update": "update"},
)
class GoogleHealthcareConsentStoreTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_healthcare_consent_store#create GoogleHealthcareConsentStore#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_healthcare_consent_store#delete GoogleHealthcareConsentStore#delete}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_healthcare_consent_store#update GoogleHealthcareConsentStore#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleHealthcareConsentStoreTimeouts.__init__)
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
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_healthcare_consent_store#create GoogleHealthcareConsentStore#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_healthcare_consent_store#delete GoogleHealthcareConsentStore#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_healthcare_consent_store#update GoogleHealthcareConsentStore#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleHealthcareConsentStoreTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleHealthcareConsentStoreTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleHealthcareConsentStore.GoogleHealthcareConsentStoreTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleHealthcareConsentStoreTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleHealthcareConsentStoreTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleHealthcareConsentStoreTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleHealthcareConsentStoreTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleHealthcareConsentStoreTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleHealthcareConsentStoreTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleHealthcareConsentStoreTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleHealthcareConsentStoreTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleHealthcareConsentStore",
    "GoogleHealthcareConsentStoreConfig",
    "GoogleHealthcareConsentStoreTimeouts",
    "GoogleHealthcareConsentStoreTimeoutsOutputReference",
]

publication.publish()
