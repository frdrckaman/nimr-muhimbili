from django.views.generic import TemplateView


class DPMonitoringView(TemplateView):
    template_name = f"nimr_web/bootstrap/dp_monitoring.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context