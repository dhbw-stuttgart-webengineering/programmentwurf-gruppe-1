"""Module for calculating grade distribution"""
from collections import Counter
from typing import List
from ..models import Grade


def get_grade_distribution(unit_id: str) -> List[float]:
    """Returns grade distribution for a given Unit as List

    Args:
        unit_id (str): Unit ID

    Returns:
        List[float]: List of grades
    """

    grades = Grade.objects.filter(id_of_unit=unit_id)

    return [float(grade.grade_first_attempt) for grade in grades]


def get_grade_distribution_as_dict(unit_id: str) -> dict:
    """Returns grade distribution for a given Unit as dict

    Args:
        unit_id (str): Unit ID

    Returns:
        dict: Dictionary of grades (key: grade, value: count)
    """

    distribution = get_grade_distribution(unit_id)

    return dict(Counter(distribution))
