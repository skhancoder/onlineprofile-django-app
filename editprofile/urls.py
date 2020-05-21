from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('publish',publish,name="publish"),
    path('profile',profile,name="profile"),
    path('deletelink/<id>',deletelink,name="deletelink"), 
    path('editlink/<id>',editlink,name="editlink"),
    path('logout',logout,name='logout')   
]