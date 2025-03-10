from django.contrib import admin
from .models import TodoList #import the model

# Register your models here.
admin.site.register(TodoList) #register the model to the admin site
