from django.views.generic import TemplateView


class PublicationView(TemplateView):
    template_name = f"nimr_web/bootstrap/publications.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
