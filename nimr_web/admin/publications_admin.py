from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple
from simple_history.admin import SimpleHistoryAdmin as BaseSimpleHistoryAdmin

from ..models import Publication

admin.site.enable_nav_sidebar = False


@admin.register(Publication)
class PublicationAdmin(BaseSimpleHistoryAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "publication_datetime",
                    "publication_title",
                    "publication_file",
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    list_display = (
        "publication_title",
        "publication_datetime",
    )

    list_filter = (
        "publication_datetime",
    )

    search_fields = (
        "publication_datetime",
        "publication_title",
    )
