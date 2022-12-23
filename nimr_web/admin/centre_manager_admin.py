from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple
from simple_history.admin import SimpleHistoryAdmin as BaseSimpleHistoryAdmin

from ..models import CentreManagerPhoto

admin.site.enable_nav_sidebar = False


@admin.register(CentreManagerPhoto)
class CentreManagerPhotoAdmin(BaseSimpleHistoryAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "manager_name",
                    "manager_designation",
                    "manager_photo",
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    list_display = (
        "manager_name",
        "manager_designation",
        "manager_photo",
    )

    search_fields = (
        "manager_name",
    )
