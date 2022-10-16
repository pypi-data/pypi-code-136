"""Core application constants."""

from django.conf import settings
from django.utils.translation import ugettext_lazy

STANDARDUSERS_ROLE = ("StandardUsers", ugettext_lazy("Standard user"))
DOMAINADMINS_ROLE = ("DomainAdmins", ugettext_lazy("Domain administrator"))
RESELLERS_ROLE = ("Resellers", ugettext_lazy("Reseller"))
SUPERADMINS_ROLE = ("SuperAdmins", ugettext_lazy("Super administrator"))

ROLES = (
    STANDARDUSERS_ROLE,
    DOMAINADMINS_ROLE,
    RESELLERS_ROLE,
    SUPERADMINS_ROLE,
)

ADMIN_GROUPS = [
    "SuperAdmins",
    "Resellers",
    "DomainAdmins",
]

LANGUAGES = (
    ("en", u"english"),
    ("fr", u"français"),
)


LDAP_GROUP_TYPES = (
    ("posixgroup", "PosixGroup"),
    ("groupofnames", "GroupOfNames"),
)

LDAP_SECURE_MODES = [
    ("none", ugettext_lazy("No")),
    ("starttls", "STARTTLS"),
    ("ssl", "SSL/TLS")
]

LDAP_AUTH_METHODS = [
    ("searchbind", ugettext_lazy("Search and bind")),
    ("directbind", ugettext_lazy("Direct bind"))
]

PERMISSIONS = {
    "StandardUsers": [],
    "DomainAdmins": [
        ["core", "user", "add_user"],
        ["core", "user", "change_user"],
        ["core", "user", "delete_user"],
        ["admin", "domain", "view_domain"],
        ["admin", "mailbox", "add_mailbox"],
        ["admin", "mailbox", "change_mailbox"],
        ["admin", "mailbox", "delete_mailbox"],
        ["admin", "mailbox", "view_mailbox"],
        ["admin", "alias", "add_alias"],
        ["admin", "alias", "change_alias"],
        ["admin", "alias", "delete_alias"],
        ["admin", "alias", "view_alias"],
        ["admin", "senderaddress", "add_senderaddress"],
        ["admin", "senderaddress", "change_senderaddress"],
        ["admin", "senderaddress", "delete_senderaddress"],
    ],
    "Resellers": [
        ["core", "user", "add_user"],
        ["core", "user", "change_user"],
        ["core", "user", "delete_user"],
        ["admin", "mailbox", "add_mailbox"],
        ["admin", "mailbox", "change_mailbox"],
        ["admin", "mailbox", "delete_mailbox"],
        ["admin", "mailbox", "view_mailbox"],
        ["admin", "alias", "add_alias"],
        ["admin", "alias", "change_alias"],
        ["admin", "alias", "delete_alias"],
        ["admin", "alias", "view_alias"],
        ["admin", "senderaddress", "add_senderaddress"],
        ["admin", "senderaddress", "change_senderaddress"],
        ["admin", "senderaddress", "delete_senderaddress"],
        ["admin", "domain", "add_domain"],
        ["admin", "domain", "change_domain"],
        ["admin", "domain", "delete_domain"],
        ["admin", "domain", "view_domain"],
        ["admin", "domainalias", "add_domainalias"],
        ["admin", "domainalias", "change_domainalias"],
        ["admin", "domainalias", "delete_domainalias"],
    ]
}

SMS_BACKENDS = [
    ("", ugettext_lazy("Choose a provider")),
    ("ovh", "OVH"),
]

if settings.DEBUG:
    SMS_BACKENDS.insert(1, ("dummy", ugettext_lazy("Dummy")))

TFA_DEVICE_TOKEN_KEY = "otp_device_id"
