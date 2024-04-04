from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm,  CreateRecordForm, UpdateRecordForm
from django.contrib.auth.models import auth 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from .models import Record
from django.contrib import messages

def index(request):
    return render(request, "bloke/index.html")

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
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
                messages.success(request, "Login successful")
                return redirect("dashboard")

    context = {"loginform": form}
    return render(request, "bloke/login.html", context=context)

@login_required(login_url="login")
def dashboard(request):
    my_records = Record.objects.all()
    context = {"records": my_records}
    return render(request, "bloke/dashboard.html", context=context)

@login_required(login_url="login")
def create_record(request):
    form = CreateRecordForm()
    if request.method == "POST":
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Record created successfully")
            return redirect("dashboard")
    context = {"form": form}
    return render(request, "bloke/create_record.html", context=context)

@login_required(login_url="login")
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)
    if request.method == "POST":
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully")
            return redirect("dashboard")
    context = {"form": form}
    return render(request, "bloke/update_record.html", context=context)

# read or view single record
@login_required(login_url="login")
def single_record(request, pk):
    all_records = Record.objects.get(id=pk)
    context = {"record": all_records}
    return render(request, "bloke/view_record.html", context=context)

@login_required(login_url="login")
def delete_record(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    messages.success(request, "Record deleted successfully")
    return redirect("dashboard")



def user_logout(request):
    auth.logout(request)
    messages.success(request, "Logout successful")
    return redirect("index")