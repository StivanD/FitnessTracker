from django.core.exceptions import PermissionDenied


def restrict_superuser_actions(get_response):
    def middleware(request):
        if not request.user.is_superuser and "admin/" in request.path:
            restricted_actions = ["delete", "add", "change"]
            if any(action in request.path for action in restricted_actions):
                raise PermissionDenied("You do not have permission to perform this action.")
        return get_response(request)

    return middleware
