from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CoreappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'coreapp'

    def ready(self):
        import coreapp.signals