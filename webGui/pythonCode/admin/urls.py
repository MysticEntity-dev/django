from django.urls import path
from django.contrib import admin
from .views import *

urlpatterns = [
    path('django/', admin.site.urls),
    path('', adminMain),
    path('worlds', adminWorlds),

]