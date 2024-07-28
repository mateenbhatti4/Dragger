from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from user.models import Payments
from django.shortcuts import redirect



def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username', 'default')
        password = request.POST.get('password', 'default')
        print(username)
        print(password)
        if username != "" and password != "":
            try:
                user=User.objects.filter(username=username,is_superuser=True).first().id
            except:
                return render(request, "admin/login.html")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return render(request, "admin/dashboard.html")
            else:
                return render(request, "admin/login.html")

        return render(request, "admin/login.html")
    return render(request, "admin/login.html")


def dashboard(request):
    users = User.objects.filter(is_superuser=False,is_active=True).count()
    payments = Payments.objects.filter().count()
    return render(request, 'admin/dashboard.html',context={'users':users,'payments':payments})


def Users(request):
    users = User.objects.filter(is_superuser=False,is_active=True)
    return render(request, 'admin/all_users.html',context={'users':users})


def Projects(request):
    return render(request, 'admin/all_projects.html')

def Profile(request):
    return render(request, 'admin/profile_settings.html')

def Payment(request):
    users=User.objects.filter(is_superuser=False,is_active=True)
    payments = Payments.objects.filter()
    return render(request, 'admin/all_payments.html',context={'payments':payments,'users':users})

def gallery(request):
    return render(request, 'admin/gallery.html')

def Logout(request):
    logout(request)
    return redirect('admin')
