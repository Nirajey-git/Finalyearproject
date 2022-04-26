from django import forms
from accounts.models import User
from .models import Appointment, AppointmentReport, History, Invoice


sexGroup = [
    ("Male","Male"),
    ("Female","Female"),
    ("Other","Other")
]

bloodGroup = [
     ("A+","A+"),
     ("A-","A-"),
     ("B+","B+"),
     ("B-","B-"),
     ("O+","O+"),
     ("O-","O-"),
     ("AB+","AB+"),
     ("AB-","AB-"),
]



class AppointmentForm(forms.ModelForm):
    appointment_time = forms.CharField(widget=forms.TextInput(attrs={'type': 'time'}))
    appointment_date=forms.CharField(widget=forms.TextInput(attrs={'type': 'date'}))
    appointment_time_end=forms.CharField(widget=forms.TextInput(attrs={'type': 'time'}))
    description = forms.CharField(required=True,widget=forms.TextInput(attrs={'type': 'text','placeholder':'Little info about this appointment'}))

    class Meta:
        model = Appointment
        exclude=("doctor","patient")





class EditPatientForm(forms.ModelForm):
    sex = forms.ChoiceField(required=False,choices= sexGroup, widget=forms.Select)
    blood_group = forms.ChoiceField(required=False,choices= bloodGroup, widget=forms.Select)
    weight=forms.CharField(label="Weight (kg)",required=False)

    class Meta:
        model = User
        fields =("email","first_name","last_name","sex",
        "address","mobile","blood_group","state","weight"
        )


class EditDoctorForm(forms.ModelForm):
    title = forms.CharField(label="Title",required=False,widget=forms.TextInput(attrs={'type': 'text','placeholder':'(ex. Dr)'}))
    
    class Meta:
        model = User
        fields =("email","first_name","last_name","title","bio",
        "address","mobile","state","working_hospital","specialist","amount"
       
        )



class AppointmentReportForm(forms.ModelForm):

    class Meta:
        model = AppointmentReport
        exclude=("patient","doctor","date_created","appointment")




class HistoryForm(forms.ModelForm):
    last_checkup=forms.CharField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = History
        exclude=("patient",)



class AppointInvoiceForm(forms.ModelForm):

    class Meta:
        model = Invoice
        exclude=("patient","doctor","of_appointment")

class InvoiceForm(forms.ModelForm):

    class Meta:
        model = Invoice
        exclude=("doctor","of_appointment")