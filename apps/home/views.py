"""Views for the home app"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.template import loader
from django.urls import reverse
from django.views.decorators.cache import cache_control
from ..utils.decorators import refresh_dualis


@login_required(login_url="/login/")
@refresh_dualis()
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request: HttpRequest) -> HttpResponse:
    """Index View

    Args:
        request (HttpRequest): HttpRequest Object

    Returns:
        HttpResponse: HttpResponde Object
    """
    context = {'segment': 'index', }

    return render(request, "home/index.html", context)


@login_required(login_url="/login/")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def pages(request: HttpRequest) -> HttpResponse:
    """Index View

    Args:
        request (HttpRequest): HttpRequest Object

    Returns:
        HttpResponse: HttpResponde Object
    """
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))
    except Exception:  # pylint: disable=broad-except # disable broad except warning, since all exception should be caught here
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
