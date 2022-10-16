"""Custom settings."""

from django import forms
from django.utils.translation import ugettext_lazy as _

from kalabash.lib.form_utils import SeparatorField
from kalabash.lib.parameters import AdminParametersForm


class ParametersForm(AdminParametersForm):
    app = "kalabash_admin_limits"

    defv_sep = SeparatorField(label=_("Default limits"))

    deflt_domain_admins_limit = forms.IntegerField(
        label=_("Domain admins"),
        initial=0,
        help_text=_(
            "Maximum number of allowed domain administrators for a new "
            "administrator. (0 to deny any creation, -1 to allow unlimited "
            "creations)"
        ),
        widget=forms.widgets.TextInput(
            attrs={"class": "col-md-1 form-control"})
    )
    deflt_domains_limit = forms.IntegerField(
        label=_("Domains"),
        initial=0,
        help_text=_(
            "Maximum number of allowed domains for a new administrator. "
            "(0 to deny any creation, -1 to allow unlimited creations)"
        ),
        widget=forms.widgets.TextInput(
            attrs={"class": "col-md-1 form-control"})
    )
    deflt_domain_aliases_limit = forms.IntegerField(
        label=_("Domain aliases"),
        initial=0,
        help_text=_(
            "Maximum number of allowed domain aliases for a new "
            "administrator. (0 to deny any creation, -1 to allow "
            "unlimited creations)"
        ),
        widget=forms.widgets.TextInput(
            attrs={"class": "col-md-1 form-control"})
    )
    deflt_mailboxes_limit = forms.IntegerField(
        label=_("Mailboxes"),
        initial=0,
        help_text=_(
            "Maximum number of allowed mailboxes for a new administrator. "
            "(0 to deny any creation, -1 to allow unlimited creations)"
        ),
        widget=forms.widgets.TextInput(
            attrs={"class": "col-md-1 form-control"})
    )
    deflt_mailbox_aliases_limit = forms.IntegerField(
        label=_("Mailbox aliases"),
        initial=0,
        help_text=_(
            "Maximum number of allowed aliases for a new administrator. "
            "(0 to deny any creation, -1 to allow unlimited creations)"
        ),
        widget=forms.widgets.TextInput(
            attrs={"class": "col-md-1 form-control"})
    )

    def __init__(self, *args, **kwargs):
        super(AdminParametersForm, self).__init__(*args, **kwargs)
        self._load_extra_parameters('A')
