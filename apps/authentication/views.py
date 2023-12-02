"""Login View"""
from datetime import timedelta

from cryptography.fernet import Fernet
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.views import logout_then_login
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.decorators.cache import cache_control

from ..utils.dualis import Dualis, InvalidUsernameorPasswordException
from .forms import LoginForm
from .models import DualisUser


def encrypt(data: str) -> str:
    """Encrypts data with the SECRET_KEY from environment

    Args:
        data (str): String to encrypt

    Returns:
        str: Encrypted String
    """
    f = Fernet(settings.SECRET_KEY.encode())
    return f.encrypt(data.encode()).decode()


def decrypt(encrypted_data: str):
    """Decrypts data with the SECRET_KEY from environment

    Args:
        encrypted_data (str): Encrypted String

    Returns:
        _type_: Decrypted String
    """
    f = Fernet(settings.SECRET_KEY.encode())
    return f.decrypt(encrypted_data).decode()


def make_login(request: HttpRequest, email, password) -> bool:
    """Makes a login with the given credentials

    Args:
        request (HttpRequest): HttpRequest Object
        email (_type_): Email
        password (_type_): Password

    Returns:
        bool: True on successfull login
    """
    dualis = None

    dualis = Dualis(
        email, password)
    
    user, _ = DualisUser.objects.update_or_create(
        email=encrypt(email), name=encrypt(dualis.get_name()))

    login(request, user,
          backend='django.contrib.auth.backends.ModelBackend')

    return True


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login_view(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    """Login View

    Args:
        request (HttpRequest): HttpRequest Object

    Returns:
        HttpResponse | HttpResponseRedirect: Renders login window or 
        redirects to home page on successfull login.
    """
    form = LoginForm(request.POST or None)

    msg = None
    if request.method == "POST":

        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            try:
                _ = make_login(request, email, password)
            except InvalidUsernameorPasswordException:
                msg = 'Ungültige Anmeldedaten'
            else:
                if form.cleaned_data.get("rememberme"):
                    request.session.set_expiry(timedelta(days=30))
                else:
                    request.session.set_expiry(0)

                response = redirect("/")
                response.set_cookie(
                    "password", encrypt(form.cleaned_data.get("password")))

                return response
        else:
            msg = 'Konnte nicht übermittelt werden.'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def logout_view(request: HttpRequest) -> HttpResponseRedirect:
    """Logout View

    Args:
        request (HttpRequest): HttpRequest Object

    Returns:
        HttpResponseRedirect: Redirects to login page.
    """

    response = logout_then_login(request)
    response.set_cookie("password", None)

    return response
