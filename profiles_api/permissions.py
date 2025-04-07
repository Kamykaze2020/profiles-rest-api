from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True
        # if the method is not in the SAFE_METHODS
        # we'll check if the obj we're updating matches the authentificated user profile
        # that is added to the authentification of the reqeuest
        # When you authenticate a reqeust in Django REST Framework it will assign the
        # authenticated user profile to the reqeuest and we can use this to compare to the
        # obj that is beeing updated and make sure they have the same id
        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
