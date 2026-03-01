from django.contrib.admin.forms import AdminAuthenticationForm
from django.contrib.auth import aauthenticate, alogin, alogout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


async def loginPage(request):
    if request.method == "POST":
        user = await aauthenticate(username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            await alogin(request, user)
            return redirect("/")
    return render(request, "accounts/login.html", context={"form": AdminAuthenticationForm})


async def newUserPage(request):
    if request.method == "POST":
        user = User.objects.create_user(request.POST["username"], "", request.POST["password1"])
        if user is not None:
            await alogin(request, user)
            return redirect("/")
    return render(request, "accounts/newUser.html", context={"form" : UserCreationForm})


async def logout_view(request):
    await alogout(request)
    return redirect("/")