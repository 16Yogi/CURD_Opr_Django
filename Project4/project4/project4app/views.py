from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def registration(request):
    if request.method=="POST":
        data = request.POST
        username = data.get('username')
        useremail = data.get('email')
        photo = request.FILES.get('photo')
        password1 = data.get('password1')
        password2 = data.get('password2')
        
        # print(username)
        # print(useremail)
        # print(photo)
        # print(password1)

        if not all([username, useremail, password1, password2]):
            return HttpResponse('All fields are required.')

        if password1 != password2:
            return HttpResponse('Password not Matched')            
        else:
            RegistrationForm.objects.create(
                username = username,
                email = useremail,
                photo = photo,
                password = password1, 
            )
            return redirect('/project4/login/')
    return render(request,'registration/register.html')

def user_list(request):
    queryset = RegistrationForm.objects.all()
    context = {"registrations": queryset}
    return render(request,'user_list.html',context)
    
def user_delete(request,id):
    queryset = RegistrationForm.objects.get(id=id)
    queryset.delete()
    return redirect('user_list')

# def update_user(request,id):
#     queryset = RegistrationFor.object.get(id=id) 
#     context = {"registrations":queryset}
#     return render(request,'registration/update_user.html',context)

def update_user(request, id):
    queryset = RegistrationForm.objects.get(id=id)  
    if request.method == "POST":
        data = request.POST
        username = data.get('username')
        photo = request.FILES.get('photo')
        password1 = data.get('password1')
        password2 = data.get('password2')
        if not all([username, password1, password2]):
            return HttpResponse('All fields are required.')
        if password1 != password2:
            return HttpResponse('Passwords do not match.')
        queryset.username = username
        if photo:
            queryset.photo = photo 
        queryset.password = password1  
        queryset.save()  
        return redirect('user_list')  
    context = {"registration": queryset}
    return render(request, 'registration/update_user.html', context)

def login(request):
    return render(request,'registration/login.html')

def logout(request):
    return render(request,'registration/logout.html')