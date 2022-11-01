from random import choices

from django.db import models

from general.models import Company, Worker, Specialization
from guest_serv.models import Guest
import time
import datetime


class Process(models.Model):
    STATUS = (
        ('1_Waiting', '1_Waiting'),
        ('2_In service', '2_In service'),
        ('3_Done', '3_Done'),
              )
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, blank=True, null=True, choices=STATUS)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    start_service = models.DateTimeField(auto_now_add=True)

    @property
    def time_in_service(self):
        return round((time.time() - self.start_service.timestamp()))


    @property
    def guest_id(self):
        return f' {--self.guest} '




