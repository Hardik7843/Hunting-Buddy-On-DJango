from django.shortcuts import render , redirect , HttpResponse
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate , login , logout
from django.contrib import messages
from app.process import examine
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        form_username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(username = form_username)
        
        if user.exists():
            messages.add_message(request, messages.WARNING ,message="User Already Exists")
            return redirect('/register/')
        
        user = User.objects.create(username = form_username,email=email , password=password )
        user.first_name = first_name
        user.last_name = last_name

        user.set_password(password)
        user.save()
        messages.add_message(request, messages.INFO ,message="Account Created Successfully")
        return redirect('/login/')
    return render(request , 'register.html')

@login_required(login_url = '/login/')
def show(request):
    if request.method == 'POST':
        data = request.POST
        job = data.get('job_desc')
        output = examine(job)  
        keywords = dict(output)
        return render(request , 'show.html', {'keywords':keywords}) 
    
    return render(request , 'show.html')


def login_page(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        if not User.objects.filter(username = username).exists():
            messages.add_message(request, messages.WARNING ,message="Wrong Username")
            return redirect('/login/')

        user = authenticate(request, username=username, password=password)
        
        if not user:
            messages.add_message(request, messages.ERROR ,message="Wrong Password")
            return redirect('/login/')
        
        else:
            login(request , user)
            return redirect(f'/user/show/{username}')
        
    return render(request , "login.html")

def logout_page(request):
    logout(request)
    return redirect('/login/')
    