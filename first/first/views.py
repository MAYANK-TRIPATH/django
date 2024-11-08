from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("This Home things")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("This is about thingyy")

def contact(request):
   return HttpResponse("Contact us thingyy")