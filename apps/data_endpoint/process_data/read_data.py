"""Module to read the data from the database"""
import os
import django
from apps.data_endpoint.models import Grade, Unit, Module

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()


def get_grades(email_id):
    """get the grades from the database"""
    matching_id = Grade.objects.filter(email_id=email_id)
    grade_list = []
    proof_existing = False
    index_of_element = 0
    grade_dict = {}

    for entry in matching_id:
        unit_id = Unit.objects.get(unit_id=entry.id_of_unit)
        module_id = Module.objects.get(module_id=unit_id.id_of_module)

        for list_entry in grade_list:
            """Check if the module is already in the list"""
            if list_entry["module_id"] == str(module_id):
                proof_existing = True
                index_of_element = grade_list.index(list_entry)
            else:
                proof_existing = False

        """Is the module already in the list, add the unit to the module"""
        if proof_existing:
            module_dict = \
                {"unit_name" : unit_id.unit_name,
                 "unit_credits" : unit_id.credits,
                 "average_first_attempt" : float(unit_id.average_first_attempt) \
                     if unit_id.average_first_attempt else None,
                 "average_second_attempt" : float(unit_id.average_second_attempt) \
                     if unit_id.average_second_attempt else None,
                 "grade_first_attempt" : float(entry.grade_first_attempt) \
                     if entry.grade_first_attempt else None,
                 "grade_second_attempt" : float(entry.grade_second_attempt) \
                     if entry.grade_second_attempt else None
                 }
            grade_list[index_of_element]["units"].append(module_dict)

            """If the module is not in the list, add it to the list"""
        else:
            unit = \
                {"unit_name" : unit_id.unit_name,
                 "unit_credits" : unit_id.credits,
                 "average_first_attempt" : float(unit_id.average_first_attempt) \
                     if unit_id.average_first_attempt else None,
                 "average_second_attempt" : float(unit_id.average_second_attempt) \
                     if unit_id.average_second_attempt else None,
                 "grade_first_attempt" : float(entry.grade_first_attempt) \
                     if entry.grade_first_attempt else None,
                 "grade_second_attempt" : float(entry.grade_second_attempt) \
                     if entry.grade_second_attempt else None
                 }
            grade_dict = \
                {"module_id" : module_id.module_id,
                 "module_abk" : module_id.module_abk,
                 "module_name" : module_id.module_name,
                 "semester" : module_id.semester,
                 "module_credit" : module_id.credits,
                 "module_average" : float(module_id.average) if module_id.average else None,
                 "units" : [unit]
                 }
        """Append the dictionary to the list"""
        grade_list.append(grade_dict)
    return grade_list
"""The grades from the database are stored in a dictionary and returned in a list"""
def get_module():
    """function to get the modules from the database"""
    module_list = []
    module_id = Module.objects.all()

    for entry in module_id:
        """Get each module from the database and save it in a dictionary"""
        try:
            """The average is not a float, so it must be converted"""
            average = float(entry.average)
        except TypeError:
            average = entry.average

        module_dict = \
            {"module_abk" : entry.module_abk,
             "module_name" : entry.module_name,
             "semester" : entry.semester,
             "module_credit" : entry.credits,
             "module_average" : average
             }
        """Append the dictionary to the list"""
        module_list.append(module_dict)


    return module_list
"""The modules from the database are stored in a dictionary and returned in a list"""
