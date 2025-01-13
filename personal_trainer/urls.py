from django.urls import path
from . import views

urlpatterns = [
    path('create-appointment/', views.create_appointment, name='create_appointment'),
    path('appointment-list/', views.appointment_list, name='appointment_list'),
]