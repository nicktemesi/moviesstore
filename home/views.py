from tempfile import template
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    template_data = {}
    template_data['title'] = 'Our Home Page'
    return render(request, 'home/index.html', template_data)

def about(request):
    template_data = {}
    template_data['title'] = 'About Us'
    return render(request, 'home/about.html', template_data)
