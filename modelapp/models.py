from django.db import models

# Create your models here.
class Course(models.Model):
    cname = models.CharField(max_length=30)
    tname = models.CharField(max_length=30)
    sdate = models.CharField(max_length=30)
    duration = models.CharField(max_length=30)
