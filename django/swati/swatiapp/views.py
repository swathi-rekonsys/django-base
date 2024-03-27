from django.shortcuts import render
from swatiapp.forms import SwathiForm

# Create your views here.
def index(request):
    form=SwathiForm()
    if request.method=='POST':
        form =SwathiForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'index.html',{'form':form})