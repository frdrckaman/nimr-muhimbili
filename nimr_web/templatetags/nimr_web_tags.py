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


@register.inclusion_tag(
    f"nimr_web/bootstrap/tags/pagination.html",
    takes_context=True,
)
def pagination(context):
    page_obj = context.get("page_obj")
    num_pages = "a" * page_obj.paginator.num_pages if page_obj else 1
    show_pagination = True if page_obj.paginator.num_pages > settings.NIMR_PAGINATION else False

    return dict(
        page_obj=page_obj,
        pages=page_obj.paginator.num_pages,
        num_pages=num_pages,
        show_pagination=show_pagination,
    )


@register.inclusion_tag(
    f"nimr_web/bootstrap/tags/staff_photo.html",
    takes_context=True,
)
def staff_photo(context, img):
    photo = str(img).split('/')
    image = img if settings.DEBUG else f"{settings.NIMR_CDN_DOMAIN}" \
                                       f"{settings.NIMR_CDN_STAFF_PHOTO}{photo[-1]}"
    return dict(
        image=image,
        debug=settings.DEBUG
    )


@register.inclusion_tag(
    f"nimr_web/bootstrap/tags/centre_manager.html",
    takes_context=True,
)
def centre_manager(context, image=None, name=None, title=None):
    for manager in context.get("object_list")[:1]:
        image = manager['image']
        name = manager['manager_name']
        title = manager['manager_designation']

    return dict(
        image=image,
        name=name,
        title=title,
        debug=settings.DEBUG
    )
