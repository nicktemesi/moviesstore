from django.shortcuts import render
from flask import request_tearing_down

# Create your views here.

def index(request):
    return render(request, index.html)

def about(request):
    return render(request, 'home/about.html')
