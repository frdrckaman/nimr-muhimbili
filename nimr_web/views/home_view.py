from django.views.generic import TemplateView
from nimr_web.models import News, Publication


class HomeView(TemplateView):
    template_name = f"nimr_web/bootstrap/base.html"

    def get_context_data(self, **kwargs):
        publications = Publication.objects.all()[:2]
        news = News.objects.all()[:16]
        context = super().get_context_data(**kwargs)
        context.update(
            publications=publications,
            news=news,
        )
        return context

