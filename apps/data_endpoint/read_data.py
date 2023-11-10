import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()
from ..data_endpoint.models import Grade, Unit, Module

def get_grades(email_id):
    matching_id = Grade.objects.filter(email_id=email_id)
    grade_dict = {}
    grade_list = []

    for eintrag in matching_id:
        unit_id = Unit.objects.get(unit_id=eintrag.id_of_unit)
        module_id = Module.objects.get(module_id=unit_id.id_of_module)
        grade_dict["module_abk"] = module_id.module_abk
        grade_dict["module_name"] = module_id.module_name
        grade_dict["semester"] = module_id.semester
        grade_dict["module_credit"] = module_id.credits
        grade_dict["module_average"] = module_id.average

        grade_dict["unit_id"] = unit_id
        grade_dict["unit_name"] = unit_id.unit_name
        grade_dict["unit_credits"]= unit_id.credits
        grade_dict["average_first_attempt"]= unit_id.average_first_attempt
        grade_dict["average_second_attempt"]= unit_id.average_second_attempt

        grade_dict["grade_first_attempt"]= eintrag.grade_first_attempt
        grade_dict["note_zweitversuch"]= eintrag.grade_second_attempt

        for key, value in grade_dict.items():
            grade_list.append((key, value))

    return grade_list       #Die Noten aus der Datenbank werden in einem
                            #  Dictionary gespeichert und in einer Liste zurückgegeben"""