from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from ..utils.dualis import Dualis, InvalidUsernameorPasswordException
from .forms import LoginForm


def login_view(request: HttpRequest) -> HttpResponse | HttpResponseRedirect:
    """Login View

    Args:
        request (HttpRequest): HttpRequest Object

    Returns:
        HttpResponse | HttpResponseRedirect: Renders login window or redirects to home page on successfull login.
    """
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")

            dualis = None

            try:
                dualis = Dualis(
                    username, form.cleaned_data.get("password"))
            except InvalidUsernameorPasswordException:
                msg = "Invalid credentials"
            else:
                request.session.set_expiry(30 * 60)
                user, _ = User.objects.get_or_create(username=username)
                login(request, user,
                      backend='django.contrib.auth.backends.ModelBackend')
                return redirect("/")
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})
