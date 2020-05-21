import logging

from django.contrib.auth.signals import user_login_failed

from .signals import get_request


logger = logging.getLogger(__name__)


def log_login_failure(sender, credentials, **kwargs):
    http_request = get_request()

    msg = "Login failure {}".format(http_request.META['REMOTE_ADDR'])
    logger.error(msg)


user_login_failed.connect(log_login_failure)