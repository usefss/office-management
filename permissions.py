from rest_framework.permissions import BasePermission


class AnyBodyPermission(BasePermission):
    def has_permission(self, request, view):
        return True


class DefaultPermission(BasePermission):
    def has_permission(self, request, view):

        if not request.user or request.user.is_anonymous:
            self.message = 'user is not authenticated, add a token to your request'
            return False

        if request.method == 'GET':
            return True

        if request.user and (request.user.is_staff or request.user.is_superuser):
            return True
        else:  # this request is not a get and user is not staff higher
            self.message = f'user is not authorized to use {request.method} on this view'
            return False
