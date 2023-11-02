from django.db import models
2


class Courses(models.Model):
    name = models.CharField(max_length=200)
    bezeichnung = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Grades(models.Model):
    name = models.CharField(max_length=200, default=None)
    grade_first = models.IntegerField(default=0, null=True)
    grade_second = models.IntegerField(default=0, null=True)
    semester = models.CharField(max_length=200, default=None, null=True)
    sum_of_credits = models.CharField(max_length=200, default=None, null=True)
    partial_credits = models.CharField(max_length=200, default=None, null=True)
    course_name = models.ForeignKey(Courses, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
