from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Membership, MembershipRequest

def membership(request):
    memberships = Membership.objects.all()
    return render(request, 'membership/membership.html', {'memberships': memberships})


