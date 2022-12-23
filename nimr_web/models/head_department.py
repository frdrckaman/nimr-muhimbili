from django.conf import settings
from django.db import models
from simple_history.models import HistoricalRecords
from ..mixin import BaseUuidModel


class HeadDepartment(BaseUuidModel):
    head_name = models.CharField(
        verbose_name='Head Name',
        max_length=160,
    )
    head_department = models.CharField(
        verbose_name='Department Name',
        max_length=200,
    )
    head_metrics = models.IntegerField(
        verbose_name='Metrics',
    )
    head_photo = models.FileField(
        upload_to=settings.NIMR_CDN_STAFF_PHOTO,
    )
    head_photo_link = models.CharField(
        verbose_name='Image path',
        max_length=200,
        blank=True,
        null=True,
        help_text="Use this if image is located on a different server"
    )

    history = HistoricalRecords()

    def __str__(self):
        return self.head_department

    class Meta(BaseUuidModel.Meta):
        verbose_name = "Head of Department"
        verbose_name_plural = "Head of Department"
