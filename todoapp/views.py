from django.shortcuts import render,redirect
from .models import todo
from .forms import todoform
from django.views.decorators.http import require_POST

from django.contrib.auth.models import User, auth

username = ""

# Create your views here.

def index(request):
    todo_list = todo.objects.filter(author= username)

    form = todoform()
    
    context = {'todo_list' : todo_list, 'form' : form}
    return render(request, 'index.html', context)

@require_POST
def addtodo(request):

    if request.method == 'POST':
        form = todoform(request.POST)
        if form.is_valid():

            new_todo = todo(author = User.objects.get(username= username), text = request.POST['text'])
            new_todo.save()
            print(username)

    return redirect('index')


def complete_todo(request,todo_id):
    x = todo.objects.get(pk=todo_id)
    x.complete = True
    x.save()

    return redirect('index')

def delete_todo(request,todo_id):
    y = todo.objects.get(pk=todo_id)
    y.delete()
    return redirect('index')



def login(request):
    return render(request, 'login.html')

def log(request):
    if request.method == 'POST':
        global username
        username = request.POST['username']
        if username != '':
            if User.objects.filter(username=username).exists():
                return redirect('index')
            else:
                user = User.objects.create_user(username=username)
                user.save()
                return redirect('index')

    return redirect('index')
