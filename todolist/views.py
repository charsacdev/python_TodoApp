from django.shortcuts import render
from .models import TodoList #import the model

# Create your views here.

#this route the request of the url to the file index
def index(request):

    todo_list = TodoList.objects.order_by('id')

    context = {'todo_list': todo_list}
    return render(request,'todolist/index.html',context)
