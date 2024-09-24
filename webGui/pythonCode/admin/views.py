from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required
def adminMain (request):
    return render(request, "adminSites\\adminMainPage.html")


def adminWorlds(request):
    return render(request, "adminSites\\worldsAdmin.html")
