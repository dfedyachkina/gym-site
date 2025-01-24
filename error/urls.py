from django.conf.urls import handler404
from django.urls import path
from . import views


urlpatterns = [
    path('', views.ustom_404, name='error404'),
]