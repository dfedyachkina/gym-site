from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AppointmentForm
from .models import Appointment, Member


@login_required
def create_appointment(request):
    if not Member.objects.filter(user=request.user, approved=True).exists():
        messages.error(request, "You must be a member to make an appointment")
        is_member = False
    else:
        is_member = True
        if request.method == 'POST':
            form = AppointmentForm(request.POST)
            if form.is_valid():
                appointment = form.save(commit=False)
                appointment.user = request.user
                appointment.is_member = True
                appointment.save() 
                messages.success(request, "Your appointment has been done")
                return redirect('appointment_list')
    form = AppointmentForm()

    template = 'personal_trainer/create_appointment.html'
    context = {
        'form': form,
        'is_member': is_member,
    }
    return render(request, template, context)


@login_required
def update_appointment(request, id):
    appointment = get_object_or_404(Appointment, id=id) 
    if not request.user == appointment.user:
        messages.error(request, "Access denied, this appointment is not yours")
        return redirect('appointment_list')

    form = AppointmentForm(request.POST or None, instance=appointment)
    if request.method == 'POST':
        if form.is_valid():
            form.save() 
            messages.success(request, "Your appointment has been updated")
            return redirect('appointment_list')

    template = 'personal_trainer/update_appointment.html'
    context = {
        'form': form,
        'appointment': appointment 
    }
    return render(request, template, context)



def appointment_list(request):
    appointments = Appointment.objects.filter(user=request.user)
    return render(request, 'personal_trainer/appointment_list.html', {'appointments': appointments})