from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.contrib import  messages
from accounts.decorators import allow_only_user
from accounts.models import MyRate, RatingModel, User, WeekDayAvailable
from .models import Appointment, AppointmentReport, History, HistoryFiles
from .forms import AppointInvoiceForm, AppointmentForm, AppointmentReportForm, EditPatientForm, HistoryForm
from django.core.exceptions import PermissionDenied
from django.db.models import F
from django.views.decorators.csrf import csrf_exempt 
from django.conf import settings
from django.db.models import Q
import datetime
import stripe
from django.db import transaction

@allow_only_user("patient")
def Patient_dashboard(request):
    doctors = User.objects.filter(is_doctor=True)
    context={"doctors":doctors}
    return render(request, 'patientdashboard.html',context)


@allow_only_user("patient")
def doctor_list(request):
    doctor = User.objects.filter(is_doctor=True)
    context = {'doctor': doctor}
    return render(request, 'doctor-list.html', context)


@allow_only_user("patient")
def doctor_profile(request, id):
    doctor = User.objects.get(id=id)
    has_rating = RatingModel.objects.filter(of_user=doctor).first()
    myrate = MyRate.objects.filter(of_user=doctor,by_user=request.user).first()

    rate=None
    avg_rating=0
    if myrate:
        rate = myrate.my_rate
    if has_rating:
        alls = doctor.all_rates.all()
        total_rating =0
        for i in alls:
            total_rating+=i.my_rate
        avg_rating=total_rating/alls.count() if total_rating != 0 else  0

    context = {'doctor': doctor,
            'has_rating':"True" if has_rating else "False",
            'rate':rate,'total_rating':avg_rating,"myrate":myrate}
    return render(request, 'doctor-profile.html', context)


@allow_only_user("patient")
def appointment(request):
    appointments = Appointment.objects.filter(patient=request.user)
    context={"appointments":appointments}
    return render(request, 'appointment.html',context)

@allow_only_user("patient")
def view_medical_history(request):
    histories = History.objects.filter(patient=request.user).order_by("-last_checkup")
    context={"histories":histories}
    return render(request, 'View-medical.html',context)

@allow_only_user("patient")
def user_history_detail(request,id):
    user =request.user
    
    history  =get_object_or_404(History,id=id)
    if not history.patient == request.user:
        return Http404
    files = history.hisotry_files.all()
    context={"history":history,'user':user,'files':files}
    return render(request, 'medical_detail.html',context)

@allow_only_user("patient")
def add_medical_history(request):
    form=HistoryForm()
    context={"form":form}
    return render(request, 'Add-medical.html',context)


def add_medical_history_json(request):
    if request.method == 'POST':
        data = request.POST
        h =History.objects.create(
                patient=request.user,
                disease_name=data.get("disease_name"),
                medicine=data.get("medicine"),
                last_checkup=data.get("last_checkup"),
                doctor_name=data.get("doctor_name"),
                description=data.get("description"),
                )
        if request.FILES.getlist('files'):
            files = request.FILES.getlist('files')
            for f in files:
                HistoryFiles.objects.create(history=h,documents=f)
        return JsonResponse({"added":True})
    return JsonResponse({"added":False})



@allow_only_user("patient")
def appointment_form(request,id):
    receipt=None
    doctor = User.objects.get(id=id)
    form = AppointmentForm()
    if request.method == 'POST':
        print(request.POST)
        payment = request.POST.get("radio2")
        form = AppointmentForm(request.POST)
        if not doctor.availability:
            messages.error(request,f"{doctor} is not available for appointment ")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
        
        if form.is_valid():
            try:
                with transaction.atomic():
                    fr =form.save(commit=False)
                    fr.patient=request.user
                    fr.doctor = doctor
                    
                    date = form.cleaned_data.get("appointment_date")
                    start = form.cleaned_data.get("appointment_time")
                    end = form.cleaned_data.get("appointment_time_end")

                    start_time = datetime.datetime.strptime(start, '%H:%M').time()
                    end_time = datetime.datetime.strptime(end, '%H:%M').time()
                    print(type(start_time),start_time)
                    same_day_appointments =Appointment.objects.filter(appointment_date=date,doctor=doctor)
                    for i in same_day_appointments:
                        print (i)
                        if start_time <= i.appointment_time_end and end_time >= i.appointment_time:
                            print('Found Overllapping boys ')
                            messages.error(request,f"Appointment time already reserved . ")
                            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

                    fr.save()
                    if payment == "cash":
                        fr.payment=payment
                        fr.save()
                    
                    stripe.api_key = settings.STRIPE_SECRET_KEY

                    
                    # if payment== "stripeToken":
                    customer = stripe.Customer.create(
                    email = request.user.email,
                    name=request.user.first_name,
                    source=request.POST['stripeToken']
                    )
                    
                    charge = stripe.Charge.create(
                        customer=customer,
                        amount=fr.doctor.amount*100 if fr.doctor.amount else 100*100,
                        currency='npr',
                        description="Appointment ",   
                    )

                    
                    if charge['paid'] == True:
                        fr.paid=True
                        fr.payment='stripe'
                        fr.receipt_url=charge['receipt_url']
                        fr.save()
                    else:
                        messages.error(request,f"Card Declined ")
                        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                    from django.core.mail import send_mail

                    send_mail(
                        'Appointment Created',
                        f'New Appointment has been created by {request.user} on {date} at {start} to {end}. Please check detail from website .',
                        settings.EMAIL_HOST_USER,
                        [doctor.email],
                        fail_silently=False,
                    )
                    send_mail(
                        'Appointment Created',
                        f'Your  Appointment has been created with {doctor} on {date} at {start} to {end}. Please check detail from website .',
                        settings.EMAIL_HOST_USER,
                        [request.user.email],
                        fail_silently=False,
                    )
                    
                    messages.success(request,f"Added Appointment with {doctor} ")
                    return redirect(fr.get_absolute_url())
            except Exception as ex:
                # print (ex)
                return redirect(':page-error-404.html') 
        else:
            messages.error(request,f"Error Adding Appointment with {doctor} ")
            print(form.errors)
    context = {'doctor': doctor,"form":form}
    return render(request, 'appointment-form.html',context)


def weekday_time_info(request):
    name = request.POST.get("name")
    user = User.objects.get(id=request.POST["id"])
    avail = WeekDayAvailable.objects.filter(name=name,user=user).first()
    return JsonResponse({
        "name":avail.name,
        "available_from":avail.available_from,
        "available_to" :avail.available_to
    })


@allow_only_user("patient")
def patient_settings(request,id):
    user = User.objects.filter(is_patient=True).get(id=id)
    form = EditPatientForm(instance=user)
    can_edit = request.user == user or request.user.is_staff 
 
    if request.method == 'POST':
        if can_edit:
            form = EditPatientForm(request.POST,instance=request.user)
            if form.is_valid():
                fr = form.save(commit=False)
                print(request.FILES)
                if request.FILES:
                    fr.profile_pic=request.FILES['propic']
                fr.save()
                messages.success(request,"Successfully edited your information ")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            
            raise PermissionDenied
    context={"form":form,"user":user,"can_edit":can_edit}
    return render(request, 'p_patient-settings.html',context)



def createRate(request):
    if request.method=="POST":
        data = request.POST
        doc_id = data.get("doc_id")
        rate = data.get("rate")
        doctor = get_object_or_404(User,id=doc_id)
        rate_model,_=RatingModel.objects.get_or_create(of_user=doctor)
        rate_model.rate =F('rate')+rate
        rate_model.save()

        my_rate,_ = MyRate.objects.get_or_create(of_user=doctor,
                        by_user=request.user
                        )
        my_rate.my_rate = rate
        my_rate.save()
        alls = doctor.all_rates.all()
        total_rating =0
        for i in alls:
            total_rating+=i.my_rate
        avg_rating=total_rating/alls.count() if total_rating != 0 else  0
        return JsonResponse(
            {"added_rating":True,
            "myrate":my_rate.my_rate,
            "avg_rating":avg_rating
            })






@allow_only_user("patient")
def appointment_detail(request,id):
    
    appointment = get_object_or_404(Appointment,id=id)
    report = AppointmentReport.objects.filter(appointment=appointment).first()
    form = AppointmentReportForm() if not report else  AppointmentReportForm(instance=report) 
    

    if "start_appointment" in request.POST:
        appointment.status = "In Progress"
        appointment.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


    context = {"appointment":appointment,"form":form}
    return render(request, 'app_detail.html',context)

def search(request):

    results = []

    if request.method == "GET":

        query = request.GET.get('search')

        if query == '':

            query = 'None'

        results = User.objects.filter(Q(specialist__icontains=query)| Q(first_name__icontains=query))

    return render(request, 'search.html', {'query': query, 'results': results})