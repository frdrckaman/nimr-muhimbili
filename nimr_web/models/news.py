from django.db import models
from django.conf import settings
from edc_utils import get_utcnow
from simple_history.models import HistoricalRecords
from ..mixin import BaseUuidModel


class News(BaseUuidModel):
    news_datetime = models.DateTimeField(
        verbose_name="News Date and Time",
        default=get_utcnow,
        help_text="Date and time of news.",
    )
    news_title = models.CharField(
        verbose_name='News Title',
        max_length=120,
    )

    news_file_url = models.CharField(
        verbose_name='File URL',
        max_length=255,
        blank=True,
        null=True,
    )

    news_file = models.FileField(upload_to=settings.NIMR_NEWS_DIR)

    history = HistoricalRecords()

    class Meta(BaseUuidModel.Meta):
        verbose_name = "News"
        verbose_name_plural = "News"
