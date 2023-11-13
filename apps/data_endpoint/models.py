"""Database models for the data_endpoint app"""
from django.db import models


class Module(models.Model):
    """Class for the modules"""
    objects = models.Manager()
    module_id = models.CharField(primary_key=True, max_length=200)
    module_abk = models.CharField(max_length=200, default=None, null=True)
    module_name = models.CharField(max_length=200, default=None, null=True)
    semester = models.CharField(max_length=200, default=None, null=True)
    credits = models.CharField(max_length=200, default=None, null=True)
    average = models.DecimalField(max_digits=2, decimal_places=1,default=0, null=True)

    def __str__(self):
        """Function to return the module_id"""
        return str(self.module_id)

class Unit(models.Model):
    """Class for the units"""
    objects = models.Manager()
    unit_id = models.CharField(primary_key=True, max_length=200)
    unit_name = models.CharField(max_length=200, default=None, null=True)
    credits = models.CharField(max_length=200,
                               default=None,
                               null=True)
    average_first_attempt = models.DecimalField(max_digits=2,
                                                decimal_places=1,
                                                default=0,
                                                null=True)
    average_second_attempt = models.DecimalField(max_digits=2,
                                                 decimal_places=1,
                                                 default=0,
                                                 null=True)
    id_of_module = models.ForeignKey(Module, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        """Function to return the unit_id"""
        return str(self.unit_id)

class Grade(models.Model):
    """Class for the grades"""
    objects = models.Manager()
    email_id = models.CharField(max_length=200)
    id_of_unit = models.ForeignKey(Unit, null=True, default=None, on_delete=models.CASCADE)
    grade_first_attempt = models.DecimalField(max_digits=2, decimal_places=1,default=0, null=True)
    grade_second_attempt = models.DecimalField(max_digits=2, decimal_places=1,default=0, null=True)

    def __str__(self):
        """Function to return the email_id"""
        return str(self.email_id)
