from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# Create your views here.

def login(request):
    return render(request, 'login.html')

def log(request):
    if request.method == 'POST':
        username = request.POST['username']
        if username != '':
            if User.objects.filter(username=username).exists():
                print('username taken')
                return redirect('login')
            else:
                user = User.objects.create_user(username=username)
                user.save()
                return redirect('index')

    return redirect('index')