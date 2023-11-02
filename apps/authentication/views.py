"""Login View"""
import base64

from Crypto.Cipher import AES
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.views import logout_then_login
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.decorators.cache import cache_control

from ..utils.dualis import Dualis, InvalidUsernameorPasswordException
from .forms import LoginForm
from .models import DualisUser
from datetime import timedelta


def encrypt(data):
    secret_key = settings.SECRET_KEY[0:16].encode("utf-8")

    cipher = AES.new(secret_key, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))
    return base64.b64encode(cipher.nonce + ciphertext + tag).decode('utf-8')


def decrypt(encrypted_data):
    secret_key = settings.SECRET_KEY[0:16].encode("utf-8")

    data = base64.b64decode(encrypted_data.encode('utf-8'))
    nonce, ciphertext, tag = data[:16], data[16:-16], data[-16:]
    cipher = AES.new(secret_key, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag).decode('utf-8')


def make_login(request: HttpRequest, email, password) -> bool:
    dualis = None

    dualis = Dualis(
        email, password)

    user, _ = DualisUser.objects.update_or_create(
        email=email, name=dualis.get_name())

    # for module in dualis.get_grades():
    #     print(module)

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
                success = make_login(request, email, password)
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
