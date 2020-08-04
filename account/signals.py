import logging
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.dispatch import receiver
from log.models import loginLog

@receiver(user_logged_in)
def sig_user_logged_in(sender, user, request, **kwargs):
    logger = logging.getLogger(__name__)
    logger.debug("user signed in: %s at %s" % (user, request.META['REMOTE_ADDR']))
    log = loginLog()
    log.loginUser = user
    log.ipaddr = request.META['REMOTE_ADDR']
    log.userAgent = request.META['HTTP_USER_AGENT']
    log.save()
