#from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def django_course(request):
    coursename = {
        'cname' : 'Django'
    }
    return render(request, 'course/django_course.html', coursename)