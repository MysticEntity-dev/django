from django.contrib.admin.forms import AdminAuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def loginPage(request):
    if request.method == "POST":
        user = authenticate(username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            return redirect("/")
    return render(request, "accounts/login.html", context={"form": AdminAuthenticationForm})

def newUserPage(request):
    if request.method == "POST":
        user = User.objects.create_user(request.POST["username"], "", request.POST["password1"])
        if user is not None:
            login(request, user)
            return redirect("/")
    return render(request, "accounts/newUser.html", context={"form" : UserCreationForm})