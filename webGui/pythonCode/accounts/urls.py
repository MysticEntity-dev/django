from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path
from django.urls import include
from .views import loginPage, newUserPage

urlpatterns = [
    path("login/",  loginPage),
    path("newUser", newUserPage)

]