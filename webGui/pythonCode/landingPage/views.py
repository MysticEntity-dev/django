from django.shortcuts import render


def landingPage (request):
    return render(request, "landingPages\landingPage.html")