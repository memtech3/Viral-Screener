from django.contrib import admin
from .models import AlertMessage, HomeMessages, Employee, Visitor, EmployeeScreeningResponse, VisitorScreeningResponse
# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    ordering = ['LastName']
    search_fields = ['FirstName','MiddleName','LastName','EmployeeID']
    readonly_fields = ('id',)

class EmployeeScreeningAdmin(admin.ModelAdmin):
    autocomplete_fields = ("Employee",)

class VisitorScreeningAdmin(admin.ModelAdmin):
    autocomplete_fields = ("Visitor",)



admin.site.register(AlertMessage)
admin.site.register(HomeMessages)
admin.site.register(Employee, PersonAdmin)
admin.site.register(Visitor, PersonAdmin)
admin.site.register(EmployeeScreeningResponse, EmployeeScreeningAdmin)
admin.site.register(VisitorScreeningResponse, VisitorScreeningAdmin)