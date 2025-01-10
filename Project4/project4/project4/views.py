from django.http import HttpResponse
from django.shortcuts import render 

def index(request):
    return render(request,'layout.html')

# def register(request):
#     return render(request,'registration/register.html')

# def login(request):
#     return render(request,'registration/login.html')

# def logout(request):
#     return render(request,'registration/logout.html')

