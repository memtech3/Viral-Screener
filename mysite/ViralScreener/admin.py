from django.contrib import admin
from .models import AlertMessage, Employee, Visitor, HomeMessages
# Register your models here.
admin.site.register(AlertMessage)
admin.site.register(Employee)
admin.site.register(Visitor)
admin.site.register(HomeMessages)