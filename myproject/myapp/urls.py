from django.urls import path
from . import views
from .views import index

urlpatterns = [
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter'),
]
