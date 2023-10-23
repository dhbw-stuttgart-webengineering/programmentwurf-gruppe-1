from datetime import timedelta, datetime
from ..data_endpoint.views import loading_view


def refresh_dualis(max_age=timedelta(minutes=30)):
    """Returns View that refreshes dualis data if it is older than max_age.

    Args:
        max_age (timedelta, optional): Maximum Age of data. Defaults to timedelta(minutes=5).
    """

    def decorator(view_func):
        def wrapped_view(request):
            last_update_time = datetime.now() - timedelta(minutes=4)  # testwise

            if datetime.now() - last_update_time > max_age:
                return loading_view(request)
            else:
                return view_func(request)

        return wrapped_view

    return decorator
