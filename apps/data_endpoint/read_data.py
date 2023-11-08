import os
import django
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()
from ..data_endpoint.models import Grades, Courses

def get_grades(email_id):
    matching_id = Grades.objects.filter(name=email_id)
    grade_dict = {}
    for eintrag in matching_id:
        kurs_id = Courses.objects.get(name=eintrag.course_name)
        grade_dict["kurs_id"] = kurs_id.bezeichnung
        grade_dict["scluessel_kurs"] = eintrag.course_name
        grade_dict["note_erstversuch"]= eintrag.grade_first
        grade_dict["note_zweitversuch"]= eintrag.grade_second
        grade_dict["semester"]= eintrag.semester
        grade_dict["summe_creditpoints"]= eintrag.sum_of_credits
        grade_dict["teil_creditpoints"]= eintrag.partial_credits
        print("data")

    return grade_dict       #Die Noten aus der Datenbank werden in ein
                            # Dictionary gespeichert und zurückgegeben