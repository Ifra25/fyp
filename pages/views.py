from django.shortcuts import render

def index(request):
    return render(request, '../templates/index.html')

def home(request):
    return render(request, '../templates/home.html')
