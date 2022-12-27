from django.conf import settings
from django.views.generic import TemplateView

from nimr_web.models import Publication, News, SliderPhoto
from nimr_web.models.centre_manager import CentreManagerPhoto


class ViewMixin(TemplateView):
    ordering = "-report_datetime"
    model = CentreManagerPhoto
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        publications = Publication.objects.all()[:2]
        news = News.objects.all()[:16]
        queryset = CentreManagerPhoto.objects.all()
        sliders = SliderPhoto.objects.all().order_by('slider_metrics')
        context.update(
            object_list=self.get_wrapped_queryset(queryset),
            publications=publications,
            sliders=self.get_wrapped_slider(sliders),
            news=news,
        )
        return context

    def get_wrapped_queryset(self, queryset):
        wrapped_objs = []
        for obj_qry in queryset:
            obj = self.get_model_dict(obj_qry)
            photo = str(obj['manager_photo']).split('/')
            if settings.DEBUG:
                obj['image'] = obj['manager_photo']
            else:
                obj['image'] = f"{settings.NIMR_CDN_DOMAIN}{settings.NIMR_MANAGER_PHOTO}{photo[-1]}"
            wrapped_objs.append(obj)
        return wrapped_objs

    def get_wrapped_slider(self, queryset):
        wrapped_objs = []
        for obj_qry in queryset:
            obj = self.get_model_dict(obj_qry)
            photo = str(obj['slider_photo']).split('/')
            if settings.DEBUG:
                obj['image'] = obj['slider_photo']
            else:
                obj['image'] = f"{settings.NIMR_CDN_DOMAIN}{settings.NIMR_CDN_SLIDER_PHOTO}{photo[-1]}"
            wrapped_objs.append(obj)
        return wrapped_objs

    @staticmethod
    def get_model_dict(queryset):
        return queryset.__dict__
