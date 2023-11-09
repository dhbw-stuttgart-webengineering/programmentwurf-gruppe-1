"""Decorators for the app."""
from datetime import timedelta
from django.utils import timezone
from ..data_endpoint.views import loading_view


def refresh_dualis(max_age=timedelta(minutes=1)):
    """Returns View that refreshes dualis data if it is older than max_age.

    Args:
        max_age (timedelta, optional): Maximum Age of data. Defaults to timedelta(minutes=5).
    """

    def decorator(view_func):
        def wrapped_view(request):
            if not request.user.last_updated:  # if no last_updated
                return loading_view(request)
            elif timezone.localtime() - request.user.last_updated > max_age:
                # if last_updated is older than max_age
                return loading_view(request)
            else:
                return view_func(request)

        return wrapped_view

    return decorator
