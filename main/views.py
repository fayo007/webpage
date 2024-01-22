from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from . import models


# front
def index(request):
    context = {}
    return render(request, 'front/index.html',context)


def contact(request):
    context = {}
    if request.method == 'POST':
        models.Form.objects.create(
            name = request.POST['name'],
            email = request.POST['email'],
            text = request.POST['text']
        )
        return redirect('index')
   
    return render(request, 'front/index.html',context)


def dashboard(request):
    context = {}
    return render(request, 'dashboard/index.html',context)


def appeal_list(request):
    appeal = models.Form.objects.all()
    return render(request, 'dashboard/appeal/list.html', {'appeal':appeal})


def appeal_delete(request, id):
    context ={}
    models.Form.objects.get(id=id).delete()
    return redirect('appeal_dashboard',context)


def gallery_list(request):
    images = models.Gallery.objects.all()
    return render(request ,'dashboard/galereya/list.html',{'images':images})



def create_image(request):
    context = {}
    if request.method == 'POST':
        models.Gallery.objects.create(
            image = request.FILES['image']
        )
        return redirect('dashboard')
    
    return render(request ,'dashboard/galereya/create.html',context)

def register_user(request):
    if request.method == 'POST':
        User.objects.create_user(
            username = request.POST['username'],
            password = request.POST['password']
        )
        return redirect('dashboard')
    return render(request, 'dashboard/auth/register.html')


def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'dashboard/auth/login.html')


def log_out(request):
    logout(request)
    return redirect('index')