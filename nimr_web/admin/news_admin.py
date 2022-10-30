from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple
from simple_history.admin import SimpleHistoryAdmin as BaseSimpleHistoryAdmin

from ..models import News

admin.site.enable_nav_sidebar = False


@admin.register(News)
class NewsAdmin(BaseSimpleHistoryAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "news_datetime",
                    "news_title",
                    "news_file_url",
                    "news_file",
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    list_display = (
        "news_title",
        "news_datetime",
    )

    list_filter = (
        "news_datetime",
    )

    search_fields = (
        "news_datetime",
        "news_title",
    )
