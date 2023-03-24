from django.urls import path
from . import views

urlpatterns = [
    path('', views.django_fee, name='django_fees')
]
