from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('list/', views.devices, name='device_list'),
]
