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
        #For each result in the data, get units of the modules
        units = Unit.objects.filter(id_of_module=result.module_id)
        for data_second in units:
            #For each unit in the units, get the average of the first and second attempt
            average_first = data_second.average_first_attempt
            average_second = data_second.average_second_attempt
            try:
                #Try to calculate the average of the first and second attempt,
                #to get the average of the module"""
                sum_of_average= (average_first + average_second)/2
            except TypeError:
                sum_of_average = average_first

            result.average = sum_of_average
            result.save()

def calculate_average_first_attempt() -> None:
    """Function to calculate the average of the first attempt"""
    data = Unit.objects.all()
    for result in data:
        #For each result in the data, get the average of the first attempt
        average = Grade.objects.filter(id_of_unit=result.unit_id).aggregate(
            average_first_attempt=Avg('grade_first_attempt'))
        result.average_first_attempt = average["average_first_attempt"]
        result.save()

def calculate_average_second_attempt() -> None:
    """Function to calculate the average of the second attempt"""
    data = Unit.objects.all()
    for result in data:
        #For each result in the data, get the average of the second attempt
        average = Grade.objects.filter(id_of_unit=result.unit_id).aggregate(
            average_second_attempt=Avg('grade_second_attempt'))
        result.average_second_attempt = average["average_second_attempt"]
        result.save()
