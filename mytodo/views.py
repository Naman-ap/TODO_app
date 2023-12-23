from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import todo
from mytodo.forms import todoform
# Create your views here.
def home(request):
    template_name="home.html"
    todo_list=todo.objects.all() #return Query set
    form=todoform()
    print(todo_list)
    context={
        "name":"TODO",
        "todo_list":todo_list,
        "form":form  }

    return render(request,template_name,context)
def add(request):
    if request.method=="POST":
        form=todoform(request.POST)
        if form.is_valid():
            todo_text=form.cleaned_data.get("todo_text")
            todo.objects.create(todo_text=todo_text)
    return redirect("home")
def delete(request,todo_id):
    if request.method=="POST":
        todo_obj=todo.objects.get(pk=todo_id)
        todo_obj.delete()
    return redirect("home")

def edit(request,todo_id):
    todo_obj=todo.objects.get(pk=todo_id)
    if request.method=="POST":
        form=todoform(request.POST)
        if form.is_valid():
            todo_obj.todo_text=form.cleaned_data.get("todo_text")
            todo_obj.save()
            return redirect("home")
    template_name="edit.html"
    
  
    form=todoform(initial={"todo_text":todo_obj.todo_text})
    context={
        "form":form,
        "id":todo_obj
    }
    return render(request,template_name,context)
