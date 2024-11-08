from django.http import HttpResponse

def home(request):
    return HttpResponse("This Home things")

def about(request):
    return HttpResponse("This is about thingyy")

def contact(request):
   return HttpResponse("Contact us thingyy")