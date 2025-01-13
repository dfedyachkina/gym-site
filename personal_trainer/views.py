from django.shortcuts import render, redirect
from .forms import AppointmentForm
from .models import Appointment
from django.contrib.auth.decorators import login_required


@login_required
def create_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save() 
            return redirect('appointment_list')
    else:
        form = AppointmentForm()

    return render(request, 'personal_trainer/create_appointment.html', {'form': form})

def appointment_list(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'personal_trainer/appointment_list.html', {'appointments': appointments})