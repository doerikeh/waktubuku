from django.apps import AppConfig


class ProfilebukuConfig(AppConfig):
    name = 'profilebuku'

    def ready(self):
        from .signals import log_user_in_failed, log_user_in_success
