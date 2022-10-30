from django.db import models

from general.models import Company, Specialization
from guest_serv.models import Guest
from datetime import datetime


class Worker(models.Model):
    name = models.CharField(max_length=80, verbose_name='Employee Name')
    company = models.ForeignKey(Company, related_name='Company', on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization, related_name='Specialization', on_delete=models.CASCADE)
    time_start_shift = models.DateTimeField(auto_now_add=True)
    time_end_shift = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f'{self.name}:{self.company}:{self.specialization}'


class Open_to_guest(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f'{self.guest}-{self.time}'


class Close_current_guest(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f'{self.guest}-{self.time}'

    @staticmethod
    def get_time_service(guest: Guest):
        return f'(time in queue)-{datetime.now()-Guest.time_register}'