from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from django.utils.translation import gettext_lazy as _
from rest_framework.authentication import get_authorization_header


class RemoteUser:
    user_id = None
    is_authenticated = True

    def __init__(self, user_id):
        self.user_id = user_id

    def to_dict(self):
        return {
            'user_id': self.user_id,
        }


class RemoteAuthentication(authentication.TokenAuthentication):
    keyword = 'Bearer'
    model = None

    def authenticate_credentials(self, key):
        # authenticate key from auth service
        response = {'athenticate': True,
                    'user_id': 12, 'user_type': 'normal', }

        if not response.get('athenticate'):
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        user = RemoteUser(response.get('user_id'))

        return (user, response)
