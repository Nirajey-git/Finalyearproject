from django.db import models
from django.urls import reverse
from accounts.models import User

departments=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]

venue = [('Itahari','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]



    
class Appointment(models.Model):
    progress_state = [("Pending", "Pending"), ("In Progress", "In Progress"),
                      ("Waiting for receiver", "Waiting for receiver"), ("Delivered", "Delivered")]

    appointment_date = models.DateField(auto_now_add=False,null=True,blank=True)
    appointment_time = models.TimeField(auto_now=False, auto_now_add=False,null=True,blank=True)
    appointment_time_end = models.TimeField(auto_now=False, auto_now_add=False,null=True,blank=True)
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointment_patient')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointment_doctor')
    description = models.TextField(null=True,blank=True)
    payment = models.CharField(max_length=100,null=True,blank=True)
    status = models.CharField(max_length=100,choices=progress_state,default="Pending",null=True,blank=True)
    receipt_url = models.URLField(max_length=500,null=True,blank=True)
    paid=models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse("Management_system:appointment_detail", kwargs={"id": self.id})
    



class AppointmentReport(models.Model):
    doctor = models.ForeignKey(User,null=True, on_delete=models.CASCADE, related_name='report_doctor')
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_report')
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    category = models.CharField(max_length=40)
    reportinfo = models.CharField(max_length=50,null=True,blank=True)
    summary = models.TextField(null=True,blank=True)
    date_created = models.DateTimeField(null=True, auto_now_add=True)


class AppointmentFiles(models.Model):
    documents = models.FileField(upload_to='appointment_files')
    appoint =  models.ForeignKey(AppointmentReport ,on_delete=models.CASCADE )



class History(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_diseases')
    disease_name = models.CharField(max_length=40)
    medicine = models.CharField(max_length=40)
    last_checkup =  models.DateTimeField(auto_now=False,auto_now_add=False,null=True,blank=True)
    doctor_name = models.CharField(max_length=50,null=True,blank=True)
    description = models.TextField(null=True,blank=True)


class HistoryFiles(models.Model):
    documents = models.FileField(upload_to='history')
    history =  models.ForeignKey(History ,related_name="hisotry_files",on_delete=models.CASCADE )

    @property
    def filename(self):
        return self.documents.url.split('/')[-1]

class Invoice(models.Model):
    payment_mode_ = [
        ('CASH','CASH'),
        ('ESEWA','ESEWA'),
        ('KHALTI','KHALTI'),
        ('STRIPE','STRIPE')
    ]
    payment_status_=[("paid","paid"),("unpaid","unpaid")]
    title = models.CharField(max_length=100)
    patient =  models.ForeignKey(User ,related_name="invoices",on_delete=models.CASCADE )
    doctor =models.ForeignKey(User ,related_name="my_invoices",on_delete=models.CASCADE )
    price = models.IntegerField()
    date_created = models.DateTimeField(null=True, auto_now_add=True)
    payment_mode =  models.CharField(max_length=100,choices=payment_mode_,null=True,blank=True)
    payment_stats = models.CharField(max_length=100,choices=payment_status_,default="unpaid",null=True,blank=True)
    of_appointment = models.ForeignKey(Appointment ,on_delete=models.SET_NULL,null=True)