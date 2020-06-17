from django.contrib.auth.backends import ModelBackend

from UAA.utils import UAAAuth


class UAABackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Send password based authentication request to UAA, returning decoded jwt token
        context = UAAAuth.authenticate(username, password)
        print(context)
        # All groups attached to the authenticated user
        scope = context['scope']
        print(scope)
        # Currently does database lookup for the user (Django default)
        super().authenticate(request, username, password, **kwargs)
