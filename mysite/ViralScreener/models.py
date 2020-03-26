from django.db import models
from django.conf import settings

# Create your models here.
class AlertMessage(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200, choices=[('success', 'green'), ('primary', 'blue'), ('warning', 'yellow'), ('danger', 'red'),])
    content = models.TextField()
    dismissable = models.BooleanField()

    def __str__(self):
        return self.name

class HomeMessages(models.Model):
    name = models.CharField(max_length=200)
    header = models.CharField(max_length=200)
    content = models.TextField()

class Employee(models.Model):
    id = models.AutoField(primary_key=True),
    LastName = models.CharField(max_length=200)
    FirstName = models.CharField(max_length=200)
    MiddleName = models.CharField(max_length=200, blank=True)
    EmployeeID = models.CharField(max_length=200, blank=True)
    models.UniqueConstraint(fields=['FirstName', 'MiddleName', 'LastName'], name='unique_person')
    readonly_fields = ('id',)
    def __str__(self):
        return " ".join((self.LastName, self.FirstName, self.MiddleName))

class Visitor(models.Model):
    id = models.AutoField(primary_key=True),
    FirstName = models.CharField(max_length=200)
    MiddleName = models.CharField(max_length=200, blank=True)
    LastName = models.CharField(max_length=200)
    models.UniqueConstraint(fields=['FirstName', 'MiddleName', 'LastName'], name='unique_person')
    readonly_fields = ('id',)
    def __str__(self):
        return " ".join(('V'+str(self.id), self.FirstName, self.MiddleName, self.LastName))

class EmployeeScreeningResponses(models.Model):#waiting for questions to ask
    id = models.AutoField(primary_key=True),
    Screener = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Contact = models.CharField(max_length=200, choices=[('y', 'Yes'), ('n', 'No'), ('u', 'Unknown')])
    DateTime = models.DateTimeField #check in later to see if this is wrong
    def __str__(self):
        return ('R'+str(self.id))

#create visitor screening model