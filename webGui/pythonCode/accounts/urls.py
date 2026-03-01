from django.urls import path
from .views import loginPage, newUserPage, logout_view

urlpatterns = [
    path("login/",  loginPage),
    path("logout/",  logout_view),
    path("newUser", newUserPage)

]