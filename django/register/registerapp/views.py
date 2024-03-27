from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add your custom fields here, if any

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


# View function for homepage
def homepage(request):
    return render(request, 'index.html')

# View function for user registration
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_login')
    else:
        form = CreateUserForm()
    return render(request, 'register.html', {'form': form})

# View function for user login
def my_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'my_login.html', {'form': form})

# View function for dashboard
def dashboard(request):
    return render(request, 'dashboard.html')

