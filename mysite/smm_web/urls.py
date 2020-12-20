from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('producto/', views.product, name='producto'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('subscripciones/', views.subscripciones, name='subscripciones'),
    path('productos/', views.productos, name='productos'),
    path('mi_perfil/', views.mi_perfil, name='mi_perfil'),
    path('estadisticas/', views.estadisticas, name='estadisticas'),
    path('dispositivos/', views.dispositivos, name='dispositivos'),
]