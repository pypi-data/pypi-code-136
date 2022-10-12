'''
# `vsphere_content_library`

Refer to the Terraform Registory for docs: [`vsphere_content_library`](https://www.terraform.io/docs/providers/vsphere/r/content_library).
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


class ContentLibrary(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vsphere.contentLibrary.ContentLibrary",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/vsphere/r/content_library vsphere_content_library}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        name: builtins.str,
        storage_backing: typing.Sequence[builtins.str],
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        publication: typing.Optional[typing.Union["ContentLibraryPublication", typing.Dict[str, typing.Any]]] = None,
        subscription: typing.Optional[typing.Union["ContentLibrarySubscription", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/vsphere/r/content_library vsphere_content_library} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param name: The name of the content library. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#name ContentLibrary#name}
        :param storage_backing: The name of the content library. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#storage_backing ContentLibrary#storage_backing}
        :param description: Optional description of the content library. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#description ContentLibrary#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#id ContentLibrary#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param publication: publication block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#publication ContentLibrary#publication}
        :param subscription: subscription block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#subscription ContentLibrary#subscription}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContentLibrary.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = ContentLibraryConfig(
            name=name,
            storage_backing=storage_backing,
            description=description,
            id=id,
            publication=publication,
            subscription=subscription,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putPublication")
    def put_publication(
        self,
        *,
        authentication_method: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        published: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param authentication_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#authentication_method ContentLibrary#authentication_method}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#password ContentLibrary#password}.
        :param published: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#published ContentLibrary#published}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#username ContentLibrary#username}.
        '''
        value = ContentLibraryPublication(
            authentication_method=authentication_method,
            password=password,
            published=published,
            username=username,
        )

        return typing.cast(None, jsii.invoke(self, "putPublication", [value]))

    @jsii.member(jsii_name="putSubscription")
    def put_subscription(
        self,
        *,
        authentication_method: typing.Optional[builtins.str] = None,
        automatic_sync: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        on_demand: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        password: typing.Optional[builtins.str] = None,
        subscription_url: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param authentication_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#authentication_method ContentLibrary#authentication_method}.
        :param automatic_sync: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#automatic_sync ContentLibrary#automatic_sync}.
        :param on_demand: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#on_demand ContentLibrary#on_demand}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#password ContentLibrary#password}.
        :param subscription_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#subscription_url ContentLibrary#subscription_url}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#username ContentLibrary#username}.
        '''
        value = ContentLibrarySubscription(
            authentication_method=authentication_method,
            automatic_sync=automatic_sync,
            on_demand=on_demand,
            password=password,
            subscription_url=subscription_url,
            username=username,
        )

        return typing.cast(None, jsii.invoke(self, "putSubscription", [value]))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetPublication")
    def reset_publication(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublication", []))

    @jsii.member(jsii_name="resetSubscription")
    def reset_subscription(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubscription", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="publication")
    def publication(self) -> "ContentLibraryPublicationOutputReference":
        return typing.cast("ContentLibraryPublicationOutputReference", jsii.get(self, "publication"))

    @builtins.property
    @jsii.member(jsii_name="subscription")
    def subscription(self) -> "ContentLibrarySubscriptionOutputReference":
        return typing.cast("ContentLibrarySubscriptionOutputReference", jsii.get(self, "subscription"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="nameInput")
    def name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nameInput"))

    @builtins.property
    @jsii.member(jsii_name="publicationInput")
    def publication_input(self) -> typing.Optional["ContentLibraryPublication"]:
        return typing.cast(typing.Optional["ContentLibraryPublication"], jsii.get(self, "publicationInput"))

    @builtins.property
    @jsii.member(jsii_name="storageBackingInput")
    def storage_backing_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "storageBackingInput"))

    @builtins.property
    @jsii.member(jsii_name="subscriptionInput")
    def subscription_input(self) -> typing.Optional["ContentLibrarySubscription"]:
        return typing.cast(typing.Optional["ContentLibrarySubscription"], jsii.get(self, "subscriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContentLibrary, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContentLibrary, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContentLibrary, "name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="storageBacking")
    def storage_backing(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "storageBacking"))

    @storage_backing.setter
    def storage_backing(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContentLibrary, "storage_backing").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageBacking", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vsphere.contentLibrary.ContentLibraryConfig",
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
        "storage_backing": "storageBacking",
        "description": "description",
        "id": "id",
        "publication": "publication",
        "subscription": "subscription",
    },
)
class ContentLibraryConfig(cdktf.TerraformMetaArguments):
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
        storage_backing: typing.Sequence[builtins.str],
        description: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        publication: typing.Optional[typing.Union["ContentLibraryPublication", typing.Dict[str, typing.Any]]] = None,
        subscription: typing.Optional[typing.Union["ContentLibrarySubscription", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param name: The name of the content library. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#name ContentLibrary#name}
        :param storage_backing: The name of the content library. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#storage_backing ContentLibrary#storage_backing}
        :param description: Optional description of the content library. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#description ContentLibrary#description}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#id ContentLibrary#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param publication: publication block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#publication ContentLibrary#publication}
        :param subscription: subscription block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#subscription ContentLibrary#subscription}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(publication, dict):
            publication = ContentLibraryPublication(**publication)
        if isinstance(subscription, dict):
            subscription = ContentLibrarySubscription(**subscription)
        if __debug__:
            type_hints = typing.get_type_hints(ContentLibraryConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument storage_backing", value=storage_backing, expected_type=type_hints["storage_backing"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument publication", value=publication, expected_type=type_hints["publication"])
            check_type(argname="argument subscription", value=subscription, expected_type=type_hints["subscription"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "storage_backing": storage_backing,
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
        if description is not None:
            self._values["description"] = description
        if id is not None:
            self._values["id"] = id
        if publication is not None:
            self._values["publication"] = publication
        if subscription is not None:
            self._values["subscription"] = subscription

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
        '''The name of the content library.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#name ContentLibrary#name}
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def storage_backing(self) -> typing.List[builtins.str]:
        '''The name of the content library.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#storage_backing ContentLibrary#storage_backing}
        '''
        result = self._values.get("storage_backing")
        assert result is not None, "Required property 'storage_backing' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Optional description of the content library.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#description ContentLibrary#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#id ContentLibrary#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def publication(self) -> typing.Optional["ContentLibraryPublication"]:
        '''publication block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#publication ContentLibrary#publication}
        '''
        result = self._values.get("publication")
        return typing.cast(typing.Optional["ContentLibraryPublication"], result)

    @builtins.property
    def subscription(self) -> typing.Optional["ContentLibrarySubscription"]:
        '''subscription block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#subscription ContentLibrary#subscription}
        '''
        result = self._values.get("subscription")
        return typing.cast(typing.Optional["ContentLibrarySubscription"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContentLibraryConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-vsphere.contentLibrary.ContentLibraryPublication",
    jsii_struct_bases=[],
    name_mapping={
        "authentication_method": "authenticationMethod",
        "password": "password",
        "published": "published",
        "username": "username",
    },
)
class ContentLibraryPublication:
    def __init__(
        self,
        *,
        authentication_method: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        published: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param authentication_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#authentication_method ContentLibrary#authentication_method}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#password ContentLibrary#password}.
        :param published: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#published ContentLibrary#published}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#username ContentLibrary#username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContentLibraryPublication.__init__)
            check_type(argname="argument authentication_method", value=authentication_method, expected_type=type_hints["authentication_method"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument published", value=published, expected_type=type_hints["published"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {}
        if authentication_method is not None:
            self._values["authentication_method"] = authentication_method
        if password is not None:
            self._values["password"] = password
        if published is not None:
            self._values["published"] = published
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def authentication_method(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#authentication_method ContentLibrary#authentication_method}.'''
        result = self._values.get("authentication_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#password ContentLibrary#password}.'''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def published(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#published ContentLibrary#published}.'''
        result = self._values.get("published")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#username ContentLibrary#username}.'''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContentLibraryPublication(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContentLibraryPublicationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vsphere.contentLibrary.ContentLibraryPublicationOutputReference",
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
            type_hints = typing.get_type_hints(ContentLibraryPublicationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAuthenticationMethod")
    def reset_authentication_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthenticationMethod", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetPublished")
    def reset_published(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPublished", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @builtins.property
    @jsii.member(jsii_name="publishUrl")
    def publish_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "publishUrl"))

    @builtins.property
    @jsii.member(jsii_name="authenticationMethodInput")
    def authentication_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authenticationMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="publishedInput")
    def published_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "publishedInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticationMethod")
    def authentication_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authenticationMethod"))

    @authentication_method.setter
    def authentication_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContentLibraryPublicationOutputReference, "authentication_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationMethod", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContentLibraryPublicationOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="published")
    def published(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "published"))

    @published.setter
    def published(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContentLibraryPublicationOutputReference, "published").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "published", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContentLibraryPublicationOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContentLibraryPublication]:
        return typing.cast(typing.Optional[ContentLibraryPublication], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[ContentLibraryPublication]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContentLibraryPublicationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-vsphere.contentLibrary.ContentLibrarySubscription",
    jsii_struct_bases=[],
    name_mapping={
        "authentication_method": "authenticationMethod",
        "automatic_sync": "automaticSync",
        "on_demand": "onDemand",
        "password": "password",
        "subscription_url": "subscriptionUrl",
        "username": "username",
    },
)
class ContentLibrarySubscription:
    def __init__(
        self,
        *,
        authentication_method: typing.Optional[builtins.str] = None,
        automatic_sync: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        on_demand: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        password: typing.Optional[builtins.str] = None,
        subscription_url: typing.Optional[builtins.str] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param authentication_method: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#authentication_method ContentLibrary#authentication_method}.
        :param automatic_sync: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#automatic_sync ContentLibrary#automatic_sync}.
        :param on_demand: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#on_demand ContentLibrary#on_demand}.
        :param password: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#password ContentLibrary#password}.
        :param subscription_url: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#subscription_url ContentLibrary#subscription_url}.
        :param username: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#username ContentLibrary#username}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(ContentLibrarySubscription.__init__)
            check_type(argname="argument authentication_method", value=authentication_method, expected_type=type_hints["authentication_method"])
            check_type(argname="argument automatic_sync", value=automatic_sync, expected_type=type_hints["automatic_sync"])
            check_type(argname="argument on_demand", value=on_demand, expected_type=type_hints["on_demand"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument subscription_url", value=subscription_url, expected_type=type_hints["subscription_url"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[str, typing.Any] = {}
        if authentication_method is not None:
            self._values["authentication_method"] = authentication_method
        if automatic_sync is not None:
            self._values["automatic_sync"] = automatic_sync
        if on_demand is not None:
            self._values["on_demand"] = on_demand
        if password is not None:
            self._values["password"] = password
        if subscription_url is not None:
            self._values["subscription_url"] = subscription_url
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def authentication_method(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#authentication_method ContentLibrary#authentication_method}.'''
        result = self._values.get("authentication_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def automatic_sync(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#automatic_sync ContentLibrary#automatic_sync}.'''
        result = self._values.get("automatic_sync")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def on_demand(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#on_demand ContentLibrary#on_demand}.'''
        result = self._values.get("on_demand")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#password ContentLibrary#password}.'''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subscription_url(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#subscription_url ContentLibrary#subscription_url}.'''
        result = self._values.get("subscription_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/vsphere/r/content_library#username ContentLibrary#username}.'''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ContentLibrarySubscription(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ContentLibrarySubscriptionOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-vsphere.contentLibrary.ContentLibrarySubscriptionOutputReference",
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
            type_hints = typing.get_type_hints(ContentLibrarySubscriptionOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAuthenticationMethod")
    def reset_authentication_method(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAuthenticationMethod", []))

    @jsii.member(jsii_name="resetAutomaticSync")
    def reset_automatic_sync(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutomaticSync", []))

    @jsii.member(jsii_name="resetOnDemand")
    def reset_on_demand(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOnDemand", []))

    @jsii.member(jsii_name="resetPassword")
    def reset_password(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPassword", []))

    @jsii.member(jsii_name="resetSubscriptionUrl")
    def reset_subscription_url(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSubscriptionUrl", []))

    @jsii.member(jsii_name="resetUsername")
    def reset_username(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUsername", []))

    @builtins.property
    @jsii.member(jsii_name="authenticationMethodInput")
    def authentication_method_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authenticationMethodInput"))

    @builtins.property
    @jsii.member(jsii_name="automaticSyncInput")
    def automatic_sync_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "automaticSyncInput"))

    @builtins.property
    @jsii.member(jsii_name="onDemandInput")
    def on_demand_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "onDemandInput"))

    @builtins.property
    @jsii.member(jsii_name="passwordInput")
    def password_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passwordInput"))

    @builtins.property
    @jsii.member(jsii_name="subscriptionUrlInput")
    def subscription_url_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subscriptionUrlInput"))

    @builtins.property
    @jsii.member(jsii_name="usernameInput")
    def username_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usernameInput"))

    @builtins.property
    @jsii.member(jsii_name="authenticationMethod")
    def authentication_method(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "authenticationMethod"))

    @authentication_method.setter
    def authentication_method(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContentLibrarySubscriptionOutputReference, "authentication_method").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationMethod", value)

    @builtins.property
    @jsii.member(jsii_name="automaticSync")
    def automatic_sync(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "automaticSync"))

    @automatic_sync.setter
    def automatic_sync(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContentLibrarySubscriptionOutputReference, "automatic_sync").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "automaticSync", value)

    @builtins.property
    @jsii.member(jsii_name="onDemand")
    def on_demand(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "onDemand"))

    @on_demand.setter
    def on_demand(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContentLibrarySubscriptionOutputReference, "on_demand").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onDemand", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "password"))

    @password.setter
    def password(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContentLibrarySubscriptionOutputReference, "password").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="subscriptionUrl")
    def subscription_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "subscriptionUrl"))

    @subscription_url.setter
    def subscription_url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContentLibrarySubscriptionOutputReference, "subscription_url").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscriptionUrl", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "username"))

    @username.setter
    def username(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContentLibrarySubscriptionOutputReference, "username").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[ContentLibrarySubscription]:
        return typing.cast(typing.Optional[ContentLibrarySubscription], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[ContentLibrarySubscription],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(ContentLibrarySubscriptionOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "ContentLibrary",
    "ContentLibraryConfig",
    "ContentLibraryPublication",
    "ContentLibraryPublicationOutputReference",
    "ContentLibrarySubscription",
    "ContentLibrarySubscriptionOutputReference",
]

publication.publish()
