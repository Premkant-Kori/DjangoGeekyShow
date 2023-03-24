#from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def django_fee(request):
    fees = {
        'fees' : 31500
    }
    return render(request, 'fees/django_fees.html', fees)