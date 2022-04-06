from rest_framework import permissions


class UserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action in ['create', 'update', 'partial_update', 'destroy']:
            return not request.user.is_anonymous
        elif view.action in ['retrieve', 'list']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        # if not request.user.is_authenticated():
        #     return False
        if view.action == ['create', 'update', 'partial_update', 'destroy']:
            return obj == request.user or request.user.is_admin
        elif view.action in ['retrieve', 'list']:
            return obj == request.user or request.user.is_anonymous
        else:
            return False
