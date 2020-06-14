from django.urls import path
from . import views

urlpatterns = [
    
    path('index', views.index, name='index'),
    path('add', views.addtodo, name='add'),
    path('complete/<todo_id>', views.complete_todo, name='complete'),
    path('delete/<todo_id>', views.delete_todo, name='delete'),
        path('', views.login, name='login'),
    path('log', views.log, name='log'),

]
