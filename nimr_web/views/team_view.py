from django.views.generic import TemplateView
from ..models.staff_profile import StaffProfile


class TeamView(TemplateView):
    template_name = f"nimr_web/bootstrap/team.html"

    def get_context_data(self, **kwargs):
        staffs = StaffProfile.objects.all()
        context = super().get_context_data(**kwargs)
        context.update(staffs=staffs)
        return context
