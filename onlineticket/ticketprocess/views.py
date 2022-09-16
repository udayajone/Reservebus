
from django.shortcuts import render,redirect
from ticketprocess.models import bus
from ticketprocess.forms import busform
from django.contrib import admin
# Create your views here.
def display_view(request):
    ticket=bus.objects.all()
    return render(request,"ticketprocess/display.html",{"ticket":ticket})

def add_view(request):
    form=busform()
    if request.method =='POST':
        form=busform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/display')

    return render(request,'ticketprocess/create.html',{'form':form})
