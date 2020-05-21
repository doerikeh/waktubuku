from .models import UserLoginActivity
from django.contrib.auth import user_logged_in, user_login_failed
from django.dispatch import receiver
from .models import UserModel
import logging

error_log = logging.getLogger('error')

def get_client_ip(request):
    x_forwarded_for = request.Meta.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.Meta.get("REMOTE_ADDR")

    return ip

@receiver(user_logged_in)
def log_user_in_success(sender, user, request=None, **kwargs):
    try:
        user_agent_info = request.META.get("HTTP_USER_AGENT", '<unknown>')[:255]
        user_login_activity_log = UserLoginActivity(login_Ip=get_client_ip(request),
                                                    login_username=user.username_user,
                                                    user_agent_info=user_agent_info,
                                                    status=UserLoginActivity.SUCCESS)

        user_login_activity_log.save()

    except Exception as e:
        error_log.error("log_user_logged_in request:%s, error: %s" % (request, e))

@receiver(user_login_failed)
def log_user_in_failed(sender, credentials, request, **kwargs):
    try:
        user_agent_info = request.Meta.get("HTTP_USER_AGENT", '<unknown>')[:255]
        user_login_activity_log = UserLoginActivity(login_Ip=get_client_ip(request),
                                                    login_username=credentials['username_user'],
                                                    user_agent_info=user_agent_info,
                                                    status=UserLoginActivity.FAILED)

        user_login_activity_log.save()

    except Exception as e:
        error_log.error("log_user_logged_in request:%s, error: %s" % (request, e))