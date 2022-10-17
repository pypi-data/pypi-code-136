from django.db import models
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from wagtail.models import Page
from wagtail.snippets.models import register_snippet
from taggit.models import Tag as TaggitTag
from django.utils.translation import gettext_lazy as _


@register_snippet
class Tag(TaggitTag):
    class Meta:
        verbose_name = _('Štítek')
        verbose_name_plural = _('Štítky')
        proxy = True


class PageTag(TaggedItemBase):
    content_object = ParentalKey(
        Page,
        related_name='%(app_label)s_%(class)s_items',
        on_delete=models.CASCADE,
    )
