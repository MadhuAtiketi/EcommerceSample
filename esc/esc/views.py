from django.http import HttpResponse

def Index(request):
    return HttpResponse("In the actual Home page")