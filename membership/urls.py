from . import views
from django.urls import path

urlpatterns = [
    path('', views.membership, name='membership'),
    path('request/<int:membership_id>/', views.request_membership, name='request_membership'),
    path('success/', views.membership_success, name='membership_success'),
]