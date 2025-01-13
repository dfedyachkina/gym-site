from django.shortcuts import render, redirect
from .models import Appointment
from django.contrib.auth.models import User

def create_appointment(request):
    if request.method == 'POST':
        user = request.user  
        date = request.POST.get('date')
        time = request.POST.get('time')
        trainer_gender = request.POST.get('trainer_gender')
        is_member = request.POST.get('is_member') == 'on'
        notes = request.POST.get('notes')

        appointment = Appointment(
            user=user,
            date=date,
            time=time,
            trainer_gender=trainer_gender,
            is_member=is_member,
            notes=notes,
        )
        appointment.save()

        return redirect('appointment_list') 

    return render(request, 'personal_trainer/create_appointment.html')