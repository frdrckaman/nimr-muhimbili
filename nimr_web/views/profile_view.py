from django.views.generic import TemplateView
from ..models.staff_profile import StaffProfile


class ProfileView(TemplateView):
    template_name = f"nimr_web/bootstrap/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        staff_profile = StaffProfile.objects.get(id=context.get("staff"))
        context.update(staff_profile=staff_profile)
        return context
