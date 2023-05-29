from django.db import models
from accounts.models import *


class ExamCenter(models.Model):
    cname = models.CharField(max_length=250)
    city = models.CharField(max_length=250)


class Students(ExamCenter):
    name = models.CharField(max_length=200)
    roll = models.CharField(max_length=200)
    group = models.CharField(max_length=200)

    def __str__(self):
        return self.name
