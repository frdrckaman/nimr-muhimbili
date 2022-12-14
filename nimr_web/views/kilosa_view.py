from django.views.generic import TemplateView


class KilosaView(TemplateView):
    template_name = f"nimr_web/bootstrap/kilosa.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context