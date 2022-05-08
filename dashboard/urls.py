from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginpage, name='login'),
    path('encender', views.encender, name='encender'),
    path('apagar', views.apagar, name='apagar'),
    path('encendido', views.encendido, name='encendido'),
    path('apagado', views.apagado, name='apagado'),
]