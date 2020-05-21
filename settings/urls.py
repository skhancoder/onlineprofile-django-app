from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('mysettings',mysettings,name='mysettings'),
    path('bioupdate',bioupdate,name="bioupdate"),
    path('themechange',themechange,name="themechange")
]