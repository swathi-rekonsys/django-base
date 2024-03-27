from django.shortcuts import render
from .models import Coffee

def home(request):
    coffees = Coffee.objects.all()
    return render(request, 'home.html', {'coffees': coffees})  # Removed space before 'coffees'
