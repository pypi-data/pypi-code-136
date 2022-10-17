from django.conf import settings
from django.db import models
from django.utils import timezone


class Notice(models.Model):

    title = models.CharField(max_length=255, default="New!")
    content = models.TextField()
    version = models.PositiveIntegerField(blank=True, unique=True)
    expires_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return (
            f"v{self.version} - "
            f"expires: {self.expires_at.strftime('%d-%b-%Y %H:%M UTC') if self.expires_at else 'never'}"
        )

    @classmethod
    def latest_notice(cls):
        return cls.objects.order_by("-version").first()

    @classmethod
    def latest_version(cls):
        if cls.objects.exists():
            return cls.latest_notice().version
        return 0

    @classmethod
    def from_settings(cls):
        if hasattr(settings, "NOTICES_VERSION"):
            try:
                version = int(settings.NOTICES_VERSION)
            except (TypeError, ValueError):
                ...
            else:
                return {
                    "notices_version": version,
                    "notices_title": getattr(settings, "NOTICES_TITLE", "New!"),
                    "notices_content": getattr(settings, "NOTICES_CONTENT", ""),
                    "notices_color": getattr(settings, "NOTICES_COLOR", None),
                }

    def has_expired(self):
        if not self.expires_at:
            return False
        return self.expires_at < timezone.now()

    def save(self, *args, **kwargs):
        if not self.id and not self.version:
            self.version = Notice.latest_version() + 1
        super().save(*args, **kwargs)
