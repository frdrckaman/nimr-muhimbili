from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple
from simple_history.admin import SimpleHistoryAdmin as BaseSimpleHistoryAdmin

from ..models import HeadDepartment

admin.site.enable_nav_sidebar = False


@admin.register(HeadDepartment)
class HeadDepartmentAdmin(BaseSimpleHistoryAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "head_name",
                    "head_department",
                    "head_metrics"
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    list_display = (
        "head_name",
        "head_department",
    )

    search_fields = (
        "head_name",
        "head_department",
    )
