
from django.urls import path
from .views import UserDataAPIView, CustomAuthToken

app_name = 'tkinter_api'

urlpatterns = [
    path('data', UserDataAPIView.as_view()), #! Ojo, este sólo debería de estar aquí para desarrollo. Eliminar/esconder en producción
    path('custom-token/', CustomAuthToken.as_view()), #? Este es el que devuelve los datos correctos al usuario que se loguea en la desktop app.

]
