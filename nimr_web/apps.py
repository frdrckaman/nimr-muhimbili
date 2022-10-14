from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'nimr_web'
    verbose_name = "NIMR Website"
