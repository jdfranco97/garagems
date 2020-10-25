from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Client, Vehicle, ServiceRecord

class ServiceRecordInLine(admin.TabularInline):
    model = ServiceRecord

class VehicleInLine(admin.TabularInline):
    model = Vehicle

class VehicleAdmin(admin.ModelAdmin):
    inlines = [
        ServiceRecordInLine
    ]

class ClientAdmin(admin.ModelAdmin):
    inlines = [
        VehicleInLine,
    ]


admin.site.register(Client, ClientAdmin)
admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(ServiceRecord)

