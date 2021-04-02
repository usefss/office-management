from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from django.utils.translation import gettext_lazy as _
from rest_framework.authentication import get_authorization_header


class RemoteUser:
    user_id = None
    is_authenticated = True
    role = None
    is_anonymous = False

    def __init__(self, user_id, role):
        self.user_id = user_id
        self.role = role

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'role': self.role
        }

    @property
    def is_patient(self):
        return self.role == 'patient'

    @property
    def is_doctor(self):
        return self.role == 'doctor'


class RemoteAuthentication(authentication.TokenAuthentication):
    keyword = 'Bearer'
    model = None

    def authenticate_credentials(self, key):
        # authenticate key from auth service
        response = {'athenticate': True,
                    'user_id': 12, 'role': 'patient', }

        if not response.get('athenticate'):
            raise exceptions.AuthenticationFailed(_('Invalid token.'))

        user = RemoteUser(response.get('user_id'), response.get('role'))

        return (user, response)
