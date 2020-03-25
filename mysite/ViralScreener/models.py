from django.db import models

# Create your models here.
class AlertMessage(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200, choices=[('success', 'green'), ('primary', 'blue'), ('warning', 'yellow'), ('danger', 'red'),])
    content = models.TextField()
    dismissable = models.BooleanField()

    def __str__(self):
        return self.name

class Employee(models.Model):
    FirstName = models.CharField(max_length=200)
    MiddleName = models.CharField(max_length=200, blank=True)
    LastName = models.CharField(max_length=200)
    EmployeeID = models.CharField(max_length=200, blank=True)
    models.UniqueConstraint(fields=['FirstName', 'MiddleName', 'LastName'], name='unique_person')
    readonly_fields = ('id',)
    def __str__(self):
        return self.id