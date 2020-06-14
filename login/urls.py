from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('log', views.log, name='log'),
]


