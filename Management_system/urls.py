from django.urls import path
from . import views

app_name = "Management_system"

urlpatterns = [
 path('patientdashboard/', views.Patient_dashboard, name='patientdashboard'),
 path('doctor-list/', views.doctor_list, name='doctor-list'),
 path('create_rate/', views.createRate, name='create_rate'),
 path('add-medical-history/', views.add_medical_history, name='add-medical-history'),
 path('add-medical-history-json/', views.add_medical_history_json, name='add_medical_history_json'),
 path('view-medical-history/', views.view_medical_history, name='view-medical-history'),
 path('view-medical-history/<int:id>/', views.user_history_detail, name='user_history_details'),
 path('weekday_time_info/', views.weekday_time_info, name='weekday_time_info'),
 path('doctor-profile/<int:id>/', views.doctor_profile, name='doctor-profile'),
 path('appointment/', views.appointment, name='appointment'),
 path('appointment-form/<int:id>/', views.appointment_form, name='appointment-form'),
 path('patient-settings/<int:id>/', views.patient_settings, name='patient-settings'),
 path('search/', views.search, name='search'),

path('appointment_detail/<int:id>/', views.appointment_detail,name="appointment_detail"),
]

