from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def about_me(request):
    return HttpResponse("This is the About page!")