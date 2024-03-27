from django.shortcuts import render
from login_credentialsapp.forms import SwatiForm

# Create your views here.
def index(request):
    form=SwatiForm()
    if request.method=='POST':
        form =SwatiForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'index.html',{'form':form})