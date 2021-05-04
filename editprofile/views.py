from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import linksave
from .forms import linksavelist
# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect('/')

def publish(request):
    links = linksave
    if request.method == "POST":
        form = linksavelist(request.POST or None)
        if form.is_valid(): 
            form.save()
            print("Data saved")
            return redirect("profile")
        return redirect("profile")
    else:
        all_items = linksave.objects.all()
        return render(request,"profile.html",{'all_items':all_items})

def deletelink(request,id):
    item = linksave.objects.get(pk=id)
    item.delete()
    return redirect("profile")

def editlink(request,id):
    item = linksave.objects.get(pk=id)
    form = linksavelist(request.POST or None, instance=item)
    form.save()
    return redirect("profile")

def profile(request):
    if request.user.is_authenticated:
        all_items = linksave.objects.filter(currentuser = request.user)
        return render(request,"profile.html",{'all_items':all_items})
    else:
        return redirect("accounts/login")
