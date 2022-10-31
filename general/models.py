from django.db import models
from django.contrib.auth.models import User
import datetime
import time


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
    start_shift = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    finish_shift = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.start_shift} {self.finish_shift}'

    @property
    def current_time(self):
        return f"{self.__current_time} min"

    @property
    def __current_time(self):
        if self.finish_shift:
            return round((self.finish_shift.timestamp() - self.start_shift.timestamp())/60)
        return round((time.time() - self.start_shift.timestamp())/60)