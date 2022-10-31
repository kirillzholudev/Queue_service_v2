from django.db import models
from django.contrib.auth.models import User


class Specialization(models.Model):
    name = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=80)
    adres = models.CharField(max_length=100, null=True)
    specialization = models.ManyToManyField(Specialization)

    def __str__(self):
        return f'{self.name}--'


class Worker(models.Model):
    name = models.CharField(max_length=50, null=True)
    specialization = models.ManyToManyField(Specialization)
    start_shift = models.TimeField(auto_now_add=False)
    finish_shift = models.TimeField(auto_now_add=False)

    def __str__(self):
        return f'{self.name} {self.start_shift} {self.finish_shift}'
