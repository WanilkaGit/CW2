from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from random import randint

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("room-list")
    else:
        form = CustomUserCreationForm
        return render(request, "auth_system/register_form.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("room-list")
            else:
                messages.error(request, message="Incorrect pass or username")
    else:
        form = AuthenticationForm()
        context = {
            "form": form
        }
        return render(request, "auth_system/login_form.html", context)

def logout_view(request):
    logout(request)
    rand_num = randint(1, 3)
    if rand_num == 1:
        return redirect("room-list")
    elif rand_num == 2:
        return redirect("login")
    else:
        return redirect("register")