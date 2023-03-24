from django.urls import path
from . import views

urlpatterns = [
    path('', views.django_course, name='django_course'),
]