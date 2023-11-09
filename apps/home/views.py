from django import template
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views.decorators.cache import cache_control
from datetime import timedelta
from ..utils.decorators import refresh_dualis


@login_required(login_url="/login/")
@refresh_dualis()
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    context = {'segment': 'index', }

    return render(request, "home/index.html", context)


@login_required(login_url="/login/")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except Exception:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
    
def own_grades_view(request):
    own_grades = [
        {'course': 'Mathematik', 'grade': 2.7},
        {'course': 'Englisch', 'grade': 1.9},
        {'course': 'Geschichte', 'grade': 3.3},
        # ...
    ]

    context = {'own_grades': own_grades}
    return render(request, 'home/index.html', context)
