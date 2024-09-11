from django.contrib.admin.forms import AdminAuthenticationForm
from django.contrib.auth import authenticate
from django.shortcuts import render
from django.contrib.auth.models import User


def loginPage(request):
    if request.method == "Post":
        user = authenticate(username=request.post["username"], password=request.post["password"])
    return render(request, "accounts/login.html", context={"form": AdminAuthenticationForm})

def newUserPage(request):
    user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")
    return render(request, "accounts/newUser.html")