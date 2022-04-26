from django.contrib import admin
from .models import  Appointment,History,HistoryFiles,Invoice

@admin.register(Appointment)
class Appointment(admin.ModelAdmin):
    list_display = ('patient','appointment_date', 'appointment_time', 'doctor')

@admin.register(Invoice)
class Appointment(admin.ModelAdmin):
    list_display = ('id','patient','doctor', 'title', 'price','payment_mode','payment_stats')

@admin.register(History)
class Appointment(admin.ModelAdmin):
    list_display = ('id','patient','doctor_name',  'disease_name','medicine','last_checkup')


admin.site.register(HistoryFiles)
