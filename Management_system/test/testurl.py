from os import remove
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Management_system.views import appointment_detail, createRate, patient_settings, appointment_form, doctor_profile, doctor_list, Patient_dashboard 
from doctor.views import doctor_settings, billing, invoice_detail, create_invoice, UserHistory, search1
class TestUrls(SimpleTestCase):

    def test_appointment_url_resolves(self):
        url = reverse('Management_system:appointment_detail', args=['1'])
        self.assertEquals(resolve(url).func, appointment_detail )

    def test_createrate_url_resolves(self):
        url = reverse('Management_system:create_rate')
        self.assertEquals(resolve(url).func, createRate )

    def test_patient_settings_url_resolves(self):
        url = reverse('Management_system:patient-settings', args=['1'])
        self.assertEquals(resolve(url).func, patient_settings )

    def test_appointment_form_url_resolves(self):
        url = reverse('Management_system:appointment-form', args=['1'])
        self.assertEquals(resolve(url).func,appointment_form )

    def test_doctor_profile_url_resolves(self):
        url = reverse('Management_system:doctor-profile', args=['1'])
        self.assertEquals(resolve(url).func,doctor_profile )

    def test_doctor_list_url_resolves(self):
        url = reverse('Management_system:doctor-list')
        self.assertEquals(resolve(url).func, doctor_list )

    def test_Patient_dashboard_url_resolves(self):
        url = reverse('Management_system:patientdashboard')
        self.assertEquals(resolve(url).func, Patient_dashboard )

    def test_doctor_settings_url_resolves(self):
        url = reverse('doctor:doctor-settings', args=['1'])
        self.assertEquals(resolve(url).func, doctor_settings )

    def test_billing_url_resolves(self):
        url = reverse('doctor:billing-list')
        self.assertEquals(resolve(url).func, billing )

    def test_invoice_detail_url_resolves(self):
        url = reverse('doctor:invoice_detail', args=['1'])
        self.assertEquals(resolve(url).func, invoice_detail )

    def test_create_invoice_url_resolves(self):
        url = reverse('doctor:create-invoice')
        self.assertEquals(resolve(url).func, create_invoice )

    def test_user_history_url_resolves(self):
        url = reverse('doctor:user_history', args=['1'])
        self.assertEquals(resolve(url).func, UserHistory )

    def test_search1_url_resolves(self):
        url = reverse('doctor:searchpatient')
        self.assertEquals(resolve(url).func, search1 )