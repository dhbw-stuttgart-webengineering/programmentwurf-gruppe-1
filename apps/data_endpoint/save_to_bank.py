import os
import django
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()
from ..data_endpoint.models import Grades, Courses

def save_dates(unit_id, unit_name, sum_unit_credits, part_unit_credits, unit_grade_first_attempt, unit_grade_second_attempt,semester, name):

    course_to_save, created = Courses.objects.get_or_create(name=unit_id)

    if created:
        course_to_save.bezeichnung = unit_name
        course_to_save.save()

    student_grades, create = Grades.objects.get_or_create(name=name, course_name=course_to_save)
    student_grades.name = name
    student_grades.grade_first = unit_grade_first_attempt
    student_grades.grade_second = unit_grade_second_attempt
    student_grades.semester = semester
    student_grades.sum_of_credits = sum_unit_credits
    student_grades.partial_credits = part_unit_credits
    student_grades.course_name = course_to_save
    student_grades.save()