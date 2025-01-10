from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegistrationForm
from .models import curdcls

# Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) 
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request,'registration/register.html',{'form':form})