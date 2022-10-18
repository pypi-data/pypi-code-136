import gettext

_t = gettext.translation('commandsheet', fallback=True)
_ = _t.gettext
ngettext = _t.ngettext
