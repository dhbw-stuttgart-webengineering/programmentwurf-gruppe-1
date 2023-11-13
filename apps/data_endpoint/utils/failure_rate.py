"""Module to calculate failure and passing rate"""
from ..models import Grade


def get_failure_rate_first_attempt(unit_id: str) -> float:
    """Returns the failure rate for a given unit

    Args:
        unit_id (str): Unit ID

    Returns:
        float: Failure rate
    """
    grades = Grade.objects.filter(id_of_unit=unit_id)

    n_passed = 0
    n_failed = 0

    for grade in grades:
        if grade.grade_first_attempt:
            if float(grade.grade_first_attempt) >= 4.0:
                n_failed += 1
            else:
                n_passed += 1

    return float(n_failed) / (n_passed + n_failed)


def get_passing_rate_first_attempt(unit_id: str) -> float:
    """Returns the passing rate for a given unit

    Args:
        unit_id (str): Unit ID

    Returns:
        float: Passing rate
    """

    return 1 - get_failure_rate_first_attempt(unit_id)
