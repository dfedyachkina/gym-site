from django.urls import path
from . import views

urlpatterns = [
    path('create-appointment/', views.create_appointment, name='create_appointment'),
]