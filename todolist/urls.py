#from django.contrib import admin
from django.urls import path
from . import views #import the view class cause its from same folder

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.index, name='index')  #calls the function index in the view file
]