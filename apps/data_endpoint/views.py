"""Data Endpoint View"""
from cryptography.fernet import InvalidToken
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse, HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.cache import cache_control

from apps.data_endpoint.process_data.collecting_data_from_dualis import save_data_in_dictionary
from ..utils.dualis import Dualis
from ..utils.dualis.exceptions import InvalidUsernameorPasswordException
from apps.data_endpoint.process_data.read_data import get_grades
from apps.data_endpoint.process_data.calculate_average import (calculate_average_module,
                                                               calculate_average_first_attempt,
                                                               calculate_average_second_attempt)
from ..authentication.views import decrypt, logout_view


@login_required(login_url="/login/")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def loading_view(request: HttpRequest) -> HttpResponse:
    """Returns loading view that redirects to the current page when data
    is refreshed

    Args:
        request (HttpRequest): HttpRequest Object

    Returns:
        HttpResponse: HttpResponse Object
    """

    if request.COOKIES.get("password"):
        return render(request, "home/loading.html",
                      {"redirect_url": request.path})
    else:
        return logout_view(request)


@login_required(login_url="/login/")
def refresh_data(request: HttpRequest) -> HttpResponse:
    """Refreshes the data of the user

    Args:
        request (HttpRequest): HttpRequest Object

    Returns:
        HttpResponse: HttpResponse Object
    """
    try:
        password = decrypt(request.COOKIES.get("password"))

        dualis = Dualis(request.user.email, password)

        data = dualis.get_grades()

        get_grades(request.user.email)

        calculate_average_first_attempt()

        calculate_average_second_attempt()

        calculate_average_module()

        save_data_in_dictionary(data, request.user.email)

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
