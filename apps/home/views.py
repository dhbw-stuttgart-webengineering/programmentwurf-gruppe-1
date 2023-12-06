"""Views for the home app"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, JsonResponse
from django.template import loader
from django.urls import reverse
from django.views.decorators.cache import cache_control
from django.conf import settings
from apps.data_endpoint.calculate_average import calculate_total_average_weighted
from apps.data_endpoint.utils.grade_distribution import get_grade_distribution_as_dict
from apps.data_endpoint.utils.failure_rate import get_failure_rate_first_attempt, get_passing_rate_first_attempt
from apps.data_endpoint.read_data import get_grades
from ..utils.decorators import refresh_dualis
import json


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

    own_grades = get_grades(request.user.email)

    # Entferne Duplikate basierend auf dem Modulnamen
    unique_modules = []
    for module in own_grades:
        module_name = module['module_name']
        
        # Überprüfe, ob das Modul bereits in unique_modules ist
        if not any(existing_module['module_name'] == module_name for existing_module in unique_modules):
            unique_modules.append(module)

    # Aktualisiere own_grades mit den eindeutigen Modulen
    own_grades = unique_modules
    total_average = calculate_total_average_weighted(request.user.email)
    for module in own_grades:
        for unit in module['units']:
            # Ersetze None-Werte durch 0
            for key in unit:
                if unit[key] is None:
                    unit[key] = 0
            # Append grade distribution
            unit['grade_distribution'] = get_grade_distribution_as_dict(unit['unit_id'])
            # Append failure rate
            unit['failure_rate'] = get_failure_rate_first_attempt(unit['unit_id'])
            # Append passing rate
            unit['passing_rate'] = get_passing_rate_first_attempt(unit['unit_id'])
    # Append total average
    own_grades.append({'total_average': total_average})
    print(json.dumps(own_grades,indent=4))
    context = {'own_grades': own_grades}
    return render(request, 'home/index.html', context)


def sitemap(_: HttpRequest) -> HttpResponse:
    """Sitemap View

    Args:
        request (HttpRequest): HttpRequest Object

    Returns:
        HttpResponse: HttpResponse Object
    """
    return HttpResponse(open(settings.STATIC_ROOT+"/sitemap.xml", encoding="utf-8").read(),
                        content_type='text/xml')


@login_required(login_url="/login/")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def pages(request: HttpRequest) -> HttpResponse:
    """Index View

    Args:
        request (HttpRequest): HttpRequest Object

    Returns:
        HttpResponse: HttpResponse Object
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
        html_template = loader.get_template(
            'home/page-404.html')  # Should be 500
        return HttpResponse(html_template.render(context, request))
