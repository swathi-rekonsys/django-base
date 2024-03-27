from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')

def SingupPage(request):
    if request.method == 'POST':
        fullname = request.POST.get('Full Name')
        email = request.POST.get('Email adress')
        username = request.POST.get('Username')  # Corrected typo
        password = request.POST.get('Password')
        confirm_password = request.POST.get('ConfirmPassword')  # Corrected typo

        if password != confirm_password:
            return HttpResponse('Your password and confirm password do not match!!')
        else:
            my_user = User.objects.create_user(username=username, email=email, password=password, full_name=fullname)  # Corrected order of arguments
            my_user.save()
            return redirect('login')

    return render(request, 'singup.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')  # Corrected typo
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Username or password is incorrect!!!')

    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')
