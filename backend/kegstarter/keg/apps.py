from django.apps import AppConfig


class KegApp(AppConfig):
    name = 'kegstarter.keg'

    def ready(self):
        from . import api  # noqa
