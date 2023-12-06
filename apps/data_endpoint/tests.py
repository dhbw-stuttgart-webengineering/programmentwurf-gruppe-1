"""Test Module"""
from django.test import TestCase
from .models import Grade, Unit
from .utils import get_failure_rate_first_attempt


class GradeTests(TestCase):
    """Grade Tests"""

    def setUp(self):
        """Setup for the tests"""
        unit_1 = Unit.objects.create(unit_id="First")
        unit_2 = Unit.objects.create(unit_id="Second")
        unit_3 = Unit.objects.create(unit_id="Third")

        values_1 = [1.0, 2.0, 3.0, 4.0, 5.0]
        values_2 = [1.0, 2.0, 5.0, None, None]
        values_3 = [None, None, None, None, None]

        for unit, values in zip([unit_1, unit_2, unit_3], [values_1, values_2, values_3]):
            for value in values:
                Grade.objects.create(
                    id_of_unit=unit, grade_first_attempt=value)

    def test_failure_rate_normal(self):
        """Test failure rate with normal values"""
        self.assertEqual(0.2, get_failure_rate_first_attempt("First"))

    def test_failure_rate_some_unassigned(self):
        """Test failure rate with some unassigned values"""
        self.assertEqual(1/3, get_failure_rate_first_attempt("Second"))

    def test_failure_rate_all_unassigned(self):
        """Test failure rate with all unassigned values"""
        self.assertEqual(0, get_failure_rate_first_attempt("Third"))
