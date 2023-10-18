from django.contrib.auth import login
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from ..utils.dualis import Dualis, InvalidUsernameorPasswordException
from .forms import LoginForm
from .models import DualisUser


def login_view(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    """Login View

    Args:
        request (HttpRequest): HttpRequest Object

    Returns:
        HttpResponse | HttpResponseRedirect: Renders login window or redirects
        to home page on successfull login.
    """
    form = LoginForm(request.POST or None)

    msg = None
    if request.method == "POST":

        if form.is_valid():
            email = form.cleaned_data.get("email")

            dualis = None

            try:
                dualis = Dualis(
                    email, form.cleaned_data.get("password"))
            except InvalidUsernameorPasswordException:
                msg = "Email oder Passwort falsch!"
            else:
                request.session.set_expiry(30 * 60)
                user, _ = DualisUser.objects.update_or_create(
                    email=email, name=dualis.getName())
                login(request, user,
                      backend='django.contrib.auth.backends.ModelBackend')
                return redirect("/")
        else:
            msg = 'Konnte nicht übermittelt werden.'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})
