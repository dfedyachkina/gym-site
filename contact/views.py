from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import GymContacts


def contact(request):
    gym_contact = GymContacts.objects.first()

    if gym_contact is None:
        messages.error(request, "Gym contact information is not available.")
        return redirect('home')

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been submitted successfully!")  # noqa
            return redirect('contact')
        else:
            messages.error(request, "Error, please try again")
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {
        'form': form,
        'gym_email': gym_contact.email,
        'gym_phone_number': gym_contact.phone_number
    })
