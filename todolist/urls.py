#from django.contrib import admin
from django.urls import path
from . import views #import the view class cause its from same folder

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.index, name='index'),  #calls the function index in the view file
    path('add/', views.addTodoItems, name='add_todo'),
    path('completed/<todo_id>', views.completedItem, name='completed'),
    path('delete_completed/<todo_id>', views.DeleteCompletedItem, name='delete_completed'),
    path('delete_all/', views.DeleteCompletedAll, name='delete_all')
]