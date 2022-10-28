import os

from django import template
from django.conf import settings
from django.http import HttpResponse, Http404
from django.urls import reverse

profile_url = 'nimr_web:profile'

register = template.Library()


@register.simple_tag(takes_context=True)
def staff_profile_link(context, staff):
    return reverse(profile_url, kwargs={'staff': staff})


@register.simple_tag(takes_context=True)
def download_publication_file(context, path):
    file_path = os.path.join(settings.NIMR_PUBLICATION_DIR, str(path))
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/pdf")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404