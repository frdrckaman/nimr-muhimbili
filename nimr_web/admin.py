from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple
from simple_history.admin import SimpleHistoryAdmin as BaseSimpleHistoryAdmin

from .models import StaffProfile

admin.site.enable_nav_sidebar = False


@admin.register(StaffProfile)
class StaffProfileAdmin(BaseSimpleHistoryAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "staff_name",
                    "staff_metrics",
                    "staff_photo",
                    "staff_bio",
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    list_display = (
        "staff_name",
        "staff_metrics",
        "staff_photo",
    )

    list_filter = (
        "staff_name",
    )

    search_fields = (
        "staff_name",
    )
