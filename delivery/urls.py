from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'delivery'
urlpatterns = [
    path('create/', views.task_create, name='create'),
]
