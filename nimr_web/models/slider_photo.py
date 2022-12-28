from django.conf import settings
from django.db import models
from simple_history.models import HistoricalRecords
from ..mixin import BaseUuidModel


class SliderPhoto(BaseUuidModel):
    slider_subtitle = models.CharField(
        verbose_name='Top subtitle',
        max_length=130,
    )
    slider_title = models.CharField(
        verbose_name='Main Title',
        max_length=255,
    )
    slider_description = models.TextField(
        verbose_name='Short description',
        blank=True,
        null=True,
    )
    slider_photo = models.FileField(
        upload_to=settings.NIMR_CDN_SLIDER_PHOTO,
        null=True,
        blank=True,
    )
    slider_photo_link = models.CharField(
        verbose_name='Link to an Image',
        max_length=100,
        null=True,
        blank=True,
        help_text="Use this if image is located on a different server"
    )
    slider_metrics = models.IntegerField(
        verbose_name="Ordering metrics",
        default=0,
    )

    history = HistoricalRecords()

    def __str__(self):
        return self.slider_subtitle

    class Meta(BaseUuidModel.Meta):
        verbose_name = "Slider Photo"
        verbose_name_plural = "Slider Photo"
