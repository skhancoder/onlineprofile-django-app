from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from editprofile.views import *
from editprofile.models import linksave

# Create your views here.
def linkprofile(request):
    all_item = linksave.objects.all()
    return render(request,"linkview.html",{'all_items':all_item})

