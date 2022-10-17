from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.models import Orderable, Page
from wagtail.snippets.edit_handlers import FieldPanel

from modelcluster.models import ClusterableModel
from wagtail_rest_pack.sitesettings.snippets import ImageSliderItem
from django.utils.translation import gettext as _


class SiteSettingsSection(Orderable, models.Model):
    page = ParentalKey(Page, on_delete=models.CASCADE, related_name='carouselitems')
    slider = models.ForeignKey(ImageSliderItem, on_delete=models.CASCADE, related_name='+')
    panels = [
        FieldPanel('slider'),
    ]

    class Meta:
        verbose_name = _('Slider')
        verbose_name_plural = _('Sliders')
