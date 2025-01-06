from django.shortcuts import render
from .landingPageController import *


def landingPage (request):
    return render(request, "landingPages\landingPage.html", context={"availWorlds":getAllAvailWorlds(request.user)})