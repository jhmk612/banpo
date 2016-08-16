from django.shortcuts import render, redirect
from black.models import People

# Create your views here.

def home(request):

    return render(request, 'index/home.html')