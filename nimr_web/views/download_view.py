import os

from django.conf import settings
from django.http import HttpResponse, Http404
from django.views import View
from django.views.generic import TemplateView


class DownloadView(View):
    # template_name = f"nimr_web/bootstrap/dp_finance.html"

    # def get_context_data(self, **kwargs):
    #     pass
        # file_path = os.path.join(settings.NEWS_ROOT, path)
        # if os.path.exists(file_path):
        #     with open(file_path, 'rb') as fh:
        #         response = HttpResponse(fh.read(), content_type="application/pdf")
        #         response['Content-Disposition'] = 'inline; filename=' + os.path.basename(
        #             file_path)
        #         return response
        # return context

        # Set FILE_STORAGE_PATH value in settings.py
        folder_path = settings.NEWS_ROOT
        # Here set the name of the file with extension
        file_name = ''
        # Set the content type value
        content_type_value = 'application/pdf'

        def get(self, request, file_name):
            self.file_name = file_name
            file_path = os.path.join(self.folder_path, self.file_name)
            if os.path.exists(file_path):
                with open(file_path, 'rb') as fh:
                    response = HttpResponse(
                        fh.read(),
                        content_type=self.content_type_value
                    )
                    response['Content-Disposition'] = 'inline; filename=' + os.path.basename(
                        file_path)
                return response
            else:
                raise Http404