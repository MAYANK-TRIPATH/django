from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #return HttpResponse("This Home things")
    return render(request, 'website/home.html')

def about(request):
    # return HttpResponse("This is about thingyy")
    return render(request, 'website/about.html')

def contact(request):
#    return HttpResponse("Contact us thingyy")
    return render(request, 'website/contact.html')