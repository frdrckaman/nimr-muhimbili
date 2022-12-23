from django.conf import settings
from django.db import models
from simple_history.models import HistoricalRecords
from ..mixin import BaseUuidModel


class StaffProfile(BaseUuidModel):
    staff_name = models.CharField(
        verbose_name='Staff Name',
        max_length=130,
    )
    staff_designation = models.CharField(
        verbose_name='Designation',
        max_length=120,
    )
    staff_metrics = models.IntegerField(
        verbose_name='Metrics',
    )
    staff_photo = models.FileField(
        upload_to=settings.NIMR_CDN_STAFF_PHOTO,
    )
    staff_photo_link = models.CharField(
        verbose_name='Image Link',
        max_length=200,
        blank=True,
        null=True,
        help_text="Use this if image is located on a different server"
    )
    staff_bio = models.TextField(
        verbose_name='Bio',
    )

    history = HistoricalRecords()

    def __str__(self):
        return self.staff_name

    class Meta(BaseUuidModel.Meta):
        verbose_name = "Staff Profile"
        verbose_name_plural = "Staff Profile"
