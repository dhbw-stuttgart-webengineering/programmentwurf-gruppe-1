"""Module to read the data from the database"""
import os
import django
from ..data_endpoint.models import Grade, Unit, Module

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()


def get_grades(email_id):
    """get the grades from the database"""
    matching_id = Grade.objects.filter(email_id=email_id)
    grade_list = []

    for eintrag in matching_id:
        unit_id = Unit.objects.get(unit_id=eintrag.id_of_unit)
        module_id = Module.objects.get(module_id=unit_id.id_of_module)
        try:
            average_first= float(unit_id.average_first_attempt)
        except TypeError:
            average_first = unit_id.average_first_attempt

        try:
            average_second = float(unit_id.average_second_attempt)
        except TypeError:
            average_second = unit_id.average_second_attempt

        try:
            grade_first = float(eintrag.grade_first_attempt)
        except TypeError:
            grade_first = eintrag.grade_first_attempt

        try:
            grade_second = float(eintrag.grade_second_attempt)
        except TypeError:
            grade_second = eintrag.grade_second_attempt

        try:
            module_average = float(module_id.average)
        except TypeError:
            module_average = module_id.average

        grade_dict =\
            {"module_abk" : module_id.module_abk,
             "module_name" : module_id.module_name,
             "semester" : module_id.semester,
             "module_credit" : module_id.credits,
             "module_average" : module_average,
             "unit_id" : unit_id,
             "unit_name" : unit_id.unit_name,
             "unit_credits" : unit_id.credits,
             "average_first_attempt" : average_first,
             "average_second_attempt" : average_second,
             "grade_first_attempt" : grade_first,
             "grade_second_attempt" : grade_second
            }
        grade_list.append(grade_dict)

    print(grade_list)
    return grade_list       #Die Noten aus der Datenbank werden in einem
                    #  Dictionary gespeichert und in einer Liste zurückgegeben"""
def get_module():
    """function to get the modules from the database"""
    module_list = []
    module_id = Module.objects.all()

    for eintrag in module_id:
        try:
            average = float(eintrag.average)
        except TypeError:
            average = eintrag.average

        module_dict =\
            {"module_abk" : eintrag.module_abk,
             "module_name" : eintrag.module_name,
             "semester" : eintrag.semester,
             "module_credit" : eintrag.credits,
             "module_average" : average
            }
        module_list.append(module_dict)


    return module_list       #Die Module aus der Datenbank werden in einem
                            #  Dictionary gespeichert und in einer Liste zurückgegeben"""
