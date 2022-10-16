from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = f"nimr_web/bootstrap/base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

