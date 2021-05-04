from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['con_pass']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid user and password")
            print("USER NOT FOUND")
            return redirect("login")
        return user
    else:
        return render(request,'login.html')

def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        crt_pass = request.POST['crt_pass']
        con_pass = request.POST['con_pass']

        if crt_pass == con_pass:
            if User.objects.filter(username=username).exists():
                messages.info(request,"User already exist")
                print("Username taken")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exist")
                print("Email taken")
                return redirect("register")
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username, password=crt_pass, email=email)
                user.save()
                print("USER IS CREATE")
        else:
            messages.info(request,"Password not match")
            print("Password not matching")
            return redirect("register")
        return redirect("/")
    else:
        return render(request,'register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

def check_user(request):
    a = login(request)
    return a
