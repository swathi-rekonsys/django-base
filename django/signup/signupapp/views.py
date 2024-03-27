from django.shortcuts import render,redirect

from .forms import signupform  

def signup(request):
    if request.method=='POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('login')  
    else:
        form = signupform()  
    return render(request,'signup.html', {'form': form})

def login(request):
    return render(request, 'login.html')