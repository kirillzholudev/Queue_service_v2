from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    name = models.CharField(max_length=80, verbose_name='Company name')
    adress = models.CharField(max_length=100, verbose_name='Company adress')

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f'{self.name}'


class Specialization(models.Model):
    title = models.CharField(max_length=80, verbose_name='Specialization')
    description = models.TextField(max_length=100)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f'{self.title}'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ManyToManyField(Company)
    product_name = models.ManyToManyField(Specialization)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f'{self.user} -- {self.company} -- {self.product_name}'

