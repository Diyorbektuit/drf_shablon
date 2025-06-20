from rest_framework.exceptions import APIException
from rest_framework.permissions import BasePermission


class AuthenticationFailed(APIException):
    status_code = 401
    default_detail = 'Incorrect authentication credentials.'
    default_code = 'authentication_failed'


class IsAuthenticated(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            raise AuthenticationFailed()
        return True
