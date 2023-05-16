from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)

class Employee(models.Model):
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class Device(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    assigned_to = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    assigned_date = models.DateTimeField(null=True, blank=True)
    returned_date = models.DateTimeField(null=True, blank=True)
    condition = models.CharField(max_length=255, blank=True)
