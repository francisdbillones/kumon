from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=20, null=False, blank=False, default="")
    last_name = models.CharField(max_length=20, null=False, blank=False, default="")
    age = models.PositiveIntegerField()
