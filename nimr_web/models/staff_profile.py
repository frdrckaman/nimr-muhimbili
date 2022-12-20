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
    staff_photo = models.CharField(
        verbose_name='Image path',
        max_length=100,
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
