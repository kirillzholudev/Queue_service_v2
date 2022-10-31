from random import choices
from time import time

from django.db import models
from datetime import datetime

from django.db.models.fields import related

from general.models import Company, Specialization


class Guest(models.Model):
    phone = models.IntegerField(null=True, blank=True)
    time_register = models.DateTimeField(auto_now_add=True, verbose_name='Time Register_in_queue')
    company = models.ManyToManyField(Company)
    service = models.ManyToManyField(Specialization)
    time_now = datetime.now().time()


    def __str__(self):
        return f'{self.phone}--{self.time_register.time()}'

