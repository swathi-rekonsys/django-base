from django.shortcuts import render
from Employeeapp.forms import EmployeeForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EmployeeForm()
    return render(request, 'index.html', {'form':form})