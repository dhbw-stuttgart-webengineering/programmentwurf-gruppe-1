"""save the data from dualis in the database"""
import os
import django
from apps.data_endpoint.models import Grade, Unit, Module

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()


def save_data(email_id,
              id_module,
              module_number,
              designation,
              credits_,
              semester,
              unit):
    """save the data from dualis in the database"""

    module_to_save, created = Module.objects.get_or_create(module_id=id_module)
    """If the module is not in the database, it will be created"""
    if created:
        module_to_save.module_id = id_module
        module_to_save.module_abk = module_number
        module_to_save.module_name = designation
        module_to_save.semester = semester
        module_to_save.credits = credits_
        module_to_save.save()

    unit_to_save, created = Unit.objects.get_or_create(unit_id=unit["id"])
    """If the unit is not in the database, it will be created"""
    if created:
        unit_to_save.unit_id = unit["id"]
        unit_to_save.unit_name = unit["name"]
        unit_to_save.credits = unit["credits"]
        unit_to_save.id_of_module = module_to_save
        unit_to_save.save()

    """Create or update the grades of the student"""
    student_grades, _ = Grade.objects.get_or_create(email_id=email_id, id_of_unit=unit_to_save)
    student_grades.name = email_id
    student_grades.grade_first_attempt = unit["grade_first_attempt"]
    student_grades.grade_second_attempt = unit["grade_second_attempt"]
    student_grades.id_of_unit = unit_to_save
    student_grades.save()
