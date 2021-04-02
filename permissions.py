from rest_framework.permissions import BasePermission


class AnyBodyPermission(BasePermission):
    def has_permission(self, request, view):
        return True


class DoctorPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user or request.user.is_anonymous:
            self.message = 'user is not authenticated, add a token to your request'
            return False

        if request.user.is_doctor:
            return True

        self.message = 'you do not have the permission to access'
        return False


class PatientPermission(BasePermission):
    def has_permission(self, request, view):
        if not request.user or request.user.is_anonymous:
            self.message = 'user is not authenticated, add a token to your request'
            return False

        if request.user.is_patient:
            return True

        self.message = 'you do not have the permission to access'
        return False
