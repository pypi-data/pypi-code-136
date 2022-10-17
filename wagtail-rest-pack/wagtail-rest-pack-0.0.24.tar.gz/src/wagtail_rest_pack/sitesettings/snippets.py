from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.images import get_image_model_string
from wagtail.fields import RichTextField

from django.utils.translation import gettext as _
from django.utils.html import strip_tags
@register_snippet
class ImageSliderItem(models.Model):
    image = models.ForeignKey(get_image_model_string(), on_delete=models.PROTECT, blank=False, null=True, default=None)
    text = RichTextField(features=['h2', 'h3', 'bold', 'italic', 'link'], max_length=200, blank=False, default="",
                         help_text=_('Text'))

    panels = [
        FieldPanel('text'),
        FieldPanel('image'),
    ]

    def __str__(self):
        return strip_tags(self.text)

    class Meta:
        verbose_name = _('Slider')
        verbose_name_plural = _('Sliders')
