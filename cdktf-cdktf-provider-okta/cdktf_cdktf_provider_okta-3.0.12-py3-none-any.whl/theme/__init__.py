'''
# `okta_theme`

Refer to the Terraform Registory for docs: [`okta_theme`](https://www.terraform.io/docs/providers/okta/r/theme).
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


class Theme(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-okta.theme.Theme",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/okta/r/theme okta_theme}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id: builtins.str,
        *,
        brand_id: builtins.str,
        background_image: typing.Optional[builtins.str] = None,
        email_template_touch_point_variant: typing.Optional[builtins.str] = None,
        end_user_dashboard_touch_point_variant: typing.Optional[builtins.str] = None,
        error_page_touch_point_variant: typing.Optional[builtins.str] = None,
        favicon: typing.Optional[builtins.str] = None,
        logo: typing.Optional[builtins.str] = None,
        primary_color_contrast_hex: typing.Optional[builtins.str] = None,
        primary_color_hex: typing.Optional[builtins.str] = None,
        secondary_color_contrast_hex: typing.Optional[builtins.str] = None,
        secondary_color_hex: typing.Optional[builtins.str] = None,
        sign_in_page_touch_point_variant: typing.Optional[builtins.str] = None,
        theme_id: typing.Optional[builtins.str] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/okta/r/theme okta_theme} Resource.

        :param scope: The scope in which to define this construct.
        :param id: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param brand_id: Brand ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#brand_id Theme#brand_id}
        :param background_image: Path to local file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#background_image Theme#background_image}
        :param email_template_touch_point_variant: Variant for email templates (``OKTA_DEFAULT``, ``FULL_THEME``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#email_template_touch_point_variant Theme#email_template_touch_point_variant}
        :param end_user_dashboard_touch_point_variant: Variant for the Okta End-User Dashboard (``OKTA_DEFAULT``, ``WHITE_LOGO_BACKGROUND``, ``FULL_THEME``, ``LOGO_ON_FULL_WHITE_BACKGROUND``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#end_user_dashboard_touch_point_variant Theme#end_user_dashboard_touch_point_variant}
        :param error_page_touch_point_variant: Variant for the error page (``OKTA_DEFAULT``, ``BACKGROUND_SECONDARY_COLOR``, ``BACKGROUND_IMAGE``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#error_page_touch_point_variant Theme#error_page_touch_point_variant}
        :param favicon: Path to local file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#favicon Theme#favicon}
        :param logo: Path to local file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#logo Theme#logo}
        :param primary_color_contrast_hex: Primary color contrast hex code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#primary_color_contrast_hex Theme#primary_color_contrast_hex}
        :param primary_color_hex: Primary color hex code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#primary_color_hex Theme#primary_color_hex}
        :param secondary_color_contrast_hex: Secondary color contrast hex code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#secondary_color_contrast_hex Theme#secondary_color_contrast_hex}
        :param secondary_color_hex: Secondary color hex code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#secondary_color_hex Theme#secondary_color_hex}
        :param sign_in_page_touch_point_variant: Variant for the Okta Sign-In Page (``OKTA_DEFAULT``, ``BACKGROUND_SECONDARY_COLOR``, ``BACKGROUND_IMAGE``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#sign_in_page_touch_point_variant Theme#sign_in_page_touch_point_variant}
        :param theme_id: Theme ID - Note: Okta API for theme only reads and updates therefore the okta_theme resource needs to act as a quasi data source. Do this by setting theme_id. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#theme_id Theme#theme_id}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(Theme.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        config = ThemeConfig(
            brand_id=brand_id,
            background_image=background_image,
            email_template_touch_point_variant=email_template_touch_point_variant,
            end_user_dashboard_touch_point_variant=end_user_dashboard_touch_point_variant,
            error_page_touch_point_variant=error_page_touch_point_variant,
            favicon=favicon,
            logo=logo,
            primary_color_contrast_hex=primary_color_contrast_hex,
            primary_color_hex=primary_color_hex,
            secondary_color_contrast_hex=secondary_color_contrast_hex,
            secondary_color_hex=secondary_color_hex,
            sign_in_page_touch_point_variant=sign_in_page_touch_point_variant,
            theme_id=theme_id,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id, config])

    @jsii.member(jsii_name="resetBackgroundImage")
    def reset_background_image(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetBackgroundImage", []))

    @jsii.member(jsii_name="resetEmailTemplateTouchPointVariant")
    def reset_email_template_touch_point_variant(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEmailTemplateTouchPointVariant", []))

    @jsii.member(jsii_name="resetEndUserDashboardTouchPointVariant")
    def reset_end_user_dashboard_touch_point_variant(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEndUserDashboardTouchPointVariant", []))

    @jsii.member(jsii_name="resetErrorPageTouchPointVariant")
    def reset_error_page_touch_point_variant(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetErrorPageTouchPointVariant", []))

    @jsii.member(jsii_name="resetFavicon")
    def reset_favicon(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFavicon", []))

    @jsii.member(jsii_name="resetLogo")
    def reset_logo(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLogo", []))

    @jsii.member(jsii_name="resetPrimaryColorContrastHex")
    def reset_primary_color_contrast_hex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimaryColorContrastHex", []))

    @jsii.member(jsii_name="resetPrimaryColorHex")
    def reset_primary_color_hex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrimaryColorHex", []))

    @jsii.member(jsii_name="resetSecondaryColorContrastHex")
    def reset_secondary_color_contrast_hex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecondaryColorContrastHex", []))

    @jsii.member(jsii_name="resetSecondaryColorHex")
    def reset_secondary_color_hex(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSecondaryColorHex", []))

    @jsii.member(jsii_name="resetSignInPageTouchPointVariant")
    def reset_sign_in_page_touch_point_variant(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSignInPageTouchPointVariant", []))

    @jsii.member(jsii_name="resetThemeId")
    def reset_theme_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetThemeId", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="backgroundImageUrl")
    def background_image_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backgroundImageUrl"))

    @builtins.property
    @jsii.member(jsii_name="faviconUrl")
    def favicon_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "faviconUrl"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @builtins.property
    @jsii.member(jsii_name="links")
    def links(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "links"))

    @builtins.property
    @jsii.member(jsii_name="logoUrl")
    def logo_url(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logoUrl"))

    @builtins.property
    @jsii.member(jsii_name="backgroundImageInput")
    def background_image_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backgroundImageInput"))

    @builtins.property
    @jsii.member(jsii_name="brandIdInput")
    def brand_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "brandIdInput"))

    @builtins.property
    @jsii.member(jsii_name="emailTemplateTouchPointVariantInput")
    def email_template_touch_point_variant_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "emailTemplateTouchPointVariantInput"))

    @builtins.property
    @jsii.member(jsii_name="endUserDashboardTouchPointVariantInput")
    def end_user_dashboard_touch_point_variant_input(
        self,
    ) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endUserDashboardTouchPointVariantInput"))

    @builtins.property
    @jsii.member(jsii_name="errorPageTouchPointVariantInput")
    def error_page_touch_point_variant_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "errorPageTouchPointVariantInput"))

    @builtins.property
    @jsii.member(jsii_name="faviconInput")
    def favicon_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "faviconInput"))

    @builtins.property
    @jsii.member(jsii_name="logoInput")
    def logo_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logoInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryColorContrastHexInput")
    def primary_color_contrast_hex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "primaryColorContrastHexInput"))

    @builtins.property
    @jsii.member(jsii_name="primaryColorHexInput")
    def primary_color_hex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "primaryColorHexInput"))

    @builtins.property
    @jsii.member(jsii_name="secondaryColorContrastHexInput")
    def secondary_color_contrast_hex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secondaryColorContrastHexInput"))

    @builtins.property
    @jsii.member(jsii_name="secondaryColorHexInput")
    def secondary_color_hex_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "secondaryColorHexInput"))

    @builtins.property
    @jsii.member(jsii_name="signInPageTouchPointVariantInput")
    def sign_in_page_touch_point_variant_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "signInPageTouchPointVariantInput"))

    @builtins.property
    @jsii.member(jsii_name="themeIdInput")
    def theme_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "themeIdInput"))

    @builtins.property
    @jsii.member(jsii_name="backgroundImage")
    def background_image(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "backgroundImage"))

    @background_image.setter
    def background_image(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Theme, "background_image").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backgroundImage", value)

    @builtins.property
    @jsii.member(jsii_name="brandId")
    def brand_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "brandId"))

    @brand_id.setter
    def brand_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Theme, "brand_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "brandId", value)

    @builtins.property
    @jsii.member(jsii_name="emailTemplateTouchPointVariant")
    def email_template_touch_point_variant(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "emailTemplateTouchPointVariant"))

    @email_template_touch_point_variant.setter
    def email_template_touch_point_variant(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Theme, "email_template_touch_point_variant").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailTemplateTouchPointVariant", value)

    @builtins.property
    @jsii.member(jsii_name="endUserDashboardTouchPointVariant")
    def end_user_dashboard_touch_point_variant(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "endUserDashboardTouchPointVariant"))

    @end_user_dashboard_touch_point_variant.setter
    def end_user_dashboard_touch_point_variant(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Theme, "end_user_dashboard_touch_point_variant").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endUserDashboardTouchPointVariant", value)

    @builtins.property
    @jsii.member(jsii_name="errorPageTouchPointVariant")
    def error_page_touch_point_variant(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "errorPageTouchPointVariant"))

    @error_page_touch_point_variant.setter
    def error_page_touch_point_variant(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Theme, "error_page_touch_point_variant").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "errorPageTouchPointVariant", value)

    @builtins.property
    @jsii.member(jsii_name="favicon")
    def favicon(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "favicon"))

    @favicon.setter
    def favicon(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Theme, "favicon").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "favicon", value)

    @builtins.property
    @jsii.member(jsii_name="logo")
    def logo(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "logo"))

    @logo.setter
    def logo(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Theme, "logo").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logo", value)

    @builtins.property
    @jsii.member(jsii_name="primaryColorContrastHex")
    def primary_color_contrast_hex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryColorContrastHex"))

    @primary_color_contrast_hex.setter
    def primary_color_contrast_hex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Theme, "primary_color_contrast_hex").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryColorContrastHex", value)

    @builtins.property
    @jsii.member(jsii_name="primaryColorHex")
    def primary_color_hex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "primaryColorHex"))

    @primary_color_hex.setter
    def primary_color_hex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Theme, "primary_color_hex").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryColorHex", value)

    @builtins.property
    @jsii.member(jsii_name="secondaryColorContrastHex")
    def secondary_color_contrast_hex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryColorContrastHex"))

    @secondary_color_contrast_hex.setter
    def secondary_color_contrast_hex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Theme, "secondary_color_contrast_hex").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secondaryColorContrastHex", value)

    @builtins.property
    @jsii.member(jsii_name="secondaryColorHex")
    def secondary_color_hex(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "secondaryColorHex"))

    @secondary_color_hex.setter
    def secondary_color_hex(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Theme, "secondary_color_hex").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "secondaryColorHex", value)

    @builtins.property
    @jsii.member(jsii_name="signInPageTouchPointVariant")
    def sign_in_page_touch_point_variant(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "signInPageTouchPointVariant"))

    @sign_in_page_touch_point_variant.setter
    def sign_in_page_touch_point_variant(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Theme, "sign_in_page_touch_point_variant").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signInPageTouchPointVariant", value)

    @builtins.property
    @jsii.member(jsii_name="themeId")
    def theme_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "themeId"))

    @theme_id.setter
    def theme_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(Theme, "theme_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "themeId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-okta.theme.ThemeConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "brand_id": "brandId",
        "background_image": "backgroundImage",
        "email_template_touch_point_variant": "emailTemplateTouchPointVariant",
        "end_user_dashboard_touch_point_variant": "endUserDashboardTouchPointVariant",
        "error_page_touch_point_variant": "errorPageTouchPointVariant",
        "favicon": "favicon",
        "logo": "logo",
        "primary_color_contrast_hex": "primaryColorContrastHex",
        "primary_color_hex": "primaryColorHex",
        "secondary_color_contrast_hex": "secondaryColorContrastHex",
        "secondary_color_hex": "secondaryColorHex",
        "sign_in_page_touch_point_variant": "signInPageTouchPointVariant",
        "theme_id": "themeId",
    },
)
class ThemeConfig(cdktf.TerraformMetaArguments):
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
        brand_id: builtins.str,
        background_image: typing.Optional[builtins.str] = None,
        email_template_touch_point_variant: typing.Optional[builtins.str] = None,
        end_user_dashboard_touch_point_variant: typing.Optional[builtins.str] = None,
        error_page_touch_point_variant: typing.Optional[builtins.str] = None,
        favicon: typing.Optional[builtins.str] = None,
        logo: typing.Optional[builtins.str] = None,
        primary_color_contrast_hex: typing.Optional[builtins.str] = None,
        primary_color_hex: typing.Optional[builtins.str] = None,
        secondary_color_contrast_hex: typing.Optional[builtins.str] = None,
        secondary_color_hex: typing.Optional[builtins.str] = None,
        sign_in_page_touch_point_variant: typing.Optional[builtins.str] = None,
        theme_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param brand_id: Brand ID. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#brand_id Theme#brand_id}
        :param background_image: Path to local file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#background_image Theme#background_image}
        :param email_template_touch_point_variant: Variant for email templates (``OKTA_DEFAULT``, ``FULL_THEME``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#email_template_touch_point_variant Theme#email_template_touch_point_variant}
        :param end_user_dashboard_touch_point_variant: Variant for the Okta End-User Dashboard (``OKTA_DEFAULT``, ``WHITE_LOGO_BACKGROUND``, ``FULL_THEME``, ``LOGO_ON_FULL_WHITE_BACKGROUND``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#end_user_dashboard_touch_point_variant Theme#end_user_dashboard_touch_point_variant}
        :param error_page_touch_point_variant: Variant for the error page (``OKTA_DEFAULT``, ``BACKGROUND_SECONDARY_COLOR``, ``BACKGROUND_IMAGE``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#error_page_touch_point_variant Theme#error_page_touch_point_variant}
        :param favicon: Path to local file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#favicon Theme#favicon}
        :param logo: Path to local file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#logo Theme#logo}
        :param primary_color_contrast_hex: Primary color contrast hex code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#primary_color_contrast_hex Theme#primary_color_contrast_hex}
        :param primary_color_hex: Primary color hex code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#primary_color_hex Theme#primary_color_hex}
        :param secondary_color_contrast_hex: Secondary color contrast hex code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#secondary_color_contrast_hex Theme#secondary_color_contrast_hex}
        :param secondary_color_hex: Secondary color hex code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#secondary_color_hex Theme#secondary_color_hex}
        :param sign_in_page_touch_point_variant: Variant for the Okta Sign-In Page (``OKTA_DEFAULT``, ``BACKGROUND_SECONDARY_COLOR``, ``BACKGROUND_IMAGE``). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#sign_in_page_touch_point_variant Theme#sign_in_page_touch_point_variant}
        :param theme_id: Theme ID - Note: Okta API for theme only reads and updates therefore the okta_theme resource needs to act as a quasi data source. Do this by setting theme_id. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#theme_id Theme#theme_id}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if __debug__:
            type_hints = typing.get_type_hints(ThemeConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument brand_id", value=brand_id, expected_type=type_hints["brand_id"])
            check_type(argname="argument background_image", value=background_image, expected_type=type_hints["background_image"])
            check_type(argname="argument email_template_touch_point_variant", value=email_template_touch_point_variant, expected_type=type_hints["email_template_touch_point_variant"])
            check_type(argname="argument end_user_dashboard_touch_point_variant", value=end_user_dashboard_touch_point_variant, expected_type=type_hints["end_user_dashboard_touch_point_variant"])
            check_type(argname="argument error_page_touch_point_variant", value=error_page_touch_point_variant, expected_type=type_hints["error_page_touch_point_variant"])
            check_type(argname="argument favicon", value=favicon, expected_type=type_hints["favicon"])
            check_type(argname="argument logo", value=logo, expected_type=type_hints["logo"])
            check_type(argname="argument primary_color_contrast_hex", value=primary_color_contrast_hex, expected_type=type_hints["primary_color_contrast_hex"])
            check_type(argname="argument primary_color_hex", value=primary_color_hex, expected_type=type_hints["primary_color_hex"])
            check_type(argname="argument secondary_color_contrast_hex", value=secondary_color_contrast_hex, expected_type=type_hints["secondary_color_contrast_hex"])
            check_type(argname="argument secondary_color_hex", value=secondary_color_hex, expected_type=type_hints["secondary_color_hex"])
            check_type(argname="argument sign_in_page_touch_point_variant", value=sign_in_page_touch_point_variant, expected_type=type_hints["sign_in_page_touch_point_variant"])
            check_type(argname="argument theme_id", value=theme_id, expected_type=type_hints["theme_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "brand_id": brand_id,
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
        if background_image is not None:
            self._values["background_image"] = background_image
        if email_template_touch_point_variant is not None:
            self._values["email_template_touch_point_variant"] = email_template_touch_point_variant
        if end_user_dashboard_touch_point_variant is not None:
            self._values["end_user_dashboard_touch_point_variant"] = end_user_dashboard_touch_point_variant
        if error_page_touch_point_variant is not None:
            self._values["error_page_touch_point_variant"] = error_page_touch_point_variant
        if favicon is not None:
            self._values["favicon"] = favicon
        if logo is not None:
            self._values["logo"] = logo
        if primary_color_contrast_hex is not None:
            self._values["primary_color_contrast_hex"] = primary_color_contrast_hex
        if primary_color_hex is not None:
            self._values["primary_color_hex"] = primary_color_hex
        if secondary_color_contrast_hex is not None:
            self._values["secondary_color_contrast_hex"] = secondary_color_contrast_hex
        if secondary_color_hex is not None:
            self._values["secondary_color_hex"] = secondary_color_hex
        if sign_in_page_touch_point_variant is not None:
            self._values["sign_in_page_touch_point_variant"] = sign_in_page_touch_point_variant
        if theme_id is not None:
            self._values["theme_id"] = theme_id

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
    def brand_id(self) -> builtins.str:
        '''Brand ID.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#brand_id Theme#brand_id}
        '''
        result = self._values.get("brand_id")
        assert result is not None, "Required property 'brand_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def background_image(self) -> typing.Optional[builtins.str]:
        '''Path to local file.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#background_image Theme#background_image}
        '''
        result = self._values.get("background_image")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def email_template_touch_point_variant(self) -> typing.Optional[builtins.str]:
        '''Variant for email templates (``OKTA_DEFAULT``, ``FULL_THEME``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#email_template_touch_point_variant Theme#email_template_touch_point_variant}
        '''
        result = self._values.get("email_template_touch_point_variant")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def end_user_dashboard_touch_point_variant(self) -> typing.Optional[builtins.str]:
        '''Variant for the Okta End-User Dashboard (``OKTA_DEFAULT``, ``WHITE_LOGO_BACKGROUND``, ``FULL_THEME``, ``LOGO_ON_FULL_WHITE_BACKGROUND``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#end_user_dashboard_touch_point_variant Theme#end_user_dashboard_touch_point_variant}
        '''
        result = self._values.get("end_user_dashboard_touch_point_variant")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def error_page_touch_point_variant(self) -> typing.Optional[builtins.str]:
        '''Variant for the error page (``OKTA_DEFAULT``, ``BACKGROUND_SECONDARY_COLOR``, ``BACKGROUND_IMAGE``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#error_page_touch_point_variant Theme#error_page_touch_point_variant}
        '''
        result = self._values.get("error_page_touch_point_variant")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def favicon(self) -> typing.Optional[builtins.str]:
        '''Path to local file.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#favicon Theme#favicon}
        '''
        result = self._values.get("favicon")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logo(self) -> typing.Optional[builtins.str]:
        '''Path to local file.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#logo Theme#logo}
        '''
        result = self._values.get("logo")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def primary_color_contrast_hex(self) -> typing.Optional[builtins.str]:
        '''Primary color contrast hex code.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#primary_color_contrast_hex Theme#primary_color_contrast_hex}
        '''
        result = self._values.get("primary_color_contrast_hex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def primary_color_hex(self) -> typing.Optional[builtins.str]:
        '''Primary color hex code.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#primary_color_hex Theme#primary_color_hex}
        '''
        result = self._values.get("primary_color_hex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secondary_color_contrast_hex(self) -> typing.Optional[builtins.str]:
        '''Secondary color contrast hex code.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#secondary_color_contrast_hex Theme#secondary_color_contrast_hex}
        '''
        result = self._values.get("secondary_color_contrast_hex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def secondary_color_hex(self) -> typing.Optional[builtins.str]:
        '''Secondary color hex code.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#secondary_color_hex Theme#secondary_color_hex}
        '''
        result = self._values.get("secondary_color_hex")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sign_in_page_touch_point_variant(self) -> typing.Optional[builtins.str]:
        '''Variant for the Okta Sign-In Page (``OKTA_DEFAULT``, ``BACKGROUND_SECONDARY_COLOR``, ``BACKGROUND_IMAGE``).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#sign_in_page_touch_point_variant Theme#sign_in_page_touch_point_variant}
        '''
        result = self._values.get("sign_in_page_touch_point_variant")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def theme_id(self) -> typing.Optional[builtins.str]:
        '''Theme ID - Note: Okta API for theme only reads and updates therefore the okta_theme resource needs to act as a quasi data source.

        Do this by setting theme_id.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/okta/r/theme#theme_id Theme#theme_id}
        '''
        result = self._values.get("theme_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ThemeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Theme",
    "ThemeConfig",
]

publication.publish()
