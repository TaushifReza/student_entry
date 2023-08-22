from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    address = models.CharField(max_length=50)
    grade = models.CharField(max_length=10)
    major = models.CharField(max_length=50)
