from django.apps import AppConfig


class VotingboothApp(AppConfig):
    name = 'kegstarter.votingbooth'
    verbose_name = 'Voting Booth'

    def ready(self):
        from . import api  # noqa
