from django.urls import path
from .views import index, inicio

urlpatterns = [

    path('usuario/', index, name='user'),

    path('cliente/', inicio, name='inicio'),

]