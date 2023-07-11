from django.db import models
from simple_history.models import HistoricalRecords
from ..mixin import BaseUuidModel


class HeadDepartment(BaseUuidModel):
    head_name = models.ForeignKey(
        'StaffProfile', on_delete=models.CASCADE
    )
    head_department = models.CharField(
        verbose_name='Department Name',
        max_length=200,
    )
    head_metrics = models.IntegerField(
        verbose_name='Metrics',
    )

    history = HistoricalRecords()

    def __str__(self):
        return self.head_department

    class Meta(BaseUuidModel.Meta):
        verbose_name = "Head of Department"
        verbose_name_plural = "Head of Department"
