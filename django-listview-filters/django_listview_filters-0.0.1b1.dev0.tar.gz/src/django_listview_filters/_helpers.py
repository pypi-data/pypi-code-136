from django.conf import settings


def get_setting(setting_name: str, default):
    """Return <setting_name> from project settings if exists.
    
    :param setting_name: Literal string of setting name, case-sensitive
    :type setting_name: str
    :param default: Value if setting does not exist
    :type default: str
    """
    string = (
        getattr(settings, setting_name) if hasattr(settings, setting_name) else default
    )
    return string
