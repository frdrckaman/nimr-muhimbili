from django.db import models
from django.conf import settings
from edc_utils import get_utcnow
from simple_history.models import HistoricalRecords
from ..mixin import BaseUuidModel


class Publication(BaseUuidModel):
    publication_datetime = models.DateTimeField(
        verbose_name="Publication Date and Time",
        default=get_utcnow,
        help_text="Date and time of publications.",
    )
    publication_title = models.CharField(
        verbose_name='Publications Title',
        max_length=120,
    )

    publication_link = models.CharField(
        verbose_name='Publications Link',
        max_length=250,
        null=True,
        blank=True
    )

    publication_file = models.FileField(
        upload_to=settings.NIMR_PUBLICATION_DIR,
        null=True,
        blank=True,
    )

    history = HistoricalRecords()

    def __str__(self):
        return self.publication_title

    class Meta(BaseUuidModel.Meta):
        verbose_name = "Publications"
        verbose_name_plural = "Publications"
