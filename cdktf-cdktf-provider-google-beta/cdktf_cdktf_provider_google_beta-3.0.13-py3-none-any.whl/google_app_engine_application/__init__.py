'''
# `google_app_engine_application`

Refer to the Terraform Registory for docs: [`google_app_engine_application`](https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application).
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


class GoogleAppEngineApplication(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineApplication.GoogleAppEngineApplication",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application google_app_engine_application}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        location_id: builtins.str,
        auth_domain: typing.Optional[builtins.str] = None,
        database_type: typing.Optional[builtins.str] = None,
        feature_settings: typing.Optional[typing.Union["GoogleAppEngineApplicationFeatureSettings", typing.Dict[str, typing.Any]]] = None,
        iap: typing.Optional[typing.Union["GoogleAppEngineApplicationIap", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        serving_status: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleAppEngineApplicationTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application google_app_engine_application} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param location_id: The location to serve the app from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#location_id GoogleAppEngineApplication#location_id}
        :param auth_domain: The domain to authenticate users with when using App Engine's User API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#auth_domain GoogleAppEngineApplication#auth_domain}
        :param database_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#database_type GoogleAppEngineApplication#database_type}.
        :param feature_settings: feature_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#feature_settings GoogleAppEngineApplication#feature_settings}
        :param iap: iap block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#iap GoogleAppEngineApplication#iap}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#id GoogleAppEngineApplication#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: The project ID to create the application under. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#project GoogleAppEngineApplication#project}
        :param serving_status: The serving status of the app. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#serving_status GoogleAppEngineApplication#serving_status}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#timeouts GoogleAppEngineApplication#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineApplication.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleAppEngineApplicationConfig(
            location_id=location_id,
            auth_domain=auth_domain,
            database_type=database_type,
            feature_settings=feature_settings,
            iap=iap,
            id=id,
            project=project,
            serving_status=serving_status,
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

    @jsii.member(jsii_name="putFeatureSettings")
    def put_feature_settings(
        self,
        *,
        split_health_checks: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param split_health_checks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#split_health_checks GoogleAppEngineApplication#split_health_checks}.
        '''
        value = GoogleAppEngineApplicationFeatureSettings(
            split_health_checks=split_health_checks
        )

        return typing.cast(None, jsii.invoke(self, "putFeatureSettings", [value]))

    @jsii.member(jsii_name="putIap")
    def put_iap(
        self,
        *,
        oauth2_client_id: builtins.str,
        oauth2_client_secret: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param oauth2_client_id: OAuth2 client ID to use for the authentication flow. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#oauth2_client_id GoogleAppEngineApplication#oauth2_client_id}
        :param oauth2_client_secret: OAuth2 client secret to use for the authentication flow. The SHA-256 hash of the value is returned in the oauth2ClientSecretSha256 field. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#oauth2_client_secret GoogleAppEngineApplication#oauth2_client_secret}
        :param enabled: Adapted for use with the app. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#enabled GoogleAppEngineApplication#enabled}
        '''
        value = GoogleAppEngineApplicationIap(
            oauth2_client_id=oauth2_client_id,
            oauth2_client_secret=oauth2_client_secret,
            enabled=enabled,
        )

        return typing.cast(None, jsii.invoke(self, "putIap", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#create GoogleAppEngineApplication#create}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#update GoogleAppEngineApplication#update}.
        '''
        value = GoogleAppEngineApplicationTimeouts(create=create, update=update)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetAuthDomain")
    def reset_auth_domain(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthDomain", []))

    @jsii.member(jsii_name="resetDatabaseType")
    def reset_database_type(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatabaseType", []))

    @jsii.member(jsii_name="resetFeatureSettings")
    def reset_feature_settings(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFeatureSettings", []))

    @jsii.member(jsii_name="resetIap")
    def reset_iap(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIap", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetServingStatus")
    def reset_serving_status(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetServingStatus", []))

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
    @jsii.member(jsii_name="appId")
    def app_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "appId"))

    @builtins.property
    @jsii.member(jsii_name="codeBucket")
    def code_bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "codeBucket"))

    @builtins.property
    @jsii.member(jsii_name="defaultBucket")
    def default_bucket(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultBucket"))

    @builtins.property
    @jsii.member(jsii_name="defaultHostname")
    def default_hostname(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "defaultHostname"))

    @builtins.property
    @jsii.member(jsii_name="featureSettings")
    def feature_settings(
        self,
    ) -> "GoogleAppEngineApplicationFeatureSettingsOutputReference":
        return typing.cast("GoogleAppEngineApplicationFeatureSettingsOutputReference", jsii.get(self, "featureSettings"))

    @builtins.property
    @jsii.member(jsii_name="gcrDomain")
    def gcr_domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "gcrDomain"))

    @builtins.property
    @jsii.member(jsii_name="iap")
    def iap(self) -> "GoogleAppEngineApplicationIapOutputReference":
        return typing.cast("GoogleAppEngineApplicationIapOutputReference", jsii.get(self, "iap"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleAppEngineApplicationTimeoutsOutputReference":
        return typing.cast("GoogleAppEngineApplicationTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="urlDispatchRule")
    def url_dispatch_rule(self) -> "GoogleAppEngineApplicationUrlDispatchRuleList":
        return typing.cast("GoogleAppEngineApplicationUrlDispatchRuleList", jsii.get(self, "urlDispatchRule"))

    @builtins.property
    @jsii.member(jsii_name="authDomainInput")
    def auth_domain_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authDomainInput"))

    @builtins.property
    @jsii.member(jsii_name="databaseTypeInput")
    def database_type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseTypeInput"))

    @builtins.property
    @jsii.member(jsii_name="featureSettingsInput")
    def feature_settings_input(
        self,
    ) -> typing.Optional["GoogleAppEngineApplicationFeatureSettings"]:
        return typing.cast(typing.Optional["GoogleAppEngineApplicationFeatureSettings"], jsii.get(self, "featureSettingsInput"))

    @builtins.property
    @jsii.member(jsii_name="iapInput")
    def iap_input(self) -> typing.Optional["GoogleAppEngineApplicationIap"]:
        return typing.cast(typing.Optional["GoogleAppEngineApplicationIap"], jsii.get(self, "iapInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="locationIdInput")
    def location_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationIdInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="servingStatusInput")
    def serving_status_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "servingStatusInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleAppEngineApplicationTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleAppEngineApplicationTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="authDomain")
    def auth_domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authDomain"))

    @auth_domain.setter
    def auth_domain(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineApplication, "auth_domain").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authDomain", value)

    @builtins.property
    @jsii.member(jsii_name="databaseType")
    def database_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "databaseType"))

    @database_type.setter
    def database_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineApplication, "database_type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseType", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineApplication, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="locationId")
    def location_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "locationId"))

    @location_id.setter
    def location_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineApplication, "location_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locationId", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineApplication, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="servingStatus")
    def serving_status(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "servingStatus"))

    @serving_status.setter
    def serving_status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineApplication, "serving_status").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "servingStatus", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineApplication.GoogleAppEngineApplicationConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "location_id": "locationId",
        "auth_domain": "authDomain",
        "database_type": "databaseType",
        "feature_settings": "featureSettings",
        "iap": "iap",
        "id": "id",
        "project": "project",
        "serving_status": "servingStatus",
        "timeouts": "timeouts",
    },
)
class GoogleAppEngineApplicationConfig(cdktf.TerraformMetaArguments):
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
        location_id: builtins.str,
        auth_domain: typing.Optional[builtins.str] = None,
        database_type: typing.Optional[builtins.str] = None,
        feature_settings: typing.Optional[typing.Union["GoogleAppEngineApplicationFeatureSettings", typing.Dict[str, typing.Any]]] = None,
        iap: typing.Optional[typing.Union["GoogleAppEngineApplicationIap", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        serving_status: typing.Optional[builtins.str] = None,
        timeouts: typing.Optional[typing.Union["GoogleAppEngineApplicationTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param location_id: The location to serve the app from. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#location_id GoogleAppEngineApplication#location_id}
        :param auth_domain: The domain to authenticate users with when using App Engine's User API. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#auth_domain GoogleAppEngineApplication#auth_domain}
        :param database_type: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#database_type GoogleAppEngineApplication#database_type}.
        :param feature_settings: feature_settings block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#feature_settings GoogleAppEngineApplication#feature_settings}
        :param iap: iap block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#iap GoogleAppEngineApplication#iap}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#id GoogleAppEngineApplication#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param project: The project ID to create the application under. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#project GoogleAppEngineApplication#project}
        :param serving_status: The serving status of the app. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#serving_status GoogleAppEngineApplication#serving_status}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#timeouts GoogleAppEngineApplication#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(feature_settings, dict):
            feature_settings = GoogleAppEngineApplicationFeatureSettings(**feature_settings)
        if isinstance(iap, dict):
            iap = GoogleAppEngineApplicationIap(**iap)
        if isinstance(timeouts, dict):
            timeouts = GoogleAppEngineApplicationTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineApplicationConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument location_id", value=location_id, expected_type=type_hints["location_id"])
            check_type(argname="argument auth_domain", value=auth_domain, expected_type=type_hints["auth_domain"])
            check_type(argname="argument database_type", value=database_type, expected_type=type_hints["database_type"])
            check_type(argname="argument feature_settings", value=feature_settings, expected_type=type_hints["feature_settings"])
            check_type(argname="argument iap", value=iap, expected_type=type_hints["iap"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument serving_status", value=serving_status, expected_type=type_hints["serving_status"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "location_id": location_id,
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
        if auth_domain is not None:
            self._values["auth_domain"] = auth_domain
        if database_type is not None:
            self._values["database_type"] = database_type
        if feature_settings is not None:
            self._values["feature_settings"] = feature_settings
        if iap is not None:
            self._values["iap"] = iap
        if id is not None:
            self._values["id"] = id
        if project is not None:
            self._values["project"] = project
        if serving_status is not None:
            self._values["serving_status"] = serving_status
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
    def location_id(self) -> builtins.str:
        '''The location to serve the app from.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#location_id GoogleAppEngineApplication#location_id}
        '''
        result = self._values.get("location_id")
        assert result is not None, "Required property 'location_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auth_domain(self) -> typing.Optional[builtins.str]:
        '''The domain to authenticate users with when using App Engine's User API.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#auth_domain GoogleAppEngineApplication#auth_domain}
        '''
        result = self._values.get("auth_domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def database_type(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#database_type GoogleAppEngineApplication#database_type}.'''
        result = self._values.get("database_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def feature_settings(
        self,
    ) -> typing.Optional["GoogleAppEngineApplicationFeatureSettings"]:
        '''feature_settings block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#feature_settings GoogleAppEngineApplication#feature_settings}
        '''
        result = self._values.get("feature_settings")
        return typing.cast(typing.Optional["GoogleAppEngineApplicationFeatureSettings"], result)

    @builtins.property
    def iap(self) -> typing.Optional["GoogleAppEngineApplicationIap"]:
        '''iap block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#iap GoogleAppEngineApplication#iap}
        '''
        result = self._values.get("iap")
        return typing.cast(typing.Optional["GoogleAppEngineApplicationIap"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#id GoogleAppEngineApplication#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''The project ID to create the application under.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#project GoogleAppEngineApplication#project}
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def serving_status(self) -> typing.Optional[builtins.str]:
        '''The serving status of the app.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#serving_status GoogleAppEngineApplication#serving_status}
        '''
        result = self._values.get("serving_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleAppEngineApplicationTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#timeouts GoogleAppEngineApplication#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleAppEngineApplicationTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineApplicationConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineApplication.GoogleAppEngineApplicationFeatureSettings",
    jsii_struct_bases=[],
    name_mapping={"split_health_checks": "splitHealthChecks"},
)
class GoogleAppEngineApplicationFeatureSettings:
    def __init__(
        self,
        *,
        split_health_checks: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        '''
        :param split_health_checks: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#split_health_checks GoogleAppEngineApplication#split_health_checks}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineApplicationFeatureSettings.__init__)
            check_type(argname="argument split_health_checks", value=split_health_checks, expected_type=type_hints["split_health_checks"])
        self._values: typing.Dict[str, typing.Any] = {
            "split_health_checks": split_health_checks,
        }

    @builtins.property
    def split_health_checks(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#split_health_checks GoogleAppEngineApplication#split_health_checks}.'''
        result = self._values.get("split_health_checks")
        assert result is not None, "Required property 'split_health_checks' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineApplicationFeatureSettings(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAppEngineApplicationFeatureSettingsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineApplication.GoogleAppEngineApplicationFeatureSettingsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAppEngineApplicationFeatureSettingsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="splitHealthChecksInput")
    def split_health_checks_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "splitHealthChecksInput"))

    @builtins.property
    @jsii.member(jsii_name="splitHealthChecks")
    def split_health_checks(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "splitHealthChecks"))

    @split_health_checks.setter
    def split_health_checks(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineApplicationFeatureSettingsOutputReference, "split_health_checks").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "splitHealthChecks", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAppEngineApplicationFeatureSettings]:
        return typing.cast(typing.Optional[GoogleAppEngineApplicationFeatureSettings], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAppEngineApplicationFeatureSettings],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineApplicationFeatureSettingsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineApplication.GoogleAppEngineApplicationIap",
    jsii_struct_bases=[],
    name_mapping={
        "oauth2_client_id": "oauth2ClientId",
        "oauth2_client_secret": "oauth2ClientSecret",
        "enabled": "enabled",
    },
)
class GoogleAppEngineApplicationIap:
    def __init__(
        self,
        *,
        oauth2_client_id: builtins.str,
        oauth2_client_secret: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param oauth2_client_id: OAuth2 client ID to use for the authentication flow. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#oauth2_client_id GoogleAppEngineApplication#oauth2_client_id}
        :param oauth2_client_secret: OAuth2 client secret to use for the authentication flow. The SHA-256 hash of the value is returned in the oauth2ClientSecretSha256 field. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#oauth2_client_secret GoogleAppEngineApplication#oauth2_client_secret}
        :param enabled: Adapted for use with the app. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#enabled GoogleAppEngineApplication#enabled}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineApplicationIap.__init__)
            check_type(argname="argument oauth2_client_id", value=oauth2_client_id, expected_type=type_hints["oauth2_client_id"])
            check_type(argname="argument oauth2_client_secret", value=oauth2_client_secret, expected_type=type_hints["oauth2_client_secret"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
        self._values: typing.Dict[str, typing.Any] = {
            "oauth2_client_id": oauth2_client_id,
            "oauth2_client_secret": oauth2_client_secret,
        }
        if enabled is not None:
            self._values["enabled"] = enabled

    @builtins.property
    def oauth2_client_id(self) -> builtins.str:
        '''OAuth2 client ID to use for the authentication flow.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#oauth2_client_id GoogleAppEngineApplication#oauth2_client_id}
        '''
        result = self._values.get("oauth2_client_id")
        assert result is not None, "Required property 'oauth2_client_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def oauth2_client_secret(self) -> builtins.str:
        '''OAuth2 client secret to use for the authentication flow.

        The SHA-256 hash of the value is returned in the oauth2ClientSecretSha256 field.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#oauth2_client_secret GoogleAppEngineApplication#oauth2_client_secret}
        '''
        result = self._values.get("oauth2_client_secret")
        assert result is not None, "Required property 'oauth2_client_secret' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Adapted for use with the app.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#enabled GoogleAppEngineApplication#enabled}
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineApplicationIap(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAppEngineApplicationIapOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineApplication.GoogleAppEngineApplicationIapOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAppEngineApplicationIapOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnabled")
    def reset_enabled(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnabled", []))

    @builtins.property
    @jsii.member(jsii_name="oauth2ClientSecretSha256")
    def oauth2_client_secret_sha256(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oauth2ClientSecretSha256"))

    @builtins.property
    @jsii.member(jsii_name="enabledInput")
    def enabled_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enabledInput"))

    @builtins.property
    @jsii.member(jsii_name="oauth2ClientIdInput")
    def oauth2_client_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauth2ClientIdInput"))

    @builtins.property
    @jsii.member(jsii_name="oauth2ClientSecretInput")
    def oauth2_client_secret_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "oauth2ClientSecretInput"))

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineApplicationIapOutputReference, "enabled").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="oauth2ClientId")
    def oauth2_client_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oauth2ClientId"))

    @oauth2_client_id.setter
    def oauth2_client_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineApplicationIapOutputReference, "oauth2_client_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauth2ClientId", value)

    @builtins.property
    @jsii.member(jsii_name="oauth2ClientSecret")
    def oauth2_client_secret(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "oauth2ClientSecret"))

    @oauth2_client_secret.setter
    def oauth2_client_secret(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineApplicationIapOutputReference, "oauth2_client_secret").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oauth2ClientSecret", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleAppEngineApplicationIap]:
        return typing.cast(typing.Optional[GoogleAppEngineApplicationIap], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAppEngineApplicationIap],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineApplicationIapOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineApplication.GoogleAppEngineApplicationTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "update": "update"},
)
class GoogleAppEngineApplicationTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        update: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#create GoogleAppEngineApplication#create}.
        :param update: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#update GoogleAppEngineApplication#update}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineApplicationTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument update", value=update, expected_type=type_hints["update"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if update is not None:
            self._values["update"] = update

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#create GoogleAppEngineApplication#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def update(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_app_engine_application#update GoogleAppEngineApplication#update}.'''
        result = self._values.get("update")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineApplicationTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAppEngineApplicationTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineApplication.GoogleAppEngineApplicationTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAppEngineApplicationTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetUpdate")
    def reset_update(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUpdate", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

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
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineApplicationTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="update")
    def update(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "update"))

    @update.setter
    def update(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineApplicationTimeoutsOutputReference, "update").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "update", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleAppEngineApplicationTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleAppEngineApplicationTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleAppEngineApplicationTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineApplicationTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleAppEngineApplication.GoogleAppEngineApplicationUrlDispatchRule",
    jsii_struct_bases=[],
    name_mapping={},
)
class GoogleAppEngineApplicationUrlDispatchRule:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleAppEngineApplicationUrlDispatchRule(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleAppEngineApplicationUrlDispatchRuleList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineApplication.GoogleAppEngineApplicationUrlDispatchRuleList",
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
            type_hints = typing.get_type_hints(GoogleAppEngineApplicationUrlDispatchRuleList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleAppEngineApplicationUrlDispatchRuleOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleAppEngineApplicationUrlDispatchRuleList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleAppEngineApplicationUrlDispatchRuleOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineApplicationUrlDispatchRuleList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineApplicationUrlDispatchRuleList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineApplicationUrlDispatchRuleList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GoogleAppEngineApplicationUrlDispatchRuleOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleAppEngineApplication.GoogleAppEngineApplicationUrlDispatchRuleOutputReference",
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
            type_hints = typing.get_type_hints(GoogleAppEngineApplicationUrlDispatchRuleOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "domain"))

    @builtins.property
    @jsii.member(jsii_name="path")
    def path(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "path"))

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "service"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleAppEngineApplicationUrlDispatchRule]:
        return typing.cast(typing.Optional[GoogleAppEngineApplicationUrlDispatchRule], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleAppEngineApplicationUrlDispatchRule],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleAppEngineApplicationUrlDispatchRuleOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleAppEngineApplication",
    "GoogleAppEngineApplicationConfig",
    "GoogleAppEngineApplicationFeatureSettings",
    "GoogleAppEngineApplicationFeatureSettingsOutputReference",
    "GoogleAppEngineApplicationIap",
    "GoogleAppEngineApplicationIapOutputReference",
    "GoogleAppEngineApplicationTimeouts",
    "GoogleAppEngineApplicationTimeoutsOutputReference",
    "GoogleAppEngineApplicationUrlDispatchRule",
    "GoogleAppEngineApplicationUrlDispatchRuleList",
    "GoogleAppEngineApplicationUrlDispatchRuleOutputReference",
]

publication.publish()
