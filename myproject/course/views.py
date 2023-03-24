from django.http import HttpResponse

# Create your views here.
def learn_django(request):
    return HttpResponse("Django Course")
