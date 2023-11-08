"""Data Endpoint View"""
from cryptography.fernet import InvalidToken
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.cache import cache_control

from ..authentication.views import decrypt, logout_view
from ..utils.dualis import Dualis
from ..utils.dualis.exceptions import InvalidUsernameorPasswordException
from ..data_endpoint.data_save import search_data
from ..data_endpoint.read_data import get_grades

# Create your views here.


@login_required(login_url="/login/")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def loading_view(request: HttpRequest):
    """Returns loading view that redirects to the current page when data is refreshed

    Args:
        request (HttpRequest): _description_

    Returns:
        _type_: _description_
    """

    if request.COOKIES.get("password"):
        return render(request, "home/loading.html", {"redirect_url": request.path})
    else:
        return logout_view(request)


@login_required(login_url="/login/")
def refresh_data(request):
    """Refreshes the data from dualis and returns 200 on success
    """
    try:
        password = decrypt(request.COOKIES.get("password"))

        dualis = Dualis(request.user.email, password)

        data = dualis.get_grades()

        get_grades(request.user.email)

        search_data(data, request.user.email)

        request.user.last_updated = timezone.localtime()
        request.user.save()

        return JsonResponse({"Success": 200}, status=200)

    except InvalidUsernameorPasswordException:
        return logout_view(request)
    except ValueError:
        return logout_view(request)
    except InvalidToken:
        print("Invalid Token")
        return logout_view(request)
