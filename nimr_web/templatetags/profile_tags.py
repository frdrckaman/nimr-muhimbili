from django import template
from django.urls import reverse

profile_url = 'nimr_web:profile'

register = template.Library()


@register.simple_tag(takes_context=True)
def staff_profile_link(context, staff):
    return reverse(profile_url, kwargs={'staff': staff})