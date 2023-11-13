"""Modul for calculating the average of the grades"""
import os
import django
from django.db.models import Avg
from ..data_endpoint.models import Grade, Unit, Module

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()


def calculate_average_module():
    """Function to calculate the average of the modules"""
    daten = Module.objects.all()
    for ergebnis in daten:
        unit_first_grade = Unit.objects.filter(id_of_module=ergebnis.module_id)
        for data_second in unit_first_grade:
            durchschnitt_first = data_second.average_first_attempt
            durchschnitt_second = data_second.average_second_attempt
            try:
                sum_of_average = (durchschnitt_first + durchschnitt_second)/2
            except TypeError:
                sum_of_average = durchschnitt_first

            ergebnis.average = sum_of_average
            ergebnis.save()


def calculate_average_first_attempt():
    """Function to calculate the average of the first attempt"""
    daten = Unit.objects.all()
    for ergebnis in daten:
        durchschnitt = Grade.objects.filter(id_of_unit=ergebnis.unit_id).aggregate(
            average_first_attempt=Avg('grade_first_attempt'))
        ergebnis.average_first_attempt = durchschnitt["average_first_attempt"]
        ergebnis.save()


def calculate_average_second_attempt():
    """Function to calculate the average of the second attempt"""
    daten = Unit.objects.all()
    for ergebnis in daten:
        durchschnitt = Grade.objects.filter(id_of_unit=ergebnis.unit_id).aggregate(
            average_second_attempt=Avg('grade_second_attempt'))
        ergebnis.average_second_attempt = durchschnitt["average_second_attempt"]
        ergebnis.save()


def calculate_total_average_weighted(email: str) -> float:
    """Function to calculate the total average weighted

    Args:
        email (str): Students Email

    Returns:
        float: Total average weighted
    """
    grades = Grade.objects.filter(email_id=email)

    total_grades = 0.0
    total_credits = 0

    for grade in grades:
        unit = Unit.objects.get(unit_id=grade.id_of_unit)

        if "T3_1000" in str(unit.unit_id):
            continue

        if grade.grade_first_attempt is None:
            continue

        if grade.grade_second_attempt:
            total_grades += (float(grade.grade_second_attempt)
                             * float(unit.credits))
        else:
            total_grades += (float(grade.grade_first_attempt)
                             * float(unit.credits))
        total_credits += float(unit.credits)
    return total_grades / total_credits


def calculate_total_average(email: str) -> float:
    """Function to calculate the total average

    Args:
        email (str): Students Email

    Returns:
        float: Total average
    """
    grades = Grade.objects.filter(email_id=email)

    total_grades = 0.0
    n_grades = 0

    for grade in grades:
        unit = Unit.objects.get(unit_id=grade.id_of_unit)

        if "T3_1000" in str(unit.unit_id):
            continue

        if grade.grade_first_attempt is None:
            continue

        if grade.grade_second_attempt:
            total_grades += float(grade.grade_second_attempt)
        else:
            total_grades += float(grade.grade_first_attempt)
        n_grades += 1

    return total_grades / n_grades
