from django.apps import AppConfig


class BeerApp(AppConfig):
    name = 'kegstarter.beer'

    def ready(self):
        from . import api  # noqa
