from django.contrib import admin
from .models import Appointment

#admin.site.register(Appointment)
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer_name', 'phone']
