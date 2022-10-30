from django.db import models
from datetime import datetime

from django.db.models.fields import related

from general.models import Company, Specialization


class Guest(models.Model):
    name = models.CharField(max_length=80, verbose_name='Yore Name')
    time_register = models.DateTimeField(auto_now_add=True, verbose_name='Time Register_in_queue')
    company = models.ManyToManyField(Company)
    service = models.ManyToManyField(Specialization)


    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f'{self.name}-{self.time_register}-{self.service}'
