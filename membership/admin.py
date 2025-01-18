from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Membership, Benefit, MembershipRequest


class MembershipAdmin(SummernoteModelAdmin):
    list_display = ('name', 'price', 'description', 'image')  
    search_fields = ('name', 'description')


