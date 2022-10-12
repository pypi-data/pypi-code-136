# python

# django
from django.db import models
from django.utils.translation import ugettext as _
from model_utils.models import TimeStampedModel

# open edx
from opaque_keys.edx.django.models import CourseKeyField


LMS_LANGUAGES = (
    ("en", "English"),
    ("es-419", "Español (Latinoamérica)"),  # Spanish (Latin America)
    ("pt-pt", "Português (Portugal)"),  # Portuguese (Portugal)
)

ALL_LANGUAGES = (
    ("en", "English"),
    ("en-uk", "English (United Kingdom)"),  # English (United Kingdom)
    ("en@lolcat", "LOLCAT English"),  # LOLCAT English
    ("en@pirate", "Pirate English"),  # Pirate English
    ("es-419", "Español (Latinoamérica)"),  # Spanish (Latin America)
    ("es-ar", "Español (Argentina)"),  # Spanish (Argentina)
    ("es-ec", "Español (Ecuador)"),  # Spanish (Ecuador)
    ("es-es", "Español (España)"),  # Spanish (Spain)
    ("es-mx", "Español (México)"),  # Spanish (Mexico)
    ("es-pe", "Español (Perú)"),  # Spanish (Peru)
    ("pt-br", "Português (Brasil)"),  # Portuguese (Brazil)
    ("pt-pt", "Português (Portugal)"),  # Portuguese (Portugal)
    ("it-it", "Italiano (Italia)"),  # Italian (Italy)
    ("fr", "Français"),  # French
)


class MarketingSites(TimeStampedModel):
    """
    Registers a marketing site by language code.
    Examples:
    -------------------
    es-419  maps to https://mx.stepwisemath.ai
    es-MX   maps to https://mx.stepwisemath.ai
    en      maps to https://stepwisemath.ai
    en-US   maps to https://stepwisemath.ai
    """

    class Meta:
        unique_together = ("language", "province")

    language = models.CharField(
        blank=False,
        choices=ALL_LANGUAGES,
        max_length=20,
        help_text=_("A language code. Examples: en, en-US, es, es-419, es-MX"),
    )
    province = models.CharField(
        max_length=20,
        blank=True,
        help_text=_(
            "A sub-region for the language code. Example: for language code en-US valid possibles include TX, FL, CA, DC, KY, etc."
        ),
    )
    site_url = models.URLField(
        default="https://stepwisemath.ai",
        blank=False,
        help_text=_("URL for for anchor tag for this language. Example: https://mx.stepwisemath.ai/contact/"),
    )

    def __str__(self):
        return self.language + "-" + self.province


class Locale(TimeStampedModel):
    """
    Stores localized urls and translated html tag element values by language code
    Used in conjunction with Mako templates to localize StepWise specific page content
    such as footer links.
    """

    class Meta:
        unique_together = ("element_id", "language")

    element_id = models.CharField(
        blank=False,
        max_length=255,
        help_text=_("An html element id. Example: stepwise-locale-contact"),
    )
    language = models.CharField(
        blank=False,
        choices=LMS_LANGUAGES,
        max_length=20,
        help_text=_("A language code. Examples: en, en-US, es, es-419, es-MX"),
    )
    url = models.URLField(
        blank=False,
        help_text=_("URL for for anchor tag for this language. Example: https://mx.stepwisemath.ai/contact/"),
    )
    value = models.CharField(
        blank=False,
        max_length=255,
        help_text=_("The text value of this html element. Example: Contacto"),
    )

    def __str__(self):
        return self.element_id + "-" + self.language


class Configuration(TimeStampedModel):
    """
    Creates the Stepwise Math configuration table for api settings.
    """

    DEVELOP = "dev"
    TEST = "test"
    PRODUCTION = "prod"

    configuration_type = (
        (DEVELOP, _("Development")),
        (TEST, _("Testing / QA")),
        (PRODUCTION, _("Production")),
    )
    type = models.CharField(
        max_length=24,
        blank=False,
        primary_key=True,
        choices=configuration_type,
        default=DEVELOP,
        unique=True,
        help_text=_("Type of Open edX environment in which this configuration will be used."),
    )
    stepwise_host = models.URLField(
        max_length=255, blank=True, help_text=_("the URL pointing to the Querium Stepwise Server.")
    )

    def __str__(self):
        return self.type


class EcommerceConfiguration(TimeStampedModel):
    """
    Course-level ecommerce configurations.
    """

    course_id = CourseKeyField(
        max_length=255,
        help_text="Open edX Course Key (Opaque Key). "
        "Based on Institution, Course, Section identifiers. Example: course-v1:edX+DemoX+Demo_Course",
        blank=False,
        default=None,
        primary_key=True,
    )

    payment_deadline_date = models.DateTimeField(
        help_text="The date after which the paywall will rise for enrolled students who have not yet paid.",
        null=True,
        blank=True,
    )

    class Meta(object):
        verbose_name = "Stepwise Math E-Commerce Configuration"
        verbose_name_plural = verbose_name + "s"

    def __str__(self):
        return self.course_id.html_id()


class EcommerceEOPWhitelist(TimeStampedModel):
    """
    Course-level EOP student lists for payment exemptions.
    """

    EOP = "eop_student"
    TESTER = "tester"
    RETAKE = "free_retake"

    whitelist_type = (
        (EOP, _("EOP Student")),
        (TESTER, _("Stepwise Math Tester")),
        (RETAKE, _("Free Retake")),
    )

    user_email = models.EmailField(unique=True)

    type = models.CharField(
        max_length=24,
        blank=False,
        choices=whitelist_type,
        default=EOP,
        help_text=_("Type of E-Commerce whitelist user."),
    )

    class Meta(object):
        verbose_name = "Stepwise Math E-Commerce Payment Exemption"
        verbose_name_plural = verbose_name + "s"
