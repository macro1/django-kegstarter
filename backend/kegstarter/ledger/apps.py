from django.apps import AppConfig


class LedgerApp(AppConfig):
    name = 'kegstarter.ledger'

    def ready(self):
        from . import api  # noqa
