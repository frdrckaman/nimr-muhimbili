from django.views.generic import TemplateView


class DPHritdView(TemplateView):
    template_name = f"nimr_web/bootstrap/dp_hritd.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context