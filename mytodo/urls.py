#from django.contrib import admin
from django.urls import path,include
from  mytodo.views import home,add,delete,edit
urlpatterns = [
  path("",home,name="home"),
  path("add/",add,name="add"),
  path("delete/<int:todo_id>",delete,name="delete"),
  path("edit/<int:todo_id>",edit,name="edit")
]
