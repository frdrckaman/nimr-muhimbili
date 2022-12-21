from django.conf import settings
from django.db import models
from simple_history.models import HistoricalRecords
from ..mixin import BaseUuidModel


class CentreManagerPhoto(BaseUuidModel):
    manager_name = models.CharField(
        verbose_name='Manager Name',
        max_length=130,
    )
    manager_designation = models.CharField(
        verbose_name='Designation',
        max_length=120,
    )
    manager_photo = models.FileField(
        upload_to=settings.NIMR_MANAGER_PHOTO,
        null=True,
        blank=True,
    )
    manager_photo_link = models.CharField(
        verbose_name='Link to an Image',
        max_length=100,
        null=True,
        blank=True,
    )

    history = HistoricalRecords()

    def __str__(self):
        return self.manager_name

    class Meta(BaseUuidModel.Meta):
        verbose_name = "Centre Manager Photo"
        verbose_name_plural = "Centre Manager Photo"
