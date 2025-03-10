from urllib import request
from django.shortcuts import redirect, render
from .models import TodoList #import the model
from .forms import TodolistForm

# Create your views here.

#this route the request of the url to the file index
def index(request):

    todo_list = TodoList.objects.order_by('id')

    form = TodolistForm()
    context = {'todo_list': todo_list,'form':form}
    
    return render(request,'todolist/index.html',context)


#Adding items to the database
def addTodoItems(request):
     if request.method == "POST":
        form = TodolistForm(request.POST)

        if form.is_valid():
            new_todolist = TodoList(text=request.POST['text'])
            new_todolist.save()

            return redirect('/')
        
        # If the form is not valid or if it's a GET request, re-render the page with an empty form
        #return render(request, 'index.html', {'form': TodolistForm()})

#Mark to do completed
def completedItem(request,todo_id):
    todo=TodoList.objects.get(pk=todo_id)
    todo.completed=True
    todo.save()

    return redirect('/')


#Delete Item from database completed
def DeleteCompletedItem(request, todo_id):
    TodoList.objects.filter(pk=todo_id, completed=True).delete()
    return redirect('/')
       
#Delete Item from database completed
def DeleteCompletedAll(request):
     TodoList.objects.all().delete()
     return redirect('/')