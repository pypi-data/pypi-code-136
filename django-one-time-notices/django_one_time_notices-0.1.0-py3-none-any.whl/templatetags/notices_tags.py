from classytags.helpers import InclusionTag
from django import template
from django.template.loader import render_to_string

from notices.models import Notice

register = template.Library()


class NoticesModal(InclusionTag):
    """
    Displays notices only if user hasn't seen it yet.
    """

    template = "notices/notices.html"

    def render_tag(self, context, **kwargs):
        template_filename = self.get_template(context, **kwargs)

        if "request" not in context:  # pragma: no cover
            return ""

        settings_config = Notice.from_settings()
        if settings_config is not None:
            version = settings_config["notices_version"]
        else:
            version = Notice.latest_version()
            if version == 0:
                return ""

            latest_notice = Notice.latest_notice()
            if latest_notice.has_expired():
                return ""

        if version == 0:  # version 0 --> clear the cookie
            return render_to_string(
                "notices/notices_clear.html", {}, getattr(context, "request", None)
            )

        try:
            cookie_version = int(context["request"].COOKIES.get("notices_seen"))
        except (ValueError, TypeError):
            # cookie wasn't there or wasn't an int
            # set to an impossible number so we show the notice
            cookie_version = -1

        if cookie_version == version:
            return ""

        data = self.get_context(context, **kwargs)
        return render_to_string(
            template_filename, data, getattr(context, "request", None)
        )


register.tag(NoticesModal)
