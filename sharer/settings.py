from django.conf import settings


ENABLE_EMAILS = getattr(settings, "SHARER_ENABLE_EMAILS", True)
BITLY_LOGIN = getattr(settings, "SHARER_BITLY_LOGIN", True)
BITLY_KEY = getattr(settings, "SHARER_BITLY_KEY", True)
