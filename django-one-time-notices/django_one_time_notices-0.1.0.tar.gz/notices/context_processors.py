from notices.models import Notice


def notices(request):
    # first try to load Notice config from settings
    settings_config = Notice.from_settings()
    if settings_config is not None:
        return settings_config

    # if no settings, load latest version from db
    version = Notice.latest_version()
    if version == 0:
        title = content = None
    else:
        latest_notice = Notice.latest_notice()
        title = latest_notice.title
        content = latest_notice.content
    return {
        "notices_version": version,
        "notices_title": title,
        "notices_content": content,
    }
