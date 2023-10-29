from django.db import models

# Create your models here


class Courses(models.Model):
    name = models.CharField(max_length=200)
    bezeichnung = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Grades(models.Model):
    name = models.CharField(max_length=200)
    grade = models.IntegerField(default=0)
    courseName = models.ForeignKey(Courses, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
