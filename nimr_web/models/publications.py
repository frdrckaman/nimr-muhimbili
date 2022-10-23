from django.db import models
from django.conf import settings
from edc_utils import get_utcnow
from simple_history.models import HistoricalRecords
from ..mixin import BaseUuidModel


class Publication(BaseUuidModel):
    publication_datetime = models.DateTimeField(
        verbose_name="Publication Date and Time",
        default=get_utcnow,
        help_text="Date and time of report.",
    )
    publication_title = models.CharField(
        verbose_name='Publications Title',
        max_length=120,
    )

    publication_file = models.FileField(upload_to=settings.NIMR_PUBLICATION_DIR)

    history = HistoricalRecords()

    class Meta(BaseUuidModel.Meta):
        verbose_name = "Publications"
        verbose_name_plural = "Publications"
