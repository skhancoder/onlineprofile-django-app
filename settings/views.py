from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from editprofile.views import *
from editprofile.models import linksave
from .models import biomodel, appearance

def mysettings(request):
    biouser = request.user
    try:
        bioitem = biomodel.objects.get(currentuser = biouser)
        return render(request,"mysettings.html",{'bioitem':bioitem})
    except:
        print("Error in mysetting")
        
        return render(request,"mysettings.html")

def bioupdate(request):
    loggeduser = request.user
    updatebio = request.POST['bio']

    try:
        biouser = biomodel.objects.get(currentuser=loggeduser)
        biouser.bio = updatebio
        biouser.save()
        return redirect("mysettings")
        
    except:
        print("error in bio update")
        biouser = biomodel(currentuser=loggeduser,bio = updatebio)
        biouser.save()
        return redirect("mysettings")
        
def themechange(request):
    loggeduser = request.user
    themecontent = request.POST['theme2']
    try:
        usertheme = appearance.objects.get(currentuser = loggeduser)
        usertheme.colortheme = themecontent
        return redirect("mysettings")
    except:
        usertheme = appearance(currentuser = loggeduser, colortheme=themecontent)
        usertheme.save()
        return redirect("mysettings")
    
    
