from django.db import models
from django.conf import settings


class Student(models.Model):
    roll_no = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    age = models.IntegerField(blank=True, null=True)
    standard = models.CharField(max_length=10,default='0')