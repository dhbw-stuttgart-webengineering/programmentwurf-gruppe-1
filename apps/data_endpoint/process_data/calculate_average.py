"""Modul for calculating the average of the grades"""
import os
import django
from django.db.models import Avg
from apps.data_endpoint.models import Grade, Unit, Module

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()


def calculate_average_module() -> None:
    """Function to calculate the average of the modules"""
    data = Module.objects.all()
    for result in data:
        # For each result in the data, get units of the modules
        units = Unit.objects.filter(id_of_module=result.module_id)
        for data_second in units:
            # For each unit in the units, get the average of the first and second attempt
            average_first = data_second.average_first_attempt
            average_second = data_second.average_second_attempt
            try:
                # Try to calculate the average of the first and second attempt,
                # to get the average of the module"""
                sum_of_average = (average_first + average_second)/2
            except TypeError:
                sum_of_average = average_first

            result.average = sum_of_average
            result.save()


def calculate_average_first_attempt() -> None:
    """Function to calculate the average of the first attempt"""
    data = Unit.objects.all()
    for result in data:
        # For each result in the data, get the average of the first attempt
        average = Grade.objects.filter(id_of_unit=result.unit_id).aggregate(
            average_first_attempt=Avg('grade_first_attempt'))
        result.average_first_attempt = average["average_first_attempt"]
        result.save()


def calculate_average_second_attempt() -> None:
    """Function to calculate the average of the second attempt"""
    data = Unit.objects.all()
    for result in data:
        # For each result in the data, get the average of the second attempt
        average = Grade.objects.filter(id_of_unit=result.unit_id).aggregate(
            average_second_attempt=Avg('grade_second_attempt'))
        result.average_second_attempt = average["average_second_attempt"]
        result.save()


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
