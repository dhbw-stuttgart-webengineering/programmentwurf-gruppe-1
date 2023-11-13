from django.test import TestCase
from .models import Grade
from .utils import get_failure_rate_first_attempt


class GradeTests(TestCase):

    def setUp(self):
        unit_1 = Unit.objects.create()
        unit_2 = Unit.objects.create()
        unit_3 = Unit.objects.create()

        Grade.objects.create(id_of_unit=unit_1, grade_first_attempt=1.0)

    def test_failure_rate_normal(self):
        self.assertEqual(0.5, get_failure_rate_first_attempt("T3INF1001.1"))

    def test_failure_rate_some_unassigned(self):
        self.assertEqual(0.5, get_failure_rate_first_attempt("T3INF1001.2"))

    def test_failure_rate_all_unassigned(self):
        self.assertEqual([], get_failure_rate_first_attempt("T3INF1001.3"))
