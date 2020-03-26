from django.contrib import admin
from .models import AlertMessage, HomeMessages, Employee, Visitor, EmployeeScreeningResponses
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    ordering = ['LastName']
    search_fields = ['FirstName','MiddleName','LastName','EmployeeID']
    readonly_fields = ('id',)

class EmployeeScreeningResponsesAdmin(admin.ModelAdmin):
    autocomplete_fields = ("Employee",)


admin.site.register(AlertMessage)
admin.site.register(HomeMessages)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Visitor)
admin.site.register(EmployeeScreeningResponses, EmployeeScreeningResponsesAdmin)