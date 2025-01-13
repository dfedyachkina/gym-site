from django.urls import path
from . import views

urlpatterns = [
    path('create-appointment/', views.create_appointment, name='create_appointment'),
    path('update-appointment/<int:id>/', views.update_appointment, name='update_appointment'),
    path('delete-appointment/<int:id>/', views.delete_appointment, name='delete_appointment'),
    path('appointment-list/', views.appointment_list, name='appointment_list'),
]