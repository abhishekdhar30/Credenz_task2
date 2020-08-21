from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from .models import Profile
from django.contrib import messages

def register(request) :
    if request.method == "POST" :
        uname = request.POST.get ('user')
        pas = request.POST.get ('pass')
        pas1 = request.POST.get ('pass1')
        fname = request.POST.get ('fname')
        lname = request.POST.get ('lname')
        eid = request.POST.get ('email')
        no = request.POST.get ('num')

        if pas == pas1 :

            if User.objects.filter (username=uname).exists ( ) :
                messages.warning (request, f'User already exists!!!')
                return render (request, "app/register.html")

            else :
                user = User.objects.create_user(username=uname, email=eid, password=pas, first_name=fname,
                                                 last_name=lname)
                user.save ( )
                profile = Profile( )
                profile.user = user
                profile.num = no
                profile.save ( )
                login (request, user)
                return render (request, "app/home.html", {"uname" : uname})


        else :
            messages.warning (request, f'Passwords do not match!!!')
            return render (request, "app/register.html")

    return render (request, "app/register.html")


def dev(request) :
    if request.method == "POST" :
        uname = request.POST.get ('user')
        pas = request.POST.get ('pass')
        user = authenticate (username=uname, password=pas)
        if user is not None :
                login (request, user)
                return render (request, "app/home.html",{"uname" : uname} )


        else :
            messages.warning(request,f'Invalid Credentials!!!')
            return render (request, "app/dev.html")

    return render (request, "app/dev.html")


def push(request) :
    logout (request)
    messages.success(request,f'Logged out Successfully!!! Login/Signup Again')
    return redirect('/')