from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple
from simple_history.admin import SimpleHistoryAdmin as BaseSimpleHistoryAdmin

from ..models import SliderPhoto

admin.site.enable_nav_sidebar = False


@admin.register(SliderPhoto)
class SliderPhotoAdmin(BaseSimpleHistoryAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "slider_subtitle",
                    "slider_title",
                    "slider_description",
                    "slider_photo",
                    "slider_photo_link",
                    "slider_metrics",
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    list_display = (
        "slider_subtitle",
        "slider_title",
        "slider_description",
        "slider_photo",
    )

    search_fields = (
        "slider_subtitle",
    )
