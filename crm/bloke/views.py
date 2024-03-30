from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm
from django.contrib.auth.models import auth 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .models import Record

def index(request):
    return render(request, "bloke/index.html")

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    
    context = {"form": form}
    return render(request, "bloke/register.html", context=context)

def login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("index")

    context = {"loginform": form}
    return render(request, "bloke/login.html", context=context)

@login_required(login_url="login")
def dashboard(request):
    my_records = Record.objects.all()
    context = {"records": my_records}
    return render(request, "bloke/dashboard.html", context=context)


def user_logout(request):
    auth.logout(request)
    return redirect("index")