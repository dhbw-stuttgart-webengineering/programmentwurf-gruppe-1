"""Test Module"""
from django.test import TestCase
from .models import Module, Unit, Grade
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


class ModuleTestCase(TestCase):
    """Test case for the Module model"""
    def setUp(self):
        """Create test data"""
        Module.objects.create(module_id="123456789",
                              module_abk="Test",
                              module_name="Test",
                              semester="Test",
                              credits="Test",
                              average=0)

    def test_model_saves_correctly(self):
        """Test if the model saves correctly"""
        obj = Module.objects.get(module_id="123456789")

        #Test if the database contains the expected values
        self.assertEqual(obj.module_id, '123456789')
        self.assertEqual(obj.module_abk, 'Test')
        self.assertEqual(obj.module_name, 'Test')
        self.assertEqual(obj.semester, 'Test')
        self.assertEqual(obj.credits, 'Test')
        self.assertEqual(obj.average, 0)


    def test_model_updates_correctly(self):
        """Test if the model updates correctly"""
        obj = Module.objects.get(module_id="123456789")

        #Change a value
        obj.module_abk = 'changed'
        obj.save()

        #Get the updated object from the database
        updated_obj = Module.objects.get(module_id="123456789")

        #Test if the value has been updated
        self.assertEqual(updated_obj.module_abk, 'changed')

    def tearDown(self):
        """Delete test data"""
        Module.objects.all().delete()

class UnitTestCase(TestCase):
    """Test case for the Unit model"""
    def setUp(self):
        """Create test data"""
        Unit.objects.create(unit_id="123456789",
                            unit_name="Test",
                            credits="Test",
                            average_first_attempt=0,
                            average_second_attempt=0)

    def test_model_saves_correctly(self):
        """Test if the model saves correctly"""
        obj = Unit.objects.get(unit_id="123456789")

        #Test if the database contains the expected values
        self.assertEqual(obj.unit_id, '123456789')
        self.assertEqual(obj.unit_name, 'Test')
        self.assertEqual(obj.credits, 'Test')
        self.assertEqual(obj.average_first_attempt, 0)
        self.assertEqual(obj.average_second_attempt, 0)

    def test_model_updates_correctly(self):
        """Test if the model updates correctly"""
        obj = Unit.objects.get(unit_id="123456789")

        #Change a value
        obj.unit_name = 'changed'
        obj.save()

        #Get the updated object from the database
        updated_obj = Unit.objects.get(unit_id="123456789")

        #Test if the value has been updated
        self.assertEqual(updated_obj.unit_name, 'changed')

    def tearDown(self):
        """Delete test data"""
        Unit.objects.all().delete()

class GradeTestCase(TestCase):
    """Test case for the Grade model"""
    mail = "test@mail.com"
    def setUp(self):
        """Create test data"""
        Grade.objects.create(email_id=GradeTestCase.mail,
                             grade_first_attempt=0,
                             grade_second_attempt=0)

    def test_model_saves_correctly(self):
        """Test if the model saves correctly"""
        obj = Grade.objects.get(email_id=GradeTestCase.mail)

        self.assertEqual(obj.email_id, GradeTestCase.mail)
        self.assertEqual(obj.grade_first_attempt, 0)
        self.assertEqual(obj.grade_second_attempt, 0)

    def test_model_updates_correctly(self):
        """Test if the model updates correctly"""
        obj = Grade.objects.get(email_id=GradeTestCase.mail)

        #Change a value
        obj.grade_first_attempt = 1
        obj.save()

        updated_obj = Grade.objects.get(email_id=GradeTestCase.mail)

        #Test if the value has been updated
        self.assertEqual(updated_obj.grade_first_attempt, 1)

    def tearDown(self):
        """Delete test data"""
        Grade.objects.all().delete()
