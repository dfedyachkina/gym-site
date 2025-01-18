from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Membership, MembershipRequest

def membership(request):
    memberships = Membership.objects.all()
    return render(request, 'membership/membership.html', {'memberships': memberships})


def request_membership(request, membership_id):
    try:
        membership = Membership.objects.get(id=membership_id)
    except Membership.DoesNotExist:
        return redirect('membership')

    membership_request = MembershipRequest.objects.create(
        user=request.user,
        membership=membership
    )
    
    return redirect('membership_success')

def membership_success(request):
    return render(request, 'membership/membership_success.html')