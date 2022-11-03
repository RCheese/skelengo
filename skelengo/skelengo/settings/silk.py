SILKY_META = True
SILKY_INTERCEPT_PERCENT = 25
SILKY_AUTHENTICATION = True
SILKY_AUTHORISATION = True

SILKY_PERMISSIONS = lambda user: user.is_superuser


def custom_intercept(request):
    if "probes/" in request.path:
        return False
    return True


SILKY_INTERCEPT_FUNC = custom_intercept
