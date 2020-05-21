from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from accounts.views import login
from editprofile.models import linksave
def home(request):
    return render(request, "homepage.html")

def anyuser(request,username):
    searchuser = username
    try:
        user = User.objects.get(username=searchuser)
        all_item = linksave.objects.filter(currentuser = searchuser)
        return render(request,"linkview.html",{'all_items':all_item,'user':user})
    except:
        return HttpResponse("Does not exist")